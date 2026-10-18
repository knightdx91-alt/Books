# Revision Report: Chapter 3 (Parnassus), Polish Cycle 1 (run 2)

**Editor:** book-editor | **Date:** 2026-10-18
**Inputs:** evaluations/chapter-3-eval.md (Floor 8.0, Prose & Voice), evaluations/continuity/chapter-3-audit.md (12 WARNINGs), disruption-chapter-3.md (none of its three operations was reverted), Ch.1 and Ch.2, voice-dna §0/§1/§4/§7, STATE guardrails, the bible's at-risk list, ENTITY_STATE.
**Words:** 6,817 → **6,834** (`wc -w`). **Scene breaks:** 0. **Dialogue:** 5.8%. **Em-dashes:** 1. **Gear:** high (median 18).
**Unchanged:** the first sentence (the 79-word spiral) is byte-identical, and so is the last line ("I stepped out into October.", 5 words, its own paragraph). No dialogue was touched.

---

## Issues addressed (before → after)

| # | Issue | Type | Before | After |
|---|---|---|---|---|
| A1 | PATH 3: third use of "you could have [verb]" (¶21) | prose | "on a point of rock you could have covered with a saucer" | "on a point of rock the size of a saucer". I tried the evaluator's "no bigger than a" first, but it tripped the tic gate (3× "bigger than a" with Ch.1 and ¶11's church). |
| A2 | PATH 2: third watch against the wrist (¶155) | prose | "The steel case of the watch went cold against my wristbone as I stood there." | "Under my cuff the steel of the watch took the cold and held it." No "wrist" or "against my" in the watch beat. |
| A3 | PATH 1 / W-05: define-by-negation paragraph opener (¶155) | prose | "It was not cave cold. Cave cold was damp and slow and came off the rock. This came from the dark behind the rock, dry, and it had an edge to it, and it went in…" | "This cold came from somewhere behind the rock. It was dry and it had an edge, where the cold off the walls was damp and slow, and it went in…". The paragraph opens on the new sensation, and "cave cold" is down from 4 to 2 (¶117, ¶139). The freezer line also changed: "came out" → "rolled out", to avoid a second "came". |
| A4 | PATH 4 / W-12a: "some… some… some" triad (¶123) | prose | "Some had been dyed, and some drilled, and some filled with lead" | "Some had been dyed or drilled through, and a few filled with lead". Also fixed in the same paragraph (evaluator #13, factual): "tens of thousands" → "more than twenty thousand". |
| A5 | PATH 5 / W-08: hot ears at the theft pre-spend the blush (¶133) | prose | "My ears went hot. I stood up too fast, and the bag swung against my hip, and I looked out at the mouth," | "I stood up too fast and looked out at the mouth,". The crossing blush (¶161–163) is now the only heat in the face in the chapter, and the hip echo with ¶169 is gone. Book-wide "[body part] went/had gone hot" is now 2 (Ch.1 eyes, Ch.3 face). |
| A6 | W-02 / evaluator #1: September contradiction (¶141, the cellar memory) | factual | "the September I was seven… My father was home that September, which was itself unusual." | "the July I was seven… My father was home that July, which was itself unusual." This now agrees with ch.1:23 and ch.3:51 ("every September"), and July falls in the dig season, when he was away. |
| B1 | W-03: impossible slot entry (¶135 crack geometry; ¶159 entry) | structural (staging) | ¶135: "It ran up and down, not across. … Lower down it opened, so that at the level of my knees it was as wide as a narrow door turned on its side. … Beyond the bend the beam had nothing to land on." ¶159: "I went in sideways with my left shoulder first…" / "and I stood in the nothing" | ¶135: "The crack ran up and down. At the height of my shoulder it was just wide enough to take my forearm, and above that it pinched shut. Lower down it widened, and along the floor it was a good foot and a half across. … Beyond the bend the beam ran on into black." ¶159: "**I sank onto my knees and** went in sideways with my left shoulder first…" / "and I **knelt** in the nothing". See *Slot mechanics* below. |
| B2 | W-04: microcassette unlocated | continuity | (absent) | ¶139: "I groped in the bag under me for another granola bar, past the sock with the tape in it, which had been down among my clothes since I laced the boots on at home. I ate the bar in the dark and the oats went down my front…". See *Microcassette* below. |
| C | W-01: "October" not earned | connective | ¶177 ended its plateau sentence on "…a paper-bag brown that I put down to the light. The air coming in…" | Two signs she can read herself are inserted after "put down to the light": "Beyond it the high summits stood lit to their tops, and there was gray rock all the way up the gullies where the snow had lain that morning. On the slope below me the thyme was over, every flower head dried to a brown husk on its stalk." See *Autumn evidence* below. |
| D1 | W-06: parked-car comparison echoes Ch.2 (¶115), plus ¶107 | prose | "a great slumped mass that would have filled a parking space, with a dull shine… laid on it, over and over, for a span of years"; ¶107 "a gray block as broad as a car's hood" | "a great slumped mass with a dull shine… laid on it for a span of years" (comparison cut, which also clears evaluator #9's "over and over" echo); ¶107 "a gray block as broad as a kitchen table". |
| D2 | W-07: two one-line "Then…" pivots | connective | ¶111 ended, then a one-line ¶113: "Then I went in." | Folded into ¶111: "…beaded red along its length. I capped the water and went in." (The paragraph opens "I drank some water standing on the lip.") **"Then my face went hot." is the only "Then…" one-liner left.** |
| D3 | W-09: paragraphs closing on a negation | prose | ¶11 "…carrying its noise somewhere I could not hear."; ¶29 "…in a way I could not have explained to the taxi driver."; ¶135 "…the beam had nothing to land on."; ¶155 "…lay on the rock and did not shake." | ¶11 "…and whatever noise it made went off down the valley on the wind."; ¶29 "…and I was more pleased with that one than with anything I had taken in Delphi."; ¶135 "…the beam ran on into black."; ¶155 "**The beam of the flashlight shook on the rock.**" The last also fixes evaluator #7: the control flex becomes a leak at the threshold, as the bible requires, with no feeling named. Protected negation closers were left alone (¶51, ¶77, ¶133, and ¶179's missing blaze). |
| D4 | W-10: household-object colors | prose | ¶17 "dishwater gray"; ¶101 "old snow gone a dull sink-white" | ¶17 "pale gray"; ¶101 "streaked with old snow," with the color clause cut. **"tea-brown" and "paper-bag brown" remain (2)**, as the audit advised. |
| D5 | W-11: Ch.2 packed-bag echo (¶5) | prose | "I had kept that canvas bag half packed in the hall closet of every apartment I had lived in since college, and in all those years I had asked nothing steeper of it than the subway stairs at City Hall." | "In all its years with me I had asked nothing steeper of that canvas bag than the subway stairs at City Hall." This drops "half packed / hall closet / every apartment / since college". |
| D6 | W-12b: taxi driver triad (¶7) | prose | "with his whole arm, and then at the bag, and then at me, and laughed" | "with his whole arm, and then at the bag, and last of all at me, and laughed". The third member's syntax is broken so the clause no longer chimes as "and then… and then…". The gesture order and the joke (strength #3) are kept. |
| — | Evaluator #8: "since I was a girl" vs 1989 at age 24 (¶161) | factual | "a scalding blush I had not had since I was a girl." | "a scalding blush of a kind I had thought I was too old for." |
| — | Evaluator #9 / N-19: breath echo (¶151 vs ¶159) | prose | "My breath showed in the beam. It went out of me white and hung there in the light and drifted toward the crack, and I got up…" | "My breath showed in the beam and drifted toward the crack, and I got up…". The held sentence keeps "my breath going out white into its beam". |

*(Paragraph numbers are post-revision lines. Folding ¶113 shifted everything after ¶111 up by two lines relative to the eval and audit citations.)*

---

## Autumn evidence added (W-01)
"October" must be Mara's inference from what she can see, and the page now gives her four cues. The **two new** ones:
1. **The summits have lost their snow.** That morning (¶101) she saw every gully "streaked with old snow". Now "there was gray rock all the way up the gullies where the snow had lain that morning." This is the strongest seasonal cue she has, and the audit had noted it went unchecked.
2. **The thyme is over:** "every flower head dried to a brown husk on its stalk". It mirrors the opening's thyme, whose smell the wind was pressing out, without echoing a phrase.

The **existing** cues stand next to them: the low, early, orange light (¶173), the chill "that had not been there at noon", the woodsmoke, and the browned plateau. The brown is still something "that I put down to the light" (protected). The new sentences come straight after that clause, so the next thing she sees contradicts her own explanation, and the reader watches her inference build. The narrator states no year and no fact. All the cues are period-neutral.

## Microcassette clause (W-04)
"I groped in the bag under me for another granola bar, past the sock with the tape in it, which had been down among my clothes since I laced the boots on at home."
- **Where:** in the duffel, among her clothes. It moved out of the boot when she put the boots on to fly. It crosses with her in the duffel.
- **When:** during the wait in the dark, as she reaches for the bar the chapter already had her eat (the granola count is unchanged).
- **How:** she touches it in the dark and says nothing about it (§4f: "touched without comment"). It is not named "the microcassette". "Rolled tight" (Ch.2) was avoided because it would have made a cross-chapter 4-gram.
- **Tracker:** objects.microcassette → "in its sock in the duffel, among her clothes (moved from the boot when she put the boots on at home); crosses with her". This resolves ENTITY_STATE CH3-6 and the audit's UNRESOLVED flag, and it matches Ch.5's planned "touched in its sock".

## Slot mechanics (W-03)
- **Geometry (¶135):** the crack is vertical, between a leaning split slab and the wall under a low roof. At standing shoulder height it takes only a forearm, and above that it pinches shut. It widens downward until at the floor it is "a good foot and a half across", roughly a tent shape.
- **The hand tests still work:** ¶137 and ¶151–155 have her standing, palm in at forearm height.
- **The entry (¶157, byte-identical):** she puts her left foot in at the wide bottom.
- **The held sentence (¶159):** she now "sank onto my knees and went in sideways with my left shoulder first and my back flat to the slab" (the leaning slab is behind and over her), with the bag pushed down in front of her, her head and shoulder blades against rock, and stone "a foot from my eyes". At the end she "knelt in the nothing".
- **¶167's "Then I was in the hall again, upright"** now means something: she backs out on her knees and stands.
- **The door simile is gone**, so there is no figurative "door" at the threshold (audit's wink note).
- **Ch.6 cascade:** it opens "on her knees in the back recess", which fits this geometry.
- **What changed in the held sentence:** only two lexical edits ("I sank onto my knees and"; "stood" → "knelt"). It is still one simile-free, aside-free sentence of about 150 words.

---

## Strengths verification
- 79-word opener; ugly shoulder sentence; establishing shot; aglet; nanny; herringbone/bedspring; the German entire (no dialogue touched); the sherds paragraph; the wrapper and the sleeve; Fenn's lentil drawing; Hanson; the lens cap: **preserved**.
- Taxi driver (#3): **preserved in substance.** Only the third member's syntax changed, per W-12.
- Anchor run ¶129–¶133: **preserved.** The procedure paragraph and "I pocketed it." are untouched. ¶133 lost only the flush and the hip, as the evaluator directed. "It was cold from the dirt and then it was not." is kept.
- Luminous dots / "still only rock"; the cellar and the Krimpet (month fixed); the pee and the optative; the unwritten postcard; the bells "because they were going"; the ear pressure: **preserved.**
- ¶155's last sentence and ¶157: **byte-identical.**
- Held sentence ¶159: **minimally altered for W-03**, which the brief requires in both places. The shape, rhythm, senses narrowing to sound, and absence of simile or aside are intact.
- 1989 bedroom and "sorry": **preserved.** Only the "girl" clause changed.
- "I backed out." / "The walls went by unread.": **preserved.**
- Outside run: **preserved and enhanced.** Every protected sentence is intact, with two evidence sentences inserted.
- Last line: **byte-identical.**
- **Disruptor's work:** the goatherd's nanny, the Hanson lapse, and the cut "Then I went on into the dark." all stand.

## Checks on the new text
- None of the following appear in new text: "you could have", "against my", "went hot" (beyond the one designed blush), "as if/as though", "wrist" in the watch beat, "cave cold" beyond 2.
- No new comparison is reused from another chapter.
- No new anaphora, define-by-negation, aphorism, emotional-temperature report, or analytical simile.
- No forward gesture or portent before the cave.
- No gesture class is added. "Groped in the bag" is a reach, not set-down/pick-up; the hand-on-bone touches stay at 2.
- Spelling is US throughout.
- Three wordings tripped the gates during the pass and were rephrased: "no bigger than a" (tic 3×), "went in under the arch" (tic 3× "under the arch"), and "into the end of the bag" / "into the duffel" (self-repeat and tic).

## Gate result: `bash tools/check_chapter.sh 3` (final)
| Gate | Result |
|---|---|
| Style | clean: simile 1.6/1k, adverb 3.9/1k, em-dash 1, foreshadow 0 |
| Grammar | clean: 0 errors (2 long-sentence reports, informational) |
| Rhythm | 0 flagged |
| Show/tell | no flags; dialogue 5.8% |
| Voice-wear (strict) | clean |
| Tic gate | clean, including gestures (object handling 5 book-wide, 0.29/1k; Ch.3 contributes 0) |
| Metaphor | fig 2.8/1k, median 18, 12.5% >40w, no flags |
| Word count | 6,834 |
| Shape | clean (needs 4 chapters) |

## Changes not made (and why)
- **Evaluator #10 (optional plateau trim):** not in this brief, and the length is already in band.
- **#11 "autumn" for the last line:** the line is locked; W-01 is solved by earning the month instead.
- **#12 "Ach so":** not in the brief; this pass touched no dialogue.
- **N-06 (Fenn misreadings), N-13 ("would have" cluster), N-14 ("Fenn had" openers):** NOTES, out of scope.
- **Bible goatherd-phone card and ENTITY_STATE patches:** outside the files this pass may touch. Flagged for the orchestrator and the entity tracker; the microcassette location is given above.

## Concerns for re-evaluation
1. Does the kneeling entry still read as the same held breath?
2. Does "The beam of the flashlight shook on the rock." land as a leak rather than a report?
3. Is "October" now felt as her inference: summits bare, thyme over, brown she had excused, chill, smoke?
4. With ¶113 folded into ¶111, does the cave entrance still register as a step over a line? (The light "came with me a little way… and stopped" still marks it.)
