#!/usr/bin/env bash
# Consolidated per-chapter gate runner (per-book copy, seeded from books/_template — every new book gets it).
# Usage: bash tools/check_chapter.sh <chapter-number>
# Runs EVERY gate a finalized chapter must pass, so none is ever skipped:
#   1. style_check   (too-flowery: simile/em-dash/adverb + cross-chapter n-grams)
#   2. grammar_check (HARD: doubled words, spacing, a/an; + long-sentence report)
#   3. rhythm_check  (flat triplets / unsanctioned anaphora)
#   4. show_tell     (too-descriptive: filter/abstraction; chapter row + book heavies)
#   5. voice_wear    (per-POV device calcification / retired phrases; --strict: self-repeat FAILS)
#   5d. closed ledger (tools/closed_ledger.tsv: the bible's SPENT/CLOSED constructions, as regexes)
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

run_all() {
line "1. STYLE (too-flowery)";      python3 tools/style_check.py 2>&1 | grep -iE "Ch *${N}\b|CEILING|RESULT"
line "2. GRAMMAR (hard)";           python3 tools/grammar_check.py 2>&1 | grep -iE "chapter-${N}\.md:|^RESULT|RESULT:"
line "3. RHYTHM";                   python3 tools/rhythm_check.py 2>&1 | grep -iE "chapter-${N}\.md|TOTAL"
line "4. SHOW/TELL (too-descriptive) — chapter row + any book-wide heavies for this ch"
python3 tools/show_tell_check.py 2>&1 | grep -E "chapter *wds|chapter-${N}\.md"
line "5. VOICE-WEAR (strict: self-repetition BLOCKS — tic budget 0)"; python3 tools/voice_wear_check.py 2>&1 | grep -iE "\[.*\].*ch |RETIRED|RESULT"
line "5a. TIC GATE (any non-allowlisted phrase 3+ times book-wide = defect)"; python3 tools/tic_report.py --gate 2>&1 | sed -n "/AUTO-RECURRENCE/,\$p"
line "5c. ECHO SCAN (2nd uses of an earlier chapter's phrase — vary them before the evaluator sees them)"; python3 tools/tic_report.py --echoes "$N" 2>&1 | head -120
E=$(python3 tools/tic_report.py --echoes "$N" 2>&1 | grep -oE "^RESULT: [0-9]+ echo" | grep -oE "[0-9]+" || echo 0)
[ "${E:-0}" -gt 0 ] && echo "RESULT: FAIL — ${E} cross-chapter echo(es); vary every one before the evaluator sees the chapter"
line "5d. CLOSED LEDGER (SPENT/CLOSED constructions from tools/closed_ledger.tsv — never restore one)"; python3 tools/closed_check.py "$N" 2>&1
line "5b. METAPHOR/SENTENCE-SHAPE (register: figurative load + long-sentence %)"
python3 tools/metaphor_check.py 2>&1 | grep -E "wds|^ *${N} " | head -2
python3 tools/metaphor_check.py "$N" >/dev/null 2>&1 || echo "   ^ over a figurative ceiling (FIG>4.0/1k or LONG>18% of sentences) — split/trim"
line "6. WORD COUNT (compare to this chapter's outline target; no per-chapter floor)"; wc -w "$CH"
line "7. SHAPE AUDIT (book-wide predictability)"; python3 ../../tools/shape_check.py . 2>&1 | grep -E "^\s+\[|RESULT|note:"
line "JUDGEMENT GATES (not mechanical — do these by hand every chapter)"
printf '  [ ] Genesis Floor >= 8.5 (book-evaluator, 7 dims) -> evaluations/chapter-%s-eval.md\n' "$N"
printf '  [ ] PACING check vs neighbors (length band, dialogue share, emotional slot, hook)\n'
printf '  [ ] update feedback/progress.md + feedback/pov-map.txt\n'
}

# Exit status reflects the gates (it used to exit 0 even when a gate printed FAIL — an evaluator caught it on
# The Hour of Ash Ch.20). Non-zero means: read the FAIL lines above before trusting the chapter.
OUT="$(mktemp)"; trap 'rm -f "$OUT"' EXIT
run_all 2>&1 | tee "$OUT"
FAILS=$(grep -cE "RESULT: *FAIL|over a figurative ceiling" "$OUT" || true)
if [ "$FAILS" -gt 0 ]; then
  printf '\n*** %s gate line(s) FAILED — the chapter is NOT clean ***\n' "$FAILS"; exit 1
fi
printf '\nALL MECHANICAL GATES CLEAN\n'
