# Generated Exports

This directory contains platform-ready brand assets generated from the canonical sources in `brand/logo/`.

Subdirectories: `x/`, `facebook/`, `linkedin/`, `github/`, `web/`, `press/`.
`manifest.json` lists every generated asset with its dimensions, purpose, and
source master. Regenerate everything with:

```bash
python3 scripts/export-brand-pack.py
```

Do not edit exported files by hand. Regenerate them from canonical vectors and `config/platforms.json`.
