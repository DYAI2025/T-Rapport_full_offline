PY=python3.11
VENV=.venv
BIN=$(VENV)/bin
ENV=.env.dev
CT2_MODELS=./models/ct2
BUNDLES=./bundles/SerapiCore_1.0.yaml
PORT_API=8765

.PHONY: preflight venv deps assets smoke api ui dev stop clean cli enroll

preflight:
	bash tools/preflight.sh

venv:
	@command -v $(PY) >/dev/null || (echo "[ERR] Python 3.11 fehlt"; exit 11)
	@test -d $(VENV) || $(PY) -m venv $(VENV)
	$(BIN)/pip install -U pip wheel
	$(BIN)/pip install -r requirements.lock

deps: venv

assets:
	@test -d $(CT2_MODELS) || (echo "[ERR] Fehlende CT2-Modelle unter $(CT2_MODELS)."; exit 12)
	@test -f $(BUNDLES) || (echo "[ERR] Fehlendes Bundle: $(BUNDLES)"; exit 12)
	@command -v ffmpeg >/dev/null || (echo "[ERR] ffmpeg fehlt."; exit 13)

smoke: deps assets
	ENV_FILE=$(ENV) $(BIN)/python tools/smoke_engine.py

api:
	ENV_FILE=$(ENV) $(BIN)/uvicorn app.adapter:app --host 127.0.0.1 --port $(PORT_API) --reload &

ui:
	ENV_FILE=$(ENV) $(BIN)/python app/ui_main.py

dev: preflight deps assets smoke api ui
	@echo "✅ Dev-Stack läuft. API auf http://127.0.0.1:$(PORT_API)"

cli: preflight deps assets
	ENV_FILE=$(ENV) $(BIN)/python app/cli.py -i tests/data/hello.wav -o out/session_001.json

enroll: deps assets
	ENV_FILE=$(ENV) $(BIN)/python tools/enroll_from_wavs_sid.py

stop:
	@pkill -f "uvicorn app.adapter:app" || true

clean: stop
	rm -rf $(VENV) build dist *.spec
