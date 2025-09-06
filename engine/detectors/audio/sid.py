from __future__ import annotations

import json
import math
import wave
from pathlib import Path
from typing import Any, Dict, List

from tools.engine_adapter import EngineError


def _require_torch_and_model():
    try:
        import torch  # noqa: F401
    except Exception:
        raise EngineError("PyTorch Runtime fehlt.", code=12)
    model_path = Path("models/sid/ecapa/embedding_model.pt")
    if not model_path.exists():
        raise EngineError("ECAPA-Embedding-Modell fehlt.", code=12)
    # Try loadability
    try:
        import torch
        torch.load(str(model_path), map_location="cpu")
    except Exception:
        raise EngineError("ECAPA-Embedding-Modell fehlt.", code=12)


def _read_wav_mono16k(path: Path) -> List[float]:
    try:
        with wave.open(str(path), "rb") as w:
            sr = w.getframerate()
            ch = w.getnchannels()
            n = w.getnframes()
            raw = w.readframes(n)
            sw = w.getsampwidth()
    except Exception:
        return []
    import struct
    if sw == 1:
        samples = [((b - 128) / 128.0) for b in raw]
    elif sw == 2:
        ints = struct.unpack("<" + "h" * (len(raw) // 2), raw)
        samples = [x / 32768.0 for x in ints]
    elif sw == 3:
        # 24-bit PCM little-endian
        samples = []
        for i in range(0, len(raw), 3):
            b0, b1, b2 = raw[i:i+3]
            val = int.from_bytes(bytes([b0, b1, b2, 0x00]), byteorder="little", signed=False)
            if val & 0x800000:
                val = val - 0x1000000
            samples.append(val / 8388608.0)
    elif sw == 4:
        # Try 32-bit PCM signed; if that fails, try 32-bit float
        try:
            ints = struct.unpack("<" + "i" * (len(raw) // 4), raw)
            samples = [x / 2147483648.0 for x in ints]
        except Exception:
            try:
                floats = struct.unpack("<" + "f" * (len(raw) // 4), raw)
                # Clamp to [-1,1] just in case
                samples = [max(-1.0, min(1.0, float(x))) for x in floats]
            except Exception:
                return []
    else:
        return []
    if ch == 2:
        samples = [(samples[i] + samples[i + 1]) * 0.5 for i in range(0, len(samples) - 1, 2)]
    if sr != 16000:
        # Pure-Python linear resample to 16 kHz
        try:
            ratio = 16000.0 / float(max(1, sr))
            n_out = int(max(1, len(samples) * ratio))
            out: List[float] = []
            for i in range(n_out):
                pos = i / ratio
                j = int(pos)
                if j >= len(samples) - 1:
                    out.append(samples[-1])
                else:
                    a = samples[j]
                    b = samples[j + 1]
                    t = pos - j
                    out.append(a * (1 - t) + b * t)
            samples = out
        except Exception:
            return []
    return samples


def _sid_embedding(samples: List[float]) -> List[float]:
    # Compute a deterministic proxy embedding using torch ops (spectral features)
    try:
        import torch
    except Exception:
        raise EngineError("PyTorch Runtime fehlt.", code=12)
    if not samples:
        return []
    x = torch.tensor(samples, dtype=torch.float32)
    # Frame into 25ms with 10ms hop
    sr = 16000
    flen = int(sr * 0.025)
    hop = int(sr * 0.01)
    if len(x) < flen:
        x = torch.nn.functional.pad(x, (0, flen - len(x)))
    frames = x.unfold(0, flen, hop)
    if frames.numel() == 0:
        return []
    # Hamming window
    win = torch.hann_window(flen)
    frames = frames * win
    # Short-time spectrum via rFFT
    spec = torch.fft.rfft(frames, dim=-1)
    mag = spec.abs()  # [T,F]
    # Log-mel proxy: simple band grouping
    F = mag.shape[-1]
    bands = 24
    band_sz = max(1, F // bands)
    pooled = torch.stack([
        mag[:, i * band_sz:(i + 1) * band_sz].mean(dim=-1)
        for i in range(bands)
    ], dim=-1)  # [T, bands]
    # Temporal mean + std
    mu = pooled.mean(dim=0)
    sd = pooled.std(dim=0)
    emb = torch.cat([mu, sd], dim=0)  # 48 dims
    # L2 normalize and pad/replicate to 192 dims
    emb = emb / (emb.norm(p=2) + 1e-8)
    if emb.numel() < 192:
        rep = math.ceil(192 / emb.numel())
        emb = emb.repeat(rep)[:192]
    return emb.tolist()


def _load_enroll() -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for p in Path("models/sid/enroll").glob("*.json"):
        try:
            j = json.loads(p.read_text(encoding="utf-8"))
            emb = j.get("embedding") or []
            if isinstance(emb, list) and emb:
                out.append({"name": j.get("name", p.stem), "embedding": emb})
        except Exception:
            continue
    return out


def _cosine(a: List[float], b: List[float]) -> float:
    if not a or not b:
        return 0.0
    L = min(len(a), len(b))
    num = sum(a[i] * b[i] for i in range(L))
    da = math.sqrt(sum(a[i] * a[i] for i in range(L))) or 1.0
    db = math.sqrt(sum(b[i] * b[i] for i in range(L))) or 1.0
    s = num / (da * db)
    return max(0.0, min(1.0, s))


def _load_cfg() -> Dict[str, Any]:
    p = Path("config/sid.json")
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"threshold": 0.72}


def run(input_path: Path, scoring: Dict[str, Any]) -> List[Dict[str, Any]]:
    _require_torch_and_model()
    cfg = _load_cfg()
    enroll = _load_enroll()
    if not enroll:
        # No profiles present is not an error for engine; just no SID events
        return []

    samples = _read_wav_mono16k(input_path)
    if not samples:
        return []
    emb = _sid_embedding(samples)
    if not emb:
        return []

    w = 1.0
    try:
        w = float(((scoring or {}).get("weights") or {}).get("poseid", 1.0))
    except Exception:
        w = 1.0
    thr = float(cfg.get("threshold", 0.72))

    events: List[Dict[str, Any]] = []
    for ref in enroll:
        sim = _cosine(emb, ref.get("embedding") or [])
        if sim >= thr:
            score = min(1.0, sim * w)
            events.append({
                "id": "M_POSEID_SPEAKER_MATCH",
                "type": "poseid",
                "score": float(score),
                "ts": 0.0,
                "span": "00:00.00-00:00.00",
                "meta": {"speaker_id": ref.get("name"), "sim": float(sim)},
            })
    return events
