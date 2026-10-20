# Dialogue Polish Report — Chapter 12 "The Kirrha Road" (run 2)

Scope: dialogue only, plus the tags and beats attached to it. Narration paragraphs are untouched apart from beats within one sentence of a line. These are byte-identical to the writer's draft (checked by diff against a saved copy):
- the first line, the stranger's "Lupus? By the Twins, it is. Lupus, walking behind mules.";
- the final punch, "A cart had stopped beside the ditch." (7 words);
- the fight's run from the knife to "The man in the brown cloak stayed in the ditch.", apart from one tag cut that makes it faster (below);
- the cap sentence, the shaking at the fall, and the Kirrha flashback.

The ledger signatures (`dialogue` → `punch`) and the 2 breaks are unchanged. The header comment carries the post-polish counts.

## Audit Summary
- **Dialogue ratio (shape_check, the ledger metric):**
  - Before: 25.9% of 5,108 words.
  - **After: 26.2% of 5,083 words** (band 25–35). Dialogue rose slightly, because I cut four narrated gaze beats and added one line for the big man.
  - The show/tell gate's own measure moved from 25.9% to 26.2%.
- **Em-dashes:** 0 → 0. **Simile:** 0.8 → 1.0/1k (the big man's "two like that"). **Adverb tags:** 1 → 0 ("warmly" cut). Median sentence 10, gear low.
- **Conversations analyzed:** 7.
  1. The stranger and the three men.
  2. The ditch.
  3. The camera at the stream.
  4. The telling.
  5. The ford: Felix, the cover story and the purse.
  6. The graybeard.
  7. The climb.
- **Lines flagged INDISTINCT:** 0.
- **Lines flagged WEAK:** 6, all resolved.
  - The big man had no voice.
  - Mara's "The glass is whole." repeated the narration two paragraphs above it.
  - Felix's "Was it…?" frame was forming: 4 uses, now 1.
  - Valens's "It was off," and "The whole of it, then," both repeated the previous speaker's words back as agreement.
  - Mara's Kallia line was garbled ("hear it … about somebody dead").
- **FLAT / speaking in themes:** 2, both resolved.
  - "People do, mostly." was the chapter's theme spoken as a generalization, straight after the killing, which the writer warnings forbid.
  - "That's how it gets told." named the theme instead of letting the contradiction show it.
- **Exposition / speech shape:** the telling ran in long blocks (one block of 13 sentences). I split it and cut its single self-pitying line (details below).
- **Tag overuse:** none. "said" stays the invisible default.
  - 1 adverb tag cut.
  - 1 tag removed inside the fight (*Rudiarius* now untagged, as VOICE UNDER PRESSURE requires).
  - 1 tag removed where the alternation makes the speaker plain ("Kallia, then. Nobody else.").
- **Bare "No.":** 3 → **2**. Valens has 1, the required "Was it one blow?" / "No." Mara has 1, "Are you cut?" / "No.". Her second "No." (to Felix's "Did you see him do it?") became "I heard it.", so Valens's "No." now lands alone.
- **Narrated non-answers:** 0. The one near miss, "Valens's eyes were on me, not on him." after Felix's "Who gets his knife?", is now an act: "Valens came past him to me."
- **Banned stage business, checked by grep and by gate:**
  - None in the chapter: nods, shrugs, sighs, swallows, "a long moment", bends, kneels, crouches.
  - Command echo: 0 candidates.
  - Gaze beats in the stream scene went from 5 to 2. I cut "He looked at the water.", "For a while he only looked." and "He looked at it a little longer." and kept "He was watching me do it." and "Then it was my neck he was looking at."
  - The "where the two had gone" watching shape went from 3 to 2. Only the beat next to dialogue was mine to change.
  - "Felix shifted the goat higher" was cut; the "shift the goat" in the narration a page later stays.
  - The "kept" cluster beside the lines was varied: "Valens kept it where it was … and walked." / "I kept my hands in the cloak." / "and kept on at them".
- **Mara's questions:** 0 (checked line by line). Her Greek is uncontracted throughout. She speaks no English anywhere.
- **Gates (run from /home/user/Books):**
  - `bash books/the-hour-of-ash/tools/check_chapter.sh 12`: style, grammar, rhythm, show/tell, voice-wear (strict), tic gate, echo scan, metaphor and shape are all clean.
  - `python3 books/the-hour-of-ash/tools/tic_report.py --echoes 12`: **0 echoes**, no command-echo candidates.
  - My first pass created 6 echoes ("he talked about", "man with the donkey", "to the next mule", "said and went on", "he said nobody", "i said he took") and 3 tic-gate recurrences ("with both hands", "went down the", "i said valens"). All are varied.

## The telling (Valens's account at the stream)
**Shape.** It is still a witness's chronology. The washing and silence break it, and Mara never asks a question:
- "They gave me the wooden sword at Corinth";
- the washed forearms;
- the emperor's year;
- **"He did the backs of his hands."**, moved up to split the arena block;
- the Gaul and the tablet;
- Felix and the goat below;
- the oath;
- the cloak water;
- "Two years …";
- the lace;
- Celer's debts and the night in the atrium;
- "My hands stayed in the cloak.";
- the dowry share;
- the cloak held in the fall;
- the flogging and the tablet taken;
- **"The cold had my feet again, up to the ankle bones."** (new: Mara's body, not a measured silence);
- Celer's claim, the record office and the escape;
- "He was quiet for a while.";
- the brother and the boy;
- the wringing;
- the knowledge path.

The longest block is now 11 sentences, down from 13.

**Changes:**
1. **The rudis and the games.**
   - "The year he was going on about." became **"He had the year right, the one on the road."** It grants the dead man his one true fact and leaves the rest of his story standing wrong, without Valens ever talking about the man he killed.
   - "The emperor didn't know that. He stayed in his chair, too. That's how it gets told." became **"Nobody on the benches knew that. The emperor never got out of his chair."** The stranger said "the emperor rose in his box", so the correction now lands by contradiction with no theme line attached. "Nobody on the benches" includes the stranger.
   - "and the emperor sent the sword down to me" became "and he sent the sword out to me across the sand". This cut a third "emperor" and the second "down" in the sentence.
2. **Plautia is named once.** "…one that people would know from the sand and stand back from. **Plautia.** I swore to her in his atrium…". The brief lists her among the account's beats, Ch.16 needs Mara to know the name, and her name is not on Valens's evasion list. It is a bare one-word fact, not Celer's "the lady Plautia".
3. **"A freedman wants work."** (a present-tense maxim) became **"After the sword I needed work."** (chronology).
4. **The order of events.** "Then the emperor gave the Greeks their freedom" followed "Two years I walked behind her" and put the freedom (late 67) after the two years (to 69). It is now "**By then** the emperor had given the Greeks their freedom, and Celer's post had gone with it. He'd stayed on…". A witness does not misorder his own evidence.
5. **No grievance.** I cut "Nobody's going to walk in there and say it aloud for me.", the account's only self-pitying line. The record office stays as a plain fact ("with my name in it").
6. **No figurative speech.** "before the winter ate them" (a metaphor in the mouth of a man who never compares) became "who couldn't feed them till spring".
7. **Kept verbatim:** "I was a good bodyguard. That was the use of me.", "They'd been shown where to stand.", "A quay doesn't ask twice.", "He wants me in a ditch."

## The road: the stranger and the three men
- **The talker** keeps every line: the fan's patter, the oath by the Twins, the two drachmas, "I've forgiven you.", "And here's the hand." His *Rudiarius* is now untagged and without "warmly". The fight starts on an unglossed, unattributed word, then the arm, then the knife.
- **The big man** had no voice. He now has one line, set against the talker's "There's not another hand like it in Achaea": **"My brother's a butcher," he said. "He's got two like that."** It is a dull, literal deflation of the legend from a hired man who is still watching the hand. It is not villain talk.
- **The third man** is unchanged: the low laugh, then "Be still, mistress. Be good." He speaks to her as to an animal.
- "Catch up the boy" became **"Go on up to the boy,"**, the idiomatic order. She does not go.
- "Valens kept walking." … "Valens kept it where it was, at his side, and walked." The second became "The hand stayed at Valens's side." (no repeated keep/walk).

## Felix
- **The camera burst** dropped two "Was it…?" frames: "What's that? Is it silver? I saw one of them go off through the olives holding on to his head. You hit him with it?" It is now a stack of question, question, boast-observation and statement-question.
- **The climb:** "Was it quick?" became **"Quick, though?"**. "Was it one blow?" is now the only "Was it" in the chapter and stays exactly as written, to Valens, with the one "No.".
- **The crust lie:** Valens no longer echoes "It was off". He accepts the lie by acting on it, deadpan and literal: **"Don't give the goat any more of it."** The goat is the one who was eating the crust a page earlier. This is the card's unintended deadpan humour, and he does not praise Felix.
- **No catchphrase** and no repeated boast: the invented sword stays. Exits by line + tag + "and": 0. "nobody" in his speech: 0. Speed is carried by the stacking.

## Mara
- **No questions.** "Did you see him do it?" / "I heard it." / "Quick, though?" / "I was watching something else." She answers a different question each time, keeps the death as a sound and refuses Felix his story. His look then says she has cheated him.
- "The glass is whole." (spoken two paragraphs after the narration's "The glass was whole.") became **"Only the rim is bent."** This is the repairer's answer, naming where it failed.
- "Kallia will hear it at the spring by morning," I said, "about somebody dead by the road below the ford." became **"Kallia will hear at the spring tomorrow that a man is dead below the ford," I said.**
- The rest is kept: "I read it twice," / "My question wanted carrying." / "Praxias wanted five drachmas." (the 5-against-500 irony is still never pointed at) / "It is only the wool," / "I am not telling Kallia a story. She gets the whole of it from me, or nothing."

## Valens (outside the telling)
- "People do, mostly." became **"He had his robbers before you opened your mouth," Valens said.** The graybeard said "Somebody's had his purse." before Felix spoke, so the line is literally true. It reads the man, deflates Felix's pride, and shows the theme (other people's stories) through one person, not as a general truth. The writer warnings ban an aphorism after the killing.
- "Then she hears we came by after." became **"She hears what the donkey man heard."** This is concrete, and it removes a "Then…" opener.
- "The whole of it, then," he said. "Her, and nobody else." (her words repeated back as compliance) became **"Kallia, then. Nobody else."**, untagged.
- "Keep what he doesn't," he said, and kept on at them. became "Valens was down the string, checking girths. "Keep what he doesn't," he said."
- Walk-offs after a line: 1 ("He was first down the goat path to the ford.", replacing "Then he left me for the ford."). No simile or comparison in his speech. Bare "Felix." 0.

## Voice Distinctiveness Results
| Character | Speeches (approx.) | Distinct | Weak | Indistinct | Post-Polish |
|---|---|---|---|---|---|
| Valens | 40 | 36 | 4→0 (two echoes, the theme line, the maxim) | 0 | **PASS** |
| Mara (Greek) | 19 | 17 | 2→0 (the glass echo, the Kallia line) | 0 | **PASS** |
| Felix | 14 | 13 | 1→0 ("Was it…?" frame) | 0 | **PASS** |
| The talker | 5 | 5 | 0 | 0 | **PASS** |
| The big man | 0→1 | n/a | n/a | n/a | **PASS** (voice added) |
| The third man | 1 | 1 | 0 | 0 | **PASS** |
| The graybeard | 4 | 4 | 0 | 0 | **PASS** |

**Cover-the-name:**
- **Valens** is contracted, level, concrete and unsubordinated, and never compares. His jokes are literal by accident.
- **Mara** is uncontracted and qualifying, and asks nothing.
- **Felix** stacks questions and boasts, and is never still.
- **The talker** is sociable and nostalgic and swears by the Twins.
- **The big man** is a dull literalist.
- **The third man** is wheedling and speaks as to an animal.
- **The graybeard** has his story ready and puts himself first ("it won't be me").

## Bible quotes my edits invalidate (character-bible.md NOT edited; for the next sync)
**MARA, Ch.12 block (≈l.234–264):**
- "The glass is whole." is now "Only the rim is bent." The narration's "The glass was whole." is unchanged.
- Add "I heard it." (to Felix's "Did you see him do it?"). It replaces her second bare "No.".
- Add "Kallia will hear at the spring tomorrow that a man is dead below the ford,".
- **Knowledge:** add that she now knows Plautia's name (said once by Valens).

**VALENS, Ch.12 block (≈l.539–581):**
- "The Gaul was older than me, and slow on his left side. The emperor didn't know that. He stayed in his chair, too. That's how it gets told." is now "The Gaul was older than me, and slow on his left side. Nobody on the benches knew that. The emperor never got out of his chair." Also new: "He had the year right, the one on the road.".
- "That's how it gets told." is no longer on the page. Drop it from the block's Spent list and from the at-risk list (or keep it there as banned; it is harmless).
- "Nobody's going to walk in there and say it aloud for me." is cut.
- "It was off," (agreeing to the crust lie) is now "Don't give the goat any more of it,".
- "People do, mostly." (in "With Felix" and in Spent) is now "He had his robbers before you opened your mouth,".
- "Kallia: 'The whole of it, then,' … 'Her, and nobody else.'" is now "Kallia, then. Nobody else.".
- Walk-off quote: "Then he left me for the ford." is now "He was first down the goat path to the ford.".
- New in the telling: "After the sword I needed work.", "Plautia." (named once), "By then the emperor had given the Greeks their freedom…", "who couldn't feed them till spring".

**FELIX, Ch.12 block (≈l.961–976):**
- "What's that? Is it silver? Was it you broke that one's head? I saw him go off through the olives, holding it. Was it with that?" is now "What's that? Is it silver? I saw one of them go off through the olives holding on to his head. You hit him with it?".
- "Was it quick?" is now "Quick, though?".
- "(unanswered by Valens, whose eyes are on Mara)" is now "Valens came past him to me.".
- Counts: "Was it…?" 1 ("Was it one blow?").

**CELER, Ch.12 by proxy (≈l.1019–1023) and the Ch.12 walk-on note (≈l.1686–1708):**
- The big man now speaks: "My brother's a butcher," … "He's got two like that."
- The talker's *Rudiarius* is untagged ("The first man took Valens by the arm.").

**AT-RISK after Ch.12 (≈l.2875–2912):**
- In the telling list, drop "That's how it gets told." (gone).
- In the robbery/cover-story list, "People do, mostly." is now "He had his robbers before you opened your mouth.".
- Add as used once: Valens's deadpan acceptance of a lie ("Don't give the goat any more of it,"); "Only the rim is bent."; "I heard it." as a refusal; the big man's butcher line; naming Plautia (once, in the oath). Ch.16 introduces her without a "you told me about her" callback.
- The counts line "bare 'No.' 3 (Valens 1, Mara 2)" is now **2 (Valens 1, Mara 1)**. Dialogue 26% → 26.2%. Words 5,108 → 5,083.

**ENTITY_STATE:** a knowledge fact for the next UPDATE. Mara learns Plautia's name in Ch.12.

## Remaining Concerns
- **Dialogue sits 1.2 points above the 25% floor.** Any later pass that cuts lines must re-measure with shape_check. The cheapest cuts would cost subtext: Felix's "Quick, though?" / "I was watching something else." and the big man's line.
- **"without looking in it"** ("he tied it on without looking in it") is narration, outside my remit. The phrase family now has one use in each of 5 chapters (1, 5, 7, 11, 12). It is the trust act and may stay, but the disruptor or editor should judge it.
- **"shift the goat on his shoulders"** (narration, the last scene) is now the chapter's only shift beat. I cut the dialogue-side one.
- **"the one on the road"** is how Valens refers to the dead man. It mentions him without the killing, which stays inside his evasion. If the continuity audit reads any reference to the dead man as a breach, the fallback is "The year was right."
- **The writer's report** quotes the old wordings ("That's how it gets told", "He stayed in his chair, too", "People do, mostly", the camera burst). It is not edited; it is history.

## Cover-the-Name Test: FINAL
| Conversation | Result | Note |
|---|---|---|
| The stranger and the three men | PASS | each man has his own register; *Rudiarius* untagged; the fight's speed unchanged |
| The ditch | PASS | "Valens came past him to me." replaces the narrated snub |
| The camera at the stream | PASS | "Only the rim is bent." |
| The telling | PASS | chronological, broken by washing and silence, no grievance line, no comparison, Plautia named |
| The ford | PASS | Felix's stack de-framed; Valens accepts the lie deadpan, no echo |
| The graybeard | PASS | "He had his robbers before you opened your mouth" replaces the theme line |
| The climb | PASS | Mara deflects twice and asks nothing; Valens's single "No."; "Kallia, then. Nobody else." |
