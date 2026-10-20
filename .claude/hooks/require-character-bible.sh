#!/bin/bash
# ============================================================================
# PreToolUse guard: no chapter is written for a book that has no character bible.
#
# Fires on Write / Edit / MultiEdit. If the target is a manuscript chapter file
# (books/**/manuscript/chapter-*.md or books/**/manuscript/chapters/*.md) and the
# book folder (nearest ancestor holding STATE.yaml) has no character-bible.md,
# the call is blocked (exit 2) with instructions to create the bible first.
# Writes to anything else — including character-bible.md itself — pass through.
#
# Enabled/disabled by REQUIRE_CHARACTER_BIBLE in .claude/pipeline.conf (default: on).
# ============================================================================
set -uo pipefail
INPUT="$(cat)"

REQUIRE_CHARACTER_BIBLE="on"
CONF="${CLAUDE_PROJECT_DIR:-$PWD}/.claude/pipeline.conf"
if [ -f "$CONF" ]; then
  # shellcheck disable=SC1090
  source "$CONF"
fi
[ "$REQUIRE_CHARACTER_BIBLE" = "on" ] || exit 0

FILE="$(printf '%s' "$INPUT" | python3 -c 'import sys,json; print(json.load(sys.stdin).get("tool_input",{}).get("file_path",""))' 2>/dev/null || echo)"
[ -n "$FILE" ] || exit 0

case "$FILE" in
  */books/*/manuscript/chapter-*.md|*/books/*/manuscript/chapters/*.md) ;;
  *) exit 0 ;;
esac
case "$FILE" in
  */books/_template/*|*/books/_series-template/*) exit 0 ;;
esac

# Walk up from the chapter's folder to the book folder (the one with STATE.yaml).
d="$(dirname "$FILE")"
BOOK=""
while [ "$d" != "/" ] && [ -n "$d" ]; do
  if [ -f "$d/STATE.yaml" ]; then BOOK="$d"; break; fi
  case "$(basename "$d")" in books) break ;; esac
  d="$(dirname "$d")"
done
[ -n "$BOOK" ] || exit 0
[ -f "$BOOK/character-bible.md" ] && exit 0

REL="${BOOK#"${CLAUDE_PROJECT_DIR:-}"/}"
cat >&2 <<EOF
📖 CHARACTER BIBLE REQUIRED: $REL has no character-bible.md, so chapters can't be written yet.
Create it first, then retry this chapter:
  1. bash tools/ensure-character-bible.sh $REL     (copies the template stub)
  2. Populate it — one voice card per named character (four axes, tic line "none", DISTINCTNESS
     GUARANTEE, sample line) from the book's foundation/outline/source and any chapters already
     written. Use book-architect (voice-card dispatch) or do it directly. See docs/CHARACTER-BIBLE.md.
EOF
exit 2
