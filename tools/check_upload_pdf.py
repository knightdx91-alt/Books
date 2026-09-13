#!/usr/bin/env python3
"""Preflight a PDF for IngramSpark: is this the upload copy or the archival one?

  python3 tools/check_upload_pdf.py interior <file.pdf> [...]
  python3 tools/check_upload_pdf.py cover    <file.pdf> [...]
  python3 tools/check_upload_pdf.py any      <file.pdf> [...]   # just report

Exit 0 if every file passes, 1 otherwise.

WHY THIS EXISTS
IngramSpark rejects a file that carries an embedded colour profile:

    PDF CONTAINS ICC COLOR PROFILES: We request files with no color profiles
    assigned. Please convert all colors to grayscale for black and white images,
    or CMYK for color images and remove all color profiles.

Every book's delivery/ folder holds three near-identical looking wraps, and only
one of them is the upload copy:

    <name>-rN.pdf              the build      — DeviceRGB, wrong colour space
    <name>-rN-PDFX1a.pdf       archival       — carries an OutputIntent (an ICC
                               profile), which is exactly what trips the warning
    <name>-rN-CMYK-noicc.pdf   THE UPLOAD     — DeviceCMYK, no profile

Told apart by filename alone that is a coin flip on a phone, so this reads what is
actually inside the file. Point it at whatever you are about to upload — or at a
download you renamed and can no longer identify — and it tells you which of the
three you are holding.

The check is structural, not a filename heuristic: it walks the raw bytes AND the
decompressed streams (so an /ICCBased inside an object stream cannot hide) looking
for /ICCBased and /OutputIntent, then reports the device colour spaces in use.
"""
import re, sys, zlib

MARKERS = (b"ICCBased", b"OutputIntent")
SPACES = (b"DeviceCMYK", b"DeviceGray", b"DeviceRGB", b"CalRGB", b"CalGray", b"Lab")

# Content-stream colour operators. A text-only interior often sets grey with a bare
# `0 g` and never declares a /DeviceGray resource at all, so the named colour spaces
# above can come back empty on a perfectly good file — the operators are the evidence
# that survives. (Matching `g` needs the leading number: `/Fm0 Do`, `/GS0 gs` and font
# names are full of stray letters.)
OPS = ((rb"[\d.]\s+g[\s\n]", "DeviceGray"),
       (rb"[\d.]\s+k[\s\n]", "DeviceCMYK"),
       (rb"[\d.]\s+rg[\s\n]", "DeviceRGB"))

# what each upload slot must be, per INGRAMSPARK-UPLOAD-GUIDE Part C
WANT = {"interior": "DeviceGray", "cover": "DeviceCMYK"}

# Colour spaces that are positively WRONG in each slot, as opposed to merely absent.
# DeviceGray inside a CMYK cover is fine — grey is a legal CMYK ink mix and Ghostscript
# emits it for black text — so only RGB convicts a cover.
BANNED = {"interior": ("DeviceRGB", "CalRGB", "Lab", "DeviceCMYK"),
          "cover": ("DeviceRGB", "CalRGB", "Lab")}


def inspect(path):
    """-> (set of profile markers found, set of device colour spaces used).

    Looks at named colour-space resources AND the operators in the content streams,
    because a file can legitimately use one without the other.
    """
    data = open(path, "rb").read()
    blobs = [data]
    for m in re.finditer(rb"stream\r?\n", data):
        end = data.find(b"endstream", m.end())
        if end < 0:
            continue
        try:
            blobs.append(zlib.decompress(data[m.end():end]))
        except zlib.error:
            pass                      # not flate, or a raw image — nothing to read
    profiles, spaces = set(), set()
    for blob in blobs:
        for name in MARKERS:
            if b"/" + name in blob:
                profiles.add(name.decode())
        for name in SPACES:
            if b"/" + name in blob:
                spaces.add(name.decode())
    for blob in blobs[1:]:            # operators only exist in decompressed streams
        for pat, name in OPS:
            if re.search(pat, blob):
                spaces.add(name)
    return profiles, spaces


def check(kind, path):
    try:
        profiles, spaces = inspect(path)
    except OSError as e:
        print(f"FAIL  {path}\n      cannot read: {e}")
        return False
    want = WANT.get(kind)
    problems = []
    if profiles:
        problems.append("carries " + " + ".join(sorted(profiles)) +
                        " — IngramSpark will reject this as 'PDF CONTAINS ICC "
                        "COLOR PROFILES'. This is the archival PDF/X-1a copy, "
                        "not the upload copy.")
    wrong = sorted(set(BANNED.get(kind, ())) & spaces)
    if wrong:
        problems.append(f"uses {'/'.join(wrong)}, but the {kind} uploads as {want}.")
    label = ", ".join(sorted(spaces)) or "no device colour space found"
    if problems:
        print(f"FAIL  {path}")
        for p in problems:
            print(f"      {p}")
        return False
    # Absence of evidence is not evidence of absence: an unusual producer may name no
    # colour space and use no colour operator. Say so rather than failing a good file.
    if want and want not in spaces:
        print(f"WARN  {path}\n      no colour profile (good), but could not confirm "
              f"{want} — nothing in the file names a colour space or sets one. "
              f"Eyeball it before uploading.")
        return True
    print(f"OK    {path}\n      {label}, no colour profile — safe to upload")
    return True


def main(argv):
    if len(argv) < 3 or argv[1] not in ("interior", "cover", "any"):
        print(__doc__.strip().split("\n\n")[1])
        return 2
    kind = argv[1]
    return 0 if all([check(kind, p) for p in argv[2:]]) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
