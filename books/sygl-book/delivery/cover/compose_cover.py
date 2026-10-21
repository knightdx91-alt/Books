#!/usr/bin/env python3
"""Composite the title over the clean Canva art for 'Sygl' (Option A: Amelia before the golden doors).
Same type system as the other Søren Stromberg title (A Bond of Scale and Silver): Young Serif title,
IBM Plex Serif tagline/author, wide-spaced author line, diamond divider. Palette: gold-to-crimson title."""
import base64, os, subprocess
from PIL import Image

AUTHOR = "SØREN STROMBERG"
TAGLINE = "They locked her away for three thousand years."
TAGLINE2 = "Now she’s free."
OUTNAME = "front-cover-sygl.png"          # 1600 x 2560 (5:8, ebook + print front panel)
HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"
def b64(p): return base64.b64encode(open(p, "rb").read()).decode()
art = b64(os.path.join(HERE, "front-art-canva-A.png"))     # clean Canva art, no text
young = b64(f"{FONT_DIR}/YoungSerif-Regular.ttf")
plex = b64(f"{FONT_DIR}/IBMPlexSerif-Regular.ttf")
plexi = b64(f"{FONT_DIR}/IBMPlexSerif-Italic.ttf")

W, H = 1600, 2560
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Young';src:url(data:font/ttf;base64,{young}) format('truetype');}}
@font-face{{font-family:'Plex';src:url(data:font/ttf;base64,{plex}) format('truetype');}}
@font-face{{font-family:'PlexI';src:url(data:font/ttf;base64,{plexi}) format('truetype');}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;background:#070405;}}
.cover{{position:relative;width:{W}px;height:{H}px;overflow:hidden;
  background:url(data:image/png;base64,{art}) center top/cover no-repeat;}}
.top{{position:absolute;left:0;right:0;top:0;height:520px;
  background:linear-gradient(180deg,rgba(7,4,5,.85) 0%,rgba(7,4,5,.45) 55%,rgba(7,4,5,0) 100%);}}
.scrim{{position:absolute;left:0;right:0;bottom:0;height:1150px;
  background:linear-gradient(180deg,rgba(7,4,5,0) 0%,rgba(7,4,5,.45) 30%,rgba(7,4,5,.82) 58%,rgba(7,4,5,.94) 100%);}}
.tag{{position:absolute;left:0;right:0;top:120px;text-align:center;font-family:'PlexI';font-size:50px;
  color:#e8d3b4;letter-spacing:.01em;filter:drop-shadow(0 3px 12px rgba(0,0,0,.95));}}

.tag2{{margin-top:14px;font-family:'PlexI';font-size:58px;color:#e0473f;}}
.titleblock{{position:absolute;left:0;right:0;top:1690px;text-align:center;}}
.main{{font-family:'Young';font-size:330px;line-height:1;letter-spacing:.14em;text-indent:.14em;text-transform:uppercase;
  background:linear-gradient(180deg,#fff3d6 0%,#f0cf86 34%,#d39a45 58%,#b8312a 92%,#8e1418 120%);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 6px 20px rgba(0,0,0,.95));}}
.divider{{display:flex;align-items:center;justify-content:center;gap:22px;margin:34px auto 0;width:560px;}}
.divider .ln{{height:2px;flex:1;background:linear-gradient(90deg,rgba(214,170,100,0),rgba(214,170,100,.85));}}
.divider .ln.r{{background:linear-gradient(90deg,rgba(214,170,100,.85),rgba(214,170,100,0));}}
.divider .dot{{width:12px;height:12px;transform:rotate(45deg);background:#c8212a;box-shadow:0 0 14px rgba(200,33,42,.8);}}
.book{{margin-top:26px;font-family:'Plex';font-size:36px;letter-spacing:.5em;text-indent:.5em;color:#d6aa64;
  filter:drop-shadow(0 2px 10px rgba(0,0,0,.95));}}
.author{{position:absolute;left:0;right:0;bottom:120px;text-align:center;font-family:'Plex';
  letter-spacing:.34em;text-indent:.34em;font-size:62px;color:#f1e6d6;text-transform:uppercase;
  filter:drop-shadow(0 3px 14px rgba(0,0,0,.95));}}
</style></head><body>
<div class="cover">
  <div class="top"></div><div class="scrim"></div>
  <div class="tag">{TAGLINE}<div class="tag2">{TAGLINE2}</div></div>
  <div class="titleblock">
    <div class="main">Sygl</div>
    <div class="divider"><span class="ln"></span><span class="dot"></span><span class="ln r"></span></div>
    <div class="book">BOOK ONE</div>
  </div>
  <div class="author">{AUTHOR}</div>
</div></body></html>'''
html_path = os.path.join(HERE, "compose.html")
open(html_path, "w").write(html)

# Render with headroom, then crop to the exact box (Chromium's viewport comes out short otherwise).
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
for scale, out in ((1, OUTNAME), (2, OUTNAME.replace(".png", "-2x.png"))):
    dst = os.path.join(HERE, out)
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    f"--force-device-scale-factor={scale}", f"--window-size={W},{H + 300}",
                    f"--screenshot={dst}", f"file://{html_path}"], capture_output=True)
    im = Image.open(dst)
    if im.size != (W * scale, H * scale):
        im.crop((0, 0, W * scale, H * scale)).save(dst)
    print("wrote", out, Image.open(dst).size)
# Ebook listing JPG (RGB, 1600 x 2560).
Image.open(os.path.join(HERE, OUTNAME)).convert("RGB").save(os.path.join(HERE, "ebook-cover-sygl.jpg"), quality=92)
print("wrote ebook-cover-sygl.jpg")
