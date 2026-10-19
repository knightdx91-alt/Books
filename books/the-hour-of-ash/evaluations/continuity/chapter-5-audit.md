# Continuity Audit: Chapter 5 (run 2, per-chapter drift audit)

**Date:** 2026-10-19
**Mode:** MANUSCRIPT AUDIT. Ch.5 checked against Ch.1–4 (finalized, re-read as they stand) and against the plan.
**Chapter reviewed:** `manuscript/chapters/chapter-5.md` (8,364 words by `wc`; 433 lines; 5 sections, 4 breaks)
**Read against:** outline.md (Ledger row 5; `## Chapter 5` beats, Beat subversion, Writer warnings; `## Chapter 6` opening), foundation.md (§3 Mara and Kallia; §4 row 5; §4f; §5; §6/6a/6b/6d; §9; §10), voice-dna.md (§0, §1, VOICE UNDER PRESSURE, §3b, §4, §6, §8), voice-bank sample-01 and sample-03, character-bible.md (Mara; Kallia; the Ch.3–5 walk-on notes; retired and at-risk lists), ENTITY_STATE.yaml (**already UPDATED for Ch.5**: `chapters_tracked: [1, 2, 3, 4, 5]`; CH5-1…CH5-6 and the CH3-7, CH4-2, CH4-3 and P5 `ch5_note`s are UNRESOLVED and processed below), STATE.yaml guardrails and canon, evaluations/continuity/chapter-4-audit.md (the carry-over watch list).
**Mechanical baseline (re-run for this audit, `bash tools/check_chapter.sh 5`):**
- Style clean: simile 2.0/1k, adverb 3.5/1k, em-dash 2, foreshadow 0.
- Grammar clean. Rhythm: 0 flagged.
- Show/tell: no flags. Dialogue 20.3%.
- Voice-wear strict: clean. Tic gate clean, including the gesture layer.
- Metaphor: median sentence 17, 12.8% of sentences over 40 words.
- Shape audit (5 chapters): CLEAN. Semicolons 3.1/1k.

**Total findings:** 43. **CRITICAL: 1 | WARNING: 17 | NOTE: 25**

The gates are clean. The CRITICAL is a registered cap broken twice; it is a clause-level fix, not a plot error. Most WARNINGs are devices just starting to form, which the gates do not see: gesture classes the gesture layer does not count, cross-chapter constructions under the n-gram length, and walk-on cadences.

---

## Scorecard by category

| Category | Result |
|---|---|
| (a) Beats / ledger | **PASS.** All six beats are present and in order: descent l.3–43 → Sacred Way l.47–149 → steps and beating l.153–191 → herald l.201–233 → spring and Kallia l.279–419 → storeroom l.423–433. The three NON-NEGOTIABLES are intact. Empty bases with fresh pry-marks: l.89–97. Herald, then AD 70 and Vespasian, with no 79: l.207–231. Kallia inspects hands and teeth and takes Mara as labor: l.305–413. Exactly 4 breaks (l.45, 151, 193, 421). Scene-set opener of 25 words; long-fade close of 66 words; neither closing nor opening paragraph is a one-liner. 8,364 words against a target of 8,300. Median 17, inside the high gear. Dialogue 20.3%, at the floor of the 20–30% band (see N-01). |
| (1) Character consistency | **Mara: WARNING ×1.** W-02: "loved" appears in her narration for the first time in the book. **Kallia against her card on first live appearance: PASS.** No proverbs. She answers the English outburst with a task (l.333). She says nothing about herself; the Thebans are her household. No thanks, and none from Mara either (l.427). She never sits, never touches Mara, and never asks Mara's name. Her own life is shown before she sees Mara (garland, feet). |
| (2) Timeline | **PASS with notes.** The chapter covers the night after Ch.4 plus the whole next day, into its night. That fits "yesterday" (l.329) and "the morning before" (l.5). It is not "the same day as Ch.4's end" (N-02). Titus's Jerusalem reaching Delphi in autumn 70 by Corinth post is plausible. Nero in Greece 66–67 and his death in June 68 are accurate. The lead's 2–3 years of weathering agrees. Notes N-03, N-09, N-22. |
| (3) Information flow | **Year: PASS.** She gets ≥68 from the guide's "He's dead now" and ~69–70 from the lead, then AD 70 and Vespasian from the herald, by her own history (l.109, 227–231). She learns nothing of Pompeii, Italy as a destination, or a door home. **WARNING ×2:** W-03 (her comprehension jumps), W-04 (CH5-6: which language her last replies are in). |
| (4) Plot threads / payoffs | **PASS.** Good setup and payoff: she skips the purification basin at the gate (l.49), and the warden asks "Who let her up here unwashed?" (l.161). Open threads are logged: the clay discs and the watching procurer (N-13). |
| (5) World rules / geography | **WARNING ×2.** W-01 (CH5-5: the taxi's direction is reversed). W-19 (the flashlight is unaccounted for while she gropes in the dark). The status obstacle is real and repeated without becoming a refrain: "Where's your man?" (l.23), the mother (l.41), "Whose is she?" (l.163), the procurer (l.271), "Whose are you?" (l.355). |
| (6) Objects | **PASS with WARNING ×1.** W-07: the rummage by feel through the duffel is now in three chapters, and the sock is again "rolled tight". The knucklebone is untouched (its touch is spent; correct). The ledger is in N-17/N-18. |
| (b) Voice | **VOICE UNDER PRESSURE at the beating: PASS.** At l.157–191 the asides die. The prose is plain physical sequence ("The bag slid. I held the strap."), the "Down." is untagged, and there is no lyricism. The asides return at l.227 ("a nose like a doorknocker"). **WARNING ×2:** W-08 (a condition report in the aftermath), W-14 (the voice-bank sample-01 frame reused). |
| (c) Emerging tics / devices | **CRITICAL ×1** (C-01 the item-by-item look, 3rd and 4th uses on the page). **WARNING ×11:** W-05, W-06, W-07, W-09, W-10, W-11, W-12, W-13, W-15 (W-08 and W-14 are counted under (b), W-18 under (e)). |
| (d) Real place / period | **Strong.** The Sacred Way runs in the right order: Corcyraean bull first; the Arcadian group opposite the Spartan navarchs; the Siphnian treasury with its caryatids and a gigantomachy frieze on Egyptian blue; the Athenian treasury at the bend; the polygonal wall written with manumissions; the black-and-white Chian altar; then the temple. The temple has stucco on poros, colored entablature, gilded shields and a family pediment. The approach from the east is right: the gymnasium track below the road, then Castalia, where pilgrims wash their hair. The Roman agora with its votive shops lies outside the gate, with a perirrhanterion. The beam-and-windlass press is right, down to the skimming shell (Columella's *concha*). Vespasian's titulature (Autokratōr Kaisar Ouespasianos Sebastos) and the archon-dated decree formula are right. NOTES N-03 to N-08. |
| (e) Retired reflexes | **PASS with WARNING ×1** (W-18, an anaphora triad of "the same…"). No foreshadowing. No define-by-negation opener. No closing aphorism, no performed candour, no device used as a button. Near-misses are in N-14. |

---

## PRIORITY: UNRESOLVED ENTITY_STATE CONFLICTS (processed first)

| ID | Verdict | Where it lands below |
|---|---|---|
| CH5-5 taxi direction | Both readings are still on the page. A geography contradiction in the literal reading. | **W-01** |
| CH5-6 language of "No." / "Eggs." / "Mine." | Both readings are still possible. A behavioral contradiction risk against the planned chaos trait. | **W-04** |
| CH5-4 microcassette, 3rd contact | The planned touch is on the page (INTENT). The repeated rummage around it is drift. | **W-07** + N-18 |
| CH5-3 unscheduled frame | INTENT. The arithmetic holds (9 exposed, 27 left on the plan count). Recommend resolving it. | N-18 |
| CH5-2 stale bible paraphrases | Documentation only. | N-21 |
| CH5-1 lodging "by the spring" | Loose wording, not an error. | N-20 |
| CH4-3 jacket/fleece | Ch.5 says "fleece" six times. Still open. | N-19 |
| CH4-2 granola unit | Ch.5 keeps the pouch as the unit. Harmless; leave. | — |
| CH3-7 door never named | Ch.5 gives her the span (1,928 years) and a plan to sit at the crack again. Not saying "door" is in character. Recommend resolving it (prose wins). | N-23 |
| P5 Corinth news speed | Ch.5 widens the gap: the post arrives in weeks. This is an outline issue for Ch.9, not a Ch.5 error. | N-24 |

---

## CRITICAL ISSUES (fix before finalize)

### [C-01] The item-by-item look, 3rd and 4th uses on the page (registered cap: "a third use anywhere in the book is a defect")
- **Category:** emerging device / at-risk list (character-bible "At-risk after Ch.1 … the item-by-item look"; Ch.4 audit C-01: "The item-by-item form is now closed for the rest of the book").
- **Evidence (on the page now):**
  - chapter-1.md:305 "Her eyes went from the pencil to the garbage bag held against my chest."
  - chapter-3.md:7 "pointed at the slope above us with his whole arm, and then at the bag, and last of all at me"
  - **chapter-5.md:37 "He took in my trousers before my face."**
  - **chapter-5.md:271 "His eyes went over my trousers and then the rest of me"**
  - Related: chapter-1.md:55 "took in my jacket" makes l.37 a near-verbatim frame ("took in my [garment]"). chapter-5.md:291 itemizes Mara from Kallia's sightline ("kneeling…, with my sleeves pushed up, in trousers, with my wet hair in my face").
- **Problem:** Ch.4's instance was cut, so the page count stood at 2. Ch.5 adds two more, both of a walk-on sizing up Mara's garment and then her: the exact sequence the Ch.4 audit closed.
- **ERROR or INTENT:** the CONTENT is INTENT, because the trousers have to be noticed: they are the status engine. The sequential-look FRAME is ERROR.
- **Suggested fix:** give each man one object of attention and a reaction, with no sequence. For l.37, something like "He looked at my trousers and kept his eyes on them." For l.271, keep "in a way I understood without any Greek at all" but attach it to a single look. Optionally thin l.291 to one or two items.
- **Cascade:** none in plot. The item-by-item form stays closed. Any garment noticed later (the himation in Ch.7) must not be staged as a look that moves from item to item.

---

## WARNING ISSUES

### [W-01] The taxi's direction is reversed (CH5-5)
- **Evidence:**
  - chapter-3.md:7 the driver "had taken the road out of his village and up across the high plain" (from Arachova, up and across, to the trailhead).
  - chapter-5.md:5 "The morning before, a taxi had carried me across this plain on asphalt, east toward Arachova and over the lip and down."
- **Problem:** read literally, the taxi carried her east to Arachova and down, which is the opposite of Ch.3. She is retracing the route in reverse ("I set off east after it"), but the sentence gives the taxi her direction.
- **Fix:** for example, "had carried me the other way across this plain, up from Arachova over the lip." Then she sets off east "back along it."
- **Cascade:** none.

### [W-02] "loved" in Mara's narration, the first use in the book
- **Evidence:** chapter-5.md:143 "I had stood among them and loved it with my whole chest." (grep: no "love/loved" anywhere in Mara's narration in Ch.1–4.)
- **Rule:** foundation §3 and the bible's Mara card: "the word *love* in her own narration until Part Two (first use no earlier than Ch.19, and rare after that)."
- **ERROR or INTENT:** ERROR. The object is the ruin, not a person, but the evasion is lexical, and Ch.1–4 kept it perfectly.
- **Fix:** keep the feeling and lose the word. For example, "and been glad of it with my whole chest," or "and it had filled my whole chest." The anchor survives: the shame lands on "I preferred it dead" (l.149).

### [W-03] Comprehension jumps without a hedge (information flow / world rule)
- **Evidence:**
  - Ch.4 established that the Phocian speech "slid straight past me, all but the case endings" (chapter-4.md:19).
  - Ch.5 manages the step up carefully at first: the press woman's "a great deal more, fast" (l.17), "That one I had whole" (l.25), the guide's speech "worn smooth… I found I could hold on to it whole" (l.59), the herald's slow voice (l.205), the procurer "without any Greek at all" (l.271).
  - Then, with no hedge, she follows the clay seller's run (l.243) and an overheard fast colloquial exchange between two men at a distance, quoted word for word, about a brother's wife and a hoof (l.249–267). The gallery and sieve exchanges are also rendered whole (l.373–407).
- **Problem:** plausible but unverified (Rule 8). One day after the goat-boy, the narration hands her rapid street banter verbatim. The bible also calls the herald "the first Greek Mara follows at book speed," and the guide precedes him.
- **Fix:** one clause before l.249, for example "I caught most of it, which was more than I had caught all day." Or cut the fountain exchange to the half she gets (the oxen and the hoof), and let the rest go past her.
- **Cascade:** the dialogue share is 20.3%. Prefer the hedge to a cut (N-01).

### [W-04] Which language are "No." / "Eggs. I can do eggs." / "Mine." in? (CH5-6)
- **Evidence:** the refusal is set at l.133–135 ("I put it away… 'Keep the coin,' I said, in English."). English is tagged at l.241, l.275, l.301–303 and l.329. Then untagged: l.345 "No.", l.349 "Eggs. I can do eggs.", l.359 "Mine.", and Kallia acts on "Mine." (l.361).
- **Problem:** if these lines are Greek, the planned all-or-nothing refusal ("won't speak it in front of Kallia for a month", foundation §3) breaks on its first night. If they are English, "Whose are you?" / "Mine." is an exchange Kallia cannot understand, and the reader will assume she did.
- **Fix:** keep them English and give Kallia one beat that shows she is reading tone, not words, after "Mine." For example, "She heard the word without the sense, and the tone without any trouble." Or tag "Mine" as English.
- **Cascade:** Ch.7's month of silence depends on this.

### [W-05] Walk-ons inspecting an object held up to the eye: 4 times in Ch.5 (a gesture class the gate does not count)
- **Evidence:**
  - The guide and the coin: l.117 "weighed it on his palm and read the capitals", l.119 "tried it between his back teeth", l.137 "bit the coin again". The last is also the same beat twice for one character, against voice-dna's "no character gets the same beat twice in a chapter".
  - The slave and the rod: l.189 "with the rod held up close to his eyes… turning it in his hand" (device-turning).
  - The herald and the tablet: l.209 "raised it at the full length of his arm and screwed his eyes at it, and brought it closer, and pushed it away again".
  - Kallia and the sieve: l.385 "looked it over front and back in the light".
  - Book-wide: chapter-3.md:47 the German "tipped the stone to the light"; chapter-4.md:125 the boy "tilted it and found his own face in it".
- **Problem:** each one is motivated, but together they make 4 in one chapter (the gesture gate's fail threshold for a class) and 6 in the book. It also risks bleeding Mara's inspecting axis ("Only Mara notices materials and joins") onto the cast.
- **Fix:** keep the herald, whose long sight is his own life, and Kallia, whose check on her labor is her axis. Cut the guide's second bite (l.137 "bit the coin again" → he simply tucks it away). Have the slave *show* the split without turning the rod up to his eyes.

### [W-06] Mara's thumbnail probe, 3 times in one chapter
- **Evidence:** l.93 "still sharp enough to catch my thumbnail"; l.109 "under my thumbnail it was soft and bright"; l.155 "coarse enough to feel under the ball of my thumb… I had my thumbnail at the edge of the flake". Also chapter-1.md:383 "with my thumbnail".
- **Problem:** touching surfaces is her axis, but voice-dna asks for a different gesture each time. Three thumbnails in 60 lines is a signature in the making.
- **Fix:** vary two of them: a fingertip, a knuckle, the edge of a coin, or the lead scored with a key.

### [W-07] The rummage by feel through the duffel, now in three consecutive chapters; the cassette's sock repeats Ch.2's words
- **Evidence:**
  - chapter-3.md:139 "groped in the bag under me… past the sock with the tape in it"
  - chapter-4.md:95 "My hands found the box by feel, under the sweater, beside the sock."
  - chapter-5.md:431 "My fingers went past the corners of the granola box and the cold body of the Pentax and found the sock, rolled tight, with its small flat weight in the toe, and under the sock the sweater"
  - chapter-2.md:137 "in a wool sock, rolled tight, in the toe of a hiking boot"
- **Problem:** the planned touch is INTENT (foundation §4f: Ch.5). But the form has become a device: a blind hand in the bag, an inventory of box, sock and sweater, in three chapters running. "Sock, rolled tight… in the toe" also echoes Ch.2, against voice-dna §3b.4 ("the same goes for the cassette… fresh words every time").
- **Fix:** keep the touch and change its staging. The sock could already be in her hand because she is using it for something (padding under her hip on the mat, say), or she could find it alone without a route past the other items. Drop "rolled tight" and "in the toe".
- **Cascade:** Ch.19 and Ch.35 touches must be staged in a third way, not by rummaging.

### [W-08] A condition report in the pressure aftermath (retired form)
- **Evidence:** l.195 "My right forearm had two raised stripes… My wrist was skinned… my knee had come through the denim. When I moved my shoulders the back of the fleece pulled… The watch was going". Second instance: l.311, the hands inventory ("a scar…, and the scratch…, and the smooth tight shine…. The only hard place…").
- **Rule:** voice-dna VOICE UNDER PRESSURE: "What it is NOT: a list, an inventory, a catalogue, a condition report". §3b.2 retires condition-reporting for everyone.
- **Problem:** l.195 is an injury-by-injury inventory immediately after the beating. l.311 serves the inspection beat and is acceptable alone; together they make the device twice in one chapter.
- **Fix:** fold l.195 into action. Let her find one injury as she does something (the fleece sticking when she sits, the watch at her ear) and let the rest go unsaid. Leave l.311.

### [W-09] "That one I had/heard whole": a comprehension construction across Ch.4–5 (3 uses)
- **Evidence:** chapter-4.md:167 "That one I heard whole."; chapter-5.md:25 "That one I had whole."; chapter-5.md:59 "I found I could hold on to it whole".
- **Problem:** this is a near-verbatim repeat across chapters (under the 4-gram gate), and a third variant in Ch.5. It is becoming her formula for "I understood".
- **Fix:** recast l.25, for example "That one came through." Recast l.59 without "whole".

### [W-10] "[color] going [color]": 3 uses book-wide (the replacement for the spent "[color] of [thing]")
- **Evidence:** chapter-3.md:173 "yellow going toward orange"; chapter-5.md:195 "red going purple"; chapter-5.md:319 "silver going gray".
- **Problem:** the "[color] of [thing]" shape is spent at 3, and this is its successor forming at the same rate.
- **Fix:** recast one of the Ch.5 pair. For example, "silver gone dull" (l.319), or l.195 "red, darkening".
- **Cascade:** add it to the bible's at-risk list at 3, spent.

### [W-11] The knowledge-provenance aside ("I knew X from [text or lab]"): 6 in Ch.5 and 3 in Ch.4
- **Evidence:** in Ch.5, l.17 "a word I knew from Aristophanes"; l.77 "I knew that blue from a few grains on a slide"; l.109 "I knew it as I knew the Gettysburg Address, and the five hundred were in Pausanias"; l.227 "the coins I had cleaned in the lab"; l.229 "I had read it in Josephus in a seminar"; l.341 "I knew the word. It was in Homer". In Ch.4, l.15 Theophrastus, l.19 "I knew those from my grammars", l.97 the Odyssey quote.
- **Problem:** every one is in character, but tagging each fact with its source is a device forming (citation as rhythm). Ch.5 alone has 6.
- **Fix:** cut the source from two or three of them and let the fact stand. Aristophanes (l.17) and Homer (l.341) are the most cuttable. Josephus (l.229) is the beat and stays.

### [W-12] The tag "said to the [non-listener]": 5 in Ch.5, after Ch.4's W-04 (cap 1 per chapter)
- **Evidence:** chapter-5.md:211 "he said to the tablet"; l.289 "she said to the dark"; l.363 "she said to the road ahead of her"; l.367 "I said to her back"; l.399 "she told the gallery". Ch.4: l.75 "to the goats", l.139 "I said to his back", l.155 "talked to the thorn".
- **Problem:** this is the tag the Ch.4 audit capped at one per chapter, and "I said to his back" / "I said to her back" is near-verbatim across chapters.
- **Fix:** keep one. "Boeotians," she said to the dark (l.289) is her own life and the best of them. Plain-tag or untag the others; l.367 can be "I said, in English" alone.

### [W-13] Walk-on laughter and the "laughed until [s]he had to [verb]" frame
- **Evidence:** chapter-3.md:7 "laughed until he had to wipe his eyes"; chapter-5.md:131 "laughed until she had to sit down on an empty statue base". Further laughs at Mara in Ch.5: l.137 (the guide), l.171 ("the others laughed"), l.277 (the procurer "laughed").
- **Problem:** the Ch.4 audit (W-07) registered "laughed until [result]" as spent and said Ch.5's laughter "must be staged differently". The guide's mimicry is staged well, with crowd and sound. The wool-seller re-uses the frame. Male walk-ons laughing at Mara now number about 7 book-wide.
- **Fix:** drop "laughed until" at l.131, for example "laughed so hard she sat down on an empty statue base". Cut one of the incidental laughs (l.171 or l.277), since the steps scene and the procurer work without them.
- **Cascade:** add "laughed until [result]" to the bible's at-risk list (2, spent). It was proposed in Ch.4 but never added.

### [W-14] The voice-bank sample-01 frame reused, and a candour-adjacent precision claim
- **Evidence:** chapter-5.md:147 "I thought, in English and in exactly those words, that it was ugly." Sample-01: "and I thought, with real shame, that it was ugly."
- **Rule:** voice-dna §6 ("No sentence, image or line from any sample may be reused"); bible at-risk ("any phrase in … a voice-bank sample: 0"). "In exactly those words" also leans toward the performed-candour family ("I want to be exact").
- **ERROR or INTENT:** "ugly" is the planned anchor (INTENT). The sentence frame is ERROR.
- **Fix:** make the verdict land differently. For example, "The word that came, in English, was *ugly*," and then the check of the pilgrims' faces.

### [W-15] The doubling cadence spreads to the walk-ons (registered as the goat-boy's alone)
- **Evidence:** l.11 "You salt them first! Salt!"; l.17 "'Two days,' she told him. 'Two days at Kirrha with the jars.'"; l.191 "Look at it… Look."; l.375–379 "My sieve." / "My good sieve, the fine one." Bible, goat-boy note: "The word-doubling cadence is HIS alone."
- **Problem:** four speakers in Ch.5 restart on a repeated word. Each is natural speech, but this was the one cadence registered to a single voice.
- **Fix:** undouble two of them, the press woman and the slave.

### [W-18] Anaphora triad (retired reflex)
- **Evidence:** l.243 "each one pressed out of the same mold with the same thumbprint on the same hip".
- **Fix:** break the third, for example "…out of the same mold, the potter's thumbprint on every hip."

### [W-19] The flashlight is unaccounted for while she gropes in the dark three times
- **Evidence:** l.3 "I felt my way along a wall"; l.423 "I found the mat with my feet… barked my hip"; l.431 the rummage by feel. The 1998 flashlight is in her kit (Ch.2:137, Ch.3 throughout) and is planned for Ch.15. Kallia takes the lamp away "because lamp oil was lamp oil" (l.419).
- **Problem:** a careful reader will ask why she does not use it.
- **Fix:** one clause giving a reason that is in character. She will not show a 1998 light in a stranger's house (the stronger reason in the storeroom), and she is saving the batteries (Ch.3:139's reason) in the sheepfold.

---

## NOTES

- **N-01 (ledger detail).** Dialogue is 20.3%, at the floor of the band, so any trim should come from narration. Median 17 is high gear. 12.8% of sentences run over 40 words, which is high but under metaphor_check's 18%. Semicolons 3.1/1k. Em-dashes 2 (l.173, l.211), both true interruptions.
- **N-02 (timeline).** Ch.5 covers the night after Ch.4 plus the following day into night, not "the same day as Ch.4's end". This is consistent: l.329 "yesterday", l.5 "the morning before", and Ch.4 N-10's request to account for the night (the sheepfold) is met. Two small things. The opening sentence and l.5 both say she walked an hour with no road (l.3, l.5), which is redundant. And "corner… corner" in one sentence (l.3).
- **N-03 (period: olive season).** The beating and pressing are in full swing in Boathoos, roughly September–October (l.9–31, l.229). The main ancient harvest and pressing ran from late autumn into winter. Early green-olive picking is defensible, and the vintage a month back (l.379, l.351) supports October. Optional: one word ("the early picking").
- **N-04 (period: the warden's dress).** "a white tunic with a purple stripe" (l.159) is a Roman rank marker (the clavus). A Delphic sanctuary official more plausibly shows his office by a wreath, a fillet or the staff alone. Optional.
- **N-05 (period: Castalia).** "five white ropes" from lion heads (l.279). The later rock-cut fountain's spout count is uncertain (it is often given as more). Lion-head spouts belong to the archaic road fountain. Low confidence; verify or leave the number out.
- **N-06 (1998 coin).** l.117–119: check whether the 1990s 100-drachma obverse carries a legend naming its portrait (Alexander). If it does, a guide who "read them perfectly well" would not ask "Who's this with the hair, some king from past the Istros?" Re-aim the joke if needed, for example by having him read the name and scoff.
- **N-07 (guide lore).** The Thasian boxer "threw every man" (l.79): Theagenes was a boxer and pankratiast, and "threw" is wrestling. The statue that killed a man stood on Thasos. "The Thessalians off their horses" (l.103) is unsourced. All of this is guide patter and acceptable as his error. The Kroton runner over an empty base is invented and works.
- **N-08 (herald).** The opening formula ("Hear, people of Delphi!"), the archon-dated decree, the sacrifice for the emperor's safety and victory, the procession from the council house, the householders' lamps and the citizens-only meat are all period-right.
- **N-09 (intra-chapter: the oxen).** The decree as quoted (l.211, l.217) gives no number, but the fountain man says "Four oxen, he says" (l.249). Either make it deliberate, a mishearing of "the fourth day", or put the number in the decree.
- **N-10 (reader wink, acceptable).** The herald's garble "the Emperor Titus Caesar Ouespasianos" (l.211) is diegetic and corrected at once. Readers who know 79 may feel it. Mara's narration takes nothing from it, so it is not foreshadowing. Flag it for the evaluator only.
- **N-11 (teeth and Chestnut Street).** The Dr. Pinsky paragraph (l.317–319, about 120 words) is more than the "glancing" Ch.5 touch the plan gives, so do not pre-spend Ch.7's full surfacing (no dentist or brush there). Philadelphia comparisons are gathering on one street: Wawa on Chestnut (4:91), Rite Aid on Chestnut (5:317), and Fenn's automat on Chestnut is planned (Ch.25). Re-site one.
- **N-12 (tour-guide risk).** The Way runs about 1,900 words. It is dramatized through a guide who is mocked, rivalled and wrong, which keeps it from being a tour. The Corcyraean bull legend (l.57) is the one passage Mara neither uses nor suffers beyond comprehension. A trim there would honor the Writer warning and also let the Way decelerate without lecturing.
- **N-13 (open threads).** The clay discs are emphasized twice and left unexplained (l.49 "I could not think what else they might be for"; l.199 bought): pay them off (Ch.7/9) or demote them to texture. The procurer and his unseen companion watch her walk to the spring (l.277). Her "No one" to Kallia's "Who saw you come down here?" (l.327–329) ignores them; that is emotional truth and fine, but the thread is open for Ch.6/7.
- **N-14 (near-misses, retired reflexes).** "I preferred it dead." (l.149) closes section 2 as a punch line. It is a personal verdict, not an aphorism, and is bible-capped at 1: acceptable. "Badly." (l.155) is a fragment in calm narration. Two paragraphs end on a negation (l.85 "…the man who was not there"; l.215 "…did not turn round"), within tolerance. "everybody" appears twice in five lines (l.143, l.147).
- **N-15 (Kallia's hands: PASS).** A different object every time (jar and lamp, garland, foot, jar mouth, lamp, lips, kerchief, door, sieve, doorway, blanket). The one repeat is "the flat of her hand" twice in 34 lines (l.337, l.371); vary one.
- **N-16 (second uses to watch; a third makes a device).**
  - The bystander startled by the Pentax shutter: 3:95–97 and 5:111.
  - The lichen-dating forensic beat: 3:179 and 5:93.
  - The duffel sliding off her shoulder before she kneels or crouches over a find: 3:123 and 5:91.
  - "fingernail" as a size: 3:49 and 5:155.
  - "tried it": 4:25 (simile, coin and lead) becomes literal at 5:119.
  - A child as the comparison: 4:73, 5:155, 5:335.
  - The comparison frame "the way [someone] [does something]": 1:7, 1:137, 4:9, 5:107, 5:287.
  - "without [verb]-ing": 4 in Ch.5 (l.71 and l.73 adjacent, l.139, l.187), about 12 in the book.
  - "look at the legs": spoken twice by two speakers (l.53, l.165), and "look at the" 3 times in speech (l.53, l.87, l.165), one short of the tic gate.
- **N-17 (the Seiko).** Struck by the rod (l.183) and still running (l.195, l.433), which Ch.6 needs. Listened to at the ear twice in one chapter (l.195, l.433). "luminous paint was long dead" restates Ch.3's dead dots in fresh words. Winding is not shown since Ch.3's morning, which fits the daily habit off the page (Ch.2:137).
- **N-18 (object ledger).**
  - **Coins:** "three coins… from the taxi" is a new, retroactive fact (Ch.3 shows no change given); one went to the guide, so two remain.
  - **Pentax:** one antiquity frame spent on the Kroton base (CH5-3; INTENT). Plan count: 9 exposed, 27 left including frame 36.
  - **Microcassette:** touched as planned (CH5-4: the 3rd contact on the page since packing).
  - **Knucklebone:** untouched (correct; its touch is spent).
  - **Not on the page:** notebook, map, lens cap, postcard and passport/wallet; their positions carry over. The Advil is not taken after a beating; rationing reads (Theano takes "the last two" in Ch.13), so a clause is optional.
  - **Hands:** described as "pink" twice (l.245, l.311).
- **N-19 (CH4-3).** Ch.5 says "fleece" six times and "jacket" never. Recommend that the tracker records one garment (a fleece jacket), with a one-word fix in Ch.3 at its next touch, or leave it.
- **N-20 (CH5-1).** The lodging is up the road and along a lane (l.361–395), while the foundation and bible say "by the Castalian spring". Amend those to "near".
- **N-21 (CH5-2, bible staleness).**
  - Kallia's line is "Who saw you come down here?", not "Who's coming after you?".
  - The sieve was "a month… to strain her must", not "since the vintage"; the vintage belongs to the runaway girl.
  - The slave's line is "they'll stop it out of my bread".
  - The clay seller says "Since the bronzes were carted off", not "Since the singer". Keep it that way: "the singer" stays at 2.
  - The herald is not "the first Greek Mara follows at book speed"; the guide comes first (l.59).
  - "Comes to the spring because the lodging is out of water" is not on the page.
- **N-22 (Ch.6 handoff, cascade).**
  - Ch.5 fixes a concrete plan, "In the morning I would go back up" (l.283, l.433), and a feast "on the fourth day" (l.211).
  - Ch.6 (November, snow, Valens at the lodging) must account for that plan not being carried out, or for a failed attempt alone.
  - "the cart track by full light" (l.433): in Ch.5, "track" names the two-rut track at the lip above Arachova (l.5), about 10 km from Delphi. Reaching the cave "by the middle of the day" is tight but feasible.
- **N-23 (CH3-7).** Resolve as "prose wins". She has the span and the plan, and not naming a door is in character.
- **N-24 (P5).** The Corinth post reaches Delphi "with the ship" in weeks (l.203, l.229). So the Ch.9 reward notice (from autumn 70, seen in spring 71) needs its own reason for arriving late. This is an outline fix, not Ch.5's.
- **N-25 (foreshadowing / canon).**
  - Zero. No 79, Pompeii, Vesuvius or "nine years". The only "Italy" is the guide's guess about her origin (l.53).
  - "I had told Gloria the ninth of June." (l.233) faces backward and matches Ch.2:133.
  - Future plans are present intentions. No narrating present.
  - Canon holds: AD 70 under Vespasian, and a woman alone has no status.

---

## SUGGESTED YAML PATCHES (for the entity-tracker UPDATE after the editor's fixes)

```yaml
suggested_patches:
  - entity: "contradictions.CH3-7"
    action: "remove_conflict"
    reason: "Ch.5 gives her the year and the 1,928-year span (ch-05 l.229-231) and a plan to return to the crack (l.283); not naming a 'door' is in character. Prose wins."
  - entity: "contradictions.CH5-3"
    action: "remove_conflict"
    reason: "INTENT: an on-page antiquity frame (the Kroton base). Plan count 9 exposed / 27 left incl. frame 36; record frames_shot_ch5: 1."
  - entity: "contradictions.CH5-4"
    action: "remove_conflict"
    reason: "planned touch delivered; record it as the 3rd on-page contact since packing; staging drift is tracked as audit W-07, not as a fact conflict."
  - entity: "contradictions.CH5-5"
    action: "keep_original"
    reason: "Ch.3 l.7 is canonical (taxi up from Arachova). Ch.5 l.5 to be reworded by the editor (W-01); remove the conflict after the fix."
  - entity: "contradictions.CH5-6"
    action: "update"
    value: { decision_pending: "editor W-04: replies to Kallia are English; Kallia reads tone" }
    reason: "the all-or-nothing refusal (month-long, Ch.7) depends on it."
  - entity: "contradictions.CH5-2"
    action: "update"
    reason: "character-bible Ch.5 notes to be corrected to the prose (N-21), then remove_conflict."
  - entity: "mara-reyes.possessions.coins"
    action: "create"
    value: { item: "three 1998 Greek coins (taxi change) in her jeans pocket; the largest, a 100-drachma piece (brass, a young man's head in profile), given to the guide; two remain", source: "ch-05 l.117-137" }
  - entity: "mara-reyes.knowledge"
    action: "add"
    value:
      - { fact: "Nero is dead ('the singer'); so it is at least AD 68", learned: "ch-05 l.107-109", method: "inferred (told_by:guide + prior_knowledge)" }
      - { fact: "the year is autumn AD 70; Vespasian is emperor; Titus has taken Jerusalem", learned: "ch-05 l.207-229", method: "inferred (herald + prior_knowledge)" }
      - { fact: "1998 less 70 = 1,928 years", learned: "ch-05 l.231", method: "inferred" }
      - { fact: "the woman at the spring is called Kallia", learned: "ch-05 l.397-409", method: "overheard" }
    reason: "nothing of Pompeii, Italy as destination, or a door home"
  - entity: "character-bible.at-risk"
    action: "add"
    value: ["item-by-item look: SPENT (Ch.5 l.37, l.271 to be fixed)", "'[color] going [color]': 3, SPENT", "'laughed until [result]': 2, SPENT", "'That one I had/heard whole': spent", "'said to the [non-listener]': cap 1 per chapter (Ch.5 had 5)", "duffel rummage by feel: spent (Ch.3-5)", "thumbnail probe: max 1 per chapter", "knowledge-provenance aside ('I knew X from [text]'): max 2 per chapter", "walk-on object-to-the-eye inspection: max 2 per chapter", "Chestnut Street as comparison anchor: 2, re-site the next"]
  - entity: "timeline[chapter=5]"
    action: "update"
    value: { time: "night after Ch.4 (sheepfold on the plain) → next day: plain, Arachova village, olive press, Delphi by afternoon, beating late afternoon, herald, dusk, Castalia after dark, Kallia's storeroom; autumn AD 70 (Boathoos); feast decreed for the 4th day after", source: "ch-05 l.3-433" }
  - entity: "threads"
    action: "add"
    value:
      - { thread: "the pierced clay discs sold in the agora", opened: "ch-05 l.49, l.199", status: "OPEN (texture or payoff)" }
      - { thread: "the procurer and his companion watched her walk toward the spring", opened: "ch-05 l.269-277", status: "OPEN" }
      - { thread: "Mara's plan to return to the crack 'in the morning'", opened: "ch-05 l.283, l.433", status: "OPEN → Ch.6 must account" }
```

---

## Bottom line

Ch.5 delivers the plan. The walk changes as the road does; the painted temple is ugly to her and she is ashamed of it; the empty bases are her first wonder; she dates the year from Josephus and her fingers, with no leap to 79; and Kallia arrives exactly to her card. The period detail is unusually accurate, and the beating's voice deflates correctly.

**Fix before finalize:**
- **C-01:** the item-by-item look, l.37 and l.271.

**Should fix (one clause or one word each):**
- W-01, taxi direction
- W-02, "loved"
- W-03, a comprehension hedge
- W-04, the language of "Mine."
- W-14, the sample-01 frame
- W-19, the flashlight

**Drift to thin (the gates do not see it):**
- Walk-on object inspection ×4 (W-05)
- Thumbnail ×3 (W-06)
- The rummage in three chapters and "rolled tight" (W-07)
- The injury inventory (W-08)
- "I had/heard whole" (W-09)
- "[color] going [color]" (W-10)
- Source citations ×6 (W-11)
- "said to the [thing]" ×5 (W-12)
- "laughed until" (W-13)
- Walk-on doubling (W-15)
- "the same… the same… the same" (W-18)
