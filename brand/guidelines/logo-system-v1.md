# Loggie Logo System v1.0

Status: geometry defined; optical pass pending.

## Core idea

**A record held in continuity, with a proof state attached.**

The **L** is the tray. The **bar** is the record. The **dot** is the proof. The bar and dot share the same rest line and are held by the tray's raised tail.

## Master mark geometry

The master mark is built on a **120 × 120** unit grid with an 8-unit margin and a 104-unit live area.

- Stroke `S`: 28 units
- Record bar: 14 × 32 units (`S / 2` wide), corner radius 4
- Proof dot: diameter 20, center `(80, 62)`
- Horizontal rhythm: stem · 10 · bar · 10 · dot
- Rest line: `y = 72`
- Tail: last `S` of the foot, rising `S / 2`
- Corners: outer 24 / 20; stem cap 10; fillet 8; tail cap 6

Canonical SVG geometry from the design system:

```svg
<svg viewBox="0 0 120 120">
  <path d="M18 8 H26 A10 10 0 0 1 36 18 V76 A8 8 0 0 0 44 84 H84 C96 84 100 70 106 70 A6 6 0 0 1 112 76 V92 A20 20 0 0 1 92 112 H32 A24 24 0 0 1 8 88 V18 A10 10 0 0 1 18 8 Z"/>
  <rect x="46" y="40" width="14" height="32" rx="4"/>
  <circle cx="80" cy="62" r="10"/>
</svg>
```

Do not redraw this shape in downstream assets. All exports must derive from the canonical master SVG.

## Wordmark

The Loggie wordmark is a constructed monoline geometric sans, not a typeset font.

- Stroke: 10 on x-height 48
- Bowls: 20-unit centerline radius with 1-unit overshoot
- Tittle: 14-unit teal proof dot
- Clear space between mark and wordmark: `1S` at lockup scale
- Minimum lockup width: 112 px
- Below 112 px: use the mark alone

The tittle is the only colored part of the wordmark.

## Color system

**Teal is a state, not a fill.** It marks proof/status accents. It is never body text and never fills the L.

- Ink: `#0C1524`
- Paper: `#FFFFFF`
- Mist: `#EEF1F5`
- Teal Bright: `#1FD1AE` — dark grounds only
- Teal Deep: `#0E8F78` — Paper and Mist
- Slate: `#5B6472`

Do not use Teal Bright on white/light backgrounds.

## Small sizes

At 16 px, use a dedicated pixel-drawn glyph, not the scaled master.

Two candidates remain for final acceptance:

- **A:** L + short bar + enlarged dot
- **B:** L + bar, no dot

Choose the winner in a real browser tab on a true 1× display. The selected glyph becomes `favicon.svg` and `favicon-16x16.png`.

At 32 px and above, use the master mark in the standard tile composition.

## Tile composition

- Master mark occupies approximately 0.66 of the 120-unit tile
- Optical nudge: +2 right, −2 up
- Keep the mark inside the 80% maskable safe circle for PWA/app-icon outputs

## Prohibited treatments

- No outline logo
- No teal-filled L
- No bright teal on light backgrounds
- No ad-hoc geometry changes between surfaces
- No manual recreation of the wordmark

## Brand direction

Loggie should feel calm, sturdy, human, and durable. Avoid visual language that reads primarily as blockchain, crypto, developer tooling, or AI infrastructure. The identity should support the product idea of personal continuity, records, messaging, proof, and long-lived history.
