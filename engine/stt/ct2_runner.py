from __future__ import annotations

import os
import json
import wave
import struct
from pathlib import Path
from typing import List, Dict, Any

from tools.engine_adapter import EngineError


def _ensure_wav_16k_mono(input_path: Path) -> List[float]:
    """Convert any WAV to 16kHz mono float samples."""
    try:
        with wave.open(str(input_path), "rb") as w:
            sr = w.getframerate()
            ch = w.getnchannels()
            n = w.getnframes()
            raw = w.readframes(n)
            sw = w.getsampwidth()
    except Exception:
        return []
    
    # Parse samples based on bit depth
    if sw == 1:
        samples = [((b - 128) / 128.0) for b in raw]
    elif sw == 2:
        ints = struct.unpack("<" + "h" * (len(raw) // 2), raw)
        samples = [x / 32768.0 for x in ints]
    elif sw == 4:
        try:
            ints = struct.unpack("<" + "i" * (len(raw) // 4), raw)
            samples = [x / 2147483648.0 for x in ints]
        except Exception:
            try:
                floats = struct.unpack("<" + "f" * (len(raw) // 4), raw)
                samples = [max(-1.0, min(1.0, float(x))) for x in floats]
            except Exception:
                return []
    else:
        return []
    
    # Stereo to mono
    if ch == 2:
        samples = [(samples[i] + samples[i + 1]) * 0.5 for i in range(0, len(samples) - 1, 2)]
    
    # Resample to 16kHz if needed
    if sr != 16000:
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
    
    return samples


def _mock_ct2_transcribe(samples: List[float]) -> List[Dict[str, Any]]:
    """Mock CT2 transcription - replace with real faster-whisper when available."""
    if not samples:
        return []
    
    # Create mock segments based on audio length
    duration = len(samples) / 16000.0
    segments = []
    
    if duration < 1.0:
        segments.append({
            "start": 0.0,
            "end": duration,
            "text": "Hello world"
        })
    elif duration < 3.0:
        segments.extend([
            {"start": 0.0, "end": 1.5, "text": "Hello"},
            {"start": 1.5, "end": duration, "text": "world"}
        ])
    else:
        # Longer audio gets more segments
        seg_count = min(5, int(duration / 2))
        seg_duration = duration / seg_count
        for i in range(seg_count):
            start = i * seg_duration
            end = min((i + 1) * seg_duration, duration)
            segments.append({
                "start": start,
                "end": end,
                "text": f"Segment {i + 1}"
            })
    
    return segments


def run_stt(input_path: Path, models_path: str = "./models/ct2") -> List[Dict[str, Any]]:
    """Run STT on input WAV, return segments with start/end/text."""
    models_dir = Path(models_path)
    
    # Check if CT2 models exist
    if not models_dir.exists() or not any(models_dir.iterdir()):
        raise EngineError("Assets fehlen (models/ct2 oder Bundle).", code=12)
    
    # Convert to 16kHz mono
    samples = _ensure_wav_16k_mono(input_path)
    if not samples:
        raise EngineError("Verarbeitung fehlgeschlagen.", code=12)
    
    try:
        # TODO: Replace with real faster-whisper/CT2 when models are available
        # from faster_whisper import WhisperModel
        # model = WhisperModel(str(models_dir), device="cpu")
        # segments, info = model.transcribe(audio=samples, beam_size=5)
        
        segments = _mock_ct2_transcribe(samples)
        
        # Write segments to expected JSON file
        segments_file = input_path.parent / f"{input_path.stem}.segments.json"
        with segments_file.open("w", encoding="utf-8") as f:
            json.dump({"segments": segments}, f, ensure_ascii=False, indent=2)
        
        return segments
        
    except Exception:
        raise EngineError("Verarbeitung fehlgeschlagen.", code=12)


def transcribe(input_path: str, models_path: str = "./models/ct2") -> Dict[str, Any]:
    """
    Lightweight transcribe API returning {"text": str, "segments": [{start,end,text}]}.
    Uses run_stt() to ensure 16kHz mono and to produce a sidecar segments JSON.
    """
    path = Path(input_path)
    segments = run_stt(path, models_path=models_path)
    # Stitch text best-effort
    text = " ".join((s.get("text") or "").strip() for s in segments if isinstance(s, dict)).strip()
    return {"text": text, "segments": segments}
