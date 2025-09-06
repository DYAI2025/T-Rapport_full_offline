import os
import sys
import json
import time
import uuid
from pathlib import Path
from typing import Any, Dict, List

# Fehlertexte (ein Satz) gemäß Vorgaben
MSG_ASSETS_MISSING = "Assets fehlen (models/ct2 oder Bundle)."
MSG_ENGINE_MISSING = "Echte Engine nicht verfügbar."
MSG_TIMEOUT = "Verarbeitung überschritt das Zeitlimit."
MSG_FAILED = "Verarbeitung fehlgeschlagen."
MSG_BUNDLE_INVALID = "Bundle enthält keine gültigen Marker."


class EngineError(Exception):
    def __init__(self, message: str, code: int = 20):
        super().__init__(message)
        self.code = code


def _ensure_assets(models: Path, bundle: Path) -> None:
    if not models.exists() or (bundle.is_dir() or not bundle.exists()):
        raise EngineError(MSG_ASSETS_MISSING, code=12)
    # Naive check: ensure bundle contains at least one include path
    try:
        txt = bundle.read_text(encoding="utf-8")
        has_includes = False
        for line in txt.splitlines():
            s = line.strip()
            if s.startswith("-") and ("markers/" in s or s.endswith(".yaml") or s.endswith(".yml")):
                has_includes = True
                break
        if not has_includes:
            raise EngineError(MSG_BUNDLE_INVALID, code=12)
    except EngineError:
        raise
    except Exception:
        raise EngineError(MSG_BUNDLE_INVALID, code=12)


def _import_engine():
    """
    Versuche die echte Engine zu importieren.
    Erwartete Kandidaten:
    - marker_engine_core.process (callable)
    - marker_engine_core (mit callable process/run)
    Keine Fallback-Simulation. Bei Nichterfolg: EngineError(12).
    """
    # 0) Bevorzugt: marker_engine_core.process (mit STT-Integration)
    try:
        from engine.marker_engine_core import process as engine_entry  # type: ignore
        return engine_entry
    except Exception:
        pass
    # 1) Fallback: lokaler Core
    try:
        from engine.core import process as engine_entry  # type: ignore
        return engine_entry
    except Exception:
        pass
    # 2) Fallback: extern benannter Kern
    try:
        from marker_engine_core import process as engine_entry  # type: ignore
        return engine_entry
    except Exception:
        pass
    try:
        import marker_engine_core  # type: ignore
        # Versuche übliche Einstiege
        if hasattr(marker_engine_core, "process") and callable(marker_engine_core.process):
            return marker_engine_core.process
        if hasattr(marker_engine_core, "run") and callable(marker_engine_core.run):
            return marker_engine_core.run
    except Exception:
        pass
    raise EngineError(MSG_ENGINE_MISSING, code=12)


def _call_engine(fn, input_path: Path, models: Path, bundle: Path, fast: bool = True, timeout_s: int = 8):
    """Rufe die echte Engine-Funktion auf. Minimal-invasiv und robust gegen unterschiedliche Signaturen."""
    # Versuche bevorzugte Signaturen
    kwargs = {
        "input_path": str(input_path),
        "models": str(models),
        "bundle": str(bundle),
        "fast": fast,
        "timeout_s": timeout_s,
    }
    
    # Innerer Aufruf mit Zeitlimit über einfachen Poll (keine Threads/Signals, portabel/offline)
    start = time.time()
    result: Any = None
    last_err: Exception | None = None

    while True:
        try:
            # Probier standardisierte Kwargs
            result = fn(**kwargs)
            break
        except TypeError:
            # Fallback: alternative Namen
            alt_kwargs = {
                "input": str(input_path),
                "models_path": str(models),
                "bundle_path": str(bundle),
                "fast": fast,
                "timeout": timeout_s,
            }
            try:
                result = fn(**alt_kwargs)
                break
            except Exception as e:
                last_err = e
                break
        except Exception as e:
            last_err = e
            break
        finally:
            if time.time() - start > timeout_s:
                raise EngineError(MSG_TIMEOUT, code=21)

    if result is None and last_err is not None:
        # Engine hat geworfen
        raise EngineError(MSG_FAILED, code=21)

    # Normalisiere Output
    events: List[Dict[str, Any]]
    if isinstance(result, dict) and "events" in result:
        events = list(result.get("events") or [])
    elif isinstance(result, list):
        events = result
    else:
        # Unbekanntes Format
        raise EngineError(MSG_FAILED, code=21)

    # Validierung Score
    has_positive = False
    norm_events: List[Dict[str, Any]] = []
    for e in events:
        if not isinstance(e, dict):
            continue
        score = e.get("score")
        try:
            if score is None:
                continue
            score_f = float(score)
        except Exception:
            continue
        if score_f > 0:
            has_positive = True
        norm_events.append(e)

    if not has_positive:
        raise EngineError(MSG_FAILED, code=21)

    return norm_events


def run_engine(input: str | Path, models: str | Path, bundle: str | Path, fast: bool = True, timeout_s: int = 8) -> Dict[str, Any]:
    """
    Einheitlicher Einstieg für CLI/Smoke/API.
    - Prüft Assets
    - Importiert echte Engine
    - Ruft Engine auf
    - Validiert Events (mind. ein score>0)
    - Liefert {session, input_path, events}
    """
    inp = Path(input)
    models_p = Path(models)
    bundle_p = Path(bundle)

    _ensure_assets(models_p, bundle_p)

    engine_fn = _import_engine()
    events = _call_engine(engine_fn, inp, models_p, bundle_p, fast=fast, timeout_s=timeout_s)

    # Convert sid events to poseid type for API consistency
    for event in events:
        if event.get("type") == "sid":
            event["type"] = "poseid"
            # Keep original ID but ensure it's clear it's speaker ID
            if "SID" in event.get("id", ""):
                event["id"] = event["id"].replace("SID", "POSEID")

    session = f"session-{uuid.uuid4().hex[:8]}"
    return {
        "session": session, 
        "input": str(inp.name),  # Return just filename for API consistency
        "events": events
    }
