#!/usr/bin/env bash
set -euo pipefail
echo "[PRE] System-Preflight"

# 1) Python 3.11
if ! command -v python3.11 >/dev/null; then
  echo "[ERR] Python 3.11 nicht gefunden." ; exit 11
fi

# 2) ffmpeg
if ! command -v ffmpeg >/dev/null; then
  echo "[ERR] ffmpeg nicht gefunden." ; exit 13
fi

# 3) Port frei?
python3.11 - <<'PY'
import socket, sys
def free(port):
    s=socket.socket()
    try:
        s.bind(("127.0.0.1", port)); s.close(); return True
    except OSError:
        return False
ok = all(free(p) for p in [8765])
print("[PRE] Port-Check 8765:", "frei" if ok else "belegt")
sys.exit(0 if ok else 14)
PY

# 4) Ordner vorhanden?
for d in models/ct2 bundles; do
  if [ ! -d "$d" ]; then echo "[ERR] Ordner fehlt: $d" ; exit 12; fi
done

echo "[PRE] OK"
