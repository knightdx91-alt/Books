# Continuity Audit: Chapter 15 (run 2, per-chapter drift audit)

**Date:** 2026-10-20
**Mode:** MANUSCRIPT AUDIT. Ch.15 "Summer Pasture" (post-disruptor) is checked against:
- Ch.1–14 as they stand on disk;
- ENTITY_STATE.yaml as of Ch.14 (read only; the tracker update is running in parallel);
- outline.md, foundation.md, voice-dna.md, character-bible.md and voice-bank samples 01–13;
- the STATE.yaml guardrails and resolved_author_decisions.

**Chapter reviewed:** `manuscript/chapters/chapter-15.md`
- **Length:** **7,787** prose words by shape_check (8,100 by `wc -w` with the header). The floor is 7,300, so there are **487 words of headroom**. The recommended WARN fixes below come to about **−51 net** (about 7,736).
- **Shape:** dialogue 33.3% (band 30–40). 3 breaks. Median sentence 17 (gear high). `long-spiral` → `quiet`, which matches the ledger.
- **Citations:** `l.NN` is the file line in chapter-15.md. Lines in other chapters are cited as `ChN l.NN`.

**Mechanical baseline** (`bash tools/check_chapter.sh 15`, run read only): **ALL CLEAN.**
- Style clean; grammar 0 errors (3 long-sentence notes); rhythm 0.
- Show/tell: no flags. Voice-wear strict clean.
- Tic gate clean, including gesture classes. Echo scan 0. Command echo 0.
- And-chains 6 (cap 9); credential asides 0 by gate (1 by hand: "as I would a bronze left too long in its crate after a dig", l.374).
- Metaphor: 1.4 fig/1k. Shape audit: SHAPE CLEAN.

**My own sweeps:**
- 4- to 6-grams of Ch.15 against Ch.1–14 and every voice-bank sample (one 6-gram hit the gate missed: W-05).
- Structural comparison against samples 03, 08 and 10, which bear on the teeth, the Valens Q&A and the heat.
- Narrator call-out pointers, counted by hand against the bible's SPENT rule.
- Paragraph-final negations by script, then checked by hand.
- The flashlight's history from Ch.2 through Ch.15, line by line.
- The crack's geometry across Ch.3, 6, 8, 14 and 15.
- An information-flow table for everyone on the pasture.
- The AD count, the calendar (Bysios to July), and the 1998-era facts.

**Total findings: 58. CRITICAL: 0 | WARN: 12 | INFO: 46**

**Summary**
- **No CRITICAL.** Every canon point in the brief holds:
  - She tells Valens 1998, the cave door and Pompeii-as-a-place. She withholds Pompeii's fate (l.282, explicitly).
  - His disbelief holds (l.496–510).
  - The mule line lands once (l.190).
  - The bargain matches outline Ch.15–17 and foundation §3.
  - No lens cap, the rim dented, the ibuprofen gone.
  - The heat stays inside canon: explicit, no purple, no clinical terms, no temperature report, em-dash 0.
- **The contraception line is safe.** l.572 is risk-awareness only. voice-dna §5 permits it exactly once, here. It implies no conception, so the canon of Lucius born summer AD 74 is untouched.
  - It does clash with the chapter's own calendar ("by my own count", l.20). That is W-06, a three-word fix.
- **CH13-7 is resolved.** The cave backfill is consistent with Ch.3/5/6/8 on the flashlight, the crack and what Valens saw.
  - Two soft spots, both INFO: the crack's back wall against Ch.3's 1998 beam (I-03), and who waited for whom at the foot of the cliff (I-04).
- **The WARNs are mostly voice drift the gates cannot see:**
  - six narrator call-out pointers, against a SPENT rule of 0 (W-01);
  - an Elateian stance Mara never witnessed (W-02);
  - two "road" comparisons inside the union (W-03);
  - a structural lift of sample-03's teeth beat (W-04) and a 6-gram from sample-11 (W-05);
  - S1 and S3 both closing on Valens walking off to the animals (W-10).
- **Four WARNs are world or continuity slips:**
  - "No emperors anywhere" in 1998 (W-07);
  - "Nobody yet" against her own Ch.6 rent arithmetic (W-08);
  - a month at the yard on the public road that the page never accounts for (W-09);
  - the watch pouch thrown into a corner with the belt (W-11).
- **One WARN is a cascade into outline Ch.16 (W-12).** Ch.15 has Kallia publicly "sail" Mara in spring, and Mara has worn the Ch.7 himation all summer. The planned autumn farewell at Kallia's sill, with the himation given, needs re-staging in the outline before the Ch.16 writer runs.

---

## Scorecard by category

| Category | Result |
|---|---|
| No-foreshadowing (§0, families A–E) | ✓ 0 breaches. AD 79 once as a present thought (l.282). I-18 lists the lines checked. |
| Oracle canon (WHERE given, WHEN withheld; Fenn's WHEN untouched) | ✓ |
| Knowledge flow (told / not told / overheard) | ✓ for Pompeii's fate and disbelief. **W-02** (the Elateian). I-16 and I-17 cover the table and Mnason's position. |
| Cave backfill (Ch.3/5/6/8/9/14) | ✓. I-01 to I-05 cover the flashlight's history, the crack and the morning. |
| Bridge to summer (Corinthian, Kallia's story, pasture, Mnason) | ✓ except **W-09**. I-31 to I-33 cover the rest. |
| History and world (AD count, monk, marriage, suit, figs, bed, 1998 facts) | ✓ except **W-07** and **W-08**. I-06 to I-10, I-19 and I-20 are polish. |
| Bargain vs outline Ch.16–17 / foundation §3 | ✓. **W-12** is a cascade. I-20 to I-22 cover the rest. |
| Heat canon | ✓ register. **W-03** (comparison budget) and **W-11** (characters stay themselves). I-44 is the full check. |
| Pregnancy | ✓ safe. **W-06** is the wording clash. I-15 covers the cascade. |
| Objects (no cap; dented rim; ibuprofen gone; watch; fig) | ✓ except **W-11**. |
| Voice drift (no tics, spent moves, voice-bank, comparisons in Valens's speech) | Gates clean. **W-01, W-03, W-04, W-05, W-10** were found by hand. Valens uses no comparison in speech ✓. |

---

## PRIORITY: ENTITY_STATE conflicts (processed first)

ENTITY_STATE holds 49 UNRESOLVED flags. The ones Ch.15 touches:

- **CH13-7 (the cave "Tomorrow")**: **RESOLVED on the page.**
  - l.22: "I had been inside it once since the consultation."
  - l.24–50: the climb the morning after, with Valens and two mules; the beam; the back wall; "It was shut, as I had wished it".
  - This agrees with Ch.14 l.134 "I wanted it shut." and Ch.13 l.360 "I want to see it shut for myself."
- **CH12-7 (who has seen the camera)**: **RESOLVED.**
  - l.232–256: shown to Valens, held, the wrong end first.
  - l.244: "The boy says it was your father's." This is the Ch.12 l.252 path, relayed.
- **CH14-4 / plot_threads.euthydikos-bowl (Ch.14 audit I-17)**: **RESOLVED.**
  - l.342: "I meant to winter in Delphi. Euthydikos has a bowl for me…"
  - l.344: "Delphi's put you on a boat. Leave yourself on it."
  - l.354: "The priest's bowl could keep its lead; it had kept it this far."
- **CH12-2 (the record's form)**: **still open.**
  - l.298: "The book with my name in it." This agrees with Ch.12 l.200, "The magistrate's book…".
  - It pushes further from outline Ch.17's "bronze-and-wax diptych" (I-22).
- **CH12-5 (who sent the three men)**: **NARROWED.**
  - Valens now attributes the road to Celer: l.326, "Celer's chose a road for it."
  - The runner comes looking for Mara at the spring (l.14).
  - The sender is still not established beyond Valens's inference.
- **CH12-4 (sailing season)**: Kallia's public story is "Gone to Kirrha at the turn of the month and onto a boat for home" (l.16), told in the month after the consultation. This is consistent with an open early-spring season. Still open as recorded.
- **CH11-4, CH12-3, CH12-8, CH12-9, CH13-3, CH13-6, CH13-8**: not touched by Ch.15.
- **No new physical-attribute contradiction.** New facts for the tracker:
  - Mara is "the tall foreigner" (the Corinthian's description, l.14). This is the first height descriptor for her anywhere.
  - Valens shaves by feel with his knife.
  - Both of Felix's shins are skinned.

---

## CRITICAL ISSUES (must fix before proceeding)

**None.** Each candidate was re-checked against the source lines before being placed below:
- Pompeii's fate is not told: l.282, "I left it standing where it was."
- Disbelief holds: l.498–510.
- The pregnancy line implies no conception: l.572.
- The cave backfill does not contradict the flashlight's history: Ch.5 l.3, Ch.6 l.18, Ch.7 l.24, Ch.8 l.24.
- The bargain matches the outline: outline Ch.15 beat 1, Ch.16, Ch.17 beat 1.

---

## WARN ISSUES (should fix)

### [W-01] Six narrator call-out pointers. The bible rule is SPENT, cap ≤1, "treat it as 0"
- **Audit:** Voice drift. Bible "Narrator call-out pointers to callbacks: SPENT … Proposed cap ≤1 per chapter; treat it as 0" (character-bible l.2924–2928). The Ch.14 audit cut two.
- **Evidence:** each instance names an earlier scene to label a thing in this one:
  - l.118: "the knife he had taken in the ditch, by feel, with no glass" (Ch.12)
  - l.220: "where the graze from the road had healed into a pale seam" (Ch.12)
  - l.234: "I wore it next to my skin still, as I had in Kallia's crowded house," (Ch.12 l.162)
  - l.252: "toward the dent in the rim where the man's head had been" (Ch.12)
  - l.282: "The rest of what I knew stood behind the name, where it had stood since Theano's step:" (Ch.13/14)
  - l.416: "the way the Elateian had stood at the gymnasium" (Ch.13; also W-02)
- **Note:** the disruptor's report records "narrator call-out pointers 0". By the bible's definition the count is six. The objects (knife, graze, dent) carry their history without being pointed at.
- **Suggested fix (−29):**
  - l.118: "the knife he had taken in the ditch" → "**his knife**" (−6)
  - l.220: "where the graze from the road had healed" → "where **a graze** had healed" (−3)
  - l.234: cut ", as I had in Kallia's crowded house," (−7)
  - l.252: cut "where the man's head had been" → "toward the dent in the rim, and I had his wrist…" (−6)
  - l.282: cut ", where it had stood since Theano's step" → "The rest of what I knew stood behind the name: eight years on…" (−7)
  - l.416: see W-02.
- **Cascade risk:** none. The dent stays on the page (the object fact). Re-run the echo scan and the rhythm gate.

### [W-02] "the way the Elateian had stood at the gymnasium": Mara never saw it
- **Audit:** Information flow (narrator knowledge).
- **Evidence:**
  - l.416: "He kept his feet planted wide, the way the Elateian had stood at the gymnasium, lunging and dancing back…"
  - Ch.11 l.242–252: Felix begs to go to the boxing and is kept in the yard. Mara is mending in the shed.
  - Ch.13 l.42: "He knocked a man down at the gymnasium yesterday…" (Felix's report). Ch.13 l.254: "The Elateian asked me yesterday at the gymnasium…" (Felix's report).
  - Mara's only sight of the Elateian is on the terrace "praying very hard over a cake" (Ch.13 l.44) and Felix "studying his hands" (Ch.13 l.92).
- **Problem:** she narrates a stance she never witnessed, as if from memory. The plausible path is Felix's endless description, so this is WARN, not CRITICAL. It is also a call-out pointer (W-01).
- **Suggested fix (−8):** cut "the way the Elateian had stood at the gymnasium," → "He kept his feet planted wide, lunging and dancing back out of range and lunging again…"
- **Alt (0):** "the way **he swore** the Elateian had stood". This keeps the boy's hero-worship but keeps a pointer.

### [W-03] Two comparisons inside the union, both built on "road". The heat budget is one
- **Audit:** Heat canon / voice drift.
  - voice-dna §5: "one characterizing comparison at most per scene (sample-10 uses one)".
  - §4: heat ≤2 similes per scene.
  - The bible records the road simile as "the scene's one comparison" and bans "road comparison" in Ch.23/34.
- **Evidence:**
  - l.562: "he had gone quite still, **the way he went still on the road** when he had heard something."
  - l.570: "He learned me after that **as a man learned a road** he meant to take again at night…"
  - Both fall after the laughter stops. The teeth simile (l.558, "like a row of new tiles") is in the comic prelude, and with it the scene has three.
- **Suggested fix (−13):** l.562 → "His knuckles stayed at my mouth, and he had gone quite still."
  - Keep l.570 as the scene's one comparison, as the bible records.
  - His stillness still pays off at l.578 ("as he could hold still for anything; then the stillness left him").
- **Cascade risk:** none. The bible's "one comparison" record becomes true.

### [W-04] The teeth beat is a structural lift of voice-bank sample-03
- **Audit:** Voice drift.
  - voice-dna §6: "No sentence, image or line from any sample may be reused".
  - Bible: "Voice-bank samples leak by structure as well as by string".
- **Evidence:**

  | Beat | sample-03 l.4 | Ch.15 l.558 |
  |---|---|---|
  | all teeth present | "Every tooth was present" | "not one was missing" |
  | white | "and nearly white" | "they were white and square and even" |
  | never near dentistry, with a list | "she had never in her life been near a dentist, a fluoride rinse, or a length of waxed floss" | "he had gone his whole life without coming within a mile of a toothbrush, or of a dentist with his little mirror and his opinions" |
  | resentment | "with a professional resentment" | "and resented them" |

  The four beats come in the same order.
- **Problem:** the outline wants the teeth noted at the wrong moment, and the subject is canon (foundation chaos trait). But this is the sample's skeleton with the nouns changed. The gates are string-based and cannot see it, and an evaluator who has the samples will.
- **Suggested fix (−13):** turn the beat on her own mouth instead of his history.
  > "His teeth showed by the doorway's glow, square and even, set in his gums like a row of new tiles. I had flossed twice a day since I was fourteen and still paid a man in a white coat to scold me, and I lay in the wreck of the herdsman's bed and held every one of his against him."
- **Cascade risk:** this is a new small fact about Mara (flossing since fourteen). It agrees with foundation §3 (floss, judged dentists) and Ch.2 l.111. The teeth surfacing still counts as 1 (bible ✓). Re-run the echo scan.

### [W-05] A 6-gram from voice-bank sample-11, which the echo scan missed
- **Audit:** Voice drift (voice-dna §6).
- **Evidence:**
  - l.560: "His hand was still under my head; I drew it out and **held it up to the doorway**."
  - sample-11 l.8 (the reserved Ch.20 visible-seam beat): "When she came for it she **held it up to the doorway** and traced the line with her fingernail".
  - The gesture is the same: inspecting a damaged thing by doorway light. It is Ch.20's anchor action.
- **Suggested fix (+1):** "I drew it out and **tipped it to the light from the door**."
  - Avoid "the doorway's glow", which l.558 already uses.
- **Pipeline note (root):** `tic_report.py --echoes` scans voice-bank samples for 5+ words but skipped this. The run is bounded by stop words ("held … the doorway"). Include stop-word-bounded n-grams of 6 or more in the sample scan (I-36).

### [W-06] The contraception thought collides with the chapter's own calendar
- **Audit:** Internal consistency / pregnancy canon. The line itself is safe (I-15).
- **Evidence:**
  - l.572: "Nothing in that hut stood between me and a child but luck, and **I had not counted a day since October**; it went through me, and I did nothing to stop it."
  - l.20: "It was July now, **by my own count**, which nobody else on the mountain kept."
  - Ch.8 l.18: "a few days past the turn of the year **by my private reckoning**."
- **Problem:** she keeps the calendar (l.20, Ch.8) and then has "not counted a day since October". The intended sense, her cycle, is clear only by inference, and a literal reader trips over it 550 lines after l.20.
- **Not a pregnancy implication.** Nothing implies conception, so Lucius (summer AD 74, conceived about autumn 73: outline Ch.20/22, foundation §10) is untouched. voice-dna §5 sanctions exactly this thought, once, in Ch.15, with no narrator resolution.
- **Suggested fix (+3):** "…but luck, and **since October I had not known where I was in my month**; it went through me, and I did nothing to stop it."

### [W-07] "No emperors anywhere": Japan had an emperor in 1998
- **Audit:** World / 1998-era knowledge (authenticity dial 8+; Mara is a classicist).
- **Evidence:** l.202: "Nobody. No emperors anywhere. There are a few kings left, who cut ribbons on bridges and wave from carriages."
- **Problem:** Akihito reigned from 1989 to 2019. Mara knows the word "emperor" professionally, so the blanket statement is hers to get right.
- **Suggested fix (0):** "Nobody, **where I live**. There are a few kings left, who cut ribbons on bridges and wave from carriages." Valens's "So the legions went home." still follows.

### [W-08] "Nobody yet. My rent will come due": this reverses her Ch.6 arithmetic
- **Audit:** Character consistency (Mara's own stated belief about home time).
- **Evidence:**
  - l.226: "Nobody yet. My rent will come due, and somebody at my work will ring my telephone…"
  - Ch.6 l.332: "the rent is due on the first, and **I'm behind by now, I suppose, unless they've given it to somebody else**."
  - Ch.13 l.224: the apartment imagined with "the heat … off".
  - Foundation §9 says the doors don't deliver to matching dates, but Mara does not know that yet.
- **Problem:** after nine months gone, "yet" and the future tense say no time has passed at home, which she did not believe in November. Nothing on the page has changed her mind.
- **Suggested fix (−3):** "**My landlord, by now.** And somebody at my work **will have rung** my telephone, and **got** my own voice on a tape, saying I am not at home."
  - Valens's "That's true, then." still lands on the tape.
- **Cascade risk:** none. It keeps the question of home time open for Fenn (Ch.25).

### [W-09] A month or more at Valens's yard that the page does not account for
- **Audit:** Timeline / plausibility (the cover).
- **Evidence:**
  - l.14: "**In the month after the consultation** a stranger had sat most of a morning on the step at the lion spouts". The 7th of Bysios is about Feb–Mar, so this is Theoxenios, about Mar–Apr.
  - l.18: "That night Kallia packed my bag … Before light I was at Valens's yard, and on the evening the mules started up for the summer pasture I followed them".
  - l.14: "We had been up on the grazing **since the snow left the high ground**." This is about May at this altitude.
  - l.54: "**In two months** I had learned to do it badly…" This counts from about May to July.
- **Problem:** several weeks fall between leaving Kallia's and the ascent. The yard is on the public Kirrha road (Ch.11 l.144), forty paces from Praxias, who gossips (Ch.11 l.346). Celer's runner has just asked for her by description. The page implies she went straight up, and the calendar says she could not have.
- **Suggested fix (+15), one clause at l.18:**
  > "Before light I was at Valens's yard, **and I kept to the loft under the stable reeds until the pasture was clear of snow;** on the evening the mules started up for the summer pasture I followed them…"
  - The loft is Ch.11's (l.144, l.238). Avoid "the barley straw in the loft", which is a Ch.11 4-gram.
- **Alt (+2):** re-time the stranger: "In the month after the consultation" → "**When the snow was going off the high ground**". But the rag on his head (I-32) would then be about two months old.

### [W-10] S1 and S3 both close on Valens walking off to the animals
- **Audit:** Voice drift (scene-button / exit device; the bible tracks Valens walk-offs per chapter).
- **Evidence:**
  - l.112, end of S1: "\"Eat one and find out.\" **Valens left us for the mules.**"
  - l.510, end of S3: "\"Then I'll believe it,\" he said, **and rose, and went to the string.**"
  - S4 then opens (l.514): "While he walked the line in the dusk…"
- **Problem:** two of three section closes use the same move: the hard truth or the dare, then he leaves for the mules.
- **Suggested fix (−7):** end S3 on the line: "\"Then I'll believe it,\" he said." S4's opening already sends him to the string.

### [W-11] The belt thrown into the corner carries her father's watch
- **Audit:** Objects / characters stay themselves in heat.
- **Evidence:**
  - l.542: "I took hold of his belt where he had dropped it and **threw it into the corner**, so that his hands would find no work in it."
  - The watch rides in the pouch on that belt: Ch.6 l.288 "He dropped the watch in the pouch at his belt"; Ch.11 l.88 "his belt pouch"; Ch.12 l.132 "He untied the pouch from his belt".
  - Valens is "enormously careful with small objects (the watch)" (foundation §3). Mara is a conservator, and the watch is the book's countdown object (foundation §4f.5).
- **Suggested fix (+3):** "…and **put it out of reach in the corner**, so that his hands would find no work in it."
- **Cascade risk:** none. The watch stays off the page here, as planned.

### [W-12] CASCADE: outline Ch.16's Delphi farewell no longer fits the page as written
- **Audit:** Plot threads / outline consistency (no Ch.15 edit needed).
- **Evidence:**
  - l.16: Kallia tells the runner, "with half the lane listening", that Mara is "Gone to Kirrha at the turn of the month and onto a boat for home".
  - l.18: Kallia packs Mara's bag; Mara leaves before light.
  - l.344: Valens: "Delphi's put you on a boat. Leave yourself on it."
  - l.354: Mara imagines Kallia telling Euthydikos's man "the Syracusan had sailed".
  - l.46 and l.598: "my himation" is with her on the mountain. That is the Ch.7 brown himation, "the girl's" (Ch.7 l.24–28), her only one.
  - Outline Ch.16: "**Delphi, autumn:** Kallia's farewell. **NON-NEGOTIABLE:** Kallia gives Mara the borrowed himation from Ch.7 … A sweep of the threshold and the broom put away. **Film (named frame):** Mara photographs Kallia's lamp on the sill in morning light."
- **Problem:**
  - The farewell needs Mara inside Kallia's house in daylight, in a town that was told in spring that she had sailed.
  - The "gift" needs a himation Mara has been wearing for five months.
  - The frame and the beat are both NON-NEGOTIABLE in the outline.
- **Suggested fix (outline patch before the Ch.16 writer runs; 0 words in Ch.15):**
  - Stage the farewell as **covert**: the string comes down by night on the way to Kirrha; Mara is in at Kallia's gate before light and gone by full day. The lamp on the sill is at first light.
  - Re-cast the himation beat as **Kallia refusing it back**: Mara folds it to return it, and Kallia sweeps round it. The gift is made by not taking it.
  - Alternatively, Ch.16 shows Mara leaving it at Kallia's in spring. That would need one Ch.15 clause, which is not recommended.
- **Cascade risk:** foundation §4 row 16, bible Kallia card ("Ch.5–16"), ENTITY plan "parted Ch.16".

---

## INFO (polish / tracking / cascades)

**The cave backfill (CH13-7)**
- **I-01** The flashlight's history holds, line by line:
  - Bought Ch.2 l.137 ("because Fenn had wanted a better one").
  - Slide/thumb switch: Ch.3 l.139 "thumbed the flashlight on", which matches l.32 "slid the switch forward".
  - Already "a yellow oval" in May (Ch.3 l.121), so "yellower than it had been in May" ✓.
  - Switched off "to save the batteries" (Ch.3 l.127).
  - **Last lit Ch.5 l.3** (the night descent: "I found a wall with the flashlight… until I put it out").
  - Hidden at the bottom of the duffel: Ch.5 l.421, Ch.7 l.24, Ch.8 l.24. **Kept from Valens in Ch.6** (l.18, "I had let him burn his pines rather than have him see it"), so l.44 is his first sight ✓.
  - Battery wear is plausible: under an hour of total use on 2 AA alkalines, plus a cave in late winter (cold sags output).
  - The new description (l.128: gray plastic, ridged barrel, about a hen's egg in weight; Energizer bunny packaging, 1989– ✓) conflicts with nothing.
  - A soft irony to keep, not fix: the "better flashlight" Fenn wanted turns out to be a light plastic two-cell.
- **I-02** "since then, four months, not a word about the light" (l.50): from the 8th of Bysios (about Feb–Mar) to July is 4–5 months ✓. l.126 "The light in the cave," is the first word about it ✓.
- **I-03** The crack's geometry. Defensible; recorded for the tracker.
  - Ch.3 l.123 (May 1998, before the door breathed): "The flashlight went into it four or five feet and found a bend. Beyond the bend the beam ran on into black."
  - l.34 (AD 71): "The beam reached past the bend and stopped a yard beyond, on a face of gray stone that closed the crack from wall to wall."
  - So the same view shows open black in 1998 and a wall in AD 71. l.38–40 ("Did it ever go on?" / "Once.") owns it as her observation, and 1,900 years of cave change covers it.
  - Ch.6 l.6/l.492: she knelt *at* the bend in torchlight with the torch behind her, and her fingers reached "as deep as they would", short of a yard. So "whose far end had always been black to me" (l.34) holds.
  - **Tracker:** record the AD 71 back wall a yard past the bend. Ch.42–44 never return to the Corycian crack (bible: "no later chapter reopens the Corycian question").
- **I-04** Who waited for whom.
  - Ch.14 l.144, Kallia: "He's gone down for the mules … **You're to wait for him** at the bottom of the climb."
  - l.24: "**Valens had been waiting** below the cliffs on the morning that followed".
  - He went down to the Kirrha-road yard and back up, so she should be first. Optional (0): "Valens **came up** below the cliffs on the morning that followed, with two mules…"
- **I-05** Ch.14 l.134 planned "my fingers on the crack". In daylight she uses the beam instead. That is a change of method, not a contradiction ✓. "with two mules" agrees with Ch.14 l.136 "with Valens and the mules" ✓. "Keep to the inside at the third turn" agrees with Ch.6's short zigzags and Ch.14 l.146's "short turns" ✓. Harvestmen overwintering in clusters in caves, and moonmilk as "old bread", are both accurate ✓.

**History, world and 1998 facts**
- **I-06** The dust map, l.274–276: "the coast goes round from it to Puteoli … 'There?' / 'Further up. There.'" Coming round from the heel, Pompeii lies *before* Puteoli, so "Further up" reads as north of a mark that is already at Puteoli. Optional (0): "**Not so far.** There."
- **I-07** l.280, "They elect two magistrates a year": Pompeii elected two duoviri and two aediles. Optional: "They elect their magistrates every year…" (−1). The bakers' endorsements (*pistores*) ✓; temple at the forum's head ✓.
- **I-08** l.452, the Italian Market "ricotta … still warm, and it had squeaked the same": fresh ricotta (a whey cheese) is soft and grainy and does not squeak. Fresh curd and very fresh mozzarella do. Optional (+3): "passed me **a knot of mozzarella** across his counter". The memory obeys CP2-2: triggered by the squeak, it goes back into the scene.
- **I-09** l.242, "on a strip as long as your arm": a 36-exposure roll (foundation §4f.2) is about 1.6 m. Optional (+1): "**as long as you are tall**".
- **I-10** l.406, Felix: "Everybody from Syracuse comes through Corinth, or round by the cape…". A Kirrha harbor boy would know that western ships come straight up the gulf, and that the cape-or-road choice is for ships bound into the Aegean. It reads as a boy's bluster that Mara answers with "Another way", so it can stand. Optional cut "or round by the cape, and nobody goes by the cape if he can pay for the road" (−17), if the editor wants his geography clean.
- **I-11** l.326, "Celer's chose a road for it.": this reads as a dropped noun (dialogue-polish's own recast). Optional (+1): "**Celer's men** chose a road for it."
- **I-41** These all check out:
  - The AD count: 1998 − 71 = 1,927 ✓. "Twenty-six, and some months" from July 71 to May 1998 ✓.
  - Dionysius Exiguus about 525, "half a thousand years after" ✓. "wrong by four years, most likely" ✓.
  - The crucifixion "forty years ago or so" (AD 30–33 → 38–41) ✓. "Titus has just burned it" (Aug–Sep 70) ✓.
  - Hero of Alexandria's self-opening temple doors (fl. c. AD 60) as sailor's hearsay ✓.
  - The Castalian spring fenced against rockfall ✓; Delphi ruinous and ticketed ✓; Grand Canyon mule rides ✓; the snowplow ✓.
- **I-42** l.376, "snowmelt" at the seep in July, against l.14 "since the snow left the high ground": the pasture is clear while summit gullies hold old snow (Ch.3 l.91), so this is plausible. Pass.
- **I-19** Marriage, l.594: "Here you say it before witnesses, and then everybody eats. Corinth has clerks."
  - Greek practice: *engyē* before witnesses, then the *gamos* feast ✓.
  - Roman practice: consent, the *deductio* and a feast; no registration was required, so "Corinth has clerks" works as his joke ✓.
  - **Downstream note (not Ch.15):** a freedman and a peregrine woman without *conubium* make a marriage *iuris gentium*. Under the *lex Minicia* the children take the lower status. Ch.18 and Ch.24 onward should not have anyone call Lucius a Roman citizen by birth without a plan.

**The bargain and its cascades**
- **I-20** The brother's suit. l.306: "I'll stand up in the brother's court for his sister **when it's heard**", and l.326: "In that court I'll have the brother's men on the benches round me". Both imply a hearing at Corinth. Canon (ARCH-5, foundation §3/§11.5) hears it in **Rome, spring 74** (Ch.22). This is Valens's expectation, not a contradiction, but Ch.16 or Ch.21 must register why the hearing moves to Rome.
- **I-21** Ch.18. l.340, "My wife. The porter will ask, and the brother, and his cook…": they live as a married couple all winter. The quay wedding (outline Ch.18) then has to be motivated beyond "the captain wants a married couple": for example, he wants witnesses, or Valens wants it true. Also, foundation §6e / voice-dna §5 "Ch.16–18 the Corinth winter: yearning without sex" must be read as *no on-page heat*, not chastity. A man and his "wife" share a room in the brother's house.
- **I-22** CH12-2. "The book with my name in it" (l.298) agrees with Ch.12 l.200. Outline Ch.17 still lifts a "bronze-and-wax diptych". Ch.17 must take a leaf or extract from the book, or the outline must change.
- **I-23** The bowl thread is closed (above). Euthydikos's "bean-sheller off his stool by the bay tree" agrees with Ch.9 l.54 and Ch.13 l.226 ✓.

**Knowledge flow**
- **I-16** Who knows what after Ch.15:

  | Who | Knows (new in Ch.15) | Does NOT know |
  |---|---|---|
  | Valens | 1998 by the Judaean count; Philadelphia "Further than Asia"; the cave was a door for one afternoon; flashlight and camera shown working; Pompeii as a place ("In Campania…", l.272); a door among the tombs; she means to "go home" through it | **Pompeii's fate** (l.282) ✓. **Believes only the flameless light** (l.498) ✓ |
  | Felix | Corinth in autumn, winter there, a ship in spring, "Italy" (l.382–386); "He comes." (via Valens) | flashlight (never seen ✓), 1998, Pompeii |
  | Mnason | "your man" (his own assumption, l.480–488) | everything; asleep across the hollow at noon (I-17) |
  | Kallia | that Mara is going up the mountain ("you'll milk for your bread", l.18) | Pompeii, the bargain |
  | The Corinthian | a tall foreigner with "something heavy and bright inside her clothes" (seen in Ch.12 l.56) | that she is on Parnassus (Kallia's story) |

- **I-17** Mnason at noon is "in the shade of his hurdles" (l.116). The fold is "on the floor of the hollow" and he "crossed the hollow toward our hut" (l.68), so he is across the hollow and asleep. That is plausibly out of earshot of "Pompeii". Optional (+3): "in the shade of his hurdles **across the hollow**".
- **I-18** No-foreshadowing lines checked, each passing:
  - l.282: AD 79 as present thought, once, in fresh words (voice-dna §0.3).
  - l.354: imagination in the present scene.
  - l.366: "Then I'll wait outside it" (dialogue; an intention).
  - l.508–510: "Suppose you see it open?" / "Then I'll believe it" (a conditional).
  - l.214: Delphi's ruin is world history, not her outcome.
  - l.296: "I had not thought he would be kind about it" faces backward.

**Bridge to summer**
- **I-31** l.16: Kallia tells the runner in public that Mara left "at the turn of the month", while Mara is still under her roof that day. The lane's silence is implied, and Ch.12 l.360 / Ch.13 l.12 have Kallia holding the whole story. Pass, but the Ch.16 writer should know the lane is complicit.
- **I-32** The runner's "rag tied round his head" a month after the camera blow (Ch.12 l.58, l.72) is plausible only for a slow wound. If W-09's alternative is taken, change it to a fresh scar above the ear.
- **I-33** Pasture geography is consistent:
  - the hollow on the summit's flank above the plateau, with firs on the western ridge (l.8, l.476);
  - the cave "on its opposite edge … against a low brow of cliff" (l.22), which matches Ch.3 l.93 and Ch.12 l.352 "Above the cave. Up there you see a man coming a whole morning off.", answered at l.514;
  - transhumance on Parnassus (huts, folds, rennet, a winter at the gorge foot) ✓;
  - the shepherd bed of forked stakes, poles, bracken and fleeces ✓.
- **I-39** Figs:
  - The sawn-off jar is Ch.11 l.34; the Caunian cutting is Ch.11 l.190; "When the summer's done" (Ch.11 l.194) = "End of the summer" (l.104) ✓.
  - Green and hard in July ✓. Fig-sap curdling (Homer *Il.* 5.902) ✓. The latex blistering lips ✓.
  - The tree "two hands taller" ✓.

**Pregnancy**
- **I-15** l.572 is risk-awareness only. It implies no conception, so canon is safe: Lucius summer AD 74, revealed end of Ch.20, about six months pregnant at the spring 74 trial. voice-dna §5 permits it once and forbids a narrator resolution. Cascade: two-plus years of lovers before a conception about autumn 73 needs no explanation. A plain body fact in Corinth (her bleeding comes) is optional and would not count as "resolving" the Ch.15 thought. Leave it to the architect.

**Voice and register**
- **I-44** Heat canon, checked:
  - No purple euphemism. No clinical terms ("had him in my hand", "drew him into me" are plain).
  - No metaphor-stacking. No temperature report ("which was worse, and better" and "it went through me" are borderline and acceptable).
  - Consent is explicit: "Here?" / "Here.", and her hand guiding his (l.570).
  - Valens speaks little and never compares. His stillness breaks (l.578).
  - The asides go quiet after "Here?". The teeth aside comes before it, as the outline places it.
  - Em-dash 0.
  - l.576's long sensory sentence (draft, heat, grit, fire, his breath) is the "senses widen" design (voice-dna §5), not a parts inventory, though it is close. Keep.
- **I-24** l.44, "the thing in my hand he left to me", shares a 4-gram with sample-05 l.4 (the camera in the fight). Optional (0): "**the light** in my hand he left to me".
- **I-25** sample-10 near-match by image: l.530 "Mnason built it to fit Mnason" against sample-10 l.2 "built for one small shepherd who did not move in his sleep" (the hut or bed sized to its maker). The collapse, the laugh and the careful hands are outline-mandated, so only this image is optional to vary.
- **I-26** l.134, "It's not warm": Valens's first verdict on a 1998 object is a short "It's [adj]", as in sample-08 ("It's alive") and Ch.6 ("Something's going in it"). Watch for a fourth.
- **I-27** l.368, "My hiccups had gone, somewhere in the course of it." closes S2 on the hiccup channel. It deflates a romantic button ("Then I'll wait outside it") and so earns its place. Keep, and note it in the bible as the one use.
- **I-28** Paragraph-final negations: 10 by script and hand (l.20, 24, 50, 88, 124, 296, 414, 526, 542, 572), about 1.3/1k. That is under the ≤1.5 watch. l.24 ("nothing said … that was not about the path") and l.50 ("he spoke of the path … not a word about the light") make the same move 13 paragraphs apart. Optional: vary l.50.
- **I-29** Props: the flashlight is handled about four times in about 350 words (l.128–146) and the camera three times (l.234–256). Both are the outline's designed demonstration beats and under the gate. Pass.
- **I-30** The hoof is Valens's work twice (l.8, the lift; l.440, paring). The bible card asks for "always a different object". Optional: l.440 → re-tying a hobble.
- **I-45** The opening chain (l.6: "Bells came ahead of the light … behind the bells came the cold … behind the cold came the thyme") is a two-step anadiplosis. The rhythm gate is clean, and the sentence is the ledger's spiral. Pass.
- **I-12** Hut pronouns: l.516 "**His** rush baskets" and "At the back **he** had made a bed" follow a paragraph about Valens, but the hut, baskets and bed are Mnason's (l.530, l.584–586). Fix (0): "**Mnason's** rush baskets hung in a row…". The following "he" then resolves.
- **I-13** l.536: the Pentax "hung as it had hung **all afternoon**", but she bathed "all over" at the seep (l.376). Optional (0): "all evening".
- **I-14** "breastbone" ×3 (l.234, 536, 542). Optional: vary l.536.
- **I-37** Teeth surface once (Valens's) ✓, not as an introduction ✓ (foundation §3 chaos; voice-dna §3b.5).
- **I-34** l.272 "below a mountain they grow wine on" plus the verse's "mountain of vines" (Ch.13): the Ch.19 anchor ("a fine mountain for vines", at-risk 1) must be worded so it doesn't read as Valens quoting Mara's Ch.15 description back at her.
- **I-40** voice-dna §5's table lists Ch.15's period material as "the olive-wood rope bed … sheep-smelling blanket". The page's forked-stake pole bed is better, because it avoids a sample-10 lift. Sync the table.

**Syncs and pipeline**
- **I-35** **Bible lag**. "At-risk after Ch.15" and the Mnason card quote the Writer's page. Sync them to this one:
  - "Was it ever further?" → page "Did it ever go on?" (l.38)
  - "Then don't burn it" → "Don't burn it, then," (l.152)
  - "a door that is only a picture of a door" is **not on the page** (page: "the door I want", l.280)
  - "No shipmaster takes on a woman alone. He'll take a wife." / "At the gangway." → "That's for the shipmaster, at the gangway." / "He asks it before he asks the fare," (l.332–336)
  - "It's lower than me" → "Mnason built it to fit Mnason" (l.530)
  - "as a man learns a road he means to take…" → "learned … meant" (l.570)
  - "the scene's one comparison" is true only after W-03
  - Mnason card:
    - "sleeps like the dead" → "sleeps through anything" (l.66)
    - "It makes no odds what." → "…so it isn't sad. Sad, she holds it back." (l.56)
    - "Tastes of kid," / "You can taste it." → "Kid," he said, chewing. "Right through it." (l.448)
    - the dog "was cursed for it" → Mnason: "I'll have your hide for a pail" (l.494)
  - Walk-on note: the Corinthian now has a quoted line (l.14); add the pitch grandmother (l.374).
  - Counts: 7,914 / 30.3% → **7,787 / 33.3%**.
- **I-36** **Pipeline note (root):** the echo scan's voice-bank pass missed W-05's 6-gram, which is bounded by stop words. Proposed change to `tools/tic_report.py`: in the sample scan, accept stop-word-bounded runs of 6 or more words.

---

## Word ledger (recommended WARN fixes)

| Fix | Δ words |
|---|---|
| W-01 (l.118 −6, l.220 −3, l.234 −7, l.252 −6, l.282 −7) | −29 |
| W-02 | −8 |
| W-03 | −13 |
| W-04 | −13 |
| W-05 | +1 |
| W-06 | +3 |
| W-07 | 0 |
| W-08 | −3 |
| W-09 (clause) | +15 |
| W-10 | −7 |
| W-11 | +3 |
| W-12 | 0 (outline) |
| **Net** | **−51 → about 7,736** (floor 7,300) |

- Dialogue-side edits: W-07 0, W-08 −3. The narration loses about 48, so the dialogue share edges up to about 33.4% (band 30–40).
- INFO extras, if taken: I-04 0, I-06 0, I-08 +3, I-09 +1, I-11 +1, I-12 0, I-17 +3.
- Re-run the echo scan, rhythm and tic gates after W-01, W-04, W-05 and W-09: all four introduce untested strings.

---

## SUGGESTED YAML PATCHES (for the entity-tracker UPDATE after the editor's fixes)

```yaml
suggested_patches:
  - entity: "meta.contradictions.CH13-7"
    action: "resolve"
    value: "Ch.15 l.22-50: the eighth-of-Bysios climb with Valens and two mules; the beam shows a back wall a yard past the bend; 'It was shut, as I had wished it'. (I-04: page has Valens waiting for her, against Kallia's 'You're to wait for him', ch-14 l.144; editor may swap.)"
    reason: "the forward constraint is met on the page"

  - entity: "meta.contradictions.CH12-7"
    action: "resolve"
    value: "camera shown to and handled by Valens (l.232-256); 'The boy says it was your father's.' (l.244) relays ch-12 l.252"
    reason: "outline Ch.15 beat 2 delivered"

  - entity: "meta.contradictions.CH14-4 / plot_threads.euthydikos-bowl"
    action: "resolve"
    value: "bowl let go: l.342 'I meant to winter in Delphi…'; l.344 'Delphi's put you on a boat. Leave yourself on it.'; l.354 'The priest's bowl could keep its lead'"
    reason: "Ch.14 audit I-17 closed"

  - entity: "meta.contradictions.CH12-2"
    action: "recheck"
    value: "'My paper … is in Corinth. The book with my name in it.' (l.298): agrees with ch-12 l.200; still against outline Ch.17's diptych"
    reason: "still open"

  - entity: "meta.contradictions.CH12-5"
    action: "narrow"
    value: "Valens attributes the road to Celer: 'Celer's chose a road for it.' (l.326); a Corinthian-voiced man with a rag round his head asks for 'the tall foreigner … something heavy and bright inside her clothes' at the lion spouts in the month after the consultation (l.14)"
    reason: "sender still inferred, not established"

  - entity: "knowledge_index.pompeii-name"
    action: "update"
    value: "knowers: Mara, Theano, Valens (told ch-15 l.268, as a place: 'In Campania. On the bay below Neapolis…'). NOT Felix, Kallia, Mnason. Pompeii's FATE: Mara only (l.282 withheld; canon Ch.37)."
    reason: "outline Ch.15 knowledge flow"

  - entity: "valens.knowledge"
    action: "add"
    value:
      - { fact: "Mara is from 1998 by 'the Judaean' count; Philadelphia is 'Further than Asia'", learned: "ch-15 l.160-180", method: "told_by:mara" }
      - { fact: "the cave was a door for one afternoon in May, then shut; she came out in October", learned: "ch-15 l.186", method: "told_by:mara" }
      - { fact: "the flashlight lights with no flame and is not warm; batteries run out and cannot be bought here", learned: "ch-15 l.32-44; l.128-150", method: "witnessed + told" }
      - { fact: "the camera 'keeps what it shows'", learned: "ch-15 l.238-242", method: "told_by:mara" }
      - { fact: "the door home is among Pompeii's tombs; she will 'go in by it'", learned: "ch-15 l.280; l.360", method: "told_by:mara" }
    reason: "Ch.15 knowledge acquisition; belief: ONLY the flameless light (l.498); disbelief otherwise holds until Ch.25"

  - entity: "valens.traits / valens.plans"
    action: "add"
    value: "shaves every few days at midday with his knife, by feel, no glass (l.118); agrees to testify in the brother's suit for archive access and the road (l.306); plan: Corinth before the autumn rains, winter there, sail in spring 'As man and wife' (l.326); Felix comes (l.358); 'Then I'll wait outside it' (l.366)"
    reason: "the bargain"

  - entity: "relationships.valens<->mara"
    action: "update"
    value: "lovers from Ch.15 (first union, Mnason's hut, July AD 71); to be presented as husband and wife in Corinth (l.340)"
    reason: "HEAT 1"

  - entity: "objects.flashlight"
    action: "update"
    value: "gray plastic, ridged barrel, thumb slide switch, about a hen's egg in weight; two cells, Energizer-bunny brand; beam yellowing with a brown edge (l.34, l.128-132). Last lit before Ch.15: ch-05 l.3. Seen by Valens: ch-15 (cave, noon). Felix: never."
    reason: "first full description"

  - entity: "objects.fathers-pentax-k1000"
    action: "add"
    value: "worn on its strap under the chiton all summer; strap has rubbed a raw patch on her breastbone (l.234, l.542); hung on a peg lens-to-wall in the hut (l.542); still no cap, rim dented"
    reason: "object state"

  - entity: "objects.valens-fig-tree"
    action: "update"
    value: "carried up on the dun in its sawn-off jar (l.18); 'two hands taller', broad lobed leaves, about a dozen green figs (l.82); ringed with stones against the mules; one fig bitten by Felix (l.600); Mnason refused a twig (l.70-80)"
    reason: "object state"

  - entity: "locations.corycian-cave"
    action: "add"
    value: "AD 71: the crack ends a yard past the bend at a sweating gray wall with moonmilk at its foot and a cluster of harvestmen (l.34); contrast ch-03 l.123 (1998: 'ran on into black')"
    reason: "I-03"

  - entity: "locations.high-pasture-hollow"
    action: "create"
    value: "a hollow on the summit's flank above the plateau; Mnason's fold (thorn hurdles, one ewe-wide gap) and his hut; a second hut lent to Valens (dry stone shoulder-high, fir-pole and turf roof, forked-stake pole bed with bracken and fleeces, broken ch-15); a seep with a cut basin above it; junipers along the upper rim; firs on the western ridge; troughs under the plateau's rim, half a day there and back"
    reason: "new location"

  - entity: "mnason"
    action: "create"
    value: "herdsman; about sixty; goatskin cap with the ears on; milks from behind at the fold gap; turns milk with kid rennet against his mother's fig; winters at his son's 'at the foot of the gorge' (son's wife from Amphissa); calls Valens Mara's 'man'"
    reason: "new named character (bible card exists)"

  - entity: "walk-ons"
    action: "create"
    value:
      - "corinthian-runner (rag round his head under his hat, Corinthian vowels; asks for Mara at the lion spouts; identity with the man Mara hit not stated) l.14"
      - "spring grandmother (hot pitch for legs) l.374"
      - "mnason's dog, son, son's wife, brother, mother (mention) l.454-466, l.494"
    reason: "Ch.15 walk-ons"

  - entity: "mara-reyes.physical"
    action: "add"
    value: "described as 'the tall foreigner' by the runner (l.14; first height descriptor); legs unshaved since May 1998 (l.374); raw patch on breastbone from the camera strap (l.234)"
    reason: "new body facts"

  - entity: "felix"
    action: "add"
    value: "both shins skinned (juniper fight, l.420); lips swollen from a bitten green fig (l.600); knows Corinth/winter/ship/Italy (l.382-386); wants the Isthmian boys' race (l.410, l.434)"
    reason: "Ch.15 state"

  - entity: "timeline_events"
    action: "add"
    value:
      - "8 Bysios AD 71: cave visit with Valens (back wall; shut)"
      - "the month after (about Theoxenios): the Corinthian at the spring; Kallia's public 'sailed' story; Mara leaves Kallia's for Valens's yard (gap to the ascent: W-09)"
      - "about May AD 71: up to the high pasture behind the mules"
      - "July AD 71: Ch.15's day; first union"
      - "planned: autumn to Corinth before the rains; winter there; sail spring AD 72"
    reason: "Ch.15 chronology"

  - entity: "plot_threads.contraception-thought"
    action: "create"
    value: "once, ch-15 l.572, risk-awareness only; no narrator resolution (voice-dna §5); does not imply conception (canon: Lucius conceived about autumn 73)"
    reason: "I-15 / W-06"

  - entity: "plot_threads.kallia-farewell"
    action: "flag"
    value: "outline Ch.16's Delphi autumn farewell must be covert (Kallia told the lane Mara sailed in spring); the Ch.7 himation has been with Mara since spring (W-12)"
    reason: "cascade"
```
