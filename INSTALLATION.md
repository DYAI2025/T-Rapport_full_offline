# TransRapport - Installation & Deployment

*Vollständige Anleitung für Setup, Installation und Deployment von TransRapport*

---

## Systemanforderungen

### Minimum-Anforderungen
| Komponente | Minimum | Empfohlen | Bemerkung |
|------------|---------|-----------|-----------|
| **CPU** | 4-Core 2.4GHz | 8-Core 3.0GHz | Intel/AMD x64 oder Apple Silicon |
| **RAM** | 8GB | 16GB | Mehr RAM = längere Sessions |
| **Storage** | 10GB frei | 20GB SSD | Für Modelle und Temp-Dateien |
| **OS** | Win10/macOS 10.15/Ubuntu 18 | Aktuelle Versionen | 64-Bit erforderlich |
| **Python** | 3.11+ | 3.11.x | Andere Versionen nicht getestet |
| **Audio** | Standard Mikrofon | USB-Mikrofon | Für Live-Aufnahmen |

### Netzwerk-Anforderungen
- **Offline-Betrieb**: Vollständig möglich nach Installation
- **Initial-Download**: ~3GB für Modelle (einmalig)
- **Firewalls**: Port 8765 für lokalen API-Server
- **Internet**: Nur für Updates und Support

---

## Installation

### Option A: Automatische Installation (Empfohlen)

#### Windows
```powershell
# PowerShell als Administrator öffnen
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Installer herunterladen und ausführen
Invoke-WebRequest -Uri "https://github.com/transrapport/installer/releases/download/v3.4/TransRapport-Installer-Win64.exe" -OutFile "TransRapport-Installer.exe"
.\TransRapport-Installer.exe
```

#### macOS
```bash
# Terminal öffnen und Installer herunterladen
curl -L "https://github.com/transrapport/installer/releases/download/v3.4/TransRapport-Installer-macOS.pkg" -o TransRapport-Installer.pkg

# Installer ausführen
sudo installer -pkg TransRapport-Installer.pkg -target /
```

#### Linux (Ubuntu/Debian)
```bash
# Repository hinzufügen
curl -fsSL https://packages.transrapport.de/gpg | sudo gpg --dearmor -o /usr/share/keyrings/transrapport.gpg
echo "deb [signed-by=/usr/share/keyrings/transrapport.gpg] https://packages.transrapport.de/debian stable main" | sudo tee /etc/apt/sources.list.d/transrapport.list

# Installieren
sudo apt update
sudo apt install transrapport
```

### Option B: Manuelle Installation (Entwickler)

#### 1. Repository klonen
```bash
git clone https://github.com/transrapport/transrapid-defkit.git
cd transrapid-defkit
```

#### 2. Python-Umgebung einrichten
```bash
# Python 3.11 installieren (falls nicht vorhanden)
# Windows: https://python.org/downloads
# macOS: brew install python@3.11  
# Linux: sudo apt install python3.11 python3.11-venv

# Virtuelle Umgebung erstellen
python3.11 -m venv .venv

# Aktivieren
# Linux/macOS:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate
```

#### 3. Abhängigkeiten installieren
```bash
# Basis-Abhängigkeiten
pip install -r requirements.lock

# Optional: Development-Tools
pip install -r requirements-dev.txt
```

#### 4. Modelle herunterladen
```bash
# Automatischer Download
make assets

# Oder manuell:
python tools/download_models.py --all
```

#### 5. System testen
```bash
# Smoke-Test
make smoke

# Vollständiger Test
make test
```

---

## Konfiguration

### Basis-Konfiguration

#### 1. Umgebungsvariablen (`.env`)
```bash
# API-Konfiguration
PORT_API=8765
HOST_API=127.0.0.1

# Modell-Pfade
CT2_MODELS=./models/ct2
BUNDLES=./bundles/SerapiCore_1.0.yaml

# Performance
MAX_CONCURRENT_SESSIONS=1
PROCESSING_TIMEOUT=300
MAX_FILE_SIZE_MB=500

# Logging
LOG_LEVEL=INFO
LOG_PATH=./logs/

# Debugging (nur für Entwicklung)
DEBUG=false
PROFILING=false
```

#### 2. Marker-Bundle anpassen
```bash
# Bundle neu generieren
python tools/build_bundle.py \
  --input markers/ \
  --output bundles/Custom_1.0.yaml \
  --include-categories ATO,SEM,CLU \
  --exclude-experimental

# Bundle aktivieren
export BUNDLES=./bundles/Custom_1.0.yaml
```

#### 3. Scoring-Parameter (`scoring/SCR_GLOBAL.json`)
```json
{
  "schema_version": "3.4",
  "weights": {
    "poseid": 1.5,      // Sprecher-Erkennung
    "risk": 1.2,        // Risiko-Marker
    "prosody": 1.0,     // Audio-Analyse
    "semantic": 0.9     // Text-Analyse
  },
  "thresholds": {
    "emit_event": 0.55, // Mindest-Score für Events
    "prosody_min": 0.6, // Prosody-Schwelle
    "risk_urgent": 0.85 // Dringliche Risiko-Marker
  },
  "fusion": {
    "method": "weighted_sum",
    "normalize": true,
    "cap": 1.0
  }
}
```

### Erweiterte Konfiguration

#### Audio-Pipeline (`config/audio.json`)
```json
{
  "input": {
    "sample_rate": 16000,
    "channels": 1,
    "bit_depth": 16,
    "format": "wav"
  },
  "processing": {
    "noise_reduction": true,
    "normalization": true,
    "vad_threshold": 0.5
  },
  "output": {
    "preserve_original": true,
    "compression": "flac"
  }
}
```

#### Prosody-Einstellungen (`config/prosody.json`)
```json
{
  "features": {
    "pitch_tracking": true,
    "intensity_tracking": true,
    "rhythm_analysis": true,
    "voice_quality": true
  },
  "thresholds": {
    "pause_min_duration": 0.3,
    "pause_max_duration": 10.0,
    "pitch_variance_threshold": 50,
    "volume_change_threshold": 15
  }
}
```

#### Speaker-ID (`config/sid.json`)
```json
{
  "enrollment": {
    "min_duration_seconds": 10,
    "max_speakers": 5,
    "similarity_threshold": 0.75
  },
  "detection": {
    "window_size_ms": 1000,
    "overlap_ms": 500,
    "confidence_threshold": 0.6
  }
}
```

---

## Deployment-Szenarien

### Szenario 1: Einzelpraxis (Desktop)

#### Setup
```bash
# Installation als Service (Windows)
sc create TransRapport binPath="C:\TransRapport\bin\transrapport.exe" start=auto
sc start TransRapport

# Installation als Service (Linux)
sudo systemctl enable transrapport
sudo systemctl start transrapport
```

#### Desktop-Verknüpfung erstellen
```bash
# Windows
echo '@echo off && cd "C:\TransRapport" && python app\ui_main.py' > "%USERPROFILE%\Desktop\TransRapport.bat"

# macOS
cat > ~/Desktop/TransRapport.command << 'EOF'
#!/bin/bash
cd ~/Applications/TransRapport
python app/ui_main.py
EOF
chmod +x ~/Desktop/TransRapport.command

# Linux
cat > ~/.local/share/applications/transrapport.desktop << 'EOF'
[Desktop Entry]
Name=TransRapport
Exec=/opt/transrapport/bin/transrapport
Icon=/opt/transrapport/share/icon.png
Type=Application
Categories=Office;Medical;
EOF
```

### Szenario 2: Mehrplatz-Praxis (Server)

#### Server-Setup
```bash
# Docker-Deployment
docker pull transrapport/server:3.4
docker run -d \
  --name transrapport-server \
  -p 8765:8765 \
  -v /data/transrapport:/app/data \
  -v /models:/app/models \
  transrapport/server:3.4

# Oder Docker Compose
cat > docker-compose.yml << 'EOF'
version: '3.8'
services:
  transrapport:
    image: transrapport/server:3.4
    ports:
      - "8765:8765"
    volumes:
      - ./data:/app/data
      - ./models:/app/models
      - ./config:/app/config
    environment:
      - MAX_CONCURRENT_SESSIONS=3
      - LOG_LEVEL=INFO
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/ssl/certs
    depends_on:
      - transrapport
EOF

docker-compose up -d
```

#### Client-Installation
```bash
# Lightweight Client (nur Frontend)
npm install -g @transrapport/client
transrapport-client --server https://server.praxis.de:8765
```

### Szenario 3: Cloud-Deployment

#### AWS Setup
```yaml
# CloudFormation Template (infrastructure.yml)
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  TransRapportInstance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-0abcdef1234567890  # TransRapport AMI
      InstanceType: c5.xlarge
      SecurityGroupIds:
        - !Ref TransRapportSecurityGroup
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash
          cd /opt/transrapport
          ./scripts/aws-setup.sh
          systemctl enable transrapport
          systemctl start transrapport

  TransRapportSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: TransRapport Security Group
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 8765
          ToPort: 8765
          CidrIp: 10.0.0.0/8  # Nur internes Netzwerk
```

#### Kubernetes Setup
```yaml
# k8s/deployment.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: transrapport
spec:
  replicas: 2
  selector:
    matchLabels:
      app: transrapport
  template:
    metadata:
      labels:
        app: transrapport
    spec:
      containers:
      - name: transrapport
        image: transrapport/server:3.4
        ports:
        - containerPort: 8765
        resources:
          requests:
            memory: "4Gi"
            cpu: "2"
          limits:
            memory: "8Gi"
            cpu: "4"
        volumeMounts:
        - name: models-storage
          mountPath: /app/models
        - name: data-storage
          mountPath: /app/data
      volumes:
      - name: models-storage
        persistentVolumeClaim:
          claimName: transrapport-models
      - name: data-storage
        persistentVolumeClaim:
          claimName: transrapport-data
---
apiVersion: v1
kind: Service
metadata:
  name: transrapport-service
spec:
  selector:
    app: transrapport
  ports:
  - port: 8765
    targetPort: 8765
  type: LoadBalancer
```

---

## Sicherheit und Compliance

### Datenschutz-Konfiguration

#### DSGVO-Compliance
```json
{
  "privacy": {
    "data_minimization": true,
    "purpose_limitation": "therapeutic_analysis",
    "storage_limitation_days": 2555,  // 7 Jahre
    "anonymization": {
      "enabled": true,
      "method": "k_anonymity",
      "k_value": 5
    }
  },
  "consent": {
    "required_before_processing": true,
    "granular_consent": true,
    "withdrawal_mechanism": true
  },
  "data_portability": {
    "export_formats": ["json", "pdf", "xml"],
    "automated_export": true
  }
}
```

#### Encryption Setup
```bash
# SSL-Zertifikat erstellen
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

# Datenbank-Verschlüsselung aktivieren
export ENCRYPTION_KEY=$(openssl rand -hex 32)
export DATABASE_ENCRYPTION=AES256
```

#### Access Control
```json
{
  "authentication": {
    "method": "local",  // Keine Cloud-Auth
    "session_timeout": 3600,
    "max_failed_attempts": 3
  },
  "authorization": {
    "roles": ["therapist", "supervisor", "admin"],
    "permissions": {
      "therapist": ["process", "view_own"],
      "supervisor": ["process", "view_all", "export"],
      "admin": ["*"]
    }
  }
}
```

### Network Security

#### Firewall-Regeln
```bash
# Linux iptables
sudo iptables -A INPUT -p tcp --dport 8765 -s 192.168.1.0/24 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 8765 -j DROP

# Windows Firewall
netsh advfirewall firewall add rule name="TransRapport API" dir=in action=allow protocol=TCP localport=8765 remoteip=192.168.1.0/24
```

#### VPN-Integration
```bash
# OpenVPN Client-Konfiguration
echo "
client
dev tun
proto udp
remote vpn.praxis.de 1194
ca ca.crt
cert client.crt
key client.key
" > transrapport-vpn.conf
```

---

## Monitoring und Wartung

### Health Monitoring

#### System-Monitoring Script
```bash
#!/bin/bash
# monitor.sh - TransRapport Health Check

API_URL="http://localhost:8765"
LOG_FILE="/var/log/transrapport-monitor.log"

check_api() {
    if curl -s "${API_URL}/healthz" | grep -q '"status":"ok"'; then
        echo "$(date): API OK" >> $LOG_FILE
        return 0
    else
        echo "$(date): API FAIL" >> $LOG_FILE
        return 1
    fi
}

check_disk_space() {
    USAGE=$(df /opt/transrapport | tail -1 | awk '{print $5}' | sed 's/%//')
    if [ $USAGE -gt 80 ]; then
        echo "$(date): DISK WARNING - ${USAGE}% used" >> $LOG_FILE
        return 1
    fi
    return 0
}

check_memory() {
    MEM_USAGE=$(free | grep '^Mem' | awk '{printf "%.0f", $3/$2 * 100.0}')
    if [ $MEM_USAGE -gt 90 ]; then
        echo "$(date): MEMORY WARNING - ${MEM_USAGE}% used" >> $LOG_FILE
        return 1
    fi
    return 0
}

# Hauptprüfung
if ! check_api || ! check_disk_space || ! check_memory; then
    # Alert senden (E-Mail, Slack, etc.)
    echo "TransRapport Health Check Failed" | mail -s "System Alert" admin@praxis.de
fi
```

#### Cron-Job einrichten
```bash
# Alle 5 Minuten prüfen
echo "*/5 * * * * /opt/transrapport/scripts/monitor.sh" | crontab -
```

### Log-Management

#### Log-Rotation (`/etc/logrotate.d/transrapport`)
```
/opt/transrapport/logs/*.log {
    daily
    missingok
    rotate 30
    compress
    notifempty
    create 0644 transrapport transrapport
    postrotate
        systemctl reload transrapport
    endscript
}
```

#### Centralized Logging (ELK Stack)
```yaml
# docker-compose.logging.yml
version: '3.8'
services:
  elasticsearch:
    image: elasticsearch:8.5.0
    environment:
      - discovery.type=single-node
    ports:
      - "9200:9200"
    
  logstash:
    image: logstash:8.5.0
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf
    depends_on:
      - elasticsearch
      
  kibana:
    image: kibana:8.5.0
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch
```

### Backup und Recovery

#### Automatisches Backup
```bash
#!/bin/bash
# backup.sh - TransRapport Backup Script

BACKUP_DIR="/backup/transrapport"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_PATH="${BACKUP_DIR}/transrapport_${DATE}"

mkdir -p $BACKUP_PATH

# Daten sichern
cp -r /opt/transrapport/data $BACKUP_PATH/
cp -r /opt/transrapport/config $BACKUP_PATH/
cp -r /opt/transrapport/logs $BACKUP_PATH/

# Datenbank-Export
sqlite3 /opt/transrapport/data/sessions.db ".backup ${BACKUP_PATH}/sessions.db"

# Komprimieren
tar -czf "${BACKUP_PATH}.tar.gz" -C $BACKUP_DIR "transrapport_${DATE}"
rm -rf $BACKUP_PATH

# Alte Backups löschen (älter als 30 Tage)
find $BACKUP_DIR -name "transrapport_*.tar.gz" -mtime +30 -delete

echo "Backup completed: ${BACKUP_PATH}.tar.gz"
```

#### Recovery-Prozedur
```bash
#!/bin/bash
# restore.sh - TransRapport Recovery Script

BACKUP_FILE="$1"
RESTORE_DIR="/opt/transrapport"

if [ -z "$BACKUP_FILE" ]; then
    echo "Usage: $0 <backup-file.tar.gz>"
    exit 1
fi

# Service stoppen
systemctl stop transrapport

# Backup entpacken
tar -xzf "$BACKUP_FILE" -C /tmp/

# Daten wiederherstellen
cp -r /tmp/transrapport_*/data/* $RESTORE_DIR/data/
cp -r /tmp/transrapport_*/config/* $RESTORE_DIR/config/

# Berechtigungen setzen
chown -R transrapport:transrapport $RESTORE_DIR

# Service starten
systemctl start transrapport

echo "Recovery completed from $BACKUP_FILE"
```

---

## Updates und Upgrades

### Automatische Updates

#### Update-Script
```bash
#!/bin/bash
# update.sh - TransRapport Auto-Update

CURRENT_VERSION=$(python -c "import app; print(app.__version__)")
LATEST_VERSION=$(curl -s https://api.github.com/repos/transrapport/transrapid-defkit/releases/latest | jq -r '.tag_name')

if [ "$CURRENT_VERSION" != "$LATEST_VERSION" ]; then
    echo "Update available: $CURRENT_VERSION -> $LATEST_VERSION"
    
    # Backup vor Update
    ./scripts/backup.sh
    
    # Update durchführen
    git fetch origin
    git checkout $LATEST_VERSION
    
    # Abhängigkeiten aktualisieren
    pip install -r requirements.lock
    
    # Modelle aktualisieren
    python tools/update_models.py
    
    # Service neu starten
    systemctl restart transrapport
    
    echo "Update completed to $LATEST_VERSION"
else
    echo "System is up to date: $CURRENT_VERSION"
fi
```

### Migration zwischen Versionen

#### Version 3.3 → 3.4 Migration
```python
# migrate_v33_to_v34.py
import json
import yaml
from pathlib import Path

def migrate_scoring_config():
    """Migrate scoring configuration to new format"""
    old_config = Path("scoring/SCR_GLOBAL.json")
    if old_config.exists():
        with old_config.open() as f:
            config = json.load(f)
        
        # Update schema version
        config["schema_version"] = "3.4"
        
        # Add new weight categories
        if "poseid" not in config["weights"]:
            config["weights"]["poseid"] = 1.5
        
        # Write updated config
        with old_config.open("w") as f:
            json.dump(config, f, indent=2)

def migrate_bundle_format():
    """Update bundle format for LEAN.DEEP 3.4"""
    bundle_path = Path("bundles/SerapiCore_1.0.yaml")
    if bundle_path.exists():
        with bundle_path.open() as f:
            bundle = yaml.safe_load(f)
        
        # Update version
        bundle["version"] = "3.4"
        
        # Ensure all includes are present
        marker_files = []
        for marker_dir in Path("markers").rglob("*.yaml"):
            marker_files.append(str(marker_dir.as_posix()))
        
        bundle["includes"] = sorted(marker_files)
        
        # Write updated bundle
        with bundle_path.open("w") as f:
            yaml.dump(bundle, f, default_flow_style=False)

if __name__ == "__main__":
    migrate_scoring_config()
    migrate_bundle_format()
    print("Migration to v3.4 completed")
```

---

## Troubleshooting

### Häufige Installationsprobleme

#### Problem: Python-Version nicht gefunden
```bash
# Lösung: Python 3.11 installieren
# Ubuntu/Debian
sudo apt install python3.11 python3.11-venv python3.11-dev

# CentOS/RHEL
sudo dnf install python311 python311-devel

# macOS
brew install python@3.11

# Windows
# Download von https://python.org/downloads/release/python-3119/
```

#### Problem: Modelle können nicht heruntergeladen werden
```bash
# Lösung: Manueller Download
mkdir -p models/ct2
cd models/ct2

# STT-Modelle
wget https://huggingface.co/guillaumekln/faster-whisper-medium/resolve/main/model.bin
wget https://huggingface.co/guillaumekln/faster-whisper-medium/resolve/main/config.json

# SID-Modelle  
mkdir -p ../sid/ecapa
cd ../sid/ecapa
wget https://huggingface.co/speechbrain/spkrec-ecapa-voxceleb/resolve/main/embedding_model.ckpt
```

#### Problem: Permission Denied
```bash
# Linux/macOS
sudo chown -R $USER:$USER /opt/transrapport
chmod +x /opt/transrapport/bin/*

# Windows (als Administrator)
icacls "C:\TransRapport" /grant %USERNAME%:F /t
```

### Performance-Probleme

#### Problem: Langsame Verarbeitung
```bash
# CPU-optimierte Installation
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# GPU-Unterstützung (CUDA)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Parallelisierung erhöhen
export OMP_NUM_THREADS=4
export MKL_NUM_THREADS=4
```

#### Problem: Speicher-Überlauf
```bash
# Swap-Datei erstellen (Linux)
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Speicher-Limits setzen
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512
```

### Netzwerk-Probleme

#### Problem: API nicht erreichbar
```bash
# Port-Check
netstat -tlnp | grep 8765
ss -tlnp | grep 8765

# Firewall-Check
sudo ufw status
sudo iptables -L

# Service-Status
systemctl status transrapport
journalctl -u transrapport -f
```

---

## Support und Community

### Offizielle Kanäle
- **Website**: https://transrapport.de
- **Dokumentation**: https://docs.transrapport.de  
- **GitHub**: https://github.com/transrapport/transrapid-defkit
- **Support-Email**: support@transrapport.de

### Community-Ressourcen
- **Forum**: https://community.transrapport.de
- **Discord**: https://discord.gg/transrapport
- **Reddit**: r/TransRapport
- **Stack Overflow**: Tag `transrapport`

### Professional Services
- **Installation-Service**: 299€ (Remote-Installation)
- **Training-Workshop**: 499€ (4h Online-Schulung)
- **Custom-Development**: Ab 1.500€ (Angepasste Features)
- **Enterprise-Support**: Ab 99€/Monat (Priority Support)

---

*Installation Guide Version 3.4 - Letzte Aktualisierung: 6. September 2025*
