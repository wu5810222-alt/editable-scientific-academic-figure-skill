#!/usr/bin/env python3
"""List selectable scientific figure styles from the bundled YAML catalog."""

from pathlib import Path
import argparse
import json
import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    path = Path(__file__).resolve().parent.parent / "references" / "style-presets.yaml"
    styles = yaml.safe_load(path.read_text(encoding="utf-8"))["styles"]
    if args.json:
        print(json.dumps(styles, ensure_ascii=False, indent=2))
        return
    print("STYLE\tLAYOUT\tDENSITY\tSHAPES")
    for name, spec in styles.items():
        print(f"{name}\t{spec['layout']}\t{spec['density']}\t{', '.join(spec['shapes'])}")


if __name__ == "__main__":
    main()
