from pathlib import Path
from typing import Any, Dict, List
import re


def _collect_patterns(markers_root: Path) -> List[str]:
    pats: List[str] = []
    # Read only simple 'frame: signal: - ...' lines to avoid YAML dependency
    for p in markers_root.rglob("*.yaml"):
        try:
            txt = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        in_signal = False
        for line in txt.splitlines():
            s = line.strip()
            if s.startswith("frame:"):
                in_signal = False
            if s.startswith("signal:"):
                in_signal = True
                continue
            if in_signal and s.startswith("-"):
                pat = s.lstrip("- ").strip()
                if pat:
                    pats.append(pat.lower())
            # Stop scanning signal block when next top-level key appears
            if in_signal and (re.match(r"^[a-zA-Z_]+:", s) and not s.startswith("-")):
                in_signal = False
    return pats


def _load_transcript(input_path: Path) -> str:
    # Minimal: If a .txt next to audio exists, use it. If input is .txt, use it as transcript.
    if input_path.suffix.lower() == ".txt" and input_path.exists():
        try:
            return input_path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            return ""
    # sidecar
    side = input_path.with_suffix(".txt")
    if side.exists():
        try:
            return side.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            return ""
    return ""


def run(input_path: Path, scoring: Dict[str, Any]) -> List[Dict[str, Any]]:
    # No STT in offline stack; give only text-based hits if transcript is present
    transcript = _load_transcript(input_path).lower()
    if not transcript:
        return []

    pats = _collect_patterns(Path("markers"))
    if not pats:
        return []

    events: List[Dict[str, Any]] = []
    for pat in pats[:256]:  # cap scan
        if pat and pat in transcript:
            events.append({
                "type": "text",
                "score": 0.6,  # minimal base score over default threshold
                "ts": 0.0,
                "meta": {"pattern": pat},
            })
    return events

