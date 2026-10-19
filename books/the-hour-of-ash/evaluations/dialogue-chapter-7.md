# Dialogue Polish Report — Chapter 7 (run 2)

Scope: dialogue only, plus the tags and beats attached to it. Narrative prose is untouched. The opening claim sentence (`narrative`), the closing question paragraph (`question`), the 3 `* * *` breaks, the anchor (the himation on the council-hall step) and the Dunphy memory are byte-identical. The only non-dialogue edits are four beats sitting next to a line of speech (listed under Tag/Beat). The header comment's word counts were updated to match the page.

## Audit Summary
- **Dialogue ratio (shape_check, the ledger metric):** 20.70% before (1,327 / 6,410), **20.74% after (1,320 / 6,366)**. The band is 20–30%. The show/tell gate's measure, which counts the title and comments, holds at 20.2%. I cut dialogue only where a line was spent or off-card, and cut beats only where they were stalls or repeats, so the share rose slightly with no padding.
- **Word count:** 6,410 → 6,366 (shape_check). `wc -w` 6,536 → 6,530.
- **Em-dashes:** 2 → 2. Both are true interruptions (the latrine and "A woman can't answer for—"). None added.
- **Conversations analyzed:** 13. The shovel; the clothes; the walking/sitting/eyes lessons; the bath; the lentils; the salt market; the carding evening; Valens at the gate; the drover at the spring; the broken jar; the Syracuse plan; the council table; "Maira. The water."; midwinter. The latrine and the Thebans count as fragments.
- **Lines flagged INDISTINCT:** 1, resolved 1.
- **Lines flagged WEAK:** 8, resolved 8.
- **FLAT_DIALOGUE:** 1 (Kallia's eye lesson stated as a maxim), resolved 1.
- **Exposition dumps:** 0. Kallia's Syracuse briefing is four sentences, but it is a coached lie with a motive, not information for the reader. Kept.
- **Tag overuse:** none. "said" is the invisible default (about 34). There are no creative tags and no adverbs.
- **Spent constructions in speech:** "Then…" reply openers 5 → 1. Sentence-initial "Nobody…" 2 → 0. "Then you…" 0. "He meant…" 0. The "did not X; she Y" pivot 0.
- **Gestures:** no nods, shrugs, sighs, swallows or "a long moment", before or after. Two duration stalls removed ("stood where they were a while", "carded for a while"). One item-by-item look (a CLOSED device) removed. Kallia handing Mara things as a beat: 3 → 2.

## Voice Distinctiveness Results
| Character | Lines | Distinct | Weak | Indistinct | Post-Polish |
|---|---|---|---|---|---|
| Kallia | ~50 | 45 | 5 | 0 | **PASS.** Imperatives and tasks, with labor as her attention. She answers a question with a job ("I want that basket done before the lamp goes", "Bank the hearth", "Walk quick"). She never speaks of herself; the jar speaks for her. No proverb remains. |
| Mara (Greek) | ~30 | 28 | 2 | 0 | **PASS.** No contractions anywhere in her Greek ("I have turned the edge on it", "Do you not want to know where it is?", "That I am free"). Curious *why*/*how* questions. She minimizes harm to herself ("Only my wrist."). |
| Mara (English) | 0 | – | – | – | No English speech this chapter. The public silence holds; see the notes. |
| Sosandros | 14 | 13 | 1 | 0 | **PASS.** The form's questions in the form's order, clipped. One longer sentence when he is pleased with himself (the Syracusan at the games). |
| Valens | 5 | 4 | 1 | 0 | **PASS.** Plain, contracted, literal. His attention is on the burning, and on her gait and her silence (bodies). "No." is a literal correction, deadpan. No closeness, no order, no comparison, no romance signal. |
| Salt-seller | 6 | 6 | 0 | 0 | **PASS.** Theatrical, loud, generous. Her grievance is the god's basin and the donkeys. |
| Sprat-seller | 1 | 1 | 0 | 0 | **PASS.** Dry, eyes on her fish. |
| Drover | 5 | 5 | 0 | 0 | **PASS.** Probes whether she belongs to anyone ("She's nothing to anybody. Ask round this spring."). Western, wine. |
| Baker's wife | 6 | 5 | 0 | 1 | **PASS.** Tells the room about her own household feud; bodies, the lamp. |
| Girl with the mole | 4 | 4 | 0 | 0 | **PASS.** Asks questions: fetter, bought, where they mark. Offers the horn powder. |
| Thebans / latrine men / the father | 4 | 4 | 0 | 0 | **PASS.** |

## Changes Made

### Subtext Additions (surface: etiquette · real: how not to be killed, per outline.md)
- **The eye lesson** (FLAT_DIALOGUE → resolved). "When a woman looks at a man, she's asking him something. … Out there, somebody answers her." This was a general maxim, the proverb register struck from Kallia's card and the closest the chapter came to a character speaking its theme. It is now **"Look at a man out there and you've asked him something." / "And somebody answers."** That is a second-person instruction tied to "out there", so it stays an etiquette rule on the surface, and the threat sits in the unattributed "somebody". The narration's next sentence ("That answer lived past the running track…") still has its referent. Technique: displacement into instruction.
- **The shut room.** "Nobody," became **"It's swept,"** followed by "Tighter, I said." She now answers *who sleeps there* with the labor she does on the room, which is deflection in her own axis. The subtext (she keeps it ready) is readable, and Ch.10's explanation is not pre-empted. It also removes a sentence-initial "Nobody".
- **The broken jar.** The beat "she looked at the pieces…, and then at my wet feet, and then at my wrist" was the CLOSED item-by-item look. It is now **"When I laid the pieces on the hearthstone she looked past them, at my wrist."** She goes straight past the jar to the place a man took hold of, so her first word, "Who?", lands as knowledge rather than inquiry. Mara's reply "On my wrist." → **"Only my wrist."** The minimizing is hers (no request to be looked after), and Kallia's speech about the jar then does the caring by displacement.
- **The council.** "Then who've you got for my house? You've had nobody else on that line for years." → **"Who stands for my house, if I don't? You've had no other name on that line for years. Write me."** Kallia answers the clerk's rule about women with the house (her axis), not with herself, and the spent "Then…" opener and the "nobody" are gone.

### Voice Adjustments
- **Kallia, the "Then…" retort was forming as her reply shape** (2 in Ch.6, 4 in Ch.7). It is now down to 1, the writer's flagged line "Then why aren't you in it?":
  - "Then the god can put an edge back on it." → **"Let the god put an edge back on it."** (her imperative)
  - "Then what do the women do all day?" → **"What do the women do all day?"**
  - "Then who've you got…" → see the council above.
- **Kallia at the bath:** "Leave her," → **"Singe your own,"**. The old line was a generic protective imperative, and the salt-seller's "Leave Antigone alone" shares its shape, so two women had the same rescue line. The new one is her tongue and a counter-task, and it lands on the baker's wife's "I'll singe them for you" / "I jumped."
- **Kallia, small:** "So the whole town heard." → **"So the town says."** ("the whole X" was at 3 in speech, with "whole spring" and "whole city" alongside.) "Every … Every other winter they go" → **"They go every other winter"**, which breaks a two-sentence "Every" run. "She handed me the carders." was cut, so her line now pivots mid-breath from the gossip to the task: **"Let them. Simple girls don't get asked anything. Tighter than that; you're making a bird's nest."** She uses few words and then work, and the third hand-it-to-her beat is gone.
- **Mara's Greek:** "Nobody carries it." → **"No one carries it."** (her Greek register, and no sentence-initial "Nobody"). "Then how am I to see…" → **"How am I to see where I am going?"** "And what do the women do, up there?" → **"And what is it for?"**: her own *why*, instead of echoing Kallia's labor question back, which made two lines land on the same words. Kallia's "Dance. Drink. Freeze." now deflects purpose into activity.
- **Sosandros:** "And what is a girl from Syrakousai doing in Phocis at the year's end?" broke his card ("never asks a person anything about herself that the form does not"). It is now **"Resident since when? On what business?"**, which is the form's next two boxes, clipped. Kallia's over-full answer (people dead, last boat, vintage) now reads as a rehearsed lie volunteering itself to a man who did not ask for a story.
- **Valens:** "She's got you walking." (a modern-leaning idiom) → **"She's taught you to walk."**, plain and literal. He is still reading her gait, on his body axis.
- **Baker's wife** (the INDISTINCT line): "Where's that, then?" could have been any woman in the room and shared the ", then?" tag with the mole girl's "What's this white, then?". It is now **"And where's that, where they've no lamps?"**, which is her lamp and her body-talk.
- **Salt-seller, "Antigone" in her mouth 4 → 2** (the shout and "Leave Antigone alone"), so the nickname cannot become her refrain. "Antigone's come down off the stage" → "She's come down off the stage". "ask for pepper, Antigone" → "ask for pepper".
- **Drover, "simple" 4 → 2** in his speech (the at-risk list retires the word after Ch.7, and he was the heaviest user): "Here's the simple one." → **"Here's the one that doesn't talk."** and "Look at me, simple." → **"Look at me."** He keeps "Kallia's simple one. Is she simple all over, or only in the mouth?". Book total for "simple" in speech is now 5 (Kallia 3, drover 2), all in Ch.7.

### Tag/Beat Replacements
- 0 tags replaced. "said" stays invisible.
- **4 beats cut or recast:**
  1. "She kept her hand off the knot in her kerchief." was cut. It was the third "knot" in 15 lines (lace, kerchief, lace), and a withholding gesture where the line already withholds.
  2. "The boots stood where they were a while. Then they turned a little…" → "The boots turned a little…". The stall and a "Then" pivot are both gone.
  3. "She carded for a while." was cut, as a duration stall. Her skipping straight past hot water to "And the wool?" is now the reaction.
  4. "She handed me the carders." was cut (see Kallia above).
- The item-by-item look at the jar was recast (see Subtext).

### Natural Speech Additions
- 0 interruptions added. The 2 existing em-dashes are kept.
- 1 deflection added ("It's swept").
- 1 mid-line pivot from gossip to task added (Kallia, "Let them…").
- Repetition kept where it is natural. Kallia's coached "came on the last boat" is said twice, at night and at the council, because a rehearsed lie is repeated verbatim. The three-line "Kallia's" chain at the spring ("She's Kallia's." / "Kallia's what?" / "Kallia's, and Kallia has a tongue on her…") is kept as the hinge that the register answers.

## Notes on the brief
- **The public silence.** Mara is silent outside the gate from the salt market on. She says nothing to Valens at the gate or to the drover, and the bath and the latrine come before the vow. At the council she speaks twice: "Mara" and, to "Daughter of?", "Aimilios". I read the patronymic as part of giving her name, since a Greek name is the name plus the father, and the narration's "first word … in nineteen days" covers it. If the author wants the break to be strictly one word, Kallia cannot supply the father's name (she has never asked), so the clerk would have to skip the question, and that cuts against his card.
- **Valens.** He has five lines: no hands, no face, no order answering closeness, no comparison, no romance signal. "No." is a literal correction from the one man who has heard her talk.
- **Sosandros and his card.** The card says "one dry put-down per encounter", and the page has two: the wall ("…It will stay up for one widow.") and the fee ("don't tell me the god pays for wax"). I left both. The wax line is his attention ("who pays for the wax"), and cutting it would only remove words from a scene that is already at the band floor. Flagged for the Writer to settle either the card or the page.

## Remaining Concerns
1. **Bible quotes my changes invalidate** (`character-bible.md` was not edited):
   - **Kallia Ch.7 block:** "Then the god can put an edge back on it." → "Let the god put an edge back on it." · "When a woman looks at a man, she's asking him something … Out there, somebody answers her." → "Look at a man out there and you've asked him something." / "And somebody answers." · "Then what do the women do all day?" → "What do the women do all day?" · "Nobody." / "Tighter, I said." → "It's swept." / "Tighter, I said." · "Then who've you got for my house? You've had nobody else on that line for years. Write me." → "Who stands for my house, if I don't? You've had no other name on that line for years. Write me." · "Every other winter they go, and this is the winter." → "They go every other winter, and this is the winter."
   - **At-risk after Ch.7:** "Kallia answering a question about the shut room ("Nobody." / "Tighter, I said.")" → ("It's swept." / "Tighter, I said."). "simple: the drover says it three times in one speech" → twice.
   - **Valens Ch.7 block:** "She's got you walking." → "She's taught you to walk."
   - **Sosandros Ch.7 block:** "And what is a girl from Syrakousai doing in Phocis at the year's end?" → "Resident since when? On what business?"
   - **Ch.7 walk-ons:** the salt-seller's "Antigone's come down off the stage" → "She's come down off the stage"; "Come again tomorrow and ask for pepper, Antigone." → "…ask for pepper."; the "Antigone" count is 3 → 2 (the CAP REACHED ruling still stands). The drover's "Here's the simple one." → "Here's the one that doesn't talk."; "Look at me, simple." → "Look at me."
   - **New page text the bible does not yet hold:** Kallia's "Singe your own," at the bath; the baker's wife's "And where's that, where they've no lamps?"; Mara's "Only my wrist." and "And what is it for?".
2. **Suggested at-risk entry:** Kallia's **"Then [retort]" reply shape** (Ch.6 ×2, Ch.7 ×1 after the pass). Hold it at ≤1 per chapter.
3. **Narration, outside my scope (flagged, not touched):** sentence-initial "Nobody" ×3 in narration (the opening paragraph's "Nobody asked it unkindly", "Nobody's girl from anywhere owned such a thing", "Nobody went for the principal"); sentence-initial "Then" ×4 in narration, none of them a one-line pivot; "She did not tell me to get up." on the step, a negation sentence but not the semicolon pivot (the gate counts 0). The disruptor or editor may want to thin the "Nobody" openers, given the bible's warning about that shape.
4. **Tooling:** the voice-wear self-repeat scan reads HTML header comments. An edit I tried to the chapter's metadata comment ("(after dialogue-polish)") failed the gate against another chapter's comment, so I reverted it. A comment should not be able to fail a prose gate, and `voice_wear_check.py` should strip `<!-- -->` the way `shape_check.py` does (an UPDATE-RULE fix at the template/root).

## Cover-the-Name Test: FINAL
- The shovel (Mara / Kallia): **PASS.**
- The clothes (Kallia / Mara): **PASS.**
- Walking, sitting, eyes (Kallia / Mara / Theban): **PASS.** The subtext now runs entirely through instruction.
- The bath (baker's wife / mole girl / Kallia / Mara): **PASS.** This was the weakest scene before the pass (one indistinct line, and two women sharing a rescue imperative and a tag).
- The lentils (Mara / Kallia): **PASS.**
- The salt market (salt-seller / sprat-seller / Mara): **PASS.**
- The carding evening (Kallia / Mara): **PASS.**
- The gate (Valens / Kallia): **PASS.**
- The spring (drover / salt-seller): **PASS.**
- The broken jar (Kallia / Mara): **PASS.**
- The Syracuse plan (Kallia / Mara): **PASS.**
- The council (Sosandros / Kallia / the father / Mara): **PASS.**
- Home and midwinter (Kallia / Mara): **PASS.**

## Gates after the pass (from /home/user/Books)
`bash books/the-hour-of-ash/tools/check_chapter.sh 7`:
- style clean (simile 2.5/1k, em-dash 2, foreshadow 0)
- grammar 0 errors
- rhythm 0
- show/tell no flags (dlg 20.2% on its own measure)
- voice-wear strict clean
- tic gate clean (and-chains 2, credential asides 1, negation pivots 0, no gesture class over cap)
- echo scan 0
- metaphor no flags (median 17, 15.5% over 40 words)
- shape CLEAN (open `narrative`, end `question`, 3 breaks)

`python3 books/the-hour-of-ash/tools/tic_report.py --echoes 7`: **0 echoes**.
