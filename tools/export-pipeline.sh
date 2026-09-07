#!/usr/bin/env bash
# ============================================================================
# export-pipeline.sh — export a books-free copy of the pipeline for sharing.
#
#   bash tools/export-pipeline.sh <target-dir>
#
# The pipeline is developed HERE, alongside the books. This script produces the
# distributable version of it — everything except the manuscripts — so the public
# pipeline repo can be refreshed without hand-copying and without drifting.
#
# Typical use:
#   git clone https://github.com/knightdx91-alt/book-pipeline /tmp/pipeline
#   bash tools/export-pipeline.sh /tmp/pipeline
#   cd /tmp/pipeline && git add -A && git commit -m "Sync pipeline" && git push
#
# WHAT IS EXPORTED
#   .claude/  tools/  docs/  books/_template/  books/_series-template/
#   README.md (the target's own, kept)  requirements.txt  .gitignore  setup-script.sh
#
# WHAT IS NOT
#   books/<any real book>/   completed-books/   PROJECT-STATUS.md
#   the BOOKS registry in collect_completed.py (real ISBNs / pen names / paths)
#
# The target's own README.md and CLAUDE.md are LEFT ALONE — they are written for
# the standalone repo and differ from this one's on purpose.
# ============================================================================
set -euo pipefail

TARGET="${1:-}"
if [[ -z "$TARGET" ]]; then
  echo "usage: bash tools/export-pipeline.sh <target-dir>" >&2
  exit 1
fi
[[ -d "$TARGET" ]] || { echo "error: target directory does not exist: $TARGET" >&2; exit 1; }

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="$(cd "$TARGET" && pwd)"
[[ "$TARGET" == "$ROOT" ]] && { echo "error: target is this repo" >&2; exit 1; }

echo "Exporting pipeline: $ROOT -> $TARGET"

# --- the pipeline itself ----------------------------------------------------
rm -rf "$TARGET/.claude" "$TARGET/tools" "$TARGET/docs"
cp -r "$ROOT/.claude" "$ROOT/tools" "$ROOT/docs" "$TARGET/"

mkdir -p "$TARGET/books"
rm -rf "$TARGET/books/_template" "$TARGET/books/_series-template"
cp -r "$ROOT/books/_template" "$ROOT/books/_series-template" "$TARGET/books/"

cp "$ROOT/requirements.txt" "$ROOT/.gitignore" "$ROOT/setup-script.sh" "$TARGET/"

# This script is about THIS repo's layout; it does not belong in the distribution.
rm -f "$TARGET/tools/export-pipeline.sh"

find "$TARGET" -path "$TARGET/.git" -prune -o -name '__pycache__' -exec rm -rf {} + 2>/dev/null || true

# --- strip the personal book registry --------------------------------------
python3 - "$TARGET/tools/collect_completed.py" <<'PY'
import re, sys
path = sys.argv[1]
s = open(path).read()
start = s.find("BOOKS = [")
if start == -1:
    sys.exit("error: BOOKS list not found in collect_completed.py")
depth, i = 0, s.index("[", start)
for j in range(i, len(s)):                     # find the matching close bracket
    if s[j] == "[": depth += 1
    elif s[j] == "]":
        depth -= 1
        if depth == 0:
            end = j + 1
            break
example = '''BOOKS = [
    # One entry per finished book. Paths are relative to the book folder; "{rev}" is
    # substituted from that book's REVISION file, so a re-cut is picked up automatically.
    #
    # dict(order="01", title="Your Book", folder="01-your-book",
    #      series="Your Series, Book One", pen="Your Pen Name",
    #      book="books/your-book",
    #      interior="delivery/production/Your-Book-6x9-interior-{rev}-GRAY-noicc.pdf",
    #      cover="delivery/cover/Your-Book-FULL-WRAP-{rev}-CMYK-noicc.pdf",
    #      epub="delivery/ebook/Your-Book.epub",
    #      ebookcover="delivery/cover/ebook-cover-your-book.jpg",
    #      pages=294, spine='0.662"', isbn="978-0-0000-0000-0", eisbn="978-0-0000-0001-7"),
]'''
open(path, "w").write(s[:start] + example + s[end:])
PY

# --- neutralize book names used as path examples ---------------------------
# The distribution should not carry real book titles, even as examples.
for f in "$TARGET/tools/gemini_review.sh" "$TARGET/tools/grok_review.sh" \
         "$TARGET/tools/make_epub.py" "$TARGET/tools/doctor.sh" \
         "$TARGET/.claude/agents/book-orchestrator.md" \
         "$TARGET/docs/SERIES.md" "$TARGET/docs/PUBLISHING.md"; do
  [[ -f "$f" ]] || continue
  sed -i \
    -e 's|books/the-gift|books/your-book|g' \
    -e 's|books/saeren/saeren-chronicles-book-2|books/your-series/book-two|g' \
    -e 's|books/saeren/saeren-chronicles|books/your-series/book-one|g' \
    -e 's|books/saeren|books/your-series|g' \
    -e 's|"The Saeren Chronicles"|"The Emberfall Cycle"|g' \
    "$f"
done

# --- verify nothing personal survived --------------------------------------
echo
echo "Checking the export for personal content..."
LEAKS="$(grep -rn -i -E 'saeren|hazel academy|post peleos|stromberg|viridia|raelynn|979-8-' \
  --include='*.md' --include='*.py' --include='*.sh' --include='*.yaml' --include='*.json' --include='*.txt' \
  "$TARGET" 2>/dev/null | grep -v '/tools/apodictic/' | grep -v '/\.git/' || true)"
if [[ -n "$LEAKS" ]]; then
  echo "WARNING — personal content found in the export:" >&2
  echo "$LEAKS" >&2
  echo "Fix it at the source in this repo, then re-run." >&2
  exit 1
fi

MANUSCRIPTS="$(find "$TARGET" -path "$TARGET/.git" -prune -o -path '*/apodictic/*' -prune -o \
  -type f \( -name 'chapter-*.md' -o -name '*.epub' -o -name '*full-manuscript*' \) -print 2>/dev/null || true)"
if [[ -n "$MANUSCRIPTS" ]]; then
  echo "WARNING — manuscript files found in the export:" >&2
  echo "$MANUSCRIPTS" >&2
  exit 1
fi

echo "Clean: no manuscripts, no personal data."
echo
echo "Next:"
echo "  cd $TARGET && bash tools/doctor.sh && git add -A && git commit && git push"
