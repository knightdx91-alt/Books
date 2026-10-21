# Book fix pass: Ch.1–10 (2026-10-21)

Sources: eval-full-manuscript.md, continuity/full-manuscript-audit.md. Cuts and swaps only.

## All chapters
- Changed "grey" to "gray" everywhere (narration and dialogue, including "graying") and stripped all `<!-- -->` comments (Ch.9, 10).

## By chapter
- **Ch.1:** "At the start of the summer" became "Earlier in the year", so the season stays neutral (WARN-003, per author note).
- **Ch.3:** Removed Amelia towing Bal (WARN-005): "Amelia waited while he stood, then set off…". Cut "She squeezed his fingers." and merged the quote that cut left glued. Fixed the steps stutter: the line now ends at "into the sun." and "Amelia stopped on the bottom step". "Bal pulled Amelia inside" became "took", since pulling is Viridia's gesture.
- **Ch.4:**
  - "in two weeks" became "any day now".
  - Cut the feet-swing.
  - Merged the "Mostly," and "That, and…" tags.
  - "Bal got up off the bed."
  - "longer than you'd believe"
  - "She went out ahead of him…"
  - Kept the fist beat, which is the one the reports keep.
- **Ch.5:**
  - The hand on the blanket is no longer flexed.
  - Cut the heel-swing and the potatoes wonder.
  - Verin gestures at his own back, and the sweater's blank place is now "between the shoulders".
  - Cut one "grinned" and the pain-tolerance line.
  - Cut the bedtime last line.
- **Ch.6:** "twisted to check his own back". Deleted the fist close/open beat and the god-catching-cold wonder.
- **Ch.7:**
  - Merged the joined quote.
  - Changed the sygl "on his chest" to "on his back as he passed".
  - The "just where Verin had promised" sentence now reads "Verin had said it would."
  - Added the optional ruling clause: "The two boys must only have shared her ride."
  - Kept the plates musing, the only wonder aside left in Ch.1–10.
- **Ch.8:** The chapter now ends on "Then she let go."
- **Ch.9:** Cut the raven-cheese wonder. Library line rewritten per NOTE-005 ("upstairs, as promised: …"). "travelling" became "traveling".
- **Ch.10:** Merged the joined quote. The rapier is now in "his hand". Cut the leg-kicking, so the only feet-swing left in this range is Ch.2's.

## Gesture clusters
About 30 swaps of look, sit and tilt words in Ch.2–10. Real clusters went down everywhere. The scanner hits that remain are mostly false positives ("started up", "one look at… one look at") and were already in the text before this pass.

## Gates
`style_check.py`, `grammar_check.py`, `voice_wear_check.py` and `tic_report.py --gate` are all clean book-wide.

## Outside my range
- Ch.19 (another editor's change) adds "Amelia had told him". I re-worded Ch.9's copy of the phrase, so it no longer trips the gate.
- Ch.11–30 gates are clean as of this run.
