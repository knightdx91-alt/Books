#!/usr/bin/env python3
"""Generate front-cover CONCEPT MOCKUPS for the Saeren trilogy.

  python3 tools/cover_concepts.py            # all books x all concepts, preview size
  python3 tools/cover_concepts.py --print    # print resolution (2452 x 3469)

Self-contained: the artwork is drawn procedurally (CSS gradients + inline SVG) and
the type is set in real fonts, then the page is rendered by headless Chromium. No
external art, no service. That means a chosen concept can be re-rendered at any
resolution later instead of being stuck at whatever a raster export happened to be.

Three concepts, each applied to all three books so they read as a SET — which is
what actually matters for a trilogy on a shelf. The layout skeleton and type system
are identical across the three; only the emblem and the accent colour change.

  A "Emblem"  full-bleed dark ground, one large luminous emblem, title low.
              Closest to the Scale & Silver treatment.
  B "Arch"    thin double-rule frame, emblem in an arch aperture, restrained
              high-contrast type. The prestige/classic-fantasy direction.
  C "Panel"   type block up top over a lit panel the emblem sits inside.
              The modern literary-trade direction.

Output: delivery-concepts/<concept>-<book>.png plus a lineup sheet per concept.
"""
import base64, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SAEREN = os.path.dirname(HERE)
OUT_DIR = os.path.join(SAEREN, "delivery-concepts")
FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

# Design canvas is 1000 x 1414 CSS px (the 6.125:9.25 cover ratio ~ 1:1.51).
CSS_W, CSS_H = 1000, 1510
PRINT_SCALE = 2.452          # -> 2452 x 3703, above the 1838 x 2775 print floor
PREVIEW_SCALE = 1.0


def b64(name):
    with open(os.path.join(FONT_DIR, name), "rb") as f:
        return base64.b64encode(f.read()).decode()


FONTS = {
    "Young": b64("YoungSerif-Regular.ttf"),
    "Italiana": b64("Italiana-Regular.ttf"),
    "Plex": b64("IBMPlexSerif-Regular.ttf"),
    "PlexIt": b64("IBMPlexSerif-Italic.ttf"),
    "Baskerville": b64("LibreBaskerville-Regular.ttf"),
}

SERIES = "THE SAEREN CHRONICLES"
AUTHOR = "POST PELEOS"

BOOKS = [
    dict(key="book-1", num="BOOK ONE", title="HAZEL\nACADEMY",
         title_flat="HAZEL ACADEMY",
         # cool moon-silver: a school, a secret kept behind a door
         accent="#8FB4D9", accent2="#DCE9F7", ground="#070B14", glow="#5C86BC",
         emblem="keyhole"),
    dict(key="book-2", num="BOOK TWO", title="THE\nRESISTANCE",
         title_flat="THE RESISTANCE",
         # ember through a fracture: the war, the thing breaking open
         accent="#D98A45", accent2="#F2D4A8", ground="#0C0806", glow="#C4551C",
         emblem="fracture"),
    dict(key="book-3", num="BOOK THREE", title="THE WEIGHT\nOF THE SOURCE",
         title_flat="THE WEIGHT OF THE SOURCE",
         # eclipse gold: the source held, the corona around an absence
         accent="#D9B15E", accent2="#F5E6BE", ground="#080706", glow="#B8863A",
         emblem="eclipse"),
]


def emblem_svg(kind, accent, glow, size=520):
    """Procedural emblem. Each is a single luminous form on darkness."""
    if kind == "keyhole":
        return f'''
<svg viewBox="0 0 400 400" width="{size}" height="{size}">
  <defs>
    <radialGradient id="kg" cx="50%" cy="46%" r="50%">
      <stop offset="0%"  stop-color="{glow}" stop-opacity=".95"/>
      <stop offset="42%" stop-color="{glow}" stop-opacity=".34"/>
      <stop offset="100%" stop-color="{glow}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="kf" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity=".97"/>
      <stop offset="60%" stop-color="{accent}" stop-opacity=".92"/>
      <stop offset="100%" stop-color="{accent}" stop-opacity=".55"/>
    </linearGradient>
  </defs>
  <circle cx="200" cy="185" r="195" fill="url(#kg)"/>
  <g fill="url(#kf)">
    <circle cx="200" cy="158" r="52"/>
    <path d="M200 196 L232 292 Q200 306 168 292 Z"/>
  </g>
  <circle cx="200" cy="158" r="52" fill="none" stroke="#FFFFFF" stroke-opacity=".5" stroke-width="1.2"/>
</svg>'''
    if kind == "fracture":
        return f'''
<svg viewBox="0 0 400 400" width="{size}" height="{size}">
  <defs>
    <linearGradient id="fg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"  stop-color="{glow}" stop-opacity="0"/>
      <stop offset="22%" stop-color="{accent}" stop-opacity=".95"/>
      <stop offset="55%" stop-color="#FFF3E0" stop-opacity="1"/>
      <stop offset="82%" stop-color="{accent}" stop-opacity=".9"/>
      <stop offset="100%" stop-color="{glow}" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="fh" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{glow}" stop-opacity=".55"/>
      <stop offset="100%" stop-color="{glow}" stop-opacity="0"/>
    </radialGradient>
    <filter id="fb" x="-60%" y="-20%" width="220%" height="140%">
      <feGaussianBlur stdDeviation="7"/>
    </filter>
  </defs>
  <ellipse cx="200" cy="200" rx="150" ry="200" fill="url(#fh)"/>
  <path d="M203 0 L191 74 L214 132 L186 206 L212 268 L189 330 L200 400"
        stroke="url(#fg)" stroke-width="15" fill="none" filter="url(#fb)"/>
  <path d="M203 0 L191 74 L214 132 L186 206 L212 268 L189 330 L200 400"
        stroke="url(#fg)" stroke-width="3.4" fill="none"/>
  <path d="M196 96 L150 122 M209 168 L252 150 M197 246 L158 276 M210 300 L246 286"
        stroke="{accent}" stroke-opacity=".5" stroke-width="1.6" fill="none"/>
</svg>'''
    # eclipse
    return f'''
<svg viewBox="0 0 400 400" width="{size}" height="{size}">
  <defs>
    <radialGradient id="eo" cx="50%" cy="50%" r="50%">
      <stop offset="0%"  stop-color="{glow}" stop-opacity="0"/>
      <stop offset="33%" stop-color="{glow}" stop-opacity="0"/>
      <stop offset="36%" stop-color="#FFF6DF" stop-opacity=".98"/>
      <stop offset="40%" stop-color="{accent}" stop-opacity=".82"/>
      <stop offset="62%" stop-color="{glow}" stop-opacity=".22"/>
      <stop offset="100%" stop-color="{glow}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="200" cy="200" r="200" fill="url(#eo)"/>
  <circle cx="200" cy="200" r="132" fill="#050403"/>
  <circle cx="200" cy="200" r="132" fill="none" stroke="#FFF6DF" stroke-opacity=".92" stroke-width="2.2"/>
</svg>'''


def page(concept, b):
    """One cover as a self-contained HTML page."""
    faces = "".join(
        f"@font-face{{font-family:'{n}';src:url(data:font/ttf;base64,{d}) format('truetype');}}"
        for n, d in FONTS.items())
    g, acc, acc2, glow = b["ground"], b["accent"], b["accent2"], b["glow"]
    title_html = b["title"].replace("\n", "<br>")

    if concept == "A":      # ---- Emblem: full bleed, big glow, title low ----
        body = f'''
<div class="cover a">
  <div class="vign"></div>
  <div class="emblem">{emblem_svg(b["emblem"], acc, glow, 620)}</div>
  <div class="scrim"></div>
  <div class="top">
    <div class="series">{SERIES}</div>
    <div class="rule"><i></i><b></b><i></i></div>
    <div class="num">{b["num"]}</div>
  </div>
  <div class="bottom">
    <h1 class="disp">{title_html}</h1>
    <div class="rule wide"><i></i><b></b><i></i></div>
    <div class="author">{AUTHOR}</div>
  </div>
</div>'''
        css = f'''
.cover.a{{background:radial-gradient(120% 80% at 50% 34%, #131C2B 0%, {g} 58%, #03060B 100%);}}
.a .emblem{{position:absolute;left:50%;top:38%;transform:translate(-50%,-50%);opacity:.96;}}
.a .scrim{{position:absolute;inset:auto 0 0 0;height:58%;
  background:linear-gradient(180deg,rgba(3,6,11,0) 0%,rgba(3,6,11,.72) 46%,rgba(3,6,11,.96) 100%);}}
.a .top{{position:absolute;left:0;right:0;top:74px;text-align:center;}}
.a .bottom{{position:absolute;left:0;right:0;bottom:112px;text-align:center;}}
.a .disp{{font-family:'Young';font-size:104px;line-height:.99;letter-spacing:.012em;
  background:linear-gradient(180deg,#FFFFFF 0%,{acc2} 42%,{acc} 78%,{glow} 118%);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 6px 22px rgba(0,0,0,.95));}}
.a .author{{margin-top:34px;font-size:31px;letter-spacing:.44em;text-indent:.44em;color:{acc2};}}
.a .series{{font-size:24px;letter-spacing:.5em;text-indent:.5em;color:{acc};opacity:.95;}}
.a .num{{font-size:18px;letter-spacing:.46em;text-indent:.46em;color:#9AA6B8;margin-top:4px;}}'''

    elif concept == "B":    # ---- Arch: framed, aperture, prestige ----
        body = f'''
<div class="cover b">
  <div class="frame"></div>
  <div class="innerframe"></div>
  <div class="arch"><div class="archglow">{emblem_svg(b["emblem"], acc, glow, 420)}</div></div>
  <div class="top">
    <div class="series">{SERIES}</div>
    <div class="num">{b["num"]}</div>
  </div>
  <div class="bottom">
    <div class="rule wide"><i></i><b></b><i></i></div>
    <h1 class="disp">{title_html}</h1>
    <div class="author">{AUTHOR}</div>
  </div>
</div>'''
        css = f'''
.cover.b{{background:linear-gradient(178deg,#10151F 0%,{g} 52%,#04070C 100%);}}
.b .frame{{position:absolute;inset:44px;border:1.6px solid {acc};opacity:.42;}}
.b .innerframe{{position:absolute;inset:54px;border:.9px solid {acc};opacity:.22;}}
.b .arch{{position:absolute;left:50%;top:35%;transform:translate(-50%,-50%);
  width:430px;height:560px;border-radius:215px 215px 10px 10px;overflow:hidden;
  border:1.4px solid rgba(255,255,255,.22);
  background:radial-gradient(80% 60% at 50% 42%, rgba(255,255,255,.07), rgba(0,0,0,0) 70%), #05080E;
  display:flex;align-items:center;justify-content:center;}}
.b .top{{position:absolute;left:0;right:0;top:104px;text-align:center;}}
.b .bottom{{position:absolute;left:0;right:0;bottom:118px;text-align:center;}}
.b .disp{{font-family:'Italiana';font-size:96px;line-height:1.02;letter-spacing:.045em;
  color:{acc2};margin-top:26px;filter:drop-shadow(0 3px 16px rgba(0,0,0,.9));}}
.b .author{{margin-top:36px;font-size:26px;letter-spacing:.42em;text-indent:.42em;color:{acc};}}
.b .series{{font-size:21px;letter-spacing:.52em;text-indent:.52em;color:{acc};opacity:.9;}}
.b .num{{font-size:16px;letter-spacing:.48em;text-indent:.48em;color:#8C97A8;margin-top:8px;}}'''

    else:                   # ---- Panel: type block over a lit emblem panel ----
        body = f'''
<div class="cover c">
  <div class="top">
    <div class="series">{SERIES}</div>
    <div class="num">{b["num"]}</div>
    <h1 class="disp">{title_html}</h1>
  </div>
  <div class="panel">
    <div class="panelglow"></div>
    <div class="emblem">{emblem_svg(b["emblem"], acc, glow, 430)}</div>
    <div class="panelfade"></div>
  </div>
  <div class="bottom"><div class="author">{AUTHOR}</div></div>
</div>'''
        css = f'''
.cover.c{{background:{g};}}
.c .top{{position:absolute;left:0;right:0;top:96px;text-align:center;z-index:3;}}
.c .series{{font-size:21px;letter-spacing:.5em;text-indent:.5em;color:{acc};}}
.c .num{{font-size:15px;letter-spacing:.46em;text-indent:.46em;color:#8B95A6;margin-top:7px;}}
.c .disp{{font-family:'Young';font-size:92px;line-height:1.0;letter-spacing:.008em;
  color:{acc2};margin-top:34px;filter:drop-shadow(0 4px 18px rgba(0,0,0,.9));}}
.c .panel{{position:absolute;left:0;right:0;bottom:0;height:52%;overflow:hidden;
  background:radial-gradient(78% 96% at 50% 62%, #16202F 0%, #080D16 62%, {g} 100%);
  border-top:1px solid {acc}55;}}
.c .panelglow{{position:absolute;inset:0;
  background:radial-gradient(52% 58% at 50% 56%, {glow}44 0%, rgba(0,0,0,0) 72%);}}
.c .emblem{{position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);}}
.c .panelfade{{position:absolute;inset:auto 0 0 0;height:34%;
  background:linear-gradient(180deg,rgba(5,8,13,0),rgba(5,8,13,.92));}}
.c .bottom{{position:absolute;left:0;right:0;bottom:74px;text-align:center;z-index:3;}}
.c .author{{font-size:28px;letter-spacing:.44em;text-indent:.44em;color:{acc2};}}'''

    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
{faces}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{CSS_W}px;height:{CSS_H}px;background:#000;}}
.cover{{position:relative;width:{CSS_W}px;height:{CSS_H}px;overflow:hidden;
  font-family:'Plex',serif;color:#fff;}}
.vign{{position:absolute;inset:0;box-shadow:inset 0 0 240px 90px rgba(0,0,0,.85);}}
.rule{{display:flex;align-items:center;justify-content:center;gap:14px;margin:18px auto 0;width:230px;}}
.rule.wide{{width:420px;margin-top:30px;}}
.rule i{{height:1px;flex:1;background:linear-gradient(90deg,rgba(220,230,245,0),rgba(220,230,245,.7));}}
.rule i:last-child{{background:linear-gradient(90deg,rgba(220,230,245,.7),rgba(220,230,245,0));}}
.rule b{{width:7px;height:7px;transform:rotate(45deg);background:{acc2};}}
h1{{font-weight:400;text-transform:uppercase;}}
{css}
</style></head><body>{body}</body></html>'''


def render(html, out, scale):
    """Render and crop to the exact cover box.

    Chromium's layout viewport comes out shorter than --window-size here, which
    silently clipped the bottom ~8% of the first pass (it ate the frame on the
    arch concept). So render with headroom and crop back to the real box.
    """
    from PIL import Image
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html); path = f.name
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu",
                    "--hide-scrollbars", f"--force-device-scale-factor={scale}",
                    f"--window-size={CSS_W},{CSS_H + 300}", f"--screenshot={out}",
                    f"file://{path}"], capture_output=True)
    os.unlink(path)
    im = Image.open(out)
    box = (round(CSS_W * scale), round(CSS_H * scale))
    if im.size != box:
        im.crop((0, 0, *box)).save(out)
    return out


def lineup(paths, out):
    """Three books side by side — the only honest way to judge a series look."""
    from PIL import Image
    ims = [Image.open(p).convert("RGB") for p in paths]
    h = 900
    ims = [im.resize((round(im.width * h / im.height), h), Image.LANCZOS) for im in ims]
    gap, pad = 34, 44
    W = sum(i.width for i in ims) + gap * (len(ims) - 1) + pad * 2
    sheet = Image.new("RGB", (W, h + pad * 2), "#141414")
    x = pad
    for im in ims:
        sheet.paste(im, (x, pad)); x += im.width + gap
    sheet.save(out)
    return out


if __name__ == "__main__":
    scale = PRINT_SCALE if "--print" in sys.argv else PREVIEW_SCALE
    os.makedirs(OUT_DIR, exist_ok=True)
    for concept in ("A", "B", "C"):
        made = []
        for b in BOOKS:
            out = os.path.join(OUT_DIR, f"concept-{concept}-{b['key']}.png")
            render(page(concept, b), out, scale)
            made.append(out)
            print("wrote", os.path.relpath(out, SAEREN))
        sheet = lineup(made, os.path.join(OUT_DIR, f"concept-{concept}-LINEUP.png"))
        print("wrote", os.path.relpath(sheet, SAEREN))
