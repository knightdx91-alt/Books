#!/usr/bin/env python3
"""Collect every finished book's upload-ready files into completed-books/.

  python3 tools/collect_completed.py           # refresh the folder
  python3 tools/collect_completed.py --check   # verify it matches source, exit 1 if stale

WHY THIS IS A SCRIPT AND NOT A HAND-COPIED FOLDER
Copies go stale the moment a book is re-cut, and a stale print file is exactly the
kind of thing that gets uploaded by mistake. So the folder is generated, every file
is checksummed into MANIFEST.md alongside the revision it came from, and --check
tells you whether what is sitting in completed-books/ is still the current build.

Each book contributes the THREE files IngramSpark actually wants:
  INTERIOR     the grayscale, no-ICC print interior
  COVER        the CMYK, no-ICC full wrap (back + spine + front, full bleed)
  EPUB         the ebook
  EBOOK-COVER  the standalone front-cover JPG the ebook listing asks for separately
The PDF/X-1a builds are archival/prepress copies and deliberately stay behind in
each book's own delivery/ folder.
"""
import hashlib, os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "completed-books")

BOOKS = [
    dict(order="01", title="Hazel Academy", folder="01-hazel-academy",
         series="The Saeren Chronicles, Book One", pen="Post Peleos",
         book="books/saeren/saeren-chronicles",
         interior="delivery/production/Saeren-Chronicles-Book-One-6x9-interior-{rev}-GRAY-noicc.pdf",
         cover="delivery/cover/Saeren-Book-One-FULL-WRAP-{rev}-CMYK-noicc.pdf",
         epub="delivery/ebook/Saeren-Chronicles-Book-One-Hazel-Academy.epub",
         ebookcover="delivery/cover/ebook-cover-book1-hazel-academy.jpg",
         pages=294, spine='0.662"', isbn="979-8-2409-9043-4", eisbn="979-8-2409-9044-1"),
    dict(order="02", title="The Resistance", folder="02-the-resistance",
         series="The Saeren Chronicles, Book Two", pen="Post Peleos",
         book="books/saeren/saeren-chronicles-book-2",
         interior="delivery/production/Saeren-Chronicles-Book-Two-6x9-interior-{rev}-GRAY-noicc.pdf",
         cover="delivery/cover/Saeren-Book-Two-FULL-WRAP-{rev}-CMYK-noicc.pdf",
         epub="delivery/ebook/Saeren-Chronicles-Book-Two-The-Resistance.epub",
         ebookcover="delivery/cover/ebook-cover-book2-the-resistance.jpg",
         pages=308, spine='0.694"', isbn="979-8-2409-9382-4", eisbn="979-8-2561-0025-4"),
    dict(order="03", title="The Weight of the Source", folder="03-the-weight-of-the-source",
         series="The Saeren Chronicles, Book Three", pen="Post Peleos",
         book="books/saeren/saeren-chronicles-book-3",
         interior="delivery/production/Saeren-Chronicles-Book-Three-6x9-interior-{rev}-GRAY-noicc.pdf",
         cover="delivery/cover/Saeren-Book-Three-FULL-WRAP-{rev}-CMYK-noicc.pdf",
         epub="delivery/ebook/Saeren-Chronicles-Book-Three-The-Weight-of-the-Source.epub",
         ebookcover="delivery/cover/ebook-cover-book3-the-weight-of-the-source.jpg",
         pages=324, spine='0.730"', isbn="979-8-1827-2380-0", eisbn="979-8-1827-2381-7"),
    dict(order="04", title="A Bond of Scale and Silver", folder="04-a-bond-of-scale-and-silver",
         series="Standalone — adult romantasy (18+)", pen="Søren Stromberg",
         book="books/scale-and-silver",
         interior="delivery/production/A-Bond-of-Scale-and-Silver-6x9-interior-{rev}-GRAY-noicc.pdf",
         cover="delivery/production/A-Bond-of-Scale-and-Silver-wrap-6x9-{rev}-CMYK-noicc.pdf",
         epub="delivery/production/A-Bond-of-Scale-and-Silver.epub",
         ebookcover="delivery/cover/ebook-cover-a-bond-of-scale-and-silver.jpg",
         pages=448, spine='1.120"', isbn="979-8-1827-2378-7", eisbn="979-8-1827-2379-4"),
]


def rev(b):
    return open(os.path.join(ROOT, b["book"], "REVISION"), encoding="utf-8").read().strip()


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


def slug(t):
    return t.replace(" ", "-")


def plan():
    """[(book, revision, [(src_abs, dst_abs, label)])]"""
    out = []
    for b in BOOKS:
        r = rev(b)
        dst_dir = os.path.join(OUT, b["folder"])
        files = []
        for key, label in (("interior", "INTERIOR"), ("cover", "COVER"),
                           ("epub", "EPUB"), ("ebookcover", "EBOOK-COVER")):
            src = os.path.join(ROOT, b["book"], b[key].format(rev=r))
            ext = os.path.splitext(src)[1]
            if label == "EPUB":
                name = f"{slug(b['title'])}{ext}"
            elif label == "EBOOK-COVER":          # not revision-stamped: art, not a build
                name = f"{slug(b['title'])}-{label}{ext}"
            else:
                name = f"{slug(b['title'])}-{r}-{label}{ext}"
            files.append((src, os.path.join(dst_dir, name), label))
        out.append((b, r, files))
    return out


def main(check=False):
    missing, stale = [], []
    p = plan()
    for b, r, files in p:
        for src, dst, _ in files:
            if not os.path.exists(src):
                missing.append(src); continue
            if check:
                if not os.path.exists(dst) or sha(src) != sha(dst):
                    stale.append(os.path.relpath(dst, ROOT))
            else:
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
    if missing:
        print("MISSING SOURCE FILES:"); [print("  ", os.path.relpath(m, ROOT)) for m in missing]
        return 1
    if check:
        if stale:
            print("STALE — completed-books/ does not match the current builds:")
            [print("  ", s) for s in stale]
            return 1
        print("completed-books/ is up to date with every book's current REVISION")
        return 0

    # --- MANIFEST -----------------------------------------------------------
    lines = ["# Manifest\n",
             "Generated by `tools/collect_completed.py`. Do not edit by hand — rerun the\n"
             "script instead. `--check` verifies these checksums against the live builds.\n"]
    for b, r, files in p:
        lines.append(f"\n## {b['title']} — {r}\n")
        lines.append(f"{b['series']} · by {b['pen']}\n")
        lines.append(f"\n{b['pages']} pages · spine {b['spine']} · "
                     f"print ISBN {b['isbn']} · eBook ISBN {b['eisbn']}\n\n")
        lines.append("| file | sha256 (short) | size |\n|---|---|---|\n")
        for src, dst, label in files:
            kb = os.path.getsize(dst) // 1024
            lines.append(f"| `{os.path.basename(dst)}` | `{sha(dst)}` | {kb} KB |\n")
    open(os.path.join(OUT, "MANIFEST.md"), "w", encoding="utf-8").write("".join(lines))

    for b, r, files in p:
        print(f"{b['title']:28s} {r:4s} -> completed-books/{b['folder']}/")
    print("\nwrote completed-books/MANIFEST.md")
    return 0


if __name__ == "__main__":
    sys.exit(main(check="--check" in sys.argv))
