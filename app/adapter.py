import os
import sys
import shutil
import json
from pathlib import Path
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel
import subprocess

# Import the unified engine adapter
sys.path.insert(0, ".")
from tools.engine_adapter import run_engine, EngineError

class Health(BaseModel):
    status: str
    offline: bool
    models_path: str
    bundle: str

def env_bool(name, default=False):
    v = os.environ.get(name, str(int(default)))
    return v in ("1", "true", "True", "YES", "yes")

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True, "hint": "Use /healthz or POST /process"}

@app.get("/healthz", response_model=Health)
def healthz():
    return Health(
        status="ok",
        offline=True,
        models_path="./models/ct2",
        bundle="./bundles/SerapiCore_1.0.yaml",
    )


@app.post("/process")
async def process(file: UploadFile = File(...)):
    # Speichere Upload als Tempfile
    tmp_dir = Path("tmp"); tmp_dir.mkdir(exist_ok=True)
    tmp_path = tmp_dir / file.filename
    with tmp_path.open("wb") as f:
        shutil.copyfileobj(file.file, f)

    # Use engine adapter directly
    models = os.environ.get("CT2_MODELS", "./models/ct2")
    bundle = os.environ.get("BUNDLES", "./bundles/SerapiCore_1.0.yaml")

    try:
        result = run_engine(str(tmp_path), models, bundle, fast=True, timeout_s=10)
        
        # Also save to out/ for compatibility
        out_dir = Path("out"); out_dir.mkdir(exist_ok=True)
        out_json = out_dir / "ui_session.json"
        with out_json.open("w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)
        
        return JSONResponse(result)
        
    except EngineError as e:
        if e.code == 504:  # Timeout
            return PlainTextResponse("Verarbeitung überschritt das Zeitlimit.", status_code=504)
        else:
            return PlainTextResponse(str(e), status_code=500)
    except Exception as e:
        return PlainTextResponse("Verarbeitung fehlgeschlagen.", status_code=500)
    finally:
        # Clean up temp file
        if tmp_path.exists():
            tmp_path.unlink()


@app.post("/export/txt")
async def export_txt(payload: dict):
    data = payload or {}
    events = data.get("events", []) or []
    transcript = data.get("transcript", "")
    lines = []
    lines.append(f"Session: {data.get('session','n/a')}")
    lines.append(f"Input:   {data.get('input','n/a')}")
    lines.append("")
    if transcript:
        lines.append("Transcript")
        lines.append("----------")
        lines.append(str(transcript).strip())
        lines.append("")
    lines.append("Markers")
    lines.append("-------")
    if not events:
        lines.append("(none)")
    else:
        lines.append("id\ttype\tscore\tts\tspan")
        for e in events:
            lines.append(f"{e.get('id')}\t{e.get('type')}\t{e.get('score')}\t{e.get('ts')}\t{e.get('span')}")
    return PlainTextResponse("\n".join(lines))
