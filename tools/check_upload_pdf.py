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

# what each upload slot must be, per INGRAMSPARK-UPLOAD-GUIDE Part C
WANT = {"interior": "DeviceGray", "cover": "DeviceCMYK"}


def inspect(path):
    """-> (set of profile markers found, set of device colour spaces used)."""
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
    if want and want not in spaces:
        problems.append(f"colour space is {'/'.join(sorted(spaces)) or 'undetermined'},"
                        f" but the {kind} uploads as {want}.")
    label = ", ".join(sorted(spaces)) or "no device colour space found"
    if problems:
        print(f"FAIL  {path}")
        for p in problems:
            print(f"      {p}")
        return False
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
