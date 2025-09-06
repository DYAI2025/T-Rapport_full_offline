#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

echo "[SMOKE] running tools/smoke_engine.py"
python tools/smoke_engine.py
test -f out/session_001.json || (echo "[SMOKE][ERR] out/session_001.json fehlt"; exit 1)
echo "[SMOKE] OK"

