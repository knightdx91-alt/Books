# Disruption Report: Chapter 6 (run 2)

**Verdict on intake:** competent and mostly alive, with a predictable tail. The wall, the laugh and the bread scene work, and so does the backward winding. The weak points were three. Valens's prediction formed a refrain inside the chapter ("if they asked me" / "pay men to ask" / "when they come up this road, they'll ask" / "when they come" / "Men will come asking"). There was a layer of repeated pause beats and looking beats. And several paragraphs explained what the reader already had. Six operations plus the gesture pass, almost all of them cuts.

- **Backup:** `manuscript/reports/chapter-6-pre-disruption.md`. It goes in `reports/`, not `chapters/`, because the gates glob `chapter-*.md` (Ch.3 and Ch.5 precedent).
- **Words (shape_check prose):** 6,767 → **6,634**, inside the 6,500–7,600 range. `wc -w`: 6,876 → 6,743.
- **Dialogue (shape_check, the ledger metric):** 36.9% → **38%**, band 35–45. The show/tell meter, which counts the title and comments, reads 33.1%.
- **Breaks:** exactly 2. **Em-dashes:** 2 → 3. The new one is an interrupted line ("Mules do not know any—"), which keeps the chapter under the cap of 4.
- **Opening:** the I-statement first sentence is byte-identical. **Closing:** the last paragraph is byte-identical: "Men will come asking," he said. "You went up by yourself. You never had a watch."
- **Gates:** `check_chapter.sh 6` all clean (style, grammar, rhythm, show/tell, voice-wear strict, tic gate + gesture layer, shape). `tic_report.py --echoes 6`: **0 echoes**. Simile density went 1.2 → 0.9/1k. And-chains: 5 (cap 9).

## The refrain (the specific item)

Before this pass, the idea "men will come and ask" was spoken five times in the last 40 lines, three of them with the same come/ask wording. It is now **stated once, in the final line**, and carried differently everywhere else:

| Where | Before | After |
|---|---|---|
| Speech opener | "So I'll tell you what I'd tell them, if they asked me." | "So here's what I make of you." The speech is now his own reading of her, not rehearsed testimony. |
| Speech close | "…he can pay men to ask. When they come up this road, they'll ask who took you up there." | "…he's got the money to look. And there's one man in Delphi who'd take a mule up Parnassus in the snow." This is a different move: **self-exposure**, not prediction. He names himself as the thread anyone could pull, and he says nothing about anyone coming. |
| After "You would think me mad." | "Don't tell me where. I don't want it in my head when they come." | "Keep to the wall," he said. "The edge has gone along this bit." This is **evasion through footing** (his attention axis). He refuses her story by changing the subject to the path, and the refusal goes unspoken. "You have not asked my name either" still lands, now against the "Don't." |
| The descent | "if you thought somebody was coming after me?" | "if you believed I was followed?" Three uses of "coming after" (L236, L238, here) are now two, and those two are question and answer. |
| The recess | "I will come after you." | "I will find my own way." This was a fourth "come after". |

The final line is now the first time the threat is said aloud as a forecast, so "Men will come asking" arrives fresh instead of as a third statement. The hook report scored Unpredictability 1/2 on exactly this point.

## Operations Applied

| # | Operation | Location | Before → After (brief) |
|---|-----------|----------|----------------------|
| 1 | **Simile Surgery** | the watch on the lane | "the way he had looked over the lane, all of it, the back first: the steel case and its scratches, the little crown…" was a self-referential simile plus the CLOSED item-by-item look. Now: "He was a long while over the back of it, and over the band where the three links had come out." That is a duration plus one detail. The Ch.2 three-links callback is kept as a re-read reward. |
| 1 | Simile Surgery | the plain at dusk | "like milk being poured off cream" was an inexact image (cream comes off milk, not the reverse), and Mara, who sees how things are made, would not get it backwards. Now: "so slowly that I could not have said when it was gone." |
| 1 | Simile Surgery | after the evidence speech | Cut "like a man giving evidence" and the and-chain around it. Now: "It was the most he had said all day. Most of it was true, and the whole of it was wrong." |
| 1 | Simile Surgery / extension | his Greek | "it was the first Greek in Delphi that came to me without my having to reach for it" became "I followed all of it without reaching". Ch.5's disruption had already cut the "first Greek I followed" move from 3 uses to 1, so this was a fourth. |
| 2 | **Emotional control break** | handing over the watch for good (descent) | "Then wind it," I said. "Every morning." was managed and composed. Now: "Then wind it." It was the wrong language. I had to fetch the Greek, and my voice would not stay level for it. "Wind it. When you wake." It is a small leak at the moment she lets her father's watch go, and it is never processed. Valens's "Forward. Till it stops, and not past." answers the Greek and is unchanged. The cave scream is still the chapter's one break; this is a crack, not a second scream. |
| 3 | **Missing Paragraph** | the lane, after "I will not." | Deleted "Across the mule's back I could not tell what he made of that, and I did not explain it; I could not have in any language." It explained the silence. Her "I will not." (she will not be here in spring) now goes straight into "I will go up without you," so she presses on before he can answer. |
| 3 | Missing Paragraph (partial) | "You go up on the mountain" | Cut the two sentences re-explaining the Sacred Way mockery and the vow of silence. The backfill (L84) already says it, and the wall scene uses the Sacred Way again, so it was three references in one chapter. The seminar-voice sentence stays. |
| 4 | **Dialogue Mess** | the plain, mules and Latin | The cleanest ping-pong in the chapter. Mara's "Mules do not know any—" is cut off by "Ditch." The gray hops a buried ditch and lands her on its neck, and he finishes the old point only "when I was back in the saddle." The interruption comes from his attention (ground under snow), not from wit. The transition paragraph after "North." ("We went on a while with nothing but the creak…") is deleted, so his jump to "What's in it that goes?" is now an unannounced change of subject. |
| 5 | **Negation Pattern Break** | the laugh | "It was not a large laugh. Nothing in it was aimed at me." became "…and ran on briefly after, a laugh with nobody at the end of it." The difference from the Sacred Way laugh is still drawn in the next sentence. |
| 6 | **Opening and-chain (judged)** | sentence 3 | "Below it the dirt was black and gritty and packed hard, and cold under my palm" → "Below it the dirt was black grit, packed hard." Mechanically it was not a 4-and chain (it had three), but it was the narrator's default rhythm in the most-read paragraph, and its "cold" pre-empted the next paragraph's "Everything in there was cold." That line now carries the word first. |
| — | **NO TICS: gesture and stage-business pass** | throughout | **Pause/delay beats** (5 → 3): cut "He waited a little for the rest of it. When nothing came…" and the "We went on a while…" paragraph. Kept: the drip in the recess ("He was quiet so long…"), "The gray went a dozen steps before he answered", and "He finished what was in his mouth first", which is specific to the bread. **Valens looking/studying** (≈10 → 7): cut "He looked across her neck at me, then down at the ice", which was also the chapter's one romance-adjacent glance; the line is now just "The gray walked on." Also cut "stood studying the path" (doubled by "watched him through two turns") and "and looked at what was under it" (doubled by the heel-testing and "reading the ground"). **Putting her on the gray and lashing the bag** (2 + 3 → 1 + 2): "He put me on the gray and lashed the bag onto the dun and went at her head" → "The gray took me down into the white with Valens at her head." **"It was not a question."** was cut as a stock beat. |

## Operations NOT Applied (and why)
- **Irrelevant thought injection:** the Writer already placed three (Ray's snow tires, the Larchwood neighbour's cat litter, the percolator). A fourth would make her scattered. Teeth are not scheduled for Ch.6 (first full surfacing is Ch.7).
- **Ugly sentence:** one exists ("My nose ran and I used my sleeve and it ran again."). Protected.
- **Precision deflation:** the numbers serve the story. The clock times (ten past one, twenty to two, five to two) are her magical thinking and the scene's clock. "Five the load / Four", "eight days", "nine days" and "January '94" are character speech or memory. There is no precision flex.
- **Protected impulse content:** Philadelphia placed in Asia, the temple painter ("He's cheap"), the kiln and "She hit Pan", Kallia's "Letters." / "Nobody asked what you carry.", the bread "exactly the temperature of a person", and the backward-winding anchor (byte-identical).

## Strongest Disruption
The refrain rework. The evidence speech now ends on Valens naming himself, "one man in Delphi who'd take a mule up Parnassus in the snow", so the fear underneath his theory is his own exposure and not a vague posse. That makes the last line do new work: the first spoken forecast, then the coached lie, then the watch erased. The footing line in place of "I don't want it in my head when they come" is the same refusal done the way this man does things, by looking at the ground.

## Risk Assessment
- **"Keep to the wall… The edge has gone along this bit."** is a third footing instruction in the chapter, after "Step where she steps" and "Sit back. Hold the saddle". Each is worded differently and does a different job (ice, riding, evasion), but the evaluator should check that "Valens gives footing orders" is not hardening into a device. If it is, the ditch call ("Ditch.") is the one to keep and this line can become a plain silence.
- **The English slip** depends on the reader remembering that "whatever got away from me got away in English" (L84). If the evaluator finds it unclear, the fix is to restore an "I said" tag, not to add any explanation.
- **Word count** fell 133 words, to 6,634. That is still inside the range, though further below the 7,200 target than before. Nothing in the outline is lost.
- **At-risk list for character-bible.md (orchestrator, please add):** the "first Greek I understood" move is now SPENT book-wide. Valens's "self-exposure" line ("one man in Delphi who'd…") should not become his standard way of voicing fear.
