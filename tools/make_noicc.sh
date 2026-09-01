#!/usr/bin/env bash
# Produce the profile-free PDFs IngramSpark actually wants on upload.
#
#   bash tools/make_noicc.sh gray <interior.pdf> <out-GRAY-noicc.pdf>
#   bash tools/make_noicc.sh cmyk <wrap.pdf>     <out-CMYK-noicc.pdf>
#
# Why not the PDF/X-1a file: per INGRAMSPARK-UPLOAD-GUIDE Part C, the print
# interior uploads as **grayscale, no ICC** (a text-only B&W interior) and the
# cover as **CMYK, no ICC**. The X-1a builds are kept as the archival/prepress
# copies; these are the upload copies. An embedded ICC profile only triggers the
# "PDF CONTAINS ICC COLOR PROFILES" warning, so we ship without one.
#
# Downsampling is switched OFF. /prepress otherwise resamples images to exactly
# 300 dpi, which is IngramSpark's floor rather than a comfortable margin — the
# author photo would land on 300.0 dpi and any rounding in their preflight could
# read as under-spec. Keeping the source resolution costs a few hundred KB.
set -euo pipefail

MODE="${1:?usage: make_noicc.sh <gray|cmyk> <in.pdf> <out.pdf>}"
IN="${2:?missing input pdf}"
OUT="${3:?missing output pdf}"

case "$MODE" in
  gray) CS=Gray; PCM=DeviceGray ;;
  cmyk) CS=CMYK; PCM=DeviceCMYK ;;
  *) echo "ERROR: mode must be 'gray' or 'cmyk', got '$MODE'"; exit 1 ;;
esac

[ -f "$IN" ] || { echo "ERROR: input PDF not found: $IN"; exit 1; }
command -v gs >/dev/null || { echo "ERROR: ghostscript (gs) not installed"; exit 1; }

gs -q -dBATCH -dNOPAUSE -dNOSAFER -sDEVICE=pdfwrite \
   -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress \
   -sColorConversionStrategy="$CS" -sProcessColorModel="$PCM" \
   -dAutoRotatePages=/None \
   -dEmbedAllFonts=true -dSubsetFonts=true \
   -dDownsampleGrayImages=false -dDownsampleColorImages=false \
   -dDownsampleMonoImages=false \
   -sOutputFile="$OUT" "$IN"

# Verify it really is profile-free — an ICC profile here is the one thing that
# makes IngramSpark complain, and it is silent otherwise.
if grep -qa "/ICCBased\|/OutputIntent" "$OUT"; then
  echo "WARNING: $OUT still contains an ICC profile or output intent"
else
  echo "wrote $OUT (${MODE}, no ICC)"
fi
