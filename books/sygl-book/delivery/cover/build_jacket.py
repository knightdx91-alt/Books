#!/usr/bin/env python3
"""Dust jacket for the Sygl 6x9 hardcover (Blue Digital Cloth w/Jacket, creme, 298 pp).

Geometry is taken from IngramSpark's own jacket template for ISBN 979-8-1829-5940-7
(Request ID CSS5486494, "Dust Jacket Cover Template", document 24 x 12.5 in):
  bleed artwork 20.938 x 9.50 in, placed at x 2.5625 / y 0.5 on the 24 x 12.5 page;
  left to right: back flap 3.25 | wrap .25 | back 6.438 | spine .813 | front 6.438 | wrap .25 | front flap 3.25;
  panels 9.25 tall; 0.125 bleed all round; pink safe area = 0.125 inside each trim edge.
The output page is the template's full 24 x 12.5 in (IngramSpark: the PDF must match the document size).

  python3 books/sygl-book/delivery/cover/build_jacket.py
  -> Sygl-6x9-hardcover-JACKET.pdf (RGB proof); then make_noicc.sh cmyk for the upload copy.
"""
import base64, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
ISBN = "979-8-1829-5940-7"
OUT = os.path.join(HERE, "Sygl-6x9-hardcover-JACKET.pdf")

def b64(p): return base64.b64encode(open(p, "rb").read()).decode()

# --- geometry (inches, page coordinates) --------------------------------------
PAGE_W, PAGE_H = 24.0, 12.5
BX, BY, BW, BH = 2.5625, 0.5, 20.938, 9.5            # bleed artwork box
TX, TY, TH = BX + 0.125, BY + 0.125, 9.25            # trim origin + panel height
FLAP, WRAP, PANEL, SPINE = 3.25, 0.25, 6.438, 0.813
x_bflap = TX
x_back = x_bflap + FLAP + WRAP
x_spine = x_back + PANEL
x_front = x_spine + SPINE
x_fflap = x_front + PANEL + WRAP
SAFE = 0.125

art = b64(os.path.join(HERE, "front-art-canva-A.png"))
young = b64(f"{FONT_DIR}/YoungSerif-Regular.ttf")
plex = b64(f"{FONT_DIR}/IBMPlexSerif-Regular.ttf")
plexi = b64(f"{FONT_DIR}/IBMPlexSerif-Italic.ttf")
plexb = b64(f"{FONT_DIR}/IBMPlexSerif-Bold.ttf")

# EAN-13 (python-barcode, SVG), no price add-on.
import barcode
from barcode.writer import SVGWriter
ean_path = os.path.join(HERE, "_ean")
barcode.get("ean13", ISBN.replace("-", ""), writer=SVGWriter()).save(
    ean_path, options={"module_width": 0.33, "module_height": 18.0, "font_size": 8,
                       "text_distance": 4, "quiet_zone": 3.5, "background": "white",
                       "foreground": "black"})
ean = b64(ean_path + ".svg")
os.remove(ean_path + ".svg")

BACK_COPY = [
    ("hook", "Nobody claims a boy born with the Blood sygl."),
    ("para", "Bal Norheart lost his left hand for it before he could crawl. No sygl, no school. That was the rule."),
    ("para", "Then the sealed temple behind his orphanage flickers. Bal flies a bedside rug through a roof that isn&#8217;t there, and finds Amelia: the Vampire Goddess, locked away by the other gods for three thousand years and furious to learn the world calls her a myth."),
    ("para", "One drink of her blood, and Bal has a hand again. One binding vow, and the goddess is his familiar. She walks out the front door beside him, straight into the Heir&#8217;s School of Magykal Artes and the empty throne the gods kept for her."),
    ("para", "Now Bal is the school&#8217;s only Blood student, the High Priest of a goddess everyone fears, and the one mage alive who can change a person&#8217;s sygl. He can do it only if they want it. Viridia, the storm-haired heir of the god Raizen, and Lora, the shy rapier prodigy, are starting to want a great many things."),
    ("para", "And the god Raizen does not share what is his."),
    ("closing", "The gods play with their followers like toys. Amelia has a better idea: play their game, and break their toys."),
    ("note", "Closed-door romance. All romantic leads are 18+."),
]
FRONT_FLAP = [
    ("fhook", "They locked her away for three thousand years. Now she&#8217;s free."),
    ("fpara", "Bal Norheart was born with the Blood sygl, the one mark nobody wants, and lost his left hand for it before he could crawl. No sygl means no magic school."),
    ("fpara", "Then the sealed temple behind his orphanage flickers, and Bal finds Amelia: originator of the Blood, betrayed by the other gods, and outraged to learn the world now calls her a myth. One drink of her blood regrows his hand. One vow makes the goddess his familiar."),
    ("fpara", "Together they walk into the Heir&#8217;s School of Magykal Artes, where being the only Blood student is dangerous, and where two very different girls are about to change everything."),
    ("fpara", "When the gods&#8217; war comes for the people Bal loves, he has to decide what kind of High Priest he will be."),
    ("fclose", "A warm new adult fantasy of found family, forbidden magic and a love big enough&#160;for&#160;four."),
]
BACK_FLAP = [
    ("bhead", "ALSO BY SØREN STROMBERG"),
    ("btitle", "<i>A Bond of Scale and Silver</i>"),
    ("bnote", "(adult romantasy, explicit)"),
    ("bhead", "WRITING AS POST PELEOS"),
    ("bnote", "The Saeren Chronicles (young adult fantasy)"),
    ("btitle", "<i>Hazel Academy</i>"),
    ("btitle", "<i>The Resistance</i>"),
    ("btitle", "<i>The Weight of the Source</i>"),
]

def blocks(items):
    return "\n".join(f'<p class="{c}">{t}</p>' for c, t in items)

css = f"""
@font-face{{font-family:'Young';src:url(data:font/ttf;base64,{young}) format('truetype');}}
@font-face{{font-family:'Plex';src:url(data:font/ttf;base64,{plex}) format('truetype');}}
@font-face{{font-family:'PlexI';src:url(data:font/ttf;base64,{plexi}) format('truetype');}}
@font-face{{font-family:'PlexB';src:url(data:font/ttf;base64,{plexb}) format('truetype');}}
@page{{size:{PAGE_W}in {PAGE_H}in;margin:0;}}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
html,body{{width:{PAGE_W}in;height:{PAGE_H}in;background:#fff;}}
.abs{{position:absolute;}}
.bleed{{left:{BX}in;top:{BY}in;width:{BW}in;height:{BH}in;background:#070405;overflow:hidden;}}
.glow{{left:{BX}in;top:{BY}in;width:{BW}in;height:{BH}in;
  background:radial-gradient(ellipse 30% 28% at 47% 100%,rgba(150,44,20,.20) 0%,rgba(0,0,0,0) 100%);}}
.frontart{{left:{x_front}in;top:{BY}in;width:{PANEL + WRAP}in;height:{BH}in;
  background:url(data:image/png;base64,{art}) 50% 38%/cover no-repeat;}}
.fshade{{left:{x_front}in;top:{BY}in;width:{PANEL + WRAP}in;height:{BH}in;
  background:linear-gradient(180deg,rgba(7,4,5,.88) 0%,rgba(7,4,5,.35) 14%,rgba(7,4,5,0) 26%,rgba(7,4,5,0) 52%,rgba(7,4,5,.55) 72%,rgba(7,4,5,.93) 100%),
             radial-gradient(ellipse 70% 30% at 50% 90%,rgba(170,52,24,.30) 0%,rgba(0,0,0,0) 100%);}}
.fedge{{left:{x_front - 0.06}in;top:{BY}in;width:0.5in;height:{BH}in;
  background:linear-gradient(90deg,#070405 0%,rgba(7,4,5,0) 100%);}}
.tag{{left:{x_front}in;width:{PANEL}in;top:{TY + 0.42}in;text-align:center;font-family:'PlexI';font-size:15pt;
  color:#e8d3b4;filter:drop-shadow(0 1pt 4pt rgba(0,0,0,.95));}}
.tag2{{margin-top:3pt;font-size:17pt;color:#e0473f;}}
.ttl{{left:{x_front}in;width:{PANEL}in;top:{TY + 6.25}in;text-align:center;font-family:'Young';font-size:96pt;line-height:1;
  letter-spacing:.14em;text-indent:.14em;
  background:linear-gradient(180deg,#fff3d6 0%,#f0cf86 34%,#d39a45 58%,#b8312a 92%,#8e1418 120%);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 2pt 6pt rgba(0,0,0,.95));}}
.div{{left:{x_front + PANEL/2 - 1.0}in;width:2.0in;top:{TY + 7.72}in;display:flex;align-items:center;gap:7pt;}}
.div .ln{{height:1pt;flex:1;background:linear-gradient(90deg,rgba(214,170,100,0),rgba(214,170,100,.85));}}
.div .ln.r{{background:linear-gradient(90deg,rgba(214,170,100,.85),rgba(214,170,100,0));}}
.div .dot{{width:4pt;height:4pt;transform:rotate(45deg);background:#c8212a;}}
.auth{{left:{x_front}in;width:{PANEL}in;top:{TY + 8.48}in;text-align:center;font-family:'Plex';font-size:18pt;
  letter-spacing:.34em;text-indent:.34em;color:#f1e6d6;filter:drop-shadow(0 1pt 4pt rgba(0,0,0,.95));}}
.spine{{left:{x_spine}in;top:{TY}in;width:{SPINE}in;height:{TH}in;display:flex;flex-direction:column;align-items:center;}}
.spine .st{{writing-mode:vertical-rl;font-family:'Young';font-size:30pt;letter-spacing:.14em;margin-top:0.55in;color:#e2b56a;}}
.spine .sa{{writing-mode:vertical-rl;font-family:'Plex';font-size:11pt;letter-spacing:.24em;color:#f1e6d6;margin-top:auto;margin-bottom:0.62in;}}
.spine .dot{{width:4pt;height:4pt;transform:rotate(45deg);background:#c8212a;margin:0.28in 0;}}
.spine .imp{{font-family:'Plex';font-size:6.5pt;letter-spacing:.12em;color:#d6aa64;text-align:center;line-height:1.25;margin-bottom:0.2in;}}
.back{{left:{x_back + 0.45}in;top:{TY + 0.55}in;width:{PANEL - 0.9}in;color:#d8c4ad;font-family:'Plex';}}
.back .hook{{font-family:'PlexI';font-weight:bold;font-size:14.5pt;color:#f1e6d6;text-align:center;margin-bottom:12pt;}}
.back .para{{font-size:10.6pt;line-height:15.2pt;margin-bottom:8pt;text-align:left;}}
.back .closing{{font-family:'PlexI';font-size:10.6pt;line-height:15pt;color:#f1e6d6;text-align:center;margin:6pt 0 9pt;}}
.back .note{{font-family:'PlexB';font-size:9.2pt;color:#d6aa64;text-align:center;}}
.bc{{left:{x_back + PANEL - SAFE - 0.3 - 1.7}in;top:{TY + TH - SAFE - 0.3 - 1.22}in;width:1.7in;height:1.22in;background:#fff;
  display:flex;flex-direction:column;align-items:center;justify-content:center;padding-top:2pt;}}
.bc .isbn{{font-family:'Plex';font-size:7pt;color:#000;letter-spacing:.04em;}}
.bc img{{width:1.51in;height:1.0in;}}
.fflap{{left:{x_fflap + 0.32}in;top:{TY + 0.75}in;width:{FLAP - 0.64}in;color:#d8c4ad;font-family:'Plex';}}
.fflap .fhook{{font-family:'PlexI';font-size:11.5pt;line-height:15pt;color:#e0473f;text-align:center;margin-bottom:12pt;}}
.fflap .fpara{{font-size:9.6pt;line-height:13.6pt;margin-bottom:8pt;}}
.fflap .fclose{{font-family:'PlexI';font-size:9.6pt;line-height:13.4pt;color:#f1e6d6;text-align:center;margin-top:8pt;}}
.bflap{{left:{x_bflap + 0.32}in;top:{TY + 0.75}in;width:{FLAP - 0.64}in;color:#d8c4ad;font-family:'Plex';text-align:center;}}
.bflap .bname{{font-family:'Plex';font-size:11pt;letter-spacing:.3em;text-indent:.3em;color:#f1e6d6;margin-bottom:12pt;}}
.bflap .bpara{{font-size:9.6pt;line-height:13.6pt;}}
.bflap .bhead{{font-family:'Plex';font-size:8pt;letter-spacing:.22em;text-indent:.22em;color:#d6aa64;margin:22pt 0 7pt;}}
.bflap .btitle{{font-family:'PlexI';font-size:10.5pt;line-height:15pt;color:#f1e6d6;}}
.bflap .bnote{{font-size:8.6pt;line-height:12.5pt;color:#d8c4ad;margin-bottom:3pt;}}
.bimp{{left:{x_bflap}in;width:{FLAP}in;top:{TY + TH - 0.85}in;text-align:center;font-family:'Plex';font-size:8pt;letter-spacing:.24em;text-indent:.24em;color:#d6aa64;}}
.fold{{top:{BY}in;width:0;height:{BH}in;border-left:0.6pt solid rgba(214,170,100,.0);}}
"""
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="abs bleed"></div><div class="abs glow"></div>
<div class="abs frontart"></div><div class="abs fshade"></div><div class="abs fedge"></div>
<div class="abs tag">They locked her away for three thousand years.<div class="tag2">Now she&#8217;s free.</div></div>
<div class="abs ttl">SYGL</div>
<div class="abs div"><span class="ln"></span><span class="dot"></span><span class="ln r"></span></div>
<div class="abs auth">SØREN STROMBERG</div>
<div class="abs spine"><div class="st">SYGL</div><div class="dot"></div><div class="sa">SØREN STROMBERG</div><div class="imp">UNDERGROUND<br/>ASSOCIATES</div></div>
<div class="abs back">{blocks(BACK_COPY)}</div>
<div class="abs bc"><div class="isbn">ISBN {ISBN}</div><img src="data:image/svg+xml;base64,{ean}"/></div>
<div class="abs fflap">{blocks(FRONT_FLAP)}</div>
<div class="abs bflap">{blocks(BACK_FLAP)}</div>
<div class="abs bimp">UNDERGROUND ASSOCIATES</div>
</body></html>"""
hp = os.path.join(HERE, "_jacket.html")
open(hp, "w").write(html)
subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                "--print-to-pdf-no-header", f"--print-to-pdf={OUT}", f"file://{hp}"], capture_output=True)
os.remove(hp)
print("wrote", OUT)
