# Disruption Report: Chapter 2 (Fenn's Notebook), run 2

Backup of the pre-disruption text: `manuscript/reports/chapter-2-pre-disruption.md`. It is kept out of `chapters/` because the gates glob `chapter-*.md` there.

**Verdict on the input:** a strong chapter. It already has its chaos (the floss decision, the jeweler break, the lamp redo), an ugly sentence, a messy Halloran call and a simile rate of 2.2/1k. Its one predictable habit was in the collage machinery. Almost every italic block was announced by a narrator lead-in sentence, and the entries shrank in a tidy decrescendo. So the scale was **4 operations**, mostly small, and two of them are subtractions.

## Operations Applied

| # | Operation | Location | Before → After (brief) |
|---|-----------|----------|----------------------|
| 1 | Simile Surgery (#11) | ¶ "I had read a good many scholia" | "as plainly as a street address, degrees and minutes, with nothing hidden in them and nothing to work out" → "as plainly as a street address." The extension restated the simile. The beat subversion ("nothing is cryptic") still lands, because the simile and the "to the minute" check carry it. **Plus one explaining clause cut** in the lamp paragraph: "Nobody came in to see it, which was the idea" → "Nobody came in to see it." This removes the second of two back-to-back "which…" asides, and the bare sentence now carries some loneliness alongside the pride. |
| 2 | Rhythm break between the documents (Missing Paragraph + a merely-true document) | end of §3; §6 | (a) **Deleted the lead-in** "By the end of that week the notebook had reached Greece." The Delphi entry now drops straight in after the jeweler, and "Delphi, at last" announces itself. (b) **Added one unannounced Fenn entry in §6**, between the passport drawer and Gloria's call, with no lead-in and no gloss: *A fellow off the Athens bus left a Herald Tribune on my table, a week old, and I read every word of it, the bridge column too, and I don't play bridge.* It is irrelevant to the quest and true to his attention (he reads systems, even ones he can't use). It interrupts the tidy June decrescendo so the reader can't predict where or how long the next italic block will be. The entry is undated, uses no numbering or listing, and the narration says nothing about it. |
| 3 | Human noise that resonates with nothing (the 30–40% rule) | §2, library stacks | Inserted mid-paragraph: "Two rows over, a boy in a hooded sweatshirt was eating sunflower seeds and spitting the shells into a Wawa cup." No reaction from Mara, and the scene carries on. The only echo is the stacks' no-food rule she is already breaking, and that is a quiet joke rather than a resonance. |
| 4 | Wrong-register beat | §6, after the consulate carbon | Added before "I folded it back…": "Whoever typed it at the consulate had put one n too many in Pennsylvania and x'd it out." Her eye goes to a typo at the gravest moment in the chapter. It is the conservator's attention used as a flinch, and it is not explained. The carbon's italic text is unchanged, and the slip still does not say where the coat was found. |

## Operations NOT Applied (and why)
- **Irrelevant Thought Injection (Mara):** skipped. The Writer already has 3 chaos moments (floss, jeweler, lamp), and the budget is 2–3. Op 3 is texture she observes, not a thought she has.
- **Emotional Control Break:** skipped. The jeweler scene already is one, and the laugh is the chapter's surprise.
- **Precision Deflation:** skipped. The remaining numbers serve the story: the film counter at 1 and the 36 frames are weight carriers, and the Plymouth's $600, the 1838 Leipzig edition and the coordinates are Fenn's or the reader's canon.
- **Ugly Sentence:** skipped. One already exists ("The lab was cold, it was always cold, it was a basement.").
- **Negation Pattern Break:** skipped. There are no define-by-negation openers.
- **Dialogue Mess:** skipped. The Halloran call already interrupts, trails off and has the tenants walk in. Gloria talks past Mara, and the jeweler talks to his telephone.
- **Phillies as the merely-true detail:** deliberately not used. The 1964 Phillies are Fenn's scheduled chaos subject (Ch.25, 26, 29, 35), and a 1968 surfacing would spend it early.

## Constraints verified
- First sentence and last sentence are byte-identical to the backup (diffed).
- Scene breaks: **6**.
- Em-dashes: **2**, unchanged. "as if"/"as though": 0. Metacognition: 0. Emotional-temperature reports: 0.
- No forward-gesture was added, and the July cheer is not glossed. The new Fenn entry sits before the June/July entries with no comment.
- New phrases were checked against Ch.1–2: none repeats. To avoid a sentence-opener pattern, the two drafted "Somebody…" openers were changed to "A fellow…" and "Whoever typed it…", because the chapter already had two "Somebody" sentence starts.
- Dialogue share: 14.4% → **14.2%** (band 10–20%).
- Anchor (handwriting capitals → small script; "the backs were smooth") and surprise (the *firma mancante* laugh) are untouched.
- No ENTITY_STATE contradiction: the slip's provenance, date and addressee are unchanged, and the Herald Tribune entry adds no plot fact.
- Net words: **4,197 → 4,240 (+43)** by `wc -w`, within ±120.
- `bash tools/check_chapter.sh 2`: style clean (simile 2.1/1k), grammar clean, rhythm 0, show/tell no flags, voice-wear strict clean, tic gate clean, metaphor no flags, shape clean.

## Strongest Disruption
Op 2(b), the bridge-column entry. Before it, every Fenn document either carried plot or tracked his decline, so the notebook read as an instrument built for this chapter. One week-old newspaper he couldn't use turns it back into a man's diary. Placed unannounced among Mara's packing, it also makes the July 21 entry feel less engineered when it arrives.

## Risk Assessment
- **The typo beat (Op 4)** is the boldest change. A reader could take it as coldness at the slip. I judge that it reads as deflection, since she folds the slip away in the next sentence, but if the Evaluator finds it undercuts the beat, cut that one sentence. Nothing else depends on it.
- **The §6 Fenn entry** puts an italic block where no reading is shown. The collage logic (a nightly ration) covers it. If the Continuity Guardian wants its reading anchored, the fix is placement only: move it to just before "The June entries were short" in §5, with no lead-in.
