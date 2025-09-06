# TransRapid Frontend Pack
- `frontend/` (statisches HTML/CSS/JS, offline)
- `api_patch/app/adapter_ext.py` (Endpunkte `/_smoke`, `/process`)
- `api_patch/MOUNT_INSTRUCTIONS.txt` (Einbau in FastAPI)

Einbau:
1) `frontend/` nach `transrapid-defkit/` kopieren
2) `api_patch/app/adapter_ext.py` nach `transrapid-defkit/app/` kopieren
3) Anweisungen aus MOUNT_INSTRUCTIONS.txt in `app/adapter.py` ergänzen
4) `make dev` starten
