# TransRapid DevKit (Offline, reproduzierbar)
Ziel: in 15 Minuten lauffähiges Dev-Stack-Setup. Kein Download, keine Magie.

## Setup
1) CT2-Modelle in `models/ct2/` kopieren.
2) Bundle nach `bundles/SerapiCore_1.0.yaml`.
3) `.env.dev.example` → `.env.dev`.
4) `make dev` starten.

## Fail-Fast & Pivot
- 15 Minuten ohne /healthz=200 → `make cli` ausführen (Offline-Artefakt-First).

## DoD
- `make preflight` Exit 0
- `make smoke` → `SMOKE:OK` ≤ 10 s, `out/session_001.json` existiert
- `make dev` → UI sichtbar, `/healthz` 200, offline=true
- Läuft ohne Internet (wenn Assets vorhanden)
