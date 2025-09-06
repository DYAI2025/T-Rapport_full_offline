# TransRapport - Dokumentation

## Überblick

TransRapport ist ein offline-fähiges System zur automatischen Analyse von Therapiegesprächen. Es erkennt therapeutisch relevante Sprachmuster, emotionale Marker und Gesprächsdynamiken in Echtzeit oder aus Aufzeichnungen.

## Inhaltsverzeichnis

1. [Systemarchitektur](#systemarchitektur)
2. [Installation und Setup](#installation-und-setup)
3. [Bedienung](#bedienung)
4. [Marker-System](#marker-system)
5. [API-Referenz](#api-referenz)
6. [Technische Details](#technische-details)
7. [Troubleshooting](#troubleshooting)

---

## Systemarchitektur

### Hauptkomponenten

#### 1. **Marker-Engine** (`engine/`)
- **Prosody-Detektor**: Analysiert Sprechgeschwindigkeit, Pausen, Betonung
- **Speaker-ID (PoseID)**: Erkennt und unterscheidet Sprecher
- **Text-Analyse**: Verarbeitet Wortinhalt und semantische Muster
- **Cluster-Analyse**: Erkennt wiederkehrende Gesprächsmuster
- **Meta-Analyse**: Übergeordnete therapeutische Dynamiken

#### 2. **Frontend** (`frontend/`)
- Benutzeroberfläche für Live-Transkription
- Datei-Upload für Audioanalyse
- Echtzeit-Anzeige erkannter Marker
- Export-Funktionen für Therapieberichte

#### 3. **Backend-API** (`app/`)
- REST-API für Audioprocessing
- WebSocket für Live-Streaming
- Offline-First Architektur
- JSON-basierte Datenübertragung

### Datenfluss

```
Audio-Input → STT (Whisper/CT2) → Marker-Detection → Event-Fusion → Export
                ↓                        ↓              ↓
           Transkript              Pattern-Erkennung   JSON-Events
```

---

## Installation und Setup

### Systemanforderungen

- **Python**: 3.11 oder höher
- **Speicher**: Mindestens 8GB RAM
- **Festplatte**: 5GB freier Speicherplatz für Modelle
- **Audio**: Mikrofon oder Audiodateien (WAV, MP3)

### Schnellstart

1. **Repository klonen:**
```bash
git clone <repository-url>
cd transrapid-defkit
```

2. **Abhängigkeiten installieren:**
```bash
make deps
```

3. **Modelle einrichten:**
```bash
make assets
```

4. **System testen:**
```bash
make smoke
```

5. **Server starten:**
```bash
make api
```

6. **Frontend öffnen:**
```bash
open frontend/index.html
```

### Detaillierte Installation

#### Python-Umgebung vorbereiten
```bash
# Virtuelle Umgebung erstellen
python3.11 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# oder
.venv\Scripts\activate     # Windows

# Abhängigkeiten installieren
pip install -r requirements.lock
```

#### Modelle herunterladen
Die KI-Modelle werden automatisch beim ersten Start heruntergeladen:
- **CT2-STT-Modelle**: Für Spracherkennung (~2GB)
- **ECAPA-Embedding**: Für Sprechererkennung (~100MB)
- **Prosody-Modelle**: Für Sprachanalyse (~500MB)

---

## Bedienung

### Web-Interface

#### Hauptansicht
Das Frontend zeigt drei Bereiche:
1. **Transkription**: Live-Text der Spracherkennung
2. **Marker-Display**: Erkannte therapeutische Muster
3. **Kontrollen**: Start/Stop/Export Buttons

#### Workflow für Live-Sitzung
1. **Mikrofon aktivieren**: "Start" Button klicken
2. **Sprechen**: System transkribiert und analysiert live
3. **Marker beobachten**: Erkannte Muster werden farbig angezeigt
4. **Session beenden**: "Stop" Button klicken
5. **Export**: Sitzungsdaten als JSON herunterladen

#### Workflow für Datei-Analyse
1. **Datei auswählen**: "Datei auswählen" Button
2. **Upload**: WAV oder MP3 Datei hochladen
3. **Analyse**: System verarbeitet die gesamte Datei
4. **Ergebnisse**: Marker und Transkript werden angezeigt
5. **Export**: Analyseergebnisse herunterladen

### Kommandozeile (CLI)

#### Einzeldatei verarbeiten
```bash
python app/cli.py -i session.wav -o results.json
```

#### Batch-Verarbeitung
```bash
for file in *.wav; do
    python app/cli.py -i "$file" -o "results_${file%.*}.json"
done
```

#### Optionen
- `-i, --input`: Eingabedatei (WAV, MP3)
- `-m, --models`: Pfad zu KI-Modellen (Standard: ./models/ct2)
- `-b, --bundle`: Marker-Bundle (Standard: ./bundles/SerapiCore_1.0.yaml)
- `-o, --out`: Ausgabedatei (JSON)

---

## Marker-System

### Marker-Hierarchie (LEAN.DEEP 3.4)

#### **ATO - Atomic Markers** (Grundbausteine)
Einzelne, isolierte Sprachelemente:
- `ATO_PAUSE_LONG`: Lange Sprechpausen (>2s)
- `ATO_SIGH`: Seufzer und tiefe Atemzüge
- `ATO_LAUGHTER`: Lachen und Gelächter
- `ATO_FILLER`: Füllwörter ("äh", "ehm")

#### **SEM - Semantic Markers** (Bedeutungsebene)
Inhaltliche und emotionale Muster:
- `SEM_PROJECTION`: Projektionen auf andere
- `SEM_RESISTANCE`: Widerstand gegen Therapie
- `SEM_INSIGHT`: Momente der Selbsterkenntnis
- `SEM_COPING`: Bewältigungsstrategien

#### **CLU - Cluster Markers** (Mustergruppen)
Wiederkehrende Gesprächssequenzen:
- `CLU_AVOIDANCE_PATTERN`: Vermeidungsverhalten
- `CLU_EMOTIONAL_CYCLE`: Emotionale Zyklen
- `CLU_THERAPEUTIC_ALLIANCE`: Therapeutische Beziehung

#### **MEMA - Meta Markers** (Übergeordnete Dynamiken)
Systemische Therapieprozesse:
- `MEMA_BREAKTHROUGH`: Therapeutische Durchbrüche
- `MEMA_REGRESSION`: Rückschritte im Prozess
- `MEMA_INTEGRATION`: Integration von Einsichten

### Audio-Marker

#### **Prosody** (`M_PROSODY_*`)
- **Rate**: Sprechgeschwindigkeit (langsam/schnell)
- **Pitch**: Tonhöhe und Melodie
- **Volume**: Lautstärke und Intensität
- **Hesitation**: Zögern und Unsicherheit

#### **Speaker-ID** (`M_POSEID_*`)
- **Client**: Klient/Patient identifiziert
- **Therapist**: Therapeut identifiziert
- **Unknown**: Unbekannte Stimme

### Scoring und Gewichtung

Jeder Marker erhält einen Relevanz-Score (0.0 - 1.0):
```json
{
  "weights": {
    "poseid": 1.5,     // Sprecher-Identifikation
    "risk": 1.2,       // Risiko-Marker
    "prosody": 1.0,    // Sprechweise
    "intent": 0.9,     // Absichten
    "action": 0.8      // Handlungen
  }
}
```

---

## API-Referenz

### Endpoints

#### `GET /healthz`
Systemstatus abfragen
```json
{
  "status": "ok",
  "offline": true,
  "models_path": "./models/ct2",
  "bundle": "./bundles/SerapiCore_1.0.yaml"
}
```

#### `POST /process`
Audiodatei zur Analyse hochladen
```bash
curl -X POST -F "file=@session.wav" http://localhost:8765/process
```

**Response:**
```json
{
  "session": "session-abc123",
  "input": "session.wav",
  "events": [
    {
      "id": "M_PROSODY_RATE_SLOW",
      "type": "prosody", 
      "score": 0.87,
      "ts": 12.5,
      "span": "00:12.50-00:15.20",
      "meta": {"wpm": 85}
    }
  ]
}
```

#### `GET /`
API-Info
```json
{
  "ok": true,
  "hint": "Use /healthz or POST /process"
}
```

### Event-Format

Jedes erkannte Event hat folgende Struktur:
```json
{
  "id": "MARKER_ID",           // Eindeutige Marker-ID
  "type": "prosody|poseid|text|cluster|meta",
  "score": 0.75,               // Konfidenz-Score (0.0-1.0)
  "ts": 15.2,                  // Zeitstempel in Sekunden
  "span": "00:15.20-00:18.45", // Zeitbereich (MM:SS.ms)
  "meta": {                    // Zusätzliche Daten
    "speaker": "client",
    "confidence": 0.89
  }
}
```

---

## Technische Details

### Projektstruktur

```
transrapid-defkit/
├── app/                     # Backend-Anwendung
│   ├── adapter.py          # FastAPI Server
│   ├── cli.py              # Kommandozeilen-Tool
│   └── ui_main.py          # Desktop-UI
├── engine/                  # Marker-Engine
│   ├── core.py             # Haupt-Engine
│   ├── detectors/          # Detector-Module
│   │   ├── audio/          # Audio-Analyse
│   │   ├── text/           # Text-Analyse
│   │   └── cluster/        # Muster-Erkennung
│   └── stt/                # Speech-to-Text
├── frontend/               # Web-Interface
│   ├── index.html         # Haupt-Seite
│   ├── app.js             # JavaScript-Logic
│   └── style.css          # Styling
├── markers/                # Marker-Definitionen
│   ├── ATO/               # Atomic Markers
│   ├── SEM/               # Semantic Markers
│   ├── CLU/               # Cluster Markers
│   └── MEMA/              # Meta Markers
├── models/                 # KI-Modelle
│   ├── ct2/               # STT-Modelle
│   └── sid/               # Speaker-ID
├── bundles/               # Marker-Bundles
├── scoring/               # Scoring-Konfiguration
└── tools/                 # Entwickler-Tools
```

### Marker-Bundle System

#### Bundle-Definition (`bundles/SerapiCore_1.0.yaml`)
```yaml
id: SerapiCore_1.0
version: "3.4"
generated: "2025-09-06"
includes:
  - markers/ATO/ATO_PAUSE_LONG.yaml
  - markers/SEM/SEM_PROJECTION.yaml
  - markers/CLU/CLU_AVOIDANCE.yaml
  # ... weitere 149 Marker
```

#### Registry-System (`DETECT_registry.json`)
Ordnet Marker den entsprechenden Detektoren zu:
```json
[
  {
    "id": "DET_PROSODY",
    "module": "engine.detectors.audio.prosody",
    "fires_marker": [
      "M_PROSODY_RATE_SLOW",
      "M_PROSODY_PITCH_HIGH"
    ]
  }
]
```

### Konfiguration

#### Scoring-Gewichte (`scoring/SCR_GLOBAL.json`)
```json
{
  "schema_version": "3.4",
  "weights": {
    "poseid": 1.5,
    "risk": 1.2,
    "prosody": 1.0
  },
  "fusion": {
    "method": "weighted_sum",
    "normalize": true,
    "cap": 1.0
  },
  "thresholds": {
    "emit_event": 0.55
  }
}
```

#### Umgebungsvariablen
- `CT2_MODELS`: Pfad zu STT-Modellen
- `BUNDLES`: Pfad zum Marker-Bundle
- `DEBUG`: Debugging aktivieren
- `PORT_API`: API-Server Port (Standard: 8765)

### Entwicklung

#### Neue Marker hinzufügen
1. YAML-Datei in `markers/` erstellen
2. Bundle neu generieren: `make bundle`
3. Registry aktualisieren: `make registry`
4. Tests ausführen: `make smoke`

#### Detector erweitern
1. Python-Modul in `engine/detectors/` erstellen
2. Registry-Eintrag hinzufügen
3. Marker-Zuordnung konfigurieren

#### Tests ausführen
```bash
make smoke          # Smoke-Tests
make cli           # CLI-Tests  
python -m pytest   # Unit-Tests
```

---

## Troubleshooting

### Häufige Probleme

#### 1. **Server startet nicht**
```
ModuleNotFoundError: No module named 'fastapi'
```
**Lösung:** Virtuelle Umgebung aktivieren und Abhängigkeiten installieren
```bash
source .venv/bin/activate
pip install -r requirements.lock
```

#### 2. **Modelle fehlen**
```
Assets fehlen (models/ct2 oder Bundle).
```
**Lösung:** Modelle herunterladen
```bash
make assets
```

#### 3. **Keine Audio-Erkennung**
```
Mikrofon nicht verfügbar
```
**Lösung:** Browser-Berechtigungen prüfen und HTTPS verwenden

#### 4. **Leere Marker-Ergebnisse**
**Lösung:** Bundle und Registry neu generieren
```bash
make bundle
make registry
```

### Logging und Debugging

#### Debug-Modus aktivieren
```bash
export DEBUG=1
make api
```

#### Log-Dateien
- `logs/engine.log`: Engine-Verarbeitung
- `logs/api.log`: API-Requests
- `logs/detector.log`: Marker-Detection

#### Performance-Monitoring
```bash
# CPU/Memory Usage
htop

# API-Performance
curl -w "@curl-format.txt" http://localhost:8765/healthz
```

### Erweiterte Konfiguration

#### Custom Marker-Bundle erstellen
```bash
python tools/build_bundle.py --input custom_markers/ --output custom.yaml
```

#### Detector-Performance optimieren
```python
# scoring/SCR_CUSTOM.json
{
  "thresholds": {
    "emit_event": 0.3,  # Niedrigere Schwelle = mehr Events
    "prosody_min": 0.6  # Höhere Prosody-Schwelle
  }
}
```

#### Multi-Language Support
```bash
# Englische Modelle laden
export CT2_MODELS="./models/ct2/en"
make api
```

---

## Support und Community

### Dokumentation
- **Technische Docs**: `/docs/technical/`
- **API-Referenz**: `/docs/api/`
- **Marker-Guide**: `/docs/markers/`

### Lizenz
**CC BY-NC-SA 4.0** - Nicht-kommerzielle Nutzung mit Quellenangabe

### Mitwirken
1. Fork erstellen
2. Feature-Branch: `git checkout -b feature/neue-funktion`
3. Commit: `git commit -m "Neue Funktion"`
4. Push: `git push origin feature/neue-funktion`
5. Pull-Request erstellen

---

**Version**: 3.4  
**Datum**: September 2025  
**Autor**: TransRapport Development Team
