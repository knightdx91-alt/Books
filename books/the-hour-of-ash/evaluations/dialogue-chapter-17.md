# Dialogue Polish Report — Chapter 17 "Games on the Isthmus" (run 2)

Scope: a dialogue-only pass over the Writer's draft (`manuscript/chapters/chapter-17.md`, 2026-10-21).

**Kept exactly, as the brief required:**
- the first line, "The boards left their dust on my fingers.", and the rest of the opening paragraph (byte-identical, md5 checked);
- the closing paragraph and the sail sentence (byte-identical, md5 checked);
- the 3 breaks and the section order;
- Valens's one bare "No." to "Will they wait?";
- Celer's slow beat at the shade line (the held sentence): not touched.

**Narration:** untouched except in three places:
- where narrated speech became speech (Plautia's briefing in the litter; the clerk in the store);
- beats and tags within one sentence of a changed line;
- one grammar slip in the sentence that reports Plautia's introduction (see Remaining Concerns).

A dialogue-polish line was added to the header comment.

## Audit Summary
- **Dialogue ratio:** 31.0% → **31.8%** by shape_check (show_tell 30.9 → **31.7**). Band 30–40, so it is now off the floor. All of the gain is in S1.

  | Section | Before | After |
  |---|---|---|
  | S1, the office | 22.5 | **25.0** |
  | S2, the lane | 34.8 | 35.3 |
  | S3, the colonnade | 41.6 | 41.5 |
  | S4, the road | 29.5 | 29.3 |

  Nothing was padded. S1 rose only by quoting what the narration had summarized, plus one Myrrhine line that turns her narrated drill into speech.
- **Words:** 7,194 → **7,190** (shape_check). style_check reads 7,202; `wc -w` reads 7,651 including the header comments. Range 6,900–7,900.
- **Median sentence:** 11 → **11** (gear low). Long sentences (>40w) 4.0%. Simile 1.2/1k. Em-dash 0.
- **Conversations analyzed:** 9.
  1. S1, the table (Plautia, Onesimus)
  2. S1, the shelves, low (Plautia, Mara)
  3. S1, the dowry reading and the runner (Onesimus, Plautia, the boy)
  4. S2, the lane (Valens, Mara)
  5. S2, the back door (Onesimus, Valens, Mara, the baker)
  6. S3, the colonnade (Celer, Valens, Plautia, Mara, Onesimus, the man with the seam)
  7. S3, after Celer (Onesimus, Plautia, Mara)
  8. S4, Plautia's farewell (Plautia, Valens, Mara)
  9. S4, the road (Valens, Mara, walk-ons)
- **INDISTINCT:** 2, both resolved.
  - Mara's "Nine names." It only echoed Valens's "Nine," and could have been anyone's.
  - Valens's "What was it she gave you?". He was standing at Plautia's back while the knife was named twice, so the question was implausible and voiceless.
- **WEAK:** 6, all resolved.
  - Plautia's three "[I/It] will…" lines in a row at the table. This was the same skeleton three times running, which breaks her rule.
  - Plautia's "Put there by whom?" and "By what?". Both are near-copies of her spent Ch.16 "By whom?".
  - Plautia's honey speech. It was an and-chain answering Celer's and-chain, so the two shared a cadence.
  - Onesimus's "He'll have run." It repeated his own S2 line "He'll have run by now." and was forming a spoken refrain.
  - Valens's "He'll be asking him who won." It repeated his "He'll ask who won." from 20 lines earlier.
- **FLAT_DIALOGUE:** 1, resolved.
  - The knife exchange in S4 stated the obvious. It is now a feeling question that Valens deflects into a practical answer (see Subtext).
- **Exposition dumps:** 0 found.
  - Plautia's litter briefing was checked for "As you know, Bob". It passes: it is a last-minute repetition of instructions before a theft, and it is new to the reader.
  - Celer's offer runs about 75 words. It is one conditional and short genial sentences, not a lecture, so it was left whole.
- **Tag overuse:** none.
  - Counts: "said" 68 (including narration), "told" 14, "asked" 2. "Said" is the house default, so none was replaced for its own sake.
  - Adverbs in tags: 2 → **0** ("he said, pleasantly"; "said Celer, kindly").
  - Plautia's "low" tag: 2 → **1**.
  - "said/told the [non-listener]": 2 → **1**. "He said it to the cake." stays; "said the clerk to nobody" became "said the clerk, waiting".

## Voice Distinctiveness Results (speech paragraphs, approx.)
| Character | Lines | Distinct | Weak | Indistinct | Post-Polish |
|-----------|-------|----------|------|------------|-------------|
| Plautia | ~32 | 26 | 5 | 0 | DISTINCT |
| Valens | ~31 | 29 | 1 | 1 | DISTINCT |
| Onesimus | ~24 | 23 | 1 | 0 | DISTINCT |
| Mara | ~24 | 23 | 0 | 1 | DISTINCT |
| Celer | ~14 | 14 | 0 | 0 | DISTINCT (beats and repetitions trimmed; see below) |
| Myrrhine (backfill) | 3 | 3 | 0 | 0 | DISTINCT |
| Felix (backfill) | 1 | 1 | 0 | 0 | DISTINCT |
| Walk-ons (runner, seam man, baker, brother, trainer, pine boys, coin seller, sausage-man, fat man) | ~14 | 14 | 0 | 0 | DISTINCT |

## Changes Made

### Subtext Additions
The outline's layer: Celer's pleasantries are a threat and an offer at once. The underneath of the whole chapter is "proof of who you are, and who holds it".

- **S1, the door.**
  - Surface: who will mind the door.
  - Underneath: Plautia buying the clerk's absence.
  - Technique: her "I will mind your door." became the blunt question "Do you expect a crowd?". He answers with his own grievance, the boys' race, so his problem comes up before the back door does.
- **S1, the shelves.**
  - Surface: where the book is.
  - Underneath: who hid it.
  - Technique: "Lost, or hidden?" now draws Mara's existing answer ("Somebody who wanted it lost and knew where to find it again"), which answers "hidden" without saying it.
- **S2, the lane.**
  - Surface: the witnesses.
  - Underneath: his past.
  - Technique: "Are they known to you?" is met by "Three of them are dead." He answers a different question than the one asked (deflection). Mara's later "Who were they?" now follows from it.
- **S3, the colonnade.**
  - Surface: a guest's courtesy.
  - Underneath: possession.
  - Technique: Celer's "Didn't you, Plautia?" became "I used to tell her so". The marriage is now in his mouth without the word *wife*.
- **S3, the clerk's leave.**
  - Surface: a kindness.
  - Underneath: Celer's ignorance of the man he thinks he owns.
  - Technique: Celer's "Go and see him crowned." assumes the grandson wins, and the clerk wants him to lose. The irony is the reader's, and nobody points at it.
- **S4, the knife.**
  - Surface: logistics (Myrrhine).
  - Underneath: Mara's guilt at taking a gift from a woman who gives everything away.
  - Technique: Mara's "Should I have refused it?" (her axis: she asks about feelings) gets "Her woman will be on the quay before us." He answers the practical half and leaves the feeling alone. This is spoken, so it is not a narrated non-answer.

### Voice Adjustments

**Celer** (genial, patient, "a friend you never had"; kept apart from Plautia)
- **Cadence split from Plautia.** The and-chain is now his alone (the boy at the rail; the judge who "goes to sleep after his lunch and wakes up and chooses"). Plautia's honey reply was recast as a subordinate period with a semicolon: "Since he could stand he has shouted before anyone gave him leave; tonight, when his nurse brings him honey in warm water that she has made too hot, he will not drink it." Every content word is kept; only the shape changed.
- **Repeated habits cut back:**
  - smile beats 3 → **1** (only "Celer smiled at him." after the donkey silence is left);
  - "Lupus" 3 → **2**;
  - tag-question plus vocative ("were we, you and I?", "wouldn't we, Onesimus?", "Didn't you, Plautia?") 3 → **2**;
  - "you and I" 2 → **1**;
  - "Come …" invitations 4 → **2** ("Come out tomorrow and sit with us" → "Sit with us tomorrow"; "Come to the house" → "The house");
  - "Then…" openers 2 → **1**.
- **No catchphrase.** No villainy is said aloud and no line is a monologue. Every pleasantry still cuts both ways.

**Plautia**
- **No skeleton twice running:**
  - the table is now question / declarative / question / declarative;
  - the superstition speech's three "He…" openers (an anaphora triad) became one period with a semicolon;
  - the seal question became her fingerprint, a formal period broken by a blunt question: "My father kept two seals, cut by the same engraver, his own and his freedman's," … "Which is that?".
- The litter briefing was turned from narration into her speech, as one subordinate period.
- **Pause beats:** S1 0, S3 1 (the chin), S4 1 (she waits for the litter).
- **Rules kept:** no contractions; "Then…" openers 1; Celer never named; nothing about the night; no coals.

**Onesimus** (bored, specific, with his own problem)
- Address "lady" 6 → **3**. Three remain: "Lady." as a whole reply, "You read, lady.", and "Lady didn't ask".
- Two new lines:
  - the store mutter, which was narrated speech: "Highest shelf in the place. The whole run of them.";
  - "The old years went up the ladder." (he puts the labor on whoever stacked them).
- "Then the last." → "That'll be the last." (his least-effort shape; it also takes a "Then" opener out of the chapter).
- "He'll have run." → "It'll be over." His second line about the race no longer repeats his first.
- "who won the boys" → "how the boys came in".
- He volunteers the chipped seal himself ("Your father's. The freedman's had a chip out of the rim."). This shows he knows the office by heart and can't be bothered.
- **No catchphrase.** The figs stay eating, never a fidget.

**Valens**
- "He'll be asking him who won." → "Asking him how." The flat correction of Mara (Felix asks, he doesn't tell) replaces the second "who won".
- **Rules kept:** no comparison in his speech; narrated non-answers 0; general-truth sayings 0 (the brief allows up to 1); bare "No." 1, kept.

**Mara**
- "Nine names." → "Are they known to you?" (her Greek has no contractions).
- "He saw it. He saw your hands. He will walk out…" → "He saw it. Your hands, and what was in them. He will walk out…". The anaphora triad is broken and the panic stays.

**Myrrhine**
- The narrated drill ("to cure me of her mistress's hem") now opens with her spoken string of small failings: "You're on it again. You'll have her over in the street."
- No price and no lupins.

**Felix:** untouched. There is no "Is it" opener.

### Tag/Beat Replacements
- 2 adverbs removed from tags.
- 2 "let that [lie / go by]" narrated non-answer frames replaced. One became "His eyes went past her…"; the other became "His head went round to the litter, and the men behind it." (it points to "My man" before he names him). The cap is ≤1 per chapter; the chapter now has 0.
- 2 "as if / as though" beats replaced next to dialogue: "as though the race might be up there" → "toward the Isthmus"; "as if she had given him a present" → "Celer had his answer ready." Chapter total 3 → **1** (the protected slow beat). The voice-dna cap is ≤1.
- 1 "said to [non-listener]" removed, 1 "low" tag removed, and 1 tag changed to "asked" ("Well?" Plautia asked).

### Natural Speech Additions
- 1 non-sequitur (the clerk answers "Do you expect a crowd?" with the boys' race).
- 1 deflection (Valens on the knife).
- 1 overheard aside (the clerk in the store).
- 0 interruptions added; em-dash stays at 0, which is the voice-dna aim.

## Constraint ledger (final page)
- **Celer:** no catchphrase; never *wife*; no direct threat; no voice raised; no monologue.
- **Onesimus:** no catchphrase; his grandson is in S1 (the race), S2 (the reveal) and S3 (Celer's "crowned").
- **Valens:**
  - comparisons in speech: 0;
  - narrated non-answers: 0;
  - general-truth sayings: 0;
  - bare "No.": 1, kept exactly.
- **Plautia:** no skeleton twice running; pause beats ≤1 per scene.
- **Myrrhine:** no prices, no lupins.
- **Felix:** no "Is it" opener.
- **Mara:**
  - she follows the slow, plain talkers (Plautia's book Latin, Celer's unhurried delivery, which the narration says is "pleasant and unhurried", and the clerk);
  - nothing fast was added for her to follow;
  - the fat man's javelin talk stays narrated, which shows she isn't following it.
- **"Isthmia":** 0.
- **Commands echoed back as compliance:** 0. The tool's one candidate is the known false positive (Olympia → loaves).
- **Spoken lines borrowed from earlier chapters:** none.
  - `tic_report.py --echoes 17` reports "none".
  - Every new line was grepped against Ch.1–16 before it went in. "the two of us" (Ch.15) and "Top shelf" (Ch.3) were rejected that way.
- **Lifts from the voice-bank samples or the bible's sample lines:** none.
- **Foreshadowing:** none (0 by the gate).

## Gates (`bash books/the-hour-of-ash/tools/check_chapter.sh 17`, from /home/user/Books)
All clean.
- **style:** clean (simile 1.2/1k, em-dash 0, foreshadow 0);
- **grammar:** 0 errors;
- **rhythm:** 0 flagged;
- **show/tell:** no flags, dialogue 31.7%;
- **voice-wear:** strict clean;
- **tic gate:** clean;
- **echo scan:** 0;
- **spoken-line echoes:** none;
- **metaphor:** no flags, median 11;
- **shape audit:** CLEAN, and `--strict` is CLEAN as well.

During the pass the gates caught seven new phrases from my edits that had appeared in earlier chapters, plus three more that would have been third uses book-wide. All were varied before finalizing:
- "every one of them";
- "tipped his head at";
- "my father's house";
- "said plautia from";
- "then you'll want";
- "do you know";
- "up under the roof";
- "since the day";
- and two joins across a full stop: "at the back. Up the ladder" and "tidied away. He looked".

## Remaining Concerns
- **A narration slip, fixed and flagged.** S1 paragraph 4 read "When we arrived he was digging, and while Plautia gave him her name and her father's, and he was digging still." The stray ", and" was removed ("…her father's he was digging still."). It is the sentence that reports Plautia's introduction, and it was broken. Nothing else in it changed.
- **S1 is still the lightest section (25%).** The rest is the theft itself: Mara's hands at the cord and the threading, the Myrrhine backfill and the roof backfill. None of it is summarized speech. Raising it further would mean inventing talk during a silent theft, which is padding the brief forbids.
- **Bible sync for the evaluator and entity-tracker.**
  - Several quoted lines in the Ch.17 blocks for CELER, PLAUTIA, ONESIMUS, VALENS and MARA, and in the at-risk-after-Ch.17 block, now differ from the page:
    - "Didn't you, Plautia?";
    - "Come out tomorrow and sit with us";
    - "Come to the house";
    - "Then go and hear who won it.";
    - "He'll have run." (the second one);
    - "If you hear who won the boys";
    - "Put there by whom?" / "By what?" / "Is that seal my father's…";
    - "I will mind your door.";
    - "The old years are at the back, lady. Up the ladder.";
    - "Then the last.";
    - "Nine names.";
    - "What was it she gave you?" / "Her grandfather's knife.";
    - "He'll be asking him who won.";
    - "He saw your hands.";
    - Plautia's honey line and her superstition speech;
    - "Lupus" in Celer's mouth is now 2.
  - The Writer's report claimed "every Ch.17 quote checked against the page". The next bookkeeping sync should re-run that check against this page.
  - New spent lines:
    - Onesimus: "Highest shelf in the place.", "It'll be over.", "That'll be the last.";
    - Plautia: "Do you expect a crowd?", "Lost, or hidden?", "My father kept two seals…";
    - Celer: "Go and see him crowned.", "I used to tell her so";
    - Mara: "Should I have refused it?", "Are they known to you?";
    - Valens: "Asking him how.";
    - Myrrhine: "You'll have her over in the street.".
- **Counts the bible's at-risk-after-Ch.17 block should carry:**
  - as if / as though: 1 (was 3);
  - smile beats for Celer: 1;
  - "who won": 2 (Felix's backfill, and Valens's "He'll ask who won.");
  - "And…" dialogue openers: 4, spread across Valens 2, Mara 1 and Celer 1 (cap 4). This is at the cap; the next chapter should give it one owner or none.
- **For hook-craft and the disruptor:** the chapter's dialogue share is now 31.8%. A trim of about 130 quoted words would put it back on the floor, so the disruptor should cut narration before speech.

## Cover-the-Name Test: FINAL
1. **S1, the table: PASS.** Plautia's periods and blunt questions against the clerk's least-effort replies and grievances. They no longer share the "I will…" chain.
2. **S1, the shelves: PASS.** "Lost, or hidden?" is Plautia's alternative-question bluntness. Mara answers plainly, in contraction-free Greek.
3. **S1, the reading and the runner: PASS.** The clerk reads flat between figs; Plautia covers the slip coolly; the boy relays.
4. **S2, the lane: PASS.** Valens is short and level, with no comparisons. Mara asks, then panics in fragments (no triad).
5. **S2, the back door: PASS.** Onesimus's family grievance is unmistakable. The baker's grievance is about coin and weather, and the two are kept apart.
6. **S3, the colonnade: PASS.**
   - Celer: warm "we", contractions, soft questions, and he alone uses the and-chain.
   - Plautia: no contractions, periods, blunt questions.
   - Valens: four-word truths.
   - Mara: one stiff line.
   - With the names covered, no Celer line could be Plautia's and no Plautia line could be Celer's.
7. **S3, after Celer: PASS.** The clerk's "You were never in." Plautia prices the swans by their maker, not by a figure.
8. **S4, the farewell: PASS.** Plautia's formality breaks into "Did you stand on my hem?". Valens's "That was where he was standing." is deadpan literalism.
9. **S4, the road: PASS.** The walk-ons each have one register (the pine boys' cries, the coin seller, the trainer's delight, the fat man's javelin). Valens's "I lead mules." and the bare "No." are untouched.
