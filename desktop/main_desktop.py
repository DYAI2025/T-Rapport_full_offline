import os
import base64
import tempfile
from pathlib import Path

import webview  # pywebview

from engine.marker_engine_core import process as engine_process

ROOT = Path(__file__).resolve().parents[1]
CT2 = str(ROOT / "models" / "ct2")
BUNDLE = str(ROOT / "bundles" / "SerapiCore_1.0.yaml")


class API:
    def healthz(self):
        return {
            "status": "ok",
            "offline": True,
            "models_path": "./models/ct2",
            "bundle": "./bundles/SerapiCore_1.0.yaml",
        }

    def process_path(self, path: str):
        return engine_process(path, models=CT2, bundle=BUNDLE, fast=True)

    def process_blob(self, name: str, b64: str):
        raw = base64.b64decode(b64)
        with tempfile.NamedTemporaryFile(prefix="tr_", suffix="_" + name, delete=False) as f:
            f.write(raw)
            tmp = f.name
        try:
            return engine_process(tmp, models=CT2, bundle=BUNDLE, fast=True)
        finally:
            try:
                os.remove(tmp)
            except Exception:
                pass

    def export_txt(self, payload: dict) -> str:
        data = payload or {}
        lines = []
        lines.append(f"Session: {data.get('session','n/a')}")
        lines.append(f"Input:   {data.get('input','n/a')}")
        lines.append("")
        tx = (data.get("transcript") or "").strip()
        if tx:
            lines += ["Transcript", "----------", tx, ""]
        lines += ["Markers", "-------"]
        ev = data.get("events") or []
        if not ev:
            lines.append("(none)")
        else:
            lines.append("id\ttype\tscore\tts\tspan")
            for e in ev:
                lines.append(f"{e.get('id')}\t{e.get('type')}\t{e.get('score')}\t{e.get('ts')}\t{e.get('span')}")
        return "\n".join(lines)


def _ui_path() -> str:
    return str((ROOT / "frontend" / "index.html").resolve())


if __name__ == "__main__":
    api = API()
    webview.create_window("TransRapport", _ui_path(), js_api=api)
    webview.start()

