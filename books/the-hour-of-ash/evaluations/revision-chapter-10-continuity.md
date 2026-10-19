# Revision Report: Chapter 10, continuity repair

**Date:** 2026-10-19
**Source:** `evaluations/continuity/chapter-10-audit.md` (run 2): 1 CRITICAL, 9 WARN. W-09, the bible sync, is out of scope here and happens separately.
**Paragraph numbers** follow the audit's convention: prose paragraphs only, numbered on the pre-repair page.

**Result:**
- **Length:** 2,528 → **2,563** words by shape_check (style_check 2,574).
- **Dialogue:** 39% by shape_check (raw 38.6%; show/tell meter 36.5%).
- **Sentence median:** 15 (mid gear).
- **Breaks:** 0.
- **Paragraphs:** 98 → 97 (p94–p95 deleted; one paragraph added at p61).
- **First sentence:** unchanged.
- **Close:** "It was a good while yet till the lamps." (9 words), classed `quiet` by shape_check.

## Prior text verified before editing

Every citation in the audit was grepped against Ch.1–9 and voice-bank samples 01–13 on disk, and all held:
- **Ch.8:** "Once the road's clear of snow he sits down in his house" (ch-08 l.202).
- **Outline:** Ch.11 "She mends harness for a week anyway" (outline l.417); Ch.12 "the seventh of Bysios is three days off" (l.451).
- **Sample-12:** "inside her belt", "folded it along its old creases", "I heard the broom", "I said that I would air it." / "I'll do it.", the goat, and "finished shelling the beans".
- **Ch.2:** "I folded it back along its own creases" (ch-02 l.145).
- **Patrae:** ch-06 l.664 and ch-09 l.394 both read "Patrae"; "Patrai" occurs 0 times outside Ch.10.
- **The oil-seller:** 0 times in Ch.1–9.
- **Ch.6:** "as far in as my arm would reach" (ch-06 l.6) and "I had no answer to that." (ch-06 l.550).
- **The ashes as Mara's dawn chore:** ch-05 l.411 and l.429, ch-06 l.310.
- **Domna and Iamblichos:** 0 times in Ch.1–9.

## Issues addressed

| ID | Before | After | Δw |
|---|---|---|---|
| **C-01** (p13) | "Have you a room? Three nights, till the god opens his house." | "Have you a room? I'm here till the god opens his house." | 0 |
| **W-01(a)** (p20) | "The letter went inside her belt, against her stomach, and she returned to the pots." | "She pushed the letter down behind her belt, against her stomach, and returned to the pots." | +1 |
| **W-01(b)** (p91) | "At dawn they had been swept already; from my mat I had heard the broom. It went to the lip of the gallery…" | "At dawn they had been swept already; I had been carrying out the ashes when she did them. She took it to the lip of the gallery…" | +3 |
| **W-01(c)** (p97) | "I folded the papyrus down along the folds it had come in, and it made a fatter packet than before." | "I folded the papyrus, and it made a fatter packet than before." | −8 |
| **W-01(d)** (p93–p95) | p93 ended "…He can have Ariston's room, at the three obols." It was followed by "Shall I go up and open it?" / "He can lift a latch." | p94–p95 deleted. p93 now ends "…He can have Ariston's room, at the three obols. If he comes to the gate before I find him, he waits in the court." | +3 |
| **W-01(e)** (p98) | "Out in the lane somebody was driving a goat that was against the whole idea, and a woman's voice was telling him so." | "Out in the lane a woman was shaking her blanket over the neighbor's wall, and the neighbor was telling her where else she might shake it." | +3 |
| **W-01(f)** (p98) | "…The step was in shade. It was a good while yet till the lamps. Half the basket was still to clean, and I pulled it back onto my knees." | "Half the basket was still to clean, and I pulled it back onto my knees. Out in the lane [e]. The step was in shade. It was a good while yet till the lamps." | 0 |
| **W-02** (p97) | "Before I folded it I read it once more, without moving my lips. To myself it was a cheerful letter, from a man with a roof to sit on in the evenings." | "Before I folded it I read it once more, without moving my lips, from the greeting down to the date." | −11 |
| **W-03** (p33) | "I took a wife here: Domna, the daughter of Iamblichos…" | "I took a wife here: Shalmath, the daughter of Iamblichos…" (Iamblichos is kept, so p37 and p85 stand) | 0 |
| **W-04** (p26) | "…given me my discharge before my time, with the money that goes with it." | "…given me my discharge before my time, and paid me out what I had saved at the standards." (p44's "the money from the cohort" stands) | +4 |
| **W-05** (p6) | "She heard that with the face she wore at the oil-seller's." | "Her face gave him nothing for that." | −4 |
| **W-06** (p20) | "The man from Patrai" | "The man from Patrae" | 0 |
| **W-07** (p21) | "…held it toward me across the wool, as far as her arm would reach." | "…held it toward me across the wool at the length of her arm." | −1 |
| **W-07** (p54) | "She wanted no answer to that, and I gave her none." | "She wanted no reply to that, and I made none." | −1 |
| **W-08** (p45) | "…returned the book across the desk at Van Pelt with the castle still in it. For a week I had wanted it back. My voice went on through the oxen without me." | "…with the castle still in it. My voice went on through the oxen without me." | −8 |
| **Thinness** (p61, new paragraph) | (Kallia's response to the missing line was one sentence plus a wool beat) | "She went to the front of the lean-to, where a reed blind hung rolled up under the eave, and pulled the slip-knot on its cord one-handed. The blind dropped open to the ground between the jar and the sun, letting down a winter's soot and a dead wasp. She came back to her place." | +55 |

**Net change:** −19 for the fixes by hand count, then +55 for the earned paragraph. shape_check measures 2,528 → 2,563, a 1-word difference from tokenizing contractions.

### Notes on specific fixes

- **W-01(b), connective repair.** The new clause cut "It" off from its antecedent, "the broom". "It went to the lip of the gallery" therefore became "She took it to the lip of the gallery". This is the one word beyond the audit's proposal.
- **W-01(e), echo repair.** The audit's wording, "shaking a blanket over her neighbor's wall", tripped the echo scan: "blanket over her" is already at ch-08 ("old blanket over her shoe"). I tried "blanket out over her", but "out over her" is in sample-11. The final wording, "shaking her blanket over the neighbor's wall", has 0 prior uses.
- **W-01(f).** The chapter still ends on a plain moment of the ongoing day, with no hook, no weighted image and no aphorism. The legume chore is no longer the last act.
- **W-02.** "roof" drops from ×7 to ×6.
- **W-03.** "Shalmath" has 0 uses anywhere in the book.

### Thinness, the earned paragraph (p59–p62, as the audit directs)

**What it is:** Kallia's one physical act at the moment the letter turns out to have no line for the house. On the first warm afternoon she lets down the lean-to's summer blind to put the water jar in shade. That is work on her own axis (hauled water and what it costs) done for the house the letter left out. The text does not explain it.

**What it avoids:**
- It is not a bend, a touch, a sit or an involuntary hand reaction, and it is not spinning.
- "one-handed" implies the wool in her other hand without adding a third wool beat.
- It adds 0 to the object-handling class and 0 to bend/stoop.

**Continuity:** The jar stands by the lean-to hearth (ch-05 l.409). The blind's soot ties forward to "Keep it out of the smoke". "She came back to her place" returns her to "from where she stood" at p64.

**Drafts rejected:**
- **Carrying the morning's wood to the hearth:** it collides with ch-07 l.394 ("She was at the woodstack, pulling out splits for the morning"), and wood is already spent on Kallia in Ch.6–8.
- **"free hand":** already at Ch.3 and Ch.8.
- **"untied":** Kallia's Ch.6 kerchief knot.
- **"unrolled":** in sample-02.
- **"came back out into the court":** it pushed "out into the" and "into the court" to 3 uses book-wide, which fails the tic gate.

**Freshness:** every new string was grepped against Ch.1–9 and samples 01–13 and has 0 prior uses. The list:
- reed blind, eave, slip-knot, one-handed, dropped open, the jar and the sun, letting down, winter's soot, dead wasp, back to her place;
- behind her belt, carrying out the ashes, waits in the court, before I find him;
- from the greeting, down to the date, paid me out, saved at, the standards, Shalmath;
- face gave, gave him nothing, length of her arm, no reply, made none, her blanket, the neighbor's wall.

## Strengths verification

**First sentence:** unchanged ("The letter had been folded down very small.", short-punch).

**HARD no-parallel rule.** The two near-misses the audit flagged are gone:
- W-02's private "cheerful letter" line;
- W-08's "wanted it back".

No new line compares Ariston's choice with Mara's.

**The anchor:** the broom across the threshold is intact at p91 and p96.

**Kallia's card:**
- She never sits and never touches Mara.
- She says "Ariston" once (p93).
- Her new speech line is an order.
- Her new act is labor.
- Her yawn is still her one involuntary reaction.

**Mechanical counts:**
- **NO FORESHADOWING:** foreshadow 0 (style clean).
- **NO TICS:** voice-wear strict clean; tic gate clean; echo scan 0; command echo 0; bend/stoop 0 in Ch.10.

**The chaos beat** (the second sweep, p91) is intact. The act at p61 is practical, not irrational, so it does not compete with the sweep.

## Gates (run from /home/user/Books)

**`bash books/the-hour-of-ash/tools/check_chapter.sh 10`:**
- **Style:** clean (simile 0.4/1k, adverbs 2.7/1k, em-dash 0).
- **Grammar:** 0 errors.
- **Rhythm:** 0 flagged.
- **Show/tell:** dialogue meter 36.5%, no flags.
- **Voice-wear (strict):** clean.
- **Tic gate:** clean.
- **Echo scan:** 0.
- **Metaphor:** fig 0.4/1k, median 15, 0% over 40 words.
- **Shape audit:** CLEAN.

**`python3 books/the-hour-of-ash/tools/tic_report.py --echoes 10`:** 0 echoes, 0 command-echo candidates.

## Changes not made

- **W-09 (bible sync):** out of scope by instruction. The sync must pick up everything this repair changed:
  - the deletions: "He can lift a latch", the goat, the "cheerful letter" line, "For a week I had wanted it back", the oil-seller face, and "inside her belt", which becomes "behind her belt";
  - the new lines: "If he comes to the gate before I find him, he waits in the court." and the reed-blind act;
  - the names and money: Patrae, Shalmath and the standards savings;
  - the move of "a good while yet till the lamps" to the close.
- **NOTES N-01 to N-25:** not applied. N-05 and N-06 are optional cuts, which the audit says to skip.

## Concerns for re-evaluation

- **The reed blind is a new object in Kallia's lean-to.** The entity tracker should record it. The evaluator should judge whether the blind reads as plain work or as a weighted image. It sits 36 paragraphs before the PLAIN STOP.
- **The new close order** ends on the lamps, with the chore third from last. Confirm it reads as the afternoon going on and not as a button.
