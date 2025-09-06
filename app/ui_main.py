import os, sys, json, urllib.request
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel

API = "http://127.0.0.1:8765/healthz"

def ping():
    try:
        with urllib.request.urlopen(API, timeout=1) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception:
        return None

def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("TransRapid Dev UI")
    layout = QVBoxLayout(w)

    status = QLabel("API prüfen...")
    layout.addWidget(status)

    btn_smoke = QPushButton("Smoke (out/session_001.json)")
    btn_smoke.setEnabled(False)
    layout.addWidget(btn_smoke)

    def run_smoke():
        import subprocess, sys
        exe = ".venv/bin/python" if os.name != "nt" else ".venv\\Scripts\\python.exe"
        subprocess.call([exe, "tools/smoke_engine.py"])

    btn_smoke.clicked.connect(run_smoke)

    info = ping()
    if info:
        status.setText(f"API ok | offline={info['offline']} | models={info['models_path']}")
        btn_smoke.setEnabled(True)
    else:
        status.setText("API nicht erreichbar. Starte 'make api' in einem Terminal.")

    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
