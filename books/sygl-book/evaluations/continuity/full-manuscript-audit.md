# Continuity Check: Full Manuscript — *Sygl*

**Date:** 2026-10-21
**Chapters reviewed:** 1–30 (manuscript/chapter-01.md … chapter-30.md, 92,812 words), read in order against
`Sygl_Complete.txt` (L4–1013), STATE.yaml `decisions`, book CLAUDE.md guardrails, project/foundation.md
(incl. Magic ledger), project/outline.md, character-bible.md. No ENTITY_STATE.yaml exists, so the tracking
databases were built from the text (Audit 6 skipped).
**Total issues found:** 30
**Critical:** 2 | **Warning:** 12 | **Note:** 16

Line numbers are `cat -n` lines in each chapter file (one paragraph per line). Every fix is the smallest
text change that removes the conflict. None adds plot. The three marked **AUTHOR CALL** need one new fact or
line, so they go to the author first.

---

## VERIFIED CLEAN (checked book-wide, no action)

- **Spelling and names:** no "sigil", "sygil", "Waisura" or "mausaelium". Viridia Vizer, Lora Aegis,
  Naisura, Aleric, Locklan and Summers are spelled the same everywhere. Ms. Summers, Mrs. Locklan and
  Mrs. Brown keep the same title throughout. The second "Aleric" on p.157 is correctly Leon (Ch.25 L178).
- **"Master":** appears only in Ch.9 (×3), Viridia's report of it in Ch.10, and "Of course, Master" in Ch.28.
  This matches the ruling.
- **Magic rules:**
  - The whip always comes from the right palm, which splits open by itself and closes after (Ch.20 L38/72, Ch.21 L108/136, Ch.27 L264).
  - The dagger forms in whichever hand is free: right in Ch.25 L146, left in Ch.27 L264.
  - The purification rune works as soon as it is carved. Only the arrow runes are charged (Ch.16 L300, Ch.18 L46).
  - Every conversion is palm to palm on the left hand.
- **Canon facts:**
  - Pierre wakes Bal (Ch.5).
  - Mrs. Brown's husband's affinity was Blood (Ch.4 L109).
  - Sygls are on the palm. Bal's tolerance for pain is noted without repeating the same wording.
  - "Sygldry" is used as the general term (Ch.1 L51, Ch.2 L197).
  - Bal recognises Viridia from the buggy (Ch.7 L117).
  - The duel is accepted on the page (Ch.28 L82).
  - "They cannot hear you" is Toma's line (Ch.29 L24).
  - The "Kona Niente" copy-paste slip is fixed (Ch.29 L206).
- **Payoffs that land:**
  - The heart ring pays off in Ch.21 L124.
  - The arrow-rune shirts are proposed in Ch.16 and finished in Ch.18.
  - The water snake (Ch.18) is called back in Ch.20, Ch.21 and Ch.23.
  - The two thrown vials pay off in Ch.29 L156.
  - The blood elemental is sent to Amelia's domain (Ch.29 L306).
  - The earth ring is bought (Ch.13), given (Ch.14), used (Ch.16) and twisted (Ch.19).
  - The card is on the nightstand in Ch.14 and Ch.15, and Viridia mentions it in Ch.16.
  - Bran is set up in Ch.13 and named in Ch.27.
  - Peter and Eric match the source. Marcus is reported in Ch.22 as the source has it.
- **Clocks and distances:**
  - Poison: dormant 24 hours, heart stops about 6 hours later (Ch.24 L168). "Six tomorrow night" (Ch.26 L74) and "close to six" (Ch.27 L68) agree.
  - Four to five days' ride, arriving "on the fifth day" (Ch.22 L92, Ch.23 L88).
  - Two days on foot, then Barda "by noon tomorrow", arriving "a little before noon" (Ch.27).
  - Two days unconscious and two days training (Ch.28).
  - Twenty miles via Whitehaven, then the pass an hour after camp (Ch.16–17).
  - The lake is "last week" in Ch.20 and Ch.21.
- **When information is revealed:**
  - The eight high priests first appear in Ch.5 L231.
  - War rules: told to Bal in Ch.18, to the girls in Ch.20, and the no-help rule in Ch.21.
  - Raizen's cheating appears in Ch.21 only.
  - The juggling talk is overheard in Ch.17 and confirmed in Ch.19 L104.
- **Props and wounds:**
  - Bal is shirtless and barefoot with the bandolier at the duel. He is still barefoot in Ch.30.
  - The rune kit is carried consistently from Ch.9 to Ch.11.
  - Bandit wounds: back and left forearm, still felt in Ch.17. Iro wounds: side, chest, back, right thigh, and the thigh is still felt in Ch.22.
  - The chest burn (Ch.27) is gone after the chalice (Ch.28 L192).

---

## CRITICAL ISSUES (must fix)

### [CRIT-001] The school sweater's sygl is on the back in some lines and on the chest/front in others
- **Audit:** 1b/4c, physical continuity. The author's canon is the back.
- **Chapters:** 5, 6, 7 against 6, 7, 11, 20.
- **Evidence (back, correct):**
  - Ch.6 L11: "She had the Tempus sygl on the back of her sweater."
  - Ch.7 L107: "Bal pulled his sweater around to look at the back. The blood sygl had come up there"
  - Ch.11 L6: "the blood sygl sat on the back of Amelia's tight black sweater"
  - Ch.20 L6: "the blood sygl between the shoulder blades"
- **Evidence (front, wrong):**
  - Ch.5 L121: "He gestured at Bal's chest, where a sygl would have been on a student's sweater."
  - Ch.5 L161: "a dark sweater with a blank place on the front"
  - Ch.6 L13: "Bal checked his own front, which was still blank"
  - Ch.7 L291: "A boy in a Terra sweater looked at the sygl on his chest"
- **Why it matters:** Ch.6 L11 and L13 contradict each other two sentences apart, and Ch.7 L107 and L291 do the same in one chapter.
- **Fix:**
  - Ch.5 L121: replace with "He gestured over his shoulder at his own back, where a student's sygl would sit."
  - Ch.5 L161: replace with "a dark sweater with a blank place between the shoulders"
  - Ch.6 L13: replace with "Bal twisted to check his own back, which was still blank"
  - Ch.7 L291: replace with "looked at the sygl on his back as he passed and then turned to stare at his face"
- **Cascade risk:** none. Ch.9 L52 ("the blood sygl on his sweater") is neutral.

### [CRIT-002] Viridia rides straight to an inn nobody has mentioned, and Amelia has already paid for rooms there **(AUTHOR CALL; the gap is in the source)**
- **Audit:** 3b, information flow / 5c, payoff without setup.
- **Chapters:** 22, 23, 24.
- **Evidence:**
  - Ch.22 L164–166: Xavier's Londra briefing names only the Three Boars.
  - Ch.22 L120: "Londra was new to her."
  - Ch.23 L122: "I usually stay at the Winespring when I'm here."
  - Ch.23 L146: she rides there with no directions, and "Bal sent Lora a questioning glance."
  - Ch.24 L14 and L24: Amelia's letter and payment arrived there "this morning".
  - Ch.24 L10: "Nobody should have known they were coming."
- **Why it matters:** The text raises the question itself (Bal's glance) and never answers it. A reader will ask how Viridia knew the Winespring and how Amelia knew to write there.
- **Fix (one line, adds a fact):** Ch.22 L166, at the end of Xavier's briefing, add: "If you need beds, our people use the Winespring, off North Street. It takes travelers of quality and doesn't ask questions."
- **Cascade risk:** none. Ch.23 L122 then reads as Viridia's cover story built on the briefing.

---

## WARNING ISSUES (should fix)

### [WARN-001] "Three thousand years" is spoken before Bal asks how long she was locked away
- **Audit:** 3b.
- **Evidence:**
  - Ch.4 L215: "I've been locked in a temple for three thousand years," Amelia said.
  - Ch.5 L211–213 (the next day): "How long were you in that place?" / "Almost three thousand."
  - Ch.6 L113 builds Bal's joke on the Ch.5 answer.
- **Fix:** Ch.4 L215: replace with "I've been locked in a temple longer than you'd believe," Amelia said. "I doubt it."

### [WARN-002] "Orientation class in two weeks", but the claiming is two days later (source slip)
- **Audit:** 2b.
- **Evidence:**
  - Ch.4 L25: "There's a new orientation class in two weeks."
  - Ch.4 L131: Mrs. Brown says he will "probably leave here in the morning".
  - The claiming is the day after the cottage (Ch.6).
- **Fix:** Ch.4 L25: replace "in two weeks" with "any day now".

### [WARN-003] The seasons jump around
- **Audit:** 2c.
- **Evidence:**
  - Ch.1 L49–51: Fredrick left "At the start of the summer" and "A month ago", so Ch.1 is midsummer.
  - About twelve days later, Ch.16 L8 has "red from the cold", L44 "Saturday came up cold and clear", and L46 "the frosty courtyard". Ch.17 L12 has "this late in the year".
  - Six weeks after that, Ch.20 L210 has "the first truly hot day in a while", and the heat continues through Ch.23–27.
- **Fix:**
  - Ch.1 L51: replace "At the start of the summer" with "Late in the summer".
  - Ch.16 L8: replace "red from the cold" with "pink from the wind".
  - Ch.16 L44: replace "cold and clear" with "cool and clear".
  - Ch.16 L46: replace "frosty courtyard" with "dewy courtyard".
- **Cascade risk:** none. The source's autumn leaves stay, and Ch.20 already frames the heat as a late hot spell.

### [WARN-004] The days of the week don't add up between Ch.15 and Ch.16, and "for weeks" is too early
- **Audit:** 2b.
- **Evidence:**
  - Ch.15 L142: "The weekend was a few days off."
  - Ch.16 L6–8 then runs through "On Monday…On Tuesday…By Wednesday" before Saturday.
  - Ch.13 L476: the job is due "by the end of the weekend".
  - Ch.16 L144: "Bal had been practicing nothing else for weeks". Only about ten days have passed since the claiming.
- **Fix:**
  - Ch.16 L6: replace "On Monday Lora asked" with "The next day Lora asked".
  - Ch.16 L8: replace "On Tuesday she asked again" with "The day after, she asked again".
  - Ch.16 L144: replace "for weeks" with "since his first class".

### [WARN-005] Amelia tows Bal along, but that gesture belongs to Viridia (author rule: no shared gestures)
- **Audit:** 6, repeated gesture.
- **Evidence:**
  - Amelia: Ch.3 L79 "towing him along behind her"; Ch.4 L217 "She towed him toward the door"; Ch.4 L213 "Bal let himself be pulled up off the bed".
  - Viridia: Ch.7 L163–165 "grabbed him by the sleeve… already towing him"; Ch.14 L46 "towed her in"; Ch.24 L280–282 "started towing him… He let himself be towed".
- **Note:** character-bible.md L82–83 says Amelia's Ch.3–4 versions "were varied", but the text was not changed.
- **Fix:**
  - Ch.3 L79: replace from "She kept hold of the new one…" with "She kept hold of the new one and walked beside him across the hall toward the doors, explaining as she went."
  - Ch.4 L213: replace with "Bal got up off the bed."
  - Ch.4 L217: replace with "She went out ahead of him in search of sustenance."

### [WARN-006] Bal's idle "who does the chores?" musing recurs about 20 times and becomes a narrator habit
- **Audit:** 6, repetition the style gates can't catch.
- **Where it appears:** Ch.5 L99, 6 L87, 7 L187, 9 L50, 11 L44, 13 L118, 14 L24, 16 L16, 17 L52, 19 L138, 21 L46, 22 L174 and L178, 23 L98, 28 L204, 29 L60 and L214, 30 L92.
- **Why it matters:**
  - Most take the same form ("who washed / who swept / who carried…").
  - Several fall in the tensest moments: just before the conversion (Ch.19), the war-council plan (Ch.22), the duel arena (Ch.29), and the god-tribunal (Ch.29).
- **Fix:** keep the Ch.7 plates musing and its Ch.30 callback, which are a deliberate pair. Cut these:
  - Ch.19 L138 (whole paragraph)
  - Ch.22 L174, the sentence "Who carried in the barrels… for his trouble?"
  - Ch.22 L178 (whole paragraph)
  - Ch.23 L98 (whole paragraph)
  - Ch.28 L204, the sentence "Once, between bouts, he sprawled… wondering whether it ever got dizzy."
  - Ch.29 L60, from "He wondered who had swept…" to the end of the paragraph
  - Ch.29 L214, the last sentence ("Bal caught himself wondering…eat.")
  - Ch.13 L118, the clause ", and whether anyone had ever told him about tongs, and whether he would listen"
  - Ch.14 L24, the first two sentences
  - Ch.16 L16, the sentences "He wondered what a squirrel… bigger nuts."

### [WARN-007] Amelia swings her feet six times, and the Ch.15 and Ch.20 entrances are nearly identical
- **Audit:** 6.
- **Evidence:**
  - Ch.2 L183, Ch.4 L31, Ch.5 L19, Ch.10 L204 (from the source).
  - Ch.15 L116: "perched on it, swinging one foot"
  - Ch.20 L148: "She sat on the arm of the couch, swinging one foot."
- **Fix:**
  - Ch.4 L31: replace with "Amelia sat back in her chair."
  - Ch.5 L19: cut "swinging her heels against the cupboard doors,".
  - Ch.15 L116: cut "swinging one foot,".
  - Ch.20 L148: cut ", swinging one foot".

### [WARN-008] Ch.30 adds an invented detail that contradicts Viridia's village
- **Audit:** 1c/5d. The Ch.30 author decision says to use "only facts already on the page".
- **Evidence:**
  - Ch.30 L22: "I knew that sound. Half my childhood was under it. Nobody else can make it thunder in fair weather."
  - This conflicts with Ch.27 L36–40 ("Are sygls really that rare in your village?" / "Yeah") and Ch.13 L218.
  - It is also new backstory.
- **Fix:** Ch.30 L22: cut from "I knew that sound." up to "fair weather." Keep "A loose thread hung off her cuff, and she wound it round her finger."

### [WARN-009] Viridia recognises Aleric from a description we never see
- **Audit:** 3b. The handoff is plausible off-page, but the source gives the description.
- **Evidence:**
  - Ch.24 L276: "I recognized him from what Thad told us. He's got a long scar right through his right eye."
  - Ch.22 never describes Aleric.
- **Fix:** Ch.22 L84, after "has already started for Londra.", add Thad: "Watch for Aleric. Scar straight down through his right eye." This uses the foundation's canon fact.

### [WARN-010] Toma's fate after Ch.29 is dropped **(AUTHOR CALL; also open in the source)**
- **Audit:** 5a.
- **Evidence:**
  - Ch.29 L242: "The girls vanished… Toma was gone with them." Aren sends all three to the school (L246).
  - Ch.30 never mentions him. A converted enemy High Priest now in the castle is an open question for the reader.
- **Fix (needs approval):** one line in the girls' account, Ch.30 near L40: "Toma came through with us," Lora said. "They took him somewhere in the castle." Or leave it open on purpose.

### [WARN-011] The same image is used three times for Amelia vanishing: the seat springing back up
- **Audit:** 6.
- **Evidence:**
  - Ch.7 L53: "The cushion beside him slowly puffed back up."
  - Ch.15 L12: "The mattress on his side came back up under him, slowly, as a cushion does when someone stands."
  - Ch.21 L172: "the grass under her feet was springing back up."
- **Fix:**
  - Ch.15 L12: cut "The mattress on his side came back up under him, slowly, as a cushion does when someone stands. Nobody had stood."
  - Ch.21 L172: replace with "Then she was gone."

### [WARN-012] Bal's fist closing and reopening repeats across the book
- **Audit:** 6.
- **Evidence:**
  - Ch.4 L121 and Ch.26 L72 (from the source; keep).
  - Ch.29 L248 (from the source: "clenchs his fist but nods"; keep).
  - Ch.6 L41: "His left hand closed. He opened it again."
  - Ch.30 L36: "Bal found his hands had closed into fists. He opened them again."
- **Fix:** delete Ch.6 L41 and Ch.30 L36.

---

## NOTE ISSUES (polish)

- **[NOTE-001] Many chapters end at bedtime.**
  - Ch.5, 8, 14, 15, 19 and 26 end on bed or sleep, and Ch.12 and 16 end on lying down.
  - This mostly follows the source. Trimming one helps.
  - **Fix:** end Ch.15 at L142 "…Saturday they would go find Lora's flowers." and cut L144.
- **[NOTE-002] Ch.24 L228: the speaker is unclear and differs from the source.** In the source, Bal asks "I take it… drinks?" **Fix:** add the tag `"…into their drinks?" Bal asked.`
- **[NOTE-003] Two quotations sit back to back with no tag in one paragraph.** This reads as two speakers.
  - Places: Ch.7 L39, Ch.10 L52, Ch.15 L56, Ch.20 L156, Ch.23 L16, Ch.26 L56, Ch.30 L30.
  - **Fix:** join each pair into a single quotation by deleting the `" "` between them.
- **[NOTE-004] Ch.4 L81–83 tags Amelia twice in a row ("Mostly," Amelia said. / "It was that," she said).** **Fix:** `"Mostly," Amelia said. "It was that, and the fact they knew they couldn't win in a straight-up fight with me."`
- **[NOTE-005] Ch.9 L204 credits Amelia with full directions to the library.** In Ch.7 L39 she gave only "second floor". **Fix:** "The library was on the second floor, as Amelia had said: straight up the main stairs, a right at the top, and then the second door on the left."
- **[NOTE-006] Ch.14 L36 says "while she lay on his bed reading it".** She read the diary on the High Priest's bed in the canyon temple (Ch.11 L168). **Fix:** "on the High Priest's bed".
- **[NOTE-007] Ch.5 L13 reuses the flexed new hand, which was meant to appear only in Ch.3.** **Fix:** replace with "Bal stayed put a little longer with his new hand on the blanket. It was still there. He got up."
- **[NOTE-008] Ch.10 L136 has the rapier in "the left hand Amelia had given him".** Elsewhere Bal fights right-handed: Ch.21 L100 swings the "left fist" while holding the sword. **Fix:** replace with "his hand had quit gripping the hilt".
- **[NOTE-009] "Months" is used where only 8–10 weeks have passed.**
  - Ch.19 L136: "months ago". Fix: "weeks ago".
  - Ch.26 L52: "all the months". Fix: "all the weeks".
  - Ch.28 L158: "It had only been months." Fix: "It had been barely two months."
- **[NOTE-010] Ch.30 L120 says "Nobody had to be anywhere in the morning but here."** The two-week break started the day before they left (Ch.20 L156), and the duel falls on about day 15, so classes resume. **Fix:** cut the sentence.
- **[NOTE-011] Ch.20 L100 says "Where's Terra, even?"** The book names gods, not sygls. **Fix:** "Where's Naisura, even?"
- **[NOTE-012] Minor dropped ends, inherited from the source. Fine to leave.**
  - Jazen's message for Fern is never delivered (Ch.27 L210).
  - Barda is left grazing at the battlefield (Ch.27 L254).
  - The first storm mage, stabbed in the eye and kicked off the platform, is never accounted for (Ch.27 L270).
  - Lora's raven appears only in Ch.16.
  - Lora's three flowers and Ms. Summers' two potions are never collected. The Ch.21 healing potion could be read as one of them, but the text doesn't say so.
  - Thad and Xavier are absent after Ch.28.
- **[NOTE-013] Identical "both hands, hauled to feet" staging for two characters.** Ch.3 L79 (Amelia to Bal) and Ch.24 L170 (Bal to Lora). **Fix:** in Ch.24, "pulled her up off the floor and kissed her."
- **[NOTE-014] The water snake changes size.** Ch.18 L58 says its head is "as big as a rowboat". Ch.21 L14 says "a snake… as big as a barn". This is fine as Bal's exaggeration. Optional fix: "as long as a barn".
- **[NOTE-015] Ch.26 L32 imagines Mrs. Locklan sending supper "to an empty room".** But they carried all their bags down that morning (Ch.25 L36). **Fix:** cut the paragraph.
- **[NOTE-016] The blood tear is wiped with the thumb in both Ch.5 L235 and Ch.14 L76.** Both are source beats; no change needed. Just keep Ch.14's handling different, as it now is.

---

## FIX LIST BY CHAPTER (for the editor)

| Ch | Line | Change | ID |
|---|---|---|---|
| 1 | 51 | "At the start of the summer" → "Late in the summer" | WARN-003 |
| 3 | 79 | "…towing him along behind her, explaining as she went." → "She kept hold of the new one and walked beside him across the hall toward the doors, explaining as she went." | WARN-005 |
| 4 | 25 | "in two weeks" → "any day now" | WARN-002 |
| 4 | 31 | → "Amelia sat back in her chair." | WARN-007 |
| 4 | 81–83 | merge into one tag (see NOTE-004) | NOTE-004 |
| 4 | 213 | → "Bal got up off the bed." | WARN-005 |
| 4 | 215 | "for three thousand years" → "longer than you'd believe" | WARN-001 |
| 4 | 217 | "She towed him toward the door…" → "She went out ahead of him in search of sustenance." | WARN-005 |
| 5 | 13 | flexing → "with his new hand on the blanket. It was still there." | NOTE-007 |
| 5 | 19 | cut "swinging her heels against the cupboard doors," | WARN-007 |
| 5 | 121 | gesture at his back, not his chest | CRIT-001 |
| 5 | 161 | "blank place on the front" → "blank place between the shoulders" | CRIT-001 |
| 6 | 13 | "checked his own front" → "twisted to check his own back" | CRIT-001 |
| 6 | 41 | delete | WARN-012 |
| 7 | 39 | join split quotation | NOTE-003 |
| 7 | 291 | "the sygl on his chest" → "the sygl on his back as he passed and then turned to stare at his face" | CRIT-001 |
| 9 | 204 | library directions per NOTE-005 | NOTE-005 |
| 10 | 52 | join split quotation | NOTE-003 |
| 10 | 136 | "the left hand Amelia had given him" → "his hand" | NOTE-008 |
| 13 | 118 | cut the tongs clause | WARN-006 |
| 14 | 24 | cut first two sentences (salt) | WARN-006 |
| 14 | 36 | "his bed" → "the High Priest's bed" | NOTE-006 |
| 15 | 12 | cut the mattress sentences | WARN-011 |
| 15 | 56 | join split quotation | NOTE-003 |
| 15 | 116 | cut "swinging one foot," | WARN-007 |
| 15 | 144 | cut (end chapter at L142) | NOTE-001 |
| 16 | 6, 8 | "On Monday" → "The next day"; "On Tuesday" → "The day after" | WARN-004 |
| 16 | 8, 44, 46 | cold/frost → wind/cool/dewy | WARN-003 |
| 16 | 16 | cut the squirrel sentences | WARN-006 |
| 16 | 144 | "for weeks" → "since his first class" | WARN-004 |
| 19 | 136 | "months ago" → "weeks ago" | NOTE-009 |
| 19 | 138 | delete paragraph | WARN-006 |
| 20 | 100 | "Terra" → "Naisura" | NOTE-011 |
| 20 | 148 | cut ", swinging one foot" | WARN-007 |
| 20 | 156 | join split quotation | NOTE-003 |
| 21 | 172 | → "Then she was gone." | WARN-011 |
| 22 | 84 | add Thad's line about Aleric's scar | WARN-009 |
| 22 | 166 | add the Winespring line (**AUTHOR CALL**) | CRIT-002 |
| 22 | 174, 178 | cut the drayman sentence; delete L178 | WARN-006 |
| 23 | 16 | join split quotation | NOTE-003 |
| 23 | 98 | delete paragraph | WARN-006 |
| 24 | 170 | → "pulled her up off the floor and kissed her" | NOTE-013 |
| 24 | 228 | add "Bal asked." | NOTE-002 |
| 26 | 32 | delete paragraph | NOTE-015 |
| 26 | 52 | "all the months" → "all the weeks" | NOTE-009 |
| 26 | 56 | join split quotation | NOTE-003 |
| 28 | 158 | → "It had been barely two months." | NOTE-009 |
| 28 | 204 | cut the hawk sentences | WARN-006 |
| 29 | 60 | cut from "He wondered who had swept…" | WARN-006 |
| 29 | 214 | cut the last sentence | WARN-006 |
| 30 | 22 | cut "I knew that sound… fair weather." | WARN-008 |
| 30 | 30 | join split quotation | NOTE-003 |
| 30 | 36 | delete | WARN-012 |
| 30 | ~40 | optional Toma line (**AUTHOR CALL**) | WARN-010 |
| 30 | 120 | cut "Nobody had to be anywhere in the morning but here." | NOTE-010 |

**Bible upkeep:** after WARN-005, character-bible.md L82–83 ("Amelia's Ch.3–4 versions were varied") will be
accurate. Until then it is not.

---

## TRACKING DATABASES

### Master timeline (day 1 = the temple)
| Day | Chapters | Events |
|---|---|---|
| 1 | 1–4 | Flight into the temple, the new hand, the bond, Mrs. Brown, packing |
| 2 | 5 | Pierre at 6:00, Verin, the portal, the cottage (an evening forest on the other plane), the feeding |
| 3 | 6–8 | Claiming, the dorm, Viridia, conversion talk, Amelia's origin |
| 4 | 9–12 | Familiar class, library, runes, Hopper, Lora, Raizen's army, canyon temple, the diary, "I like you too" |
| 5 | 13–14 | Free day: New Spring, Dawn Hall, the card |
| 6 | 15 | Make-up day, Lora at the Blood table, "Together" |
| ~7–11 | 16 | Week of homework (see WARN-004) |
| Sat/Sun | 16–17 | Bandits, Heath and the heart ring; Saegen Woods, the bear, juggling; back after curfew |
| +6 weeks | 18 | Jobs, flaming dagger, shirts, water snake (the last week), Fern, Toma's file, war rules |
| B0 | 19 | The rule announced; conversions; war declared that night |
| B0+1 | 20–22 | Sean and the whip; the lake; Iro; the council; the temple; the plan. The break starts tomorrow. |
| B1 | 23 | Depart at noon |
| B5 | 23–24 | Londra; James; poison brewing; Aleric seen |
| B6 | 24 | Brew done about 5 p.m. |
| B7 | 25–26 | Letter; Three Boars lunch; poison drunk around 1 p.m.; camp |
| B8 | 27 | Walking south; about 6 p.m. the thunder; girls taken |
| B9–10 | 27 | Two days on foot; Jazen and Barda |
| B11 | 27 | Night ride; battle before noon; Bal unconscious |
| B13 | 28 | Wakes; Toma's army in 2 hours; parley; blue cloth; chalice |
| B15 | 29–30 | Duel; Raizen confined; home (last day of the two-week break, see NOTE-010) |

### Character fact sheet (as written)
- **Bal:** 16. Blood sygl on the regrown left palm. Very high pain tolerance.
  - Wounds: back and left forearm (Ch.16); left side, chest and stomach cuts, back R-shoulder to L-hip, right thigh (Ch.21); chest burn (Ch.27); glass cuts (Ch.29).
  - Black horse (Ch.25–27).
  - Fights with the rapier right-handed (see NOTE-008).
- **Amelia:** looks a few years older than Bal; black hair to mid-back; red eyes; ruby teardrop earrings; black dress. Familiar brand on the forehead, which she can hide. Blood tears.
- **Viridia:** pale blue hair and eyes; a little taller than Bal; tan. Hair crackles when nervous and lies still when afraid (Ch.26). Spear. Earth ring on the left middle finger. Hopper (she). Green arrow-shirt.
- **Lora:** brown hair, long; glasses; freckles. Former Waves sygl. Her own enchanted rapier. A raven, sick (Ch.16).
- **Thad:** slight; black ponytail; pale; sharp nose; stubble with no colour given.
- **Xavier:** broad; tan; clear blue eyes; scarred hands.
- **Fern:** short and stocky; long grey beard; grey eyes.
- **Aleric:** scar from brow through the right eye, which is clouded. **Titus:** stout, red neck. **Leon:** youngest, wispy beard.
- **Toma:** 56. Blue robes sewn with lightning. Akora, his life-bonded storm elemental.
- **Heath:** grey-haired; pitted chain shirt; red-gold heart ring on the right hand.
- **Iro:** short brown hair; sharp blue eyes; woodsman's clothes.
- **Jazen Grey:** centurion. **Barda:** white warhorse, "he".

### Knowledge database (key items)
| Fact | Who learns it, and where | Status |
|---|---|---|
| Eight high priests trapped Amelia | Bal, Ch.5 | clean |
| Conversion mechanics | Bal, Ch.8; the girls, Ch.19 | clean |
| War rules | Bal, Ch.18; the girls, Ch.19 (partly) and Ch.20; no-help rule, Ch.21 | clean |
| Raizen's cheating | Ch.21, reported by Amelia | clean |
| Heart ring → Heath dead | Bal infers, Ch.21 L124 | clean |
| The juggling talk | Girls overhear Ch.17; confirmed Ch.19 | clean |
| Viridia's village and Bran | Overheard Ch.13; told Ch.27 | clean |
| How long Amelia was locked away | Ch.4 pre-empts Ch.5 | WARN-001 |
| The Winespring Inn | Viridia, Ch.23 | **no source** (CRIT-002) |
| What Aleric looks like | Viridia, Ch.24 | **no source** (WARN-009) |
| Toma has no gift (but does) | Fern's file Ch.18, paid off Ch.29 L106 | clean |

### Plot threads
| Thread | Opened | Status |
|---|---|---|
| Heart ring | 16 | Resolved 21 |
| Arrow-rune shirts | 16 | Resolved 18; deliberately never tested |
| Water snake | 18 | Resolved 21 and 23 |
| Thrown vials | 29 | Resolved 29 |
| Blood elemental | 29 | Sent to Amelia's domain (29) |
| Amelia's demand | 18 | Resolved 29 |
| Amelia's diary (Bal vows to find it) | 11 | Open, a light tease as in the source |
| Toma | 18 | **Open after 29** (WARN-010) |
| Bran | 13 | Resolved 27 |
| Peter | 11 | Complete |
| Thad and Xavier | 11 | Last seen 28 (NOTE-012) |
| Eric, Marcus | 22 | Single appearances as in the source |
| Ms. Summers' potions, Lora's flowers, Lora's raven, Jazen's message, Barda | various | Minor, from the source (NOTE-012) |
| Spell-ledger watch | whip in Ch.20, 21, 27, 29 | Within the source's use; no new spells found |
