# Continuity Audit: Chapter 10 (run 2, per-chapter drift audit)

**Date:** 2026-10-19
**Mode:** MANUSCRIPT AUDIT. Ch.10 "Kallia's Letter" is checked against Ch.1–9 as they stand on disk (all re-read in full), against the plan and against canon.
**Chapter reviewed:** `manuscript/chapters/chapter-10.md`
- Length: **2,528** prose words by `shape_check` (2,537 by style_check, 2,694 by `wc -w` with header). Target 2,800, range 2,500–3,100.
- **98 prose paragraphs**, 0 breaks.

**Paragraph numbering:** `ch-10:pN` counts prose paragraphs only. The title, the two HTML comments and `* * *` breaks are not counted. This is the ENTITY_STATE and Ch.6–9 audit convention. So p1 is "The letter had been folded down very small…" and p98 is "Out in the lane…". Prior-chapter cites use the files as they stand now: Ch.2 69, Ch.5 210, Ch.6 341, Ch.7 195, Ch.8 241, Ch.9 200.

**Read against:**
- outline.md: Ledger row 10, and `## Chapter 9` through `## Chapter 12`.
- STATE.yaml: guardrails, canon, ARCH decisions.
- foundation.md: the Kallia mini-profile ("her son Ariston enlisted with an auxiliary cohort in Syria").
- voice-dna.md: §6 and §8 (PLAIN STOP).
- character-bible.md:
  - the Kallia and Ariston cards, including every "as written" block;
  - the Ch.10 walk-on block;
  - every at-risk/spent block (after Ch.1, 3, 5, 6, 7, 7 cycle 1, 8, 8 cycle 1, 9, 9 cycle 1, 10) and the at-risk table.
- voice-bank/samples 01–13, read in full.
- ENTITY_STATE.yaml (committed: `last_updated_chapter: 9`, `chapters_tracked: [1..9]`). Its Ch.10 rows are plan rows (`source: outline:ch-10`). I treated them as unverified, so every Ch.10 fact below comes from the page.

**Mechanical baseline** (re-run read-only, `bash tools/check_chapter.sh 10`):
- **Style and grammar:** style clean (simile 0.4/1k, em-dash 0, foreshadow 0); grammar clean; rhythm 0.
- **Show/tell:** dialogue meter 36.7%.
- **Voice-wear and tics:** voice-wear strict is clean. The tic gate is clean, gesture layer included. Echo scan 0. Command-echo candidates 0.
- **Narration counts:** and-chains 1, credential asides 0, negation pivots 0, "So" openers 0.
- **Metaphor:** fig 0.8/1k, median sentence 15, 0% of sentences over 40 words.
- **Shape:** the shape audit is CLEAN.
- **My own sub-gate sweeps:** 3- to 6-grams against Ch.1–9 and the voice bank, keeping grams with 2+ content words. They found:
  - 2 cross-chapter echoes the 5-gram scan cannot see (W-07);
  - 3 voice-bank string hits, all from sample-12;
  - and, by shape, the sample-12 close rebuilt (W-01).

**Total findings:** 35. **CRITICAL: 1 | WARN: 9 | NOTE: 25**

**Summary:**
- **The CRITICAL is a timeline lock.** The Elean's "Three nights, till the god opens his house" puts the first consultation day three days after Ch.10. The outline needs more than a week for Ch.11 and "three days off" again at Ch.12. It is a two-word fix.
- **The heaviest WARN is the close.** The last five paragraphs reassemble sample-12, the voice bank's own Ch.10 calibration, out of its non-mandated furniture:
  - the letter "inside her belt";
  - "heard the broom";
  - the refold along the old folds;
  - Mara offering to ready the room and Kallia declining;
  - a goat complaining off-stage;
  - a legume chore as the final act.
- **The HARD no-parallel rule holds on the letter of the law.** No line names Mara's situation. The nearest miss is p97, "To myself it was a cheerful letter, from a man with a roof to sit on in the evenings." It is an image weighted with meaning, one paragraph from a PLAIN STOP, and it is Mara siding privately with the son who chose his made life (W-02).
- **Kallia is clean on every card axis.** She never sits and never touches Mara. She answers "How old was he?" with a task, says "Ariston" once, and never speaks of herself.

**Word ledger for the proposed fixes:** net about **−20** (CRIT 0; WARN −20). The chapter would land at about **2,508** by shape_check, still above the 2,500 floor, with 8 words of margin. See the THINNESS section before any further cut.

---

## Scorecard by category

| Category | Result |
|---|---|
| (a) Beats / ledger | **PASS.** Single-scene ✓ (Ch.9 Collage / Ch.11 Chronological, so no consecutive repeat). **Open:** "The letter had been folded down very small." is 8 words, an object → `short-punch` ✓, and the outline's ≤8 holds. **Close:** "Half the basket was still to clean, and I pulled it back onto my knees." is 15 words → `quiet` ✓. **Breaks:** 0 ✓. **Dialogue:** 36.7% meter (writer's comment: 39%), band 30–40 ✓ (top half). **Gear:** median 15, mid ✓. **Length:** 2,528 vs 2,800 (range floor 2,500) ✓, thin margin. **Beats:** 1 NON-NEGOTIABLE, Mara reads perfectly and her gift delivers the blow (p23–p58; p34 "the best Greek I had spoken since October") ✓. 2, Emesa, wife, child coming, discharge land; greetings by name and none for the room (p26, p33, p41, p44, p55, p59) ✓. 3 NON-NEGOTIABLE, Kallia says his name once, p93 "He can have Ariston's room" ✓. 4, she goes out to let the room to the pilgrim from Elis, and the chapter stops (p93–p98) ✓, but see W-01 (the stop's furniture) and W-02. The anchor holds: the broom still over the threshold when she goes out (p96) ✓. The emotional surprise, good news as bereavement, carries through the yawn (p43), the proxy questions (p35–p53) and "Tell him the baker's old mother is living." (p89) ✓. The chaos beat, the irrational second sweep, is at p91 ✓. The subtext questions "Is she Greek? / Can she weave?" are on the page verbatim (p35, p37) ✓. |
| (1) Character consistency | **Kallia: PASS.** **Never sits:** she stands to spin "beside the lean-to" (p21); looks "from where she stood" (p64); stops at "the foot of the stair" (p88). **Never touches Mara:** the letter is held out across the wool (p21); the obol is set "on the bottom stair, where I would have to pass it" (p90); no hand-to-hand anywhere. **Speech card:** short imperatives ("Water," p7; "Go on." p40; "Keep it out of the smoke," p65); practical questions ("Which arm?", "Bought?", "On what?", "And whoever carries it to Syria?"); a task as the answer to the unaskable ("How old was he, when he went?" → "Put a plate on those, or the mice will be in." p78–p79); one "Then" retort ("Then drink in Elis.", p12, at the cap); no proverb; nothing about herself. **Established facts:** the swept room is consistent with ch-07:p37: swept "every morning, before she did her own threshold or the court", broom left across, "the other one" for the house. p91's "At dawn they had been swept already" agrees, and the mid-afternoon second sweep is the new, irrational act ✓. The broom, "head against one post and the handle against the other", is compatible with Ch.7's "at the same slant" (ch-07:p37) and "at its slant" (ch-07:p186): a broom longer than the doorway spans post to post only on a slant ✓. "Not husbands and not sons" (ch-08:p1), "Who would I send in?" (ch-08:p107), "It's swept" (ch-07:p95) and "Letters." (ch-06:p73) are all explained retroactively, with nothing re-asked ✓. **The council-list line:** "You've had no other name on that line for years" (ch-07:p169) holds at a son gone two and a half years (N-01). **Widow** (ch-06:p315 "She's the widow Kallia's") fits "Here it's for the father's father" (p42), since the son would be named for her dead husband, and the Ch.7 husband's-brother question stays unanswered ✓. Gray hair under a dark kerchief (ch-05:p140, ch-08:p67) matches p92 ✓, and "shoes" matches ch-07:p175 ✓. **Nikaso: PASS.** She has black hair (ch-08:p13 ↔ p66). She is the wife of the man with the sieve (ch-08:p18), and the sieve still has its hole (ch-05:p189–p191, ch-08:p13 ↔ p69). "Midway along the lane" vs "three gates down" is in N-13. **Philista's drum** (ch-08:p45 ↔ p55) ✓. **Sostrata** is the baker's wife, and the baker's mother sleeps "between us" (ch-08:p194 ↔ p59) ✓. **Mara: PASS.** She reads Greek (ch-07:p151, ch-09:p7 "You read, then?" "Yes."). Her Greek is uncontracted. There is no English, so the CONTINUITY COMMITMENT holds. Credential asides 0. |
| (2) Timeline | **CRITICAL ×1 (C-01).** Otherwise PASS. Late winter AD 71, the same season as Ch.9: "the first afternoon of the year with heat enough in the sun to work without a cloak" (p21) follows Ch.9's almond flower (ch-09:p129). It does not contradict Ch.9's noon sun softening wax on the paving (ch-09:p93), which is surface heat, not cloakless air ✓. "In four months" (p20) and "since October" (p34) agree with ch-03 "I stepped out into October" ✓. The child "before the middle of the winter" (p41) is answered by "The middle of winter's gone by." (p51) ✓. The letter is dated "the twentieth of Hyperberetaios" (p58), ≈ 20 October in the Syro-Macedonian calendar, after the upper city fell in September (ch-05:p108) ✓; but see N-03 on compression. On the harbour road: the page attributes the winter delay to "nobody he'd trust was bound for Delphi" (p2), not to a shut road. That is better than the plan, since Valens hauled the Kirrha road all winter (ch-06:p313 "I was at Kirrha.") (N-04). |
| (3) Information flow | **PASS.** **Did Kallia ever tell Mara the son's name?** No. "Ariston" appears on the page twice: inside the letter's formula, read by Mara (p24), and once in Kallia's mouth (p93). Nikaso says "Is it him?" without a name (p67). The name is absent from Ch.1–9 (grep: 0) ✓. **Does anyone know the room is his?** Before p93 Mara does not. Ch.7 gave her only "It's swept" (ch-07:p95). p59's "nor for anything under its roof" and p91's description of the last door do not identify it as his. The reveal is Kallia's own "Ariston's room" (p93) ✓. Mara learns that Kallia *has* a son only from the letter's "his mother" (p24). Before that she had the unexplained "Letters." / "east" exchange (ch-06:p68–p74) and the "not sons" rule (ch-08:p1). The town knows: Nikaso (p67). That is plausible, given Mara's month of silence (ch-07:p71) ✓. **"You read the clerk's wax"** (p22) is earned: Kallia heard Mara recite the register (ch-07:p177) ✓. **Kallia cannot read** (ch-07:p177 "What did he put?") ↔ p64 ✓. **Ariston's greetings** use only facts he could know by AD 68. The narration's "the old woman who slept between the baker and his wife" (p59) is Mara's knowledge from Ch.8's song (ch-08:p194), attributed to her, not to him (N-10) ✓. |
| (4) Objects and money | **PASS.** The letter's route is Emesa → coast → Corinth → coaster → Kirrha wine-seller's nail (p2), and it reaches Delphi with the Elean (p1). It goes into Kallia's belt (p20), then Mara's hands (p21), then the niche "behind the cumin" (p97). The Elean offers "two obols a night" (p15) and then "Three … Three obols." (p17), and Kallia lets the room "at the three obols" (p93) ✓. That fits the book's scale: the salt is an obol's worth (ch-07:p63), the clerk's fee two obols (ch-07:p173), the smith's price three drachmas (ch-09). **An obol for a sheet** (p90) is the low end but plausible (N-19). The carrier's "cup" is covered by Mara (p87). Mara's own money (the priest's coins, two brass) is not touched ✓. **New objects:** the good himation on the peg by the storeroom (p92); the niche with the good knife and cumin (p97); the cracked plate (p80); the crock (p77). |
| (5) History / world | **WARN ×2** (W-03 the Emesene-royal name; W-04 discharge money for an auxiliary). The letter formula is authentic: πολλὰ χαίρειν, "Before everything I pray for your health", the daily proskynema "to the gods of this place", the farewell, the date by month and place, and the address on the verso ✓. "ARISTON" in Greek is 7 letters, which matches "It was seven letters." (p64) ✓. Hyperberetaios is correct for Emesa ✓. Naming customs are correct on both sides: in Emesa a boy may take his maternal grandfather's name when there is no son; in Greece the father's father (p41–p42) ✓. The geography is right: the Orontes runs north, so "half a day below Emesa" is downstream; Lebanon and Anti-Lebanon keep snow into summer; summer irrigation channels; flat roofs used in the evening (p44) ✓. A stone "off the wall" breaking an arm above the elbow, which knits but will not straighten, is a plausible siege wound and a plausible *missio causaria* (p26) ✓. The Aigion–Kirrha crossing is right for a man from Elis (p1, p17) ✓. Emesa = Homs, and the crusader castle near Homs is Krak des Chevaliers ✓. Van Pelt is Penn's library, consistent with Ch.2's "the university library" (ch-02:p10) ✓. |
| (6) NO FORESHADOWING | **PASS.** The gate reads 0. On a manual read, "would" forms are conditional or habitual (p2, p76, p87); "He'll be home for the god's day, won't he?" is Nikaso's wrong guess, in speech; and "will have been all round the stadium" is a present inference. Nothing reaches past the afternoon. |
| (7) NO TICS | **Mechanical: PASS. Manual: no defect, three WATCH items:** the in-chapter running bits "cup" ×9 and "living" ×5 (N-07); spindle business ×6 (N-08); "roof" ×7 (N-09). Caps held: "said/told the [non-listener]" 1 ("She said it to the letter.", p57); Kallia's "Then" retort 1; "the way [X]" frames 2 (p20, p30); "as if" 1 (p71); hinge-family openers 0; "Somebody/Nobody" paragraph opener 1 (p66); bend/stoop/lean beats 0 (the bible's Ch.10 zero order is honored); kneel/crouch 0; command echo 0; gaze-arrival "then" 0; hearthstone shape 0; lying-awake coda 0; laughs 0; cloth smells 0; taste reactions 0; Kallia exits 1 (the gate); Kallia hands Mara a thing 1 (the letter). |
| (8) Spent moves (every bible block) | **WARN ×3** (W-01 refold, inside the sample-12 cluster; W-05 an unseen-scene pointer; W-08 the memory kicker). Clean against the rest, each checked by string and by shape: the [color]-of-[thing] shape (0; "a thumb of gray clay" is not it); "Whoever [made] it had" (0; p2's "Whoever let rooms … would" is not the maker frame); the unseen maker judged (0); the stranger-freeze (0, since Kallia keeps spinning through Nikaso); the "to the [joint]" depth frame (0); a wound reopening (0); men in a public place (0); the emotional peak as a laugh (0, the peak is the yawn); the body-rebel channel (hands rested; the face and eyes used); "the one / the only" (0 claims). |
| (9) Voice-bank lifts (zero allowed) | **WARN ×1 (W-01), sample-12 by string and by structure.** No other sample leaks: 01–11 and 13 show 0 shared grams with 2+ content words beyond common idiom ("could have told", "put her hand"). |
| (10) HARD rule: no Ariston/Mara parallel | **PASS on the letter, WARN on two near-misses** (W-02 p97; W-08's p45 "For a week I had wanted it back", a thing left in a far country and wanted back). p34 "…it was his from beginning to end" and p76 "I could have left out the roof…" concern Mara as reader and do not compare choices ✓. |
| (11) Voice drift | **PASS.** Mid gear. The asides are dry and scarce: "a goat that was against the whole idea", "the cracked one but it fit". The 1998 intrusion breaks into the reading (p45) and ends on an act. One gnomic generalization (p20, N-11). The narration stays inside the afternoon. The ugly sentence is kept (p80). |

---

## PRIORITY: UNRESOLVED ENTITY_STATE CONFLICTS (processed first)

The ENTITY_STATE on disk covers Ch.1–9. I reviewed its open flags for relevance to Ch.10: CH1-2, CH1-3, CH2-1, CH2-3, CH2-4, CH2-5, CH3-1, CH3-2, CH3-3, CH4-2, CH4-3, CH4-4, CH5-3, CH5-4, CH6-5, CH8-2 and blueprint P1, P3, P4. **None touches a Ch.10 fact.** No Ch.10 action is required on them.

The plot thread **`kallias-son`** (opened ch-07:p37; preplants ch-06:p68–p74 and ch-08:p1, p107; payoff Ch.10) is paid as planned.

Two plan rows the page supersedes (prose wins; tracker to update, see patches):
- ENTITY l.4409 "up the hill with the first carter of the year" → the page has a pilgrim from Elis carrying it from a Kirrha wine-seller (p1–p2).
- ENTITY l.1300 "Kallia's kitchen" → the court, the step and the lean-to (p21, p46).

---

## CRITICAL ISSUES (must fix before proceeding)

### [C-01] "Three nights, till the god opens his house" puts the first consultation day three days after Ch.10
- **Audit:** Timeline.
- **Chapters:** 10 against the outline for Ch.11–13 (forward-binding) and ENTITY timeline rows 11–12.
- **Evidence:**
  - ch-10:p13: "Have you a room? **Three nights, till the god opens his house.**" "The god opens his house" is the year's first consultation day: Kallia's "Once the road's clear of snow he sits down in his house and answers whoever's paid" (ch-08:p99); the priest's wife's "for the god's return" (ch-09:p98).
  - outline Ch.11 beat 2: "She mends harness for a week anyway"; ENTITY timeline ch.11 "about a week+".
  - outline Ch.12, "Opens toward Ch.13": "**the seventh of Bysios is three days off**" (ENTITY l.4597).
- **Why CRITICAL:** if the Elean is right, the seventh of Bysios falls three days after Ch.10, and Ch.11's week plus Ch.12's three-days-off cannot happen. A reader who meets "three days off" in Ch.12 will count back.
- **Suggested fix (word-neutral):** p13 → "Have you a room? **I'm here** till the god opens his house." (−2 +2). p19's "people come early for the god" then reads as two-plus weeks early, which is natural once the sea has opened.
- **Cascade risk:** none in Ch.10. p69's "He'll be home for the god's day" stays. Ch.11–12 writers must keep at least ~10 days between Ch.10 and the seventh of Bysios. If the Elean returns in Ch.11+ as the lodger in Ariston's room, his stay runs to the god's day at three obols (≈ 7–9 drachmas over 2–3 weeks), which is plausible for a pilgrim already paying a pelanos.

---

## WARN ISSUES (should fix)

### [W-01] The close rebuilds voice-bank sample-12 (the Ch.10 calibration) out of its non-mandated furniture
- **Audit:** voice-bank lifts (zero allowed; voice-dna §6: "No sentence, image or line from any sample may be reused"); bible after Ch.8: samples "leak by structure as well as by string".
- **What is legitimately shared** (outline-mandated, not lifts): the man from Elis, the letter, the broom across the threshold, the room let to him.
- **What is lifted:**

| # | ch-10 | sample-12 | Fix (fresh vs Ch.1–9 and the bank; grepped) | Δw |
|---|---|---|---|---|
| a | p20 "The letter went **inside her belt**, against her stomach, and she returned to the pots." | "until it was small enough to put **inside her belt**" | "She pushed the letter down **behind her belt**, against her stomach, and returned to the pots." | +1 |
| b | p91 "At dawn they had been swept already; from my mat **I had heard the broom**." | "**I heard the broom** on the floor, a long stroke and a short one" | "At dawn they had been swept already; **I had been carrying out the ashes when she did them**." (ties to her standing chore, ch-05:p202) | +2 |
| c | p97 "I folded the papyrus down **along the folds it had come in**, and it made a fatter packet than before." | "folded it **along its old creases**" (also ch-02:p67 "I folded it back along its own creases"; the Ch.9 audit already cut this move once, ch-09 W-04) | "I folded the papyrus, and it made a fatter packet than before." | −8 |
| d | p94–p95 "Shall I go up and open it?" / "He can lift a latch." (Mara offers to ready the room; Kallia declines) | "I said that I would air it." / "I'll do it." | Delete p94–p95. Append to Kallia's p93 speech: "…He can have Ariston's room, at the three obols. **If he comes to the gate before I find him, he waits in the court.**" (an order, which is her card, and the name slides by inside business) | +3 |
| e | p98 "Out in the lane somebody was driving **a goat that was against the whole idea**, and a woman's voice was telling him so." | "**The goat in the yard began complaining** about its water." | "Out in the lane **a woman was shaking a blanket over her neighbor's wall, and the neighbor was telling her where else she might shake it.**" | +3 |
| f | p98 last act: "Half the basket was still to clean, and I pulled it back onto my knees." (a legume chore resumed as the final sentence) | last act: "and finished **shelling the beans**." | Reorder p98 so the chore is not the last act: "Half the basket was still to clean, and I pulled it back onto my knees. Out in the lane [e]. The step was in shade. **It was a good while yet till the lamps.**" The last sentence is 9 words → still `quiet` ✓, a plain moment of the ongoing day. | 0 |

- **Net:** +1. With (d), dialogue is unchanged in share.
- **Cascade:** none. The bible's Ch.10 spent list must then drop "He can lift a latch" and the goat (see W-09).

### [W-02] p97 places an image weighted with meaning one paragraph from the PLAIN STOP, and it is the nearest miss on the no-parallel rule
- **Audit:** Ledger (PLAIN STOP: "no image weighted with meaning", voice-dna §8; outline HARD writer warning) and the HARD rule.
- **Evidence:**
  - ch-10:p97: "Before I folded it I read it once more, without moving my lips. **To myself it was a cheerful letter, from a man with a roof to sit on in the evenings.**"
  - The roof is the chapter's weighted image: the letter at p44; Kallia's "A roof you sit on … Where does the rain go?" at p46; "For the house there was no line, nor for anything under its roof" at p59; and Mara's "I could have left out the roof" at p76.
  - Read in private, the line has Mara, the book's other far-from-home woman, siding with the son's made life. That is the author's thumb the outline forbids ("No comparison of Ariston's choice to Mara's in narration"), arriving as sympathy rather than statement.
- **Suggested fix:** "Before I folded it I read it once more, without moving my lips, **from the greeting down to the date.**" (−11; plain, fresh: "from the greeting" and "down to the date" both have 0 prior uses.)
- **Cascade:** the bible's spent entry "Reading a document silently after reading it aloud … 'To myself it was a cheerful letter…'" must be re-worded to the new line (W-09).

### [W-03] "Domna … at Emesa" is a historian's wink at Julia Domna's house
- **Audit:** World/history; this book's wink rule (Ch.8 audit Theano; Ch.9 W-08, a curse-tablet name; Ch.9's Thracian-name wink).
- **Evidence:** ch-10:p33 "I took a wife here: **Domna**, the daughter of **Iamblichos**, who sells horses to the cohort."
  - Domna is the signature name of Emesa's priestly-royal line: Julia Domna, born c. 160.
  - Iamblichos is that dynasty's founding name: Iamblichus I.
  - Paired at Emesa, the two read as a nod, and Mara, a classicist who glosses Emesa as Homs at p45, would register it. Her silence then reads as the author's.
- **Suggested fix (0 words):** rename the wife to an ordinary Aramaic name in Greek dress, e.g. **Shalmath** (Palmyrene *Šlmt*). Keep Iamblichos, a common Syrian name once Domna is gone; Kallia asks it again at p84–p85.
- **Cascade:** the bible's Ariston card and its Ch.10 mention-only line; ENTITY (patch).

### [W-04] "with the money that goes with it": auxiliaries drew no discharge bounty
- **Audit:** History (Roman auxiliary plausibility, AD 70).
- **Evidence:**
  - ch-10:p26 "On account of it the prefect has given me my discharge before my time, **with the money that goes with it**."
  - p44 "With the money from the cohort and what came with her, I have bought land".
  - foundation.md, Kallia profile: "her son Ariston enlisted with an **auxiliary cohort** in Syria". The page's "cohort" plus "prefect" (*praefectus cohortis*) is correct for an auxiliary.
- **The problem:**
  - The *praemia* paid by the aerarium militare went to legionaries on honourable discharge. Auxiliaries received no cash bounty: after 25 years, citizenship by diploma, and nothing on an early *missio causaria*.
  - A Phocian non-citizen could not properly be a legionary, and a legion's cohort would not be under "the prefect".
  - What an early-discharged auxiliary *did* take away was his back pay and his savings held at the standards (*deposita ad signa*).
- **Suggested fix:** p26 "…has given me my discharge before my time, **and paid me out what I had saved at the standards**." (+4; "saved at" and "the standards" have 0 prior uses.) p44's "the money from the cohort" then stands as written.
- **Cascade:** none. The dowry ("what came with her") carries most of the land price after under two years' savings, which suits a horse-dealer with no son (N-02).

### [W-05] "the face she wore at the oil-seller's" points at a scene the book never showed
- **Audit:** Reverse-Chekhov / spent move (bible after Ch.8: narrator call-out pointers, "Proposed cap ≤1 per chapter; treat it as 0").
- **Evidence:** ch-10:p6 "She heard that with the face she wore **at the oil-seller's**." There is no oil-seller in Ch.1–9 (grep 0). Kallia's on-page haggles are with Valens over the oak (ch-06:p64, "Four. It's wet.") and with the cheese-man, where Mara watched *his* face (ch-07:p30).
- **Suggested fix:** "**Her face gave him nothing for that.**" (−4; "face gave" and "gave him nothing" have 0 prior uses.) Avoid Ch.5's "without any change in her face" (ch-05:p146).

### [W-06] "Patrai" against the book's "Patrae"
- **Audit:** Name consistency.
- **Evidence:** ch-10:p20 "The man from **Patrai**". Prior uses: ch-06:p328 (Valens) "That's a big house. Corinth, or **Patrae**."; ch-09:p190 "My cousin's master in **Patrae**". The book otherwise uses Latinate/English forms for that city.
- **Fix:** "Patrae" (0 words). Bible Ch.10 walk-on line likewise.

### [W-07] Two second uses of earlier-chapter phrases that the 5-gram echo scan cannot see (CLAUDE.md step 5c: vary every 2nd use)
| ch-10 | prior | Fix | Δw |
|---|---|---|---|
| p21 "held it toward me across the wool, **as far as her arm would reach**." | ch-06:p1 "as far in **as my arm would reach**" | "…across the wool **at the length of her arm**." (avoid ch-08:p66 "at the full stretch of her arm" and ch-04:p45 "at arm's length") | −1 |
| p54 "She wanted **no answer to that**, and I gave her none." | ch-06:p271 "I had **no answer to that**." | "She wanted **no reply to that**, and I made none." | −1 |

### [W-08] p45's memory closes on a kicker, a spent move, and the kicker is a second near-parallel
- **Audit:** Spent moves (bible after Ch.7 cycle 1, "The memory-paragraph kicker … SPENT. A memory insert ends on its image, an act or an object") and the HARD rule.
- **Evidence:** ch-10:p45 "…returned the book across the desk at Van Pelt with the castle still in it. **For a week I had wanted it back.** My voice went on through the oxen without me."
  - The short dry sentence comments on the memory.
  - Its content (a thing let go in a far country, then wanted back) sits beside Kallia's loss and Mara's own exile.
- **Suggested fix:** cut "For a week I had wanted it back." (−8). The memory then ends on its object ("with the castle still in it") and the paragraph on the act ✓.

### [W-09] character-bible.md's Ch.10 blocks quote 13 lines that are not on the page, and the spent list therefore mis-counts
- **Audit:** Bible currency (CLAUDE.md: the Writer keeps it current; bible spent lists govern Ch.11+).
- **Evidence:** a grep of chapter-10.md finds 0 hits for each of the following, which the bible presents as on-page:
  - Kallia's "Everywhere has rain."; "with a cast in her eye from his kiln"; "There'll be a child by now."; "Go and stand him one, if you want the lions."; "…and there's nothing there with a roof on it that isn't full to the tiles."; "There's the lamps to fill before the gallery comes down."
  - Mara's "He writes as one who is content there"; "I found a plate."; "She put the letter inside her belt".
  - The spent entries "My eyes ran a line ahead of my voice…" and "In the lane my Greek arrived in single words…" (this makes the written-vs-spoken contrast's "CLOSED at 3" count include a passage that is not there).
  - "the narration names him only as 'Kallia's son' (×1)".
  - The Elean's "Since the autumn, he says." and "Syria, he said. Is it bad?".
- **Fix:** re-sync the Kallia Ch.10 block, the Ariston Ch.10 block, the Ch.10 walk-on block and "At-risk after Ch.10" to the final page *after* the fixes above. That covers "He can lift a latch" / the goat / "cheerful letter" if those are cut, Patrae, and the wife's name.

---

## NOTES (polish / tracking)

- **N-01 Ariston's age and service against Kallia's age.**
  - No age is stated for him. Kallia is "a woman of fifty" (ch-05:p140), and he took Thrasyllos's mules "at ten years old" (p56).
  - An enlistment in AD 68–69 at about 18–25 puts his birth when Kallia was 23–30 ✓.
  - Her "no other name on that line for years" (ch-07:p169) holds at two and a half years.
  - "How old was he, when he went?" is deliberately unanswered (p78), so leave it.
- **N-02 Plausibility of a cohort at Emesa.**
  - In AD 70 Emesa was Sohaemus's client kingdom, and its royal troops served under Titus at Jerusalem.
  - A Roman auxiliary cohort was plausibly near: Raphanaea is a legionary base about 30 km away.
  - Serving soldiers could not contract legal marriage, but a de facto wife was normal and a Greek letter calls her "wife".
  - "The year before it I took a wife" reads as before or around enlistment.
  - No change; the page never says "Roman" or "auxiliary", so it would also survive a royal-army reading.
- **N-03 Compression of the date and the route.**
  - The upper city fell in September (ch-05:p108). Before 20 Hyperberetaios (≈ 20 Oct) he must be discharged, travel about 400 km to Emesa, and buy land, oxen and a man (p44).
  - The letter must then reach Kirrha before the last ship, "eight days" before ch-06:p69 (≈ mid-November).
  - Each step is possible, and together they are tight.
  - Optional: p44 "I have bought land" → "I am buying land" (0 words) eases the first leg.
- **N-04 The winter delay is better than the plan.** The plan has the letter waiting on "the harbour road"; the page has "nobody he'd trust was bound for Delphi" (p2), which survives Valens's winter traffic on the Kirrha road (ch-06:p313). Kallia asked Valens about letters from the east at the very season the letter hung at Kirrha (ch-06:p68–p74): a quiet irony, left unpointed ✓.
- **N-05 p30, Jerusalem.**
  - "that summer" has no antecedent summer at narration time (late winter AD 71). Option: "**in the summer just gone**" (+2, 0 prior).
  - "I knew it … as a date on a page" undersells ch-05:p97–p108, where she heard the herald cry it in the square. Optional recast; not required.
  - "the Temple" is capitalized here but "temple" is lowercase at ch-05:p97 and p108; pick one.
- **N-06 "At the vintage" (p32).** This is the 4th "at the vintage" book-wide (ch-05:p171; ch-08 Timo ×2), and the second departure from Kallia's house dated to a vintage (the girl, ch-05:p171 and ch-07:p12). Optional cut, "Two and a half," said Kallia. (−3). Only cut it if the floor allows.
- **N-07 In-chapter running bits.**
  - "cup" ×9 (p2, p9–p11, p74, p87). Mara's "As the Elean did" (p87) is a pointer back inside the chapter.
  - "living" ×5 (p55, p56, p67, p68, p89).
  - Both are designed and both are under the gate. Close both after Ch.10, and add them to the at-risk list.
- **N-08 Spindle business ×6** (p21 ×2, p40, p54, p61, p88). It never reaches 3 in 400 words (the nearest window is about 480). The bible WATCH stands: no spinning as Kallia's stage business in Ch.11–16.
- **N-09 "roof" ×7** (p17, p44, p46, p59, p76, p97; plus "full to the tiles", p93). After W-02 it is ×6, which is fine as the chapter's one weighted noun.
- **N-10 Callback pointer at p59.** "He had found room for the old woman who slept between the baker and his wife" points at Ch.8's song (ch-08:p194). This is the one borderline pointer. The information flow is sound: the mother "moved in on us for the winter" (ch-07:p42), so Ariston could not know the bed arrangement, and the sentence gives him only the greeting. Keep it, since the floor is tight; "the baker's mother" is capped at 1 book-wide, so do not substitute that.
- **N-11 Gnomic line at p20.** "Letters came in two kinds, I thought, and either kind got read at once: the bad to be done with, and the good to be had." It is aphorism-shaped, though not a close. WATCH.
- **N-12 p8 "I filled the dipper at the jar."** This echoes ch-09:p162 "She filled the basin at the jar". Optional: "I brought the dipper up full from the jar." (+2).
- **N-13 p66 "from three gates down."** ENTITY deliberately removed a gate count (CH8-5 resolution). It is compatible with "Midway along the lane" (ch-08:p13; ch-05:p183). The tracker should record it as the page's count.
- **N-14 Attribution of p70 and p72.** Neither is tagged, and Nikaso is looking at "the papyrus in my hands" (p71), so a reader may hear Mara. The bible assigns both to Kallia. An optional tag on p70 is +2.
- **N-15 Blocking at p91.** "The papyrus **still** lay open in my lap": Mara has been up at the crock (p77) and found the plate (p80). → "The papyrus lay open in my lap again." (0).
- **N-16 The held beat at p62.** It is measured by the lodger's tunic stirring on the rail. This is kin to the SPENT "held moment measured by indifferent passing traffic" (Ch.1, 5, 9), though not traffic. WATCH.
- **N-17 p45 "My voice went on through the oxen without me."** This is not the retired voice-failing channel. Do not repeat a voice-detaching beat before Ch.20.
- **N-18 Sight-reading a 1st-c. hand.** It is plausible because the hand is "small and level from top to foot" (p23) and the address is "in the same small hand" (p59), i.e. a clear, near-scribal hand. No change.
- **N-19 Obol for a sheet (p90).** Egyptian prices run about 1–2 obols a sheet, and Greece would be dearer. It is the low end but fine; the carrier's cup is Mara's problem (p87).
- **N-20 The stadium houses.** The houses "by the stadium" (p18, p93) sit near Ch.5's "house down past the stadium road that takes in girls on their own" (ch-05:p130). If the joke is unintended, it is harmless. WATCH if the Elean returns.
- **N-21 "Castalian" first reaches the page here,** inside the letter's address (p59). Sosandros said "The lodging over the spring" (ch-07:p143) ✓.
- **N-22 "postcard"** is now in five chapters (ch-02:p17, ch-03:p66, ch-05:p65, ch-06:p176, ch-10:p45), each a different use. WATCH.
- **N-23 Ledger close after W-01(f).** The last sentence becomes "It was a good while yet till the lamps." (9 words), which is still `quiet`, and the outline's "the afternoon going on" is literal ✓.
- **N-24 Kallia's "Which arm?" (p27).** It comes right after "the left arm" is read, and it is deliberate shock-blankness. Keep it.
- **N-25 Thinness.** See below.

---

## THINNESS (2,528 against the 2,500 range floor)

**Beat budget against the page:**

| Beat | Budget | On the page |
|---|---|---|
| The gate / the Elean | 550 | p1–p19, ≈ 420 |
| The belt hours | 200 | p20, 148 |
| Formula / war / arm | 400 | p21–p30, ≈ 380 |
| The wife | 450 | p31–p40, ≈ 190 |
| Child / roof / land / Emesa | 400 | p41–p54, ≈ 350 |
| Greetings / nothing for the house | 350 | p55–p62, ≈ 270 |
| Name / Nikaso / reply | 450 | p63–p90, ≈ 520 |
| The sweep / out | 250 | p91–p96, ≈ 250 |
| Alone | 150 | p97–p98, 134 |

- **The light beat is the wife** (≈ 190 against 450). It is also the outline's subtext engine ("Is she Greek? Can she weave?" asking whether he is happy). The page carries it in two questions and one deflection. That is the right *weight*, and it should not be padded.
- **If the editor needs words to hold the floor after these fixes** (net −20 → ≈ 2,508), the place to earn them is p59–p62: the moment the reading finds no line for the house. Kallia's response there is currently one sentence ("Kallia stood in the sun with the wool in her hand.") plus a wool beat. A short physical act of hers belongs here: work, not a gesture class already near its cap, and not spinning. It would deepen the chapter's one unbearable fact without explaining it.
- **Do not take the optional cuts** in N-05 or N-06 unless words are added elsewhere.

---

## SUGGESTED YAML PATCHES (for entity-tracker UPDATE after the editor's fixes)

```yaml
suggested_patches:
  - entity: "timeline[chapter=10]"
    action: "update"
    value: { time: "one afternoon, just after noon to mid-afternoon ('a good while yet till the lamps')", season: "late winter: 'the first afternoon of the year with heat enough in the sun to work without a cloak'", year: "AD 71", note: "the god's first consultation day is ahead but NOT dated on the page after C-01 (the Elean stays 'till the god opens his house'); must leave >= ~10 days for Ch.11-12" }
    reason: "C-01; page facts p21, p98"
  - entity: "objects.ariston-letter"
    action: "create"
    value: { written: "Emesa, 'the twentieth of Hyperberetaios' (~20 Oct AD 70)", route: "Emesa -> Corinth -> coaster 'at the back end of the sailing' -> Kirrha wine-seller's nail all winter -> the pilgrim from Elis", sealed: "thread twice round, a thumb of gray clay; brown tidemark", now: "in the lean-to niche behind the cumin (p97)" }
    reason: "new object, ch-10:p1-p2, p23, p58-p59, p97"
  - entity: "ariston"
    action: "update"
    value: { wife: "Shalmath (if W-03 applied; else Domna), daughter of Iamblichos, horse-seller to the cohort", service: "the cohort before Jerusalem 'from springtime until the city was taken'; left arm broken above the elbow by a stone off the wall, knit, will not straighten; early discharge by the prefect", land: "half a day below Emesa on the river; wheat, olives on the bank, a channel; a yoke of oxen and a man", child: "due before midwinter AD 70-71; sex unknown at Delphi", left_delphi: "at the vintage, two and a half years before (AD 68)", greets: ["Nikaso and her husband", "Philista (the drum)", "the baker, Sostrata, his old mother", "Thrasyllos (dead)", "Glauke's girls"] }
    reason: "ch-10:p24-p58"
  - entity: "kallia.knowledge"
    action: "add"
    value: { fact: "Ariston alive, married at Emesa, a child, land, discharged; no line for the house", learned: "ch-10:p24-p59", method: "told_by:mara-reyes (read aloud)" }
  - entity: "mara-reyes.knowledge"
    action: "add"
    value: [ { fact: "Kallia has a son, Ariston, in Syria", learned: "ch-10:p24", method: "read" }, { fact: "the shut, swept room is Ariston's", learned: "ch-10:p93", method: "told_by:kallia" } ]
  - entity: "nikaso.knowledge"
    action: "add"
    value: { fact: "Ariston living, married in Syria, a child (assumes a grandson)", learned: "ch-10:p67-p73", method: "told_by:kallia" }
    reason: "she carries it down the lane (p75)"
  - entity: "plot_threads.kallias-son"
    action: "update"
    value: { status: "paid (Ch.10); coda Ch.16", reply_thread: "OPEN: Kallia's obol on the bottom stair 'For the sheet'; one line, 'Tell him the baker's old mother is living'; carrier east 'for a cup'; Kallia asked Iamblichos's name again (p84)" }
  - entity: "plot_threads.elean-lodger"
    action: "create"
    value: { status: "open", detail: "a young man from Elis, peeling scalp, seasick from Aigion, to be let Ariston's room at three obols 'till the god opens his house'; name him and card him if he returns" }
  - entity: "locations.kallias-house"
    action: "add"
    value: [ "the last door on the gallery: oldest, gray planks silvered at the foot, wooden latch, cord loop over the latch-peg (p91)", "her good himation on the peg by the storeroom (p92)", "the lean-to's cold end wall has a niche: the good knife, a twist of cumin (p97)", "the crock by the jar (p77)" ]
  - entity: "locations.kallias-lane"
    action: "update"
    value: { nikaso_gate: "'three gates down' from Kallia's (p66), compatible with 'Midway along the lane' (ch-08:p13)" }
  - entity: "naming.patrae"
    action: "keep_original"
    reason: "ch-06:p328 and ch-09:p190 use 'Patrae'; ch-10:p20 'Patrai' is the outlier (W-06)"
  - entity: "outline-plan rows l.1300 and l.4409"
    action: "update"
    reason: "the page has the court/step/lean-to and the Elean pilgrim, not 'the kitchen' and 'the first carter of the year'"
```

---

## Proposed-wording freshness check

Every proposed string was grepped against Ch.1–9 and voice-bank/samples 01–13. All of the following have 0 prior uses:
- "I'm here till"
- "behind her belt"
- "carrying out the ashes"
- "waits in the court"
- "shaking a blanket" / "neighbor's wall"
- "from the greeting" / "down to the date"
- "saved at" / "the standards"
- "face gave" / "gave him nothing"
- "length of her arm"
- "no reply" / "made none"
- "summer just gone"

"a good while yet" occurs only in Ch.10 itself. Rejected candidates and their collisions: "over the wool" (ch-07 ×2), "under the wall" (×2), "the summer before" (ch-03), "whole length of" (×1), "full stretch of her arm" (ch-08:p66), "at arm's length" (ch-04:p45), "without any change in her face" (ch-05:p146), "the baker's mother" (capped at 1).
