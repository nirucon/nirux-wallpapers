# NIRUX wallpapers

Optional 4K and 8K wallpapers for the NIRUX desktop themes, published as verified release assets.

**Status: beta** · Part of the [NIRUX](https://github.com/nirucon/nirux) suite · [Artwork terms](#license)

## About

NIRUX ships only its default **Noir** wallpaper. This repository holds the
wallpapers for the nine other built-in themes and two colour-variant packs for
Carl Larsson and Erik Satie (red, blue, green and noir).

It also holds **NIRUX Signature**: the Noir photograph (photo by Nicklas
Rudolfsson, 2025) toned in each built-in theme's own colours, one 4K picture
per theme. With `theme_style = "signature"` in NIRUWM every theme shows its
Signature picture instead of its own artwork; switch back and forth with
`niructl wallpaper style toggle` or from the theme and wallpaper pickers.

The images are not committed to the Git history. They are published as
[GitHub release assets](https://github.com/nirucon/nirux-wallpapers/releases),
so cloning this repository is small and NIRUX downloads only what you ask for.
The NIRUX installer pins the release, each asset's byte count and its SHA-256
checksum, and refuses anything that does not match. A new wallpaper revision is
always a new release; existing assets are never replaced.

## Features

Release `v1.0.0`; each theme archive contains a 4K and an 8K PNG. Each `-extras`
archive holds four colour variants, 4K and 8K (eight files).

| Asset | Contents |
|---|---|
| `nirux-wallpaper-nord.tar.xz` | Nord, 4K + 8K |
| `nirux-wallpaper-satie.tar.xz` | Erik Satie, 4K + 8K |
| `nirux-wallpaper-carl-larsson.tar.xz` | Carl Larsson, 4K + 8K |
| `nirux-wallpaper-forest-vigil.tar.xz` | Forest Vigil, 4K + 8K |
| `nirux-wallpaper-blood-of-urdr.tar.xz` | Blood of Urðr, 4K + 8K |
| `nirux-wallpaper-root-and-stone.tar.xz` | Root and Stone, 4K + 8K |
| `nirux-wallpaper-blue-horizon.tar.xz` | Blue Horizon, 4K + 8K |
| `nirux-wallpaper-the-norns.tar.xz` | The Norns, 4K + 8K |
| `nirux-wallpaper-winter-nights.tar.xz` | Winter Nights, 4K + 8K |
| `nirux-wallpaper-carl-larsson-extras.tar.xz` | Carl Larsson red, blue, green, noir |
| `nirux-wallpaper-satie-extras.tar.xz` | Erik Satie red, blue, green, noir |

Release `v1.1.0` adds one asset and keeps every `v1.0.0` asset where it is:

| Asset | Contents |
|---|---|
| `nirux-wallpaper-signature.tar.xz` | NIRUX Signature, ten themes, 4K each (about 47 MiB) |

The Signature pictures are made with `tools/make-signature.py` from the 8K Noir
source and NIRUWM's theme palettes: the darker of background and foreground
takes the shadows, the theme accent carries the midtones and the lighter one
the highlights, so light themes stay the right way round and the title stays
readable. A new theme palette only needs the script run again.

Release `v1.2.0` (2026-11-11) replaces seven theme archives with a new style
in the same colours: Nord, Forest Vigil, Blood of Urðr, Root and Stone, Blue
Horizon, The Norns and Winter Nights. Satie, Carl Larsson, the extras and the
Signature pack stay in their earlier releases. NIRUX 0.12.261 and later download
the new pictures on `nirux update` for every theme you already have, and keep a
picture you changed yourself.

`SHA256SUMS` is attached to the release and also committed here. The nine theme
archives are about 375 MiB together; the two extras packs about 254 MiB.

The separate [`nirux-theme-*`](https://github.com/nirucon?tab=repositories&q=nirux-theme)
theme packs carry their own wallpaper and do not use this repository.

## Requirements

- An installed [NIRUX](https://github.com/nirucon/nirux) (it does the download,
  verification and installation).
- About 540 MiB free for everything, less for single themes.

## Installation

### With NIRUX

The installer offers the nine theme wallpapers during `nirux install`. Later,
from a terminal (or the download action under **Wallpaper** in NIRU Launcher):

```sh
nirux wallpapers download themes          # the nine theme wallpapers (default)
nirux wallpapers download theme nord      # one theme
nirux wallpapers download extras          # both colour-variant packs
nirux wallpapers download carl-larsson    # one pack (also: satie)
nirux wallpapers download all             # everything
nirux wallpapers status
```

Theme names for `theme NAME`: `nord`, `satie`, `carl-larsson`, `forest-vigil`,
`blood-of-urdr`, `root-and-stone`, `blue-horizon`, `the-norns`, `winter-nights`.

### Manually

Download an archive and `SHA256SUMS` from the release, then check and unpack it:

```sh
sha256sum --check --ignore-missing SHA256SUMS
tar -xJf nirux-wallpaper-nord.tar.xz
```

## Usage

Choose images in **NIRU Wallpaper** or apply a theme in **NIRU Theme Selector**;
a theme that follows its wallpaper picks up the downloaded image. A theme
without its image simply paints its background colour. Running the download
from an existing session refreshes the active theme; no logout is needed.

## Files and paths

| Path | Purpose |
|---|---|
| `$XDG_PICTURES_DIR/Wallpapers/NIRU/` (usually `~/Pictures/Wallpapers/NIRU/`) | Installed wallpapers; NIRUWM's default `wallpaper.theme_dir` |

More detail, including ownership and removal rules, is in
[NIRUX docs/WALLPAPERS.md](https://github.com/nirucon/nirux/blob/main/docs/WALLPAPERS.md).

## Uninstall

```sh
nirux wallpapers remove
```

This keeps the default Noir images and any files you changed or added yourself.

## Status, disclaimer and how it's made

**Status: beta.** The v1.0.0 assets are complete and verified by NIRUX; new images or revisions will come as new releases.

NIRUX and every niru* project are made by me, Nicklas Rudolfsson
([@nirucon](https://github.com/nirucon)), for me. They are tailored to my own
needs, preferences and workflows, on my own machines. If they fit yours too,
that's a nice bonus.

- **Free to use with NIRUX.** The wallpapers are free to download and use
  with NIRUX. Unlike the code in the rest of the suite they are artwork, not
  open source: see [License](#license).
- **No guarantees.** There is no warranty of any kind. Use it at your own
  risk, read what you install and keep backups of anything that matters.
- **How it's made.** Some of these projects I built from scratch by hand. In
  more recent releases I have used Claude, Anthropic's AI, to do much of the
  heavy lifting under my direction: I decide what to build and how it should
  behave, and I test it on my own machines. It saves me a lot of time, and
  the result is quite OK.
- **Alpha, beta, dev, and maybe forever.** Most things here are alpha, beta
  or dev, and may stay that way. Maybe one day there will be a real stable
  release, but given how fast development moves, and how I am as a person,
  maybe never :)

| Label | Meaning |
|---|---|
| dev | Under active construction; may not build, install or work yet. |
| alpha | Works on my machines, but incomplete or rough; expect breaking changes. |
| beta | In daily use on my machines and mostly complete; rough edges remain. |

## License

Wallpaper artwork © Nicklas Rudolfsson. The assets are published for use with
NIRUX; no separate permission or licence for redistribution is granted unless
stated explicitly. This repository therefore has no open source LICENSE file.
