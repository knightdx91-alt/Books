#!/usr/bin/env python3
"""
Stamp a PDF/X-1a:2001 OutputIntent onto a PDF that is ALREADY device-CMYK and
ICC-free (the `-CMYK-noicc` wrap that make_noicc.sh produces), without Ghostscript.

    python3 tools/pdfx_outputintent.py IN-CMYK-noicc.pdf OUT-PDFX1a.pdf [--title "..."]

WHY THIS EXISTS
IngramSpark's cover upload previews a plain CMYK/no-ICC PDF as BLANK/WHITE (no
OutputIntent, so the previewer has nothing to render it with) and the same file
can show blank on phone viewers. A PDF/X-1a file (CMYK + OutputIntent) previews
correctly and is what IngramSpark documents as expected. make_pdfx.sh does this
with Ghostscript (`gs -dPDFX ... PDFX_def.ps`), but the web containers do not
always have `gs` and cannot apt-get it. This script does the same thing to the
finished CMYK file with pikepdf: it changes NO pixels and NO colour values, it
only adds what PDF/X-1a requires around them:

  * Root /OutputIntents  -> one /GTS_PDFX intent whose DestOutputProfile is
                            tools/icc/default_cmyk.icc (the same Ghostscript
                            profile accepted IngramSpark covers carry)
  * Info /GTS_PDFXVersion (PDF/X-1a:2001), /Trapped /False, /Title
  * /TrimBox + /BleedBox on every page (= MediaBox, a full-bleed wrap)
  * header version 1.3, as Ghostscript writes for PDF/X-1a

PRECONDITIONS it refuses on (PDF/X-1a forbids them, and this tool does not
convert colour): any /ICCBased, /DeviceRGB, /CalRGB or /Lab colour space, or a
transparency group / soft mask. Run make_noicc.sh cmyk first if you see that.

VERIFY the result the same way as any upload file:
    python3 tools/check_upload_pdf.py cover OUT-PDFX1a.pdf
and render it (pdftoppm) next to the input -- the pages must look identical.
"""
import argparse
import os
import sys

try:
    import pikepdf
    from pikepdf import Name, Dictionary, Array, String
except ImportError:
    sys.exit("ERROR: pikepdf not installed -- pip install pikepdf")

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ICC = os.path.join(HERE, "icc", "default_cmyk.icc")
FORBIDDEN_CS = {"/ICCBased", "/DeviceRGB", "/CalRGB", "/Lab"}


def scan_forbidden(pdf):
    """Return a list of human-readable reasons this file is not PDF/X-1a-safe."""
    problems = []
    seen = set()

    def walk(obj, path, depth=0):
        if depth > 40:
            return
        try:
            key = obj.objgen
        except AttributeError:
            key = None
        if key is not None and key != (0, 0):
            if key in seen:
                return
            seen.add(key)
        if isinstance(obj, pikepdf.Name):
            if str(obj) in FORBIDDEN_CS:
                problems.append(f"{path}: colour space {obj}")
            return
        if isinstance(obj, pikepdf.Array):
            for i, item in enumerate(obj):
                walk(item, f"{path}[{i}]", depth + 1)
            return
        if isinstance(obj, (pikepdf.Dictionary, pikepdf.Stream)):
            if isinstance(obj, pikepdf.Stream) and obj.get("/Type") == Name.Metadata:
                return
            if "/SMask" in obj and obj.SMask != Name.None_:
                problems.append(f"{path}: soft mask (/SMask)")
            if obj.get("/S") == Name.Transparency:
                problems.append(f"{path}: transparency group")
            for k, v in obj.items():
                if k in ("/Parent", "/P", "/Prev", "/Dest", "/OpenAction"):
                    continue
                walk(v, f"{path}/{k[1:]}", depth + 1)

    for n, page in enumerate(pdf.pages, 1):
        walk(page.obj, f"page {n}")
    return problems


def stamp(src, dst, title, icc_path):
    if not os.path.exists(icc_path):
        sys.exit(f"ERROR: ICC profile not found: {icc_path}")
    icc_bytes = open(icc_path, "rb").read()
    if icc_bytes[36:40] != b"acsp" or icc_bytes[16:20] != b"CMYK":
        sys.exit(f"ERROR: {icc_path} is not a CMYK ICC profile")

    pdf = pikepdf.open(src)
    problems = scan_forbidden(pdf)
    if problems:
        print("REFUSED -- not PDF/X-1a-safe as-is (convert with make_noicc.sh cmyk first):")
        for p in problems:
            print("  -", p)
        sys.exit(2)

    # Output intent, same shape and strings as Ghostscript writes from PDFX_def.ps
    profile = pdf.make_stream(icc_bytes)
    profile.N = 4
    intent = pdf.make_indirect(Dictionary(
        Type=Name.OutputIntent,
        S=Name.GTS_PDFX,
        OutputCondition=String("Commercial CMYK offset/POD"),
        OutputConditionIdentifier=String("Custom"),
        Info=String("default_cmyk.icc - replace with printer profile if specified"),
        DestOutputProfile=profile,
    ))
    pdf.Root.OutputIntents = Array([intent])

    # PDF/X-1a page boxes: a full-bleed wrap's trim box is the whole page
    for page in pdf.pages:
        mb = page.MediaBox
        if "/TrimBox" not in page.obj:
            page.obj.TrimBox = Array(mb)
        if "/BleedBox" not in page.obj:
            page.obj.BleedBox = Array(mb)

    with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:
        meta["dc:title"] = title
        meta["pdfxid:GTS_PDFXVersion"] = "PDF/X-1a:2001"
        meta["pdf:Trapped"] = "False"
    pdf.docinfo[Name.Title] = String(title)
    pdf.docinfo[Name.GTS_PDFXVersion] = String("PDF/X-1a:2001")
    pdf.docinfo[Name.Trapped] = Name("/False")

    pdf.save(dst, force_version="1.3", object_stream_mode=pikepdf.ObjectStreamMode.disable,
             linearize=False, fix_metadata_version=True)

    # Report
    out = pikepdf.open(dst)
    oi = out.Root.OutputIntents[0]
    pg = out.pages[0]
    w = float(pg.MediaBox[2]) - float(pg.MediaBox[0])
    h = float(pg.MediaBox[3]) - float(pg.MediaBox[1])
    print(f"wrote {dst}")
    print(f"  pdf {out.pdf_version}  pages {len(out.pages)}  page {w/72:.3f} x {h/72:.3f} in")
    print(f"  OutputIntent {oi.S}  profile N={oi.DestOutputProfile.N}  {len(icc_bytes)} bytes")
    print(f"  GTS_PDFXVersion {out.docinfo.get('/GTS_PDFXVersion')}  Trapped {out.docinfo.get('/Trapped')}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--title", default=None, help="PDF title (default: output file name)")
    ap.add_argument("--icc", default=DEFAULT_ICC, help="CMYK ICC profile for the OutputIntent")
    a = ap.parse_args()
    if os.path.abspath(a.src) == os.path.abspath(a.dst):
        sys.exit("ERROR: src and dst must differ")
    title = a.title or os.path.splitext(os.path.basename(a.dst))[0]
    stamp(a.src, a.dst, title, a.icc)


if __name__ == "__main__":
    main()
