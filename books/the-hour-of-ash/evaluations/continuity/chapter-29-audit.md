# Continuity Check: Chapter 29 "Saturnalia" (MANUSCRIPT AUDIT)

**Date:** 2026-10-24
**Audited text:** `manuscript/chapters/chapter-29.md` as it stands (md5 `77e94134…`; after writer, dialogue-polish, hook-craft, disruptor; 6,950w). Line refs are to that file.
**Checked against:** Ch.1–28 (targeted greps plus an independent 4/5-gram and short-spoken-line scan), ENTITY_STATE.yaml as of Ch.28 (read only; CH20-6 forward constraint, felix/lucius/aelia/valens/august-fenn/gratas-husband rows, ch28_requested_checks), outline Ch.28–30, foundation, voice-dna §0/§1/§3b, character-bible (Voices from lives, MARA, VALENS, FENN incl. speech-habit ledger, FELIX, GRATA, LUCIUS, AELIA, CERDO, MNASON fronted-object rule, Ch.29 walk-on block, At-risk after Ch.28: SPENT / CLOSED / CUT / WATCH / Ch.29 guards), the four pass reports.
**Gates re-run by me:** `tic_report.py --echoes 29` 0 echoes, no command or spoken-line echoes; `closed_check.py 29` clean; `style_check.py` Ch29 clean. Everything below was found by reading, not by the gates.
**Total issues:** 39. **Critical:** 3 | **Warning:** 16 | **Info:** 20

**Verdict:** The spine is sound. The festival timeline is internally exact: the invitation "the night after tomorrow" (day 1), "to our supper tomorrow" (day 2), Felix home that evening, Fenn "a day behind" at breakfast on day 3, and feast night all land on the same night. Ages are right (Lucius about 2y5m, Aelia about 11 months). The count "our fifth" Saturnalia is right (arrival spring AD 72). Felix's leave does not conflict with his oath. Fenn's 1950 story is accurate to the play, and his age, 16, is right. Felix's law agrees with his history. Saturnalia customs are sound. There is no tomb, no "cool" passage, no mountain and no aphorism, and the closing line is singular and consistent. **The three CRITs are all repeats of rulings made in earlier audits:** a CLOSED Felix silence, a spoken fronted object (Mnason's alone), and the "in all my time in that town" construction that Ch.28's CRIT-003 cut, now used twice. Each fix changes 1 to 8 words.

---

## CRITICAL ISSUES (must fix before the evaluator)

### [CRIT-001] Felix's reported silence: CLOSED on his card
- **Audit:** 1 / voice (FELIX card, Spent in Ch.21: "his silence as a reported beat ('asked nothing' and kin): CLOSED; show it, never label it"; enforced as Ch.28 CRIT-007)
- **Evidence:** l.450: "The king had held his peace as long as he could bear. He mounted Grata's bench with his wreath slipping."
- **Fix (l.450):** "The king mounted Grata's bench with his wreath slipping." Use "The king", not "He", because l.448 ends on Fenn.
- **Cascade:** the narrated-silence census drops from 5 to 4. W-09's second cut brings it to 3.

### [CRIT-002] Spoken fronted object in Valens's mouth (Mnason's alone)
- **Audit:** 1 / voice (bible l.5401 "Rule (Ch.15 eval C4): a fronted object in speech belongs to Mnason alone. No other speaker fronts an object"; restated l.7090, l.8838; Valens has already had one recast, "I've heard of Neapolis.")
- **Evidence:** l.168: "I heard. The wood I'll cut anyway," said Valens.
- **Fix (l.168):** "I heard. I'll cut the wood anyway," said Valens.

### [CRIT-003] "In all our time on that street" / "in all our years there": the construction Ch.28 cut as foreshadowing, used twice
- **Audit:** law (voice-dna §0 families C/D; precedent Ch.28 CRIT-003, which cut "in all my time in that town" because it measures the Pompeii years as a finished span seen from after their end)
- **Evidence:**
  - l.12: "In all our time on that street he had brought the basket to my plank bareheaded, taken his coppers and gone."
  - l.48: "the old cobbler's shelf held more light than our shop had burned in all our years there."
- **Fix:** l.12: "Until that morning he had always brought the basket to my plank bareheaded, taken his coppers and gone." l.48: "…more light than our shop had burned since we came."
- **Cascade:** l.10 "our fifth in that street" stays. It counts up to the present moment, and the count is correct (Saturnalias AD 72–76).

---

## WARNING ISSUES

### [WARN-01] "since no one carted that week" vs Fenn on the fish-sauce cart
- **Audit:** 2 / objects (the disruptor left this for the guardian)
- **Evidence:** l.80 "There was bark on his shoulders from cutting her firewood, since no one carted that week." Then l.146 Fenn "perched on the jars of the fish-sauce carter's cart", l.186 Valens: "Sit at the back of it going home", l.188 the stage is "a platform of boards on two carts".
- **Fix (l.80):** "…since no wood came round by cart that week."

### [WARN-02] Fenn's Mummers line reuses the narrator's Ch.5 comparison and Mara's Ch.25 Broad Street parade
- **Audit:** 4 / voice (voice-dna §1.5 "no comparison is used twice in the book"; FENN bleed guard: Mara must never pick up his idiom, and he must never pick up hers)
- **Evidence:** Ch.5 l.139 (Mara, of the painted temple): "The Mummers had got at it." Ch.25 l.130 (Mara): "my father took me down Broad Street for the parade". Ch.29 l.150: "It's the Mummers," … "it's New Year's Day on Broad Street, and all it wants is a banjo and a string band in feathers." / l.152 "You're on the wrong coast for a banjo."
- **Fix:** l.150: "It's the Gimbels parade," Fenn said, dropping into English, "it's Thanksgiving morning, and all it wants is Santa going up a fire ladder into the store window." l.152: "You're a long way from Gimbels."
- **Cascade:** Gimbels is a new period reference (1 of 2). Grep it before committing.

### [WARN-03] Fenn asks Mara for a Greek word
- **Audit:** 1 / information (FENN: "In Greek, perfect, formal and courtly after more than three decades … the only character whose second language is better than his first is current"; Mara's Greek is from books)
- **Evidence:** l.388: "What's the Greek for an umpire?" he asked me, and I gave him *brabeus*, the judge at the games.
- **Fix (l.388):** "…with English leaking out of it wherever the Greek gave way; for the umpire he settled on *brabeus*, the judge at the games." l.434's *brabeus* still pays off.

### [WARN-04] Valens asks about "the stealing", which nobody has explained in a language he speaks
- **Audit:** 3 / information flow
- **Evidence:** l.442 "Show me how the stealing goes." and l.588 "He's to show me the stealing." The only steal on the page is Ch.25 l.136 ("Chico Ruiz steals home"), in English, which Valens does not follow. The Greek lesson at l.346–l.390 covers the throw, the club, running, catching, strikes, wide ones and the foul ball.
- **Fix (l.388):** "through the three strikes and the four wide ones and the base a fast man could steal," (one clause; plausible-but-unshown becomes shown).

### [WARN-05] "A cap" as a batter's protection: wrong for Fenn's 1968
- **Audit:** 3 / world (batting helmets were standard by the late 1950s; the National League required them from 1956)
- **Evidence:** l.372: "A cap." … "Wool, with a peak at the front for the sun."
- **Fix (l.372):** "Wool, with a peak at the front for the sun, and lately a hard shell in it." l.374 "Valens touched his own cap." still works, and the Chapman answer at l.378 now explains why the shell came.

### [WARN-06] Ch.29 guard ("nobody repeats 'You were sitting down' or answers it in words"): the chapter edges toward an answer
- **Audit:** guard (At-risk after Ch.28, Ch.29 guards)
- **Evidence:** l.454 Valens's freedom tale: "When it finished, I hadn't fallen down." That is arena posture, in words, to Felix, the chapter after "You were sitting down." On top of it Felix orders Valens to sit: l.290 "you sit and he sits and I sit and they fetch", l.314 "Sit. You've been bought." Together they read as the book answering Ch.28's last line.
- **Fix:** l.454: "There was a Gaul. I beat him." (Ch.12 l.180 is "I put the Gaul down", so avoid "down".) l.290: "you eat and he eats and I eat and they fetch". l.314: "Leave it. You've been bought." Keep l.290's opening "Sit," to Cerdo; that is ordinary hosting.

### [WARN-07] Fenn, who knows the year, tells Grata she will "live to a great age"
- **Audit:** law-adjacent (voice-dna §0 family E routes ash irony to the reader; here it is put in the mouth of the one character who knows the date, which reads as planted foreshadowing). Also l.468 "do not marry before thirty" (Felix is about 21 at the eruption).
- **Evidence:** l.510 "I'm making this up as I go" / l.512 "You will live to a great age, madam," he told her, "and eat lentils without end."
- **Fix (l.512):** "You will have grandchildren, madam," he told her, "and eat lentils without end." Grata's "Any midwife would have told me that" still lands. Keep l.468 as the chapter's one joke fortune.

### [WARN-08] "the bow he kept for Valens": a habit named by the narrator, which also contradicts Ch.25
- **Audit:** 1 / voice (Voices from lives: no one comments on another character's habit; nameable-rule test). Also a fact clash: Ch.25 l.84 gives the waist bow to Mara ("bowed from the waist, a real bow"), and the FENN card lists "the bow from the waist" as SPENT.
- **Evidence:** l.164: "Fenn bowed to him from the waist, the bow he kept for Valens."
- **Fix (l.164):** "Fenn bowed to him." (l.296's "deep bow, Puteoli-fashion" to Cerdo then stands alone.)

### [WARN-09] Narrated-silence census 5 (cap 3, per the Ch.28 census); Valens's stillness was to be rested
- **Audit:** 7 (census) plus WATCH ("Valens's stillness: rest it")
- **Evidence:** l.264 Fenn "kept his English to himself"; l.270 "his first words since the crossing"; l.384 "Valens let that go by."; l.450 (CRIT-001); l.582 "He let it alone". The two "let" silences for Valens make a repeated shape.
- **Fix:** CRIT-001, plus l.384: "Valens's big finger went among the pits and nudged the one on the little hill back to the spot Fenn had moved it from." That leaves 3.

### [WARN-10] "For a breath": 5th use book-wide, back to back with Ch.28, and "For some breaths" in the same chapter
- **Audit:** 8 (refrain forming; the n-gram floor misses 3-word phrases)
- **Evidence:** Ch.8, 21, 23 and 28 (once each); Ch.29 l.470 "For a breath Felix was away at the fullery's shut door."; l.252 "For some breaths he hung so."
- **Fix (l.470):** "Felix looked off at the fullery's shut door. Then he made his next law."

### [WARN-11] Fenn's "sir" ×5 makes a nameable courtesy rule
- **Audit:** voice (nameable-rule test; Ch.27 recorded "sir" 2)
- **Evidence:** l.166, l.298 (to Cerdo), l.334, l.390, l.444.
- **Fix:** l.334 "Permit me." (cut ", sir"); l.390 "The runner was here, and the ball came from here…". That leaves 3.

### [WARN-12] Felix: three stacked-question bursts
- **Audit:** voice (nameable-rule test; FELIX counts: bursts 3 in Ch.24, then WATCH 2 in Ch.26; "Felix owes no stacked questions")
- **Evidence:** l.104 "where is he, is that him, look how long he's got!"; l.408 "Do they pay them, how much, is it better than a lanista pays?"; l.412 "Their faces? Could you get my face on one?"
- **Fix (l.412):** "Could you get my face on one?"

### [WARN-13] The superlative-"ever" frame ×3 across two speakers (Felix's bleed guard: no boast formula repeated)
- **Audit:** voice
- **Evidence:** l.132 Felix "That's the best law anybody ever made."; l.460 Grata "Shortest tale ever told at a festival table, and the best,"; l.500 Felix "Worst song I ever heard," (and l.568 "Best night of the whole festival").
- **Fix:** l.132 "Somebody write that one on a wall." (fame, and walls, are his life). l.460 "Short and done, and you could learn from it, Felix," said Grata. Keep l.500.

### [WARN-14] Place as addressee: "to the street", "told the plank", "told the dark"
- **Audit:** voice (one construction, three speakers, one chapter)
- **Evidence:** l.142 "said Grata to the street"; l.460 "Grata told the plank"; l.516 "'The street stays up,' Felix told the dark from our doorway, and the dark paid him no heed." (Also l.14 "for him, for me and for the street".)
- **Fix:** l.460 is handled by WARN-13. l.516: "'The street stays up,' Felix said from our doorway." Keep l.142.

### [WARN-15] "Felix's mouth fell open": kin of the Ch.28 CUT string
- **Audit:** CUT log (Ch.28 CRIT-007 cut "Felix's mouth came open. Nothing followed, and he shut it."; Ch.25 "His mouth came open.")
- **Evidence:** l.492: "Felix's mouth fell open."
- **Fix:** delete the sentence. Grata's line follows directly.

### [WARN-16] Festival-span vantage: "all festival long", "the last piece of evidence" and "all week", on night 3 of a festival that continues
- **Audit:** 2 / §0 stance (the horizon is the narrated moment). Felix is king "till the last day" (l.118), Fenn goes "Tomorrow" (l.588), and "Come back next year" (l.558) all show the festival is still running.
- **Evidence:** l.10 "Evidence for it came to me all festival long"; l.274 "The table was the last piece of evidence"; l.594 "I had made my case all week".
- **Fix:** l.10 "Evidence for it came to me from the festival's first morning"; l.594 "I had made my case for three days". l.274 can stay ("last" of the case as made).

---

## INFO

- **I-01 Timeline: VERIFIED.** Day 1 (Dec 17): caps, the invitation "The night after tomorrow" (l.20). Day 2: the forum and the fountain (l.58, "Next morning"); "to our supper tomorrow" (l.94); Felix home "that evening" (l.102), served by Albucius "last night" (= day 1); the law for "tomorrow night" (l.128). Day 3: Fenn "at breakfast, a day behind Felix" (l.146), "tonight" (l.158), the stage, the feast. The two invitation phrasings agree.
- **I-02 Felix's ten days vs his Ch.28 oath: NO CONFLICT.** Ch.28 records three years to Albucius, 400 down, and a troupe quartered at the theaters in Pompeii itself. Nothing forbids leave, and the troupe is still in town ("sheep towns" was his fear, not a posting). Optional: "the troupe" includes Albucius's slave fighters, for whom ten days at home is a stretch. "He's given us sworn men ten" would avoid it.
- **I-03 Felix's law vs his history: CONSISTENT.** He was bought off the Cilician (Ch.11 l.448, "He paid more for me than he paid for the black"), so Mara's "Then you will be among the waited-on" (l.130) is true, and "That had not occurred to him" fits a boy who tells his own purchase as a boast. Valens "Once." / "Once is plenty." agrees with Ch.11. Fenn "never been bought": nothing on file says otherwise. Mara: registered free as Kallia's kinswoman (Ch.7). Grata's "nobody waits on me" correctly puts her among the never-bought.
- **I-04 Lucius's "Tata" (l.328): first on the page, CONTRADICTED NOWHERE (grep Ch.1–28: 0).** It is planned (LUCIUS card: "He calls Valens Tata … made clear by context once"). The context ("he told his father") meets the one-time gloss, so later uses need none. Single words fit the "About 2" stage and Ch.27's "Smoke / Duck / Bone / Again". *Tata* is the attested Latin nursery word. The cover-the-name sample line uses the word, not its phrase, so there is no collision.
- **I-05 Fenn's 1950 story: ACCURATE.** Oct 1 1950, Ebbets Field: tied in the bottom of the 9th; Abrams and Reese on; Snider's single; Ashburn's weak arm and early charge; Abrams out at home; coach Milt Stock blamed; Sisler's 3-run homer in the 10th; swept by the Yankees. Born Aug 1934, so "sixteen" is right. "since Eisenhower" (1953–61) contradicts nothing (no page shows him singing it later). "thirty-five years" (l.430) = AD 41–76, correct; voice-dna bans only "in all the years since". Chapman (Cleveland, 1920, died next morning) and Mays ("nine more years", 1921–29) are correct. Reserve clause correct for 1968. Minor: Fenn's home is up Germantown Avenue (Ch.26) and the appliance store is on Frankford Avenue, a long walk; it is defensible, since that is the point of the line.
- **I-06 Grata's palm-reading vs the guard "the palm is not mentioned": NO VIOLATION.** The guard and Felix's card ("no further palm anywhere in the book") refer to the scratched palm-branch, SPENT in the Ch.28 tunnel. Grata's palm is her hand, a sense the book uses freely (Ch.28 l.358 "printed itself into both palms"). The disruptor ruled the same. Optional polish: "palm" → "hand" at l.508 and l.514 keeps the word off the page in the chapter after. l.520 already says "Grata's hand".
- **I-07 Closing line "Under the baker's shutter…": CORRECT AS SINGULAR.** It agrees with l.550 "through the shutter", l.564 "the baker's door" and every other "the baker" (the master). The plural would have pointed at the two crossing bakeries. "again" anchors on Cerdo's l.292 ("He'll let it die"). It is a quiet image with no aphorism and no device-button.
- **I-08 World rules, Saturnalia AD 76: SOUND.** The *pilleus* on all heads, master and slave alike (l.12, l.32). "Io, Saturnalia!". Dice in the open, with the aedile's man dicing. Four *tali*, where Venus (every face different) makes the king and the dog is the bad throw (Tacitus *Ann.* 13.15 for king-by-throw). Royal orders to dance and soot on the face (Lucian, *Saturnalia*). Masters serving slaves. Wax *cerei* as gifts. Clay figures under the forum colonnade. One mild stretch: in Rome the Sigillaria was the festival's later days, and buying on day 2 is defensible for a provincial town. Nuts and the walnut castles. The EID MAR pileus between two daggers. Mimes without masks, with a woman in the troupe. Harshness about 7: Cerdo's forearms, his mat by the oven, the ten-year-old on the mill, Grata's girl who got "a cap and a cup at the door every year". Present, not grinding.
- **I-09 Objects: CLEAN.** Four mules ("The four mules." / "Four."); the dun (she) and the black (a biter, consistent with Ch.11 and Ch.16). No upper floor: "lifted until his hair brushed the beam" and "taller than this house" fit a single storey, and "your stair" is Fenn's at Puteoli. The hare bowl is not mentioned. Fenn's notebook is not mentioned (Mara holds it; he refused it in Ch.25). New objects for the tracker: Lucius's ball (two figure-eight pieces of white hide, red thread, a cork heart wound with wool), the dun-painted clay mule with no tail, Aelia's peg doll with the leg in the wrong socket, Felix's bay wreath, Cerdo's stamped eight-wedge loaf, and the olive-pit field left on the plank. One loose end: l.566 Fenn sleeps with "the felt cap beneath" his hat, but he is never shown taking a pilleus. Either give him one at l.148 or cut ", and the felt cap beneath".
- **I-10 Fenn's speech-habit ledger: WITHIN CAPS.** Doubling 1 ("Ashburn, Richie Ashburn", l.390). "guy" 0 (at cap, not touched). "fellow" 1. "and all / and everything" 0. Capacity sizing ≤2. "kid" / "okay" 0. Greek lines carry no contractions. One unsignalled switch: l.402 ("I don't believe my feet…") is English, with only the contractions to mark it, after a Greek exchange. Optional: "Then the tenth," he said in English, "…". The "in English" tag is used 7 times; vary one or two.
- **I-11 First meetings and knowledge.** Fenn meets Felix, Grata and Cerdo for the first time here (Felix was absent in Ch.25 and Ch.27). Felix's knowledge of "the Chaldean" and the "shaking hand" (l.128, l.158) is plausible from household talk since Ch.26. l.158 "you wait on me tonight, and him, and the oven man": "him" has no referent, because Valens comes out only at l.164. Optional fix: "and Valens". CH20-6's forward constraint holds: the Kalends appear only as dates (Grata l.280, Cerdo l.542), and Valens never names or pictures the tomb.
- **I-12 Whole short spoken lines.** "Once." (Mara, Ch.15 l.40 → Valens l.316: a different speaker 14 chapters later, low risk). "Go on." (l.386): the first whole-line use (Ch.10 and Ch.22 are tails of longer turns). "Why?" and "Good." are generic. None needs a change.
- **I-13 Bible sync (for the evaluator's FINAL pass).** The Ch.29 walk-on block and the CERDO "as written" note quote draft lines that are not on the page: "Poured for by a Chaldean. Me."; "It's the boys with the walnuts," / "Grown up."; the fountain girl's "she's had to stand behind me since daybreak", "Tomorrow she can go first", "Then there's no festival,"; Cerdo's "I'll be up till the cocks"; the carter's "with a warning". The FENN chaos schedule says "the 1964 Phillies (Ch.25, 26, 29, 35)", but the page gives 1950, which is fresh and allowed (subjects, not phrases). Record it.
- **I-14 Valens's register.** "This is lighter." / "The food was better." are measurements from his life, not figurative comparisons, and are allowed under "Voices from lives". l.174 "The sea's taken a bite out of the road there" is his one figurative turn. Optional: "The sea's had half the road there."
- **I-15 Grata's "before my Secundus" (l.338)** can be read as her husband. Secundus is her son (Ch.26 l.140) and the husband is unnamed. Optional: "before my Secundus was born".
- **I-16 "as far as the" ×3:** l.480 and l.484 are Mara's adjacent lines, plus l.596. Optional, l.484: "Felix, I cannot carry a tune to the door."
- **I-17 Plot threads opened (none mis-closed):** the stealing lesson "Tomorrow, before he goes"; Valens hauling to Puteoli in spring and climbing Fenn's stair (room before Fenn's death in winter 78–79); Cerdo's "Come back next year"; Mara's shame left unresolved, with no aphorism, as the outline requires. Ch.28's threads are respected: Felix is alive, the bout is not recapped, "You were sitting down" is not repeated (but see WARN-06), and Prima appears only as a glance at a shut door.
- **I-18 Law sweep.** Beyond CRIT-003, WARN-07 and WARN-16, no foreshadowing. No "Seventy-nine, I thought". No "cool". No tomb. Nobody names the mountain, and it does not appear. No closing aphorism. Mara's singing in English is to listeners, so her Ch.7 commitment holds. My 4/5-gram scan against Ch.1–28 finds only function-word chains, and the gate echo scan is 0.
- **I-19 Lucius "exactly"** (l.344, after Ch.27's "stops on every base 'exactly'"): 2 uses. WATCH, so a precision rule does not form. Lucius fist mentions 3 (l.188, l.252 ×2).
- **I-20 l.490 "I gave Fenn the jug."** The beat is unclear (surrender? freeing her hands?). Optional: "I set down the jug." The later "The jug stood empty in front of Cerdo" (l.518) does not depend on it.

---

## SUGGESTED YAML PATCHES (for the entity-tracker's next UPDATE; not applied)

```yaml
suggested_patches:
  - entity: "lucius.voice / lucius.knowledge"
    action: "add"
    value: { fact: "calls Valens 'Tata' (first on the page)", source: "ch-29:l.328" }
  - entity: "lucius.possessions"
    action: "add"
    value: { item: "fenns-baseball", note: "two figure-eight hides, red thread, cork heart wound with wool; Puteoli saddler from a wax drawing", source: "ch-29:l.322-l.328" }
  - entity: "cerdo"
    action: "create"
    reason: "new named character (oven slave of the bakery opposite; flue; the jug)"
  - entity: "august-fenn.relationships.felix / pomponia-grata / cerdo"
    action: "add"
    reason: "first in-person meetings, ch-29"
  - entity: "valens.knowledge"
    action: "add"
    value: { fact: "baseball as Fenn tells it in Greek: club, throw, run, catch, strikes, wide ones, foul, night lights, 30,000 watching, a death by a pitch, the club owns the player", method: "told_by:august-fenn", note: "'stealing' named but not explained on the page (WARN-04)" }
  - entity: "felix.status_log"
    action: "add"
    value: { chapter: 29, status: "on ten days' leave from Albucius; Saturnalia king by the Venus throw; sleeps against the dun" }
```

---

## TRACKING (Ch.29 additions)

| Day (Dec AD 76) | Event | Lines |
|---|---|---|
| 17 (day 1) | caps at daybreak; Cerdo invited for "the night after tomorrow"; the fountain girl; wax payments begin | l.12–l.56 |
| 18 (day 2) | forum figures; dice at the fountain; Valens in a cap ("supper tomorrow"); Felix home on leave, king by Venus, the law | l.58–l.142 |
| 19 (day 3) | Fenn arrives at breakfast; the walk to the crossing; the mime; the feast; the jug; Cerdo recalled at the second firing | l.146–l.596 |
| 20 (planned) | the stealing lesson "before he goes" | l.588 |

---

## Repair log (book-editor, 2026-10-24)

Edited in place, `manuscript/chapters/chapter-29.md`. Before each swap went in, I checked it against the bible's SPENT, CLOSED and CUT lists for Ch.27–28 and the Ch.29 guards, against what the dialogue-polish and disruptor passes had cut, and against Ch.1–28 by grep. Line refs are to the pre-repair file.

### CRITICAL
| # | Finding | Fix on the page |
|---|---|---|
| CRIT-001 | l.450 Felix's reported silence ("had held his peace") | "The king mounted Grata's bench with his wreath slipping." |
| CRIT-002 | l.168 Valens fronts an object ("The wood I'll cut anyway") | "I heard. I'll cut the wood anyway," said Valens. |
| CRIT-003 | l.12 "In all our time on that street…" | "On other mornings he brought the basket to my plank bareheaded, took his coppers and went." I did not use the audit's "Until that morning": Ch.16 l.22 has "until that morning I had…". |
| CRIT-003 | l.48 "in all our years there" | "…more light than our shop had ever burned." I did not use the audit's "since we came": it is already in Ch.6 and Ch.19, so this would have been a third use. |

### WARNING
| # | Finding | Fix on the page |
|---|---|---|
| WARN-01 | l.80 "no one carted" vs the fish-sauce cart | "since no wood came round by cart that week." |
| WARN-02 | l.150/152 Mummers / Broad Street reuse | l.150: "It's the Gimbels parade … it's Thanksgiving morning, and all it wants is Santa going up a fire ladder into the store window." l.152: "You're on the wrong coast for Gimbels." I kept "wrong coast" so that Fenn's "I'm on the wrong everything." still answers it. Gimbels gets 0 hits in Ch.1–28. Ch.2's "Thanksgiving, 1967" is Fenn's own document, with no phrase overlap. |
| WARN-03 | l.388 Fenn asks Mara for the Greek | "…wherever the Greek gave way. For the umpire he settled on *brabeus*, the judge at the games." The l.434 payoff stands. |
| WARN-04 | "the stealing" never explained to Valens | l.388: "through the three strikes and the four wide ones and the base a fast man could steal," |
| WARN-05 | l.372 wool cap as 1968 protection | "Wool, with a peak at the front for the sun, and a hard shell over it, the last I saw." "by the time I left" tripped a 3× recurrence and "before I left" echoed Ch.22, so both were varied away. |
| WARN-06 | Answering "You were sitting down" | l.454 "There was a Gaul. I beat him." The tag was dropped to clear a "him said valens" echo with Ch.27; the speaker is clear from Felix's order. This agrees with Ch.12 and avoids "down". l.290 "you eat and he eats and I eat and they fetch" (Felix's opening "Sit," to Cerdo kept). l.314 "Not you. You've been bought." I used "Not you" instead of "Leave it" so that it does not pre-echo Valens's "Leave those." at l.584. Also l.320 "sat back down" became "settled again" (narration near the guard phrase). |
| WARN-07 | l.512 Fenn's "live to a great age" fortune | "You have a son, madam," he told her, "and a husband, and more lentils than any woman in Campania." The fortune now tells only the visible present and predicts nothing. Grata's "Any midwife would have told me that" still lands, since a midwife delivered the son. "Do not marry before thirty" stays as the chapter's one joke fortune. |
| WARN-08 | l.164 "the bow he kept for Valens" | "Fenn bowed to him." The SPENT waist-bow is gone too. |
| WARN-09 | Narrated-silence census 5 | CRIT-001 plus l.384, now "Valens's big finger went among the pits and nudged…". The 3 left are l.264, l.270 and l.582. |
| WARN-10 | l.470 "For a breath" | "Felix looked off at the fullery's shut door. Then he made his next law." l.252 "For some breaths" sits inside the protected anchor and is untouched. The gesture gate is clean. |
| WARN-11 | Fenn "sir" ×5 | l.334 "Permit me."; l.390 "The runner was here, and…". That leaves 3 (l.166, l.298, l.444). |
| WARN-12 | Felix's stacked-question bursts ×3 | l.412 is now "Get my face on one.", an imperative. The audit's "Could you get my face on one?" made a cross-paragraph echo ("the street could") with Ch.28. That leaves 2 bursts (l.104, l.408). |
| WARN-13 | Superlative "ever" boast ×3 | l.132 "Somebody write that one on a wall." l.460 "Short and done, and you could learn from it, Felix," said Grata. l.500 is kept. The boasts are now 2 (l.500, l.568). |
| WARN-14 | Place as addressee ×3 | l.460 handled by WARN-13. l.516: "'The street stays up,' Felix said from our doorway." Only l.142 is left. |
| WARN-15 | l.492 "Felix's mouth fell open." | Deleted. |
| WARN-16 | Festival-span vantage | l.10 "Evidence for it came to me as the festival went along, our fifth in that street". The audit's "from the festival's first morning" doubled l.12's "opening morning", and a "the first day / from the first" draft tripped two 3× recurrences. l.594 "I had been making my case since the caps went on". "for three days, and" tripped a 3× recurrence, and the new wording points back to the first piece of evidence. l.274 stays. |

### INFO applied (trivially right)
- I-06: l.508 "Grata's palm" → "Grata's hand". l.514 "left her palm in his" → "left it in his", which also avoids three "hand" in 12 lines.
- I-09: l.566 cut ", and the felt cap beneath" (Fenn never takes a pilleus).
- I-10: l.402 "'Then the tenth,' he told me, '…'" signals the switch to English without adding an 8th "in English" tag.
- I-11: l.158 "and him" → "and Valens".
- I-14: l.174 "The sea's had half the road there".
- I-15: l.338 "before my Secundus was born".
- I-16: l.484 "I cannot carry a tune to the door."
- I-20: l.490 "I set down the jug."

INFO not applied: I-02 (optional, left as written), I-13 (bible sync belongs to the evaluator's FINAL pass; character-bible.md is not touched here), and the rest, which are verifications.

### Untouched by instruction
The opening claim (l.8), the closing line, Valens's olive-pit questions, "I shall get olives in", the farce and Lucius's roll, Mara's cup rising to Cerdo's jug, and the bad song (apart from cutting WARN-15's sentence, which sits inside that paragraph).

### Gates after repair
- `bash tools/check_chapter.sh 29`: **ALL MECHANICAL GATES CLEAN**. Style clean; grammar 0 errors; rhythm 0; show/tell clean; voice-wear strict clean; tic gate clean (gestures included); **5c echo scan 0**; **5d closed ledger clean**; metaphor clean.
- `python3 ../../tools/shape_check.py .`: **SHAPE CLEAN**. Ch.29 opens narrative and closes quiet.
- Words: shape 6,950 → **6,897**; style 6,965 → **6,912**; show/tell 6,969 → **6,916**.
- Dialogue: **37%** shape, **36.6%** show/tell (band 35–45; was 36.5%).
- The l.6 header comment is updated.

### For the bible sync (not applied here)
These new or changed lines will need to go into the card quotes and the Ch.29 walk-on block:
- Fenn: the Gimbels line ("wrong coast for Gimbels"), the "hard shell" line, and the Grata fortune.
- Felix: "Somebody write that one on a wall.", "Not you. You've been bought.", and "Get my face on one."
- Valens: "There was a Gaul. I beat him." and "The sea's had half the road there".
- Grata: "Short and done…".
- Fenn's period-reference census: Mummers and Broad Street are off the page; Gimbels and Thanksgiving are on it.
