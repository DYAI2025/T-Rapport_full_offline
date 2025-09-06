import json
import subprocess
from pathlib import Path


def test_cli_produces_events():
    root = Path(__file__).resolve().parents[1]
    out = root / "out/session_001.json"
    if out.exists():
        out.unlink()

    cmd = ["python", "app/cli.py", "-i", "tests/data/hello.wav", "-o", str(out)]
    proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True)

    assert proc.returncode == 0, f"CLI failed: {proc.stderr.strip()}"
    assert out.exists(), "Output JSON not created"

    data = json.loads(out.read_text(encoding="utf-8"))
    assert isinstance(data, dict), "Output is not a JSON object"
    assert "session" in data and isinstance(data["session"], str)
    assert "input" in data
    assert "events" in data and isinstance(data["events"], list)

    # At least one positive score
    scores = []
    for e in data["events"]:
        if isinstance(e, dict) and "score" in e:
            try:
                scores.append(float(e["score"]))
            except Exception:
                pass
    assert any(s > 0 for s in scores), "No positive score in events"

