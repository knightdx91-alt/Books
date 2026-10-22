# Continuity Audit: Chapter 21 (run 2, per-chapter drift audit)

**Date:** 2026-10-22
**Mode:** MANUSCRIPT AUDIT. Ch.21 "The Wolf's Old Name" (post-dialogue-polish, hook-craft and disruptor; 7,075 prose words by `wc` with the comments stripped) is checked against:
- Ch.1–20 as they stand on disk (targeted greps; Ch.11, 12, 16, 17, 19 and 20 read at the relevant passages);
- ENTITY_STATE.yaml as of Ch.20 (read only; the parallel Ch.21 UPDATE was not touched);
- outline.md (Ch.21 and its ledger row; Ch.22, 28, 30 and 31 for forward collisions);
- foundation.md (§3 Valens's mind-reading of Grata, Felix's palm-branch; §10 timeline, Felix ~21 at the eruption);
- voice-dna.md (§0 families A–E, §1 dialogue conventions and anti-patterns, the weight carriers);
- character-bible.md (the Valens, Felix, Grata, Plautia, Nicanor and Fabius cards; the Ch.21 walk-on block; the At-risk registries after Ch.5 through Ch.20, the at-risk phrase table);
- STATE.yaml guardrails and resolved_author_decisions (CP3-3, CP3-5, CP4-1, CP4-2, END-1).

**Citations:** `l.NN` is the line in `manuscript/chapters/chapter-21.md`. Other chapters are cited as `ChN l.NN`.

**Mechanical baseline (read only):**
- `tic_report.py --gate --file chapter-21.md`: **clean**. And-chains 6 (cap 9); credential asides 0; negation pivots 1 (cap 1); gesture classes under cap.
- `tic_report.py --echoes 21`: 58 advisory 3-gram echoes; **0 command echoes; 0 spoken-line echoes**. The detector misses several things this audit found by hand (C-01, C-02, C-03, W-01, W-05).
- Dialogue share is **40.0–40.1%, exactly on the ledger floor**. Every fix below that cuts speech is offset by larger narration cuts; the net estimate after the ledger is about 40.4%. Re-measure after the repair.

**Total findings: 34. CRITICAL: 4 | WARN: 19 | INFO: 11**

---

## Summary

The chapter meets the outline:
- **Beat 1 (summons):** on the page, by the AUTHOR-CP4-2 route (the Puteoli board, fetched by the lime carter of Ch.20 l.259), not the outline's "freedman at Grata's counter". The knowledge path is clean.
- **Beats 2–3:** Nicanor recognises Valens, the LVPVS graffiti appear, the editor makes his offer, Felix's face changes, and Valens refuses flatly ("No," l.268) while staying undecided about Rome.
- **Beats 4–5:** Mara argues "speak and be believed", Valens argues for being nobody and the child's safety, and the chapter closes on an open question (l.530).
- **The anchor:** Felix's palm scratched by the barracks gate.
- **The emotional surprise:** the hand that rises, then gets scrubbed.
- **Mind-reading:** Valens reads Grata's flirting as hostility.
- **Guards held:** the pregnancy telling is Mara's and comes early (Ch.20 audit I-10). Felix still believes Valens cannot read. There is no tomb, painted door, "seam", "niche", "painted plaster" or "hand flat" on the page. There is no mountain and no AD 79. The children's status is untouched (CP4-1). Foreshadowing families A–E are clean (see I-08). No arena fight is set up for Valens.

**The four CRITICALs:**
- Three are registry violations: devices the bible has CLOSED or SPENT.
- One is a physical contradiction inside the anchor scene (the wreath).

Each CRITICAL has a fix of a few words.

**The WARNs fall into four groups:**
- **Cross-chapter rebuilds.** The recognition beat rebuilds Ch.12's opener and Ch.17's trainer. The laugh rebuilds Ch.14's. The worn stair step is used a 4th time. Grata's hand "where his shoulder had been" mirrors Ch.19.
- **Canon friction.** "Nero freed with his own hand" against Valens's own account in Ch.12. A second "Gaul" from the Corinth school. "Cenchreae" against the book's "Kenchreai". The brother's letter has no sender's name. The earnest money halves while the offer rises. "The street climbed" against Ch.19's "straight on down". The Parilia offer is left dangling.
- **Devices forming in-chapter.** Felix's silence marked by "asked nothing" (×2 here, 4 book-wide). Valens deflecting by the Ides (×3). Spoken "Then…" openers ×3 (cap 2). "Somebody had [verb]" ×2 (cap 1). Narrated non-answers ×2. A said-to-the-[thing]. "and then" ×15.
- **Smaller items.** A borrowed Ch.19 line ("Some do."), a two-paragraph speaker run that misreads, and an oblique self-opening door in the hospital memory.

---

## CRITICAL ISSUES (fix before the evaluator runs)

### [C-01] "at a run" — CLOSED at 2 (Ch.10, Ch.13)
- **Audit:** NO TICS / closed-device registry. Bible At-risk after Ch.13: "**"at a run": 2 book-wide (Ch.10, Ch.13), CLOSED.**"
- **Evidence:**
  - Ch.10 l.140: "Somebody came in at the gate at a run."
  - Ch.13 l.86: "the boy went at a run."
  - **l.26:** "He was gone at a run, and back for the second nosebag…"
- **Fix (−3):** "He was gone at a run," → "He was gone,"
- **Cascade:** none. "and ran again" still closes the sentence.

### [C-02] A third (and fourth) "whose" question — SPENT at 2
- **Audit:** at-risk phrase table: "Whose are you?" / "Whose is she?" are capped at 2 (Ch.5, SPENT): "A third 'whose' question would make it a refrain." Ch.17 l.494 ("Whose school?") already went past the cap.
- **Evidence:**
  - **l.282** (Nicanor): "Whose is he?"
  - **l.430** (Valens, ventriloquising the advocate): "Who is the witness's wife. Whose daughter."
- **Fix (±0):**
  - l.282: "Whose is he?" → "Is he yours?" Valens's "His own. I freed him." still answers it.
  - l.430: "Whose daughter." → "Who her father was."
- **Cascade:**
  - Nicanor's card "Ch.21 as written" quotes "Whose is he?". The bible sync must update it.
  - The registry entry becomes: "whose": 3 on the page (Ch.5 ×2, Ch.17), CLOSED.

### [C-03] The gaze-holding frame "kept [poss] eyes on the [X]" — CLOSED
- **Audit:** bible At-risk after Ch.14: "**The gaze-holding frame "kept [poss] eyes on the [X]": CLOSED** (Ch.7, Ch.8, Ch.13, Ch.12)", restated after Ch.16 ("`kept [poss] (eyes|face|gaze)`: inside the CLOSED gaze-hold").
- **Evidence:** **l.290:** "Valens walked past it with the string. He kept his eyes on the road. Then, three paces on, he turned them."
- **Fix (−6):** "Valens walked past it with the string. Three paces on, he looked back."
- **Cascade:** this also removes a "Then," hinge opener. "The fish faces the wrong way" (l.292) still follows.

### [C-04] The wreath is lifted off whole, then goes "into shadow" with the palm
- **Audit:** objects and physical continuity, inside the anchor scene that closes the chapter.
- **Evidence:**
  - **l.526:** "Valens set his thumbnail to the wreath where its two ends met, pressed, and lifted it off with the wreath whole."
  - **l.530:** "The palm went into shadow, and the wreath, and the name."
- **Problem 1: the contradiction.** If the flake came off whole, the wreath is no longer on the gatepost to go into shadow. The "it" in "lifted it off" also has no antecedent: is it the flake, or the name?
- **Problem 2: a spent probe.** A thumbnail pressed into plaster is Ch.19's probe, SPENT ("the thumbnail probe is Ch.19's one", At-risk after Ch.19). It comes two paragraphs after Mara's fingertip in the palm's stroke (l.512).
- **Fix (≈ −3):**
  - l.526: "Valens set the point of his knife where the wreath's two ends met and lifted the wreath off whole."
  - l.530: "The palm went into shadow, and the wreath, and the name." → "The palm went into shadow, and the name."
- **Cascade:** tool-tip frames become 2 (with l.82), which is at the cap of ≤2 per chapter.

---

## WARNING ISSUES (should fix)

### [W-01] The recognition beat rebuilds Ch.12's opener and Ch.17's trainer
- **Audit:** cross-chapter rebuild. The registry allows a 4th stranger-reads-Valens beat here ("WATCH at 3 … none before Ch.21's trainer"), so the beat itself is planned. Its sub-beats, though, are lifted from Ch.12 and Ch.17:
  - **The man:** Ch.12 l.8, "short and sunburned … a pleasant, creased face"; **l.176**, "A short bald man … brown and creased".
  - **The followers he has already told:** Ch.12 l.18, "These two never saw you fight. I told them about it the whole crossing."; **l.200**, "The murmillo I told you of".
  - **The mule quip and Valens's mule deflection:** Ch.12 l.6, "Lupus, walking behind mules."; Ch.17 l.496–498, "I lead mules." / "Mules!"; **l.200**, "Mules, is it?" and **l.206**, "I drive mules," Valens said. This is a near-verbatim reply in the same mouth.
  - **Nicanor says "Lupus" twice** (l.194, l.200). His card's bleed guard reads "he says it once, as a name".
- **Fix (≈ −11):**
  - l.176: "He was brown and creased, in a good cloak," → "He was bandy-legged, in a good cloak,"
  - l.200: cut "Mules, is it?"
  - l.200: "This is Lupus. The murmillo I told you of, that Nero freed with his own hand." → "This is him. The murmillo Nero freed." This also clears W-02.
  - l.206: "I drive mules," → "I rake sand,". Nicanor's "So you do." still answers it.
- **Cascade:** Nicanor's card quotes the old line; sync it.

### [W-02] "Nero freed with his own hand" against Valens's own account
- **Audit:** canon. In Ch.12 l.180 Valens says: "The emperor never got out of his chair. I put the Gaul down, and he sent the sword out to me across the sand". Nicanor was there, so he would know. The herald's "from the hand of Caesar himself" (l.228) is a herald's puff and can stay.
- **Fix:** fixed by W-01's l.200 recast.

### [W-03] A second "Gaul" from Valens's Corinth, and the Gaul + Patrae pairing again
- **Evidence:**
  - **l.194:** "with the Gaul that had no wind and the boy from Patrae that cried"
  - Ch.12 l.16 and l.180: the Gaul is the opponent of the freedom bout.
  - Ch.16 l.316: "a lanista from Patrae and a Gaul that's killed four".
- **Problem:** a reader will take Nicanor's Gaul for the man Valens "put down".
- **Fix (±0):** "the Gaul that had no wind and the boy from Patrae that cried" → "the Syrian that had no wind and the boy from Argos that cried".

### [W-04] "Cenchreae" against the book's "Kenchreai"
- **Evidence:** l.200 and l.274 have "Cenchreae". Ch.12 l.188 and Ch.17 l.232 have "Kenchreai". The book keeps Greek port names even in Latin speech (it uses "Lechaion" throughout, including Valens's Latin in Ch.20 l.257).
- **Fix (±0):** "Cenchreae" → "Kenchreai" at l.200 and l.274.

### [W-05] Valens's "Some do." is a borrowed line (Ch.19 l.335, same mouth)
- **Audit:** At-risk after Ch.20: "A 1–2-word whole line in the same mouth across chapters: 0; it is a borrowed line." The Ch.19 spoken-shapes list names "Some do," as SPENT.
- **Evidence:** **l.392:** "Some do." He did not raise his voice; he never did.
- **Fix (−2, dialogue):** cut `"Some do."`. The paragraph then opens "He did not raise his voice; he never did. "A child's coming. …"

### [W-06] The laugh rebuilds Ch.14 and pre-spends Ch.22's emotional surprise
- **Evidence:**
  - **l.90:** "I had my fingers to my mouth and the laughing went on through them, and my eyes ran"
  - Ch.14 l.62: "I put my wrist across my mouth and it came round the sides anyway"
  - Ch.15 l.548: the helpless laugh.
  - The outline makes Ch.22's surprise "Mara's uncontrollable laughter".
- **Fix (−17):** l.90 → "That was when I began to laugh, and he waited at the hearth with oak shavings in his hair and looked at me until I was done."

### [W-07] Felix's silence marked by "asking nothing": ×2 here, 4 book-wide
- **Evidence:**
  - Ch.12 l.318: "he asked nothing whatever"
  - Ch.13 l.124: "asked nothing more"
  - **l.88:** "went to his blanket with no question about the noise; he had stopped asking, that season, about anything Valens did with wood"
  - **l.296:** "and he asked not one thing."
  - l.204 ("Felix slid down, wordless.") adds a third Felix-silence beat to this chapter.
- **Problem:** the asker falling silent is becoming his device.
- **Fix (−17):** l.88 → "Felix let himself in from the stalls and went to his blanket." Keep l.296. It closes the section and is the one earned use.

### [W-08] Valens deflects by the Ides three times, plus a deliberation pause
- **Evidence:**
  - l.128: "The Ides is far enough."
  - **l.434–438:** "Then his mouth began a word and gave it up." / "The Ides is three months off," he said. / "Less."
  - l.530: "I can count to the Ides."
- **Fix (−17, of which 6 are dialogue):** cut l.434–438 entirely. l.432 ("…and he let it lie.") runs straight into l.440 ("He lay back and closed his eyes.").
- **Cascade:**
  - The deliberation-pause count for the chapter drops to 0.
  - "Ides" in Valens's mouth drops to 2.

### [W-09] Two Valens narrated non-answers (cap ≤1), and "The street climbed" contradicts Ch.19
- **Evidence:**
  - **l.470:** "He did not answer that. The street climbed, and the high back wall of the big theater rose dark ahead."
  - l.530: "and he did neither of those things".
  - Ch.19 l.247: Grata's route from the fountain is "Left at the fountain … and straight on down till you've the gate in front of you".
  - Ch.19 l.253: "down that street as far as it goes".
  - l.14: Felix cuts behind the theater "to save the hill".
- **Problem:** going left at the fountain for the theaters is downhill, so the street cannot climb.
- **Fix (−5):** l.470 → "The street fell away, and the high back wall of the big theater rose dark ahead."

### [W-10] Spoken "Then…" openers: 3 (WATCH cap ≤2)
- **Evidence:**
  - l.286 (Nicanor): "Then I'll not need to ask you."
  - **l.498** (Valens): "Then send him off again."
  - l.524 (Valens): "Then he'd know…"
- **Fix (−1):** l.498 → "Send him off again."

### [W-11] "[S]omebody had [verb]" inference sentences: 2 (cap ≤1, At-risk after Ch.17)
- **Evidence:**
  - l.288: "somebody had already worked on the pier with a nail."
  - **l.526:** "somebody had scratched LVPVS again"
- **Fix (±0):** l.526: "…on his toes, somebody had scratched LVPVS again, smaller this time…" → "…on his toes, LVPVS showed again, smaller this time…"

### [W-12] Said-to-the-[non-listener]
- **Evidence:** **l.430:** "And they'll ask about you." He said it to the burn.
- **Context:** this is the gated family (Ch.5's "said to the [thing]" ×5; counted in every chapter since Ch.17). The rope burn is already Valens's maintenance object at l.350 and l.374.
- **Fix (−5):** cut "He said it to the burn."

### [W-13] Speaker runs that misread
- **l.400–402:** "The door was sticking." / "There's always a way out. I find it first."
  - The two lines are consecutive Valens paragraphs. By alternation the second reads as Mara's.
  - **Fix (±0):** merge them into one paragraph: "The door was sticking. There's always a way out. I find it first."
- **l.378–382:** Valens: "I saw you see it…" / "I saw." / "Nobody at the Basilica," I said…
  - The untagged "I saw." makes two Mara paragraphs in a row and echoes "I saw you see it".
  - **Fix (−2, dialogue):** cut l.380.

### [W-14] The hospital's self-opening doors
- **Evidence:** **l.132:** "…and the doors at the end of the corridor that opened by themselves when you stepped on the black mat in front of them. I had stood on that mat twice to watch them do it."
- **Problem:** this is a door that opens by itself, at the end of a corridor, in the first night of the pregnancy. It invites a symbolic read against the time-door, which has no page presence before Ch.30 (CP4-2 and AUTHOR-END-1 guards). Under voice-dna §0 any line that does a forward job is out, whether or not the gate's words are in it.
- **Fix (−30):** end the sentence at "…of its smell of floor wax and lilies." and cut the mat sentence.

### [W-15] Grata's husband and the dice: the Ch.19 joke again
- **Evidence:**
  - **l.328:** "My husband's never lifted anything heavier than a dice cup."
  - The Ch.19 spent list has "the dice joke" ("If you hear dice, that's him…").
  - The dice debts are Ch.31's (outline beat 1).
- **Fix (±0):** "a dice cup" → "a wine cup".

### [W-16] Grata's hand "where his shoulder had been" mirrors Ch.19's plant
- **Evidence:**
  - Ch.19 l.243: Valens "looked at the place on his sleeve where her hand had been"
  - **l.342:** "she stood with her hand up where his shoulder had been."
- **Problem:** the same frame in reverse. The payoff is already in the shoulder-brush.
- **Fix (−4):** "…she stood with her hand still up."

### [W-17] The worn stair step and the thumb in its hollow, a 4th time
- **Evidence:**
  - Ch.17 l.194: "The step down had a hollow worn in it."
  - Ch.20 l.107: "the top tread, where the wood's worn hollow"
  - Ch.20 l.529 and l.539: Zosimus's stone step "gone hollow in the middle", found "with my thumb"
  - **l.76:** "pressing his thumb into the hollow worn in the tread's middle"
  - l.88: "hollowed to the depth of my finger"
- **What to keep:** the tread itself is the right payoff of Ch.20 l.107.
- **Fix (−3):** l.76 → "pressing his thumb into the middle of the tread."

### [W-18] "and then": ×15 (book's previous high 11, in Ch.19; Ch.20 had 3)
- **Evidence:** eight are in narration: l.88, l.222 ×3, l.232 ×2, l.300, l.332.
- **Fix (−4):**
  - l.222: "wheezed and then caught" → "wheezed and caught"
  - l.222: "looked round at his friends, and then lifted his hand" → "looked round at his friends and lifted his hand"
  - l.232: "turned, and then those behind them" → "turned, then those behind them"
  - l.332: "and then the far shoulder" → "and the far shoulder"

### [W-19] Two open details in the Fabius offer
- **The Parilia offer is left dangling.**
  - Evidence: **l.324:** "My master can wait for him until the Parilia."
  - Problem: the 21st of April falls during the Rome trip, and nothing in Ch.22–28 closes it. Ch.28 forbids setting up a bout for Valens, and a dated offer is a setup. Nicanor's "I said you'd lost your wind" (l.500) already closes Fabius's pursuit.
  - Fix (−9, dialogue): cut the sentence.
- **The earnest halves as the offer rises.**
  - Evidence: at the gate the offer is "Two thousand sesterces … half of it now" (l.266). On the plank it is "three thousand … Five hundred there, for earnest" (l.310), and l.312 calls that purse "more than the contractor would pay Valens between one vintage and the next".
  - Problem: 500 HS is under two years of Grata's rent (24 HS a month, Ch.19 l.237), so the year's-pay claim strains.
  - Fix (±0): "Five hundred there" → "Fifteen hundred there".
- **Plautia's brother's letter has no sender's name.**
  - Evidence: **l.108:** "*Plautia's brother, to Gaius Iulius Valens, greeting.*" A Roman letter opens on the sender's name.
  - Fix (−1): "*Sextus Plautius to Gaius Iulius Valens, greeting.*" Plautia is "daughter of Sextus" (Ch.17), and l.116 ("Her brother wants me") identifies him without a gloss.
  - Cascade: a card stub for the brother in the bible (named in Ch.21, by letter only).

---

## INFO (polish, history notes, handoffs)

### [I-01] History and world rules: PASS
- **The amphitheater** is consistent with Pompeii. The Large Palaestra and vineyard lane (l.164). The long north passage under the seats. Women in the top ring "the law said so" (l.218; Suetonius, *Aug.* 44). A podium painted with hunts. A water organ. A morning *venatio* and afternoon pairs. Awnings "if the sun's out" (the real *vela erunt*). *Missio* by the raised finger. The palm and the thrown purse.
- **The barracks** are the quadriporticus behind the theaters, converted after the AD 62 quake (l.472). This matches Ch.20 l.27 ("live behind the theaters").
- **The summons** has period-true legal texture: "The praetor has given us our day and our judge" (formulary procedure), and the April hearing in the Basilica Julia fits Ch.16 l.570 ("two years from this spring" = spring 74).
- **Other period details:** the fan graffito (fish-crested helmet, LVPVS) is a new wall kind, so the Ch.20 wall-set guard holds. Sesterces, Falernian as a gift, the white toga under the tribunal awning (a candidate's *toga candida*), and a Saturnalia *munus* are all plausible.

### [I-02] Timeline: PASS
- **The opening:** "Twenty-six days" before the Saturnalia (17 Dec), so the chapter opens about 21 Nov AD 73, the morning after Grata's reveal. That keeps the Ch.20 reveal out of December (Ch.20 audit I-02).
- **The pregnancy:** about seven weeks at the opening. Conception about October is consistent with "with the heat" (l.72), Lucius born summer 74, and "six months pregnant" in spring 74 (Ch.23). No line notices any earlier gap (CP3-3).
- **The show and after:** the show is about 17 Dec. The freedman's visit and the argument are about 18–19 Dec. "The Ides is three months off" / "Less." is correct for that date (cut under W-08 in any case).
- **S4:** "the last month of the winter" (February AD 74), before the freedman's window opens on the Kalends of March. This hands cleanly to Ch.22 (Rome, April).
- **Felix's age:** "twelve, at Kirrha" (c. AD 70; bible), "Fifteen, then. Sixteen." in winter 73–74, and "four years" (l.524) are consistent with the foundation (~21 at the eruption) and outline Ch.28 (eighteen in AD 76).
- **Optional (±0):**
  - l.444 "three mornings running … On the fourth" against Nicanor's "Three days he's sat on my step" (l.496): "three mornings running" → "two mornings running", and "On the fourth" → "On the third".
  - l.80 "In the summer." (Felix's slip was the summer of 72, Ch.20 l.103) → "The summer we came."

### [I-03] Information flow: PASS (table below)
- **Nicanor** knows "Lupus" first-hand (he trained him at Corinth). **Fabius** gets it from Nicanor's three "at the oil" (l.212). **The bowl** gets it from the herald and Felix's pointing arm. **The street and Grata** have it from the benches and the baths (l.302, l.332).
- **The freedman** finds the shop because the rim voices place Valens ("Him that lodges at Grata's", l.238). He reads Mara's board (l.304).
- **The pregnancy** travels by gossip: Grata → the fish carter (Ch.20) → the carter's friends (l.30) → the baker's boy → Felix (l.138), and also to the grandmother ("Grata says the heat", l.246). Grata's "I've told nobody" (l.34) holds, because the carter overheard her own reveal.
- **Mara** knows nothing she should not:
  - Valens told Celer "Rome" with Mara present: Ch.17 l.370 and l.424.
  - Valens promised Plautia to stand up: Ch.16 l.572.
  - The first-night gate question: Ch.19 l.251.
  - Felix believes Valens cannot read: Ch.11 l.444–448.
  - Felix has no papers: Ch.11 l.476–488.
- **Felix has heard "Lupus" before.** He was on the road in Ch.12, and he had the sword's story at second hand in Ch.16 l.316. His stillness at l.196 reads as scale, not news. That is acceptable.
- **Plautia's brother's Latin** is poor (Ch.17 l.438), but a scribe writes the letter and Plautia's note is in her own hand. This is consistent.

### [I-04] Objects: PASS
- **Wrists:** the watch and the bracelet are not on the page (still right and left wrist).
- **The leaf:** not on the page (Valens holds it, Ch.19 l.93). The summons does not ask for it, so Ch.22 must bring it.
- **The summons tablet:** sealed, read behind the curtain, "on the shelf above the bed, by the oil jar".
- **Objects paid off in-chapter:** the spice-seller's scales (fetched "early"), the comb, the old tread (burned) and the new oak tread.
- **Open thread:** Felix's promised murmillo bowl for the child (l.142).
- **Layout:** "our curtain" (l.104, l.412) is the first curtain on the page. Ch.19 l.245 and l.265 give a barred plank door between the back rooms. Accept, or let one later clause hang it.
- **Optional (±0):** l.398 "tried the bar on that door, twice" → "tried that door twice". In Ch.19 the bar was set once and the door was closed twice.

### [I-05] Reserved-word guard, CP4-1, Ch.31 guard: PASS
- **Reserved words:** seam / niche / painted plaster / hand flat / tomb are 0 / 0 / 0 / 0 / 0. "door" appears only as house doors. Mara's fingertip in the scratched plaster at l.512 is a gatepost, not a threshold, so it can stay.
- **Children (CP4-1):** no word of citizenship or status. The advocate's questions are about Mara.
- **Ch.31 guard:** Ch.31 is not pre-spent. The show-painter is "up a ladder" by day, in Felix's report only. No household hand holds a ladder or a light, and there is no lamp on a pole.

### [I-06] Handoff to Ch.22 ("the nine")
- **The collision:** "nine" here means the fights, three times (l.200, l.228, l.320), plus the freedman's "when I was nine" (l.316). Ch.22's outline says "the living witnesses among the nine". Ch.22 must name the leaf's witnesses as "the witnesses" or "the names on the leaf", never "the nine".
- **Optional (−1):** l.316 "when I was nine" → "when I was small".
- **Nicanor as a witness:** he knew Valens at the school, so a reader may ask why he is not a witness against Celer's backdated sale. Ch.22 forbids a surprise witness. Leave him out, and do not have anyone raise him.
- **Ch.22's "he chose to come":** the chapter ends undecided, and Ch.22 shows the choice by result.

### [I-07] Handoff to Ch.28
- **Pre-staged backfill:** S4 already stages "Felix missing → Valens finds him at the barracks gate at night". Outline Ch.28 beat 2's backfill ("Felix vanished. Valens found him at the barracks, sworn") must be staged another way, for example word from Nicanor or Felix telling them at supper.
- **Nicanor's role:** Ch.21 implies the decision is Nicanor's ("Nobody can stop him but Nicanor", "I'll take him"). Ch.28 lists a separate "Lanista". The outline or bible should decide whether Nicanor is the lanista or the lanista's trainer.
- **The palm "under the seats"** in Ch.28 must be worded fresh: no nail and no doubled-cut stem.
- **Felix's palm habit:** foundation §3 says he scratches one "on every wall he leans against". It begins here.

### [I-08] Foreshadowing read (families A–E): CLEAN
- In-scene predictions (Nicanor l.212, l.504) and Valens's closing question about the grown child (l.530) are character speech about the near future.
- **l.312:** "and the child would come in the summer" is Mara's expectation of a due season in the scene, not narrator reach.
  - Optional (±0): "and the child was due in the summer".

### [I-09] Smaller voice notes (optional)
- **l.204** "his face had gone young": a kin of the CLOSED "had gone (quiet|still)". Optional: cut the clause.
- **l.212** "the youngest walking backward till the dark took him" echoes the Ch.17 trainer "walking backward again" (Ch.17 l.498). Optional: "the youngest looking back till the dark took him".
- **The freedman's clean nails:** three times (l.304, l.326, l.332). Optional: cut ", and Grata told him he'd clean nails" at l.326. Grata says it at l.332.
- **"Is it true…?":** twice (Felix l.138, the freedman l.320). Optional: l.320 "Is it true your husband never asked" → "Your husband never asked".
- **"palm" as hand and as branch:** l.484 "held his palm open for the nail" sits beside the palm-branch. Optional: "held out his hand for the nail".
- **Body-part rulers:** three in narration (forearm l.28, finger l.88, hand l.476). Optional: l.88 "hollowed to the depth of my finger" → "hollowed deep".
- **Grata's generalisations about men** ("they always are", l.34; "They come back when it's money", l.328; Ch.20's "the way husbands do", "none of them are"). WATCH. Optional: cut "they always are, " at l.34.
- **The herald and the rim chorus** (l.226–242) are kin to Ch.5's herald-then-overheard-men set piece (SPENT). This one differs in function (identification, not arithmetic). Keep it, but no third herald-chorus.

### [I-10] Bible sync (for the tracker and Writer, not the manuscript)
- **The freedman card is stale.** It says the Capua Lupus was "killed at Puteoli 'the spring after'" and that "he'll find another wolf" is spent. On the page the line is "He keeps a cookshop at Puteoli now … He's fat. I went in once." (l.320), and its referent is the father on the nearest reading. Neither "killed" nor "another wolf" is on the page.
- **Nicanor's card:** update "Whose is he?" (C-02), "Lupus" said once (W-01), and "The murmillo I told you of" (W-01).

### [I-11] Ledger and pacing
- **Ledger row:**
  - Chronological ✓, with the "two rooms" alternation ✓.
  - Open mid-dialogue (Felix) → `dialogue` ✓.
  - Close: a reported question ending in "?" → `question` ✓.
  - 3 breaks ✓.
  - Dialogue at 40.0% sits on the floor (see the baseline).
  - Gear mid planned, but the median is 12 and lands low (the writer's logged deviation).
- **Neighbours:** Ch.20 Collage and Ch.22 Parallel, so no repeat ✓.

---

## Information-flow table (end of Ch.21, late winter AD 74)

| Fact | Knows | Does not know | Path on the page |
|---|---|---|---|
| Mara is pregnant | Grata, the fish carter and friends, Valens (told by Mara), Felix, the street, the grandmother, Nicanor (by look) | — | l.58; l.30; l.138; l.246; l.508 |
| The summons (Rome, April; Puteoli from the Kalends of March to the Ides) | Valens, Mara; the lime carter carried it sealed | Felix (read behind the curtain), Grata | l.56, l.104–112 |
| Plautia asks after Mara and wants her brought | Valens, Mara | — | l.112 |
| Valens is "Lupus", nine times victor, freed at Corinth | Nicanor (first-hand), his three fighters, Fabius, the whole bowl, the street, Grata, Fabius's freedman | — | l.194–212, l.228–232, l.302, l.332 |
| Fabius's offer (2,000, then 3,000 + earnest) and its refusal | Valens, Mara, Nicanor, Grata (saw the purse go back) | Felix (on the page) | l.266–274, l.310–328, l.362–366 |
| Valens reads | Mara | Felix ("Felix thinks I can't read") | l.104, l.520 |
| Felix wants to swear to Nicanor; Nicanor will take him "with a beard" | Felix, Valens, Mara, Nicanor | Grata (implied) | l.478–508 |
| Mara's Delphi registration and the Syracuse cover | Mara (Valens partly) | Valens does not hear the detail ("I told him none of it") | l.432 |

---

## SUGGESTED YAML PATCHES (recommendations only; the tracker applies them after the editor's fixes)

```yaml
suggested_patches:
  - entity: "valens.knowledge (summons, learned_chapter 21)"
    action: "update"
    value: { method: "letter from Plautia's brother via the Puteoli board, fetched by the lime carter", source: "ch-21 l.56, l.108-112" }
    reason: "plan row says told_by:plautias-brothers-freedman (outline beat 1); AUTHOR-CP4-2 and the page route it through the board"
  - entity: "pomponia-grata.knowledge (summons at her counter)"
    action: "remove"
    reason: "the page never brings the summons to Grata's counter; she does not know of it"
  - entity: "valens.knowledge"
    action: "add"
    value: { fact: "Mara is pregnant; due 'with the heat'", learned: "ch-21 l.58-72", method: "told_by:mara" }
    reason: "Ch.20 I-10 handoff: the telling is Mara's"
  - entity: "felix.knowledge"
    action: "add"
    value: { fact: "Mara is pregnant", learned: "ch-21 l.138", method: "gossip: baker's boy < carter < Grata" }
    reason: "new"
  - entity: "nicanor"
    action: "create"
    reason: "new named character (trainer from Valens's Corinth school, now at the Pompeii barracks); card exists in the bible"
  - entity: "gaius-fabius-rufinus"
    action: "create"
    reason: "new named character (editor of the Saturnalia show AD 73; aedile candidate); offstage"
  - entity: "plautias-brother"
    action: "update"
    value: { name: "Sextus Plautius (if W-19 is applied)", first_named: "ch-21 l.108" }
    reason: "W-19"
  - entity: "objects.summons-tablet"
    action: "create"
    value: { location: "shelf above the bed, by the oil jar", source: "ch-21 l.128" }
    reason: "new object"
  - entity: "locations.grata-cobbler-shop.roof-stair"
    action: "update"
    value: "worn top tread replaced with oak by Valens, Nov AD 73; old tread burned"
    reason: "pays Ch.20 l.107"
  - entity: "plot_threads.fabius-offer"
    action: "add"
    value: "opened and refused ch-21; closed by Nicanor's 'I said you'd lost your wind' (l.500); Parilia date cut if W-19 is applied"
    reason: "W-19; Ch.28 guard"
  - entity: "registries.at_a_run"
    action: "keep_original"
    value: 2
    reason: "C-01 removes the third use"
  - entity: "registries.whose_question"
    action: "update"
    value: "3 on the page (Ch.5 x2, Ch.17 'Whose school?'); CLOSED; Ch.21's two removed by C-02"
    reason: "C-02"
  - entity: "felix.traits"
    action: "add"
    value: "first palm-branch scratched, barracks gatepost, late winter AD 74 (ch-21 l.474-476); cannot write his name"
    reason: "foundation §3 behaviour begins"
```

---

## Fix ledger (for book-editor; every edit is local)

| ID | Line | Change | Δ words |
|---|---|---|---|
| C-01 | 26 | "He was gone at a run," → "He was gone," | −3 |
| C-02 | 282 / 430 | "Whose is he?" → "Is he yours?"; "Whose daughter." → "Who her father was." | +1 |
| C-03 | 290 | "He kept his eyes on the road. Then, three paces on, he turned them." → "Three paces on, he looked back." | −7 |
| C-04 | 526 / 530 | "set the point of his knife where the wreath's two ends met and lifted the wreath off whole"; cut ", and the wreath" | ≈ −4 |
| W-01/02 | 176 / 200 / 206 | "bandy-legged"; cut "Mules, is it?"; "This is him. The murmillo Nero freed."; "I rake sand," | ≈ −13 |
| W-03 | 194 | "the Syrian that had no wind and the boy from Argos that cried" | 0 |
| W-04 | 200 / 274 | "Cenchreae" → "Kenchreai" | 0 |
| W-05 | 392 | cut "Some do." | −2 |
| W-06 | 90 | the laugh to one clause | −17 |
| W-07 | 88 | "…and went to his blanket." | −17 |
| W-08 | 434–438 | cut the three lines | −17 |
| W-09 | 470 | "The street fell away, and…" | −5 |
| W-10 | 498 | "Send him off again." | −1 |
| W-11 | 526 | "LVPVS showed again" | −2 |
| W-12 | 430 | cut "He said it to the burn." | −5 |
| W-13 | 400–402 / 380 | merge the two Valens lines; cut "I saw." | −2 |
| W-14 | 132 | end at "…floor wax and lilies." | −30 |
| W-15 | 328 | "a dice cup" → "a wine cup" | 0 |
| W-16 | 342 | "…she stood with her hand still up." | −4 |
| W-17 | 76 | "pressing his thumb into the middle of the tread." | −3 |
| W-18 | 222 ×2 / 232 / 332 | drop four "then"s | −4 |
| W-19 | 324 / 310 / 108 | cut the Parilia sentence; "Fifteen hundred there"; "*Sextus Plautius to…*" | −10 |
| **Total** | | | **≈ −142** |

**After the fixes:** the chapter is about 6,930 words, against a target of 7,200 with no per-chapter floor. Dialogue is about 40.4%: speech loses about 31 words and narration about 110, so the share rises slightly. Re-measure, because the floor is 40.

**Re-run after the edits:**
- `bash tools/check_chapter.sh 21`
- `tic_report.py --echoes 21`
- `python3 tools/shape_check.py books/the-hour-of-ash`

The opener (l.8) and the closing paragraph's question (l.530 from "He turned to me instead") are untouched, apart from C-04's three-word cut earlier in l.530.

---

## Repair log (book-editor, 2026-10-22)

Edits made in place in `manuscript/chapters/chapter-21.md`. ENTITY_STATE.yaml and character-bible.md were not touched. Four of the audit's own replacement strings were varied after the gates flagged them (marked ⚠).

| ID | Status | How |
|---|---|---|
| C-01 | done | "He was gone at a run," → "He was gone," |
| C-02 | done ⚠ | l.282: the audit's "Is he yours?" echoes a spoken line in Ch.13 (l.218), so it became **"Who does he belong to?"** (no other use in the book). "His own. I freed him." still answers it. l.430: "Whose daughter." → "Who her father was." |
| C-03 | done ⚠ | The audit's "he looked back" made a new 3-gram echo, so it became "Valens walked past it with the string. Three paces on, he stopped." This also drops the "Then," hinge. |
| C-04 | done ⚠ | "the point of his knife" made a pronoun-swapped echo of Ch.11 and a self-repeat in voice-wear, so it became **"Valens slid his knife in where the wreath's two ends met and lifted the wreath off whole."** The thumbnail probe is gone. l.530: ", and the wreath" cut. The closing question is untouched. |
| W-01 | done | "bandy-legged"; "Mules, is it?" cut; "This is him. The murmillo Nero freed."; "I rake sand," |
| W-02 | done | Done by the W-01 recast. "Nero freed" now matches Ch.12 (Nero sends the sword from his chair). The herald's "from the hand of Caesar himself" stays as puff. |
| W-03 | done | "the Syrian that had no wind and the boy from Argos that cried" |
| W-04 | done | "Cenchreae" → "Kenchreai" ×2 |
| W-05 | done | "Some do." cut |
| W-06 | done | Cut to one clause, and the second "at the hearth" dropped as well: "That was when I began to laugh, and he waited with oak shavings in his hair and looked at me until I was done." |
| W-07 | done | "Felix let himself in from the stalls and went to his blanket." |
| W-08 | done | l.434–438 cut. |
| W-09 | done | "He did not answer that." cut. "The street fell away, and…" now matches Ch.19's downhill route. |
| W-10 | done | "Send him off again." The chapter now has 2 spoken Then-openers. |
| W-11 | done | "LVPVS showed again, smaller this time…" |
| W-12 | done | "He said it to the burn." cut, and the two speech fragments joined. |
| W-13 | done | The two Valens lines merged. "I saw." cut. |
| W-14 | done | The sentence now ends at "…floor wax and lilies." The self-opening doors are gone. |
| W-15 | done | "a wine cup" |
| W-16 | done ⚠ | The audit's "with her hand still up" self-repeats an earlier Mara chapter, so it became "and she was left with her hand in the air." |
| W-17 | done | "pressing his thumb into the middle of the tread." |
| W-18 | done | Four "then"s dropped (l.222 ×2, l.232, l.332). |
| W-19 | done, with an override | Parilia sentence cut. "Fifteen hundred there". **Sender:** per the author's override, no name was invented. Narration: "It was from Plautia's brother, in a scribe's hand, round and even." The letter opens "*To Gaius Iulius Valens, greeting.*" The brother stays unnamed and off the page. **The I-10/YAML "Sextus Plautius" patch should NOT be applied.** |
| I-01, I-03, I-05, I-07, I-10, I-11 | n/a | Pass, handoff or bible-sync notes. Nothing to change in the manuscript. Ch.22's witnesses were left alone. |
| I-02 | partly done | "two mornings running … On the third" now agrees with Nicanor's "Three days". Skipped "The summer we came": the arrival season is not verified against Ch.19/20, so "In the summer." stays. |
| I-04 | done | "tried that door twice", which matches Ch.19. Curtain/plank-door layout: accepted as is. |
| I-06 | done ⚠ | "when I was nine" → "when I was little" ("small" self-repeated). "nine" now means only the fights. |
| I-08 | done | "the child was due in the summer" |
| I-09 | partly done | Done: "his face had gone young" clause cut; "looking back till the dark took him"; the l.326 clean-nails clause cut; "Your husband never asked…"; "they always are, " cut; "hollowed deep". Varied: "held his palm open for the nail" became "Valens reached for the nail.", because "held out his hand" hit the 3× book-wide tic gate. Kept as is: the herald and rim chorus. |

**Re-measure:**
- Prose words: 6,890 (wc, comments stripped); 6,869 by shape_check; 6,891 by show_tell.
- Dialogue: 42% by shape_check, 41.9% by show_tell. Inside the 40–50% band.
- Gates: `check_chapter.sh 21` prints ALL MECHANICAL GATES CLEAN. Voice-wear strict is clean. The tic gate is clean. Shape is clean.
- `tic_report.py --echoes 21`: 0 command echoes, 0 spoken-line echoes. No 3-gram echo is new compared with the pre-repair baseline; the advisory echoes dropped from 58 to 56.
- Unchanged: the opener (Felix and the bear) and the closing question.

**Bible-sync note for the tracker:** Nicanor's card should now quote "Who does he belong to?", not "Is he yours?".
