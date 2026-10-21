#!/usr/bin/env python3
"""Generate a clearly-marked PLACEHOLDER ebook cover so tools/make_epub.py can run
before the real art exists. Title and author come from delivery/ebook.yaml.

    python3 books/sygl-book/tools/make_placeholder_cover.py

Writes the path named by `cover:` in the config (1600 x 2263 px, RGB JPG, ratio
1.414). NOT FOR RELEASE: replace it with the real front cover JPG and point
`cover:` at that file.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from production_common import BOOK, load_config  # noqa: E402
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"


def main():
    cfg = load_config()
    out = os.path.join(BOOK, cfg["cover"])
    if "PLACEHOLDER" not in os.path.basename(out):
        sys.exit(f"refusing to overwrite a non-placeholder cover: {out}")
    W, H = 1600, 2263
    im = Image.new("RGB", (W, H), (38, 10, 14))
    d = ImageDraw.Draw(im)
    big = ImageFont.truetype(f"{FONT_DIR}/CrimsonPro-Bold.ttf", 300)
    mid = ImageFont.truetype(f"{FONT_DIR}/CrimsonPro-Regular.ttf", 96)
    small = ImageFont.truetype(f"{FONT_DIR}/CrimsonPro-Italic.ttf", 64)
    d.rectangle([60, 60, W - 60, H - 60], outline=(170, 140, 90), width=6)
    d.text((W / 2, 820), cfg["title"], font=big, fill=(236, 226, 210), anchor="mm")
    d.text((W / 2, 1750), cfg["author"], font=mid, fill=(214, 190, 140), anchor="mm")
    d.text((W / 2, 2080), "placeholder cover — not for release", font=small,
           fill=(150, 120, 110), anchor="mm")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    im.save(out, "JPEG", quality=90)
    print(f"wrote {out} ({W}x{H})")


if __name__ == "__main__":
    main()
