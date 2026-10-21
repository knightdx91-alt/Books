# Sygl — pending fixes from outside reads (NOT APPLIED)

Status 2026-10-21: held by the author until the ChatGPT close reading ("Installment" files) is in.
Nothing below has touched the manuscript.

## Sources
| Read | File | Triage |
|---|---|---|
| Muse, chapter notes | feedback/muse-reading-notes-2026-10-21.txt | evaluations/muse-triage-2026-10-21.md |
| Muse, sentence-level close reading (8,335 sentences, 664 flags) | feedback/muse-close-reading-2026-10-21.txt | evaluations/muse-close-triage-ch01-09.md, -ch10-18.md, -ch19-30.md |
| ChatGPT close reading (29 installments, 1,357 notes) | feedback/chatgpt-close-reading-2026-10-21.txt | evaluations/chatgpt-triage-ch01-09.md, -ch10-18.md, -ch19-30.md |
| ChatGPT editorial assessment | feedback/chatgpt-editorial-assessment-2026-10-21.txt | (story-level; mostly conflicts with rulings) |

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

## ChatGPT round (2026-10-21)
- 25 more apply-ready edits: `fixsets/gpt-ch01-09.py` (11), `gpt-ch10-18.py` (5), `gpt-ch19-30.py` (9). Now included in `apply_all.py`.
- All 256 edits (231 Muse + 25 ChatGPT) tested together: no collisions; all four gates clean; **89,913 words (87 under 90k)**.
- Strongest agreements (both readers): juggling with no left hand as a boy; Bal's surname in Ch.1; concrete -> stone;
  72-hour flowers; Viridia's ring terms; "nearly two hours"; "Bal knew he was telling the truth" -> "believed";
  cask dent; war-rule wording; "Heath meant nothing".
- ChatGPT's pressure points: purification rune NOT planted (GB3 plants it in Ch.9 — take this OR Muse's Ch.18 version, not both);
  Toma's "no inheritance gift" is a deliberate script payoff (GB8 adds "The file had been wrong."); life bond named in Ch.29 only
  (script; leave); injuries consistent except Ch.17 head (G17.22/G17.25) and Ch.29 "none left in him" (GB9).
- Offset to reach 90k without inventing plot (recommended set, ~+105): Ch.5 "Nobody else was awake yet to say goodbye to." (+9);
  Ch.18 healed-scar line (+11); Ch.22 Xavier's directions to the Winespring (+10); Hopper stays at the dorm (+15);
  Ch.22 Bal's pitch and Xavier's objection in 2-3 lines (+60).
- Small author calls: Ch.10 "I'm nothing like anyone else you've known" -> "I won't treat you the way other people have."?;
  keep "Nothing spilled" and "Probably" (drop/amend pending 14.112 and 15.081)?; Ch.22 "wrote ahead" -> "will write ahead"?;
  Ch.3 statue "the face it lit was hers" (new detail)?

## Author decisions (2026-10-21, one by one)
1. Ch.13 bookshop line: **B** — restore the script wording "I'm not like anyone else you've known."
2. Ch.14: "Her eyes had gone bright behind her glasses. Nothing spilled." -> "Her eyes had gone bright with unshed tears behind her glasses." (author's own wording; "Nothing spilled" dropped; REPLACES pending fix 14.112). Ch.15: take Muse's fix 15.081 as pending ("Going by the teachers' faces, the school would make it a rule.").
3. Ch.22 Xavier: **A** — "Rooms will be waiting for you at the Winespring Inn," he added. "Lady Amelia will write ahead to arrange them."
