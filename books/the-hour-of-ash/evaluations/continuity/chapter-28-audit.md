# Continuity Check: Chapter 28 "Felix in the Arena" (MANUSCRIPT AUDIT)

**Date:** 2026-10-24
**Audited text:** `manuscript/chapters/chapter-28.md` as it now stands (md5 `1683aa77…`; after writer, dialogue-polish, hook-craft, disruptor). Line refs are to that file.
**Checked against:** Ch.1–27 (targeted greps), ENTITY_STATE.yaml as of Ch.27, outline Ch.28 (warnings, beat subversion) and Ch.29, foundation.md, STATE.yaml guardrails and AUTHOR-* decisions (CP4-1, CP5-0b, CP5-1 included), voice-dna.md §0/§1/§3b, character-bible.md (Voices from lives, FELIX, VALENS, NICANOR, PRIMA, ALBUCIUS, RUSTICUS, SECUNDUS, At-risk after Ch.26/27/28, the Ch.21 barracks-gate guard).
**Total issues:** 41. **Critical:** 7 | **Warning:** 18 | **Info:** 16

**Verdict:** The spine is clean. Felix's age, status, illiteracy and sherd are right. The news reaches the family without Ch.21's barracks-gate route. Nicanor (trainer) and Albucius (lanista) agree with Ch.21. The arena history is accurate and kept light. Valens never steps onto the sand, nobody names the mountain, there is no tomb, the children are never called citizens, and nobody answers the last line. **The CRITs are local:** one logic break (beasts that were not at home), one cast break (Grata's "boy" as a barefoot child), one forward-reaching clause, the whose-frame rebuilt with Ch.5's answer, two whole spoken lines said again, and a narrated-silence census overrun. Every fix is a cut or a swap of 1–4 words. After the fixes, dialogue stays at about 30% (the Grata cut removes about 50 spoken words).

---

## CRITICAL ISSUES (must fix before the evaluator)

### [CRIT-001] Felix "left your beasts fed and watered" while all four mules were on the Puteoli trip
- **Audit:** 2/5 (logic, objects)
- **Chapters:** 27 and 28
- **Evidence:**
  - Ch.27 l.36: "Valens had led the dun up behind me, the other three strung after her" (all four mules at Puteoli).
  - Ch.28 l.44: "with the four mules in a string behind".
  - Ch.28 l.46 (Grata): "He left your beasts fed and watered for two days and the stable mucked out, he did it in the dark, I give him that, and after that my boy did them, and you'll give him something for it, he did them badly but he did them."
- **Fix (l.46):** replace that sentence with: "He left your stable mucked out, in the dark." (This also drops "I give him that", which Prima echoes at l.126 as "Give him that".)
- **Cascade:** l.48's coppers beat depends on the boy. See CRIT-002, which is fixed by the same cut.

### [CRIT-002] "Grata's boy" is a barefoot child, but Grata's only son is Secundus, the would-be aedile
- **Audit:** 1 (character consistency)
- **Evidence:** Ch.19 l.~136, "My son's at the baths. A lad who means to stand for aedile one day". Ch.20 l.433, her son reads her the Polybius panel "as he set off to bathe". Ch.26 l.140, "my Secundus's" (the Ch.26 CUT list bans "that wall's my boy's"). Ch.28 l.46, "my boy's no use anywhere" and "after that my boy did them". Ch.28 l.48: "Grata's boy had followed her out and stood rubbing one bare foot on the other, hoping to hear what he was owed, and Valens dropped two coppers in his palm, no questions asked. The boy looked at them and ran."
- **Fix:** l.46: "but my husband's no use on a road and my boy's no use anywhere." becomes "but my husband's no use on a road." l.48: delete the two sentences "Grata's boy had followed … The boy looked at them and ran." so the paragraph is "Valens slipped the dun's lead."
- **Cascade:** strike the "Grata's boy" walk-on from the bible's Ch.28 walk-on block (l.~4775). Secundus stays unseen until Ch.31.

### [CRIT-003] Foreshadowing: "in all my time in that town"
- **Audit:** law (voice-dna §0, families C/D)
- **Evidence:** l.250: "I was certain he would do something; nothing in all my time in that town had seemed so sure."
- **Why:** "all my time in that town" measures her Pompeii years as a finished span, seen from after their end. That is a narrating-present outcome implication.
- **Fix:** "nothing in all my time in that town had seemed so sure" becomes "nothing had ever seemed surer".

### [CRIT-004] The CLOSED whose-frame is rebuilt, and with Ch.5's own answer
- **Audit:** law (bible at-risk table: the "who-pays / 'Whose …?' question frame is now CLOSED for every speaker from Ch.23"; Ch.21 CUT "Is he yours?")
- **Evidence:** Ch.5 l.353–357: "Whose are you?" … "Mine." Ch.28 l.358–360: "That bird," she said. "Was he anything of yours?" / "Mine," said Valens.
- **Fix (l.358):** "Was he anything of yours?" becomes "You know him?" Keep "Mine," said Valens. The answer now goes past the question, and the belonging question no longer pairs with Ch.5's answer.

### [CRIT-005] Whole spoken line said again by the same speaker: "Grata would."
- **Audit:** 8 (echo; 2nd use = hard fail)
- **Evidence:** Ch.20 l.197, Felix: "Grata would." Ch.28 l.176, Felix: "Grata would."
- **Fix (l.176):** "Course she did."

### [CRIT-006] "Since when?" is a whole spoken line for the third time book-wide
- **Audit:** 8 (refrain forming; the echo scan's word floor misses 2-word lines)
- **Evidence:** Ch.21 l.66 (Valens), Ch.24 l.66 (Valens), Ch.28 l.74 (Mara): "Since when?"
- **Fix (l.74):** "From when?" ("How long?" is already used in Ch.2 and Ch.8.)

### [CRIT-007] Narrated-silence census: 7 against a cap of 3; Felix's reported silence is CLOSED
- **Audit:** 7 (exhaustive narrated-state census) plus the FELIX card ("his silence as a reported beat ('asked nothing' and kin): CLOSED")
- **Evidence:** l.14 "I could have told her. I watched the sand instead." / l.24 "and after that he had said nothing" / l.86 "If he had an answer, he kept it." / l.200 "Felix's mouth came open. Nothing followed, and he shut it." (also a 3-word echo of Ch.25 l.54, "His mouth came open.") / l.232 "Nicanor, who gave no answer," / l.268 "turned in at the fullery without another word" / l.308 "in silence, for once".
- **Fix:** l.24, cut ", and after that he had said nothing". l.200, delete the paragraph (l.202 already carries "Valens said"). l.232, cut ", who gave no answer," so it reads "He paused at Grata's marble to speak to Nicanor, and then he was walking away…". l.268, cut " without another word". That leaves l.14, l.86 and l.308, which is 3.
- **Cascade:** the narrated mouth states drop from 3 to 2. Felix's silence after "A thraex wants quick." is now shown by absence.

---

## WARNING ISSUES

### [WARN-01] Geography: no Sarno bridge on the road from Puteoli
- l.44: "Aelia had slept since the Sarno bridge". The bay road from Puteoli comes in through Neapolis and Herculaneum to the Herculaneum Gate. The Sarno lies south and east of the town (Ch.19 and Ch.21 put the Sarno *Gate* on the far side). **Fix:** "since the Sarno bridge" becomes "since Herculaneum".

### [WARN-02] Anachronism: a tunic has no pocket
- l.114: "its edges rubbed soft by his pocket." **Fix:** cut " by his pocket" so it reads "its edges rubbed soft."

### [WARN-03] "The dun's thrown a shoe" against the book's period rule (no nailed shoes)
- The outline Ch.24 note says "No nailed horseshoes: the period's equids went barefoot or in strapped hipposandals". Ch.24 trims the dun's bare hooves ("There's nothing left on her to take off"). l.252 reads: "The dun's thrown a shoe," he said. (Ch.26 l.48's "the mules being shod" already strains this; do not compound it.) **Fix:** "The dun's kicking," he said.

### [WARN-04] "bowl" means the arena and the hare bowl in adjacent paragraphs
- l.248 "Lucius went nowhere without the bowl" is followed by l.250 "I had heard the bowl roar that name". l.306 "the bowl answered it with a faint dry hum" is followed by l.310 "The bowl was half full when we climbed to the top of it". A reader can take the hare bowl as half full. **Fix:** l.250, "the bowl roar" becomes "the benches roar". l.310, "The bowl was half full when we climbed to the top of it" becomes "The seats were half full when we climbed to the top". The bout sections (l.36, l.334) can keep "bowl".

### [WARN-05] Arena order: the venatio should come before the pairs
- l.316: "We sat through two pairs and a hunt." The normal day ran the hunt in the morning and the pairs later. **Fix:** "We sat through the hunt and two pairs." (l.22 "the morning's pairs" still holds, and l.316's "During the hunt" is unchanged.)

### [WARN-06] "That wants washing." rebuilds Ch.20's spoken frame
- Ch.20 l.39, Felix: "That wants shouting." Ch.28 l.376, Valens to Felix: "That wants washing." Valens also says "A thraex wants quick." at l.198. **Fix:** "Wash that."

### [WARN-07] A boy's arena wish meets an adult's helpless laugh: Ch.21's frame again
- Ch.21 (the freedman): "he laughed so hard he had to put me down". Ch.28 l.192: "and he laughed till he had to sit, with the whole yard watching." **Fix:** cut "till he had to sit" so it reads "and he laughed, with the whole yard watching."

### [WARN-08] Felix's blush through the ears is a repeat
- Ch.13: "His ears had gone red to the tips." Ch.22: "his ears went red". Ch.28 l.214: "Felix went red from his collar to the rims of his ears." **Fix:** "Felix went red to the collar."

### [WARN-09] Felix's exit with his shoulders up, after an argument with Valens (Ch.21's exit)
- Ch.21: "Off he stalked homeward, nail in hand and shoulders up". Ch.28 l.232: "walking away to the fountain with his shoulders hunched to his ears." **Fix:** cut " with his shoulders hunched to his ears".

### [WARN-10] The editor in the shade with a very white toga: Ch.21's image
- Ch.21: "a youth whose toga showed very white against the shade". Ch.28 l.348: "in the shade of the canvas, gray-haired, his toga very white, a slave at his side". **Fix:** cut "his toga very white, ".

### [WARN-11] "without having got up" copies Ch.27's involuntary-action frame
- Ch.27 l.108: "without having decided to move". Ch.28 l.338: "I was standing too, without having got up." **Fix:** cut ", without having got up".

### [WARN-12] Felix says "too thin" for the third time book-wide
- Ch.13 "He said I'm too thin." / Ch.21 "too thin to finish" / Ch.28 l.196 "Because I'm too thin to hold the board up." **Fix:** "Because my arms won't hold the board up."

### [WARN-13] Prima stops treading twice; her card says "stops only once"
- l.108 "She stopped treading and stood in the gray water." / l.122 "She stood still and considered her white legs in the water." **Fix (l.122):** "She considered her white legs in the water."

### [WARN-14] Census: "grip" ×4 (cap 3)
- l.96 "gripped a rail" / l.128 "gripped it at both ends" / l.178 "gripped two of its fingers" / l.310 "gripping him by both ears". **Fix (l.128):** "Prima hauled the stained cloth clear of the basin and twisted it, and gray drips coursed to her elbows."

### [WARN-15] Census: narrated watching ×5 (cap 3)
- l.14 (Mara), l.24 (Lucius), l.144 "Valens watched Albucius's face", l.330 "I had forgotten to watch it", l.366 "The Gaul watched Lucius go by on his father's arm". **Fix:** l.144 becomes "Valens gave the writing no glance at all." l.366 becomes "The Gaul made a face at Lucius, crossing his eyes."

### [WARN-16] Census: "Felix stood" ×4 (cap 3)
- l.170 "he stood in our doorway", l.332, l.334, l.354. **Fix (l.170):** "then he stood in our doorway" becomes "then he was in our doorway".

### [WARN-17] Paying at Grata's three times (drift toward the closed who-pays family)
- l.180 (Grata's demand, keep), l.232 "Nicanor rose, paid Grata, and came", l.308 "who'd had a bowl of her chickpeas and paid for it and said". Ch.21 already has "and paid" at Grata's bench. **Fix:** l.232 becomes "Nicanor rose and came to stand in our doorway." l.308 becomes "who'd had a bowl of her chickpeas and said".

### [WARN-18] "Nucerian gate": the spelling breaks with Ch.19's "Nuceria Gate", and the door's gate is named in a no-tomb chapter
- l.12: "She sells eggs by the Nucerian gate." **Fix:** "She sells eggs in the forum." ("the Sarno Gate" is already used three times; "Nola" is taken by Rusticus and Prima.)

---

## INFO

- **I-01 Felix: consistent.** He is "eighteen, he tells me" (l.142). That agrees with Ch.21's "Fifteen, then. Sixteen." (winter 73–74), Ch.26's "seventeen that winter, or said he was" and ENTITY's birth AD 58. Free by word only: "of no town he could name", "He never even asked me for a paper" (Ch.11, Ch.19). He can't read: he "watched every letter go in"; Mara reads the tablet; Prima's "He told me it, letter by letter" fits Ch.11, where he knows the letters by shape. The palm follows Ch.20's "a name scratched on every wall in this town but mine" and Ch.21's palm under LVPVS. The Ch.28 palm is fresh (no nail, no doubled stem, no lamp; "drawn with something with a point"), unattributed, and SPENT. Prima is consistent with her card. **Sherd:** "I had scratched those capitals myself, in Valens's shed below Delphi, the winter we met" matches Ch.11 l.434 (a shard of the same jar, in the shed, capitals, ΦΗΛΙΞ). The eyebrow matches Ch.26 (crusted cut, "The dun threw her head", left uncommented). Valens's "Since the must was in the vats" matches Prima's "in the autumn".
- **I-02 News route: clean.** Grata in the street, Prima at the vats, then Albucius's room behind a wine shop, then Nicanor bringing Felix home. "He went nowhere near the barracks or the lanista" (l.250). Ch.21's barracks gate is not rebuilt.
- **I-03 Nicanor vs Ch.21: consistent.** He is the trainer (bald; the rod's one beat at the lintel). The beard "the price of trying him" matches Ch.21's "when I've a beard". His prediction fails on the page (l.238, l.324). "The day of the bear, your middle one went home on his feet." matches Ch.21 l.212/224. *Small points:* l.240 has no tag (Valens is the likely speaker; Mara also saw it). "Twelve years I've worked for Albucius" (since about AD 64) is compatible with training Valens at Corinth before then, and with the AD 59–69 ban if the troupe toured. Nicanor's "And he's told you he'll sell him back" is plausible off-page (Albucius told him), not shown.
- **I-04 Arena history: accurate and light.** The oath matches Petronius 117 (uri, vinciri, verberari, ferro necari): "The burning and the chains and the rods and dying by the iron". A three-year term is plausible. No buyout before the first fight, put as the lanista's business ("I owe the duumvir a pair"); this is better than an invented law. Lanista and editor are distinct, and the editor pays for the dead (as in Gaius's account). The edictum "twenty pairs, a hunt, and awnings", with only the editor's name and filiation, is classic Pompeian. The barracks at the theaters date from after AD 62. The thraex has the griffin crest, brimmed and visored helmet, fasciae, two high greaves, quilted manica, sica and small shield. The murmillo has the fish crest, a tall curved scutum and one left greave. *Optional:* thraex greaves usually came over the knee ("from knee to instep … so high"). The summa rudis rod, the whips, and "kill him, whip him, burn him" (Seneca, Ep. 7.5) are right. Stantes missi is announced by the herald for the editor. Women in the top ring (the lex Iulia theatralis) and the dark-tunic men there are right. Outside stairs and awning masts at the top fit Pompeii.
- **I-05 Prices are consistent across Albucius, Felix and Nicanor** (400 down, "less forty, greaves", the smith's 35). "Two hundred sesterces of bear" is cheap but not checkable. Albucius's "the price comes down on him" runs against how gladiator values rose with experience, but Nicanor marks it as unusual ("Go round every school … asking for that"). Leave it.
- **I-06 Ages.** Late spring AD 76: Lucius about 1 year 10 months, "He is not two yet", the wetting and "Lix" fit (the Ch.29 outline has him "about two and a half" in December). Aelia is about 4–5 months, in the sling, "staring at her earrings". Both fit.
- **I-07 Mules and house.** Four mules ("the dun, the black, the two others"), matching Ch.26 and Ch.27. No upper floor: curtain, pallet, party wall; no stair and no "upstairs". *Nit:* "crossed over" (l.308) and "across" (l.180/270) sit oddly with Ch.19/20's "next door", but the party wall (l.294) settles it.
- **I-08 Laws, clean:** no mountain; no tomb, Eros or Kalends; no "citizen"; Valens stays in the tunnel under the seats and never steps onto the sand; no "by degrees"; no Mara laugh or mouth channel; talking to objects 0 (l.12 "to the bench at large" is people); no em-dash; the present-tense generalisation 1 (the dog whistle).
- **I-09 Speech-habit census (≤2 per speaker): passes.** Felix "Nicanor says" 2, "never" 2, "whole" 2. Prima "never" 2, "twice" 2. Mara "And…" 2, "Nobody…" openers 2, statement plus dry fragment 1. Valens "Lupus's boy" 2 (one speech). Valens's short "He's…" verdicts (free / charging / right) are worth watching. No comparison in Valens's speech; "haul him home by the ear" is dead idiom (CP5-0b).
- **I-10 Nameable-rule test: passes.** Felix gets single questions (the card's "stacks questions" is rotated, as the Ch.26 WATCH asks). Albucius's eggs and Prima's treading come from their lives, not rules.
- **I-11 "could not afterward have told you one thing about it" (l.168)** is past-facing, but it addresses a "you". Optional: "and could not have said one thing about it that evening."
- **I-12 "against a day nobody had named" (l.134)** is safe: the jar dates from Lucius's birth (summer 74, before Fenn's WHEN). Watch that nothing builds on it.
- **I-13 Near-echoes of Ch.21's amphitheater, reworded and acceptable:** "the lane past the exercise ground and the vines" (Ch.21: "between the palaestra wall and the vineyards"); "band after band" (Ch.21: "in their bands"); a food-eating woman beside Mara at the games. They are situations, not strings.
- **I-14 Small nits:** "Stabiae road" (l.134) where Ch.20 has "Stabian road"; the hare "in brown slip" on Ch.20's "brown" bowl; "every soul but one was up" with Lucius also seated (the next line settles it); a cluster of three "knew" in l.16–18; the Ch.21 murmillo bowl promised to the baby is never bought (not a contradiction). The header comment (l.6) still carries the writer's counts.
- **I-15 Gesture classes are at their cap:** Valens's hand on Lucius 3 (l.32, 314, 342); bending 4 (Prima, Valens stooped, Rusticus, the duumvir); kneel/crouch 2. Add none in editing.
- **I-16 Ch.29 setup: clean.** Nothing is pre-spent (no candles, caps, figurines, mime, tears or baseball). Nobody answers "You were sitting down." Felix's "sheep towns" threat does not block his Saturnalia leave. For the Ch.29 writer: rest Valens's stillness, no stacked-question debt, the palm not mentioned, the bowl at most a glance, the line never answered in words.

---

## TRACKING (Ch.28 additions)

**Timeline:** late spring AD 76. The family leaves for Puteoli (Ch.27). Felix swears himself the next day. They come home in the evening (S2). Nine days later are the duumvir's games. Albucius visits the next morning; Nicanor brings Felix at dusk; Prima is at the fountain on day 5; the last night; the games, at noon.

**Knowledge:** Mara and Valens learn of the oath from Grata (l.46). The pair, Rusticus and the greaves come from Albucius and Felix. Felix assumes Valens hasn't come to the sand "since the bear" (from Nicanor). Felix learns of Prima's message from Mara (l.212). The bean woman never learns who Valens is. Felix sees Valens seated (l.380).

**Threads:** the sherd moves to Prima (it was Felix's crack behind the shelving). The hare bowl goes to Lucius. The savings jar is untouched. The release is purchasable after the first fight (open). Felix's three-year term is open.

## SUGGESTED YAML PATCHES (for the entity-tracker, after the editor's fixes)

```yaml
suggested_patches:
  - entity: "walk_ons.ch28.gratas_boy"
    action: "remove"
    reason: "CRIT-002 cut; Grata's only son is Secundus (ch-19:p136, ch-20:p433, ch-26:p63)"
  - entity: "felix.knowledge / felix.timeline"
    action: "update"
    value: { left: "the day after the family left for Puteoli (ch-28 l.46)", stable: "mucked out only (CRIT-001; all four mules at Puteoli, ch-27 l.36)" }
  - entity: "objects.felix_name_sherd.location"
    action: "update"
    value: "Prima, in her neckline (ch-28 l.114); formerly the crack behind the shelving (ch-28 l.60)"
  - entity: "objects.hare_bowl.owner"
    action: "update"
    value: "Lucius, given by Felix (ch-28 l.228)"
  - entity: "plot_threads.whose_frame"
    action: "keep_closed"
    reason: "CRIT-004: ch-28 l.358 recast to 'You know him?'"
  - entity: "timeline.ch28"
    action: "create"
    value: "late spring AD 76; the games nine days after the return from Puteoli"
```

---

## Repair log (book-editor, 2026-10-24)

Pre-repair backup: scratchpad copy only (not in the book folder). After the repair: body 6,677 words (shape 6,664), dialogue **30.5%** (shape 31%), band 25–35. `bash tools/check_chapter.sh 28` prints **ALL MECHANICAL GATES CLEAN** (echo scan 0, tic gate clean, voice-wear strict clean, shape clean). ENTITY_STATE, character-bible, foundation and outline were not touched. The bible's "Grata's boy" walk-on strike (CRIT-002 cascade) and the YAML patches are left to their owners.

| Item | Status | How / why skipped |
|---|---|---|
| CRIT-001 | done | l.46: the fed-and-watered sentence is now "He left your stable mucked out, in the dark." "I give him that" goes with it. |
| CRIT-002 | done | l.46: "…my husband's no use on a road." l.48: the boy and the coppers are cut, so the paragraph is "Valens slipped the dun's lead." |
| CRIT-003 | done | "nothing had ever seemed surer." |
| CRIT-004 | done, varied | The audit's "You know him?" put the tag next to the question as "she said. "You know…", which made 3x "said you know" book-wide (Ch.1, 25, 28) and failed the tic gate. The line is now `"You know that bird?" she said.` with no belonging frame. "Mine," said Valens is untouched. |
| CRIT-005 | done | "Course she did." |
| CRIT-006 | done | "From when?" |
| CRIT-007 | done | Cut l.24's "and after that he had said nothing", the whole l.200 mouth paragraph, l.232's "who gave no answer", and l.268's "without another word". Narrated silences are now 3 (l.14, l.86, l.308). |
| WARN-01 | done | "since Herculaneum". |
| WARN-02 | done | "its edges rubbed soft." |
| WARN-03 | done, varied | I did not use "The dun's kicking": the law asks that the dun's problem stay a foot matter. The line is now "The dun's cracked a hoof." That is a bare-hoof problem, matching the Ch.24 trimming, and it involves no shoe or nails. |
| WARN-04 | done | "the benches roar"; "The seats were half full when we climbed to the top". |
| WARN-05 | done | "We sat through the hunt and two pairs." |
| WARN-06 | done | "Wash that." |
| WARN-07 | done | "and he laughed, with the whole yard watching." |
| WARN-08 | done | "Felix went red to the collar." |
| WARN-09 | done | The hunched shoulders are cut. |
| WARN-10 | done | "his toga very white" is cut. |
| WARN-11 | done | "I was standing too." (the Ch.27 involuntary frame is cut). The grit-in-the-palms control break remains. |
| WARN-12 | done | "Because my arms won't hold the board up." |
| WARN-13 | done | "She considered her white legs in the water." |
| WARN-14 | done | "…clear of the basin and twisted it, and gray drips…". The grip census is now 3. |
| WARN-15 | done | "Valens gave the writing no glance at all." / "The Gaul made a face at Lucius, crossing his eyes." Watching is now 3. This also removes the doubled "his father's arm" in l.366. |
| WARN-16 | done | "then he was in our doorway". |
| WARN-17 | done | "Nicanor rose and came to stand in our doorway." / "who'd had a bowl of her chickpeas and said". |
| WARN-18 | done | "She sells eggs in the forum." |
| I-01, I-02, I-05–I-10, I-12, I-13, I-15, I-16 | no action | These are confirmations or watches. No gesture was added (I-15). |
| I-03 (l.240 untagged) | skipped | The line reads as Valens's in context. Adding a tag would add a beat for no gain. |
| I-04 (greaves over the knee) | skipped | Optional, and the "knee to instep … so high" image stands. |
| I-11 | done, varied | This was the you-address after the fact. The audit's wording "could not have said" echoed Ch.6, so the line is now "and by supper could not name one thing about it." |
| I-14 Stabiae/Stabian | skipped | "on the Stabian road" fails the echo scan against Ch.20. "Stabiae road" (the road to Stabiae) is accurate, so it stays. |
| I-14 header | done | Line 6 now carries the current counts. Other I-14 nits (the "knew" cluster, "every soul but one") are left as they are. |
