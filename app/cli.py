import argparse, json, sys
from pathlib import Path

# Ensure project root import path when run from app/
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.engine_adapter import run_engine, EngineError, MSG_ASSETS_MISSING, MSG_ENGINE_MISSING, MSG_TIMEOUT, MSG_FAILED

def main():
    ap = argparse.ArgumentParser(description="TransRapid CLI (Offline-Artefakt-First)")
    ap.add_argument("-i","--input", required=True, help="Input-Datei (wav/mp3/txt)")
    ap.add_argument("-m","--models", default="./models/ct2", help="Pfad zu CT2-Modellen")
    ap.add_argument("-b","--bundle", default="./bundles/SerapiCore_1.0.yaml", help="Bundle-Datei")
    ap.add_argument("-o","--out", default="out/session_001.json", help="Output-JSON")
    args = ap.parse_args()

    models = Path(args.models)
    bundle = Path(args.bundle)
    if not models.exists() or not bundle.exists():
        print("Assets fehlen (models/ct2 oder Bundle).", file=sys.stderr)
        sys.exit(12)

    try:
        res = run_engine(args.input, str(models), str(bundle), fast=True, timeout_s=8)
    except EngineError as e:
        print(str(e), file=sys.stderr)
        sys.exit(e.code)
    except Exception:
        print(MSG_FAILED, file=sys.stderr)
        sys.exit(21)

    Path("out").mkdir(exist_ok=True)
    payload = {"session": res.get("session"), "input": str(args.input), "events": res.get("events", [])}
    Path(args.out).write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    # Exit 0 bei Erfolg, keine weitere Ausgabe notwendig

if __name__ == "__main__":
    main()
