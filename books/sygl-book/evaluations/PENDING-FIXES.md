# Sygl — pending fixes from outside reads (NOT APPLIED)

Status 2026-10-21: held by the author until the ChatGPT close reading ("Installment" files) is in.
Nothing below has touched the manuscript.

## Sources
| Read | File | Triage |
|---|---|---|
| Muse, chapter notes | feedback/muse-reading-notes-2026-10-21.txt | evaluations/muse-triage-2026-10-21.md |
| Muse, sentence-level close reading (8,335 sentences, 664 flags) | feedback/muse-close-reading-2026-10-21.txt | evaluations/muse-close-triage-ch01-09.md, -ch10-18.md, -ch19-30.md |
| ChatGPT close reading (installments) | Drive, not yet read | — |

## Apply-ready fixes (story unchanged): 231 edits
- Round 1 (Muse notes): B1–B12 — `fixsets/muse-round1-B1-B12.py`
- Close reading Ch.1–9: 60 edits — `fixsets/close-ch01-09.py` (FIXES; OPTIONAL list = optional cuts)
- Close reading Ch.10–18: 78 edits — `fixsets/close-ch10-18.py`
- Close reading Ch.19–30: 81 edits — `fixsets/close-ch19-30.py`
- Apply all at once: `python3 evaluations/fixsets/apply_all.py` (exactly-once check per edit).

Tested together on a scratch copy (2026-10-21): all 231 apply with no collisions; style, grammar,
tic_report --gate and voice_wear_check (strict) all clean. **Word count after: 89,841 — 159 below the
90,000 target.** Offset needed (see below) before or with applying.

## Word-count offset options (author's call)
- Ch.22: dramatise Bal's pitch and Xavier's objection in 2–3 lines instead of summary (~+60).
- Ch.18: plant the purification rune in the rune montage (~+15).
- Ch.27: "He had nothing to eat, and did not look for anything." (~+11).
- Ch.13: Soren knows "Norheart" because the claiming story reached New Spring (~+6).
- Ch.22: Xavier's directions to the Winespring (~+10); Hopper stays at the dorm (~+15).
- Or hold back some of the 231 cuts.

## Author's-call items (highlights; full lists in the triage files)
- Right-palm whip: optional one line, "Blood magic had no need of the sygl hand." (Ch.20)
- Ch.12 "That honestly is all she told me": recommended polish "She only said you liked me. That's all, I promise."
- Leave (script or ruling): conversion pacing, both-at-once conversion, climax by accident, Ch.27 mysteries,
  ring's "other things", Amelia's memories withheld, Ch.30 recap length, Muse's "agency pattern",
  "those three beautiful women", "Converted. Last night." (correct), "movie" simile (world has TV).
