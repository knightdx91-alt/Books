# Continuity Audit: Chapter 22 "The Basilica Julia" (run 2, per-chapter drift audit)

**Date:** 2026-10-23
**Mode:** MANUSCRIPT AUDIT. Ch.22 is audited as it stands on disk (440 lines; after writer, dialogue-polish, hook-craft and disruptor). The writer's report quotes lines that have since changed, so every quote below is taken from the page.
**Checked against:**
- Ch.1–21 by targeted greps. Ch.12 (the telling), Ch.16 (Plautia, Marcus, the brother's house), Ch.17 (Celer, the leaf, the bladder) and Ch.21 (the summons, Fabius) were read at the relevant passages.
- ENTITY_STATE.yaml as of Ch.21, read only. The parallel Ch.22 UPDATE was not touched.
- outline.md: Ch.22 and its ledger row, plus Ch.23, 28 and 31 for forward collisions.
- foundation.md §3 and §10.
- STATE.yaml guardrails, plus CP3-3, CP3-5, CP4-1, CP4-2 and END-1.
- voice-dna.md.
- character-bible.md: the Valens, Plautia, Celer, Marcus and Myrrhine cards; the Ch.22 walk-on block; the At-risk registries after Ch.12, 14, 16, 17, 21 and 22.
- The Ch.22 dialogue, hook and disruption reports.

**Citations:** `l.NN` means a line in `manuscript/chapters/chapter-22.md`. Other chapters are cited as `ChN l.NN`.

**Mechanical baseline (read only):** `tic_report.py --echoes 22` finds 105 advisory 3-gram echoes, 0 spoken-line echoes and 1 command-echo candidate (reported speech, not a defect). The detector misses C-01, C-02, C-04, W-04, W-05 and W-06 below.

**Total findings: 34. CRITICAL: 4 | WARN: 14 | INFO: 16**

---

## Summary

The chapter delivers the outline:
- Valens says his own name to the back of the aisle (l.194–196).
- The sneeze, the "Salve" chorus and the laugh. The laugh never goes through the mouth and never uses "behaved".
- Mara is walked out (l.248).
- The Forum is whole against the 1991 ruins (l.274, l.286). The memory is triggered by the gaming board and goes back into the scene.
- The amphitheatre is in scaffolding, and the thought about it comes once (l.374).
- The verdict is money (l.400).
- Celer settles privately and stays genial (l.416–428).
- Marcus is on the steps (l.430–436).
- The chapter ends on Plautia's plain spoken line.

**The leaf is proved on the page,** as the Ch.17 continuity requires:
- two living witnesses named on it (the dyer, the fourth name; the merchant, the seventh);
- the consul's dates against the backdated bill;
- the seals said to be "on its knot", which is "wherever the book is", and Celer holds the book.

**Guards held:**
- The witnesses are never "the nine". Nicanor is absent. The brother is unnamed.
- Valens's choice to come is shown by result (the Puteoli wine shop on the Kalends).
- No tomb. No "door" except house doors. No seam, niche, painted plaster, hand flat, mountain or 79.
- Foreshadowing 0.
- The child is never gendered and never called a citizen (CP4-1).
- No arena fight is set up (Ch.28). No household hand holds a ladder or a lamp (Ch.31).

**The four CRITICALs are registry or staging violations, each fixable in a few words:**
- C-01: Celer's withdrawn hand.
- C-02: the spent bladder channel.
- C-03: a seating contradiction inside the laugh scene.
- C-04: a banned Ch.12 wording.

---

## CRITICAL (fix before the evaluator)

### [C-01] Celer's offered hand, refused and turned to the toga: a CLOSED device
- **Audit:** Character / NO TICS.
- **Evidence:** l.88: "and crossed to us with his hand out, and when the hand was not taken he used it to settle the fold at his shoulder."
- **Registry:**
  - At-risk after Ch.17: "a hand held out toward a person and withdrawn: SPENT (Ch.14, Ch.17)".
  - The Celer card's Ch.22 rule: "stages the superstition, if at all, once and differently (no scaffold, no shade line, no litter round, **no hand withdrawn**)".
  - Ch.17 l.354 ended exactly this way, with the hand put away in the toga ("hid it in his toga").
- **Fix (−21 words):** `"Valens," he said, and crossed to us with his hand out, and when the hand was not taken he used it to settle the fold at his shoulder.` → `"Valens," he said, and crossed to us.`
- **Cascade:** none. "They tell me it's Valens now." still follows.

### [C-02] Mara's bladder as a body rebel: the channel is SPENT
- **Audit:** Voice / NO TICS (body channels).
- **Evidence:** l.246: "Somewhere in all that I wet myself a little, which was the worst thing yet and made it much worse."
- **Registry:**
  - At-risk after Ch.17: "Body-rebel channels: … the bladder SPENT (Ch.17)" and "The bladder / latrine body rebel: SPENT."
  - Ch.17 l.84 used it: "My bladder was another matter … it had waited the length of the streets for this moment to want out."
  - The writer's own at-risk-after-Ch.22 entry lists "the small wetting" as part of the fifth laugh shape. That entry conflicts with the Ch.17 closure.
- **Fix (word-neutral; keeps the shift thread):** `I wet myself a little,` → `I sweated through my shift,` The rest of the sentence stands.
- **Cascade:**
  - These still read true with sweat: l.254 "a wet shift", l.258 Myrrhine's "stain", l.334 the shift soaking, Mara's refusal "It is not her work." (l.358), and Plautia's gift (l.360).
  - Bible: replace "the small wetting" in the at-risk-after-Ch.22 list.
- **Alternative (orchestrator only):** log a ruling that a pregnancy leak during a laugh is not the Ch.17 channel. The registry, as written, does not allow it.

### [C-03] Myrrhine cannot have her elbow in Plautia's side: the seating puts Mara between them
- **Audit:** Character location (room audit).
- **Evidence:**
  - l.84: "Plautia sat on the front bench … between her brother and me, with Myrrhine at my elbow."
  - l.246: "Myrrhine's thigh was against mine … and to my left Plautia went stiller."
  - l.266 (Myrrhine): "She was shaking too, my lady. Under the veil. **I had my elbow in her side and I felt it.**"
  - The order on the bench is brother, Plautia, Mara, Myrrhine. S1 binds Mara to sit beside Plautia (l.76, "Tomorrow you will sit beside me").
- **Fix (+3 words; uses her own "I was holding you up" two sentences earlier):** `I had my elbow in her side and I felt it.` → `I had my arm round you and my hand on her. I felt it.`
- **Cascade:** Plautia's "Myrrhine says that I shook." (l.364) is unaffected. Mara's own reading ("went stiller") stays as her misreading, which is the design.

### [C-04] "told where to stand": the Ch.12 telling's banned wording, moved into the advocate's mouth
- **Audit:** Information flow / NO TICS (spent wordings).
- **Evidence:**
  - l.92: "Misconduct proved by two house slaves **who were told where to stand**".
  - Ch.12 l.192: "They'd been shown where to stand."
- **Registry:** the bible's Ch.12 block: "Ch.22 must not reuse these wordings: … 'They'd been shown where to stand.'" The At-risk after Ch.17 rule adds that a line's skeleton is never moved into another mouth. Dialogue-polish cut the same idea from Valens's testimony, and it survives here.
- **Fix (−4 words):** `by two house slaves who were told where to stand,` → `by two coached house slaves,` "coached" appears in no earlier chapter.
- **Cascade:** the testimony's "The stable boy said it after her, to the steward." (l.230) still shows the coaching.

---

## WARN (fix in the editor pass)

### [W-01] Timeline: from the Kalends of March to mid-April, about five weeks are not accounted for
- **Evidence:**
  - l.16: the freedman finds them at Puteoli "on the morning of the Kalends of March", and "He had paid for everything since".
  - l.50–58: on the evening of the arrival, Plautia says "Tomorrow my brother's advocate will read my dowry out".
  - l.328 and l.368: the sentence comes on the judge's third day.
  - l.394: the Parilia (21 April) "fell the morning after the judge's third day".
  - Counting back puts the arrival in Rome around 15–16 April. Puteoli to Rome is roughly a week by carriage (Via Campana, then the Appian).
- **Why it matters:** Ch.21 set a March pickup for an April hearing (l.108), so some wait is planned. The page never says where the wait was, and a careful reader will ask.
- **Fix (+5 words, fact only):** l.16 `He had paid for everything since without being asked,` → `He had paid for everything since without being asked, a month at Sinuessa included,`
  - Sinuessa sits on the Appian Way south of Tarracina, so it does not pre-spend Ch.23's inn. It is named in no earlier chapter.
  - Avoid Capua: Ch.13 uses it, for the schools.
- **Pregnancy count:** "Five. Nearly six." in mid-April fits Grata's olive-month reading (Ch.20) and a July birth (ARCH-8). It still fits after the fix. Ch.23's "six months" holds.

### [W-02] "your man" now points at the wrong person
- **Evidence:**
  - l.140: Celer to the brother: "Your man has a carter's lungs … mine sings." Here "your man" means our advocate.
  - l.418: Celer is speaking "to **the brother's advocate**".
  - l.420: "I'm told **your man** said something on the second day about the Cornelian law."
  - Spoken to the advocate, "your man" can only mean Valens, who would not raise the lex Cornelia. Everywhere else in the chapter (13 times) the narration says "our advocate", so "the brother's advocate" also reads as a second lawyer.
- **Fix (−1 word):** l.418 `what he was saying to the brother's advocate.` → `what he was saying to the brother.`
- **Cascade:** l.416 already has him shaking "our advocate's hand, and the brother's", so the brother is beside him.

### [W-03] Marcus's "new tunic": a third use, and a historical slip
- **Evidence:**
  - l.430: "His new tunic had a purple border".
  - Earlier uses for Marcus: Ch.16 Plautia, "in a new tunic, beside his father"; Ch.17 l.332 Celer, "in the new tunic".
  - A third use reaches the book-wide tic threshold. Dialogue-polish already removed a fourth from Celer's Ch.22 line.
- **History:** a freeborn boy's purple border belongs to the toga praetexta. A tunic carries clavi (stripes), not a border.
- **Fix (−1 word):** `His new tunic had a purple border,` → `His toga had a purple border,`
- **Cascade:** none. "toga" on this page is otherwise Celer's (l.86) and the advocate's (l.96).

### [W-04] Marcus biting metal re-runs Ch.16's bracelet anchor, with a "He bit" ladder
- **Evidence:**
  - l.388 (Myrrhine): "He bit everything. He bit a silver spoon flat, and I bought its twin … and he bit that." She walked a while. "He bit my ear and hung on…"
  - Ch.16 l.232 and l.244: the bracelet's tooth marks ("Someone had cut his teeth on it."; "He had two teeth at the bottom by midsummer"). Ch.16 l.296 has Felix's bite test on the same gold.
- **Problems:**
  - A baby teething on precious metal is the Ch.16 anchor's subject, retold.
  - "He bit" appears four times in one speech (anaphora).
  - Marcus's "Does Uncle's dog still bite?" and Plautia's "It bit a magistrate" (l.432–434) bring the chapter to six.
  - "She walked a while" is the chapter's fourth "a while".
- **Fix (−30 spoken words and −4 of narration; keeps the hip, the ear and the red ears):** l.388 → `"I had the boy on my hip the whole of his first year. He bit my ear and hung on, and laughed, and his ears went red, and I couldn't get him off."`
- **Cascade:**
  - Myrrhine's buying-back trait still shows once, through the shift (l.366).
  - Bible: Myrrhine's Ch.22 block loses "the bitten spoon".
  - Dialogue share loses about 0.3 points (see the net note at the end).

### [W-05] Valens's "Who … Who … Where" fragment ladder: his own Ch.21 skeleton, and a triad
- **Evidence:**
  - l.312: "Who was in it. Who was on the roofs, and in the doorways. Where the dogs were."
  - Ch.21 (bible-quoted Valens fear): "Who is the witness's wife. Who her father was. Which house in Syracuse."
  - Same mouth, same skeleton, one chapter apart. It is also an anaphora triad, a retired reflex.
  - The Ch.21 guard asked that the Ch.22 questions be worded fresh. This is the same skeleton moved into his answers.
- **Fix (−6 words):** `"Who was in it. Who was on the roofs, and in the doorways. Where the dogs were."` → `"Who was on the roofs, and where the dogs were."`

### [W-06] "Two years behind": three uses in the book, and Celer's Ch.17 skeleton given to his advocate
- **Evidence:**
  - l.66 (Plautia): "In two years behind my chair he never told me…"
  - l.306 (Celer's advocate): "Two years behind the lady," … "in the street behind her litter…"
  - Ch.12 l.188: "Two years I walked behind her."
  - Ch.17 l.356 (Celer): "Two years at her back".
  - At-risk after Ch.17: "'at her back': CLOSED … A line's skeleton is never reversed into another character's mouth a chapter later."
- **Fixes:**
  - l.306 (−4 words): `"Two years behind the lady," the advocate was saying, "in the street behind her litter,` → `"In the street behind her litter," the advocate was saying, "`
  - l.66 (−3 words): `In two years behind my chair he never told me` → `In two years he never told me`

### [W-07] Plautia's roof scene has two pause beats; "thought about it" appears twice; "a while" appears four times
- **Evidence:**
  - l.58: "She left her hand on the rim a while".
  - l.76: "She thought about it with her face toward the far hill."
  - The Plautia rule for Ch.17/22 allows at most one pause beat per scene.
  - l.340: Valens "thought about it".
  - "a while" at l.58, l.254, l.388 and l.438. The book has 23 uses.
- **Fixes:**
  - l.76: delete `She thought about it with her face toward the far hill.` The paragraph then opens on `"Then I shall take it.`
  - l.58: `She left her hand on the rim a while, then took it away` → `She left her hand on the rim, then took it away`
  - With W-04, "a while" falls to 2 (l.254, l.438). Hook-craft's optional cut at l.438 stays optional.
- **Cascade:** "the far hill" falls from 2 to 1 (bible WATCH).

### [W-08] Valens's watching is narrated ahead of his testimony; the Basilica is reported as floor then exits
- **Evidence:**
  - l.42: "He had dropped our bag by the doorpost and stood with the street in view past the porter's shoulder."
  - l.84: "with the whole aisle in front of him and the way out at both ends of it."
  - Then S6 dramatises the same thing in his own words (l.308–312).
- **Rules broken:**
  - Bible, Parallel chapters: "the narration never pre-describes an image the other strand will dramatize".
  - Ch.13 block: "Ch.22's Basilica must not be reported as exits and floors in the same order". l.80 gives the floor and l.84 the exits.
  - At-risk after Ch.21: doorway stagings, "no third in Ch.22". Ch.21 has Felix, Grata and "Valens lingered in the doorway". l.42 adds another.
- **Fixes:**
  - l.84 (−16 words): `Valens waited with the witnesses along the pier, with the whole aisle in front of him and the way out at both ends of it.` → `Valens waited with the witnesses along the pier.`
  - l.42 (−14 words): `He had dropped our bag by the doorpost and stood with the street in view past the porter's shoulder.` → `He had dropped our bag.`

### [W-09] A lying-awake section close: a SPENT device
- **Evidence:** l.182: "I lay awake with the child's foot in my palm until the shutters went gray."
- **Registry:**
  - At-risk after Ch.8: "The lying-awake night coda: SPENT … No chapter-end listening-in-the-dark until further notice, in any wording." Here it closes a strand of a Parallel chapter, after a section of listening in the dark.
  - "in my palm until" is also a Ch.20 echo, per the echo scan.
- **Fix (−16 words):** delete the sentence. S3 ends `…the knocking of the next wheel and the next, he slept.`
- **Cascade:** the S3→S4 hook verdict was "strong" for the old exit. The new exit (he sleeps; she has just told him where to look) carries the same stake. The child's foot stays in the section (l.148, l.160).

### [W-10] Hiccups: the word and the channel were spent in Ch.15
- **Evidence:**
  - l.374: "under my hand the child had the hiccups".
  - Ch.15 used hiccups as Mara's body rebel four times; the Ch.17 registry says "hiccups SPENT (Ch.15)". The disruptor added this line and asked for it to be logged.
- **Judgement:** these are the child's hiccups, not Mara's, but the reader meets the same word inside Mara's body-report.
- **Fix (−1 word):** `the child had the hiccups` → `the child jumped at the noise`
  - The mallets and cranes are in the scene, and a fetus at six months does react to sound.
  - If the orchestrator rules that the child's hiccups are a different channel, keep the line and log it as SPENT.

### [W-11] Celer laughs three times
- **Evidence:**
  - l.108: "Celer laughed. It was a warm, easy laugh…"
  - l.138: "and Celer laughed at it with the rest."
  - l.428: "Celer laughed, delighted."
  - His card gives him smiling as his physicality. A repeated laugh beat in one chapter is turning into his device. Ch.17's "his laughing" already linked him on the roof.
- **Fix (−3 words):** l.138 `and into the next court, and Celer laughed at it with the rest.` → `and into the next court, Celer's bench included.`

### [W-12] The ladder detour steps "into the sun" when he is already in it, close to the closed shade line
- **Evidence:**
  - l.416: "waited for us outside in the sun."
  - l.418: "Celer stepped down two steps into the sun and along, round the foot of the ladder".
  - Celer card: in Ch.22 the superstition is staged "once and differently (no scaffold, **no shade line**…)". The sun/shade pairing is Ch.17's (l.354, l.390).
- **Fix (−3 words):** l.418 `stepped down two steps into the sun and along,` → `stepped down two steps and along,`

### [W-13] Plautia's purse count is an anaphora triad
- **Evidence:** l.44: "counted out for one traveler, and then for two, and then for one again". The disruptor removed another Plautia triad from l.66 (a retired reflex).
- **Fix (−4 words):** `counted out for one traveler, and then for two, and then for one again,` → `counted out for two, and then for one again,`

### [W-14] "consul … two months" echoes Celer's father (Ch.16), so a reader may merge the two men
- **Evidence:**
  - l.132 (the judge): "My friend's uncle was consul that year, for his two months."
  - Ch.16 (Plautia): "For his father's father, who held the consulship two months in a bad year."
  - Two different two-month consuls tied to the same suit invite the reader to think the assessor's uncle is Celer's family. l.136's "He'd have liked the extra months" already carries the short term.
- **Fix (−1 word):** `for his two months.` → `for his turn.`

---

## INFO

### Legal history (kept light; checked)

- **[I-01] Procedure.** On the page: a single *iudex* with three friends on stools as his *consilium*, a water clock, no jury (l.82). The *actio rei uxoriae* sits correctly: the praetor gave "our day and our judge" in the Ch.21 letter, and the condemnation is pecuniary ("The sentence is money", l.398–400).
  - "within the time the law allows him" is right for dowry restitution in instalments.
  - "I find for the plaintiff" is safe: the plaintiff is Plautia, with her brother as the managing kinsman and tutor. Women did not plead, which matches "nobody will ask me a single thing".
- **[I-02] The retained sixth.** *Retentio propter mores*: a sixth for the graver misconduct, which meant adultery (Ulpian, *Reg.* 6.12). l.58 and l.92 agree with each other and with Ch.12 l.196.
- **[I-03] The lex Cornelia de falsis** (l.420). It was extended by senatorial decrees beyond wills and coin to forged instruments. Nero's AD 61 decree on corded and sealed tablets (Suet. *Nero* 17) sits under this case. The threat is mutual: the leaf was cut from a public book. That is right, and it stays unexplained.
- **[I-04] Can a senator be sued this way?** Yes. Any husband, including a senator, could be sued for the dowry. A senatorial *iudex* ("broad purple stripe") is plausible when the parties are senatorial.
- **[I-05] Testimony.**
  - Celer's advocate: "a slave is not heard against his master" (l.98). That is the correct rule, and it turns on the status question.
  - The judge hears him first and weighs him ("decide afterward what he's worth", l.190). A private *iudex* had that discretion.
  - The ex-gladiator jab (l.318) is realistic: arena infamy could be used to impeach a witness. The judge ruling it "not in the matter" is fine.
- **[I-06] Celer's praetorship** (l.68, "a candidate for the praetorship must be seen to dine in Rome"). This fits a former legate of a proconsul who stood below praetorian rank. Praetorian elections sat in the Senate under Vespasian.
- **[I-07] The consul list.**
  - The bill is dated in Nero's Greek year (AD 66–67).
  - AD 66 suffects are known in part: Annius Afrinus, Paccius Africanus, Arruntius Aquila, Vettius Bolanus.
  - For AD 67 the standard lists give only the *ordinarii*, Fonteius Capito and L. Iulius Rufus. The suffects are unattested.
  - The uncle is unnamed, so nothing on the page contradicts a known consul.
  - **Guard:** never name him. If a later page dates the bill, put it in AD 67.
  - The Ch.17 book label "P. VETT. L. CANIN." is the colony's duoviri, not consuls, so it does not collide with Vettius Bolanus.
- **[I-08] The Basilica Julia.**
  - Four courts at once with curtains between them, and the centumviral court hearing a will next door (l.80). Pliny *Ep.* 6.33 and Quintilian 12.5.6 fit this.
  - "A court of a hundred men" is a fair translation of *centumviri*.
  - Gaming boards cut in the floor and the steps are real.
  - A dowry *iudex* sitting in a side aisle is plausible staging.

### Rome, AD 74

- **[I-09] The Flavian Amphitheatre.**
  - Begun about AD 70–72, so "not a third built" with one or two tiers of arcades in 74 is right.
  - Travertine from the Tibur quarries by road (and oxcarts allowed by day as public building work, which agrees with l.10).
  - Iron cramps run in with lead; treadwheel cranes.
  - "Out of Judaea" (the spoils).
  - Nero's drained lake; the Sacra Via over the Velia.
  - The Argiletum's cobblers.
- **[I-10] The Forum.**
  - The Temple of Castor whole (the Tiberian rebuild).
  - The round Temple of Vesta smoking; it was restored after 64.
  - The Basilica Julia.
  - Martial's broken-glass-for-sulphur-matches peddler.
  - Iron-tyred night carts under the daylight wheel ban.
  - "Salve" to a sneeze (Pliny *NH* 28.23).
  - All right.
- **[I-11] The Parilia ash** (l.286): "calf's ash, and blood dried on bean stalks".
  - Ovid (*Fasti* 4.731–734) gives three things: the October Horse's blood, the calf's ash (from the Fordicidia, 15 April) and empty bean stalks. The page fuses the blood onto the stalks.
  - The timing is right: the Fordicidia ash exists by day two (about 17 April).
  - Optional fix: `calf's ash, and blood dried on bean stalks,` → `calf's ash, a horse's dried blood and bean stalks,`
- **[I-12] The courts on games days.**
  - Counted back from the Parilia, the hearing days fall inside the *ludi Ceriales* (12–19 April). Forensic business was normally suspended on games days (Cic. *Cael.* 1).
  - The page never dates the hearing days, so no fix is needed.
  - Guard: no later chapter names the hearing's calendar date.
- **[I-13] Small accuracy touches (optional).**
  - Seals "hanging from the cord in a row like fruit" (l.98): Roman witnesses sealed over the cord, along the tablet's groove, not as pendants. The narrator is a conservator. Fix: `with the seals hanging from the cord in a row like fruit` → `with the seals pressed over the cord in a row`. This also cuts a simile and the Ch.13 "in a row like" frame.
  - "fine Coan linen" (l.360): Coan cloth was a silk gauze. Fix: `Coan linen` → `Egyptian linen`.
  - "the next hill along" (l.50): from the Quirinal the next hill is the Viminal. Fix: `the next hill along` → `the hill beyond the next`.
  - "Facing the Basilica's steps … the temple of Castor" (l.286) is true only at the Basilica's east end, across the Vicus Tuscus. It can stand.

### Character, information flow, objects

- **[I-14] Consistent; no action.**
  - **Valens's name and freeing:**
    - Gaius Iulius Valens, the lanista's freedman (Ch.16).
    - Thrace; "five years" in the sand (Ch.12).
    - The sword "came down … from the tribunal". Nero touched it and did not rise. This matches Ch.12 ("never got out of his chair … sent the sword out") and the Ch.21 W-02 repair. "his clerk wrote me down" is compatible with Ch.12's "a magistrate wrote my name".
    - The prior-sale claim, "a full month ahead" = Ch.12's "the month before the games".
    - Wages from "the legate's steward". "Legate" is Valens's habitual title; Celer was legate when he hired him.
    - The frame is "summer. Vitellius had Rome." (July 69).
  - **Celer:**
    - knows Mara's name (Ch.17, "Bring Mara.");
    - "Lupus" in Ch.17 and "practicing" Valens now, even though Plautia always said Valens (Ch.16). That is his insult, not a slip;
    - the toga "new again" follows Ch.17 l.308;
    - he never says "wife" and never threatens directly.
    - His dinner-foot habit (l.352) has an on-page path to Mara before the payoff at l.420.
  - **Plautia:**
    - no contractions; never names Celer; "my former husband" 0 (book-wide still 1);
    - her built hair covers both ears, which hides the Ch.16 torn lobe;
    - the dowry's "earrings" sit quietly beside that lobe;
    - she is about 30 (b. c. 44);
    - "five years" since 69;
    - the Esquiline house is "for the year". This agrees with Marcus "brought down this morning".
  - **Marcus:**
    - born "the autumn after the fire" (autumn 64), so nine; never given as a number;
    - formula, then the rush;
    - holds the veil, which she does not touch;
    - his ears follow Ch.16 and Ch.17 and are not pointed at.
    - "Uncle's dog … the one on the chain" is reconciled with Ch.16's friendly porch dog by "the one on the chain".
  - **Myrrhine:**
    - from Plautia's father's house, twelve at the autumn-63 wedding;
    - prices and buying-back are hers alone;
    - Greek to Mara.
  - **The brother:** unnamed; a house of his own at Corinth (Ch.16/17); a rented house on the Quirinal for the suit.
  - **Mara:**
    - 26 in July 1991 fits a Jan–Apr 1965 birthday (Ch.6 "thirty-three", Ch.14 fourteen in April 1979);
    - the passport is in Ch.2;
    - "first summer abroad" agrees with "Emilio never took her abroad" (Ch.7);
    - her Latin is uncontracted;
    - one comprehension report ("a word … that I did not catch").
  - **Knowledge paths on the page:**
    - Plautia's knowledge of the Kalends ("So the freedman wrote");
    - Myrrhine to Mara, and Myrrhine to Plautia ("Myrrhine says that I shook");
    - the gallery woman's "this gladiator" is court gossip after the name was said;
    - the advocate's knowledge of the cut book comes through Plautia (Ch.17);
    - the witnesses are found by the names on the leaf with the brother's silver.
  - **Objects:**
    - The leaf: no seal; "cut from a book, with a knife"; the knot invoked but not described, as Ch.17's guard allows.
    - The book is with Celer.
    - The watch and the bracelet are not on the page: no wrist conflict.
  - **Felix:** stays in Pompeii with the contractor's string (Ch.21 l.162, l.328). Nothing of Ch.28 is pre-spent.
- **[I-15] Forward guards.**
  - **Ch.23:**
    - Mara is "Five. Nearly six." here, so "six months" at the inn holds.
    - Valens is not triumphant on the page ("They asked me the rest."), so the sadness is unspent.
    - The onion surfaced here as "They grew those … smell the village", so Ch.23 needs fresh words (no village, autumn or smell-before-seeing).
    - **New:** Ch.22 spent his palm on her belly and the heel ("That's a heel." / "It's the shape of one."). Ch.23's heat must handle the pregnant body through other touches.
    - The Plautia shift may travel with them, but not as a button.
  - **Ch.28:** no arena fight is set up. Celer's advocate's gladiator jab goes unanswered.
  - **Ch.31:**
    - Mara climbs a ladder to the roof (l.50). She does not hold one.
    - A slave hangs greenery from a ladder (l.418).
    - No household lamp, no "hold the ladder", no crew.
    - Clean.
  - **Fabius's Parilia offer:** closed by absence. Valens is in Rome on the 20th. Ch.21 had already refused it flatly; the bible's "left unanswered" line should read "refused (Ch.21); Valens in Rome at the Parilia".
- **[I-16] Small echoes and repeats (optional; editor's choice).**
  - "She hauled me to my feet." (l.286) and "Myrrhine hauled me back" (l.374): `She hauled me to my feet.` → `She got me to my feet.`
  - "the voice he used on the string in a crosswind" (l.196) reuses Ch.1's frame for Emilio's voice ("in the voice he used when he thought only I could hear"). Fix: `He gave it the voice he used on the string in a crosswind,` → `He said it as he would hail the string in a crosswind,`
  - "his ears stuck out" (l.430) is a Ch.4 3-gram. Fix: `his ears stuck out from it` → `his ears poked out of it`
  - "The porters were still at their walnuts" (l.436): this is days after S5, so "still" reads as the same afternoon. Fix: `were still at their walnuts` → `were at their walnuts again`
  - "wound" three times (l.124, l.230, l.406); "a hand taller" and "a finger's width" are body-part rulers (WATCH, 2).

---

## Net effect of the fixes

- **Words:** about −150 in all (C-01 −21; W-04 −34; W-08 −30; W-09 −16; the rest small).
- **Spoken words cut:** about 50 (W-04, W-05, W-06, W-13, W-14).
- **Narration cut:** about 100. The narration cuts roughly offset the spoken cuts, so the dialogue share should stay near 35.6–35.9% against the 35% floor. Re-measure with `show_tell` after the repair. If it dips below 35.0, restore W-13 or W-14 first; both are spoken.
- **Gates to re-run after the repair:** `check_chapter.sh 22` and `tic_report.py --echoes 22`.
  - Every replacement string above was grepped against Ch.1–21. "coached", "for his turn", "arm round you", "my hand on her", "Sinuessa", "His toga had", "jumped at the noise", "Celer's bench included", "got me to my feet", "poked out", "hail the string" and "pressed over the cord" appear in no earlier chapter.

---

## SUGGESTED YAML PATCHES (for the entity-tracker's next UPDATE; not applied)

```yaml
suggested_patches:
  - entity: "timeline (ch-22)"
    action: "add"
    value: { event: "Puteoli Kalends of March -> Rome eve of hearing ~15-16 April AD 74; hearing day 1, day 2 (testimony), sentence on the judge's third day = 20 April; Parilia 21 April", gap: "about five weeks unplaced unless W-01's 'a month at Sinuessa' is applied" }
    reason: "W-01"
  - entity: "mara-reyes.physical.pregnancy_1"
    action: "add"
    value: { ch22: "'Five. Nearly six.' on arrival in Rome (mid-April AD 74); the child's foot/heel under Valens's palm" }
    reason: "consistent with Grata's olive-month reading and a July birth"
  - entity: "mara-reyes.body_channels"
    action: "update"
    value: "bladder remains SPENT (Ch.17); Ch.22's laugh = heels, shoulders, bench, eyes and nose (+ sweat if C-02 applied)"
    reason: "C-02"
  - entity: "scene.ch22.basilica.seating"
    action: "add"
    value: "front bench: the brother, Plautia, Mara, Myrrhine; Valens and the two Corinth witnesses by the pier"
    reason: "C-03 room audit"
  - entity: "quintus-arrius-celer.ch22"
    action: "add"
    value: "loses; brings Marcus 'this morning'; settlement: Marcus to dine at the brother's every market day in Rome and at Corinth when sent for; 'Nobody wants the Cornelian law'; the ladder detour on foot; the foot 'go[ing] on the step'"
    reason: "new facts"
  - entity: "assessor's uncle"
    action: "create"
    value: "unnamed; consul (suffect) in the bill's year; spent the bill's month at his villa at Tibur. Never to be named (no known-list conflict for AD 67)"
    reason: "I-07"
  - entity: "marcus.ch22"
    action: "add"
    value: "first on the page; toga (if W-03) with purple border; Greek pedagogue; 'Uncle's dog … the one on the chain' (a second dog at the brother's Corinth house)"
    reason: "W-03, I-14"
  - entity: "valens.knowledge"
    action: "add"
    value: { fact: "Celer's right foot taps under the table when kept waiting", learned: "before ch-12 (Corinth service)", told_to: "Mara, ch-22 l.352" }
    reason: "knowledge path for the l.420 payoff"
  - entity: "fabius-rufinus.parilia-offer"
    action: "update"
    value: "refused (Ch.21); Valens in Rome on 20-21 April (Ch.22)"
    reason: "I-15; the bible's 'left unanswered' is inexact"
  - entity: "walk-ons ch-22"
    action: "create"
    value: "the freedman (the brother's); the widow (off-page); the iudex; three assessors; our advocate; Celer's advocate; the water-clock slave; the dyer (4th name); the seasick merchant (7th name); the onion man / sneezer; the attendant; the gallery woman with a baby; two walnut porters; the Vestal girl; the ladder slave; Marcus's pedagogue; the reader of the will (next court)"
    reason: "coverage"
```

---

## Repair log (book-editor, 2026-10-23)

**CRITICAL**
- **C-01** done: the clause is cut to `"Valens," he said, and crossed to us.` and the next line stands.
- **C-02** done: `I wet myself a little,` → `I sweated through my shift,`. The shift thread still holds: the wet shift on the steps, Myrrhine's stain and fuller, the shift soaking in the basin, "It is not her work.", and Plautia's gift with Myrrhine's morning line. The bible's "small wetting" entry is NOT edited (out of scope). The entity-tracker or orchestrator should replace it with "sweat through the shift".
- **C-03** done: Myrrhine now says `I had my arm round you and my hand on her. I felt it.`
- **C-04** done: `by two coached house slaves,`

**WARN**
- **W-01** done, with the orchestrator's override (no Sinuessa). The house paragraph now reads `…people with business at law, and we had a month in it before the court sat.` They reach Rome in March, about a week from Puteoli. The roof scene stays on the arrival evening, so its dating is undone:
  - `Tomorrow my brother's advocate will read` → `When the judge sits, my brother's advocate will read`
  - `Tomorrow you will sit beside me` → `On the day, you will sit beside me`
  - Plautia's "eleven days" (her own time in Rome) still fits.
  - The Parilia sentence is kept unchanged.
- **W-02** done: `what he was saying to the brother.`
- **W-03** done: `His toga had a purple border,`
- **W-04** done: Myrrhine's line is the audit's version (the hip, the ear, the red ears). The spoon and the "He bit" ladder are gone, and so is "She walked a while".
- **W-05** done: `"Who was on the roofs, and where the dogs were."`
- **W-06** done, both: the l.306 opener is now `"In the street behind her litter," the advocate was saying, "at the door…`; l.66 is `In two years he never told me`.
- **W-07** done: the "thought about it with her face toward the far hill" beat is deleted, and so is "a while" on the rim. "a while" is now 2 in the chapter and "far hill" is 1.
- **W-08** done, both: `He had dropped our bag.` and `Valens waited with the witnesses along the pier.`
- **W-09** done: the lying-awake sentence is deleted. S3 ends on "he slept."
- **W-10** done: `under my hand the child had the hiccups` → `the child stretched in me from one hip to the other`. This is a slow stretch, which is physically right at about 6 months. It does not use the heel, a hand on the belly, a jolt (the laugh scene already has one) or a startle. "stretched" is used of the child in no earlier chapter.
- **W-11** done: `and into the next court, Celer's bench included.`
- **W-12** done: `stepped down two steps and along,`
- **W-13** done: `counted out for two, and then for one again,`
- **W-14** done: `for his turn,` The quote's punctuation on the page was a comma, not a full stop.

**INFO taken**
- I-11: `calf's ash, a horse's dried blood and bean stalks,`
- I-13:
  - seals: `pressed over the cord in a row`;
  - linen: `fine Egyptian linen`;
  - hill: `the second hill over lay dark already`. I did not use the audit's "the hill beyond the next", because "beyond the next" is a Ch.19 3-gram.
- I-16:
  - `She got me to my feet.`
  - `his ears poked out on either side`. I dropped "of it": "out of it on" tripped voice-wear self-repeat.
  - `were at their walnuts again`
  - The crosswind line is now `He pitched it as he would hail the string in a crosswind,`. I did not use the audit's "He said it as…": "He said it as" repeats Ch.15, and after "Freed at Corinth." it formed the self-repeat "at corinth he said". Both are BLOCKING under voice-wear.

**INFO not taken:** I-12 (no date on the page, guard only), I-16 "wound" ×3 and the body-part rulers (WATCH only, no defect), and I-01–I-10 and I-14–I-15 (no action needed).

**After the repair**
- `check_chapter.sh 22`: ALL MECHANICAL GATES CLEAN.
- Prose 7,212 words (show_tell); file `wc` 7,551.
- Dialogue 35.8%, above the 35% floor. W-13 and W-14 did not need restoring.
- `tic_report.py --echoes 22`: 99 advisory echoes, down from 105. None of them comes from a replacement string. Spoken-line echoes are 0, and the one command-echo candidate is unchanged (reported speech).
- Kept: the opening spiral, the name anchor, the sneeze, the testimony substance and Plautia's closing line, exactly.
