import os, sys, json
from pathlib import Path

# Ensure project root is importable when run from tools/
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.engine_adapter import run_engine, EngineError, MSG_ASSETS_MISSING, MSG_ENGINE_MISSING, MSG_TIMEOUT, MSG_FAILED

def _ensure_synthetic_wav(path: Path):
    try:
        import wave, struct, math
        sr = 16000
        dur = 2.0
        n = int(sr * dur)
        data = []
        # low baseline, then 200ms spike for prosody
        for i in range(n):
            t = i / sr
            v = 0.02 * math.sin(2 * math.pi * 220 * t)
            if int(0.9 * sr) <= i < int(1.1 * sr):
                v = 0.7
            data.append(int(max(-1.0, min(1.0, v)) * 32767))
        path.parent.mkdir(parents=True, exist_ok=True)
        with wave.open(str(path), 'wb') as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(sr)
            frames = b''.join(struct.pack('<h', x) for x in data)
            w.writeframes(frames)
    except Exception:
        pass

def main():
    # ENV/Defaults
    models = Path(os.environ.get("CT2_MODELS", "./models/ct2"))
    bundle = Path(os.environ.get("BUNDLES", "./bundles/SerapiCore_1.0.yaml"))
    audio = Path("tests/data/prosody_smoke.wav")
    # Generate a deterministic synthetic file to guarantee prosody events
    _ensure_synthetic_wav(audio)

    try:
        res = run_engine(str(audio), str(models), str(bundle), fast=True, timeout_s=8)
    except EngineError as e:
        print(str(e), file=sys.stderr)
        sys.exit(e.code)
    except Exception:
        print(MSG_FAILED, file=sys.stderr)
        sys.exit(21)

    out = Path("out"); out.mkdir(exist_ok=True)
    # CLI/API erwarten Feldname "input"; adapter liefert "input_path"
    emit = {"session": res.get("session"), "input": Path(res.get("input_path", "")).name, "events": res.get("events", [])}
    (out / "session_001.json").write_text(json.dumps(emit, indent=2, ensure_ascii=False))
    print("SMOKE:OK")

if __name__ == "__main__":
    main()
