from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from tools.engine_adapter import EngineError


def process(input_path: str, models: str, bundle: str, fast: bool = True, timeout_s: int = 10) -> Dict[str, Any]:
    """
    STT-integrated core:
    - Runs CT2/STT to generate transcript + segments (if assets present)
    - Delegates to engine.core.process for detector orchestration (prosody reads sidecar)
    - Returns enriched payload with transcript and segments
    """
    inp = Path(input_path)
    transcript = ""
    segments: List[Dict[str, Any]] = []

    try:
        # Import locally to avoid hard dependency if CT2 assets are missing
        from engine.stt.ct2_runner import transcribe
        # Attempt STT; if CT2 models missing, raises EngineError(12)
        stt = transcribe(str(inp), models_path=models)
        transcript = (stt or {}).get("text", "") or ""
        segments = (stt or {}).get("segments", []) or []
    except EngineError:
        # Propagate asset-related errors to the caller
        raise
    except Exception:
        # Non-fatal: continue without segments
        transcript = ""
        segments = []

    # Delegate to existing orchestrator
    from engine.core import process as base_process
    res = base_process(input_path=input_path, models=models, bundle=bundle, fast=fast, timeout_s=timeout_s)
    # Enrich response
    if isinstance(res, dict):
        res.setdefault("session", "local")
        res.setdefault("input", inp.name)
        res["transcript"] = transcript
        res["segments"] = segments
        return res
    return {"session": "local", "input": inp.name, "transcript": transcript, "segments": segments, "events": []}
