# TransRapport Frontend - 5-Minuten-Handbuch

## Installation

Die drei Dateien sind bereits erstellt:
- `frontend/index.html` - Hauptseite
- `frontend/style.css` - Dark Theme Styling 
- `frontend/app.js` - JavaScript Logik

## Backend starten

```bash
cd transrapid-defkit
make dev
```

Das Backend läuft dann auf `http://127.0.0.1:8765`

## Frontend nutzen

1. **Öffne den Browser** und gehe zu: `http://127.0.0.1:8765/`
2. **Health prüfen**: Klick auf "Health prüfen" - Statuspunkt wird grün/rot
3. **Smoke-Test**: Klick auf "Smoke ausführen" - führt internen Test aus
4. **Datei analysieren**: 
   - Wähle eine `.wav`, `.mp3` oder `.txt` Datei
   - Klick auf "Verarbeiten"
   - Ergebnis erscheint als JSON
5. **Historie**: Letzte 10 Sessions werden automatisch gespeichert

## Design-Konzept

**Farbsystem:**
- Hintergrund: `#0a0a0a` (fast schwarz)
- Panels: `#1a1a1a` (dunkelgrau) 
- Akzent: `#22c55e` (grün für Status OK)
- Fehler: `#ef4444` (rot für Fehler)

**Spacing:**
- Grid-Gap: `1.5rem` (Desktop), `1rem` (Mobile)
- Panel-Padding: `1.5rem` (Desktop), `1rem` (Mobile)
- Buttons: `0.75rem 1.5rem`

**Komponenten:**
- Responsives Grid-Layout
- Fokus-Zustände für Barrierefreiheit
- Copy-to-Clipboard für JSON-Outputs
- localStorage für Session-Historie
- Monospace-Font für JSON-Darstellung

## Fehlerbehebung

**"Backend nicht erreichbar":**
```bash
make dev
```

**Keine Antwort von /healthz:**
- Prüfe ob FastAPI läuft
- Prüfe Browser-Konsole (F12)

**Datei-Upload funktioniert nicht:**
- Nur `.wav`, `.mp3`, `.txt` Dateien erlaubt
- Prüfe Backend-Logs

## Technische Details

- **Kein Build nötig** - direkt lauffähig
- **Keine externen Dependencies**
- **System-Fonts only** 
- **Same-Origin Requests** zu `/healthz`, `/_smoke`, `/process`
- **LocalStorage** für Session-Persistierung
- **CSS < 30KB, JS < 50KB**
