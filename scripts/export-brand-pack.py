#!/usr/bin/env python3
"""
export-brand-pack — generates every platform asset in exports/ from the
masters in brand/logo/ and the targets in config/platforms.json.

The composition vocabulary (what each target's "composition.kind" means):

  tile          mark on an opaque Ink square at 0.66 scale, nudged +2/-2;
                inside the 80% maskable circle, so circular crops never clip
  tile-rounded  the same tile with rounded corners (small favicons only)
  glyph         the pixel-drawn 16px glyph, rendered 1:1 on its grid
  cover         Ink ground, dark lockup centered in the target's safeArea,
                optionally the tagline beneath it
  transparent-lockup
                light-ground lockup fitted to an exact transparent canvas
  share-card    the full OG card (headline + status line), from export-logo

Composition and recolouring by rule only — the drawing logic lives in
export-logo.py and is imported from there, so the two exporters cannot drift.
Safe areas and dimensions live in config/platforms.json, not here.

Run:  python3 scripts/export-brand-pack.py [--out DIR]   (default: exports)
Needs librsvg's GObject bindings (gi, Rsvg 2.0), pycairo, and Pillow.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location("export_logo", ROOT / "scripts" / "export-logo.py")
lib = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lib)

MASTER_MARK = "brand/logo/loggie-mark.svg"
MASTER_WORDMARK = "brand/logo/loggie-wordmark.svg"
MASTER_GLYPH = "brand/logo/loggie-glyph-16.svg"
LOCKUP_SOURCES = f"{MASTER_MARK} + {MASTER_WORDMARK}"


def cover(w: int, h: int, comp: dict, lock_dark: str, tagline: str) -> Image.Image:
    """Ink ground; the dark lockup centered in the safe area, tagline under it."""
    img = Image.new("RGBA", (w, h), lib.INK)
    sa = comp["safeArea"]
    sx, sy = sa["left"], sa["top"]
    sw, sh = w - sa["left"] - sa["right"], h - sa["top"] - sa["bottom"]

    with_tag = comp.get("tagline", False)
    lock_h = round(sh * (0.46 if with_tag else 0.60))
    lw, lh = lib.size_for_height(lock_dark, lock_h)
    if lw > sw * 0.9:
        lw, lh = lib.size_for_width(lock_dark, round(sw * 0.9))

    tag_font = tag_w = tag_h = 0
    gap = 0
    if with_tag:
        tag_font = ImageFont.truetype(lib.FONT_BOLD, max(20, round(lh * 0.34)))
        box = ImageDraw.Draw(img).textbbox((0, 0), tagline, font=tag_font)
        tag_w, tag_h = box[2] - box[0], box[3] - box[1]
        gap = round(lh * 0.42)

    block_h = lh + (gap + tag_h if with_tag else 0)
    lx = sx + (sw - lw) // 2
    ly = sy + (sh - block_h) // 2
    img.alpha_composite(lib.render(lock_dark, lw, lh), (lx, ly))
    if with_tag:
        ImageDraw.Draw(img).text(
            (sx + (sw - tag_w) // 2, ly + lh + gap), tagline,
            font=tag_font, fill="#9CA3AF",
        )
    return img.convert("RGB")


def transparent_lockup(w: int, h: int, lock: str) -> Image.Image:
    """Fit the light-ground lockup inside an exact transparent canvas."""
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    lw, lh = lib.size_for_width(lock, round(w * 0.92))
    if lh > h * 0.82:
        lw, lh = lib.size_for_height(lock, round(h * 0.82))
    lx = (w - lw) // 2
    ly = (h - lh) // 2
    img.alpha_composite(lib.render(lock, lw, lh), (lx, ly))
    return img


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", type=Path, default=ROOT / "exports")
    out: Path = ap.parse_args().out

    cfg = json.loads((ROOT / "config" / "platforms.json").read_text())
    tagline = cfg["tagline"]

    mark = lib.master("loggie-mark.svg")
    wordmark = lib.master("loggie-wordmark.svg")
    mark_dark = lib.recolor(mark, lib.DARK)
    wordmark_dark = lib.recolor(wordmark, lib.DARK)
    lock = lib.lockup(mark, wordmark)
    lock_dark = lib.lockup(mark_dark, wordmark_dark)
    tile_square = lib.tile(mark, rounded=False)
    tile_round = lib.tile(mark, rounded=True)

    manifest: list[dict] = []

    def emit(rel: str, img: Image.Image, purpose: str, source: str) -> None:
        path = out / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        img.save(path, optimize=True)
        manifest.append({
            "path": rel, "width": img.width, "height": img.height,
            "purpose": purpose, "source": source,
        })
        print(f"  {rel:<42} {img.width}x{img.height}  {path.stat().st_size / 1024:.1f} KB")

    def emit_svg(rel: str, svg: str, purpose: str, source: str) -> None:
        path = out / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(svg)
        w, h = (round(v) for v in lib._viewbox(svg))
        manifest.append({
            "path": rel, "width": w, "height": h,
            "purpose": purpose, "source": source,
        })
        print(f"  {rel:<42} svg {w}x{h}")

    for platform, targets in cfg["platforms"].items():
        for name, t in targets.items():
            w, h = t["width"], t["height"]
            kind = t["composition"]["kind"]
            rel = f"{platform}/{name}-{w}x{h}.png"
            purpose = f"{platform} {name}"
            if kind == "tile":
                emit(rel, lib.render(tile_square, w, h).convert("RGB"), purpose, MASTER_MARK)
            elif kind == "tile-rounded":
                emit(rel, lib.render(tile_round, w, h), purpose, MASTER_MARK)
            elif kind == "glyph":
                emit(rel, lib.render(lib.master("loggie-glyph-16.svg"), w, h), purpose, MASTER_GLYPH)
            elif kind == "cover":
                emit(rel, cover(w, h, t["composition"], lock_dark, tagline), purpose, LOCKUP_SOURCES)
            elif kind == "transparent-lockup":
                emit(rel, transparent_lockup(w, h, lock), purpose, LOCKUP_SOURCES)
            elif kind == "share-card":
                emit(rel, lib.share_card(mark_dark, wordmark_dark), purpose, LOCKUP_SOURCES)
            else:
                raise SystemExit(f"unknown composition kind {kind!r} for {platform}/{name}")

    # Press kit: transparent high-resolution marks and lockups, the square
    # icon, and the lockup SVGs (the only composed vectors not in brand/logo/).
    emit("press/loggie-mark-1024.png", lib.render(mark, 1024, 1024),
         "press transparent mark, light grounds", MASTER_MARK)
    emit("press/loggie-mark-dark-1024.png", lib.render(mark_dark, 1024, 1024),
         "press transparent mark, dark grounds", MASTER_MARK)
    emit("press/loggie-lockup-2400.png", lib.render(lock, *lib.size_for_width(lock, 2400)),
         "press lockup, light grounds", LOCKUP_SOURCES)
    emit("press/loggie-lockup-dark-2400.png", lib.render(lock_dark, *lib.size_for_width(lock_dark, 2400)),
         "press lockup, dark grounds", LOCKUP_SOURCES)
    emit("press/loggie-icon-1024.png", lib.render(tile_square, 1024, 1024).convert("RGB"),
         "press square icon tile", MASTER_MARK)
    emit_svg("press/loggie-lockup.svg", lock, "press lockup vector, light grounds", LOCKUP_SOURCES)
    emit_svg("press/loggie-lockup-dark.svg", lock_dark, "press lockup vector, dark grounds", LOCKUP_SOURCES)

    (out / "manifest.json").write_text(json.dumps({
        "generated": date.today().isoformat(),
        "tagline": tagline,
        "assets": manifest,
    }, indent=2) + "\n")
    print(f"\n  {len(manifest)} assets + manifest.json -> {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")


if __name__ == "__main__":
    main()
