# Outline Audit (pre-writing): *The Hour of Ash*, run 2

**Date:** 2026-10-18
**Mode:** OUTLINE AUDIT. No chapters exist yet. The plan was audited against itself.
**Inputs:** `STATE.yaml` (guardrails, resolved decisions, ARCH-1..13), `foundation.md`, `outline.md` (44 ch + Macro-Structure + Ledger), `voice-dna.md`, `character-bible.md`, `ENTITY_STATE.yaml` (meta.conflicts_index C1–C14, plan_gaps), `research/story-bible.md` (canon). `research/prior-run-2026-07/` was ignored.
**Rule of this report:** this report flags problems and does not rewrite them. Each finding gives a file, a chapter and the quoted line (`file:line`). "Resolution needed" says what has to be decided. It does not supply replacement text.

**Totals: 3 CRITICAL · 26 WARNING · 29 NOTE**

Entity-tracker conflicts: all 14 are confirmed (C1–C14). Three are CRITICAL (C8, C9, C10), five are WARNING (C4, C5, C7, C12, C13) and six are NOTE (C1, C2, C3, C6, C11, C14). There are **44 new findings** that the tracker did not raise as conflicts (21 WARNING, 23 NOTE).

---

## CRITICAL (fix in the planning docs before the chapter that carries them is drafted)

### [CRIT-001] Pompeii "seventeen years after the quake" in AD 72 *(tracker C8, confirmed)*
- **Audit:** Timeline / world.
- **Evidence:**
  - `outline.md:644` (Ch.19, NON-NEGOTIABLE beat 4): "a city seventeen years after the quake and still mending."
  - `foundation.md:274` (§5 Mending): "In Pompeii, a city still rebuilding seventeen years after the AD 62 earthquake"
  - Ch.19 has the dateline *Puteoli · spring, AD 72* (`outline.md:633`).
- **Issue:** 62 + 17 = 79. In AD 72 the quake was **ten** years earlier, so the figure is wrong by seven years. It sits in a NON-NEGOTIABLE beat, so the Writer will print it, and readers check exactly this kind of arithmetic.
- **Resolution needed:** correct both lines ("ten years"). **Cascade:** Ch.20 (AD 72–73) and Ch.30 (AD 77, "re-plastering already") must use the matching figure if they cite one.

### [CRIT-002] "The truth cost three years" (frame AD 69 → trial AD 74 = five) *(tracker C9, confirmed)*
- **Audit:** Timeline / character.
- **Evidence:**
  - `outline.md:756` (Ch.23 emotional surprise): "after vindication he is sad. The truth cost three years and changes nothing about his back."
  - `foundation.md:214` (§4 row 23): "the truth cost three years"
  - `foundation.md:95`: "In 69 Celer framed his wife with her bodyguard." Ch.22 has the dateline *Rome · spring, AD 74*.
- **Issue:** from 69 to spring 74 is about five years. Ch.12 delivers the 69 date on the page and Ch.22 carries the 74 dateline, so a reader holds both numbers when Ch.23 says "three."
- **Resolution needed:** correct to five, or re-anchor the count to something that really is three years and state that anchor. **Cascade:** Ch.12's telling and Plautia's "twice in three years" (`foundation.md:154`) must agree with whichever anchor is chosen.

### [CRIT-003] Marcus is "seven" in both AD 71–72 and AD 74 *(tracker C10, confirmed and extended)*
- **Audit:** Character (age) / timeline.
- **Evidence:**
  - `foundation.md:154` (Plautia profile, the Ch.16 frame, winter 71–72): "her husband kept their son, Marcus, now seven, after the divorce. She has seen him twice in three years."
  - `outline.md:734` (Ch.22, AD 74, NON-NEGOTIABLE): "A glimpse of Plautia with Marcus, seven, on the basilica steps."
  - `character-bible.md:237` (Plautia card): "her son Marcus, seven", and `character-bible.md:464`: "MARCUS — Plautia's son, aged 7 (glimpsed Ch.22)".
- **Issue:** the Ch.16 Writer reads the foundation profile ("now seven") and the Ch.22 Writer reads a NON-NEGOTIABLE "seven." That is a two-to-three-year age contradiction printed in two chapters. The character bible has a third copy of the number, with no year attached.
- **Resolution needed:** fix Marcus's birth year once (for example, born c. AD 64–65 makes him about 7 in 71–72 and 9–10 in 74, or the reverse). Update the foundation, outline Ch.22 and both bible cards. The Marcus card's "formal beyond his years" voice must also fit the chosen age.

---

## WARNING (should fix; would confuse a careful reader, break a gate, or strain a guardrail)

### A. Entity-tracker conflicts confirmed at WARNING

**[WARN-001] ARCH-4 says the Oracle does not speak to Mara face to face; outline Ch.13 has Theano name Pompeii to her in person** *(C12)*
- `STATE.yaml:110`: "FLAG for the author: the Oracle speaks to Mara through Valens's errand rather than face to face."
- `outline.md:463` (Ch.13 premise): "Then the Pythia herself sends for Mara and names the city." `outline.md:475`: "Theano's last word, which ends the chapter: 'Pompeii.'"
- The outline is actually *closer* to canon (`research/story-bible.md:37`: "The Oracle of Delphi tells her WHERE"). The decision log is the stale document, but it is the record the author will review. **Resolve STATE ARCH-4 before Ch.13.** This does not block Ch.1–12.

**[WARN-002] Fenn's "thirty-four years of waiting" in AD 76** *(C13)*
- `outline.md:869` (Ch.27, dateline AD 76): "she watches what thirty-four years of waiting have done to him." From AD 41 to AD 76 is 35 years. (Ch.25 in AD 75 = 34 is correct, and Ch.35's "thirty-eight years" for winter 78–79 is correct.)

**[WARN-003] The foundation's escalation ladder says she "gives up home" after Ch.25; the outline keeps her hoping** *(C7)*
- `foundation.md:36`: "She refuses the arithmetic, plans to leave Campania with her family before then, and gives up home."
- `outline.md:954` (Ch.30): "Mara runs to the tomb hoping the doors might breathe early." No chapter between 25 and 32 shows a plan to leave Campania.
- The ladder is the arc spec the evaluator reads, and it contradicts the beats. Resolve which one is canon.

**[WARN-004] The foundation's Ch.38 anchor breaks the voice-dna mountain rule** *(C5, upgraded)*
- `foundation.md:229`: "The last frame of film spent on Vesuvius, smoking very faintly at dawn"
- `outline.md:1177`: "a thread of cloud on the summit that may only be cloud"
- `voice-dna.md:111`: "Before Ch.39 the mountain does nothing on the page"
- The tracker logged this as a detail conflict. It is more than that: "smoking" is a portent, so the foundation version breaks the NO-FORESHADOWING mountain rule. The outline wording is the compliant one. Align the foundation to it.

**[WARN-005] Ch.7 legal status: "property" or "dependent kinswoman"** *(C4)*
- `foundation.md:198`: "being registered as Kallia's property"
- `outline.md:298`: "being registered as Kallia's dependent kinswoman 'from Syracuse'"
- These are different legal states (slave vs free dependent), and Ch.7's emotional surprise depends on which one is meant. Downstream, Ch.16 (Kallia releasing her) and Ch.18 (a legal marriage needs a free bride) only work with "kinswoman."

### B. New: information flow

**[WARN-006] How does Mara find the Nuceria Gate tomb on her first day in Pompeii?**
- `foundation.md:375`: "The home door is a tomb outside Pompeii's Nuceria Gate, named in Theano's answer."
- `outline.md:471` (Ch.13): the answer names no gate: "*…where the dead go out of the city.*" Theano adds only "Pompeii."
- `outline.md:645` (Ch.19, NON-NEGOTIABLE): "Alone, Mara walks out of the Nuceria Gate into the tombs … A small freedman's tomb with a painted false door."
- Pompeii has necropoleis outside several gates (Herculaneum, Vesuvius, Nola, Stabian, Nuceria). The payoff (a specific tomb, found at once) has no setup. Either Theano's answer must narrow it, as the foundation claims, or Ch.19 must show a search. Decide before Ch.13.

**[WARN-007] Valens knows about Plautia's brother's dowry suit with no source**
- `outline.md:448` (Ch.12 adds): "the knowledge that Celer wants him dead, not merely recaptured (the dowry suit)."
- `outline.md:525` (Ch.15): "Plautia's brother's suit needs his testimony."
- `foundation.md:95`: "Plautia's brother is now suing for the dowry … That is why Celer's men are still looking for him."
- Valens has hidden in Phocis since 69. How does he know a suit has been filed and that he is its witness? He is the one who tells Mara (Ch.12), so the plan needs a knowledge path: a message from Plautia, word from Celer's men, or deduction from the notice.

**[WARN-008] Valens's knowledge of the door has no planned delivery** *(extends the tracker's plan_gap)*
- `outline.md:502` (Ch.14): "She does not tell him." Ch.15 has her tell him she is "from nineteen centuries ahead," but does not say whether she mentions the door or Pompeii.
- `outline.md:816` (Ch.25): Fenn's story and the WHEN are spoken **in English** ("a language no one knows"), so Valens cannot follow them.
- `outline.md:1041` (Ch.33): "Valens's practical questions: what would *he* be there?" This assumes he knows a door leads to 1998.
- Pin down what Valens is told, and when, about (a) the destination (Pompeii, needed for the Ch.15 bargain), (b) the door, and (c) the date. Ch.37's "everything" must not repeat information he already has.

**[WARN-009] Fenn's earlier predictions contradict "waiting since 62", and his knowledge of AD 79 is undecided**
- `outline.md:819` (Ch.25 NON-NEGOTIABLE): "'Late summer, seventy-nine.' He has been waiting for it since 62."
- `outline.md:820`: "Fenn admits two earlier predictions (71, 73) failed."
- If he predicted the Pompeii door for 71 and 73, he has not been waiting for 79 since 62. The two beats contradict each other inside one scene. Related gaps: (a) Fenn is an educated American who has lived in Campania for decades, and he almost certainly knows Pompeii dies in 79, which changes how he delivers the date (tracker plan_gap). (b) How does he know the door opened in 62 "for a day" if he arrived three days late (`outline.md:817`)? (c) In 71 and 73 he would have been at the Nuceria tomb, and in 73 Mara was living in Pompeii.

**[WARN-010] Fenn's own notebook and Margaret's death: an unplanned beat that endangers the Ch.35 evasion**
- `outline.md:132` (Ch.1): Szabo bought the lot at "Margaret Fenn's estate sale … 'Her brother.'" `foundation.md:114`: "His sister Margaret kept his boxes until her death in 1997."
- `character-bible.md:139`: Fenn never says his sister's name in person until Ch.35. `outline.md:1097` (Ch.35 NON-NEGOTIABLE): "he says his sister's name, Margaret, for the first time."
- Mara arrives in Ch.25 carrying **Fenn's own 1968 notebook**, and she knows Margaret's name and the fact of her death. No chapter plans what Mara tells him: whether she shows him the notebook, or tells him Margaret is dead and kept his boxes. A reader will expect that scene. If Mara says "Margaret" first, the Ch.35 "first time" beat loses its force. Schedule the decision (Ch.25, 26 or 35).

**[WARN-011] Provenance of Fenn's notebook (Ch.1–2: in the immediate write window)**
- `outline.md:161` (Ch.2): "Fenn, 1968: 'I put my hand in at the back and the air was cold…'" `outline.md:165`: "Fenn's last entry, July 1968, cheerful: back before Labor Day, Margaret can stop telling people he's in Mexico."
- `foundation.md:114`: "He vanished in Greece in summer 1968." `outline.md:1097` (Ch.35): "Philadelphia, the morning he left, the note on the hall table."
- If he was writing in Greece in July 1968 and then vanished there, how did the notebook (and the map) get back into Margaret's boxes in Philadelphia? Possibilities are effects shipped home, or an earlier trip followed by a second departure. Without one line of provenance, Ch.2 raises the question the moment the reader thinks about it.

**[WARN-012] Tremor notes "kept since 72": motive comes before the information, and the plant is in the same chapter as the payoff**
- `outline.md:1127` (Ch.36): "her own tremor notes, kept since 72 in her 1998 notebook. The figures agree."
- The rule that makes tremors relevant to the door ("breathe with the earth") reaches her in **Ch.25 (AD 75)** (`outline.md:817`). No chapter from 19 to 35 shows her keeping notes. The tracker lists "planted 36 / paid 36" but did not flag it.
- She could plausibly log tremors from 72 as an eruption watch (she knows 62 and 79), but that motive needs one on-page plant (Ch.20 or Ch.30). The tracker also notes that "her 1998 notebook" vs Fenn's notebook is unresolved.

**[WARN-013] Character-bible rule "no future tense about the door after Ch.25 until Ch.36" vs outline Ch.30 and Ch.33**
- `character-bible.md:71-72` and `voice-dna.md:256`: "After Ch.25 she will not use the future tense about the door until Ch.36."
- `outline.md:1042` (Ch.33 NON-NEGOTIABLE): "At Puteoli: will the door take them?" Ch.33 as a whole is "the case for taking her children through the door". Ch.30 is "hoping the doors might breathe early."
- The voice rule, read literally, cannot coexist with the planned beats. Narrow the rule (for example, to the *date*) or reword the beats.

### C. New: timeline, age, pregnancy

**[WARN-014] Ch.25 (AD 75): Mara is pregnant with Aelia, but the plan does not say so**
- `outline.md:806` (Ch.25 dateline): "*Puteoli · AD 75*" (no season). `STATE.yaml:114` (ARCH-8): "Aelia winter 75–76". `outline.md:845` (Ch.26): "Aelia three weeks old."
- Aelia is conceived around March–May 75. Unless Ch.25 falls in early 75, Mara is visibly pregnant (up to about 7 months) while travelling to Puteoli with a baby. Give Ch.25 a season and, if needed, the pregnancy.

**[WARN-015] Lucius "mortified" at about two and a half**
- `outline.md:934` (Ch.29, December 76, NON-NEGOTIABLE): "Valens weeps; Lucius is mortified." Also in `foundation.md:111`.
- `character-bible.md:307`: "About 2 (Ch.27–29): single words and two-word requests; names objects; watches."
- Lucius was born in summer 74, so he is about 2 years 5 months. Embarrassment at a parent is not a plausible reaction at that age, and it contradicts the age-stage card.

### D. New: world rules (the law of the doors)

**[WARN-016] How long an opening lasts: "for a day" in 62 vs the pre-dawn minutes in 79**
- `outline.md:817` (Ch.25): "The quake of 62 opened Pompeii's for a day, and he arrived three days late."
- `outline.md:1318` (Ch.43): "The seam closes, and she watches it close." The opening runs from before dawn to before first light (Ch.44).
- If a reader learns in Ch.25 that an opening lasts a day, then in Ch.42–43 they will ask why Mara cannot wait until the surge to decide. Either Ch.25 says "briefly" (as `foundation.md:360` does) or the plan accounts for the difference.

**[WARN-017] "The one it brought" misstates the law that the climax uses**
- `foundation.md:360`: "A door takes back anyone who came through a door, from any time, but **no one native to its side**."
- `foundation.md:32`, `179`; `outline.md:817` (Ch.25): "A door takes back the one it brought, so it will take her"; `outline.md:1293` (Ch.42).
- The Pompeii door brought no one. Mara came through the Corycian Cave. Read literally, Fenn's phrase predicts the Pompeii door will *not* take her, which is the opposite of the "promise" use. The allowlisted wording and the canonical rule must say the same thing.

### E. New: plot logic and object continuity

**[WARN-018] The locked plan in Ch.37 (door first, boat as backup) is reversed in Ch.40 (boat first, then door)**
- `outline.md:1148` (Ch.37): "The plan is locked: wait at the door, with the boat at the river mouth if it fails."
- `outline.md:1229` (Ch.40): "the family reaches the river mouth, where the boat cannot come in, and then turns back for the tombs and the door."
- The family abandons the agreed order without any planned beat. Ch.39 or Ch.40 needs the reason (Valens enforcing his "flee now" case, the door not yet cold in daylight), or Ch.37's plan must change.

**[WARN-019] Ch.38: Grata is sent away "next week," which is after the 24th**
- `outline.md:1184` (Ch.38, 19 August, NON-NEGOTIABLE): "She gives Grata money to visit her sister in Nuceria 'next week.'"
- From 19 August, "next week" falls on or after about 26 August. By Ch.36 Mara knows the date (24 August), so as written her rescue attempt defeats itself and reads as an author slip. The timing word has to fall before the 24th, or the plan must make the delay Grata's choice and say so.

**[WARN-020] The film roll's frame-by-frame spend has no on-page beats between Ch.3 and Ch.38**
- `foundation.md:258`: "Each frame is a decision about what to keep: Kallia's lamp, Valens asleep, Lucius's first steps, Fenn with his Zippo." `voice-dna` lists "the film counter and the frames she chooses" as a weight carrier.
- In the outline, frames 1–9 are in Ch.3 (`:190`), Ch.19 is "raised and lowered", Ch.38 is "the last frame" (`:1183`), and **no other chapter schedules a single frame.** That leaves 26 frames and four named subjects unassigned. The book's "true record" (§4f) never shows up on the page. Assign the named frames to chapters.

**[WARN-021] The ibuprofen is packed and never accounted for, and the fever chapter is where readers will ask**
- `outline.md:164` (Ch.2 packing, NON-NEGOTIABLE): "…granola bars, ibuprofen, her toothbrush and floss."
- `outline.md:1009` (Ch.32): "Her modern knowledge is useless." `:1015`: "*amoxicillin* in her head, useless as a prayer."
- A reader will ask "what about the ibuprofen?" during Lucius's fever. Plan where it went (used up, spoiled, or given to someone), or cut it from the packing list.

### F. New: guardrails (NO TICS, NO FORESHADOWING, allowlist caps)

**[WARN-022] Teeth are scheduled in 12 chapters, against the foundation's three; introductions-by-teeth cluster**
- `foundation.md:88`: "It surfaces Ch.7, Ch.20 and Ch.31."
- The outline adds Ch.1 (`:140`, "the eulogist's veneers"), Ch.2, Ch.4 (`:227`, "the boy's are perfect"), Ch.5, Ch.8, Ch.15, Ch.19, Ch.23 (`:768`, "the landlady's"), Ch.24 (`:783`, "the midwife's terrible teeth"), plus Ch.7/20/31.
- `character-bible.md:82` / `voice-dna.md:321`: "at most one introduction-by-teeth in any four chapters". This is already breached by Ch.1 + Ch.4 (eulogist, goat-boy) and by Ch.23 + Ch.24 (landlady, midwife). It is the device-emergence pattern the NO TICS law exists to prevent.

**[WARN-023] "The seventh of Bysios" is planned four times against a cap of 3, and the docs disagree on the cap**
- Uses: Ch.11 (`outline.md:418`, NON-NEGOTIABLE): "carry her question on the seventh of Bysios"; Ch.12 (`:449`): "the seventh of Bysios is three days off"; Ch.13 title (`:459`, which counts per `voice-dna.md:387`); Ch.13 opener (`:467`): "On the seventh of Bysios…".
- `voice-dna.md:387`: "Remaining uses: Ch.11 **or** 12, and the Ch.13 opener. Nothing later." vs `foundation.md:394` and the `tools/style_check.py:61` comment: "at most one later."
- Ch.11 and Ch.12 as planned would put the phrase over the cap before Ch.13 is written, which blocks the gate.

**[WARN-024] The Ch.26 anchor can only be delivered as a forward gesture**
- `outline.md:841`: "Fenn's English read aloud to a three-week-old who will never know the language." Also `foundation.md:217`.
- "Will never know" asserts an unreached outcome (NO-FORESHADOWING family C, outcome implication; compare the banned "I would never … again"). If the Writer lifts the anchor wording, the chapter fails the gate or the stance. Re-express the anchor as a present-tense fact of the scene.

**[WARN-025] Callback designs: two beats depend on a line "landing again"**
- `foundation.md:251` (§4d): "Ch.25: as a *promise* … Ch.42 or 43: as a *limit*." The promise-to-limit irony works only if the phrase recurs.
- `foundation.md:262` (§4f #6): "Theano's words 'where the dead go out of the city' (Ch.13) … Re-read: in Ch.44 they go out of the city by that road." See also `outline.md:1293`, `:1337`, `:1343`.
- The outline hedges both ("if used at all"), but the foundation designs them as payoffs. That conflicts with STATE's NO TICS clause and `voice-dna.md` §3b.3: "No beat in this book depends on a character's line 'landing again.'" Make it explicit that Ch.42 and Ch.44 work without the phrase.

### G. New: history (the "keep the political backdrop accurate" guardrail)

**[WARN-026] Celer is "legate on the proconsul's staff at Corinth" in AD 69, while Achaea was "free"**
- `foundation.md:95` and `character-bible.md:258`: "legate on the proconsul's staff at Corinth. In 69 Celer framed…"
- `foundation.md:357`: "Vespasian **revoked** the 'freedom' Nero had granted Achaea." Nero's grant (67) removed the province's governor, and Vespasian restored provincial rule only in the early 70s. So in 69 there was no proconsul of Achaea, and the foundation contradicts its own backdrop. Re-title Celer's 69 post, or move the frame to after the restoration. Check the Ch.16–17 "provincial record office" (AD 71–72) against the same date.

---

## NOTE (polish, low-risk, or by-design items worth recording)

| ID | Location (file:line, ch.) | Finding |
|---|---|---|
| N-01 | `foundation.md` §3 Grata "(Ch.20–40)" vs `outline.md:644` Ch.19 | **C1 confirmed.** Grata first appears in Ch.19 (she rents the rooms). The outline wins; fix the foundation's range. |
| N-02 | `foundation.md:257` "touched without comment in Ch.5, 19 and 35" vs Ch.35 entry | **C2 confirmed.** The Ch.35 cassette touch is missing from the outline. Add it or drop it from the foundation. |
| N-03 | `foundation.md:111` "Pompeii's small theatre" vs `outline.md:934` "a street stage" | **C3 confirmed.** Venue mismatch for the mime. |
| N-04 | `foundation.md:91` "two mundane breaks … Neither is earned by the plot" vs `outline.md:1364` "breaks 6/20/22" | **C6 confirmed.** The Ch.6 scream *is* plot-earned (the shut door), so by the foundation's own definition it is not one of the "unearned" breaks. Re-label rather than recount. |
| N-05 | `foundation.md:385` "Four on-page heat scenes: Ch.15, 23, 34" | **C11 confirmed.** The count says four but three are listed. Also, three documents give three different cut-offs: "none after Ch.38" (foundation), "Nothing explicit from Ch.35 on" (`voice-dna` §5), "none from Ch.39" (STATE ARCH-13). The plan satisfies all three (heat only in Ch.15, 23 and 34). **Heat placement check: PASS.** |
| N-06 | `outline.md:795` vs `:823` | **C14 confirmed.** The rumor comes from Grata's husband, but the Ch.25 "Builds on" line calls it "Grata's rumor." |
| N-07 | `outline.md:611` Ch.18 "kept it wound for sixteen months" | November 70 → after the Isthmia (spring 72) is about 17–18 months. |
| N-08 | `outline.md:624` Ch.18 "let her notice the hands are right" | A Roman who counts seasonal hours has no means of setting a 12-hour dial to "right" time. This needs a line (for example, setting it at noon by the sun) or the beat should be "still running." |
| N-09 | `outline.md:190` Ch.3 "The exposure counter … reads 9" vs `foundation.md:258` "She shoots nine frames" | On a K1000 the counter shows the *next* frame after advancing. "Reads 9" means 8 frames shot. Decide which, so the total of 36 adds up. |
| N-10 | `outline.md:302` Ch.7 "'Syracuse' accent excuse … passes as a Syrian name" | Syracuse is in Sicily, not Syria. The two covers sit oddly together, especially with Ariston in Syria in Ch.10. |
| N-11 | `outline.md:470`, `:502` Ch.13–14 "at the inn" / "Valens asleep on the inn floor across the doorway" | Mara lives at Kallia's lodging under a strict guardian. It is unclear whether "the inn" is Kallia's house, and Kallia allowing a man to sleep across Mara's doorway needs a reason. |
| N-12 | `outline.md:329` / `:473` "shouts at crows" vs `foundation.md:143` "feeds the sanctuary crows"; `character-bible.md:211` "Twice a month that god has me down a hole" | These can be reconciled, but align them. "Twice a month" conflicts with the fixed (monthly) consultation days in `foundation.md:357`. |
| N-13 | `outline.md:379` Ch.10 letter from Emesa, "late winter, AD 71" | The sea was closed November–March (`foundation.md:357`). The letter needs an overland or delayed route. |
| N-14 | `outline.md:702` Ch.21 summons reaches Pompeii | It is not stated who knew the family's address. Plautia knew "Italy", and Celer's men are still hunting. Add one line of knowledge path. |
| N-15 | `outline.md:643` Ch.19 Puteoli → coast road → Pompeii → necropolis as one "walk" | About 40+ km with mules plus the tomb visit is realistically two days. A "hot day" in spring is also a stretch. |
| N-16 | `outline.md:869` Ch.27 (AD 76) | Aelia is a nursing infant of a few months. Her whereabouts on the Cumae trip are unplanned. |
| N-17 | `outline.md:1117` Ch.36 dateline "July" vs `foundation.md:358` "news reaches Campania within days" of 23 June | Allowable if the notice is posted late, but state it. |
| N-18 | `outline.md:1090` Ch.35 premise "months short of the door he waited thirty-eight years for" | In Ch.35 Mara still rejects the date (until Ch.36), so her narration cannot assert the door is "months" away. Also, 38 years (since AD 41) and "waiting for it since 62" (`:819`) use different anchors. |
| N-19 | `outline.md:1062` "happiest hour" (Ch.34), `:1176` "The last ordinary day" (Ch.38), `:1256` "final ordinary closeness" (Ch.41), `:1177` "the last frame" (Ch.38) | These design labels use banned family-B framing. Writer warnings cover them, but they must not migrate into prose. "Last frame" is literal (frame 36) and should be written as an act, not a tag. |
| N-20 | `outline.md:1316`, `:1309`, `foundation.md:234`, `:245` "through the door into 1998" | By the book's own rule, doors do not deliver to matching dates (1968→41 and 1998→70 imply an offset of about 1,927–28 years, which would land around 2006). Mara cannot know it is 1998. Ch.42's "1998, or near it" (`:1290`) is the only stance-safe phrasing, so the Ch.43 narration should not assert "1998." |
| N-21 | `outline.md:1292` Ch.42 NON-NEGOTIABLE "Aelia's hand: plaster. Lucius's: plaster. Valens's: plaster." | An anaphora triad (a retired reflex) is built into a mandatory beat, and the chapter's own warning bans triads. |
| N-22 | `outline.md:879` Ch.27 "Fenn's rage at a 1990s word, in person this time" | A one-off failed-emotional-management beat (Ch.26, the letter) becomes a repeated bit. Watch it for device emergence. |
| N-23 | Ch.35 (`:1099`) Zippo, dime, paperback; knucklebone Ch.3 → Ch.26 | The 1968 relics have no plan after Ch.35, against `foundation.md` §5 "the last ones go home without her." The knucklebone is untouched for 23 chapters, and its hand-off from Lucius to Aelia (Ch.44) is unplanned. |
| N-24 | `outline.md:645` Ch.19 dormant door "faintly cool" vs `:961` Ch.30 "nothing, only warm plaster" | The dormant door reads colder than the door after a tremor. The temperature sequence needs a rationale. |
| N-25 | `foundation.md:147` "freed him informally" vs `outline.md:905` "sworn … as a free man"; `outline.md:360` Celer claims Valens "as property of the household" | Felix's informal freedom makes his oath as an auctoratus legally doubtful. Celer's ownership claim over a man freed from a lanista's troupe has no stated legal basis. |
| N-26 | `outline.md:60` "Opening sigs: no sig over 18%" | short-punch = 8/44 = **18.2%** (Ch.4, 10, 17, 20, 23, 28, 36, 42). This passes the tool (`shape_check` limit 40%) but breaks the ledger's own target. Collage chapters that open on a document (Ch.2/9/20/26) will compute as `dialogue` if the document is set in quotation marks. Ch.14 and Ch.40 open with ≤8-word lines but are not on the one-sentence-opening-paragraph list. |
| N-27 | `outline.md:470-471` Ch.13 | If both the priest's or the voice's answer and Valens's word-for-word repetition are rendered, "where the dead go out" is spent twice in Ch.13, which puts the cap of 3 at risk once Ch.19 and Ch.44 are counted. |
| N-28 | `outline.md:727`, `:733` Ch.22 "a juror sneezes"; "Plautia gets access to her son" | A dowry action went before a single *iudex*. The Basilica Julia housed the centumviral (inheritance) court. Custody access is not a remedy in a dowry suit (`foundation.md:154` calls it "leverage"). This is texture accuracy only. |
| N-29 | `outline.md:789` Ch.24 "re-shoeing a mule at midnight"; `voice-dna.md:346` | Roman equids wore hipposandals; nailed shoes are debated for the period. Separately, voice-dna's "The gate files currently allowlist only 'the one it brought'" is stale: all three phrases are now in `style_check.py`, `voice_wear_check.py` and `tic_report.py`. |

---

## TRACKING SUMMARY (plan-level)

### Knowledge chains (the four the brief named)
| Information | Origin | Who learns, when, how | Verdict |
|---|---|---|---|
| **WHERE** (Pompeii) | Oracle, Ch.13 | Public riddle via Valens (`:471`), then Theano says "Pompeii" (`:475`). No earlier leak: Ch.1–2 Halloran's "Campanian survey" is neutral, and Fenn's 1967–68 notebook predates any Italian door. | **PASS** with a guard: Ch.2 documents must not mention Italy. Open issues: WARN-001 (ARCH-4) and WARN-006 (which gate). |
| **WHEN** (late summer 79) | Fenn, Ch.25 | Mara Ch.25 (refused until Ch.36). Valens Ch.37. Ch.14's "Eight years" is Mara's own inference of the window, not the WHEN; Theano withholds it. | **PASS.** Open issues: WARN-009 (Fenn's 71/73 predictions, his knowledge of 79), WARN-012 (tremor-notes motive). |
| **Mara's origin** | Mara | Valens told Ch.15 (disbelieves), believes Ch.25 (overhears English). Fenn Ch.25. Aelia knows of Philadelphia by Ch.41 (FLEX). Kallia, Plautia and Grata never learn. Felix is unplanned. | **PASS.** Open issue: WARN-008 (what Valens knows about the door). |
| **Lupus / the frame** | 69 | Notice Ch.9, so Mara infers. Valens tells her Ch.12. Celer "Lupus" Ch.17. The Pompeii arena Ch.21. Public testimony Ch.22. | **PASS.** Open issues: WARN-007 (the suit), N-14 (the summons address). |

### Character availability (spot checks)
Felix: Ch.11 → 12 → 15 → 16 → 18 → (19–20 unmentioned) → 21 → 27 (missing) → 28 → 29 (on leave) → 37 (term served) → 38 → 40 (lost to sight). Consistent. Plautia: Ch.16, 17, 22. Celer: Ch.12 (his men), 17, 22. Grata: Ch.19–40, alive in Ch.40. Fenn: Ch.25–35, dies winter 78–79, absent from Ch.34. No impossible placements were found.

### Ages and pregnancies
Mara 33 (1998) → 42 body-age (79) ✓. Valens ~32 (70) → ~41 ✓. Felix ~12 (70) → 18 (76, Ch.28) → ~21 ✓. Fenn 34 (1968/AD 41) → 68 (AD 75) ✓. Lucius: conceived ~October 73, ~6 months pregnant in spring 74 ✓, born summer 74, 3 in summer 77 ✓, 5 at the eruption ✓ (Ch.29 behaviour WARN-015). Aelia: born winter 75–76, 3½ ✓ (Ch.25 pregnancy WARN-014). Marcus ✗ (CRIT-003).

### Plot threads with no scheduled payoff (orphans)
By design (fine): Halloran's Campania, Secundus's election, Grata's fate and travel money, Felix's fate, Mrs. Dunphy, Plautia's bracelet. **Unplanned (flagged):** ibuprofen (WARN-021), the 26 unassigned frames (WARN-020), the Zippo/dime/paperback and the knucklebone hand-off (N-23), Fenn's notebook reunion and Margaret's death (WARN-010), the map's whereabouts and the flash (tracker plan_gaps), Grata fancying Valens (stated in the foundation but never paid on the page).

### Guardrail sweep
- **NO FORESHADOWING:** one anchor needs a forward gesture (WARN-024). The foundation's Ch.38 anchor is a portent (WARN-004). There are label and narration risks (N-18, N-19, N-20). Everything else is stance-safe.
- **NO TICS:** teeth over-scheduled (WARN-022), callback designs (WARN-025), a repeated rage bit (N-22), allowlist over-spend (WARN-023, N-27). No beat depends on "Do they still have mules?", "fine mountain for vines" or "Mama, look" recurring ✓.
- **Heat:** Ch.15/23/34 only; none from Ch.39 ✓ (N-05).
- **Ledger:** approach counts 11/10/5/5/5/5/3 ✓, never two in a row ✓. Ending sig shares quiet 27 / punch 23 / long-fade 20 / dialogue 20 / question 9 ✓, never three in a row ✓. Σ 260,300 ✓. Opening short-punch 18.2% (N-26).

---

## SUGGESTED YAML PATCHES (for the entity-tracker's next UPDATE, after the planning docs are corrected)

```yaml
suggested_patches:
  - entity: "locations.pompeii.facts[0].conflict"
    action: "update"
    reason: "CRIT-001 — canonical: AD 72 is ten years after the AD 62 quake; correct outline:ch-19 + foundation:§5"
  - entity: "plot_threads.valens-known.note_conflict"
    action: "update"
    reason: "CRIT-002 — frame 69 → trial 74 = five years; Ch.23 line must change"
  - entity: "characters.marcus.physical.age"
    action: "update"
    reason: "CRIT-003 — fix one birth year; propagate to foundation Plautia profile, outline Ch.22, both bible cards"
  - entity: "characters.valens.knowledge"
    action: "add"
    value: { fact: "Plautia's brother is suing Celer for the dowry; Valens is the witness", learned_chapter: "TBD (pre-12)", method: "TBD" }
    reason: "WARN-007 — knowledge used in Ch.12/15 without a source"
  - entity: "characters.valens.knowledge"
    action: "add"
    value: { fact: "the door exists, is in Pompeii, leads to Mara's time", learned_chapter: "TBD (15 or 25–33)", method: "told_by:mara-reyes" }
    reason: "WARN-008 — Ch.33 presupposes it"
  - entity: "world_rules[0]"
    action: "update"
    reason: "WARN-017 — allowlisted phrase 'the one it brought' contradicts 'anyone who came through a door'; record the reconciled wording"
  - entity: "world_rules (opening duration)"
    action: "add"
    reason: "WARN-016 — 62 opening 'for a day' vs 79 pre-dawn close; record the canonical duration"
  - entity: "objects.film-roll.spend_plan"
    action: "update"
    reason: "WARN-020 — assign the four named frames to chapters; resolve counter semantics (N-09)"
  - entity: "objects.ibuprofen"
    action: "create"
    reason: "WARN-021 — packed Ch.2, no resolution; Ch.32 exposure"
  - entity: "characters.august-fenn.knowledge"
    action: "add"
    value: { fact: "Mara carries his 1968 notebook; Margaret died 1997", learned_chapter: "TBD (25/26/35)", method: "told_by:mara-reyes" }
    reason: "WARN-010 — unplanned beat that governs the Ch.35 'Margaret' evasion"
  - entity: "plot_threads.backup-boat"
    action: "update"
    reason: "WARN-018 — Ch.37 order (door→boat) vs Ch.40 order (boat→door)"
```
