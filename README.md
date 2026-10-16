# Loggie Branding

Date: 2026-10-16

Canonical brand source and export repository for Loggie. This repo is the
source of truth for Loggie's logo geometry, wordmark, colors, social/profile
assets, marketing-site graphics, favicons, app icons, and share cards.

## Rule

Do not hand-redraw or manually resize shipped brand assets. Canonical vectors
live in `brand/logo/`; platform-ready files are generated from those sources
using the dimensions and safe-area rules in `config/platforms.json`.

## Brand concept

**A record held in continuity, with a proof state attached.**

- The **L** is the tray.
- The **bar** is the record.
- The **dot** is the proof.
- Teal is a **state/accent**, not the identity fill.

## Repository layout

```text
brand/
  logo/                  # canonical SVG masters + the Logo System sheet (PDF)
  guidelines/            # logo system / usage docs
  new-logo-10-2026-concept.png

config/
  platforms.json         # output dimensions, formats, safe-area/composition rules

exports/                 # generated platform deliverables (committed)
  x/  facebook/  linkedin/  github/  web/  press/
  manifest.json          # every generated asset: path, size, source, purpose

scripts/
  export-logo.py         # marketing-site asset set (favicons, lockups, share card)
  export-brand-pack.py   # platform pack driven by config/platforms.json
```

## Canonical sources

- `brand/logo/Loggie Logo System.pdf` — the design sheet (v1.0, 5 pages).
- `brand/logo/loggie-mark.svg` — master mark, light grounds. The only
  full-size artwork.
- `brand/logo/loggie-mark-dark.svg` — the rule-derived dark-ground mark
  (Ink → Paper, Teal Deep → Teal Bright), committed for direct consumption.
- `brand/logo/loggie-wordmark.svg` — master wordmark (constructed monoline,
  not a typeset font).
- `brand/logo/loggie-glyph-16.svg` — the 16 px favicon glyph: candidate A from
  page 04 of the sheet (L, short bar, enlarged dot), drawn on the pixel grid.

## Canonical palette

| Token | Hex | Use |
|---|---|---|
| Ink | `#0C1524` | mark, wordmark, dark ground |
| Paper | `#FFFFFF` | light ground, reversed mark |
| Mist | `#EEF1F5` | soft tiles and panels |
| Teal Bright | `#1FD1AE` | proof dot on Ink only |
| Teal Deep | `#0E8F78` | proof dot on Paper and Mist |
| Slate | `#5B6472` | one-color gray, captions |

## Exporting

```bash
# Full platform pack (X, Facebook, LinkedIn, GitHub, web, press) -> exports/
python3 scripts/export-brand-pack.py

# Marketing-site asset set -> a consumer's own directory
python3 scripts/export-logo.py --out ../loggie-marketing/pilot/public
```

Both need librsvg's GObject bindings (`gi`, Rsvg 2.0), pycairo, and Pillow.

## Production policy

1. Edit canonical geometry only in `brand/logo/`.
2. Never edit generated files in `exports/` by hand.
3. Profile/avatar exports are square with breathing room for circular crops.
4. Covers keep critical content inside the safe area defined in
   `config/platforms.json`, because platforms crop responsively.
5. At 16 px, use the dedicated favicon glyph, never the scaled master mark.
6. Bright teal is never used on light backgrounds (1.9:1 on Paper).
7. Keep user-facing Loggie branding centered on people, history, records,
   identity, messaging, continuity, and proof — not blockchain or
   agentic-system imagery.

## Consumers

- `sites/loggie-marketing/pilot` — ships generated assets in its `public/`;
  regenerate from here when a master changes.
- `sdk/loggie-sdk` cli-kit — the CLI banner renders the same mark in
  half-blocks; it is code, not a generated asset, and lives with the SDK.
- `app.loggielabs.com` — still on the retired orb; migration pending.

The orb-era system is preserved in the pilot repo at tag `v0.1.0`.

## Status

Logo System **v1.0**. The 16 px favicon decision is made (candidate A, page 04
of the sheet) and the wordmark master is frozen. Remaining before tagging a
brand release: visually review every platform asset at real display size, and
upload the exports to each platform.
