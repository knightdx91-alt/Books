#!/usr/bin/env bash
# ============================================================================
# new-book.sh — scaffold a new book FOLDER inside this monorepo (books/<slug>/)
# from books/_template/. No new repo, no GitHub step — everything lives on `main`.
#
# Usage:
#   bash tools/new-book.sh <slug> "<Book Title>"
# Example:
#   bash tools/new-book.sh the-glass-road "The Glass Road"
#
# Run from the repo root.
# ============================================================================
set -euo pipefail

SLUG="${1:-}"; TITLE="${2:-}"
if [[ -z "$SLUG" || -z "$TITLE" ]]; then
  echo "usage: bash tools/new-book.sh <slug> \"<Book Title>\"" >&2; exit 1
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TPL="$ROOT/books/_template"
DEST="$ROOT/books/$SLUG"
TODAY="$(date +%Y-%m-%d)"

[[ -d "$TPL" ]] || { echo "error: template not found at $TPL" >&2; exit 1; }
[[ -e "$DEST" ]] && { echo "error: $DEST already exists" >&2; exit 1; }

# Full working structure for a book project.
mkdir -p "$DEST"/{research,manuscript/chapters,evaluations/continuity,feedback,delivery/editorial,delivery/production,voice-bank/samples,tools}

# Seed from the template.
[[ -f "$TPL/STATE.yaml" ]]            && cp "$TPL/STATE.yaml" "$DEST/STATE.yaml"
[[ -f "$TPL/CLAUDE.md" ]]             && cp "$TPL/CLAUDE.md"  "$DEST/CLAUDE.md"
[[ -f "$TPL/tools/style_check.py" ]]  && cp "$TPL/tools/style_check.py"  "$DEST/tools/style_check.py"
[[ -f "$TPL/tools/grammar_check.py" ]]&& cp "$TPL/tools/grammar_check.py" "$DEST/tools/grammar_check.py"

# Fill placeholders.
sed -i "s|<BOOK TITLE>|$TITLE|g; s|<YYYY-MM-DD>|$TODAY|g" "$DEST/STATE.yaml" "$DEST/CLAUDE.md" 2>/dev/null || true

cat > "$DEST/feedback/progress.md" <<EOF
# Progress — $TITLE

Scaffolded $TODAY by tools/new-book.sh into books/$SLUG/.

## Next steps
1. Stage source material into research/ (draft + any roadmap/bible).
2. Fill STATE.yaml (premise, genre, comps, canon, guardrails, open decisions).
3. Edit tools/style_check.py ALLOWLIST with this book's deliberate motifs.
4. Architect pass — foundation.md + outline.md. The architect SELECTS a
   macro-structure per book (Section 0.5); it will NOT default to 3-act/20-chapters.
5. Run the chapter loop in order; commit per chapter (to main).

## Resume point
Nothing drafted yet.
EOF

echo "Created books/$SLUG/ (\"$TITLE\"). Next: stage source material, fill STATE.yaml, run the architect."
echo "Then commit & push to main:  git add books/$SLUG && git commit -m \"Scaffold $TITLE\" && git push origin main"
