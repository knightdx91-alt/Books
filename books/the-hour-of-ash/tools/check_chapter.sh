#!/usr/bin/env bash
# Consolidated per-chapter gate runner for The Hour of Ash.
# Usage: bash tools/check_chapter.sh <chapter-number>
# Runs EVERY gate a finalized chapter must pass, so none is ever skipped:
#   1. style_check   (too-flowery: simile/em-dash/adverb + cross-chapter n-grams)
#   2. grammar_check (HARD: doubled words, spacing, a/an; + long-sentence report)
#   3. rhythm_check  (flat triplets / unsanctioned anaphora)
#   4. show_tell     (too-descriptive: filter/abstraction; chapter row + book heavies)
#   5. voice_wear    (per-POV device calcification / retired phrases; --strict: self-repeat FAILS)
#   5a. tic gate     (tic_report --gate: no phrase/catchphrase recurs 3+ times book-wide)
#   6. word count    (vs the outline target — NO per-chapter floor; length varies by design)
#   7. shape audit   (book-wide predictability check, tools/shape_check.py at the repo root)
# Genesis Floor >= 8.5 (book-evaluator) and the PACING check are judgement gates —
# this script prints a reminder; they are not mechanical.
set -uo pipefail
cd "$(dirname "$0")/.." || exit 2
N="${1:?usage: check_chapter.sh <chapter-number>}"
CH="manuscript/chapters/chapter-${N}.md"
[ -f "$CH" ] || { echo "no such chapter: $CH"; exit 2; }

line() { printf '\n=== %s ===\n' "$1"; }

line "1. STYLE (too-flowery)";      python3 tools/style_check.py 2>&1 | grep -iE "Ch *${N}\b|CEILING|RESULT"
line "2. GRAMMAR (hard)";           python3 tools/grammar_check.py 2>&1 | grep -iE "chapter-${N}\.md:|^RESULT|RESULT:"
line "3. RHYTHM";                   python3 tools/rhythm_check.py 2>&1 | grep -iE "chapter-${N}\.md|TOTAL"
line "4. SHOW/TELL (too-descriptive) — chapter row + any book-wide heavies for this ch"
python3 tools/show_tell_check.py 2>&1 | grep -E "chapter *wds|chapter-${N}\.md"
line "5. VOICE-WEAR (strict: self-repetition BLOCKS — tic budget 0)"; python3 tools/voice_wear_check.py --strict 2>&1 | grep -iE "\[.*\].*ch |RETIRED|RESULT"
line "5a. TIC GATE (any non-allowlisted phrase 3+ times book-wide = defect)"; python3 tools/tic_report.py --gate 2>&1 | sed -n "/AUTO-RECURRENCE/,\$p"
line "5b. METAPHOR/SENTENCE-SHAPE (register: figurative load + long-sentence %)"
python3 tools/metaphor_check.py 2>&1 | grep -E "wds|^ *${N} " | head -2
python3 tools/metaphor_check.py "$N" >/dev/null 2>&1 || echo "   ^ over a figurative ceiling (FIG>4.0/1k or LONG>18% of sentences) — split/trim"
line "6. WORD COUNT (compare to this chapter's outline target; no per-chapter floor)"; wc -w "$CH"
line "7. SHAPE AUDIT (book-wide predictability)"; python3 ../../tools/shape_check.py . 2>&1 | grep -E "^\s+\[|RESULT|note:"
line "JUDGEMENT GATES (not mechanical — do these by hand every chapter)"
printf '  [ ] Genesis Floor >= 8.5 (book-evaluator, 7 dims) -> evaluations/chapter-%s-eval.md\n' "$N"
printf '  [ ] PACING check vs neighbors (length band, dialogue share, emotional slot, hook)\n'
printf '  [ ] update feedback/progress.md + feedback/pov-map.txt\n'
