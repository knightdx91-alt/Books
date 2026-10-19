# Revision Log: Chapter 7, continuity repair

**Date:** 2026-10-19
**Source:** `evaluations/continuity/chapter-7-audit.md` (run 2): 2 CRITICAL, 20 WARN.
**Applied:** C-01, C-02, W-01 to W-18, W-20. **Skipped:** W-19 (the character-bible sync is done separately).
**Method:** each cited prior passage was re-checked on disk (Ch.1–6 and the voice-bank samples) before the fix went in. Every changed span was then n-gram-checked at 3 to 6 words against Ch.1–6, the samples and Ch.7 itself. Paragraph numbers follow the audit's convention (prose paragraphs only).

## Changes (before → after)

| ID | Where | Before | After | Note |
|---|---|---|---|---|
| C-01 | p140 | "I had been to Syracuse, as it happened, at fourteen, in a rented Fiat, with my father driving one-handed and pointing out of the window at quarries from Catania on. I remembered a fountain full of papyrus and ducks, and a gelato that tasted of nothing but cold." | "I knew Syracuse, as it happened, from his slides: a quarry deep enough to stand a church in, a fountain full of papyrus and ducks, and his voice in our dark kitchen telling me the gelato there tasted of nothing but cold." | Audit wording. Verified against foundation §3 ("never took her"), ch-01 (the September slides; the taxi "for Sicily") and ch-06 ("maybe twice"). It avoids "every September" and "bedsheet". |
| C-02 | p10 | "a himation the color of wet sand" | "a himation of wet-sand brown" | Audit wording. The shape is spent at ch-01 "pink of boiled ham" and "color of an old nickel". |
| C-02 | p151 | "pale in the dark wax, the color of the wood showing through" | "pale in the dark wax where the bare wood showed through" | Audit wording. "the color of" is now 0 in Ch.7. |
| W-01 | p71 | "and I said nothing outside Kallia's gate after that, to anyone, for a month." | "and for a month after that, outside Kallia's gate, I said nothing to anyone if I could help it." | Audit's "that I could help" read as "anyone that I could help", so it became "if I could help it". Leaves room for p158 and p163, and "nineteen days" (p159) still marks the break. |
| W-02 | p174 | "I had spent fifteen years at a bench keeping things" | "For ten years I had sat at a bench keeping things" | Audit wording "had given ten years … smooth" echoed ch-05 "a speech he had given ten thousand times, worn smooth", so I recast it. Matches ch-03 "ten years in a basement lab" without its 4-gram. |
| W-03 | p180 | "What name did you give him?" | "Say your name for me." | Audit wording. Kallia stood beside Mara at p158, so the old question made no sense. |
| W-04 | p135 | "you came on the last boat before the sea shut" | "you came on one of the last boats before the sea shut" | Audit wording. Verified against ch-06 "The last ship went out of Kirrha eight days ago" and "Since the olives". |
| W-04 | p153 | "She came on the last boat, after the vintage." | "She came on one of the last boats, after the vintage." | The rehearsed cover line is still said twice, as before (Kallia coaching, then Kallia to the clerk). |
| W-05 | p161 | "among the sea-nymphs" / "a sea-nymph or a star with four legs" | "among the Nereids" / "a Nereid or a star with four legs" | Audit wording. The narration no longer touches the rumor's word (ch-04 "Nymphē."; ch-06 "a nymph", "The nymph."). |
| W-06 | p174 | "and laughed into it. I laughed without a sound, with my shoulders. I could not stop." | "and laughed into it without a sound, with my shoulders." | **Not the audit wording.** "until it had run its course" would bring back the "laughed until [result]" shape, which the bible lists as SPENT after Ch.3. A purely subtractive fix: the loss of control is gone, so the Ch.22 laughter break stays unspent. |
| W-07 | p92 | "There was no Greek for that, and no English either." | "Hers was the one question I could not answer by doing something." | Audit wording. The spent "(n)either language" family is gone and the paragraph no longer ends on a negation. |
| W-08 | p58 | "and I knew to the grain what a powder like that did to a glazed surface if you let anybody near the glaze with it, and the girl" | "; I had seen burnished slip scoured to a dull fog by less, and the girl" | **Adjusted from the audit.** "glazes" became "burnished slip" because the bible marks glaze comparisons SPENT (Ch.2, Ch.6). Removes the ch-05 "I knew to the decimal what … did to the" frame and one "anybody". |
| W-09 | p59 | "had decided it ought to have and with every breathing breathed, and the Greek" | "had decided it ought to have, and the Greek" | Audit wording, a cut. |
| W-09 | p63 | "with the breathing on the front of the word and the pitch climbing wherever the accent stood" | "careful with every syllable" | Audit wording. Not "best Attic" (ch-05) and not "the way the books printed it" (ch-04). |
| W-10 | p160 | "once who asked for a cup of water like a man in a play." | "once, and half the stand had to help him get a cup of water." | Audit wording. The listener's comparison for her Greek is closed. |
| W-11 | p184 | "in the fourth grade, in a green cardigan with the second button gone" | "in fourth grade, in a green cardigan short of its second button" | Audit's "that had lost its second button" echoed ch-05 "a brown cloak that had lost the pin of its brooch", so I used "short of" instead. The green and the missing button (canon) are kept. |
| W-11 | p76 | "the hearth was down to a red bed under the ash" | "the hearth had burned low" | Audit wording (sample-12 lift). |
| W-11 | p36 | "The women of Delphi, so far as I could tell" | "Delphi's women, so far as I could tell" | Audit wording (sample-03 lift). |
| W-11 | p161 | "as plainly as a man spelling a word he had seen all his life" | "as easily as a man spelling a name he had known all his life" | Audit wording. Also clears the third book-wide "as plainly as a" (ch-02, ch-03). |
| W-11 | p183 | "and Kallia told him the hedge was better company" | "and Kallia answered that the hedge was better company" | Audit's "and Kallia said" is itself a 3-gram in sample-04 ("and Kallia said Syracuse"), so it became "answered that". |
| W-11 | p38 | "looked at me over it" | "eyed me over it" | Audit wording (sample-02 lift). |
| W-11 | p48 | "turned it to the window to look" | "turned it toward the window to look" | Audit wording (sample-09 lift). |
| W-12 | p184 | "…said we could go. I never found out why, and nobody else in that room did either, so far as I could tell." | "…said we could go." | Audit wording, a cut. The paragraph no longer copies ch-06's Larchwood "nobody ever learned" close. |
| W-13 | p100 | "Once on my good hearthstone and once on a Theban." | "Once on my good hearthstone and once in the lentils." | Audit wording. The "a Theban" victim no longer carries over from ch-06. The bible's SPENT mark goes in with the separate sync. |
| W-14 | p128 | "…bought one since." She swept the pieces off the hearthstone into the ash pail with the side of her foot. "Go back down and fetch the water in the old one. It leaks. Walk quick." | "…bought one since. Go back down and fetch the water in the old one. It leaks." She swept the pieces off the hearthstone into the ash pail with her toe. | Reordered per the audit. "Walk quick." and "the side of" dropped. Audit's "with her foot" doubled p18's "with her foot" for Kallia (no beat twice in a chapter), so it became "with her toe". |
| W-15 | p129 | "before the governor's men in Corinth thought to ask for it." | "before Rome put a governor back in Corinth to ask for it." | Audit wording. Verified against foundation §3 (the freedom of 67 abolished the post). |
| W-16 | p95 | "who slept in the room at the top of the stair" | "who slept in the shut room upstairs" | Audit wording. One location for the room (p37, the end of the gallery). |
| W-17 | p85 | "I mend old pots for my living, pots older than this house, that somebody has dug up." | "My work is pots older than this house, that somebody has dug up." | Audit wording. The job formula is no longer repeated (ch-03, ch-05 "for a living", ch-06). |
| W-18 | p10 | "without anybody in that house setting eyes on it" | ", unseen by a soul in that house" | Audit wording. |
| W-18 | p25 | "if nobody spoke to me" | "if the court stayed quiet" | Audit wording. |
| W-18 | p36 | "There were other lessons that nobody had to teach me, because the town did it for her." | "Some lessons the town taught for her." | Audit wording. |
| W-18 | p122 | "if anybody in Delphi had wanted a jar back that had been broken once" | "if Delphi had any use for a jar that had been broken once" | Audit wording. With W-08 and W-12: nobody 8→5, anybody 6→3, somebody 8 (thematic, kept), everybody 2. Total 24→18. |
| W-20 | p48 | "a round pitted mark about as broad as an obol and puckered in the middle" | "a round pitted mark, puckered in the middle" | Audit wording, a cut. |
| W-20 | p117 | "and one hand raised to steady it, as broad as a doorway." | "and one hand raised to steady it." | Audit wording, a cut. "as broad as" is now 0 in Ch.7. |
| (header) | comment | Word count 6,142 / wc 6,306 / Dialogue 21.6% | 6,041 / wc 6,213 / 21.3%, plus a repair note | Bookkeeping. |

## Held fixed
- **First sentence** (27 words, `narrative`) and **closing question**: untouched.
- **Breaks:** 3 (shape_check).
- **Dialogue:** 22% (shape_check) / 21.3% (show/tell meter), inside 20–30.
- **Gear:** median sentence 17 (metaphor_check and shape_check), 15.0% over 40 words.
- **Words:** 6,041 by shape_check (was 6,142); `wc -w` 6,213. At or above the 6,000 floor.
- Knowledge-provenance asides ("I knew X from"): 1 (C-01), under the cap of 2. Credential asides by the detector: 0.

## Gates (run from /home/user/Books)
- `bash books/the-hour-of-ash/tools/check_chapter.sh 7`: style clean (simile 2.3/1k, adverb 3.0/1k, em-dash 2); grammar 0 errors; rhythm 0 flagged; show/tell no flags; voice-wear strict clean; tic gate clean (and-chains 2, asides 0, negation pivots 0, gestures under cap); echo scan 0; metaphor fig 2.6/1k; shape audit CLEAN.
- `python3 books/the-hour-of-ash/tools/tic_report.py --echoes 7`: **0 echoes**.

## Left for the separate bible sync (W-19 and cascades)
- Mention-only list: remove the Fiat trip (C-01).
- At-risk: "the [color] of [thing]" CLOSED at 2 (C-02); spitting-oak haggle SPENT (W-13); spent entry becomes "a Nereid or a star with four legs" (W-05); the other at-risk additions in the audit's YAML block.
- `objects.the-girls-himation` description should read "wet-sand brown".
