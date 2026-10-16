# Loggie Branding

Canonical brand source and export repository for Loggie.

This repo is the source of truth for Loggie's logo geometry, wordmark, colors, social/profile assets, marketing-site graphics, favicons, app icons, and share cards.

## Rule

Do not hand-redraw or manually resize shipped brand assets. Canonical vectors live in `brand/logo/`; platform-ready files are generated from those sources using the dimensions and safe-area rules in `config/platforms.json`.

## Brand concept

**A record held in continuity, with a proof state attached.**

- The **L** is the tray.
- The **bar** is the record.
- The **dot** is the proof.
- Teal is a **state/accent**, not the identity fill.

## Repository layout

```text
brand/
  logo/                 # canonical SVG sources only
  guidelines/           # logo system / usage docs
  colors/               # tokens and palette references

config/
  platforms.json        # output dimensions, formats, safe-area notes

exports/
  x/
  facebook/
  linkedin/
  github/
  web/
  app/
  press/

scripts/                 # deterministic export tooling
```

`exports/` contains generated deliverables. The master vectors in `brand/logo/` remain authoritative.

## Canonical palette

| Token | Hex | Use |
|---|---|---|
| Ink | `#0C1524` | mark, wordmark, dark ground |
| Paper | `#FFFFFF` | light ground, reversed mark |
| Mist | `#EEF1F5` | soft tiles and panels |
| Teal Bright | `#1FD1AE` | proof dot on Ink only |
| Teal Deep | `#0E8F78` | proof dot on Paper and Mist |
| Slate | `#5B6472` | one-color gray, captions |

## Initial platform targets

- X profile: 400 × 400
- X header: 1500 × 500
- LinkedIn personal cover: 1584 × 396
- LinkedIn Page logo: 400 × 400
- LinkedIn Page cover: 1512 × 256
- GitHub profile / org avatar: 500 × 500 working master
- Open Graph / social share card: 1200 × 630

Platform requirements change. `config/platforms.json` records when each target was verified and whether the dimension comes from an official source or an internal delivery convention.

## Production policy

1. Edit canonical geometry only in `brand/logo/`.
2. Never edit generated files in `exports/` by hand.
3. Profile/avatar exports should be square and include enough breathing room for circular crops.
4. Covers must keep critical content inside a defined safe area because platforms crop responsively.
5. At 16 px, use the dedicated favicon glyph rather than scaling the master mark.
6. Bright teal is never used on light backgrounds.
7. Keep user-facing Loggie branding centered on people, history, records, identity, messaging, continuity, and proof—not blockchain or agentic-system imagery.

## Status

The logo system is at **v1.0 geometry / optical pass pending**. Before declaring a brand release final:

- complete the wordmark optical pass;
- choose the 16 px favicon candidate in a real 1× browser tab;
- add canonical SVG masters;
- add deterministic export tooling;
- visually review every platform asset at real display size.
