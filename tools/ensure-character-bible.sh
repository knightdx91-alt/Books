#!/usr/bin/env bash
# ensure-character-bible.sh — make sure a book folder has a character-bible.md.
#
#   bash tools/ensure-character-bible.sh <book-dir>        # scaffold one book if missing
#   bash tools/ensure-character-bible.sh --list            # list book folders that lack one
#
# A book folder is any folder under books/ that holds a STATE.yaml (series sub-books included).
# If the bible is missing, this copies books/_template/character-bible.md in and fills the title.
# The copy is a STUB: an architect pass (or the orchestrator's voice dispatch) must then populate
# it from the book's foundation/outline/source and any chapters already written, before the next
# chapter is drafted. The PreToolUse hook require-character-bible.sh blocks chapter writes until
# the file exists.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TPL="$ROOT/books/_template/character-bible.md"

list_missing () {
  find "$ROOT/books" -name STATE.yaml -not -path '*/_template/*' -not -path '*/_series-template/*' \
    -not -path '*/superseded/*' -print0 2>/dev/null \
  | while IFS= read -r -d '' st; do
      d="$(dirname "$st")"
      [ -f "$d/character-bible.md" ] || echo "${d#"$ROOT"/}"
    done | sort
}

if [ "${1:-}" = "--list" ]; then
  list_missing
  exit 0
fi

[ $# -eq 1 ] || { echo "usage: $0 <book-dir> | --list" >&2; exit 2; }
DIR="$(cd "$1" && pwd)"
[ -f "$DIR/STATE.yaml" ] || { echo "error: $1 has no STATE.yaml — not a book folder" >&2; exit 1; }

if [ -f "$DIR/character-bible.md" ]; then
  echo "ok: ${DIR#"$ROOT"/}/character-bible.md already exists"
  exit 0
fi
[ -f "$TPL" ] || { echo "error: template missing at $TPL" >&2; exit 1; }

TITLE="$(python3 - "$DIR/STATE.yaml" <<'EOF' 2>/dev/null || true
import sys, re
for line in open(sys.argv[1], encoding="utf-8"):
    m = re.match(r'\s*title:\s*"?([^"#\n]+)"?', line)
    if m:
        print(m.group(1).strip()); break
EOF
)"
[ -n "$TITLE" ] || TITLE="$(basename "$DIR")"

sed "s/<BOOK TITLE>/$(printf '%s' "$TITLE" | sed 's/[&/\]/\\&/g')/" "$TPL" > "$DIR/character-bible.md"
echo "created: ${DIR#"$ROOT"/}/character-bible.md (template stub)"
echo "next: populate it before drafting more chapters — one voice card per named character, from"
echo "      foundation/outline/source and any chapters already written (docs/CHARACTER-BIBLE.md)."
