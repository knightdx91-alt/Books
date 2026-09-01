#!/usr/bin/env bash
# Convert an RGB build to PDF/X-1a:2001 (CMYK + OutputIntent) for IngramSpark.
# Requires Ghostscript (gs). Run AFTER production/build_pdf.py or compose_wrap.py.
#
#   bash production/make_pdfx.sh                 # interior (default)
#   bash production/make_pdfx.sh <in.pdf> <out.pdf>
#
# Body text is pure K-only black (set in build_pdf.py), so the CMYK conversion
# yields clean single-plate black with no rich-black registration fuzz.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"
REV="$(cat "$ROOT/REVISION" 2>/dev/null || echo "")"
SUF=""; [ -n "$REV" ] && SUF="-$REV"

IN="${1:-$ROOT/delivery/production/A-Bond-of-Scale-and-Silver-6x9-interior${SUF}.pdf}"
OUT="${2:-${IN%.pdf}-X1a.pdf}"
DEF="$HERE/PDFX_def.ps"

cd "$ROOT"   # PDFX_def.ps references the ICC profile by a ROOT-relative path
[ -f "$IN" ] || { echo "ERROR: input PDF not found: $IN"; exit 1; }
command -v gs >/dev/null || { echo "ERROR: ghostscript (gs) not installed"; exit 1; }

# -dNOSAFER is required so the PDF/X def file can read the ICC profile via the
# PostScript `file` operator (default -dSAFER blocks absolute paths). Inputs are
# local, trusted build artifacts.
gs -dPDFX -dBATCH -dNOPAUSE -dNOOUTERSAVE -dNOSAFER \
   -sDEVICE=pdfwrite \
   -dPDFSETTINGS=/prepress \
   -dCompatibilityLevel=1.3 \
   -sColorConversionStrategy=CMYK \
   -sProcessColorModel=DeviceCMYK \
   -dEmbedAllFonts=true -dSubsetFonts=true \
   -dAutoRotatePages=/None \
   -sOutputFile="$OUT" \
   "$DEF" "$IN"

echo "wrote $OUT"
