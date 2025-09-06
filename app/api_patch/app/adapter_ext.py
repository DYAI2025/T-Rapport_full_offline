from fastapi import UploadFile, File, APIRouter
from fastapi.responses import JSONResponse
from pathlib import Path
import os, shutil, json, time, subprocess

router = APIRouter()

def attach_extra_routes(app):
    app.include_router(router)

@router.post('/_smoke')
async def run_smoke():
    try:
        cmd = [os.getenv('VENV_PY', '.venv/bin/python'), 'tools/smoke_engine.py']
        subprocess.run(cmd, check=True)
        data = Path('out/session_001.json').read_text(encoding='utf-8')
        return JSONResponse(json.loads(data))
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@router.post('/process')
async def process(file: UploadFile = File(...)):
    tmp_in = Path('tmp'); tmp_in.mkdir(exist_ok=True)
    dest = tmp_in / file.filename
    with dest.open('wb') as f:
        shutil.copyfileobj(file.file, f)
    out_data = {'session': f'ui-{int(time.time())}', 'input': file.filename,
                'events': [{'type':'marker_probe', 'score':0.61, 'ts':0.0}]}
    return JSONResponse(out_data)
