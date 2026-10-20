# Revision Report: Chapter 11, Polish Cycle 1

**Editor:** book-editor | **Date:** 2026-10-20 | **Source:** `evaluations/chapter-11-eval.md` (POLISH; Floor 8.0, held by Prose & Voice), PATH TO 8.5 items 1–9, plus ENTITY_STATE CH11-2 and CH11-5.
**Untouched:** the first sentence (¶6, byte-identical) and the final spoken line (byte-identical), and every Strength to PRESERVE except where the eval's own revision touched it.
**Every new string was pre-grepped** against Ch.1–10 and all 13 voice-bank samples (0 prior uses) and inside Ch.11 (0 other uses).

## Measurements after the pass
| Measure | Before | After |
|---|---|---|
| Words (shape_check / style_check / `wc -w`) | 6,038 / 6,055 / 6,209 | **5,929 / 5,946 / 6,107** (range 5,600–6,800) |
| Dialogue % (show_tell / shape_check) | 36.9 / 37 | **37.7 / 38** (band 35–45) |
| Median sentence (metaphor_check, shape_check) | 14 | **14** (mid gear held; no joins were needed) |
| Breaks | 3 | 3 |
| Em-dashes | 2 | **1** (Felix's cut-off report only) |
| Bare "No." lines | 3 | 3 (Valens 2, Mara 1; none added) |
| Narrated non-answers | 5 | **1** ("He answered neither.") |
| "low" in the chapter | 4 (3 as Valens's voice) | **1** (the protected first sentence) |
| `check_chapter.sh 11` | clean | **clean on every gate** |
| `tic_report.py --echoes 11` | 0 | **0** |
| shape_check | CLEAN | CLEAN (`long-spiral` → `dialogue`) |

## Issues addressed (before → after)

| # | Issue | Type | Before | After |
|---|---|---|---|---|
| 1a | P5 near-kiss: the struck knot gesture (setup) | prose | "Valens had come in with the black's halter, and he stayed, and found a knot in the end of a lead rope to work at." | "Valens had come in with the black's halter, and he stayed, with a foot up on the bench, to put a new lace in his boot." |
| 1b | P5: the knot at the freedom question | prose | "The knot slackened under his thumbs; he was a while silent, and I let the question stand." | "The lace stopped at his ankle; he was a while silent, and I let the question stand." |
| 1c | P5: the knot after "Who took yours?" | prose | "He hung the rope up with the knot still in it." | "He ran the lace on up the shin and tucked the end in." (no "knot" or "tied": the act ends without a knot near his hands. Ch.7's broken lace becomes an unpointed re-read reward.) |
| 1d | P5: the first face ruler (distance measured once) | prose | "…and lifted my head from the knot, and his face was a hand's width from mine." | "…and lifted my head, and his face was there." "Short of it by the width of a finger" is now the only measurement. |
| 1e | P5: sample-10's "Neither of us … and then we both did" + P3's nose | prose | "The nick in his eyebrow showed, and the healed break in his nose. Neither of us moved, and then we both did, his head coming down and my face lifting to meet it." | "The nick in his eyebrow showed. He came nearer, and my face lifted to meet his." (The eval's "His head came down" was tried and rejected: with the protected "…had been held up came down, and I was hungry" it made "came down and" 3× book-wide, failing the tic gate.) |
| 1f | P5: knees, then hunger (Ch.4 / sample-09) | prose | "I sat down. There was the packsaddle on its trestle behind me, and my knees put me onto it, with the cut ends…" | "I sat down. The packsaddle had been on its trestle at my back, and I was on it, with the cut ends…" (the body acts before she knows it, with no knees. "behind me, and I" was tried first and failed voice-wear self-repetition.) |
| 1g | P5: the second "Neither of us" | prose | "…and hung it back up. Neither of us said anything. He was out in the yard next…" | "…and hung it back up. He was out in the yard next…" |
| 2a | P1 Felix's speed beats speech (¶268) | prose | "Felix had it lit and there before the word was well out." | "Felix had it there, lit." |
| 2b | P1 (¶308) | prose | "Felix reached him before Praxias had the last word out." | "Felix left his bucket and went to him." |
| 2c | P1 (¶340) | prose | "Before his name had finished, the boy was through the gate." | "The boy was out of the gate and after him." (The eval's "off up the road after him" made "up the road" 3× book-wide (Ch.5, 7, 11) and failed the tic gate.) ¶6's "before he had finished" is kept as the one use. |
| 3a | P3 Nikaso's nose on Valens (¶98) | prose | "Close to, his nose had once been broken, and had healed a shade crooked, and a white nick ran through one eyebrow, across the grain of the hair." | "Close to, a white nick ran through one eyebrow, across the grain of the hair." |
| 3b | P3 (¶498) | prose | "…and the healed break in his nose." | cut (see 1e) |
| 4 | P4 Felix's intro on the Ch.4 goat-boy frame | prose | "He was a thin one of twelve or so in a tunic made for somebody broader, belted up with a length of rope, and his hair stood up every way at once, with straw in it." | "He was a thin one of twelve or so, with straw in his hair." |
| 5a | P2 narrated non-answer (¶322) | prose | "Valens gave him no answer, and he went off uphill, telling the quail about it." | "He went off uphill, telling the quail about it." |
| 5b | P2 "let it be" (¶388) | prose | "He let it be. At the edge of the town he took the priest's lane…" | "At the edge of the town he took the priest's lane…" |
| 5c | P2 "let it go by" (¶534) | prose | "He let that go by him. I waited for him to tell me why." | "I waited for him to tell me why." |
| 5d | P2 non-answer gloss, sample-10 shape (¶546) | prose | "That got no answer. He had it, and he kept it." | "He had it, and he kept it." |
| 5e | P2: the one kept | — | "He answered neither." | unchanged. No refusal was turned back into a bare "No."; "He kept the stone going." (¶54) is a work beat and stays, per the eval. |
| 6a | P6 "Women?" (Ch.8's one-word line) | prose | "Women?" / "Women too. Children, once they are old enough to be late." | "Children?" / "Once they are old enough to be late." |
| 6b | P6 breaking Ch.7's catechism shape (all questions from the asker) | dialogue | "Not everybody is awake at dawn." / "Who isn't?" / "The rich," I said. … | "Not everybody is awake at dawn." / "I am." / "The rich," I said. … (his question becomes a flat claim about himself, and she answers past it. Also a #17 clean-dialogue offset.) |
| 6c | P6 Mara's origin cut at a dash a third time | prose | "In my country—" I began, and he was on his feet, and the bells were in my lap… | "A lock does. In my country every door has its own." / He was on his feet then, and the bells were in my lap… (no dash, no tag. The tagged version "A lock does," I said. "In my… gave "I said in my" and failed voice-wear self-repetition.) |
| 7a | P7 low Latin to a mule, out of her hearing (¶264) | prose | "…and talked to her. It was Latin, and low, and so little of it reached me that it might have been the same few words over and over." | "…and talked to her. Very little of it reached me, and what did was the same few words over and over." (Felix still supplies the Latin at ¶446.) |
| 7b | P7 "low" as his voice tag (¶512) | prose | '"He's been up since before it was light," he said, very low.' | '"He's been up since before it was light," he said.' |
| 7c | "low" count to ≤1 | prose | "…and the black waited with her foot in it and her head low…" | "…her head down…" ("hanging" was tried and rejected because it repeated "the girths hanging" in the near-kiss). |
| 8 | P8 "with great bitterness" | prose | '"You've never seen anything," Felix said, with great bitterness, and took himself off…' | '"You've never seen anything," Felix said, and took himself off…' (the forked stalls and the dog leaving the yard carry it) |
| 9a | PATH item 9: "a dozen of them" (Ch.9) | factual | "with the mules' bells in his lap, a dozen of them, stuffing…" | "with the mules' bells heaped in his lap, stuffing…" |
| 9b | PATH item 9: "kept his eyes on the" (Ch.7, possessive swap) | factual | "Valens kept his eyes on the hoof, and Felix stopped short." | "Valens was watching the hoof, and Felix stopped short." |
| 9c | PATH item 9: "fist" in adjacent sentences | factual | "eased the sack out of his fist without hurry" | "eased the sack out of his hand without hurry" |
| C1 | ENTITY CH11-2: money container (Ch.9 rag) | factual | "There were three drachmas in a knot at the corner of my himation, all that the priest had paid me…" | "There were three drachmas in the rag at my belt, all that the priest had paid me…" |
| C2 | CH11-2 (follow-through) | factual | "I untied the knot first and held out the obol." | "I untied the rag first and held out the obol." (¶408's "knotted in with the remains of the priest's money" still agrees: it is the rag.) |
| C3 | ENTITY CH11-5: Boeotians on the Kirrha road | factual | "a family from Boeotia with a grandmother in a basket chair…" | "a family of Achaeans with a grandmother in a basket chair…" (Achaeans cross the gulf by boat to Kirrha, which matches the Aigion goat boats at ¶556. Valens's "Boeotians at the back, drunk by noon" is the sanctuary crowd and stays.) |

## Strengths verification
- First sentence (¶6): byte-identical, including "very low" and "before he had finished".
- Final spoken line: byte-identical. `long-spiral` → `dialogue` confirmed by shape_check.
- The awl (¶138), the figs (¶150–¶200), Kallia (¶286–¶296), the sherd reveal lines, "Who took yours?", the anchor (¶508), and "He had it, and he kept it.": untouched.
- The near-kiss keeps every beat in its order: "Hold this end," / "Hard."; the knife on the bench; his face there; the lamp lighting him; the movement toward each other; "Short of it by the width of a finger"; the girths; her seat; the hunger (byte-identical); the wick; the stretch and crack; "I went out after him."
- "Lessons. Work. Each other.", "Late for what?" and "Who keeps the door, while they sleep?" are kept. The bells exchange is two lines shorter in effect, as the eval asked.
- No bends, kneels, crouches or memories were added (gesture classes unchanged; memories 0). "He came nearer" is not a bend or lean.

## Changes not made (and why)
- Optional #11 (", at daybreak") and #12 (the anchor's because-clause): optional in the eval and not in this brief.
- #13 (Valens's walk-offs) and #14 (the whetstone beat): WATCH only, with no Ch.11 change prescribed. Ch.12 limits: ≤3 walk-offs, ≤1 bare "No.", ≤1 bare "Felix.".
- #16 (character-bible sync) and #17 (root pipeline checks): bookkeeping and pipeline work, outside a prose cycle. Left for the orchestrator.

## Concerns for re-evaluation
1. **"Short of it by the width of a finger"** (protected) now follows "my face lifted to meet his." Its "it" means the meeting, not a head. Please check that it reads cleanly.
2. **"I am."** (6b) is the one invented line beyond the eval's prescriptions. It was added to break Ch.7's question-only catechism. Please judge it against Valens's card: a flat fact about himself, no comparison.
3. **"Felix left his bucket and went to him."** is less fast than the line it replaced. That is deliberate: Felix's speed now rests on ¶6, his talk and his actions ("did nothing at a walk").
4. **The lace** is on a new object class for Valens's hands (footwear). It is not a knot, and it is never tied in narration. Please confirm that it does not read as the struck device in new clothes.
