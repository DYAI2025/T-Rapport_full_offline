import sys
import json
from datetime import datetime
from pathlib import Path

from engine.detectors.audio.poseid import _require_runtime_and_encoder, _read_wav_mono16k, _pseudo_embedding

def fail(msg: str, code: int = 12):
    print(msg, file=sys.stderr)
    sys.exit(code)


def main():
    try:
        _require_runtime_and_encoder()
    except Exception as e:
        fail(str(e), 12)

    incoming = Path("models/poseid/enroll/incoming")
    out_dir = Path("models/poseid/enroll")
    out_dir.mkdir(parents=True, exist_ok=True)

    wavs = sorted(incoming.glob("*.wav"))
    if not wavs:
        # Nothing to enroll is OK (no-op)
        sys.exit(0)

    for wav in wavs:
        try:
            samples = _read_wav_mono16k(wav)
            if not samples:
                # Skip incompatible files silently
                wav.unlink(missing_ok=True)
                continue
            emb = _pseudo_embedding(samples)
            name = wav.stem
            out = {
                "name": name,
                "embedding": emb,
                "meta": {"sr": 16000, "created": datetime.utcnow().isoformat() + "Z"},
            }
            (out_dir / f"{name}.json").write_text(json.dumps(out), encoding="utf-8")
            wav.unlink(missing_ok=True)
        except Exception:
            fail("Verarbeitung fehlgeschlagen.", 20)

if __name__ == "__main__":
    main()

