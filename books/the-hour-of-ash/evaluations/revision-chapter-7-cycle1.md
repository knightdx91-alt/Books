# Revision Report: Chapter 7, Polish Cycle 1

**Editor:** book-editor | **Date:** 2026-10-19 | **Input:** `evaluations/chapter-7-eval.md` (POLISH: Floor 8.0, Prose & Voice; Casual 8.5)
**Scope:** evaluator fixes 1-10 (PATH items 1-10) plus the recommended section-4 scene (Revision #11 / PATH 11). Nothing else touched.

**Result:** 6,041 -> **6,128** prose words (shape_check; style_check 6,145; `wc -w` 6,308) | dialogue **22%** (shape) / 21.0% (show_tell) | 3 breaks | median **17** | first sentence byte-identical (`narrative`, 27 words) | final question byte-identical | `check_chapter.sh 7` **all clean** | `tic_report.py --echoes 7` **0 echoes**.

---

## Issues Addressed (before -> after)

| # | Eval item | Location | Before | After | Type |
|---|---|---|---|---|---|
| 1 | P10 oak callback (Ch.6: Kallia smelled the split; she never looked it over) | ¶82 | "They looked the way Kallia had looked at the oak, for weight and for flaws, and they made no secret of it." | "They looked me over for weight and for flaws, and they made no secret of it." | logic |
| 2a | P1 echo-compliance | ¶38 | "I took shorter steps. The toes of the boots showed at every one, two scuffed brown noses…" | "The toes of the boots still showed at each step, two scuffed brown noses…" ("each", not the eval's "every": "at every step" is a Ch.5 3-gram) | prose |
| 2b | P1 echo-compliance | ¶158 | "I made it tighter. The lodgers had gone up, …" | "The lodgers had gone up, …" | prose |
| 2c | P1 (kept) | ¶138 | "Say it again." / "I said it again." | unchanged: the salt joke needs it. Echo-compliance now 1 in Ch.7 | — |
| 3a | P2 "So" opener | ¶34 | "So she taught me to walk. She did it in the court between the hearth and the gate, …" | "She gave her lessons in the court between the hearth and the gate, …" (the eval's "She taught me in the court" tripped voice-wear: "me in the court" is Ch.6 ¶82) | prose |
| 3b | P2 "So" opener | ¶132 | "So I went to the market with an obol in my fist, …" | "I went to the market with an obol in my fist, …" | prose |
| 4a | P3 act-before-will | ¶76 | "I was back in Kallia's lane before I had decided where I was going, with my whole face burning, …" | "I was back in Kallia's lane with my whole face burning, …" | prose |
| 4b | P3 act-before-will | ¶376 | "I turned my head for Mera at the water before I had thought about it." | "I turned my head for Mera at the water." | prose |
| 4c | P3 related | ¶376 | "My eyes went to the ground of their own accord in the lane and kept there" | "My eyes went to the ground in the lane and kept there" | prose |
| 4d | P3 (kept) | ¶334 | "The Greek of it was out before I had decided anything about it." | unchanged (her father's name). Gate: 'before I decided' 3 -> 1 | — |
| 5 | P4 memory kicker | ¶288 | "…tasted of nothing but cold. It did not seem the right moment to bring that up." | "…tasted of nothing but cold." | prose |
| 6a | P5 queue laugh (first) | ¶348 | "…he was writing, the men in the line behind us were laughing at something Kallia had said, and she was undoing her kerchief knot for the fee." | "…he was writing, the father behind us was back on his wall, and she was undoing her kerchief knot for the fee." | prose / emotion |
| 6b | P5 bath laugh | ¶112 | "The woman with the lamp laughed and gave me my arm back." | "The woman with the lamp gave me my arm back." | prose |
| 7a | P6 second use (Ch.5 ¶265) | ¶64 | "Kallia came and planted herself before me with a pot in her hands." | "Kallia came and stood square before me with a pot in her hands." (not the eval's "in front of me with": that 4-gram is the Ch.5 source line itself) | prose |
| 7b | P6 second use (Ch.1 ¶19) | ¶32 | "\"Not to carry water in.\" She was already going. \"The hem hides the boots…\"" | "\"Not to carry water in. The hem hides the boots if you walk right. You don't walk right.\"" (also one walk-off fewer: 3 -> 2) | prose |
| 7c | P6 second use (Ch.6 ¶32) | ¶348 | "It was nothing. It was the size of nothing, and it took up my entire mouth." | "It was the size of nothing, and it took up my entire mouth." | prose |
| 8a | P7 exclusivity | ¶92 | "said Kallia, who was washing standing up, the only woman in the room on her feet." | "said Kallia, who was washing standing up." | prose |
| 8b | P7 exclusivity (thinned to the eval's proposed cap of 3) | ¶146 | "aimed with real skill at the one tragedy I had read through twice" | "aimed with real skill at a tragedy I had read through twice" | prose |
| 8c | P7 exclusivity (thinned) | ¶190 | "Hers was the one question I could not answer by doing something." | "Hers was a question I could not answer by doing something." | prose |
| 8d | P7 rarity gloss | ¶366 | "She listened to it with her hands still, which was rare." | "She listened to it with her hands still." | prose |
| 8e | P8 second "that was all" | ¶196 | "…and then, \"Tighter, I said,\" and that was all I got out of her about it." | "…and then, \"Tighter, I said.\"" | prose |
| 8f | P9 it/it/it triad | ¶26 | "It was heavy, and it was not new, and it smelled of somebody." | "It was heavy and not new, and it smelled of somebody." | prose |
| 8g | Syracuse memory joke tail (written by the continuity repair) | ¶288 | the kicker sentence | Removed in #5. I re-read the remaining memory: it ends on the father's voice and "tasted of nothing but cold", an image with no button. "as it happened" in the first clause is a mild aside, left alone. No further change | check |
| 9 | Revision #11: the cost in scene (section 4) | ¶376 -> ¶376 + new ¶378 | The 200-word summary, with the address in one clause: "I gave up English even with myself in the storeroom at night, because nobody in there understood it, and when I tried one evening to say my whole address aloud in the dark, street and apartment number, I had to go back for the zip code." | ¶376 keeps the claim, Mera, the eyes, the hedge joke and the ugly sentence. New ¶378 is a **222-word** storeroom scene: lamp out, a Theban snoring on the gallery, the address said "in one breath… Philadelphia, P-A"; after the two letters, nothing; "A one came, and then a nine, and after the nine only guesses"; "I had to go back for the zip code, the long way" (the underline kept in the eval's own words); she walks the address back in her head through the vestibule, past her mailbox ("my name inked on a bit of tape"), up the stairs, until "on the second landing the figures turned up again in their right order"; "from the next night I kept even my own company in Greek." The preserved stopping sentence (the himation's smell) closes the paragraph. | structural (thin spot) / emotion |

### Scene constraints (item 9), checked
- **Present scene, no foreshadowing:** the scene stays in one night near the month's end. "From the next night" covers the days already in the section, so it never reaches beyond the narrated month. style_check foreshadow 0.
- **No listener:** she is alone, and the Thebans are asleep. No "said to the [non-listener]" and no English confession to anyone.
- **No fourth emotional break, no voice failure** (retired for Ch.7-9): she says it plainly and lowers her voice by choice ("for the Thebans' sake"). Nothing in her body rebels. No laugh and no mockery.
- **Shows the cost of passing:** the address does not break off at a dramatic point. It breaks off at the part the form always wanted (¶6's clerk), and only a mental walk back through her own building recovers it. Her name on the mailbox tape is set against the MAIRA in wax, and the text never says so.
- **The Hostile's sentence-order point** (English given up and tried in the same sentence) is fixed. She tries it first and gives it up after.
- **"zip code" stays at 2**, the designed pair (¶6, and the scene). "in the dark" is avoided.

### Freshness (every new or replacement phrase grepped against Ch.1-6 and voice-bank/samples)
At 0 prior uses: "looked me over", "stood square before", "back on his wall", "heavy and not new", "still showed at each", "gave her lessons", "washing standing up", "Hers was a question", "went with the rest", "how much of it had gone", "near the end of the month", "along the gallery", "a hundred counters", "dry cleaner", "circulation desk", "in one breath", "two letters", "came nothing", "five figures", "listened for them", "hanging oregano", "only guesses", "the long way", "street door", "under my breath", "the Thebans' sake", "vestibule", "mailboxes", "my name inked", "bit of tape", "the whole of it over", "from the house number", "second landing", "turned up again", "in their right order", "my own company".

Caught and replaced before the gates ran: "a strip of masking tape" (Ch.1 ¶337), "in front of me with" (Ch.5 ¶265), "and waited for them" (Ch.1 ¶259), "came back in" (sample-12), "there was nothing" (Ch.3 ×2), "among the jars" (Ch.5 ¶429). Caught by the gates and replaced: "lay on my back" (Ch.5, echo + voice-wear), "me in the court" (Ch.6, voice-wear), "from the top" and "I went back" (tic gate, 3 book-wide). One rhythm anaphora (four "I…" sentence openers in a row in the new scene) was broken up.

## Strengths Verification
- First sentence and paragraph (#1): byte-identical.
- The himation paragraph ¶26 (#3): only the prescribed P9 recast.
- Lessons, latrine, bath, salt market, carding, Valens, spring, council, step, close (#4-#14, #16): untouched apart from the prescribed edits. ¶146's "the laugh went back where it came from" and ¶190's exchange are intact.
- ¶376's stopping sentence and ugly sentence (#15): both kept verbatim. The stopping sentence now closes the storeroom scene, where it also echoes the address she "had to think about".
- Dunphy ¶380 and the closing ¶382-¶400: byte-identical, including the final question.

## Rules check
- Dialogue 22% (band 20-30). The edits are all narration, apart from merging Kallia's ¶32 line into one quote.
- Breaks: 3. Gear: median 17 (shape_check and metaphor_check), mean 22.3.
- No "did not X; she Y" pivot (negation pivots 0). No "He meant". No "So I…" opener ('So' openers 0).
- Laughs: the row (¶146, load-bearing), the man at the fountain (¶146) and the step (¶356). The step laugh is the only one Mara completes.
- Exclusivity claims: 3 (¶56, ¶78, ¶356). Kallia rarity glosses: 2 (¶12, ¶56). "that was all": 1 (¶20). Act-before-will: 1 (¶334). Echo-compliance: 1 (¶138).

## Gates (run from /home/user/Books)
- `bash books/the-hour-of-ash/tools/check_chapter.sh 7`: style clean (simile 2.3/1k, adverb 2.9/1k, em-dash 2), grammar 0 errors, rhythm 0 flagged, show/tell no flags, voice-wear strict clean, tic gate clean, echo scan 0, metaphor no flags, shape CLEAN.
- `python3 books/the-hour-of-ash/tools/tic_report.py --echoes 7`: 0 echoes.

## Changes Not Made (and Why)
- Eval #12 (¶330, the dog Maira) and #13 (sun over the cliffs, first-week comprehension, Syrakousai): optional and outside the brief.
- Eval #14 (character-bible sync) and #15 (pipeline gate additions): bookkeeping and pipeline work, not chapter edits. The tic gate already counts 'So' openers and 'before I decided'.
- ¶12 "which she did not often trouble to do": left in place. The eval prescribed only the ¶366 gloss, and ¶12 is inside preserved strength #2's span.

## Concerns for Re-evaluation
- Check that the new ¶378 reads as scene rather than summary, and as the cost rather than a fourth break.
- Check "Hers was a question" (¶190), which drops the eval's "keep" on that line to meet its own proposed cap of 3 exclusivity claims.
- Check "She gave her lessons" (¶34): the walking is now carried by the line before it ("You don't walk right.") and the "Shorter." that follows.
