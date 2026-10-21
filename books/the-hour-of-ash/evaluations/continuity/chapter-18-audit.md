# Continuity Audit: Chapter 18 (run 2, per-chapter drift audit)

**Date:** 2026-10-21
**Mode:** MANUSCRIPT AUDIT. Ch.18 "Lechaion" (post-disruptor) is checked against:
- Ch.1–17 as they stand on disk;
- ENTITY_STATE.yaml as of Ch.17 (read only; the tracker update is running in parallel and this audit does not touch it);
- outline.md (Ch.18 as patched for the same afternoon; Ch.19 for the handoff);
- foundation.md (§4f re-read item 5 "The watch-winding", the §4 chapter table, §3 Valens), voice-dna.md (§0, §1, §3b), character-bible.md (Mara, Valens, Felix, Pacuvius, the Ch.18 walk-on block, the at-risk list), the voice-bank samples;
- STATE.yaml guardrails and resolved_author_decisions (AUTHOR-CP3-3, CP3-5, END-1).

**Chapter reviewed:** `manuscript/chapters/chapter-18.md`
- **Length:** **2,636** prose words by shape_check (floor 2,500, so **136 words of headroom**). Dialogue **33.6%** by show_tell (band 30–40, floor 30). 0 breaks. Median sentence 15 (gear mid).
- **Ledger:** the opener is an I-statement of more than 8 words, an in-moment fact ("I reached the quay … with the taste of blood in my mouth from running"). The close is a 7-word single-sentence paragraph, a punch ("They drew the plank in after us."). It is a single scene, under an hour, the same early afternoon. All of this matches the ledger row.
- **Citations:** `l.NN` is the file line in chapter-18.md. Lines in other chapters are cited as `ChN l.NN`.

**Mechanical baseline** (`bash tools/check_chapter.sh 18`, run read only): **ALL CLEAN.**
- Tic gate clean, gesture classes included. And-chains 3 (cap 9). Credential asides 0. Negation pivots 0. "So" openers 0.
- `tic_report.py --echoes 18`: **0 echoes, 0 command echoes, 0 spoken-line echoes.**
- Metaphor 1.1 fig/1k, 3 similes. Shape audit: SHAPE CLEAN.

**My own sweeps:**
- 4–6-grams of Ch.18 against Ch.1–17 and every voice-bank sample, including stop-word-bounded grams. This found the voice-bank frame lift in W-10 and the Ch.15 lift in W-12.
- Intra-chapter 3–4-grams.
- A count of the "without" family across the whole book.
- The watch traced through every chapter that mentions it.
- A sun-altitude calculation for Lechaion (37.93°N) at 12:40 local solar time across the spring declinations.
- Roman marriage law (conubium; Digest 23.2.5; lex Minicia), the Latin oath convention (Gellius, *NA* 11.6), and the Lechaion→Puteoli route.
- An information-flow table for Felix and for the master.
- The card rules for Pacuvius, Valens and Felix, counted line by line.

**Total findings: 32. CRITICAL: 0 | WARN: 14 | INFO: 18**

**Summary**
- **No CRITICAL.** There is no hard contradiction with Ch.1–17, ENTITY_STATE, the outline or canon. Nothing explains the watch or points it toward the ending (END-1 holds). Foreshadowing is 0 by my reading. There is no pregnancy-gap line (CP3-3), and "Isthmia" appears 0 times (CP3-5).
- **The brief's history questions:**
  - **The marriage framing is safe.** The page claims consent before witnesses, to satisfy a shipmaster, and nothing more. Without conubium it is *matrimonium iniustum*, which is still a marriage (I-01).
  - The master's refusal is plausible (I-02).
  - Mules on board, the Lechaion harbor and the ship's gear all check out (I-04).
  - The route is not stated on the page (I-03).
  - **The shadow is borderline.** "Shorter than my sandal" works only for a post under roughly 40–60 cm (W-03).
- **The watch:**
  - Its history agrees in every detail (I-05).
  - Right wrist against the gold on the left agrees with Ch.16 (I-05).
  - **One mechanical slip.** "Wound tight to its end" at 12:40 does not fit the dawn winding shown in Ch.11 (W-02).
- **The WARNs:**
  - two information-flow gaps in Felix's arrival burst (W-01);
  - three period details: the oath, the "before there were priests" claim, and the barrel (W-04, W-05, W-06);
  - Mara's retired voice-failing channel (W-07);
  - a contraction in Mara's Greek (W-08);
  - the "without" cluster, at 3rd book-wide uses (W-09);
  - a voice-bank frame lift (W-10);
  - Felix borrowing Valens's Ch.16 mule command (W-11);
  - a Ch.15 heat-scene phrase reused (W-12);
  - "twice over" at its 5th use (W-13);
  - character-bible lag (W-14).
- **Word ledger:**
  - If every WARN fix below is applied as written, the net is about **−47 words, to ~2,589**, still above the 2,500 floor.
  - Dialogue moves to about **33.6%** (speech −17 words).
  - With the two optional INFO trims the totals are about 2,579 words and 33.5%.

---

## CRITICAL ISSUES

None.

---

## WARNING ISSUES

### [W-01] Felix asks after things he was never told
- **Audit:** 3 (information flow)
- **Evidence:** l.16 "Where've you been? **Did you get it?** Why are your arms white?" and l.22 "Are you along? Only you two? **Where's the lady with the litter?**"
- **Problem 1, "it":**
  - ENTITY records Felix as absent for the plan: `felix.knowledge_absent_ch16` "the plan for the games (he is in the court with a lamp while it is made)". Ch.15 gave him only "Corinth, the winter, the ship and Italy" (`knowledge_absent_ch15`: not 'man and wife', and not the papers).
  - Ch.17 l.278 shows that he knew he was being sent ahead while they stayed in the city. It does not show that he knew what they stayed for.
  - "Did you get it?" makes the reader ask how the boy knows.
- **Problem 2, "the lady with the litter":**
  - Felix has lived all winter in the house of Plautia's brother. He watched her go down the porch step to the baths in Ch.16 (l.282–296).
  - "The lady with the litter" is a stranger's tag for her, and nothing on the page tells him she was going with them that day.
- **Severity:** WARN, not CRIT. There is a plausible off-page path: the household's freedman walked down with him at dawn and knew the plan. Rule 8 applies: plausible but unverified.
- **Minimal fix:**
  - Cut "Did you get it?" (−4).
  - Optional: cut "Where's the lady with the litter?" (−6).
  - The burst still stacks three or more questions, as his card requires: "Where've you been? Why are your arms white?" / "Are you along? Only you two?"
- **Cascade risk:** none. Valens answers neither question as written, and the leaf is not mentioned anywhere in Ch.18.

### [W-02] "Wound tight to its end" does not fit his morning winding
- **Audit:** 4 (world rules: the object) and 1 (behavior)
- **Evidence:** l.102 "I put my nail to the crown to give it its turns, and the crown stood hard against my nail; the spring was wound tight to its end."
- **What the book has established:**
  - Ch.6 l.264 Mara tells him "Every morning."
  - Ch.11 (Felix) says "Each day before he's had his bread he does something to it, with his back to me."
  - A 1966 hand-wound Seiko takes roughly 35–40 crown turns for about 40 hours.
- **The problem:** wound at dawn and read at 12:40, the movement has run about six or seven hours, so the crown would take several turns before stiffening. A crown that "stood hard" at the first touch means it was wound within the last hour or less.
- **The brief's own check:** the brief's 1.5-day test ("running, so wound within ~40 h") is the right test for *running*. A *full* spring is the stricter claim.
- **Severity:** WARN. The flour on the crystal (l.102) lets a careful reader suppose he took it out at the oven, but the page does not show it.
- **Minimal fix** (keeps "already wound" and adds no explanation): "…to give it its turns, and it went round twice under my nail and stood hard." (−5). Two turns reads as "he wound it this morning", which is exactly the daily care Ch.11 set up.
- **Cascade risk:** none. The voice-dna §3b.4 rule ("wound" verb phrase differs at Ch.18/24/32/41) is still satisfied.

### [W-03] The post's shadow "shorter than my sandal" needs a very short post
- **Audit:** 2 (time) and 4 (world physics)
- **Evidence:** l.104 "The hands stood at twenty to one, and beside my foot the mooring post laid a shadow on the stone shorter than my sandal, tipped a little east."
- **Calculation** (Lechaion 37.93°N; 12:40 local solar time, hour angle 10°). The page dates the day between the Kalends ("married at the Kalends", l.40) and the Ides ("not … before the Ides", l.50) of a spring month:

  | Sun's declination (≈ date) | Sun altitude | Shadow ÷ height | Tallest post that casts a shadow under a 26 cm sandal |
  |---|---|---|---|
  | +5° (early April) | 55.8° | 0.68 | ~38 cm |
  | +9° (mid April) | 59.7° | 0.58 | ~45 cm |
  | +15° (early May) | 65.4° | 0.46 | ~57 cm |
  | +18° (mid May) | 68.2° | 0.40 | ~65 cm |

- **What holds:** the direction is right. The sun stands 18–26° west of south, so the shadow points that much east of north, and "tipped a little east" is correct for a time just past noon. The juxtaposition of watch and shadow does the outline's "near enough to the sun's noon" work.
- **What fails:** a typical stone bollard is 50–80 cm and a timber post more. Most readers will picture something taller than about 40–55 cm, and its shadow would be two or three sandal-lengths.
- **Minimal fix:** "…the mooring post laid a short shadow on the stone, tipped a little east." (−3). Or keep the ruler and make the post squat: "the squat stone bollard by my foot".
- **Cascade risk:** none. Felix's "since the shadow was over by that post" (l.16) still works.

### [W-04] "by Castor" is the women's oath
- **Audit:** 4 (world: language)
- **Evidence:** l.78, the gray sailor: "Then get your mules up, **by Castor**, the yard's nearly there."
- **Problem:** in Latin usage *ecastor/mecastor* was a woman's oath. Gellius, *NA* 11.6: Roman men did not swear by Castor, nor women by Hercules. A man swears *edepol*, by Pollux.
- **Severity:** WARN. Classicist readers know this line, and the book's narrator is a classicist.
- **Minimal fix:** "by Pollux" (0 words). It also avoids echoing the Kirrha-road talker's "By the Twins" (Ch.12).
- **Cascade risk:** update the Ch.18 walk-on block in the character bible, which quotes "by Castor".

### [W-05] Pacuvius's "before there were priests" inverts the history
- **Audit:** 4 (world: institutions)
- **Evidence:** l.60 "It wants no priest and no cake, only the two of you saying so with two others to hear it, **the way it was done before there were priests to ask**, and I don't care to be told how they manage it in Corinth."
- **Problem:**
  - The oldest Roman form, *confarreatio*, is precisely the one that *had* the priests (the flamen Dialis and the pontifex) and the spelt cake.
  - Marriage by plain consent (*sine manu*) is the later norm, not the primeval one.
  - The clause is a character's folk claim, but Mara would know it is backwards and the page lets it stand.
  - The rest of the speech is sound: no priest, no cake, consent, and his own two witnesses as proof for the mother-in-law.
- **Minimal fix:** cut the clause (−10): "…only the two of you saying so with two others to hear it, and I don't care to be told how they manage it in Corinth."
- **Cascade risk:** the Pacuvius card quotes the clause and calls the rule "stated once in the book". Update the card (see W-14). The daughter's "Yours had a cake" (l.98) still pays off "no cake".

### [W-06] A barrel at Lechaion in AD 72
- **Audit:** 4 (world: material culture)
- **Evidence:** l.8 "across the basin somebody was hammering a barrel hoop, two blows and a rest"
- **Problem:**
  - Coopered barrels are a north-western, Gallic and Alpine container in the 1st century AD.
  - The Aegean and Corinthian trade moved in amphorae. The book itself shows this: Ch.16's coaster carries oil jars.
  - A cooper at work is an unlikely first sound on a Greek quay, and a sharp reader will notice it in the opening paragraph.
- **Minimal fix:** "somebody was hammering at a hull, two blows and a rest, two blows and a rest" (0 words). This keeps the designed rhythm. "Hammering at" and "a hull" have no prior uses.
- **Cascade risk:** none.

### [W-07] Mara's voice failing as a body reaction is a retired channel
- **Audit:** 1c (behavior) / voice drift
- **Evidence:** l.74 "'Yes.' **There was no voice under it, and it broke in the middle with the run still in it.** 'Will you?'"
- **The bible's rule** (at-risk after Ch.6): "Mara's voice failing as her body's reaction … RETIRED for Ch.7–9. The next mapped body break is Ch.20's weeping; any body rebel before then uses a different channel." The only surviving earlier use is Ch.5 l.325 ("The voice went on me there").
- **The second problem:** the sentence makes the run a body-state for the third time in under 70 lines:
  - l.8 "the taste of blood in my mouth from running";
  - l.36 "The run was in my legs and my ears were full of my own blood";
  - l.74 "with the run still in it".
  - l.54 already gives the breath beat: "I found enough breath for Latin, if not much of it."
- **Minimal fix:** '"Yes," I said. "Will you?"' (−17). The ten words are unchanged.
- **Cascade risk:** the comment header's "Ten words" line is unchanged.

### [W-08] Mara's Greek is contracted once
- **Audit:** 1c / voice drift (Mara's card: her Greek stays uncontracted, held from Ch.6 through Ch.17)
- **Evidence:** l.86 "**We're** all of us watching the yard," I told him.
- **Problem:** this is to Felix, in Greek. Every other Mara line in the chapter is uncontracted: "I am a free woman," / "We were the only two people leaving," / "Ask her," and so on.
- **Minimal fix:** "We are all of us watching the yard," (+1).

### [W-09] The "without" family reaches third uses book-wide, and the chapter has the book's highest density
- **Audit:** voice drift (NO TICS; STATE guardrail: "any phrase recurring 3+ times across the book that is not an allowlisted motif is a defect the editor removes before finalize")
- **Density:** Ch.18 has **7** "without" (6 adverbial), **2.65/1k**. The book's previous high is Ch.7 at 1.79/1k, and the Ch.15–17 average is about 0.33/1k. Earlier chains already cut this family (Ch.2 audit "Keep one 'without looking'"; Ch.12 disruptor "'without looking' family cut"; Ch.17 disruptor cut "without turning her head").
- **Third uses:**
  - **"without stopping"**: l.82 (Felix crying) and l.140 ("Valens, chasing the black, shouted without stopping."), plus Ch.17 l.286 "without stopping his song" = **3**.
  - **"said X, without turning [round/around/his head]"** as a tag tail: Ch.1 l.273, Ch.5 l.69, and l.98 "said the master, without turning round" = **3**.
  - **"without being [participle]"**: Ch.1 l.255 "without being asked", Ch.12 l.100 "without being told", and l.102 "moved without being shouted at" = **3**.
- **Minimal fixes:**
  - l.98: '"Yours had a cake," said the master, and the girl considered that…' (cut ", without turning round", −3).
  - l.140: "Valens shouted back, chasing the black." (−1).
  - l.102: "…small and steady, the only thing moving on that quay that nobody was shouting at." (+1). The phrase has no prior use.
  - Keep l.82 (Felix's "out loud and without stopping"); it becomes the chapter's one use.
- **Result:** Ch.18 goes to 4 "without" (1.5/1k), and none of the three frames reaches a 3rd use.
- **Cascade risk:** none. "Over his shoulder" was avoided as a replacement because it already has 2 prior uses (Ch.4, Ch.14).

### [W-10] Voice-bank frame lift from sample-09 (Fenn's reserved Ch.25 line)
- **Audit:** voice drift (voice-bank lift; the gate reads samples at 5+ words, and this is a slotted frame, so it missed it)
- **Evidence:** l.30 (the master) "Your boy's **been sitting on that** plank **since the** third hour". The source is `voice-bank/samples/sample-09-dialogue-fenn.md` l.16 "I've **been sitting on that** number **since the** quake."
- **Problems:**
  - That is Fenn's date line, budgeted for Ch.25. Printing its frame here makes Ch.25 the echo.
  - In the same chapter, Felix has l.84 "I've been sat in it since sunup", so the "been sitting/sat in X since Y" frame is used twice within 55 lines.
- **Minimal fix:** "Your boy's been on that plank since the third hour" (−1).
- **Cascade risk:** none. Felix's "been sat in it" (his dialect) stays as the chapter's one use.

### [W-11] Felix borrows Valens's Ch.16 mule command
- **Audit:** voice drift (command/spoken-line echo the scan cannot see: different speaker, slotted)
- **Evidence:** l.116 "'**Up**,' said Felix. '**Up, you.** You went on a boat before…'" The source is Ch.16 l.424, Valens to the fallen black: "Up, now, you old fool. Up,"
- **Problem:** the same doubled "Up … you … Up" to a mule, two chapters apart. Felix copying Valens could be character, but the page does not frame it as imitation, so it reads as the narrator reusing a line.
- **Minimal fix:** "'On, you,' said Felix. 'You went on a boat before…'" (−1). The phrase has no prior use.

### [W-12] "the heat of him" reused from the Ch.15 heat scene
- **Audit:** voice drift (cross-chapter lift; stop-word-bounded, so below the gate)
- **Evidence:** l.102 "The case held **the heat of him**." The source is Ch.15 l.574 "as I felt the doorway's draft and **the heat of him** and the grit of the earth floor".
- **Problem:** this is the first union's phrase, reused on the watch.
- **Minimal fix:** "The case was warm from him." (−1). It also answers Ch.6 l.242 ("still warm on the inside of the band") without repeating it.

### [W-13] "twice over" at its 5th book-wide use, now in Valens's mouth
- **Audit:** voice drift (NO TICS 3+ rule; bleed of narrator phrasing into Valens)
- **Evidence:** l.38 '"I'll pay the fare again," Valens said. "**Twice over.**"'
- **Prior uses** (all Mara's narration): Ch.2 l.3, Ch.9 l.276, Ch.10 l.44, Ch.13 l.238.
- **Minimal fix:** cut "Twice over." (−2). His offer stands on "I'll pay the fare again", and the master's "It isn't the fare." answers it unchanged.

### [W-14] The character bible lags the page (Pacuvius card and the Ch.18 walk-on block)
- **Audit:** 6 (state divergence: bible vs manuscript)
- **The Pacuvius card's "Ch.18 as written" quotes lines that dialogue-polish and the disruptor changed or cut:**
  - "telling my men about a mountain" → page: "telling the crew";
  - "Then Delphi can have you back." → cut;
  - "Nobody's carrying anybody's wife onto my ship, nor anybody's woman either." → page: "I'll put no man's wife aboard, nor any man's woman either.";
  - "My man at the plank can stand for it, and your boy." → page: "That one at the plank can stand for it, and the boy.";
  - "Nobody's throwing anything at my ship." → page: "Throw a nut at this ship and you'll swim after her.";
  - "That's the yard! … That's my yard at the top! On my ship or off my plank" → page: "The yard's up! … Aboard or off the plank, the lot of you, and I'm not particular which!".
- **The walk-on block also lags:**
  - the fish-seller's "Whose is the black?" → page: "That black's yours, is she?";
  - "he throws a sprat and hits a dog" → the dog was cut ("the fish-seller threw one after her");
  - the plank sailor's "by Castor" (if W-04 is applied).
- **Fix:** resync both from the final page at finalize. If W-05 is applied, strike the "before there were priests" clause from the card's line list and from its Syntax note.

---

## INFO

### [I-01] Roman marriage: the page's framing is safe (the brief's question)
- **The rule:** consent (*affectio maritalis*) between parties with capacity made a marriage. No priest, ceremony or registration was legally required. Witnesses were evidence, not a constituent element.
- **Valens:** formally manumitted by a citizen lanista and entered before a magistrate, so a Roman citizen *libertus* (Gaius Iulius Valens).
- **Mara:** registered at Delphi as Kallia's free kinswoman "from Syracuse", so a *peregrina*. There is no conubium between them.
- **The result** is *matrimonium iuris gentium* (*non iustum*): **still a lawful marriage, not concubinage**.
- **Other bars:** none apply. The lex Iulia's bars on marrying freedpersons applied to the senatorial order. A woman *sui iuris* needed no tutor's consent to marry *sine manu*.
- **The page claims only consent before two hearers**, to satisfy a shipmaster. It never claims citizen consequences.
- **Forward note for the architect** (Ch.22 onward):
  - Without conubium, Lucius and Aelia take their mother's peregrine status (the lex Minicia; Gaius, *Inst.* 1.78) and are not in Valens's *potestas*.
  - No later chapter should treat them as Roman citizens by birth unless a grant (for example, after the Rome suit) supplies it.

### [I-02] The master's refusal and the daughter's marriage both check out
- **The refusal:** under the lex Iulia de adulteriis, harbouring or aiding an adulteress was *lenocinium*. That gives Pacuvius a real legal fear, and the Ostia anecdote (l.40) gives him a personal one.
- **The daughter:** "married at the Kalends to a man at Puteoli she's never set eyes on, and I'm taking her to his mother's house" (l.40) matches Digest 23.2.5 (Pomponius). A woman may marry an absent man by letter or messenger, provided she is led into his house. The voyage *is* her *deductio*.
- "Yours had a cake" (a *mustaceum*) is right.
- Felix's nuts (l.62) are right for both cultures: Roman *sparsio nucum*, and the Greek *katachysmata* showered on a bride.

### [I-03] The route and duration are not stated on the page (handoff to Ch.19)
- **The realistic route:** from Lechaion west down the Corinthian Gulf, through the Rhion narrows, across the Ionian to the toe of Italy, through the Straits of Messina, and up the Tyrrhenian coast to Puteoli. In spring, with mixed winds, that is about **7–12 days**.
- **Wrong routes:** round Cape Malea is the eastern route, and it belongs to Cenchreae and the diolkos, not to Lechaion.
- **On the page:** Ch.17's "a day out to sea" by Celer's supper is consistent. The tow boat off the bow (l.14) is the right answer to an onshore afternoon breeze at a north-facing harbor.
- **For Ch.19:** do not compress the crossing into a night. Any landfall (Rhegium, the Straits) is optional.

### [I-04] Harbor and ship details verified
- **Lechaion:** an artificial harbor with an outer harbor between moles and inner basins. "Across the basin" (l.8), "past the mole" (l.40, l.98) and "along the mole" (l.52) are consistent.
- **The ship:**
  - stern-to Mediterranean mooring, with the gangplank from the stern (l.10);
  - a goose-head (*cheniscus*) sternpost;
  - a square sail brailed through lead brail rings, with lines down its face (l.14);
  - the yard raised on a halyard and made fast (l.138);
  - cleats on the plank (l.156).
- **Mules as deck cargo** on a merchantman are plausible. A marble ship refusing them (l.50) is a nice true-to-trade touch. Blindfolding a balking animal (l.142) is real handling.
- **Small note:** the stern rope is lifted "on the mole" (l.138) while the ship lies "along the quay" (l.10). This only works if the quay runs along a mole, which is common. No fix needed.

### [I-05] The watch: full history checked, and every detail agrees
- **The history:**
  - **Ch.1** l.387–389: a 1966 Seiko, steel band, nick in the crystal at two o'clock; wound "between finger and thumb" after "My thumbnail found the crown"; set by the clock radio.
  - **Ch.2** l.33: three links out, so "snug against my wristbone".
  - **Ch.3** l.9: wound on the balcony. Worn on the left, implied by the left hand at Ch.3 l.139–141 (ENTITY: "ch-03:p70 implies the left").
  - **Ch.6** l.26: set "by the shortest shadow of her gatepost". Paid to Valens in **November AD 70** (l.242). Winding taught forward "until it will not go any more" (l.274–278). The band will not go round his wrist, so it goes in his belt pouch (l.288).
  - **Ch.7** l.100: the pale band. l.220: in his pouch.
  - **Ch.11** l.88–92: kept going; "he had not put a finger to the hands" (it runs fast against the spout's shadow). Felix sees the daily winding.
  - **Ch.12** l.132: the pouch is in Mara's hands, "the watch was going", and is given back at the stepping stones.
  - **Ch.13–17:** not mentioned.
  - **Ch.18:** returned. That makes 17 months, as the outline requires.
- **Ch.18's details agree with all of this:** "steel" and "links of the band" (l.102, l.108), the clasp (l.108–110), "the small nick by the two" (l.102), "the finest of the three hands" (Ch.6 "the thin seconds hand"), and Valens's thumb "too broad" (Ch.6 "His thumb covered the crown entirely").
- **Wrists:**
  - Plautia's gold is on the left: Ch.16 "On the left. It was made for the left."
  - The watch goes to the right, and "the wrong wrist" (l.112) is literal, because her habit was the left.
  - **From Ch.19 on, the watch is on her RIGHT wrist** unless the page moves it. This matters for Ch.26 ("winds the Seiko on her wrist while she sleeps"), Ch.41 and Ch.43–44.
- **The setting of the hands:**
  - The near-noon reading implies Valens learned to set the hands after Ch.11.
  - Pulling the crown out to set it was never shown being taught; Ch.6 taught winding only.
  - There is a plausible off-page path in the Ch.15–16 lover months.
  - By the outline's design ("Don't explain that he kept the watch wound"), leave it unexplained.
- **Flour** in the links and on the crystal (l.102) is consistent with Ch.17's baker's back door.

### [I-06] END-1 and foreshadowing: clean
- **Nothing on the page explains the watch, counts it down, or points it toward the tomb.**
  - "The only thing … that moved" is a comic aside.
  - "The watch sat on the wrong wrist and ticked." (l.112) is literal.
- This honors foundation §4f item 5: "no one ever calls it one".
- **Forward guard:** do not give Ch.24, Ch.32 or Ch.41 another one-line "…and ticked." paragraph, or it becomes a device.
- Felix's "you never died of it. Who ever died of a plank?" (l.116) is diegetic and comic, so it is allowed. The narrator never comments on it.
- Foreshadowing count by reading: 0.

### [I-07] The Ch.17 → Ch.18 handoff holds
- **Time:**
  - Ch.17: "near enough noon" at the oven, then "The sun was a little past its height" at the city's last gate.
  - About 3 km of gardens, part of it run, puts arrival near 12:35.
  - The watch reads 12:40 (l.104), and the shadow is short and tipped east. Consistent.
- **The sail** from Ch.17's last line is the goose ship's own (l.14). The hoisting becomes the master's deadline ("till the yard's at the top", l.60). This meets the outline's "not waved away".
- **Felix and the mules:**
  - On the quay since before sunrise with the household's freedman (Ch.17 l.278), so "since sunup" (l.84) and "He paid me at sunrise" (l.30).
  - Four mules: the dun, the black and the two unsold, which agrees with l.12 and l.146.
  - The bags and the fig in its jar are there.
- **Valens:**
  - The pine crown, "half bald" with resin on his fingers in Ch.17, becomes "mashed in his grip" and "a crown that's got no leaves on it" in Felix's word (l.134).
  - The flour on his arms (Ch.17 l.420) explains "Why are your arms white?" (l.16) and l.70.
  - Optional: after the resin, "His fingers smelled of bread" (l.110) could be pine. It is not a defect.
- **Mara's things:**
  - The borrowed dress and its hem (l.36) are consistent.
  - **The pen-knife is unchanged.** It was pushed into her belt in Ch.17, and Ch.18 neither mentions nor contradicts it.
  - The camera under her dress is unmentioned and consistent.
- **The leaf** is not mentioned. Ch.19's "The papers work" needs it still on Valens. Nothing in Ch.18 (the chase, the jar) contradicts that.

### [I-08] Pacuvius against his card: matches (apart from W-05 and W-14)
- **What matches:**
  - His attention is the far port's opinion: the mother-in-law and "the magistrate's people at Puteoli".
  - "It isn't the fare."
  - Long consequence run-ons, then a verdict: "Then she's nobody's, which is worse."
  - He never comes down the plank; the bare white foot is set down "with care".
  - "spread his hands" once; no oath; his daughter unnamed.
  - "my [ship/deck/girl]" appears 3 times, matching the polish.
- **Repetition:**
  - He says "no man's wife" twice (l.40, l.56). That falls within "answers an argument by restating the terms". Optional: vary l.40 to "a boy to say she isn't married".
  - The booking is varied three ways, as the card requires.
- **"Pacuvius":** an Oscan-Campanian nomen, apt for a Puteoli trader. He is named once, by the sailor (l.78), and is "the master" in narration.

### [I-09] Valens's voice: clean
- **The rules hold:** no simile or comparison in speech; no vow; no abstraction; bare "No." 0; questions practical ("Where's the freedman?", "Is there another ship for Italy?").
- **His lines fit his card:**
  - His footing orders come from the plank on the page: "Tread on the cleats," / "It gives in the middle."
  - "Keep off her heels" keeps his attention on the animal.
  - "He was watching the dun." (l.106) carries his evasion at the watch, which is right.
- **The ten words** are "Will you be my wife, Mara?" / "Yes." / "Will you?" / "Yes,", which is exactly 10, with no speech. This honors the outline's warning.
- "Nobody's coming after her." (l.58) is understatement of danger (his card), given Celer's man at the fountain in Ch.17. It is not an error.
- **Doublings:** the chapter has three: the hammer's "two blows and a rest" ×2 (designed), Felix's "I told him you'd come, I told him you'd come running" (his rush), and Valens's "Cover her eyes, Felix. Her eyes." Optional: cut "Her eyes." to keep Valens out of the shared doubling rhythm that Ch.4's audit flagged.

### [I-10] "The girl in the blue hood" is used three times, twice as the same paragraph opener
- **Evidence:** l.42 "a girl in a blue hood", then l.68 and l.96, both of which begin "The girl in the blue hood had …".
- **Optional fix:** l.96 "The girl had taken the cucumber out of her mouth." (−4). The role label then stays a description, not a tag.

### [I-11] The cucumber memory meets CP2-2 at the edge
- **What meets the rule:**
  - It is triggered in scene (l.68, the girl's bitter end).
  - It is two sentences, well under the "longer memory" size.
  - It does not close on a lost name.
  - Mara's mother is consistent with Ch.14.
  - The rubbing-out-the-bitterness practice is a real folk method.
- **What is at the edge:** the paragraph ends inside the memory. The return to the scene is the next paragraph ("Valens faced me…"), which is acceptable. If the editor wants the return inside the paragraph, the trigger can carry it, but no fix is required.
- **Silence:** the memory's silence about her mother's absence at her wedding is good subtext. Do not gloss it.

### [I-12] "told the harbor" is the chapter's one "said/told the [non-listener]"
- **Evidence:** l.94 "the sailor told the harbor".
- **The cap** is 1 per chapter (bible at-risk after Ch.5), so it is within the cap.
- **Book-wide, though**, it is the 5th: Ch.5 "said to the dark", Ch.7 "told the room", Ch.13 "told the terrace", Ch.15 "told the roof", and now Ch.18. **WATCH:** give Ch.19 none.

### [I-13] Celer's "every day" against the master's "not before the Ides"
- Ch.17 has Celer say "Ships leave Lechaion every day now the sea's open". Ch.18 l.50 has the master say "Not out of this harbor before the Ides", and Felix confirms "Not one of them's going over but him" (l.52).
- These are consistent: Celer is speaking of ships in general, and the master of ships for Italy.

### [I-14] The freedman's movements
- The master says he went "away to the races" at sunrise (l.46). Felix says "Gone back up for the men's race" (l.22). Ch.17 says the men's race comes later the same day.
- Both accounts fit: he went out to the Isthmus for the day. No fix.

### [I-15] "with that face" (l.40)
- This is the first time anyone characterises Valens's face aloud. It is consistent with the arena (the nick in his eyebrow, Ch.11) and the flour, and it contradicts no body fact. No fix.

### [I-16] Foundation table row 18 is stale
- **Evidence:** foundation §4 table, row 18: "The watch, given back on a **wet** quay as a wedding gift, wound".
- **Conflict:** the patched outline and the page have the quay dry and sunlit ("spray is fine, rain is not"; l.8 "The stone was dry and glaring").
- **Fix:** amend foundation to "sunlit quay". The prose wins.

### [I-17] Handoff notes for the Ch.19 writer
- **"By the time the grain ship…"** in the outline's opening example would misname the vessel.
  - Ch.18's ship is Pacuvius's goose-stern merchantman, with its cargo unstated.
  - Alexandrian grain ships did not run Lechaion–Puteoli.
  - Use the goose ship, or the master's ship.
- **Who is aboard:** Pacuvius, his daughter (bound for the mother-in-law's house) and the gray sailor. The card says he gets "something else" if he returns. "The magistrate's people at Puteoli" (l.40) primes the clerk Valens is sure has marked him; keep them separate people.
- **Booking:** the passengers are booked as "a muleteer, with a wife and a boy". That is the account Pacuvius will give at Puteoli.
- **Felix's tunic** is still knotted over the dun's eyes, unless returned on the page.
- **The watch is on Mara's right wrist** (I-05).
- **The leaf** is under Valens's tunic.
- **The knife** is in Mara's belt.

### [I-18] Gates and counts (for the record)
- 2,636 words. Dialogue 33.6%. Em-dash 1 (Mara cut off, l.54). Ellipsis 1 (l.40, the master outrunning Mara's Latin, which is a good comprehension beat consistent with Ch.16's "When it runs, I lose it").
- Similes 3 ("as if nothing in Achaea…", "the way cords hold up a blind", "like a diving board"). They are characterizing, use 1998 domains, and none is reused book-wide.
- Credential asides 0. Kneel/crouch 0. "So" openers 0 (the tool's WATCH for 5 consecutive chapters is about other chapters, not this one).
- Tic gate, voice-wear and the echo scan are all clean.

---

## TRACKING DATABASES (Ch.18 additions)

### Character facts (new on the page)
| Character | Fact | Line |
|---|---|---|
| Mara | Watch on her **right** wrist (left carries Plautia's gold, which has "a child's teeth in it already") | l.108–112 |
| Mara | Married to Valens on Lechaion quay, consent before Felix and the gray sailor | l.72–78 |
| Mara | Mother: cut the bitter cucumber end, rubbed the faces to a froth, ate the end standing with salt | l.68 |
| Valens | Flour dried in his forearm hair; fingers smell of bread; thumb too broad for the watch's catch; closes it with his nail | l.70, l.110 |
| Valens | Proposes in six words; returns the watch without speech | l.72, l.100 |
| Felix | Cries open-mouthed ("It's the sun… Don't look at me."); in his loincloth, every rib showing; tunic used as the dun's blindfold; wears the pine crown | l.82–88, l.142–148 |
| Pacuvius (NEW, named once) | Master of the goose-stern ship; leather cap, tunic hitched through his belt; one sandal lost, left foot bare and very white; harbor Latin; a daughter married at the Kalends to a man at Puteoli | l.24–60, l.98 |
| The master's daughter | Blue hood; eats a cucumber; "was mine like that?" | l.42, l.96 |
| The gray sailor | Tar to the elbows; witness; kicked by the dun into a coil of cable | l.78, l.120–126 |

### Timeline
- **Spring AD 72**, the boys' race day of the games for Titus's triumph. The day falls between the Kalends and the Ides of the month (l.40, l.50).
  - Sunrise: the freedman pays the master. Felix is on the quay with the mules.
  - Third hour: Felix is on the plank.
  - About 12:35–12:40: Mara and Valens arrive.
  - The wedding, the watch at "twenty to one", then the loading.
  - The ship is ready to cast off on the afternoon breeze, under tow.

### Knowledge
| Item | Who knows | How |
|---|---|---|
| They were not married before today | the master and "every man on my deck" | Felix told the crew (l.30–34) |
| They are married now | Pacuvius ("I heard."), the sailor, Felix, the daughter, the rowers by implication | witnessed (l.72–80) |
| The booking "muleteer, wife, boy" | Pacuvius | the freedman at sunrise (l.30) |
| The theft / the leaf | Felix: **not shown** (W-01) | — |

### Plot threads
- **The watch** (re-read thread): RETURNED (Ch.18). Next: wound without comment at Ch.24 and Ch.32; Valens winds it in the tomb at Ch.41.
- **Plautia's bracelet:** on her left wrist, chekhov_open.
- **Felix's tunic:** on the dun.
- **The pine crown:** on Felix.
- **Pacuvius's sandal:** spent.

---

## SUGGESTED YAML PATCHES (for entity-tracker; recommendations only, not applied)

```yaml
suggested_patches:
  - entity: "objects.fathers-seiko-watch"
    action: "update"
    value: "Ch.18: returned to Mara on Lechaion quay without speech (l.100); running, flour in the links and on the crystal; crown wound (see W-02 for the final wording); reads 'twenty to one' with a short post-shadow tipped east (near local noon, implying Valens set it; unexplained by design); on her RIGHT wrist, clasp closed by Valens (l.108-l.112)"
    reason: "custody change Valens -> Mara; wrist is new canon for Ch.19-44"
  - entity: "mara-reyes.relationships.valens"
    action: "update"
    value: "married (Ch.18): consent before witnesses (Felix, the plank sailor) on the quay; 'Will you be my wife, Mara?' / 'Yes.' / 'Will you?' / 'Yes,'"
    reason: "state change lovers -> spouses"
  - entity: "pacuvius"
    action: "create"
    reason: "new named character (l.78), master of the goose-stern merchantman; daughter unnamed"
  - entity: "felix.knowledge"
    action: "add"
    value: { fact: "Mara and Valens are married (witnessed; he stood for it)", learned: "ch-18:l.72-l.80", method: "witnessed" }
  - entity: "felix.knowledge_absent_ch18"
    action: "add"
    value: "whether the theft succeeded / what 'it' was (his 'Did you get it?' is unanswered; see W-01)"
  - entity: "plautias-bracelet"
    action: "update"
    value: "Ch.18: still on Mara's left wrist; she will not put the steel against it"
  - entity: "valens-pine-crown-for-felix"
    action: "update"
    value: "given to Felix on the quay (l.88); 'a crown that's got no leaves on it'; worn aboard"
```
