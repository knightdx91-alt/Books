# Disruption Report: Chapter 1 (The Reception), run 2

**Verdict on the incoming draft: strong.** It already has three chaos moments from the Writer: the all-or-nothing choice at the stairs, the hessian thought in the cab, and the check made out with her father's phone number. It also has an ugly sentence (the warm ziti), wrong-register talk from the walk-ons (Sterno, the barber's bet, the lobster in the diving helmet) and plenty of texture that points at nothing. So the target was 2–4 operations, all of them subtraction except one swapped dialogue line. Four operations were applied, touching seven places.

Backup of the pre-disruption text: `manuscript/reports/chapter-1-pre-disruption.md`. It is kept out of `chapters/` because the gates glob `chapter-*.md` there.

## Operations Applied

| # | Operation | Location | Before → After | Why |
|---|-----------|----------|----------------|-----|
| 1a | Simile Surgery (#11) | ¶ "I had spent most of the forty minutes…" (reception) | "…the way I watched a cracked pot that had come up from storage**: looking past the crack to the body around it,** to see where the strain had gone." → "…the way I watched a cracked pot that had come up from storage, to see where the strain had gone." | The middle clause explained the comparison. "Where the strain had gone" is the part the next two sentences pick up ("It had gone into the dean…"), so that part stays. |
| 1b | Simile Surgery (#11) | ¶ Seiko winding (bedroom) | "it was ticking, quick and light **and absolutely indifferent, the way it had ticked on his wrist in Paphos at two in the morning**." → "it was ticking, quick and light." | The extension did two things it shouldn't. "Indifferent" read a feeling into the watch, and the Paphos callback tidily stitched Doug's cut eulogy story to the watch, a graduated payoff. It also cuts "two in the morning" from 3 uses to 2 (tic hygiene). |
| 2 | Anaphora / tidiness break | ¶ "A collector will not. A decorator will…" (haggling) | "I looked at the doorway in blue ballpoint **with its little scribbled dark**, and at the **little** hook of the query after it, and at the coast that had cost a navy**, and I did not know what I was doing**." → "I looked at the doorway in blue ballpoint and the hook of the query after it, and at the coast that had cost a navy." | This broke an "and at… and at… and at" triad. It also cut a repeat of "scribbled dark" from the ink paragraph and a doubled "little". The self-report "I did not know what I was doing" was the third of three "I acted before I knew" notes, with "I had not known I was going to ask it" and "I had said it before I had checked anything", so it was a pattern forming. Now her bid of "Eight" arrives with no narration in front of it. |
| 3 | Dialogue mess (wrong-register non-sequitur) | Doug exchange, by the chafing dishes | "Are you keeping the house?" / **"I haven't decided."** / "The last week…" **Doug touched the peeling skin on his nose and looked at his fingertip.** "Every season…" → "Are you keeping the house?" / **"Your nose is peeling."** / **He touched it and looked at his fingertip.** "The last week… Every season…" | The cleanest Q&A in the chapter now has a swerve. Mara dodges the house question (an evasion in character) with a conservator's surface remark that is slightly rude. It is the irritation surprise again, and it is earned by her watching the lifted flake through the whole eulogy. Doug talks straight past it into his porch story. The gesture is unchanged, but it now reacts to her line instead of decorating his. "I said thank you again" still has its antecedent. |
| 4 | Missing paragraph / graduated-reveal cuts | (a) ¶ after the check; (b) ¶ "I looked at the question mark…"; (c) start of the ink paragraph | (a) Deleted the one-line paragraph "She never glanced at the number." (b) Cut "It was the only mark on the sheet that didn't." after "It did not look sure." (c) "**Then there was the ink.** Across the mountains above Castri…" → "Across the mountains above Castri…" | (a) told us what the next paragraph already shows, since Szabo checks the signature and the license and pockets the check. (b) explained the observation and clicked Szabo's "He is just very sure" shut like a small button. (c) was a drumroll for step three of the map → watermark → ink sequence, and cutting it lets the ink arrive without an announcement. |

**Net words:** 7,171 → 7,103 by `wc -w` (−68).

## Operations NOT Applied (and why)
- **Irrelevant thought injection:** skipped. The Writer's hessian/burlap thought is already there and there are three chaos moments in total, so the limit is reached. A fourth would make her seem scattered.
- **Emotional control break:** skipped. The check-and-heater beat already is one ("It's this heater," I said, to nobody), and it is protected as impulse content.
- **Ugly sentence:** skipped. One exists (the warm ziti put in "anyway").
- **Precision deflation:** skipped. The numbers serve the story or the Devoted Reader: the 1966 Seiko, December 1991, the haggle from 1,400 to 1,150, the verdigris in six/seven places, the 38° 31′ N / 22° 32′ E coordinates, and the eleven rosebushes (a walk-on's own texture).
- **Negation break:** nothing to break. No sentence-initial define-by-negation in narration. "Not to nothing" and "not everything, not this" are in-character speech and are not openers.
- **Texture with no resonance:** nothing added. The chapter already has enough of it (the Christmas-party fire bill, the barber's nephew, the lobster in the helmet, Gloria's earrings, the Hogarth restrike, the coffee ring on Southwark), and the brief prefers subtraction.
- **Untouched on purpose:** the first and last sentences, the anchor sequence at the machine (all three plays, "Mara? Which one stops it?", the tape weighing "less than the cake had"), the cake-eating payoff ("annoyed about that too"), the hessian thought, and Gloria's look.

## Verification (after the edits)
- `bash tools/check_chapter.sh 1`: style clean (simile 2.1/1k, em-dash 2), grammar clean, rhythm 0 flagged, show/tell dialogue 32.0%, voice-wear strict clean, tic gate clean, metaphor fig 2.4/1k, shape clean (open `I-statement`, end `quiet`).
- Em-dashes: 2, both in dialogue interruptions as before. None added.
- "as if"/"as though": 1, unchanged. No forward-gestures added. No new phrase introduced (every edit removes words or reuses words already in the sentence).
- Scene breaks: 3, unchanged. The first sentence is byte-identical. The last sentence ("Every second or so the red light came on and went off, and each time it lit the lid of the cigar box.") is intact.
- Continuity: no ENTITY_STATE fact is touched. Removing "I haven't decided" leaves the house question open rather than contradicting anything.

## Strongest Disruption
**#3, "Your nose is peeling."** It is the only place where the irritation surprise gets out of the narration and into her mouth in front of someone. She cannot answer a kind question about her father's house, so she reports on a man's skin, and he is too busy grieving at her to notice. The remark is rude, funny, true to the conservator and evasive all at once, and it costs about two words.

## Risk Assessment
- **#3** could read as cold if an evaluator misses that Mara watched the flake through the whole eulogy. The setup is about 40 lines earlier and is explicit, so I judge the risk low.
- **#1b** removes the only physical link between the watch and Doug's Paphos story. That link was a tidy echo, not plot, and the watch's history still lives in "four decades of trench walls."
