#!/usr/bin/env python3
"""Generate copy/paste-ready platform bios and descriptions from config/copy.json."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "config" / "copy.json"
OUT = ROOT / "exports" / "copy"


def main() -> None:
    cfg = json.loads(SRC.read_text())
    OUT.mkdir(parents=True, exist_ok=True)

    rendered: dict[str, dict[str, dict]] = {}
    md = [
        "# Loggie platform copy",
        "",
        "Generated from `config/copy.json`. Do not edit generated files by hand.",
        "",
        "## Canonical messaging",
        "",
    ]

    for key, value in cfg["canonical"].items():
        md += [f"### {key}", "", str(value), ""]

    for platform, fields in cfg["platforms"].items():
        rendered[platform] = {}
        md += [f"## {platform}", ""]
        txt = []
        for field, spec in fields.items():
            text = spec["text"]
            count = len(text)
            limit = spec.get("maxCharacters")
            if limit is not None and count > limit:
                raise SystemExit(
                    f"{platform}.{field} is {count} characters; max is {limit}"
                )
            rendered[platform][field] = {
                "text": text,
                "characters": count,
                **({"maxCharacters": limit} if limit is not None else {}),
                **({"source": spec["source"]} if "source" in spec else {}),
                **({"notes": spec["notes"]} if "notes" in spec else {}),
            }
            suffix = f" — {count}/{limit} chars" if limit is not None else f" — {count} chars"
            md += [f"### {field}{suffix}", "", text, ""]
            if spec.get("notes"):
                md += [f"_Note: {spec['notes']}_", ""]
            txt += [f"[{field}]", text, ""]
        (OUT / f"{platform}.txt").write_text("\n".join(txt).rstrip() + "\n")

    payload = {
        "generatedFrom": "config/copy.json",
        "updated": cfg.get("updated"),
        "canonical": cfg["canonical"],
        "platforms": rendered,
    }
    (OUT / "platform-copy.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    (OUT / "platform-copy.md").write_text("\n".join(md).rstrip() + "\n")

    print(f"Generated copy pack for {len(rendered)} platforms -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
