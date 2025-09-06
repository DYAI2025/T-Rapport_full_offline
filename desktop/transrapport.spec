# PyInstaller spec for TransRapport desktop app
import sys
import os
from PyInstaller.utils.hooks import collect_submodules

hidden = collect_submodules('engine') + [
    'webview',
    'engine.detectors.audio.prosody',
    'engine.detectors.audio.sid',
    'engine.detectors.text.generic',
]

block_cipher = None

a = Analysis(
    ['desktop/main_desktop.py'],
    pathex=['.'],
    hiddenimports=hidden,
    datas=[
        ('frontend', 'frontend'),
        ('bundles', 'bundles'),
        ('models', 'models'),
        ('scoring', 'scoring'),
        ('DETECT_registry.json', '.'),
    ],
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz, a.scripts, a.binaries, a.zipfiles, a.datas,
          name='TransRapport', console=False)

# macOS .app bundle
app = BUNDLE(exe, name='TransRapport.app', icon=None)

