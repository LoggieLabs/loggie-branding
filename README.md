# Loggie Branding

Date: 2026-10-16

Canonical brand source and export repository for Loggie. This repo is the
source of truth for Loggie's logo geometry, wordmark, colors, social/profile
assets, marketing-site graphics, favicons, app icons, share cards, and
platform-specific public copy.

## Rule

Do not hand-redraw or manually resize shipped brand assets. Canonical vectors
live in `brand/logo/`; platform-ready files are generated from those sources
using the dimensions and safe-area rules in `config/platforms.json`.

Do not hand-maintain bios/descriptions separately on each platform. Canonical
messaging and platform-length variants live in `config/copy.json`; generated
copy/paste-ready files live in `exports/copy/`.

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
  copy.json              # canonical messaging + platform-specific text variants

exports/                 # generated platform deliverables (committed)
  x/  facebook/  linkedin/  github/  youtube/  gmail/  web/  press/
  copy/                   # generated bios, descriptions, links, signature copy
  manifest.json          # every generated visual asset: path, size, source, purpose

scripts/
  export-logo.py         # marketing-site asset set (favicons, lockups, share card)
  export-brand-pack.py   # visual platform pack driven by config/platforms.json
  export-copy-pack.py    # platform copy pack driven by config/copy.json
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
- `config/copy.json` — canonical tagline/descriptions plus per-platform variants
  and character ceilings where we have a reliable limit or working target.

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
# Full visual platform pack -> exports/
python3 scripts/export-brand-pack.py

# Public copy pack -> exports/copy/
python3 scripts/export-copy-pack.py

# Marketing-site asset set -> a consumer's own directory
python3 scripts/export-logo.py --out ../../sites/loggie-marketing/pilot/public
```

The copy exporter validates any declared character maximum before writing the
pack, and emits one human-readable `platform-copy.md`, one structured
`platform-copy.json`, plus a copy/paste-ready `.txt` file for each platform.
This keeps X, LinkedIn, Facebook, GitHub, YouTube, Gmail and web copy aligned
without forcing the same length everywhere.

Visual exporters need librsvg's GObject bindings (`gi`, Rsvg 2.0), pycairo,
and Pillow. The copy exporter uses only the Python standard library.

## Production policy

1. Edit canonical geometry only in `brand/logo/`.
2. Never edit generated files in `exports/` by hand.
3. Edit public messaging in `config/copy.json`, not directly on generated copy
   files; platform variants may differ in length but must preserve the same
   underlying positioning.
4. Profile/avatar exports are square with breathing room for circular crops.
5. Covers keep critical content inside the safe area defined in
   `config/platforms.json`, because platforms crop responsively.
6. At 16 px, use the dedicated favicon glyph, never the scaled master mark.
7. Bright teal is never used on light backgrounds (1.9:1 on Paper).
8. Keep user-facing Loggie branding centered on people, history, records,
   identity, messaging, continuity, and proof — not blockchain or
   agentic-system imagery.
9. Platform copy must not introduce unsupported product, compliance, security,
   or availability claims simply to fill a longer description field.

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
brand release: regenerate the visual and copy packs, visually review every
platform asset at real display size, proofread the platform copy in each live
editor, then upload/publish the final exports.
