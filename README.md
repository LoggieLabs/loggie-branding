# loggie-branding

Date: 2026-10-16

Source of truth for the Loggie brand: Logo System v1.0 (the L-tray mark with
the proof dot), moved out of `sites/loggie-marketing/pilot` on 2026-10-16.

## Contents

- `brand/logo/Loggie Logo System.pdf` — the logo system sheet (v1.0, 2026-10).
- `brand/logo/loggie-mark.svg` — master mark. The only full-size artwork.
- `brand/logo/loggie-wordmark.svg` — master wordmark.
- `brand/logo/loggie-glyph-16.svg` — the 16px glyph: candidate A from page 04
  of the logo sheet (L, short bar, enlarged dot), drawn on the pixel grid.
- `brand/new-logo-10-2026-concept.png` — the October 2026 concept sheet.
- `scripts/export-logo.py` — derives every shipped logo file (favicons,
  lockups, dark variants, tiles, share card) from the masters. No redraws;
  composition and recolouring by rule only.

## Exporting assets

```bash
python3 scripts/export-logo.py [--out DIR]   # default: ./public
```

Needs librsvg's GObject bindings (`gi`, Rsvg 2.0) and pycairo.

Consumers point `--out` at their own asset directory, e.g. the pilot
marketing site:

```bash
python3 scripts/export-logo.py --out ../loggie-marketing/pilot/public
```

## Consumers

- `sites/loggie-marketing/pilot` — ships generated assets in `public/`
  (committed there; regenerate from here when a master changes).
- `sdk/loggie-sdk` cli-kit — CLI banner renders the same mark in half-blocks;
  it is code, not a generated asset, and lives with the SDK.
- `app.loggielabs.com` — still on the retired orb; migration pending.

The orb-era system is preserved in the pilot repo at tag `v0.1.0`.
