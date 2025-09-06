import sys
import json
from datetime import datetime
from pathlib import Path

# Ensure project root on path when run from tools/
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.detectors.audio.sid import _require_torch_and_model, _read_wav_mono16k, _sid_embedding


def fail(msg: str, code: int = 12):
    print(msg, file=sys.stderr)
    sys.exit(code)


def main():
    # Minimal checks
    try:
        _require_torch_and_model()
    except Exception as e:
        fail(str(e), 12)

    incoming = Path("models/sid/enroll/incoming")
    out_dir = Path("models/sid/enroll")
    out_dir.mkdir(parents=True, exist_ok=True)

    wavs = sorted(incoming.glob("*.wav"))
    if not wavs:
        # Nothing to do is OK
        sys.exit(0)

    for wav in wavs:
        try:
            samples = _read_wav_mono16k(wav)
            if not samples:
                # keep the WAV for inspection
                continue
            emb = _sid_embedding(samples)
            if not emb:
                # keep the WAV for inspection
                continue
            name = wav.stem
            payload = {
                "name": name,
                "embedding": emb,
                "meta": {"sr": 16000, "created": datetime.utcnow().isoformat() + "Z"},
            }
            (out_dir / f"{name}.json").write_text(json.dumps(payload), encoding="utf-8")
            # delete only after successful JSON write
            wav.unlink(missing_ok=True)
        except Exception:
            fail("Verarbeitung fehlgeschlagen.", 20)


if __name__ == "__main__":
    main()
