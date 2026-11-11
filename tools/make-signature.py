#!/usr/bin/env python3
"""Make the NIRUX Signature wallpapers: one photograph, toned per theme.

The source is the black-and-white NIRUX Noir picture (8K PNG). Every built-in
theme gets the same picture mapped through its own palette:

- the darker of the theme's background and foreground takes the shadows,
- the theme accent (focus) carries the midtones, blended with its muted
  colour so the picture stays calm,
- the lighter of the two takes the highlights, with a faint pull towards the
  accent.

Ordering the stops by lightness instead of by role keeps light themes (Carl
Larsson) the right way round, and keeps the black "NIRUX" title dark on a
light sky in every theme.

    python3 tools/make-signature.py SOURCE-8K.png THEMES-DIR OUT-DIR

THEMES-DIR holds niru-*.toml (NIRUWM's themes/ directory). Output:
nirux-wallpaper-signature-<theme>-4k.png, 3840x2160. Needs Pillow.
"""
import pathlib
import re
import sys

from PIL import Image

Image.MAX_IMAGE_PIXELS = None


def palette(path):
    colours = {}
    for line in path.read_text().splitlines():
        m = re.match(r'\s*(\w+)\s*=\s*"?#?([0-9a-fA-F]{6})"?', line)
        if m:
            colours[m.group(1)] = tuple(int(m.group(2)[i:i + 2], 16) for i in (0, 2, 4))
    return colours


def lum(c):
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def mix(a, b, t):
    return tuple(round(x + (y - x) * t) for x, y in zip(a, b))


def stops(p):
    bg, fg = p["background"], p["foreground"]
    dark, light = (bg, fg) if lum(bg) <= lum(fg) else (fg, bg)
    accent = p.get("focus", p.get("muted", fg))
    muted = p.get("muted", accent)
    mid = mix(accent, muted, 0.45)
    return [
        (0.00, dark),
        (0.30, mix(dark, accent, 0.35)),
        (0.58, mid),
        (0.84, mix(light, accent, 0.16)),
        (1.00, light),
    ]


def lut(points):
    """A 256-entry colour table through the stops, per channel."""
    table = []
    for i in range(256):
        x = i / 255
        for (x0, c0), (x1, c1) in zip(points, points[1:]):
            if x0 <= x <= x1:
                t = (x - x0) / (x1 - x0) if x1 > x0 else 0
                table.append(mix(c0, c1, t))
                break
    return table


def main():
    source, themes_dir, out_dir = map(pathlib.Path, sys.argv[1:4])
    out_dir.mkdir(parents=True, exist_ok=True)
    grey = Image.open(source).convert("L").resize((3840, 2160), Image.LANCZOS)
    for theme in sorted(themes_dir.glob("niru-*.toml")):
        slug = theme.stem.removeprefix("niru-")
        table = lut(stops(palette(theme)))
        r = grey.point([c[0] for c in table])
        g = grey.point([c[1] for c in table])
        b = grey.point([c[2] for c in table])
        out = out_dir / f"nirux-wallpaper-signature-{slug}-4k.png"
        Image.merge("RGB", (r, g, b)).save(out, optimize=True)
        print(out.name)


if __name__ == "__main__":
    main()
