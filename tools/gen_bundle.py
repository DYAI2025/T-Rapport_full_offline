#!/usr/bin/env python3
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:
    print("Bundle enthält keine gültigen Marker.")
    sys.exit(12)


def main() -> int:
    root = Path('.').resolve()
    markers = sorted(str(p.relative_to(root)) for p in root.rglob('markers/**/*.yaml'))
    if not markers:
        print("Bundle enthält keine gültigen Marker.")
        return 12
    out = root / 'bundles' / 'SerapiCore_1.0.yaml'
    out.parent.mkdir(parents=True, exist_ok=True)
    # Write deterministically with double quotes to satisfy simple awk counters
    lines = []
    lines.append('schema_version: "3.4"')
    lines.append('name: "SerapiCore_1.0"')
    lines.append('includes:')
    for p in markers:
        lines.append(f'  - "{p}"')
    out.write_text("\n".join(lines) + "\n", encoding='utf-8')
    print(f"Wrote bundle with {len(markers)} includes -> {out}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
