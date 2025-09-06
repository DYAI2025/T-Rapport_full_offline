#!/usr/bin/env python3
import json
import re
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:
    print("Registry-Update fehlgeschlagen.")
    raise


def ensure(det_map, det_id, module, file_path):
    if det_id not in det_map:
        det_map[det_id] = {
            "id": det_id,
            "module": module,
            "file_path": file_path,
            "fires_marker": [],
            "last_updated": "",
            "schema_version": "3.4",
        }


def add_fire(det_map, det_id, marker_id):
    fm = det_map[det_id].setdefault("fires_marker", [])
    if marker_id not in fm:
        fm.append(marker_id)


def main():
    root = Path('.').resolve()
    reg_path = root / 'DETECT_registry.json'
    if reg_path.exists():
        try:
            registry = json.loads(reg_path.read_text(encoding='utf-8'))
        except Exception:
            registry = []
    else:
        registry = []

    det_map = {e.get('id'): e for e in registry if isinstance(e, dict) and e.get('id')}
    ensure(det_map, "DET_TEXT_GENERIC", "engine.detectors.text.generic",  "engine/detectors/text/generic.py")
    ensure(det_map, "DET_PROSODY",      "engine.detectors.audio.prosody", "engine/detectors/audio/prosody.py")
    # Keep module path for poseid detector consistent with current code
    ensure(det_map, "DET_POSEID",       "engine.detectors.audio.sid",     "engine/detectors/audio/sid.py")

    marker_ids = []
    for p in root.rglob("markers/**/*.yaml"):
        try:
            docs = list(yaml.safe_load_all(p.read_text(encoding='utf-8')))
        except Exception:
            continue
        for d in docs:
            if isinstance(d, dict) and 'id' in d and isinstance(d['id'], str):
                marker_ids.append((d['id'].strip(), str(p).lower()))

    for mid, path in marker_ids:
        if mid == "M_POSEID_SPEAKER_MATCH":
            add_fire(det_map, "DET_POSEID", mid)
        elif "/audio/" in path or "prosody" in path:
            add_fire(det_map, "DET_PROSODY", mid)
        else:
            add_fire(det_map, "DET_TEXT_GENERIC", mid)

    out = list(det_map.values())
    reg_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    fired = len({i for e in out for i in (e.get('fires_marker') or [])})
    print("Registry now distinct IDs fired:", fired)


if __name__ == '__main__':
    main()
