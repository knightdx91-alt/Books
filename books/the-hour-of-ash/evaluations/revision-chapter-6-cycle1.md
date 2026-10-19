# Revision Report: Chapter 6, Polish Cycle 1

**Editor:** book-editor | **Date:** 2026-10-19
**Input:** `evaluations/chapter-6-eval.md` (POLISH; Floor 8.0, held by Prose & Voice alone), the orchestrator's brief, `evaluations/disruption-chapter-6.md`, STATE.yaml guardrails, voice-dna.md, character-bible.md, ENTITY_STATE.yaml (Valens).
**Backup of the pre-cycle text:** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/chapter-6.pre-cycle1.md` (scratch only).

## Numbers
| | Before | After |
|---|---|---|
| Prose words (shape_check) | 6,680 | **6,643** (−37) |
| style_check words | 6,690 | 6,653 |
| `wc -w` (includes header comments) | 6,806 | 6,797 (the header comment grew; prose went down) |
| Dialogue (shape_check, ledger metric) | 37% | **38%** (band 35–45) |
| Breaks | 2 | 2 |
| Median sentence | 11 | 11 |
| First sentence / final spoken line | — | byte-identical (diffed) |

## Gates (run from /home/user/Books)
`bash books/the-hour-of-ash/tools/check_chapter.sh 6`: style clean (simile 0.9/1k, adverb 3.2/1k, em-dash 3, foreshadow 0) · grammar 0 · rhythm 0 flagged · show/tell no flags · voice-wear strict clean · tic gate clean (and-chains 5, credential asides 1) · echo scan 0 · metaphor no flag (fig 1.4/1k) · shape CLEAN.
`python3 books/the-hour-of-ash/tools/tic_report.py --echoes 6`: **0 echoes.**

## Issues Addressed (before → after)

### Logic (eval Revisions #1–#3, #14; Pacing holds)
| # | Where (eval ¶) | Before | After | Note |
|---|---|---|---|---|
| 1 | ¶562 firs seam | "…the flakes settling between them. We were under the firs before I saw them. The light went off the snow…" | "…the flakes settling between them. The light went off the snow…" | The firs now arrive once, at "We came in among the firs". |
| 2 | ¶272 father's mornings | "My father had wound it at the kitchen counter each morning of my childhood while the percolator went…" | "My father had wound it at the kitchen counter on the few mornings he was there, while the percolator went…" | Fits "maybe twice in my whole life" (¶336) and Ch.3's July. Avoids Pat's "When he was home". Anchor otherwise byte-identical. |
| 3 | ¶18 duffel (audit N-22) | "Behind him my duffel leaned on the slab" | "At his feet my duffel leaned on the slab" | "Beside him" set off an echo ("standing beside him", Ch.1), and a bare "My duffel…" made a My/My opener pair that rhythm_check flagged. "At his feet" clears both. |
| 4 | ¶208–¶210 hiccup | "I will not." / (new ¶) "I will go up without you," I said. | "I will not. I will go up without you." | Merged into one paragraph with no tag. The eval's tagged version ("…," I said. "I will…") set off the "i said i will" echo (Ch.4). Speaker is clear from the alternation. |

### Orchestrator fix (the route)
| # | Where | Before | After |
|---|---|---|---|
| 5 | ¶82 | "…before it came to me that I had no idea of the way." | "…before it came to me that I had no idea how to get from the town up onto the plain." |

She knew the plain-to-cave route in Ch.5. What she lacks is the climb from the town, and the next sentence ("between the plain and Delphi stood only cliff") now supports this directly.

### Character (eval Revision #4, the Valens body sentence)
| # | Where | Before | After |
|---|---|---|---|
| 6 | ¶94 | "He leaned on her shoulder and said something into her ear, low and level, in Latin." | "He leaned on her shoulder, and she had to brace a foot under his weight; his hands were older than the rest of him. He spoke into her ear, low and level, in Latin." |

The new sentence is 24 words. The gray mule shows his size by bracing under his weight. Mara's repairer's eye, which reads wear, gives his age: his hands, with the laddered scar from the paragraph above, look older than he is. There is no look sequence, no face, eyes or teeth, no beauty word and no romance signal. ENTITY_STATE holds: the scar stays on the back of his right hand (¶90, untouched), and "big, unhurried, ~32" stays unstated but now readable. A first draft used "he was younger than his hands", which echoed Ch.5's "He was younger than I was" and failed voice-wear strict. A second used "He said something…", which echoed Ch.5. Both were recast.

### Prose and law items (eval P1–P9, PATH items 1–9)
| # | Item | Before | After |
|---|---|---|---|
| 7 | P1 ¶664 (frozen pivot) | "The mule did not pull; she sat back on her haunches…" | "The mule sat back on her haunches…" |
| 8 | P1 ¶28 (same frame across a stop) | "He found it in the pouch at his belt and did not give it to me. He let me see it in the torchlight, lying on his palm…" | "He found it in the pouch at his belt and let me see it in the torchlight, lying on his palm…" (the thumb on the band still says he won't hand it over) |
| 9 | P2 ¶236 | '"You've got that." He meant the coin. "Who's coming after you?"' | '"You've got that coin. Who's coming after you?"' |
| 10 | P2 ¶626 | '…She won't mind." He meant the kiln.' | '…She won't mind."' ("Nine days she's been at it" / "Easy, girl" carry it) |
| 11 | P2 ¶422 (the fourth "meant") | "It took me a little while to understand that he meant the watch." | "It took me a little while to understand he was asking about the watch." |

After items 9–11 the chapter has **one** narrator "He meant" gloss: "He meant the gray mule and my laughing." (¶236, kept as the eval directs).

| # | Item | Before | After |
|---|---|---|---|
| 12 | P3 ¶8 (Ch.3's crack wording) | "Now the whole mountain had turned to cold: the rock, the air, the iron of the shovel, which…" | "Now the whole mountain had turned to cold, down to the iron of the shovel, which…" |
| 13 | P3 ¶500 | "The rock was cold. The air did not move." | "The rock was cold. Behind me the torch flame stood straight up." |

Item 13 shows the dead draft as a flame with no lean, in new words that are not Ch.3's "air moving", and it removes one paragraph-final negation. ¶486 ("Rock. Air. Cold that was only cold.") and ¶20 are kept, as the eval directs.

| # | Item | Before | After |
|---|---|---|---|
| 14 | P4 ¶336 (Ch.5 content) | "I mend broken things in a basement for money, and I'm good at it, which nobody here is ever going to find out." | "I make the cracks in old pots disappear, and I'm good at it, which nobody here is ever going to find out." |

Item 14 drops "basement", "for money/for a living", "back together" and "out of the ground". The irony clause is kept. The rest of the confession is byte-identical.

| # | Item | Before | After |
|---|---|---|---|
| 15 | P5 ¶498 (anaphora triad) | "I did the water this morning. I did the floors every day for a month. I did everything anybody asked me. Please." | "I did the water this morning. I've done the floors every day for a month, and everything anybody asked me. Please." |
| 16 | P6 ¶524 (4-gram from the repair) | "I ate it crouched in the mouth of the crack with my bleeding hand held away from it…" | "I ate it bent under the low roof of the crack with my bleeding hand held away from it…" (word-neutral; "crouched in the mouth" now ×1, Valens ¶468) |
| 17 | P8 ¶516 (explains the laugh; the Emotion 9.0 lever) | "…a laugh with nobody at the end of it. I had been laughed at on the Sacred Way, in front of half the Way, and I knew the difference even in the dark with my hand bleeding." | "…a laugh with nobody at the end of it." (the recommended cut; the Way/Way clunk and the lit-torch "dark" go with it) |
| 18 | P9 ¶72 (fourth body measure) | "came away whole, broad as my two hands, and under it…" | "came away whole, and under it…" (body-unit measures now 3, at the ration) |
| 19 | P7 ¶186 / ¶628 (second uses) | "He took in my boots, which…" / "Valens would have gone by. I watched him decide it. But the gray…" | "He looked down at my boots, which…" / "Valens would have gone by. But the gray…" |

For ¶186 I used "looked down at my" rather than the eval's "looked at my", which would have made a within-chapter 4-gram with ¶228's "he looked at my hands".

## Strengths Verification
- The first sentence and the final two paragraphs are byte-identical (diffed against the backup).
- Strength #15, the anchor (¶254–¶292), is byte-identical except fix #2, which the eval permits.
- Strength #24, the wall (¶496–¶534), is changed only by the permitted items 13, 15, 16 and 17. "The noise I made had no word in it.", the echo, "Valens laughed.", "a laugh with nobody at the end of it", "Good.", "exactly the temperature of a person", "salted it with conviction" and "It was the first thing you did up here I understood." are untouched.
- Strength #18, the confession and "Philadelphia", is untouched apart from the one job clause (#14).
- Strengths #3, #9, #14 and #27 (Kallia's lane, the watch hand-over, the descent's welfare questions, the English slip): untouched.
- Strength #6 (the ladder scar, ¶90) and #8 (the gray "would not consider anything"; "It was the plain truth about her, and I laughed." / "The gray walked on."): untouched. The body sentence sits between them and keeps the Latin line and the gloss as they were.
- The disruptor's operations are all intact (the refrain rework, the English slip, "Ditch.", the cuts). None was reverted.

## Changes Not Made (and Why)
- **#15, the Latin gloss (¶94):** optional. The joke needs it, and Ch.5 set the precedent.
- **#16, the Valens/Kallia "who carries the cost" overlap:** the eval says no change in Ch.6.
- **#17 (character-bible sync) and #18 (pipeline regex and the within-chapter 4-gram gate):** bookkeeping and root-pipeline work, outside a chapter polish. These go back to the orchestrator.
- **#1 and #5 minor patterns** (the "Then…" retorts, "like a model under glass", "loaded to the ears"): not on the PATH, and the "Then…" retorts are a preserved strength.

## Concerns for Re-evaluation
1. **The body sentence (¶94):** check that "she had to brace a foot under his weight" reads as size and not clumsiness, and that "his hands were older than the rest of him" reads as Mara dating wear, not as a romance glance. It is one sentence, it comes after the scar, and it is not an inventory.
2. **"I make the cracks in old pots disappear"** is spoken while she is digging at a crack. That irony is hers, in the scene, with no forward reach. Confirm it does not read as engineered (#18).
3. **The untagged "I will not. I will go up without you."** Speaker attribution rests on the alternation after "Why tomorrow? It'll be there in the spring."
4. Paragraph-final negations are down by one (¶500). "Nothing moved across them." (¶20) stays, as the eval directs.
5. For the bible's at-risk list (orchestrator): "He meant [X]." used 1 in Ch.6; "took in my" SPENT; watching someone "decide" SPENT; "crouched in the mouth" 1.
