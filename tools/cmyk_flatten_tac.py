#!/usr/bin/env python3
"""cmyk_flatten_tac.py — flatten a cover PDF to a 300 ppi CMYK image PDF with a hard
total-ink (TAC) ceiling, no ICC profile.

Why: Ghostscript's RGB->CMYK conversion turns dark cover art into rich black at ~300%
total ink; IngramSpark's limit is 240% (default cap here 225%: the JPEG encoding can add ~10 points). Browser-
rendered covers (gradients, drop shadows) also leave RGB transparency groups that a
plain Ghostscript pdfwrite pass keeps as DeviceRGB; flattening to one raster removes them.

Method: Ghostscript separates the flattened page to CMYK (its normal, colour-faithful
conversion); then, only where total ink exceeds the cap, the shared grey of C/M/Y is
moved into K (grey-component replacement — visually neutral), and C/M/Y are scaled
down only if that is not enough. Colours below the cap are untouched.

    python3 tools/cmyk_flatten_tac.py <in.pdf> <out-CMYK-noicc.pdf> [--tac 225] [--dpi 300]

Then verify:  python3 tools/check_upload_pdf.py cover <out.pdf>
"""
import argparse, os, subprocess, tempfile
import numpy as np
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--tac", type=float, default=225.0)
ap.add_argument("--dpi", type=int, default=300)
a = ap.parse_args()

with tempfile.TemporaryDirectory() as td:
    tif = os.path.join(td, "sep.tif")
    subprocess.run(["gs", "-q", "-dNOPAUSE", "-dBATCH", "-dSAFER", "-sDEVICE=tiff32nc",
                    f"-r{a.dpi}", "-dTextAlphaBits=4", "-dGraphicsAlphaBits=4",
                    f"-sOutputFile={tif}", a.src], check=True)
    cmyk = np.asarray(Image.open(tif)).astype(np.float32) / 255.0

c, m, y, k = (cmyk[..., i] for i in range(4))
cap = a.tac / 100.0
tot = c + m + y + k
excess = np.maximum(tot - cap, 0)
# GCR: moving d of grey from C,M,Y into K lowers total by 2d.
g = np.minimum(np.minimum(c, m), y)
d = np.minimum(np.minimum(excess / 2, g), 1 - k)
c, m, y, k = c - d, m - d, y - d, k + d
# Still over (saturated colours with no grey to move): scale C/M/Y.
cmy = c + m + y
over = (cmy + k) > cap
s = np.where(over & (cmy > 0), np.clip((cap - k) / np.maximum(cmy, 1e-6), 0, 1), 1.0)
c, m, y = c * s, m * s, y * s
out = (np.stack([c, m, y, k], axis=-1) * 255 + 0.5).clip(0, 255).astype(np.uint8)
img = Image.fromarray(out, mode="CMYK")
img.save(a.out, resolution=float(a.dpi), quality=95)
tac = out.astype(np.float32).sum(axis=-1) / 255 * 100
print(f"wrote {a.out}  {img.size[0]}x{img.size[1]} @ {a.dpi} ppi  max TAC {tac.max():.0f}% (cap {a.tac:.0f}%)")
