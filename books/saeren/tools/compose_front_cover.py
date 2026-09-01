#!/usr/bin/env python3
"""Composite series typography over a cover ART BED to make a finished front cover.

  python3 tools/compose_front_cover.py book-1 delivery-concepts/art/<art>.png

This is the Scale & Silver workflow, generalised: the ART comes from outside
(Canva, a commissioned illustrator, stock), and the TYPE is set here in real fonts
so it is sharp, consistent across the trilogy, and re-renderable at any size.

Two things happen before the type goes on:
  1. a warm grade, because generated night art trends blue/teal and the Saeren
     palette is deliberately green-black + amber (the adult Stromberg line owns
     the blue/silver look — the trilogy must not read as the same series);
  2. a bottom scrim, so the title sits on darkness rather than on cobblestone.
"""
import base64, os, subprocess, sys, tempfile
from PIL import Image, ImageEnhance
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SAEREN = os.path.dirname(HERE)
FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
CSS_W, CSS_H = 1000, 1500

SERIES = "THE SAEREN CHRONICLES"
AUTHOR = "POST PELEOS"
BOOKS = {
    "book-1": dict(num="BOOK ONE", title="HAZEL<br>ACADEMY"),
    "book-2": dict(num="BOOK TWO", title="THE<br>RESISTANCE"),
    "book-3": dict(num="BOOK THREE", title="THE WEIGHT<br>OF THE SOURCE"),
}


def warm_grade(im, strength=0.55):
    """Pull the blue cast out of the night and push it green-amber."""
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    lum = a.mean(2, keepdims=True) / 255.0
    mid = np.clip(1.0 - np.abs(lum - 0.45) * 2.2, 0, 1)      # act on midtones
    a[..., 0] += 26 * strength * mid[..., 0]                  # R up
    a[..., 1] += 12 * strength * mid[..., 0]                  # G up a little
    a[..., 2] -= 30 * strength * mid[..., 0]                  # B down
    out = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    return ImageEnhance.Color(out).enhance(1.06)


def lift(im, gamma=0.62, black=10):
    """Open the shadows without washing out the highlights.

    The raw night art measures ~15% mean luminance with only ~1.6% of pixels
    above 128 — too dark to survive a 160px retailer thumbnail, and ~85% ink
    coverage, which plugs up on cream stock. This lifts the low end on a curve
    so the mood stays but the detail comes back.
    """
    a = np.asarray(im.convert("RGB")).astype(np.float32) / 255.0
    a = np.clip((a ** gamma) + black / 255.0, 0, 1)
    return Image.fromarray((a * 255).astype(np.uint8))


def scrim(im, height=0.42, power=2.1):
    """Darken the bottom so type reads, without flattening the whole image."""
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    h = a.shape[0]
    y0 = int(h * (1 - height))
    t = np.linspace(0, 1, h - y0) ** power
    a[y0:] *= (1 - 0.86 * t)[:, None, None]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def b64(name):
    with open(os.path.join(FONT_DIR, name), "rb") as f:
        return base64.b64encode(f.read()).decode()


def build_html(book, art_path):
    b = BOOKS[book]
    art = base64.b64encode(open(art_path, "rb").read()).decode()
    gloock, plex = b64("Gloock-Regular.ttf"), b64("IBMPlexSerif-Regular.ttf")
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Gloock';src:url(data:font/ttf;base64,{gloock}) format('truetype');}}
@font-face{{font-family:'Plex';src:url(data:font/ttf;base64,{plex}) format('truetype');}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{CSS_W}px;height:{CSS_H}px;background:#000;}}
.c{{position:relative;width:{CSS_W}px;height:{CSS_H}px;overflow:hidden;font-family:'Plex',serif;
   background:url(data:image/png;base64,{art}) center/cover no-repeat;}}
.top{{position:absolute;left:0;right:0;top:62px;text-align:center;}}
.series{{font-size:25px;letter-spacing:.52em;text-indent:.52em;color:#FFF6E2;
  text-shadow:0 2px 10px rgba(0,0,0,1),0 0 26px rgba(0,0,0,.9);}}
.num{{margin-top:10px;font-size:16px;letter-spacing:.48em;text-indent:.48em;color:#E9DCBC;
  text-shadow:0 2px 10px rgba(0,0,0,1),0 0 22px rgba(0,0,0,.9);}}
.bot{{position:absolute;left:0;right:0;bottom:78px;text-align:center;}}
h1{{font-family:'Gloock';font-weight:400;font-size:96px;line-height:1.0;text-transform:uppercase;
  letter-spacing:.012em;
  background:linear-gradient(180deg,#FFF8E6 0%,#F0DCAC 44%,#D9B36A 78%,#B8863A 112%);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 5px 20px rgba(0,0,0,.98));}}
.rule{{display:flex;align-items:center;justify-content:center;gap:16px;width:400px;margin:30px auto 0;}}
.rule i{{height:1px;flex:1;background:linear-gradient(90deg,rgba(228,214,174,0),rgba(228,214,174,.75));}}
.rule i:last-child{{background:linear-gradient(90deg,rgba(228,214,174,.75),rgba(228,214,174,0));}}
.rule b{{width:7px;height:7px;transform:rotate(45deg);background:#E8D6AE;}}
.author{{margin-top:28px;font-size:29px;letter-spacing:.44em;text-indent:.44em;color:#F0E2C0;
  text-shadow:0 2px 16px rgba(0,0,0,.98);}}
</style></head><body>
<div class="c">
  <div class="top"><div class="series">{SERIES}</div><div class="num">{b["num"]}</div></div>
  <div class="bot"><h1>{b["title"]}</h1>
    <div class="rule"><i></i><b></b><i></i></div>
    <div class="author">{AUTHOR}</div></div>
</div></body></html>'''


def main(book, art_path, scale=1.0):
    prepped = os.path.join(tempfile.gettempdir(), f"_bed_{book}.png")
    im = Image.open(art_path).convert("RGB").resize((CSS_W, CSS_H), Image.LANCZOS)
    scrim(lift(warm_grade(im)), height=0.38, power=2.4).save(prepped)

    out_dir = os.path.join(SAEREN, "delivery-concepts")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, f"front-{book}.png")
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(build_html(book, prepped)); path = f.name
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    f"--force-device-scale-factor={scale}",
                    f"--window-size={CSS_W},{CSS_H + 300}",
                    f"--screenshot={out}", f"file://{path}"], capture_output=True)
    os.unlink(path); os.unlink(prepped)
    box = (round(CSS_W * scale), round(CSS_H * scale))
    img = Image.open(out)
    if img.size != box:
        img.crop((0, 0, *box)).save(out)
    print("wrote", out)
    return out


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("usage: compose_front_cover.py <book-1|book-2|book-3> <art.png> [--print]")
    main(sys.argv[1], sys.argv[2], 2.452 if "--print" in sys.argv else 1.0)
