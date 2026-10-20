# Continuity Audit: Chapter 12 (run 2, per-chapter drift audit)

**Date:** 2026-10-20
**Mode:** MANUSCRIPT AUDIT. Ch.12 "The Kirrha Road" (post-disruptor) checked against Ch.1–11 as they stand on disk, the plan, canon, and the bible.
**Chapter reviewed:** `manuscript/chapters/chapter-12.md`
- Length: **4,946** prose words by `shape_check`, 4,959 by style_check, 5,129 by `wc -w` with the header. Target 5,600; the writer's own header range is 5,000–6,200.
- **184 prose paragraphs**, 2 breaks (after p60 and p116).

**Paragraph numbering:** `ch-12:pN` counts prose paragraphs only, the same convention as the Ch.6–11 audits. The title, the two HTML comments and the `* * *` breaks are not counted. p1 is "Lupus? By the Twins, it is…" and p184 is "A cart had stopped beside the ditch." File line numbers are given as `l.NNN` where they help.

**Read against:**
- outline.md: the ledger, row 12, and `## Chapter 9` through `## Chapter 19`.
- STATE.yaml: guardrails, canon, ARCH-1..18, AUTHOR-CP2-1..4.
- foundation.md: the Valens, Felix, Plautia and Celer profiles and §6 (history).
- voice-dna.md: §0, §1 (including VOICE UNDER PRESSURE) and §3b.
- character-bible.md:
  - the Mara, Valens, Felix and Celer cards and their Ch.11 and Ch.12 "as written" blocks;
  - the Ch.11 and Ch.12 walk-on blocks;
  - every at-risk and spent block (after Ch.1 through after Ch.12) and the at-risk table.
- voice-bank samples 01–13. Sample-05 (Ch.12's road) and sample-13 got the closest reading.
- ENTITY_STATE.yaml as committed (`last_updated_chapter: 11`). The tracker is adding Ch.12 in parallel, so every Ch.12 fact below comes from the page.
- The Ch.12 dialogue, hook and disruption reports, and the Ch.11 audit (C-01, W-03, N-02, N-11, N-12).

**Mechanical baseline** (`bash tools/check_chapter.sh 12`, re-run read-only): **ALL CLEAN.**
- Style: simile 1.0/1k, em-dash 0, foreshadow 0. Grammar 0. Rhythm 0.
- Show/tell: dialogue 26.9%.
- Voice-wear strict: clean. Tic gate: clean. Echo scan 0. Command echo 0.
- Narration counts: and-chains 5, credential asides 0, negation pivots 0, "So" openers 0.
- Metaphor: fig 1.8/1k, median sentence 10.
- Shape: CLEAN (`12 4946 2 27 10 dialogue punch`).

**My own sweeps:**
- Ch.12 3- to 5-grams against voice-bank samples 01–13 and every bible **Sample line**. One 5-gram lift was found (W-06).
- A structural comparison with sample-05 (W-07).
- A by-hand comparison of every introduction, look, exit and pause against the closed and spent registries in the bible (C-01, W-01, W-02, W-04, W-05, W-17, W-18).
- Phrase counts book-wide for "mule-man", "one blow", "the singer" and "[color] going [color]".

**Total findings: 51. CRITICAL: 1 | WARN: 23 | INFO: 27**

**Summary:**
- **The one CRITICAL is a closed device reopened.** p46 has Valens's eyes travel over "the rest of me … head to foot, and across the camera in my arms, and off it". That is the item-by-item look, CLOSED since the Ch.4 and Ch.5 audits, and it shares "the rest of me" with the Ch.5 line those audits cut.
- **Information flow is clean on every axis the brief named, with one gap.**
  - Mara's comprehension holds: she knows *Rudiarius* from books, unglossed, and follows Valens's plain Greek.
  - Felix learns nothing of Lupus or the arena. He is ahead with the goat when the names are said, and at the ford during the telling.
  - Valens's "You saw the month on it" is grounded in Ch.9.
  - The gap: nobody says how Celer knew to send men to the Kirrha road (W-11; ENTITY knowledge_gap still OPEN).
- **Plot threads:**
  - **Money gap CH11-3 is CLOSED on the page as an act.** Mara pays for the goat; the dead man's denarii cover the cake and Praxias's drachma (I-01).
  - **Celer's men:** two survivors run, having heard the name "Mara" (I-11).
  - **The Oracle goal:** "three days", allowlisted bridge use 1 of 3 ✓.
  - **The Pentax:** it survives, the cap is lost, and Valens and Felix have now seen it (I-12, W-20).
- **No foreshadowing ✓. No forward reach in the narration ✓.**
- **Voice:** Mara's level-2 rehearsal mostly holds.
  - One evaluative aside sits inside the fight (W-08).
  - She asks no question all chapter, as designed.
  - Valens's card is strained by an emerging maxim habit (W-03), a rebuilt silence (W-04) and the boot lace returning at the frame (W-05).
- **History and geography:** the Kirrhaean plain is described as olive country with terraces. Ancient tradition keeps that plain sacred and unplanted (W-16). The internal geography also wobbles ("rose off the plain" after an ambush already above it).

**Word ledger for the proposed fixes:** about **−58 words** (W-20 excluded, since it is the orchestrator's call).
- The chapter would land at about **4,888** by shape_check. That is further under the writer's 5,000 range floor; there is no per-chapter floor (I-02).
- Dialogue rises slightly, to about 27.1%, because most cuts are narration.
- p1 and p184 are untouched, so the ledger signature (`dialogue` → `punch`) is unchanged.

---

## Scorecard by category

| Category | Result |
|---|---|
| (a) Ledger / beats | **PASS.** **Structure:** In medias res, after Ch.11 Chronological and before Ch.13 Parallel ✓. Internal shape *violence first, story after* ✓. **Open:** p1 is in quotes → `dialogue` ✓. **Close:** p184, 7 words, a one-sentence closing paragraph (allowed for Ch.12) → `punch` ✓. Concrete, no aphorism ✓. **Breaks:** 2 ✓. **Dialogue:** 26.9%, inside the 25–35 band ✓. **Gear:** median 10 (low) ✓. **Length:** 4,946 against 5,600 (−12%; I-02). **Beat 1** NON-NEGOTIABLE: three men; short, ugly, mostly unseen; the Pentax swung in panic; the cap lost; one dead, two run ✓. No flash ✓. **Beat 2** NON-NEGOTIABLE: his hands shaking at the fall, held still (p65–p72) ✓. **Beat 3** NON-NEGOTIABLE: the telling while washing, in chronological order. The rudis, Nero's games, Plautia, Celer and the dowry are all there, and "I was a good bodyguard. That was the use of me." is said once ✓. The knowledge path is one passage (p103–p111) ✓; see W-11. **Beat 4:** Felix carries the goat home; the body is left to the road ✓. **Anchor** ✓. **Chaos:** onion memory at the stream ✓; Mara's unprompted memory absent, as briefed ✓. **Subtext:** Mara asks no question in the whole chapter (every "?" is someone else's) ✓. **Opens toward Ch.13:** "It was three days to the seventh of Bysios." (p180) ✓. |
| (1) Character consistency | **CRITICAL ×1 (C-01). WARN ×6:** W-01, W-02, W-03, W-04, W-05, W-19. **Valens:** the scar on the back of the right hand (ch-06:p42; ch-09:p169) agrees with p4, p11 and p71. p71 feels "the marks where each stitch had gone in" without re-quoting the ladder ✓. Boots and laces (ch-07; ch-11:p225) ✓. A knife carried at his back (ch-11:p54) fits "it was not his own" (p36) ✓. No simile in his speech ✓. Bare "No." 1 (p164), at the cap set by the Ch.11 audit ✓. Bare "Felix." 0 ✓. Walk-offs 1 ✓. His first spoken "Mara." (p25) is untagged and its own beat ✓ (ch-11:p269 "He had it, and he kept it."). Backstory against foundation §3: rudis at Corinth in Nero's tour (66–67) after "five years in the sand"; Celer a legate on the proconsul's staff; two years as sworn bodyguard; the post lost with the freedom (late 67); the frame "The year of all the emperors, in the summer" (69); flogged; tablet seized; over the wall; across the gulf; the Kirrha quay "that winter" (69–70); the mules "off a Corinthian dealer" (agrees with ch-06 "They came from Corinth" and Praxias's "His mules are", ch-11:p13) ✓. The one plan departure is W-21. **Felix:** about twelve ✓ (the Calf-Bearer "had been twelve"). Stacked questions ✓. Never says he is afraid ("It was that crust") ✓. Fewer lines than Ch.11, as briefed ✓. "nobody" 0; "already" 0; exits with line + tag + "and" 0 ✓. See I-06 and I-07. **Mara:** her Greek is uncontracted in every line (checked one by one). No English anywhere ✓. Credential asides 0 ✓. Teeth 0. Laughs 0. **The walk-ons** are compared against every earlier introduction of their kind: W-01. |
| (2) Timeline | **PASS.** Ch.11 closed on "the day after tomorrow, at daybreak" (ch-11:p278). Ch.12 is that day: Kirrha in the morning (p118, p120), the fight on the way back, the fall in the afternoon ("my feet in the sun", p77), the climb at evening ("good evening", p166), and the gulf "still held some light" at the close (p183) ✓. **Travel:** Delphi to Kirrha and back is a day's round trip for a loaded string. That matches Ch.11's "to Kirrha for oil or salt fish and back up" (ch-11:p69) and the lamp seller's "If you don't stop" ✓. **The cart:** the son runs back to Kirrha and the headman comes with a cart while they wash, talk and climb, which is plausible at two to three hours ✓. **The god's day:** "Three days" (p171) and "three days to the seventh of Bysios" (p180). This agrees with Ch.14's plan ("Celer's men were on the road three days ago") and with Ch.11's arithmetic (about 13 days from the yard's first day) ✓. "Next month would do as well" agrees with Praxias's "The god sits every month now till the winter" (ch-11:p155) ✓. **Season, early spring AD 71:** plane buds "just broken", snow water in the stream, "the first boats of the year" with "new pitch still soft". This follows Ch.10's sea closed all winter and Ch.11's late winter ✓. The killers come on the first Lechaion boat, which explains why Celer's men arrive only now, although the notice reached Delphi "after the snow" ✓. **Since the arrival:** October AD 70 → early March AD 71, about five months. Not stated on the page and not contradicted ✓. One logic point about traffic: W-15. |
| (3) Information flow | **WARN ×1 (W-11). Otherwise PASS.** **Mara's languages:** "*Rudiarius*" is Latin she knows from books, left unglossed (voice-dna §1, pressure rule) ✓. The telling is in Valens's plain Greek, which she has followed since ch-06 ✓. "By the Twins" is a period oath ✓. **Who knows Valens is Lupus:** Mara, now confirmed by a stranger and by his own telling. The graybeard's party knows only "mule-man" (W-14). **Felix:** he leads the string from the front and is out of earshot for "Lupus" and *Rudiarius* ("Go on up to the boy", p10). During the telling he is down at the ford (p89). He knows that Valens killed a man, that Mara hit one with "my father's" silver-looking thing, and the cover story. He does **not** know the arena or Corinth, which keeps the bible's "Ch.21's lanista is where he hears of Corinth" ✓. His "Spicula … After the murmillo. The one the emperor gave a house to." (p154) is arena-mad lore (Suetonius, *Nero* 30), not knowledge of Valens ✓. **Valens's knowledge:** "You saw the month on it." She read the copy, which ends "posted at Corinth in the month Dadaphorios" (ch-09:p169), and he saw her there (ch-09:p197) ✓. "A copy came up here after the snow, with the oil carts" agrees with "With the oil from Thebes. First carts since the snow" (ch-09:p186) ✓. "I saw it too" is consistent with the Ch.11 reading reveal: from Ch.12 his literacy is a plain fact between them ✓. **The graybeard:** he passed the body and says "Somebody's had his purse" (the cut thong is visible) ✓. **Kallia:** Mara will tell her "the whole of it", with Valens's leave. That sets up Ch.14 (Kallia puts Valens across the doorway) ✓. |
| (4) Plot threads and objects | **WARN ×5:** W-09, W-10, W-12, W-13, W-20. **Money (CH11-3): CLOSED as an act.** "I paid it myself, out of my rag … and the rag was thin after it" (p120); then "This would. It would buy the cake, and Praxias's drachma, and leave plenty over." (p134). Valens pays for the sprats (p120). The goat purchase is not a counted-down haggle (Ch.11 N-12) ✓. "three drachmas" is not on the page, as the bible asked ✓. **The watch:** one clause, "Through the leather the watch was going." (p64). That is the bible's allowance before Ch.18; the pouch is returned at p133 ✓. **The sherd:** "in my belt, against the knot of the rag" (p175) ✓. **The Pentax:** the strap under her clothes (p8, p27); swung (p27–p28); the cap lost in the oil (p31, p56). Inspected: hair in the rewind crank, the filter ring dented, "The glass was whole." (p78) ✓. "The camera had no flash" (ch-03:p57) is respected ✓. Why it was on her: the lodgers in rows and the duffel under the stair (p79). This agrees with ch-08 "my bag under the stair" and with Kallia's crowded house before the god's day (Ch.14 plan) ✓. The flashlight is left in the duffel ✓. **Celer's men:** the three came off the Lechaion boat ("I told them about it the whole crossing", p7; p120's boat) ✓. **The Oracle goal:** the goat is bought and carried, Valens keeps to the plan ("Three days"), and the precinct's crowd is his safety (p173; I-03). |
| (5) World / history | **WARN ×2:** W-16 (the sacred plain), W-18 (Nero as "the singer", a third time). **Checked and correct (I-23):** the rudis and *rudiarius*; Nero's Greek tour (66–67) and the freedom of Achaea (late 67); a legate on the proconsul's staff; the post lapsing during the freedom; 69 "of all the emperors"; dowry retention for adultery ("you keep a share of what she brought", *retentio propter mores*); the husband keeping the child; manumission recorded by a magistrate and a lanista's copy; Isis at Kenchreai; the Craneion; Vespasian denarii new in early 71; Spiculus; the Calf-Bearer in the old Acropolis museum (correct for 1998); Orestes at Delphi; first sailings in early spring. The coin wording is I-04. **Kirrha/Itea:** Kirrha is the harbor with a mole; Aigion lies across the gulf; Itea is never named (correct, it is modern) ✓. |
| (6) NO FORESHADOWING | **PASS.** The gate reads 0, and a manual read agrees. Nothing in the narration reaches past the bend at dusk. "I'll stay up the summer." (p174) is speech and a plan. "It was three days to the seventh of Bysios." is present reckoning. The last image is present-scene. The Lechaion boat at p120 is narrated after the fact, inside the chapter's own day. It is not a pre-announcement. |
| (7) NO TICS / spent moves | **CRITICAL ×1 (C-01). WARN ×10:** W-01, W-02, W-03, W-04, W-05, W-14, W-17, W-18, W-19, W-23. **Clean:** command echo 0; "said/told the [non-listener]" 0 (Felix "telling the mules" is animal address and is not counted); a held silence measured by something moving 0 (p99 is bare, but see W-04); narrated non-answers 0; "Then…" speech openers 0; hinge openers 0; "the one / the only" 0; "He meant…" 0; "before I had [verb]" 0; the [color]-of-[thing] shape 0; "Whoever [made] it had" 0; absent-workman verdict 1 (the green darn, at cap); the depth-to-joint frame 1 ("up to the ankle bones", cap 2); lying-awake coda 0; cloth smells 0; the stranger-freeze 0; walk-on holding an object to the eye 0. |
| (8) Voice-bank lifts (zero allowed) | **WARN ×2:** W-06 (a bible sample line, verbatim 5-gram) and W-07 (sample-05 by structure). Sample-10 shares only "of olive wood" (a bed against a stick, no shared image). Sample-13's "I put the cap back on the lens" is now impossible on the page (I-14). |
| (9) Memories (AUTHOR-CP2-2) | **PASS.** Mara: none. "It was my father's" is a fact, not a memory. The Ch.1 echo of the strap winding is unpointed (I-22). **Valens:** the onion memory surfaces once. It is triggered by the crushed plant (p75), unexplained ("They hung them under the eaves. In strings, to dry."), and goes straight back into the scene (the knife, p76) ✓. |
| (10) Voice drift | **WARN ×2 (W-03, W-08); INFO ×3 (I-06, I-07, I-08).** **Pressure level 2** (voice-dna §1): the fight runs in plain verbs and short sentences. "Wine. Sweat."; "Mara." is untagged; the senses narrow to sound ("The ditch hid them. I heard them."). One evaluative clause survives inside the rolling-cap sentence (W-08). **The asides return** at the stream in a sensible order: materials (camera, cloak, "Cold water. Hot would have set it."), then comparison (the Calf-Bearer), then aside (Orestes). **Valens:** his longest speech so far is a witness's chronology without self-pity ✓. The maxims are W-03. |

---

## PRIORITY: ENTITY_STATE conflicts (processed first)

Committed ENTITY covers Ch.1–11. The open flags were reviewed: CH1-2, CH1-3, CH2-1, CH2-3, CH2-4, CH2-5, CH3-1, CH3-2, CH3-3, CH4-2, CH4-3, CH4-4, CH5-3, CH5-4, CH6-5, CH8-2, CH10-4, CH10-6, CH11-3, CH11-4, and post-patch P1, P3, P4.
- **CH11-3 (the money gap) is auto-resolved by the page.** See I-01 and the patches.
- **CH11-4 (Felix knows the trip and the watch):** consistent. Felix is not present when Mara holds the pouch at the fall. No action.
- **CH5-3 (film frames):** no frame is shot in Ch.12; the camera is swung, not used. Still open as plan-vs-page; no Ch.12 action.
- **knowledge_gaps, "How Celer learned (autumn AD 70) that Valens was in Phocis":** Ch.12 was the planned place to close it, and the page does not. This is W-11.
- **None of the others touches a Ch.12 fact.**

---

## CRITICAL ISSUES (must fix before proceeding)

### [C-01] The item-by-item look, reopened (a registered CLOSED device)
- **Audit:** NO TICS / closed-device registry. The bible's At-risk after Ch.1 says "a third use anywhere in the book is a defect". At-risk after Ch.5 says "item-by-item look … CLOSED — any later look at a garment is one object or a duration, never a sequence". The Ch.4 audit (C-01) and Ch.5 audit (C-01) treated this frame as CRITICAL.
- **Evidence:**
  - ch-12:p46 (l.96): "**He ran his eyes over the rest of me regardless, head to foot, and across the camera in my arms, and off it.**"
  - The cut Ch.5 instance (ch-5 audit C-01): "His eyes went over my trousers and then the rest of me". Same frame, same "the rest of me".
  - The two live uses: ch-01 "Her eyes went from the pencil to the garbage bag held against my chest."; ch-03 "pointed at the slope above us …, and then at the bag, and last of all at me".
- **ERROR or INTENT:** the CONTENT is intent. He checks her for wounds, and the reader should register that he sees the camera and does not ask. The FRAME (a gaze moving from item to item) is the error. The camera notice is already carried by his "Is it broken?" at p80.
- **Suggested fix:** p46 → "**He looked for blood on me anyway.** Then he dropped into the ditch. …" (−14). One duration, no sequence. "looked for blood" / "for blood" have 0 uses in Ch.1–12 and the voice bank. It avoids Ch.7's "looked me over".
- **Cascade:** the disruptor's gaze count ("Valens's gaze on Mara" 2) drops to 1. The bible's Ch.12 Valens block quotes neither form. Nothing in plot.

---

## WARN ISSUES (should fix)

### [W-01] The talker's introduction is assembled from Ch.5's two walk-on introductions
- **Audit:** Bible, At-risk after Ch.11 FINAL: "Body facts and introductions do not travel between characters … Every new introduction is compared with every earlier one of its kind".
- **Evidence:**
  - ch-12:p2: "now he **fell in at Valens's left side** as though he had been asked. He was short and sunburned, **in a good brown cloak** with the dust of the plain on its hem."
  - ch-12:p7: "He kept pace beside us, **thumbs hooked in his belt**."
  - ch-05:p24, the guide: "He **fell into step beside me** talking, a lean, bandy-legged man **in a brown cloak**".
  - ch-05:p129, the square man: "planted himself in front of me **with his thumbs in his belt**. He was younger than I was, **with a good cloak** and a bad smile."
- **Fix:**
  - p2 → "…and now **he was at Valens's left side** as though he had been asked. He was short and sunburned, and **the dust of the plain was on the hem of his cloak**."
  - p7 → "He kept pace beside us **with his hands behind his back**." This also hides the knife hand, which pays off at p18.
  - p18 "from under the brown cloak" → "from under his cloak".
  - Net about +1. "hands behind his back" and "the hem of his cloak" have 0 prior uses.
- **Cascade:** p36's "The man in the brown cloak" goes under W-07. The bible's walk-on block ("a good brown cloak") needs a re-sync.

### [W-02] Mara's eyes-down beat, CLOSED after Ch.7
- **Audit:** Bible, At-risk after Ch.7 cycle 1: "Mara's eyes-down business, the chapter's subject in Ch.7: CLOSED after Ch.7."
- **Evidence:**
  - ch-12:p15 (l.34): "**I watched the stones in front of my feet.**"
  - The Ch.7 lesson and its uses: "Your eyes go there. On the ground in front…" (ch-07:p20); "my gaze on the ground in front of me" (ch-07:p63); "My eyes went to the ground in the lane and kept there" (ch-07:p183).
- **Fix:** delete p15 (−9). p14's low laugh runs straight into p16's "*Rudiarius*", which tightens the menace. Do not swap in "I said nothing", which is the narrated non-answer family.

### [W-03] Valens's gnomic present-tense maxims are forming a proverb habit
- **Audit:** NO TICS ("no proverb habit"). Valens card: "In Greek (Part One) he is flatly literal … No wry asides." Ch.11 audit N-02: "No crafted quip in Ch.12."
- **Evidence:**
  - **Ch.11:** "A fig that gives has gone to the wasps." / "A wasp likes a thing that keeps still." / "Chian are for men who've never had a Caunian." / "In a line a man looks at the back of the man in front of him." / "Paper gets taken off you,"
  - **Ch.12:**
    - p98 "They asked my name and I said Valens. **A quay doesn't ask twice.**"
    - p111 "**Whoever wants five hundred brings a rope.**"
    - p148 "**He had his robbers before you opened your mouth,**" (a deflating quip)
  - That is eight general-truth sentences in two chapters. Each is good alone. Together they make him a man who talks in sayings.
- **Fix:**
  - Cut "A quay doesn't ask twice." (−5). "They asked my name and I said Valens." already carries it.
  - Keep p111. It is load-bearing for the knowledge path.
  - Optional for p148: "**He'd made his mind up on the road,**" Valens said. This is plain report, not a quip (0 prior uses).
- **Cascade:** the bible's Ch.12 spent list ("A quay doesn't ask twice.") gets a re-sync. Ch.13's word-for-word repetition must not be framed with any saying.

### [W-04] p99 rebuilds Ch.11's "He was a while silent." in the same place in a telling
- **Audit:** cross-chapter echo of a beat in near-wording, which the 5-gram scan cannot see (CLAUDE.md 5c spirit). Bible: "A held silence is left bare."
- **Evidence:**
  - ch-11:p238 "**He was a while silent.**" sits before "Paper gets taken off you," which is his frame, unexplained.
  - ch-12:p99 (l.204) "**He was quiet for a while.**" sits before "Her brother took her home," which is his frame, explained.
  - It is the same beat at the same trigger, one chapter apart.
- **Fix:** delete p99 (−6). p97 ("The cold had my feet again…") already holds the gap, and p100's tag "he said" marks the restart.

### [W-05] The boot lace returns at the frame: the third chapter of Valens's lace, and the struck knot device's function
- **Audit:** Bible, At-risk after Ch.11 FINAL:
  - "The struck knot device … **A recast that removes a device checks that the replacement does not keep the device's function at the device's trigger.**"
  - "Valens is not to become the third character with a stopped-work tell".
- **Evidence:**
  - ch-12:p93 (l.192): "He sat on the lip of the pool with his boots in it. **One of his laces had come undone, and the end of it trailed in the water. He left it there.**"
  - Ch.7 had the broken, knotted lace. Ch.11 had the new lace (and F1 cut "The lace stopped at his ankle" at the freedom question). Ch.12 now has the lace undone and abandoned while he tells the frame.
  - The lace, as a barometer of his feeling about the frame, is back at the device's trigger.
- **Fix:** p93 → "He sat on the lip of the pool with his boots in it." (−19).
- **Cascade:** the bible's Ch.12 counts note ("knot near his hands 0 (his boot lace 'had come undone … He left it there.')") changes to "lace 0".

### [W-06] "a house on the Craneion" is a verbatim lift from a bible sample line (calibration only: 0 allowed)
- **Audit:** Bible at-risk table: "any phrase in a sample line in this file or in a voice-bank sample | 0 | calibration only". Script hit: the 5-gram "a house on the craneion".
- **Evidence:**
  - ch-12:p94 (l.194): "He'd bought **a house on the Craneion** he couldn't pay for."
  - PLAUTIA's sample line: "who keeps my son in **a house on the Craneion** with a nurse".
- **Fix:** "He'd bought a house he couldn't pay for, **out where the cypresses are**." (+2; 0 prior uses). The Craneion is the cypress grove (Pausanias 2.2.4), so the fact is the same and the wording is fresh.
- **Cascade:** Ch.16's Plautia must not use the sample line either (writer prompt note).

### [W-07] Sample-05's skeleton for the fight's end, by structure
- **Audit:** voice-dna §6. Bible after Ch.8: samples "leak by structure as well as by string".
- **Evidence:**
  - sample-05: "He got up and ran, and the other one ran after him, **and the one under the wheel did not get up.**"
  - ch-12:p35–p36: "…the big man dropped it and ran. … The one I had hit pushed himself off the stones and went after him … **The man in the brown cloak stayed in the ditch.**"
  - Same order: two run in sequence, then the dead one's stillness as a non-motion. The death is already on the page twice: p33 "and then nobody was" and p40 the foot.
  - The outline mandates the content ("one man dies; two run"). The third, redundant beat is the sample's.
- **Fix:** cut the last sentence of p36 (−9). p36 ends "There was a knife in his hand, and it was not his own."

### [W-08] An evaluative clause inside the level-2 fight
- **Audit:** voice-dna §1, VOICE UNDER PRESSURE level 2: "The asides die … She narrates only what hands and bodies do … no interpretation".
- **Evidence:** ch-12:p31 (l.66), the anchor sentence: "…past the mule's back hooves, past the big man's feet, **a great distance for so small a thing,** until it met the edge of the oil…"
  - The sentence is the chapter's one designed sight-narrowing, and it is good.
  - The clause is the narrator weighing the event: a dry aside at the height of the fight.
- **Fix:** delete "a great distance for so small a thing," (−8). The run of "past … past …" already gives the distance.

### [W-09] "Praxias wanted five drachmas." contradicts what Mara told Valens herself
- **Audit:** internal fact (Ch.11 to Ch.12).
- **Evidence:**
  - ch-11:p161, Mara to Valens: "To carry my question for four drachmas. And then for three and a half."
  - ch-12:p110 (l.226): "**Praxias wanted five drachmas.**"
  - Valens knows the last price, so her line misstates it to the one man who knows.
- **Fix:** "**Praxias wanted three and a half.**" (+1; 0 prior uses). It is still more than she had, so her point stands.

### [W-10] "Those three brought knives." against a fight with one knife and a stick
- **Audit:** internal consistency (scene to speech).
- **Evidence:**
  - ch-12:p111 (l.228): "Whoever wants five hundred brings a rope. **Those three brought knives.**"
  - On the page: the talker's knife (p18), the big man's olive stick (p11, p21, p35), and the third man's bare hands (p23). The reader has just watched the stick.
- **Fix:** "Whoever wants five hundred brings a rope. **Those three brought none.**" (0). The rope is the evidence, and the knife needs no plural.

### [W-11] The knowledge path does not say how Celer knew where to send the men (ENTITY knowledge_gap OPEN)
- **Audit:** Information flow. ENTITY knowledge_gaps: "How Celer learned (autumn AD 70) that Valens was in Phocis … (Ch.12's knowledge path)" OPEN. Rule 8 applies: plausible but unverified.
- **Evidence:** ch-12:p103 (l.212): "Last autumn a freedman of her brother's found me at the harbor … I said I wouldn't. **Inside the month that notice went up in Corinth.**"
  - The page implies the leak but never states it.
  - The men came straight to the Kirrha road on the first boat. A reader can ask how Celer knew the harbor.
- **Fix:** p103 → "…I said I wouldn't. **He'll have said where he found me.** Inside the month that notice went up in Corinth." (+7; 0 prior uses).
  - It is Valens's inference, plain and unsubordinated. It fits his card ("asks who saw").
  - It stays short of his mind-reading chaos, because it is probably right.
- **Cascade:** ENTITY knowledge_gap → RESOLVED (inferred by Valens, ch-12:p103). The Ch.16 Plautia scenes can confirm or complicate it.

### [W-12] The cracked jar is propped beside the body, which undercuts the robbery story Valens is building
- **Audit:** plot logic and objects; Valens's attention axis ("exits, who saw").
- **Evidence:**
  - ch-12:p49 (l.102): "the jar came off into his arms, and **he propped it in the angle of the wall, and it went on leaking there**."
  - p53: "That's what it was. A traveler with his purse cut."
  - p141, Felix to the graybeard: "We came on him … and came on up, because of the oil."
  - A muleteer's oil jar left by a corpse ties his string to the spot. The graybeard passed it, and the headman's cart is on its way.
- **Fix:** p49 → "…and the jar came off into his arms, and **he carried it to the terrace edge and tipped it over among the olives below**." (+4; 0 prior uses). The spilt oil on the road can stay: a spill is not an owner's mark, and the cap needs it.

### [W-13] Re-balancing one mule unbalances the next
- **Audit:** objects and Valens's animal competence.
- **Evidence:** ch-12:p132 (l.272): "He **moved a jar off the next mule's load** and roped it opposite the single one on the mule that had lost hers, so that she would carry level". With a jar a side, the next mule now carries one.
- **Fix:** "He **found a stone the weight of the lost jar** and roped it opposite the single one on the mule that had lost hers, so that she would carry level, and tried the knots with his weight." (+3; "found a stone" and "weight of the lost jar" have 0 prior uses). Balancing a load with a stone is standard packer's practice.

### [W-14] "mule-man" is now 4 book-wide, from three speakers plus the narration
- **Audit:** Ch.11 audit N-11 ("'Mule-man' is now 2 … No third speaker uses it."); voice-dna §1 address forms; the role-label rule in the bible's after-Ch.8 block.
- **Evidence:**
  - ch-06:p307 (the burner); ch-11:p157 (Praxias).
  - ch-12:p143 (l.294): "You've been in the thorns, **mule-man**."
  - ch-12:p166 (l.340): "each of them said good evening to **the mule-man** and got good evening back."
- **Fix:**
  - p143 → "You've been in the thorns." (−1).
  - p166 → "…and each of them said good evening and got good evening back." (−3).

### [W-15] Pilgrims leaving for the boats three days before the first consultation
- **Audit:** timeline logic (who is on the road and why).
- **Evidence:**
  - ch-12:p166 (l.340): "**Pilgrims came down from the town against us, going to sleep at Kirrha for the boats**".
  - Ch.11 established the flow: "going down while the pilgrims came up. There were more of them every day" (ch-11:p69). This is three days before the year's first consultation, when nobody has consulted yet.
- **Fix:** "**Traders** came down from the town against us, going to sleep at Kirrha for the boats" (0; 0 prior uses). The lamp seller in the same sentence fits the change.

### [W-16] The Kirrhaean plain is drawn as olive country with terraces; ancient tradition keeps it sacred and bare, and the page's own geography wobbles
- **Audit:** world and history ("historically accurate to a certain point"); internal geography.
- **History:**
  - The plain below Kirrha was Apollo's consecrated land after the First Sacred War. Its cultivation by Amphissa caused the Fourth Sacred War (Aeschines, *Against Ctesiphon* 107–113).
  - Pausanias, a century after this book, still finds it bare: the people will not plant trees in it (10.37).
  - ch-12:p183 (l.374): "**The whole plain lay under us, gray with olives**".
- **Internal geography:**
  - The ambush happens "between the terrace walls" (p9), off "the edge of the road … into the ditch below the terrace" (p21), with the walkers seen "**Far down toward the sea, where the olives ended**" (p54). That is a hillside above the plain.
  - Yet after the ford, "**The road rose off the plain in bends**" (p166), as if they had been on the flat.
- **Fix (keeps every beat):** put the olives and terraces on the foothills, where the fight already is, and make the plain the god's bare land.
  - p166 → "**The road went on up in bends**, stony, between walls." (0 prior uses).
  - p183 → "**The whole plain lay under us, bare and darkening, from the foot of the hills to the shore.**" (0 prior uses for "bare and darkening" and "the foot of the hills").
  - This also clears W-17. Valens's "This is the god's road." (p51) gains a literal ground under it, unpointed.
- **Cascade:** none earlier. Ch.5–11's olives are in the Pleistos valley and on the slopes below Delphi, which is correct. Ch.16's crossing from Kirrha should keep the plain bare.

### [W-17] "[color] going [color]", SPENT after its one use
- **Audit:** Bible, At-risk after Ch.5: "**[color] going [color]** (1, Ch.3: SPENT)". Ch.5 audit W-10 cut two more uses.
- **Evidence:** ch-03:p80 "yellow going toward orange"; ch-12:p183 "**gray** with olives and **going blue**".
- **Fix:** W-16's p183 wording removes it.

### [W-18] Nero identified by his singing for the third time ("the singer", SPENT)
- **Audit:** Bible at-risk table: "'the singer' (Nero) | 2 | Ch.5 guide: SPENT; name him or vary".
- **Evidence:**
  - ch-05:p46 "The singer," and ch-05:p50 "the singer?"
  - ch-12:p6 (l.16): "Corinth. **The year the emperor came over to sing.**"
  - The wording is new, but the device is the same: Nero known by his singing.
- **Fix:** "Corinth. **The year the emperor was in Greece.**" (−1; 0 prior uses). Valens's "He had the year right" (p86) still answers it.

### [W-19] "one blow" reaches 3 book-wide, as a two-chapter question-and-answer pair
- **Audit:** NO TICS ("any phrase recurring 3+ times across the book that is not an allowlisted motif is a defect"; the gate cannot see a 2-word phrase); Valens's evasion ("never says: anything about the men he killed").
- **Evidence:**
  - ch-11:p118 "with his fists, **with one blow**"; ch-11:p121 "Have you ever seen a man killed **with one blow**?" / p122 "No."
  - ch-12:p163–p164 (l.334–336): "**Was it one blow?**" / "**No.**"
  - The pair answers Ch.11's lie with the truth. That is a designed callback, which the bible records as DONE. But the phrase is now a three-time refrain, and his "No." gives Felix a detail of the killing.
- **Fix (orchestrator call):** p163 → "**Did he go down straight off?**" (+2; 0 prior uses). Valens's "No." stays true and keeps his one bare "No.". The irony survives without the catch-phrase. If the orchestrator keeps the callback, log "one blow" as at cap (3) and never used again.

### [W-20] The lens cap is left in the oil beside the corpse, against the concealment logic the chapter states
- **Audit:** plot logic and objects (a Chekhov risk).
- **Evidence:**
  - ch-12:p56 (l.116): "I went past where the cap lay in the oil, face up, its letters dark with it, and kept going."
  - ch-12:p79 (l.164), 23 paragraphs later: "The camera was the thing in that bag a thief would take first, and **the thing I could least explain to anybody who took it**".
  - A plastic disc printed with Latin capitals lies beside a murdered man, and the headman's cart is arriving (p184). The anchor gives it enormous weight. A careful reader will expect it to be found.
  - The outline mandates the loss ("the lens cap doesn't [survive]"). The bible logs "The cap is LOST … do not mention a cap."
- **Fix options (orchestrator):**
  - (a) **Recommended:** keep the staging. Add one present-scene clause at the end of p78 that shows Mara knows and lets it go: "**Its cap lay in the oil beside him, with the maker's name on it in letters nobody at Kirrha would read as a word.**" (+20; 0 prior uses for "Its cap lay" and "letters nobody"). It turns an author oversight into her choice and closes the thread rather than opening it. Never pay it off.
  - (b) Alternatively, p31 ends with the cap going "over the edge of the terrace into the olives below". That loses the oil image and p56; not recommended.
  - Either way, ENTITY records the cap at the scene, status LOST, `payoff: none (author decision)`.

### [W-21] The page changes Celer's legal claim from the foundation's, and Ch.17/22 rest on the old one
- **Audit:** plan against prose (prose wins; flagged for patching) and forward plot logic.
- **Evidence:**
  - foundation §3 (Valens): Celer "claims the arena freedom **was never registered before a magistrate** and that he had bought Valens from the lanista before it could be … **The archive copy in Corinth proves the registration**, which is why Valens needs it (Ch.17)."
  - ch-12:p88 (l.182): "**a magistrate wrote my name in his book**".
  - ch-12:p98 (l.202): "His story was that he'd bought me from the lanista the month before the games, **so the lanista had no right to free me, and the magistrate had written down a mistake** … The magistrate's book is still in the record office at Corinth, with my name in it."
  - On the page, the registration is not in dispute. The dispute is whether the lanista still owned him. So the archive copy alone no longer refutes Celer.
- **Fix:** none in Ch.12. The page is coherent and stronger. **Patch foundation §3 and the Ch.17/Ch.22 outline beats to the page.**
  - The record proves the lanista freed him before witnesses and the emperor.
  - Celer's counter is a backdated bill of sale, which the Rome suit must defeat: the lanista's books, the date, or Celer's hiring him for wages after the games.
  - Ch.12 supplies the last one for free: "After the sword I needed work. Celer … wanted a man".
- **Cascade:** Ch.15 bargain ("He needs his manumission record from Corinth"), Ch.17 archive and Ch.22 testimony. The entity-tracker logs this as a CH12 plan-vs-prose flag.

### [W-22] The bible's Ch.12 blocks quote the writer's draft, not the final page
- **Audit:** bible currency (the blocks say "re-sync after the downstream passes"; this is that flag).
- **Evidence (each checked against chapter-12.md; none is on the page):**
  - **Valens block:**
    - "The emperor didn't know that. He stayed in his chair, too. **That's how it gets told.**" The page has "Nobody on the benches knew that. The emperor never got out of his chair."
    - "Nobody's going to walk in there and say it aloud for me."
    - "**People do, mostly.**" The page has "He had his robbers before you opened your mouth,".
    - "'It was off,' (agreeing the crust lie)". On the page "It was off" is Felix's; Valens says "Don't give the goat any more of it".
    - "The whole of it, then," … "Her, and nobody else." The page has "Kallia, then. Nobody else."
    - "Then he left me for the ford." The page has "He was first down the goat path to the ford."
    - "takes it back 'without looking in it'". The page has "At the stepping stones I gave him back his pouch."
  - **Mara block:** "The glass is whole." is quoted as her speech; it is narration on the page ("The glass was whole."). "no filter would **ever** screw onto it **again**" is "no filter would screw onto it now".
  - **Felix block:** "Was it you broke that one's head? I saw him go off through the olives, holding it. Was it with that?" is "I saw one of them go off through the olives holding on to his head. You hit him with it?". "Was it quick?" is "Quick, though?".
  - **At-risk after Ch.12:** "That's how it gets told." and "People do, mostly." are listed as spent but are not on the page. "bare 'No.' 3 (Valens 1, Mara 2)" is 2 on the page (Valens 1, Mara 1).
- **Fix:** re-sync the Valens, Mara and Felix Ch.12 blocks, the Ch.12 walk-on block and At-risk after Ch.12 to the final page **after** the fixes above. That includes C-01, W-01, W-03, W-05, W-06, W-09, W-10, W-18 and W-19.

### [W-23] Sentence-initial "Nobody" in narration ×2 (cap 1 per chapter)
- **Audit:** Bible, At-risk after Ch.7: "no sentence-initial 'Nobody' in narration beyond one per chapter".
- **Evidence:** ch-12:p30 "**Nobody** came at me." and ch-12:p79 "**Nobody** was supposed to see it."
- **Fix:** cut "Nobody was supposed to see it." (−5). The previous sentence already says so ("the thing I could least explain…"). Narration indefinites (somebody/nobody) stand at 6; WATCH.

---

## INFO (polish / tracking / cascades)

- **I-01 CH11-3 resolved by the page.**
  - Goat: paid by Mara at Kirrha ("the rag was thin after it", p120).
  - Sprats: Valens (p120).
  - Cake and Praxias's drachma: from the dead man's denarii ("leave plenty over", p134); tipped into her rag (p137).
  - The empty purse: let go in the stream (p137).
  - The rag now holds the priest's remainder, Kallia's papyrus obol, the two 1998 coins and the denarii, never summed.
- **I-02 Length.** 4,946 against 5,600 (−12%), and below the writer's own 5,000 range floor even before the −58 of these fixes. There is no per-chapter floor, and the beat does not want padding.
  - Running book total by `wc -w` (with headers) after Ch.1–12: about 66.3k against Σ targets for Ch.1–12 of 69.6k (−4.8%).
  - Projected at that rate the book lands about 248k: above 245k, but the 6.2% planned margin is now about 1%.
  - The orchestrator should let Ch.13 (8,000) and Ch.15 (7,800) land full.
- **I-03 The crowd logic is coherent but not voiced.**
  - Ch.11: the crowd is the danger (eyes, a priest writing names).
  - Ch.12: the crowd is safety ("A knife in there would have a hundred men on it.").
  - The new fact (they want him dead, not taken) explains the turn; Mara asks nothing, by design.
  - Smaller point: "a slave every few paces with a rod" (p173) repeats Ch.11's "a slave of the god's with a rod" (ch-11:p33) in his mouth. Optional: cut "Inside the precinct there's a slave every few paces with a rod." and let "A knife in there would have a hundred men on it" stand (−11).
- **I-04 "Corinthian bronze" (p134)** is the name of a famous luxury alloy (*aes Corinthium*). A conservator narrator would hear the clash. Optional: "and **bronze of Corinth's striking** underneath" (0 prior uses).
- **I-05 "the spout" (p85)** names the waterfall with Ch.11's yard-trough word (and the spout's shadow clock). Optional: "in **the fall**".
- **I-06 Felix's openers:** "Is it silver?" / "Is she? Is she ill?" make 3 "Is…" openers, and "Is she" twice in one burst. Valens's "Is it broken?" adds a fourth "Is it…". Not a frame yet (Ch.11 cut Felix's "Is it…?" from 7 to 2). Rotate in Ch.13.
- **I-07 The narrator pointing at Felix's question habit** (p157: "he asked nothing whatever, which in my hearing he had never managed before"). One dry aside, fine. A second would turn his syntax into a running joke.
- **I-08 The Orestes aside (p137)** is a generalization after the killing, close to the outline's "NO aphorism after the killing". It stays: it is specific (Orestes), mid-scene and not a button, and the purse sinking follows it. The bible logs it as SPENT.
- **I-09 The purse sinks as the walkers arrive** (p137–p138), and the graybeard's donkey drinks in the same ford. It is a nice tension beat, but a careful reader may ask why no one sees a cut purse in clear water. Optional: let it go before they are in sight.
- **I-10 The goat's three days.** "Bring the goat to me at the yard the evening before" (p173) implies Mara keeps Spicula at Kallia's. Ch.13 should show where she was kept, in passing. The bible: Spicula's name only as an object fact in Ch.13.
- **I-11 Survivors' knowledge (for Ch.17).** The two who ran heard Valens call "Mara." (p25) and felt the camera. Celer can know her name and that a woman with Lupus fought. Celer's Ch.17 pleasantries may use it, or not; the tracker records it either way.
- **I-12 Ch.15 cascade, the camera.**
  - Valens has seen it (p46, after C-01 by implication; "Is it broken?", p80).
  - Felix has seen it and asked "Is it silver?". He got "It was my father's".
  - Ch.15's "She shows him the flashlight and the camera" becomes showing what it *does*. Felix's knowledge of a foreign "silver" thing is a gossip risk. The tracker logs it.
- **I-13 The watch.** Ch.12 spends the one clause the bible allowed before Ch.18 (p64). Ch.13–17 have **0 watch touches**.
- **I-14 Sample-13 (Ch.19 register) contains "I put the cap back on the lens".** That act is now impossible. The Ch.19 writer prompt must say the lens is uncapped and the filter ring dented.
- **I-15 Valens's injuries at the consultation (Ch.13, three days on):** a grit graze along the cheekbone (p74), a raised welt across the left forearm (p85), split knuckles on the left hand (p85), and stick bruises across the shoulders (p21). A priest writes the carrier's name, and a crowd looks at the back of the man in front. Ch.13 should not show him unmarked.
- **I-16 The knife washed after the closeness (p76).** This is the same object class as Ch.11's whetstone and knife, two chapters running for "work for his hands". Practical here (blood), so it stands. Ch.13's hands should find another object.
- **I-17 "temper" ×3** in the chapter (Felix ×2; the narrator's Calf-Bearer "in a temper"). A deliberate in-chapter pick-up; leave it, and do not carry it forward.
- **I-18 Depth-by-joint:** "up to the ankle bones" (p97) is 1, under the cap of 2.
- **I-19 Absent-workman verdict:** the green darn "that matched nothing else on it" (p91) is 1, at the cap.
- **I-20 Walk-on laughs ×2** (the talker p6; the third man p14). Menace, not texture to loosen a scene; fine.
- **I-21 Exits by gait or footwear:** p57's slapping sandal and p58's "at her pace" (cf. ch-09:p194 "at his ordinary pace"). The bible cap is 1 per 3 chapters. Optional: p58 → "Valens came behind me with the last mule." (−3).
- **I-22 The strap wound "until there was no strap left" (p37)** quietly rhymes with Emilio's "strap wound around it in the same three turns" (ch-01:p192). It is unpointed and good. Keep it that way, and never call it back.
- **I-23 Checked and correct:**
  - *rudis* and *rudiarius*;
  - Nero in Greece 66–67 and the Isthmian freedom (late 67);
  - a legatus on a proconsul's staff, the post lapsing with the freedom;
  - 69 as the year of several emperors;
  - dowry retention for a wife's adultery, and the husband keeping the child;
  - manumission recorded by a magistrate, with a lanista's copy on a tablet;
  - Isis at Kenchreai and the Craneion (cypress grove; see W-06);
  - denarii of Vespasian fresh in early 71 and Corinth's colonial bronze;
  - Spiculus the murmillo and Nero's gifts (Suetonius, *Nero* 30);
  - the Moschophoros in the old Acropolis Museum (right for 1998);
  - Orestes purified at Delphi;
  - Aigion across the gulf;
  - early-spring sailings with fresh pitch;
  - oaths "By the Twins"; no modern units or idiom in ancient mouths;
  - US spelling;
  - the K1000's rewind crank and filter thread.
- **I-24 ENTITY coverage (6b/6c; the tracker is running).** New in Ch.12:
  - the talker (dead), the big man and the third man (survivors);
  - the Aigion dealer; the sprat woman; the oil men; the graybeard's party (the son, the headman, the cart);
  - the lamp seller; Spicula;
  - mention-only: Celer's steward, "the girl who did her hair", Plautia's mother, the fisherman and the Corinthian mule dealer;
  - places: the ford with plane trees and stepping stones, the cleft and pool, the Kirrha mole and its goat pen.
  - Every Ch.12 entity is stale in the committed YAML until the UPDATE lands.
- **I-25 "Go on up to the boy" (p10) is not obeyed,** and no beat says so. In panic that is fine, and p11 (the big man on her side) implies she is hemmed. No change.
- **I-26 Plautia's household (for Ch.16).** "Her father had given plenty with her" and "Her brother took her home" imply the father is dead and the brother is head of the house. "To her mother's house" puts the mother alive in 67–69. Ch.16 must agree.
- **I-27 Valens's "No." to "Was it one blow?"** tells Felix a detail of a killing, which is a hairline breach of his evasion card. W-19's fix keeps the "No." but makes the question about the man going down, not about Valens's blow. If W-19 is declined, log the breach as deliberate and unique.

---

## SUGGESTED YAML PATCHES (for entity-tracker UPDATE after the editor's fixes)

```yaml
suggested_patches:
  - entity: "meta.contradictions[CH11-3]"
    action: "remove_conflict"
    value: { flag: "RESOLVED", resolved_date: "2026-10-20", resolution: "settled by the page as an act: Mara pays the Aigion dealer for the goat herself ('the rag was thin after it', ch-12:p120); Valens pays for the sprats (p120); the dead man's denarii 'would buy the cake, and Praxias's drachma, and leave plenty over' (p134), tipped into her rag (p137)" }
  - entity: "meta.knowledge_gaps['How Celer learned … Valens was in Phocis']"
    action: "update"
    value: { status: "RESOLVED if continuity W-11 is applied (Valens's inference: 'He'll have said where he found me.', ch-12:p103); else still OPEN" }
  - entity: "timeline[chapter=12]"
    action: "create"
    value: { day: "the 'day after tomorrow' of ch-11:p278; three days before the 7th of Bysios (p171, p180)", span: "dawn at Delphi -> morning at Kirrha (goat, sprats, oil) -> the ambush on the way back -> afternoon at the fall -> evening climb -> dusk at a bend above the plain", season: "early spring AD 71: plane buds just broken; snow water; first boats of the year with new pitch" }
  - entity: "valens.history"
    action: "update"
    value: { rudis: "Corinth, during Nero's visit, after 'five years in the sand'; a magistrate wrote his name; the lanista had a copy made on a tablet (ch-12:p86; p88)", bodyguard: "sworn to Plautia in Celer's atrium before his household gods; two years; slept across her door when Celer was away (p90; p92)", frame: "summer 69, in Celer's atrium at night; two house slaves as witnesses ('the girl who did her hair'); flogged by the fishpond; the steward took the tablet (p94; p96)", celers_claim: "bought from the lanista the month before the games, so the lanista could not free him (p98) — DEPARTS from foundation §3 ('never registered'); see audit W-21", flight: "over the garden wall the same night; a fisherman across the gulf for his belt buckle; carried on the Kirrha quay that winter; named himself Valens; mules bought from a Corinthian dealer (p98)", witness: "Plautia's brother's freedman found him at the harbor last autumn; he refused; the notice went up in Corinth within the month (p103)" }
  - entity: "valens.physical"
    action: "add"
    value: [ { trait: "grit graze along the cheekbone", source: "ch-12:p74", mutable: true }, { trait: "welt across the left forearm (the stick); left knuckles split", source: "ch-12:p85", mutable: true }, { trait: "cloak of good fulled wool, hem darned in green thread; washed, worn wet", source: "ch-12:p91; p112", mutable: true } ]
  - entity: "valens.knowledge"
    action: "add"
    value: [ { fact: "Celer wants him dead, not returned ('He wants me in a ditch.')", learned: "ch-12:p111", method: "inferred (the men brought knives, no rope)" }, { fact: "Mara has a heavy foreign object that was her father's; it can break", learned: "ch-12:p46; p80", method: "witnessed" } ]
  - entity: "mara-reyes.knowledge"
    action: "add"
    value: [ { fact: "the whole frame: rudis, oath, Plautia, Celer's debts, the dowry share, the seized tablet, the record office, Celer's purchase story, the flight, the freedman, the notice's timing", learned: "ch-12:p84-p111", method: "told_by:valens" }, { fact: "Valens is Lupus, confirmed", learned: "ch-12:p1-p16", method: "witnessed" } ]
  - entity: "mara-reyes.physical"
    action: "add"
    value: [ { trait: "a raised line across the front of her throat where the himation dragged", source: "ch-12:p114", mutable: true }, { trait: "left sandal thong re-knotted double", source: "ch-12:p121", mutable: true } ]
  - entity: "felix.knowledge"
    action: "add"
    value: [ { fact: "Valens killed a man on the road", learned: "ch-12:p38-p42; p158-p164", method: "witnessed (aftermath)" }, { fact: "Mara hit one of the men with a heavy foreign thing 'my father's'", learned: "ch-12:p122-p124", method: "witnessed + told_by:mara-reyes" }, { fact: "the cover story ('we came on a man in a ditch')", learned: "ch-12:p127-p131", method: "told_by:valens" } ]
    note: "does NOT know Lupus, the arena or Corinth (out of earshot; at the ford during the telling)"
  - entity: "objects.fathers-pentax-k1000"
    action: "update"
    value: { ch12: "carried under her chiton on its strap since the lodgers came (p79); swung into a man's head (p27-p28); filter ring dented, glass whole, hair in the rewind crank (p78); seen by Valens and Felix; back inside her clothes (p124)", frames: "none shot in Ch.12" }
  - entity: "objects.pentax-lens-cap"
    action: "update"
    value: { status: "LOST", where: "in the spilt oil on the road by the ditch where the talker died (ch-12:p31; p56)", payoff: "none (author decision; see audit W-20)" }
  - entity: "objects.fathers-watch"
    action: "update"
    value: { ch12: "in Valens's pouch, going; handed to Mara to hold at the fall and returned at the stepping stones (p64; p70; p133)", next_touch: "Ch.18 (none in Ch.13-17)" }
  - entity: "objects.maras-money-rag"
    action: "update"
    value: { ch12: "goat paid from it (thin after); the dead man's denarii (some new, Vespasian) tipped in (p120; p134; p137)", note: "never itemized again" }
  - entity: "objects.maras-sherd"
    action: "update"
    value: { ch12: "in her belt against the rag knot (p175)" }
  - entity: "spicula"
    action: "create"
    value: { kind: "the consultation goat", physical: "brown she-goat, white blaze by the horns (p118)", source: "the Aigion dealer's pen at Kirrha, chosen by Felix (p118-p119)", named: "Spicula, by Felix, after Nero's murmillo (p154)", keeper_next: "Mara, until 'the evening before' at the yard (p173)" }
  - entity: "plot_threads.celers-men"
    action: "create"
    value: { status: "open", detail: "three off the first Lechaion boat; the talker dead in the ditch (purse cut, sandals left); the big man and the third man (hit by Mara) fled into the olives; both heard 'Mara.'", source: "ch-12:p1-p36" }
  - entity: "plot_threads.consultation"
    action: "update"
    value: { money_gap: "CLOSED (CH11-3)", goat: "bought (Spicula)", carrier: "Valens, unchanged ('Three days'; the crowd as safety)", date: "three days off (p180)" }
  - entity: "plot_threads.high-grazing"
    action: "create"
    value: { status: "planned", detail: "'When the god's day is done, the mules are for the high grazing … Above the cave … I'll stay up the summer.' (p174); feeds Ch.15" }
  - entity: "locations.kirrha"
    action: "update"
    value: { features: ["a mole; boats tied at its root; goat pen of hurdles there; a sprat-frier", "first boats of the year in early spring; a Lechaion boat on the morning wind"], plain: "see audit W-16 (bare sacred plain recommended)" }
  - entity: "locations.the-ford"
    action: "create"
    value: { description: "a stream out of a cleft crossing the road under stepping stones; plane trees; above, a chest-high lip and a clear pool on pale gravel", source: "ch-12:p61; p63" }
  - entity: "kallia.knowledge"
    action: "add"
    value: { fact: "PENDING: Mara will tell her 'the whole of it' (Valens's leave: 'Kallia, then. Nobody else.')", source: "ch-12:p178-p179" }
  - entity: "meta.contradictions"
    action: "add"
    value: { id: "CH12-1", entity: "valens.history (Celer's legal claim)", plan: "foundation §3: 'never registered before a magistrate'; the archive 'proves the registration'", prose: "registered by a magistrate; Celer claims the lanista had sold him a month before (ch-12:p88; p98)", flag: "UNRESOLVED (patch foundation and Ch.17/22 to the page; audit W-21)" }
```

---

## Proposed-wording freshness check

Every proposed string was grepped against Ch.1–12 and voice-bank samples 01–13. Each has 0 prior uses:
- "He looked for blood on me anyway."
- "he was at Valens's left side"
- "the dust of the plain was on the hem of his cloak" / "with his hands behind his back"
- "He'd made his mind up on the road," (optional)
- "out where the cypresses are"
- "Praxias wanted three and a half."
- "Those three brought none."
- "He'll have said where he found me."
- "he carried it to the terrace edge and tipped it over among the olives below"
- "found a stone the weight of the lost jar"
- "Traders came down"
- "The road went on up in bends" / "bare and darkening, from the foot of the hills to the shore"
- "The year the emperor was in Greece."
- "Did he go down straight off?"
- "Its cap lay in the oil beside him … letters nobody at Kirrha would read as a word"
- "bronze of Corinth's striking" (optional)

**Rejected candidates and why:**
- "looked me over" (ch-07:p39)
- "at the first" (3 prior uses)
- "I said nothing" (a narrated non-answer: family cap)
- "Carters" (it would pre-echo the closing cart)
- "came over for the games" ("for the games" ×2)
- "into the olives" (×2 already in Ch.12)
