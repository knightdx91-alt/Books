# Evaluation: Chapter 28 — Felix in the Arena (run 2) · In medias res: the bout → the nine days that led to it → the bout's end
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-24 | **Cycle:** 0
**Text evaluated:** `manuscript/chapters/chapter-28.md`, md5 `8c6b954795196e2a69b23370d6b917a5`. This is the page after writer → dialogue-polish → hook-craft (one word) → disruptor → continuity repair (CRIT-001…007, WARN-01…18 and the INFO actions, all logged in `continuity/chapter-28-audit.md`). Nothing the repair fixed is raised again.

**Measured on the real file** (from the book folder):
- `bash tools/check_chapter.sh 28`: **ALL MECHANICAL GATES CLEAN** (style with foreshadow 0, grammar, rhythm, show/tell, voice-wear strict, tic gate with gestures, metaphor, SHAPE CLEAN).
- `python3 tools/tic_report.py --echoes 28`: **0 echoes**, 0 command echoes, 0 spoken-line echoes.
- `--gate`: clean. The "jaw ×2" is a false positive: both hits are the beard on his jaw (l.170, l.370), not a gesture.
- Body **6,677** words (shape 6,664; 95% of 7,000). 4 breaks / 5 sections. Dialogue **30.5%** (band 25–35). Median sentence 11 (low gear). 8 similes (fig 1.5/1k). Em-dash 0. And-chains 3/9.
- Section lengths and dialogue: S1 851w at 4% · S2 1,611w at 42% · S3 1,720w at 56% · S4 1,202w at 22% · S5 1,293w at 7%.
- Shape: `short-punch` ("The crowd roared for the wrong man.", 7 words) → `dialogue` ("You were sitting down."). This matches ledger row 28.

**Read against:** the book's CLAUDE.md; STATE.yaml guardrails, retired reflexes, AUTHOR-CP2-2, CP2-3, CP4-1/2, CP5-0b and CP5-1; outline ledger row 28 and `## Chapter 28` (beats, writer warnings, beat subversion), plus the Ch.27 cascade and the Ch.29 section; voice-dna; character-bible ("Voices from lives, not rules"; FELIX, NICANOR, PRIMA, ALBUCIUS and RUSTICUS cards and their Ch.28 blocks; the NO TICS law; At-risk after Ch.27 with the ten Ch.28 guards, and At-risk after Ch.28); chapter-27 (the handoff); chapter-21 (the show, the tunnel pier graffito, the barracks gate); the dialogue, hook and disruption reports; the continuity audit and its repair log; `chapter-27-eval.md` for the bar, the format and the speech-habit census rules recorded there.

**Genre profile:** commercial historical romance / time-slip (comp *Outlander*). Anti-AI band: commercial (0–8 clean). Pattern #11 cap: >6 instances or >0.8/1k. Dimension 7 = **IMMERSION**. Engagement (STATE): empathy 55 / fascination 30 / self-insertion 15. **Theme RECEDES** by design (outline), so it is not penalised for absence.

*(l.N = line number in the evaluated file, md5 8c6b9547.)*

---

## HEADLINE
**CVI-Launch:** **9.4** (8.9, plus 0.5 for a strong anchor) | **CVI-Legacy:** **6.8** | **Genesis Floor:** **8.0** | **Genesis Average:** **8.57** | **Casual Reader:** **9.0**

**Engagement type (this chapter):** Empathy 60 (a boy alone on the sand in borrowed bronze; the father who will not stand) · Fascination 30 (the honest lanista, the crowd that wants blood and gets mercy) · Self-insertion 10.

**Divergence alert:** none (9.4 against 8.0 is 1.4).

The beat subversion lands completely. The bout is dull. Felix will not take the neck of a man tying his greave. The crowd throws a sandal. The champion's courage is to sit, and the son reads that courage as shame in the last line. The anchor, "every soul but one was up. / Valens sat. Lucius sat on his knee." (l.336–338), is among the book's best images.

The Floor sits on hygiene. It is not a structural problem:
1. **Two spoken lines are reused.** "And you?" (l.124) is its **fourth** whole-line use book-wide (Ch.11, 24, 26). "Mine," said Valens (l.358) repeats Ch.5 l.357's "Mine.", Mara's own answer to "Whose are you?". The repair changed the question and left the answer in place.
2. **The cycle-0 census fails four times.**
   - Prima's treading: 8 notes inside ~1,000 words.
   - Grata settling Aelia: 3 inside ~250 words.
   - Albucius eating: 3 inside ~300 words.
   - Valens's boots: 4 inside ~200 words.
3. **Three speech habits go over cap, and one device is shared.**
   - Felix's "cry [a] name": 3.
   - Grata's "had it from": 3.
   - "the fountain" as the town's gossip: 3, shared between Grata and Prima.
4. **The palm is explained, and the explanation rebuilds a Ch.21 frame.** "Its maker had been called out before he could finish." (l.368) gives a reason for an unfinished scratch, the same move as Ch.21 l.288's LVPVS ("where whoever cut it had been jostled"). It is also Pattern #11 on the chapter's chaos image.
5. **Small items:**
   - "a long sliding groan, new to me" (l.36): Ch.21 l.224 already gave her a "low and drawn out" crowd noise.
   - "For no reason at all" labels the irrelevant thought (l.308).
   - "from every side" twice (l.10, l.332).
   - Prima "fished" twice (l.114, l.120) and "hauled" twice (l.112, l.128).
   - "lay awake" twice (l.248, l.304).
   - One dramatic "And then" opener (l.324).
   - The greaves end at the knee.

Every item is a cut or a swap of a clause or less. No beat changes.

**Gate:** Floor 8.0 < 8.5 → **POLISH** (Casual 9.0 ✓, pacing ✓, mechanical gates ✓). The tested fix set below (25 replacements) projects **Floor 8.5 / Average 8.71**.

---

## PACING VS NEIGHBOURS (gate item, judged)

| | Ch.27 | **Ch.28** | Ch.29 (planned) |
|---|---|---|---|
| Shape | Chronological walk, 3 breaks | **In medias res, 4 breaks** | Essayistic (claim → evidence → shame), 3 breaks |
| Length | 7,472 | **6,664** (95%; 6,603 body after the fix set) | 6,600 |
| Gear / median | high / 17 | **low / 11** | high |
| Dialogue | 36% | **30.5%** (31.0% after fixes) | 35–45% |
| Reading speed | a slow walk; still in the cave | **fast bout; measured backfill; fast end** | — |
| Slot | the cautionary mirror (Fenn) | **a secondary's own life; theme recedes** | the family at its fullest |
| Pull | QUESTION PLANT | **EMOTIONAL GUT PUNCH (dramatic irony)** | quiet image |

- **The contrast holds on both sides.** No two neighbours share an approach, a gear, a dialogue band or a pull type. Ch.27's long high-gear talk hands off to a short-sentence chapter with two near-silent bout sections (4% and 7% dialogue). Ch.29 then returns to a high-gear essay.
- **The reading speed is delivered.**
  - S1 is fast once the kit paragraph (l.16, ~170 words) is past; it is orientation the reader needs.
  - S2 and S3 are measured: Grata's flood, the night talk, the vats, the lanista, the contract argument. Each scene has its own engine: can he be bought out, will Valens act, does the girl care.
  - S4 compresses a week into Mara's wrong certainty, then slows for the night before (the feet at Corinth, the humming bowl).
  - S5 runs the dullness on purpose (the beans passed down the bench, the water-boy) into the fastest run in the chapter: strap → roar → rod → cut → herald → sandal. It decelerates in the tunnel to the last line.
- **Value shift, three axes:**
  - **Felix:** anonymous ("nobody caught it", l.10), then alive and jeered, and he reads his father wrong.
  - **Valens:** Mara is sure he will do something ("nothing had ever seemed surer", l.248). He sits.
  - **Mara:** the expectation of rescue becomes grit printed in her palms.
- **The Devourer's soft spot:** the bout is held off for ~4,500 words (68% of the chapter). The cliff at l.40 ("went in again") and the S4 hinge (l.316, "Then the herald cried Rusticus, and the benches answered.", which turns l.10 back on itself) carry it. It is acceptable for the ledger's shape, and this evaluation asks for no change.
- **Handoff:** the Ch.27 guards hold. Felix's absence arrives as news on the return. No Ch.21 barracks-gate route. Nothing sets up a bout for Valens. The palm is the last reservation. Nobody names the mountain. "Lix" is the only word from Lucius. No Kalends walk, no voicemail. Ch.29 inherits "Felix alive" and an unanswered line.

**PACING: OK.**

---

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | **9.0** | Four elements:<br>(1) The champion's courage is to sit: "Along the whole long curve of the top ring, every soul but one was up. / Valens sat. Lucius sat on his knee." (l.336–338). Ch.21's raised open palm comes back as an open hand "on the stone at his side" (l.340).<br>(2) Felix's mercy is the dull bout's climax, and the crowd's fury answers it: Rusticus "bent sideways to his left shin… and began to tie it" while "The bowl went mad for him to do it" (l.330–332).<br>(3) The honest lanista with a sulking bear: "A sniff, he tells me. Two hundred sesterces of bear." (l.156).<br>(4) Prima: "That fat's better than burned." (l.126). | none |
| Theme | **8.5** | Recedes as planned. What remains is carried by acts:<br>- "He's free. I said it at Kirrha, with the Cilician listening. You don't say that and then come round after and haul him home by the ear." (l.80)<br>- the cloth of savings carried "the way that boy's mother at Nuceria must have carried hers" (l.134)<br>- "I'd be one more pair of feet on that sand. I'll watch." (l.290)<br>Texture is far above 30%: the pear boy and the bear, the wine stain "they'll say it was me", the water-boy, the Gaul crossing his eyes, Grata's husband's one sung line. | not 9.0: Valens states the free/haul line in so many words (l.80), and the hare "never gained an inch" (l.242) is a slightly pointed emblem |
| Characters | **8.0** (uncapped 9.0) | **Felix** is distinct by speed and single questions ("Robbed me? He gave me what he promised.", l.218; "Why's that?", l.218). He boasts in four shapes (the oath "never tripped", the greaves "made to my legs", "quicker on his feet than Rusticus" by message, "His ear was mine for the taking"). He refuses his wish aloud, "I'd sooner you stayed away" (l.226), then hunts the good benches in the parade (l.310).<br>**Valens** misreads greed ("He wants more. He's looked the boy over", l.162) and chooses where to sit and why (l.274), with no comparisons and nothing remarked.<br>**Albucius, Prima, Nicanor (the wrong prediction), Rusticus (the strap), the bean woman** (chanting "at her husband's niece's husband", l.336) each have their own life.<br>**Mara's chaos is 4/4** (below). | **Spoken-line reuse (law):** "And you?" 4th book-wide; "Mine." from Ch.5.<br>**Census, 4 failures:** Prima treading 8; Grata/Aelia 3 in ~250 words; Albucius eating 3 in ~300 words; Valens's boots 4 in ~200 words.<br>**Speech habits over cap:** Felix "cry… name" 3; Grata "had it from" 3; "the fountain" 3, shared by two speakers (bleed).<br>→ **cap 8.0**, the same practice as Ch.24–27 for clause-level census and reuse failures. Spec-literal reading of NO-TICS would be 7.5; the book's evaluators have applied 8.0 when every failure is a one-clause fix, and this evaluation keeps that line so scores stay comparable. |
| Prose & Voice | **8.0** | **Stopping sentences:**<br>- "whenever a cart rolled by outside the bowl answered it with a faint dry hum on the floor… Toward cockcrow I rose and nudged it onto the blanket's edge, a fingernail's breadth. The humming stopped. He slept on." (l.304)<br>- "every soul but one was up. / Valens sat." (l.336–338)<br>- "Felix's name went up after it into the noon, and nobody caught it." (l.10)<br>- "and the lanista counted every coin and gave the cloth back to her full." (l.52)<br>**Underlines:** "they might have been borrowed off someone else" (l.96); "with the face of a boy cheated once already" (l.94); "the knock came to us after the sight of it, small and flat" (l.36); "When I unclenched my hands, the bench's grit had printed itself into both palms." (l.360); "I looked down to see were they still on me." (l.298).<br>**Ugly sentence:** "I slept some and not much and then it was morning." (l.86).<br>**Voice under pressure:** S5 clips to "He would make them go on. There was no doubt in me." / "For a breath the sound meant nothing to me." (l.348–352). | not 8.5 at cycle 0:<br>- the palm explained, with Ch.21's frame (l.368, #11)<br>- "For no reason at all" labels the chaos device (l.308)<br>- "new to me" against Ch.21 (l.36)<br>- "from every side" ×2 (l.10, 332)<br>- "fished" ×2 and "hauled" ×2 in Prima's scene<br>- "lay awake" ×2<br>- "And then he did nothing…" (#6, l.324)<br>- "a dish of eggs… eating eggs" doubled (l.136) |
| Pacing | **8.5** | See PACING VS NEIGHBOURS. The ledger is matched; the value shift is clean; the ending is the strongest pull in Part Two since Ch.25. | not 9.0: the ~4,500-word hold on the bout and S4's summary paragraph (l.248) |
| Emotion | **9.0** | **The anchor lands exactly as outlined** (l.336–340), and the wet knee makes it truer: "During the hunt he wet himself, and Valens shifted him to the dry knee." (l.314).<br>**Surprise as designed:** the dull fight; the crowd enraged by mercy; the bean woman joins the chant against her own family; comedy in dread (the bear "sulking", the pear boy's "There was a bear before").<br>**Body rebel:** grit printed in her palms; dressed before he is back from the stable (l.248).<br>**Techniques:** dramatic irony in the last line; objects (the bowl, the sherd, the strap, the palm); withholding (the palm never attributed); humour; displaced subtext ("Why's that?" answered with Albucius's gate, l.218–220). | none |
| Immersion | **9.0** | The Pompeian edictum with only the editor's name and his father's ("twenty pairs, a hunt, and awnings", l.88); the auctoratus oath as Petronius gives it (l.108); the thraex and murmillo kit (l.16, 26); the summa rudis rod, the whip slaves, "kill him, whip him, burn him" (Seneca, l.336); stantes missi cried by the herald for the editor (l.350); women in the top ring and the dark-tunic men; the awnings hauled up the masts; the lanista's tablet "less forty, greaves" (l.144); a fullery's treading basins and bleached legs. Harshness holds at ~7: one cut, "a dark finger's length", and no gore. | not 9.5: thraex greaves rose over the knee, and the page has "from knee to instep" (l.16) and "to the knee" (l.184). Fixed by I1–I2. |
| **FLOOR** | **8.0** | Characters, Prose | |
| **AVERAGE** | **8.57** | (9.0 + 8.5 + 8.0 + 8.0 + 8.5 + 9.0 + 9.0) / 7 | |

---

### Narrated-state census: EXHAUSTIVE, cycle 0 (spec: >3 notes of one state, or 3 inside ~500 words, fails)
**Class rulings, fixed here so later cycles do not re-argue them:**
- The anchor (Valens seated with Lucius on his knee: l.20, l.338, l.340) is ONE designed frame, opened in S1 and closed in S5.
- The griffin at l.16 is the kit described, not a state. The griffin *aimed* (Felix looking through it) counts.
- Object threads with a different function each time are not states (the satchel ruling in Ch.27): the hare bowl (given 226, shown 242, carried 246, slept beside 304) and the bean woman's bag (held 12, shared 324, spilled 332, gathered 354).
- Fight actions are not states unless the same action is re-noted. Shield-high (324, 332, 342) is counted, because it is Valens's advice taken.

| Character | State | Lines | Count / spacing | Verdict |
|---|---|---|---|---|
| Valens | hand / arm on the boy | 32 · 312 · 340 | 3, spread | OK (at cap; add none) |
| Valens | seated outside the anchor | 66 "sat out on the shop step… sitting out there yet" · 242 took my stool · 274 sat on the bed | 3 notes, but 66 says it twice | → **C6** (66 once). Sitting is the chapter's engine; keep the backfill to one note each |
| Valens | attention elsewhere | 144 no glance · 314 the ropes on the masts · 340 eyes on the sand | 3, spread | OK |
| Valens | boots / laces | **274 · 278 · 284 · 288** | **4 inside ~200 words** | **FAILS** → C7a, C7b → 2 (274 start, 288 the boots toes to the wall) |
| Valens | silence / delay | 86 kept his answer · 296 let so long go by | 2 | OK |
| Felix | restless feet / bounce | 18 · 192 · 324 | 3, spread | OK |
| Felix | griffin aimed | 36 · 332 · 352 | 3, spread over S1 and S5 | OK |
| Felix | stood (bout) | 330 · 332 · 352 | 3 | OK (the repair's WARN-16 holds) |
| Felix | shield high | 324 · 332 · 342 | 3 | OK |
| Felix | chin lifted | 196 · 310 | 2 | OK |
| Felix | halts | 218 · 370 (36 is a fight action) | 2 | OK |
| Felix | talking fast | 170 · 372 | 2 | OK |
| Lucius | watching | 24 · 364 | 2 | OK |
| Lucius | grips | 178 · 310 (96 is Prima's) | 2; grip class 3 | OK |
| Lucius | "fist" (WATCH ≤3) | 0 | — | OK |
| Aelia | asleep / awake / fed | 44 · 52 · 66 | 3 different states | OK |
| Grata | settling Aelia | **46 lifted and settled on her shoulder · 52 rocking · 56 hitched up her shoulder** | **3 inside ~250 words** | **FAILS** → C2 → 2 |
| Prima | treading | **96 rose and trod · 98 kept on treading · 104 came down hard · 108 "A tread, another." · 108 stopped · 108 trod again, harder · 118 went on treading · 120 without breaking her step** | **8 inside ~1,000 words** | **FAILS** (and a nameable rule: "she treads harder when it hurts") → C1a–C1e → 2 beats (96 intro; 108 the card's one stop and resume) |
| Prima | sherd against her skin | 118 · 336 | 2 | OK |
| Albucius | eating | **136 eating eggs / dish of eggs · 148 ate half an egg · 148 fingers on a napkin** | **3 inside ~300 words** (the eggs said twice in 136) | **FAILS** → C8, P5 → 2 |
| Nicanor | bald head · cheek · squint · rod tap | 170 · 232 · 236 · 240 | 1 each | OK |
| Rusticus | board turned to track Felix | 30 · 324 · 342 (26 is the intro) | 3 | OK |
| Bean woman | bag / beans | 12 · 324 · 332 · 354 | object thread | OK by ruling |
| Mara | watching elsewhere / eyes off the fight | 14 · 34 · 328 (248 studied his face) | 3 | OK (34 and 328 are the strap's setup and payoff) |
| Mara | wrong certainty | 248 "nothing had ever seemed surer" · 348 "There was no doubt in me" (34 "expected") | 2 + 1 | OK (her distortion; watch the shape) |
| Mara | hands | 208 wanted something · 360 grit | 2 | OK |
| Mara | sleeplessness | 86 · 248 "lay awake" · 304 "I lay awake" | 3, with "lay awake" verbatim twice | → **C9** → 2 |
| Gesture class | bend / stoop | 112 Prima · 242 Valens · 330 Rusticus · 346 the duumvir | 4 across 4 people; gate cap for 6.6k = 6 | OK (add none) |
| Gesture class | kneel / crouch / squat | 62 · 226 | 2 | OK |

### Speech-habit census: EVERY speaker, one pass (spec: >2 of one habit fails)
Rules as recorded in `chapter-27-eval.md` cycle 2: pronoun-copula openers ("He's…", "That's…") are grammar, not habit. Reporting verbs ("He said…") are grammar. A walk-on repeating the noun of their subject is subject matter, not habit.

| Speaker | Habit | Lines | Count | Verdict |
|---|---|---|---|---|
| Felix | "cry [a] name" as his measure of fame | 122 (relayed by Prima) "no crowd ever cried a baker's name" · 226 "they'd cry your name" · 372 "no one will cry my name" | **3** | **FAILS** → C5 → 2 |
| Felix | "Nicanor says" | 218 · 372 | 2 | OK (Nicanor named 6× in his speech: his world, not a tic) |
| Felix | "never" | 172 · 218 | 2 | OK |
| Felix | "whole" | 192 · 226 | 2 | OK |
| Felix | "everybody" | 214 · 222 | 2 | OK |
| Felix | questions | "Did she show you?" · "Robbed me?" · "Why's that?" · "You saw him?" | 4 shapes, single | OK. The card's stacked bursts are rotated out, as the Ch.26 WATCH asked |
| Felix | doubled phrase | 196 "Say so, then. Say I can't." | 1 | OK |
| Valens | "How much…?" | 146 · 182 | 2 | OK |
| Valens | "Who…?" | 190 · 234 | 2 | OK |
| Valens | "Albucius" as opener | 216 · 220 | 2 | OK |
| Valens | "He's…" verdicts | 80 · 186 · 194 | grammar by rule | OK (watch) |
| Valens | doubled phrase | 274 "Lupus's boy" ×2 | 1 | OK |
| Mara | "And…" opener | 78 · 124 | 2 | OK. V1 takes it to 1 |
| Mara | "Nobody…" | 92 · 110 | 2 | OK |
| Mara | statement + dry fragment | 84 "…with him. The sherd." · 210 "The girl at the fullery. Prima." | 2 | OK (at the cap from Ch.28) |
| Prima | "never" | 104 · 108 | 2 | OK |
| Prima | "twice" | 108 · 126 | 2 | OK |
| Prima | retort answering a boast with a price | 126 "fat's better than burned" · 254 "bread's heavy when there's enough of it" | 2 | OK (her card's axis) |
| Prima | "I'm to…" | 122 · 254 | 2 | OK |
| Prima + Grata | "the fountain" as the gossip | Grata 46 "the fountain had it from her by noon" · Prima 104 "my aunt told the fountain" · Prima 258 "The fountain says so." | **3, shared by two speakers** | **FAILS** (a shared device; bleed) → C4 → 2 |
| Grata | "[X] had it from [Y]" | 46 ×2 · 306 | **3** | **FAILS** → C3 → 2 |
| Grata | "the fuller's girl" | 46 ×2 | 2 | OK |
| Albucius | "he tells me" | 142 · 156 | 2 | OK (at cap) |
| Albucius | "the duumvir" | 148 ×3 · 152 | his subject | OK by rule |
| Nicanor | — | orders and verdicts; one simile ("the way a pup goes at a cart wheel") | — | OK |
| Bean woman | "bird" | 12 · 356 | 2 (her question returning) | OK |
| Pear boy | "bear" | 90 · 94 | his subject | OK |

### Spoken lines reused (law), checked by hand below the scan's word floor
Every ≤5-word spoken line in Ch.28 was matched against Ch.1–27:
- **"And you?" (l.124):** Ch.11 l.544, Ch.24, Ch.26 l.222. This is the **fourth** use. It is the same severity as the repair's CRIT-006 ("Since when?" at 3). → **V1**.
- **"Mine," said Valens (l.358):** Ch.5 l.357, "Mine.", Mara's answer to "Whose are you?", one of the book's charged lines. The repair broke the question frame (CRIT-004) and kept the answer. A whole line said again is a second use, and this one borrows Ch.5's weight instead of earning its own. → **V2**: "My boy," said Valens. It closes the chapter's "Lupus's boy" thread (l.274: he will not let the crowd make Felix *Lupus's* boy). Albucius's "your boy" (l.148) gets its answer. The dramatic irony of the last line sharpens, because Felix never hears his father claim him to a stranger.
- "Mara." and "Lupus," are names; "Yes." is exempt.

### Nameable-rule test (AUTHOR-CP5-0b)
- **Felix:** pass after C5. The risk was lexical ("cry a name"); his want for fame is his life, and it stays.
- **Prima:** fails on the treading ("she treads harder when it hurts"). → C1. Her two retorts are her card's axis; leave them at 2.
- **Valens:** no comparison and nothing remarked. The sitting is the chapter's situation, not a rule, once the backfill notes are single (C6). Pass.
- **Grata:** her floods are her voice (one direct, two reported). The gossip-chain construction fails at 3 → C3.
- **Albucius, Nicanor, Rusticus:** pass.
- **Mara:** pass (two wrong certainties, each a different situation).

---

## CVI-Launch Breakdown (Commercial Assessment)
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8/10 | A cliff at l.40, then backfill with its own engines and a fast S5. The hold on the bout is long (~4,500 words). |
| Tomorrow Test | 5 anchors → 10 | IMAGE: the one man sitting while the ring stands, the boy on his dry knee; the bowl humming on the floor, nudged a fingernail's breadth; Rusticus tying his greave and Felix not taking the neck; the unfinished palm. QUOTE: "You were sitting down." / "That fat's better than burned." |
| Casual Reader | 9/10 | See the reports. |
| Shareability (quote/plot/emotional) | 3/3/4 → 6/6/8 → MAX 8 × 0.6 + AVG 6.67 × 0.4 = **7.5** | "the gladiator who won't stab a man tying his shoe, and the crowd throws a sandal" / "fat's better than burned" / the father who sits |
| Concept Pitch | yes (10) | "The boy he freed swears himself to the arena, and the old champion's only move is to sit in the top row with his baby on his knee and watch." |
| Human Closeness | yes (10) | A household around a boy who left it; father, son, wife, toddler, girl, landlady |

**CVI-Launch = 0.2(8) + 0.2(10) + 0.2(9) + 0.2(7.5) + 0.1(10) + 0.1(10) = 8.9, plus 0.5 for a strong anchor = 9.4.**

**CVI-Legacy (default weights)** = Originality 9.0 × .30 + Theme 8.5 × .25 + Cultural vocabulary 3 × .20 + Re-readability 6 × .15 + Identity 5 × .10 = 2.70 + 2.125 + 0.60 + 0.90 + 0.50 = **6.8**.

Re-readability comes from the Ch.21 inversions: the raised palm against the open hand on the stone, Felix pulled down in Ch.21 against Valens alone seated now, and the barracks "Are you [ashamed]?" against "You were sitting down." The legacy figure is low because this is a breathing chapter by design; it is not a defect.

---

## Anti-AI Scan (20 Patterns) — 6,677 words; commercial band (0–8 clean)
1. Forced symmetry: **Found, 1** (minor). "He gave two steps. Rusticus gave two steps." (l.342) is earned (a stalemate).
2. Empty poetic vocabulary: Clear.
3. Rule of three: **Found, 4** (0.6/1k, moderate): l.22 wives / grandmothers / dark tunics; l.136 "broad, soft, clean-shaven"; l.352 nut shells, crusts, a sandal; l.364 "oil, sand dust and wet stone". The syntax varies and none is anaphoric. The chant (l.336) is quoted Seneca and is excluded.
4. Em-dashes: 0. Clear.
5. Empty metaphors: Clear. All 8 similes characterise.
6. "And" openings: **Found, 1 in narration** (minor): "And then he did nothing with any of it." (l.324). → P4. Speech "And…" openers are Mara's at 2, and V1 takes them to 1.
7. Pseudo-philosophical closings: Clear. S3 closes on the hare "never gained an inch" (l.242), an object image; the Theme row notes it as slightly pointed.
8. Excessive parallelism: **Found, 1** (minor): "Over supper I studied his face for it. After dark I listened for him." (l.248).
9. Overly smooth transitions: Clear. "Nine days before," cuts hard.
10. Described emotions: **Found, 2** (minor): "impatient to be let go" (l.18); "I was certain" (l.248) is a distortion stated so it can be proved wrong.
11. Explanatory extension: **Found, 4** (0.6/1k, minor; under the cap of 6 / 0.8): l.22 "who sat at the top because the good seats were spoken for"; l.60 "so that no dust could settle where the hare ran"; l.208 "because my hands wanted something"; **l.368 "Its maker had been called out before he could finish."** The last one explains the chapter's chaos image and rebuilds Ch.21's frame. → L1.
12. Binary negation opener: Clear.
13. Precision flex: **Found, 1** (minor): "Ten places along" (l.336). The prices (400, forty, thirty-five, two hundred) are the contract plot, not a device.
14. Emotional control demonstration: **Found, 1** (minor): "I could have told her. I watched the sand instead." (l.14). The control fails later (l.360).
15. Authoritative description: Clear. The kit is filtered through what "nothing had warned me" of (l.16).
16. Philosophical asides: Clear. "The duumvir's mean. Dead men cost him." is trade talk.
17. Clean dialogue: **Found, 1** (minor). The contract argument (l.182–206) is turn-based but at cross-purposes ("Keep it up, then." / "I keep it where I like."). The two adjacent Valens paragraphs (l.198/200) show Felix's silence by absence.
18. Thematic echo chamber: Clear.
19. Graduated reveal: Clear (in medias res, per the ledger).
20. Emotional temperature report: Clear.

**Total: 10 patterns present, all minor except #3** (watch band 9–11, low end). After the fix set, #6 and #11's worst instance go, and the total falls to about 8 (clean).

## Laws scan
- **NO FORESHADOWING:** clean. "against a day nobody had named" (l.134) dates from before the WHEN. Prima's "Two years… or three" (l.122) and Felix's "the rest of my three years" (l.372) are character speech; the irony is the reader's own historical knowledge, which the law allows. No narrator line reaches forward. style_check foreshadow 0.
- **Nobody names the mountain; no tomb:** clean (grep: mountain / Vesuv / tomb / Kalends / Eros / citizen all 0).
- **Valens never steps into the arena:** clean. He stays in the top ring, then in the tunnel under the seats.
- **No glorious set-piece:** clean. The bout is a rim knock, a turned blow, circling, the strap, one cut.
- **Felix has no catchphrase:** clean after C5.
- **Harshness ~7:** held.
- **NO TICS:**
  - Phrase and gesture gates clean.
  - The census is above: 4 narrated-state failures and 3 speech-habit failures (one shared), all fixed in one set.
  - Nameable-rule test above.
- **Retired reflexes:** no significance-tagging, no define-by-negation, no anaphora triad (the Seneca chant is quotation), no performed candour, no device as a scene-button, no closing aphorism.
- **No spoken line reused:** two failures (V1, V2), above.
- **Closed / spent lists:**
  - The whose-frame stays closed ("You know that bird?" asks no belonging question; V2 keeps the answer clear of Ch.5).
  - "by degrees" 0; "a long moment" 0.
  - Felix's reported silence: 0 (the repair's CRIT-007 holds).
  - "too thin" 0; ears-red 0; shoulders-up exit 0; the white toga 0.
  - Lucius's Smoke / Duck / Bone / Again 0.
  - The palm: one use, the last reservation, unattributed.
- **Ch.21 not rebuilt:**
  - The barracks gate is not used. The herald does not cry Lupus. The tunnel is a different passage.
  - **One frame was rebuilt:** an unfinished graffito with its cause supplied (Ch.21 l.288 "where whoever cut it had been jostled" → l.368). → L1.
  - "a long sliding groan, new to me" (l.36) contradicts Ch.21 l.224's "low and drawn out" noise. → L2.
  - The egg-selling niece and the food-eating neighbour sit near Ch.21's egg basket and sausage girl. These are situations, not strings; INVESTIGATE only, no change.
- **AUTHOR-CP2-2 (memory inserts):** Gloria's rice (l.308) is triggered by the saffron and is one sentence. It is labelled "For no reason at all", which is wrong (the saffron is the reason) and mediates the device. → P1. The eyebrow paragraph (l.64) is a recall triggered by the empty corner and picked up at l.70. OK.

---

## Character Chaos Check (Primary — Mara)
- **Irrelevant thought: present.** Gloria's yellow rice and Ray salting it (l.308); the pear boy's bear (l.90–94).
- **Cognitive distortion: present, inhabited.** Mara plans Valens's rescue for him: "Lupus for a nobody… Or on the day itself he would vault the parapet" (l.248). "He would make them go on. There was no doubt in me." (l.348). Both are wrong.
- **Unprompted memory: present, triggered and returning.** The saffron → Gloria; the empty corner → the split eyebrow (l.64) → "You knew about the eyebrow" (l.70).
- **Failed emotional management: present.** "When I unclenched my hands, the bench's grit had printed itself into both palms." (l.360); "Once, when he left our bed for the stable in the night, I had my clothes on before he got back." (l.248).
- **Voice under pressure: demonstrated.** S5's sentences shorten and harden (l.338, 348).

## Secondary Character Chaos
- **Felix:** his own moment. The palm left unfinished; the bowl given to Lucius; he hunts the good benches after forbidding them.
- **Valens:** his own moment. He unpicks and re-stitches a sound strap (l.66); "I couldn't feel my feet" (l.298); he misreads Albucius.
- **Prima:** her own moment. The wine stain "they'll say it was me" (l.112); the baker's nephew and the second oven.
- **Albucius:** his own moment. The bear off its food.
- **Nicanor:** his own moment. The prediction fails on the page.
- **Grata:** her own moment. The Nuceria cousin; the silent take-over of Aelia "for once".
- **Rusticus:** his own moment. The strap tied in full view.
- **Lucius:** his own moment. He stands on the clean patch and pats it (l.62); the threshold fall with the bowl held up (l.246).

---

## The Tomorrow Test
**What the reader remembers:** a whole ring of benches on its feet screaming for the whip, and one man sitting in it with a toddler on his dry knee. Then the boy in the tunnel: "You were sitting down."
**Anchor type:** BOTH (image: the seated man; the bowl humming on the floor, nudged a fingernail's breadth; the greave tied in plain view. Quote: "You were sitting down." / "That fat's better than burned.").
**Verdict:** ANCHOR EXISTS. Its type (gestural / visual, a body's stillness) differs from Ch.27's tactile palm on rock and Ch.26's read letter.

**Shareability:** "The kid could have killed the guy while he was tying his shoe, and he didn't, and the whole arena threw things at him."

---

## Reader Reports
### The Devourer
- Hooked by line 1 and by the bird on his head.
- Annoyed for a page that the cut to "Nine days before" (l.44) holds the fight. Grata's flood wins them back ("I'll not charge you for knowing it").
- Skims the painter panel, reads Prima and Albucius at speed, and slows for the contract argument.
- S4's planning paragraph is summary they would skim.
- S5 is a pure page-turn from the strap to the sandal.
- Would finish. Soft spot: the length of the hold.

### The Critic
- Underlines l.10, l.52, l.96, l.304, l.336–338 and l.360, and the last line.
- Admires that the palm is never attributed and that Valens's reasons are given once and never glossed.
- Disappointed by:
  - the palm's last sentence explaining what the image already showed
  - "For no reason at all" naming its own chaos device
  - Prima treading in every other sentence
  - Albucius's eggs twice in one sentence
  - "from every side" twice
  - "Mine." as a Ch.5 callback the scene has not earned in its own words

### The Hostile
- "'A long groan, new to me' — she heard the crowd groan at the Saturnalia show (Ch.21)."
- "'Mine' — that's Mara's line to Kallia in Ch.5. Lazy."
- "'And you?' again."
- "Thraex greaves came over the knee."
- "How does Felix pick out one seated man in the top ring, through a punched visor, from the middle of the sand?" (INVESTIGATE only: he hunted the benches in the parade, a gap in a standing ring shows, and the line is his claim. No change.)
- "Valens speaks two paragraphs running at l.198/200." (INVESTIGATE only: it reads as Felix's silence.)

### The Casual Reader — 9.0
- Stays for the bird helmet, Grata, and the girl with white legs who calls him an idiot.
- LIKES Felix at once: the boast about his greaves, "Say I can't."
- Feels the end in the stomach without needing it explained.
- Would tell a friend "the gladiator chapter where nothing happens and it wrecked me."
- The backfill does not lose them, because every scene has a person in it they enjoy.
- No vibes problem.

### The Devoted Reader (active)
- Will notice:
  - the open hand on the stone against Ch.21's raised palm
  - Felix pulled down in Ch.21 against Valens alone seated now
  - the barracks question "Are you [ashamed]?" against the last line
  - the bear thread (Ch.21's bear → the pear boy's "There was a bear before" → Albucius's sulking bear)
  - the sherd moving from the crack to Prima's skin
  - the palm unfinished on the right
- Would catch "Mine." from Ch.5 and the Ch.21 graffito frame (fixed by V2 and L1).
- Will write the Reddit post about Valens sitting.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| Spoken lines reused ("And you?" 4th; "Mine." from Ch.5) | | ✓ | ✓ | | ✓ | IMPORTANT → V1, V2 |
| Palm explained / Ch.21 graffito frame (l.368) | | ✓ | | | ✓ | SHOULD FIX → L1 |
| Census failures (Prima treading, Grata/Aelia, Albucius eating, boots) | | ✓ | ✓ | | | SHOULD FIX → C1, C2, C7, C8 |
| "new to me" against Ch.21 | | | ✓ | | ✓ | SHOULD FIX → L2 |
| Speech habits ("cry a name", "had it from", the fountain) | | ✓ | | | | INVESTIGATE (cheap; fixed C3–C5) |
| Prose doubles; "For no reason at all"; "And then" | | ✓ | | | | INVESTIGATE (cheap; fixed P1–P5, C9) |
| Greaves height | | | ✓ | | ✓ | INVESTIGATE → I1, I2 |
| Bout held ~4,500 words | ✓ | | | | | INVESTIGATE (no change: ledger shape) |
| Felix sees a seated man from the sand | | | ✓ | | | INVESTIGATE (no change) |
| Egg seller / food neighbour near Ch.21 | | | | | ✓ | INVESTIGATE (no change) |

---

## Revision Recommendations (Ranked) — ONE fix set, all tested
Script: `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes28/apply_fixes.py <chapter-28.md>`. It runs **25 replacements**. Each must match exactly once, or the script aborts and writes nothing. A re-run on a fixed file aborts safely (tested).

**Tested on a scratch copy** (`/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/eval28/books/the-hour-of-ash/`, with the repo `tools/` linked so the shape audit runs):
- `bash tools/check_chapter.sh 28`: **ALL MECHANICAL GATES CLEAN**.
- `--gate`: clean.
- `--echoes 28`: **0 echoes**, 0 command echoes, 0 spoken-line echoes.
- Hand re-check: no ≤5-word spoken line of Ch.28 now repeats Ch.1–27, except names and "Yes.".
- Body **6,603** words, dialogue **31.0%** (band 25–35). `short-punch` → `dialogue` unchanged.
- Result md5: `d18ec6403c38c9d617954a7fae26f292`.

**How the replacement strings were checked:**
- Against Ch.1–27 by the echo scan and the tic gate.
- Two first drafts failed the gate and are **not** in the script: "What did you tell him?" (made "what did you" a 3× spoken refrain) and "from above the knee" (made "from above the" 3× in prose).
- Against the bible's CUT/SPENT lists and closed frames: "My boy" is not spoken anywhere in Ch.1–27, and Grata's cut "my boy" was hers, about Secundus, and is not restored. No whose-frame. "chanting" is new to dialogue. "They say so at the vats" puts no new figurative habit on Prima; it is where she works.
- Against this census: the fixes add no gesture, no sit, no tread, no "fountain", and no new "whole/every".
- No earlier pass's cut is restored. The opener, the anchor (l.336–340) and the last line are untouched.

| ID | Location | Problem type | What happens now | Why it fails | Revision direction (exact, in script) | Project rule? |
|---|---|---|---|---|---|---|
| V1 | l.124 | Voice (spoken reuse) | "And you?" | 4th whole-line use book-wide (Ch.11, 24, 26) | "What was your answer?" (Prima's "That fat's better than burned." answers it exactly) | No (law already) |
| V2 | l.358 | Voice (spoken reuse) / Character | "Mine," said Valens. | Ch.5 l.357's "Mine." said again; borrows Ch.5's charge | "My boy," said Valens. (closes "Lupus's boy", l.274, and answers Albucius's "your boy", l.148) | Yes: a charged one-word line is never re-spoken by another character |
| L1 | l.368 | Continuity (Ch.21 frame) / Style #11 | "…and then nothing. The rest of that side was bare plaster. Its maker had been called out before he could finish." | Supplies the cause of an unfinished scratch, as Ch.21 l.288 did; explains the chapter's chaos image | End the paragraph at "…and on the right two fronds, and then nothing." | Yes: an unfinished mark is never given its cause by the narrator |
| L2 | l.36 | Continuity | "a long sliding groan, new to me, that travelled the whole oval" | Ch.21 l.224 gave her a "low and drawn out" crowd noise | "a long sliding groan that went right round the oval" | No |
| C1a–e | l.98, 104, 108, 118, 120 | Character (census) | treading 8×: "kept on treading" / "came down hard on her left foot" / "A tread, another." / "went on treading" / "without breaking her step, fished" | 8 notes in ~1,000 words; nameable | Cut the four beats; l.108's stop and resume stays as her one break; "hooked the strap out" (also ends "fished" ×2) | No |
| C2 | l.56 | Character (census) | "Grata hitched Aelia up her shoulder." | Third Aelia-handling beat inside ~250 words | Cut; the two quotes join | No |
| C3 | l.306 | Character (speech habit) | "because she'd had it from the trainer, who'd had a bowl of her chickpeas and said" | Grata's "had it from" ×3 | "because the trainer had eaten a bowl of her chickpeas and said" | No |
| C4 | l.258 | Character (shared device) | "The fountain says so." | "the fountain" as gossip ×3 across Grata and Prima | "They say so at the vats." | Yes: no town metonymy is shared between speakers in one chapter |
| C5 | l.226 | Character (speech habit) | "they'd cry your name before I was halfway" | Felix's "cry [a] name" ×3 | "they'd be chanting Lupus before I was halfway" | No |
| C6 | l.66 | Character (census) | "and he was sitting out there yet" | The sit said twice in one paragraph; the backfill dilutes the anchor | "and he was out there yet" | No |
| C7a–b | l.278, 284 | Character (census) | "He stood the first boot against the plaster." / "His hands went on with the laces." | Boots 4× inside ~200 words | Cut both; the quote merges to "…They don't call heralds. Bring Lucius." and the l.284 paragraph is "I would have argued it." | No |
| C8 | l.148 | Character (census) | "He rubbed his fingers clean on a napkin." | Albucius eating 3× inside ~300 words | Cut; the quotes join | No |
| C9 | l.304 | Character (census) | "Soon he slept. I lay awake. Lucius lay" | Sleeplessness 3; "lay awake" verbatim with l.248 | "Soon he slept. Lucius lay" (her wakefulness is shown by the hum and cockcrow) | No |
| P1 | l.308 | Style (mediated chaos) | "For no reason at all I thought of my cousin Gloria's…" | Labels the device; the saffron is the reason | "I thought of my cousin Gloria's…" | No |
| P2 | l.332 | Style | "The noise came from every side together" | "from every side" ×2 (l.10) | "The noise came from all sides together" | No |
| P3 | l.128 | Style | "Prima hauled the stained cloth clear" | "hauled" ×2 in the scene (l.112) | "Prima dragged the stained cloth clear" | No |
| P4 | l.324 | Style #6 | "And then he did nothing with any of it." | Dramatic And-opener | "Then he did nothing with any of it." | No |
| P5 | l.136 | Style | "with a dish of eggs at his elbow and their shells picked off into a small white pile" | Eggs twice in two sentences | "with the shells picked off into a small white pile at his elbow" | No |
| I1–I2 | l.16, 184 | Immersion (factual) | "from knee to instep" / "Bronze ones, to the knee." | Thraex greaves rose over the knee | "from mid-thigh to instep" / "Bronze ones, past the knee." | No |

### Fix order: Logic/Character (V1, V2, L1, L2, C1–C9) → Structural (none) → Connective (none) → Prose (P1–P5) → Factual (I1–I2)

### Bookkeeping for finalize (not page edits)
- **Bible: re-sync the Ch.28 blocks from the final page.** Stale or changed strings:
  - FELIX: "Grata would." → "Course she did."; "too thin" → "my arms won't hold the board up"; "laughed till he had to sit" → "laughed, with the whole yard watching"; "Nicanor told me all that" → "I had all that my first day."; "Never. He gave me…" → "Robbed me? He gave me…"; "cry your name" → "chanting Lupus"; the after-bout burst as on the page.
  - VALENS: "That wants washing." → "Wash that."; "Mine." → "My boy."
  - PRIMA: treading beats cut; "fishes" → "hooks"; "The fountain says so" → "They say so at the vats"; "And you?" → "What was your answer?".
  - ALBUCIUS: no napkin; "I'd have bet on today"; "Nicanor wrote the name in"; "the price comes down on him".
  - RUSTICUS: the wife sells eggs "in the forum", not by the Nucerian gate.
  - NICANOR: "paid" at Grata's is gone; "Forty he's had off him".
  - Walk-ons: strike "Grata's boy" (audit CRIT-002 cascade).
  - At-risk after Ch.28: "Mine." → "My boy."; "That wants washing." → "Wash that."; the palm's last two sentences CUT; log every old string above as CUT.
- **Header (l.6):** the counts will be stale after the fix set (body 6,603, dialogue 31.0%).
- **ENTITY:** greaves over the knee; Prima's source "the vats".

## Strengths to PRESERVE
- The opener l.8 and l.10 ("…into the noon, and nobody caught it.").
- The kit and "I knew him by his feet" (l.16–18). Only I1 touches it.
- Grata's flood and the Nuceria cousin "gave the cloth back to her full" (l.46–56). Only C2 touches it.
- The clean patch and Lucius patting it (l.60–62).
- The night talk: "Since the must was in the vats." / "haul him home by the ear" / "If he had an answer, he kept it." / "I slept some and not much…".
- The pear boy.
- Prima's bleached legs, the wine stain, the sherd "letter by letter", and "That fat's better than burned."
- Albucius, the bear and "A sniff, he tells me."
- Valens's misreading at the corner.
- "Say so, then. Say I can't."
- The bowl given to Lucius ("Keep your fingers off where the hare is.").
- Nicanor's verdict and "Twice this year." with the rod tap.
- "I couldn't feel my feet… After, I had them back."
- The humming bowl nudged a fingernail's breadth.
- The strap-tying refusal.
- The anchor l.336–340, verbatim.
- The herald, the sandal end over end, and the grit in her palms.
- The Gaul crossing his eyes.
- The unfinished palm (shorter after L1, never attributed).
- The last line and its silence after.

---

## PATH TO 8.5
- **Characters 8.0 → 8.5 requires:** no reused spoken line, every census row ≤3 with none at 3-in-500, and no speech habit over 2.
  - Apply V1 and V2 (the reuses), C1a–e (Prima's treading down to her one stop), C2 (Grata/Aelia), C7a–b (boots), C8 (Albucius), C9 (sleeplessness), C6 (the doubled sit), and C3–C5 (the "had it from", "the fountain" and "cry a name" habits).
  - Every one is a cut or a ≤6-word swap. No line of Felix's boasting, no Prima retort and no Valens decision is touched.
  - After the set, the census table has no failing row, and the nameable-rule test passes for Prima, Grata and Felix.
- **Prose 8.0 → 8.5 requires:** the chapter's best images trusted and its hygiene clean, since the stopping sentences already qualify (l.304, l.336–338, l.10).
  - Apply L1 (the palm ends on "and then nothing."; this also removes the Ch.21 frame), L2 ("new to me"), P1 (the chaos label), and P2–P5 (the doubles and the And-opener).
  - The opener, the anchor and the last line keep their words.

**Projected after the fix set:** Originality 9.0 · Theme 8.5 · Characters 8.5 · Prose 8.5 · Pacing 8.5 · Emotion 9.0 · Immersion 9.0 (I1–I2 correct the greaves; it stays at 9.0) → **Floor 8.5 / Average 8.71**, Casual 9.0. No dimension moves more than +0.5.

## VERDICT
**POLISH.** Floor 8.0 (Characters, Prose) < 8.5. Casual 9.0 ✓. Pacing OK ✓. Mechanical gates clean ✓.

Apply `apply_fixes.py` to `manuscript/chapters/chapter-28.md`, re-run `bash tools/check_chapter.sh 28` and `python3 tools/tic_report.py --echoes 28`, then re-evaluate (cycle 1) using the census rulings recorded above.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

---

## Cycle 1
**Evaluator:** book-evaluator (independent) | **Date:** 2026-10-24 | **Text:** `manuscript/chapters/chapter-28.md` md5 `d18ec6403c38c9d617954a7fae26f292`. That is exactly the tested cycle-0 result, so the 25-replacement script was applied verbatim (commit 5bd0d38). Line numbers below are for this file.

**Measured:**
- `bash tools/check_chapter.sh 28`: ALL MECHANICAL GATES CLEAN. Shape is clean: `short-punch` → `dialogue`.
- `--echoes 28`: 0 echoes, 0 command echoes, 0 spoken-line echoes.
- Body 6,603 words; dialogue 31.0%.

### Verdict: **POLISH** (cycle 1). Floor **8.0** (Characters).
- Casual 9.0 ✓. Pacing OK ✓. Gates clean ✓.
- Every cycle-0 finding is resolved on the page.
- Three new findings remain:
  - One item cycle 0 missed: Grata's gossip chain, which repeats Ch.20.
  - Two doubles that my own cycle-0 swaps created: "right round", and the thigh/shin wobble.
  - One phrase my C4 swap kept: "say so" ×4 in the chapter.
- All four are fixed by a 4-replacement tested script. **Projected after it: Floor 8.5 / Average 8.71 → PASS.**

### 1. Cycle-0 findings verified on the page

| ID | Now on the page | Status |
|---|---|---|
| V1 | l.124 "What was your answer?", answered by "That fat's better than burned." | ✓ |
| V2 | l.358 "My boy," said Valens. Not spoken anywhere in Ch.1–27, and Grata's cut "my boy" is not restored | ✓ |
| L1 | l.368 ends "…and on the right two fronds, and then nothing." The cause is not given, so the Ch.21 frame is gone | ✓ |
| L2 | l.36 has no "new to me". **But see R2:** the swap "went right round the oval" doubles l.310's "right round to the gate" | ✓ / new double |
| C1a–e | Prima's treading is down to the intro (l.96) plus the one stop and resume (l.108). l.120 has "hooked the strap out", so "fished" is now ×1 (l.114) | ✓ |
| C2 | Grata/Aelia: l.46 settled, l.52 rocking | ✓ |
| C3 | l.306 "because the trainer had eaten a bowl of her chickpeas" | ✓ (but see R1) |
| C4 | l.258 "They say so at the vats." **But** "the fountain" as gossip is still shared, by Grata l.46 and Prima l.104, so cycle 0's own rule ("no town metonymy shared between speakers") is not yet met. See R1 | partial |
| C5 | l.226 "chanting Lupus". Felix's "cry… name" is now 2 (l.122 relayed, l.372) | ✓ |
| C6 | l.66 "and he was out there yet". The sit is said once | ✓ |
| C7a–b | Boots at l.274 and l.288 only. "I would have argued it." (l.284) reads as elliptical, not dangling | ✓ |
| C8 | l.148 has no napkin. Albucius is narrated eating twice (l.136, 148) | ✓ |
| C9 | l.304 "Soon he slept. Lucius lay…". "lay awake" ×1 (l.248) | ✓ |
| P1 | l.308 "I thought of my cousin Gloria's…". The label is gone and the saffron triggers it | ✓ |
| P2 | l.332 "from all sides together". 0 uses in Ch.1–27 | ✓ |
| P3 | l.128 "dragged". "hauled" ×1 in the scene | ✓ |
| P4 | l.324 "Then he did nothing with any of it." | ✓ |
| P5 | l.136 "with the shells picked off into a small white pile at his elbow". "eggs" ×1 in the sentence pair | ✓ |
| I1 | l.16 "from mid-thigh to instep". **But see R3:** "to the top of the thigh. Over each shin a greave… from mid-thigh" puts "thigh" in adjacent sentences and a thigh-high greave "over each shin" | ✓ fact / new wobble |
| I2 | l.184 "Bronze ones, past the knee." | ✓ |

The census rows hold as classified at cycle 0. No failing row remains:
- Prima treads 2 beats.
- Grata 2, Albucius 2, boots 2.
- Valens seated outside the anchor: 3, spread.
- Mara sleepless: 2.

The fixes added no new narrated state. "hooked" / "dragged" are Prima's hands at work, once each.

### 2. New problems check (fix-created, or missed at cycle 0)
Every replacement string was checked against Ch.1–27, the voice-bank, voice-dna, the bible's SPENT/CUT lists and the ten Ch.28 guards.
- **No guard is broken:** the palm is unattributed, nobody names the mountain, and the herald does not cry Lupus.
- **No CUT string is restored.**
- **No continuity break:** "past the knee" and "mid-thigh" agree with each other and with l.34's strap "below the knee".

Four items remain:

| ID | Location | Problem type | What happens now | Why it fails | Revision direction (exact, in script) | Project rule? |
|---|---|---|---|---|---|---|
| R1 | l.46 (Grata) | Character (speech habit, book-wide) + Continuity (2nd use) | "and the fuller's girl had it from him first and the fountain had it from her by noon." | Ch.20 l.579 Grata: "she reckons I had it from her **at the fountain**". With Ch.28's two uses, that is the same gossip chain 3× in her mouth book-wide. "had it from her" plus the fountain is a 2nd use the echo scan cannot see, because the word order is reversed. It is also the last thing keeping "the fountain" as gossip shared with Prima (l.104), against C4's rule. Missed at cycle 0, which counted inside the chapter only | "and the fuller's girl was the first he told." Prima's "He told me first." (l.104) now corroborates her, and her "my aunt told the fountain" stays hers alone | Yes: speech-habit census also checks the speaker's earlier chapters |
| R2 | l.36 | Style (double, created by L2) | "a long sliding groan that went right round the oval" | "right round" also at l.310 (and Ch.4 l.133). My swap planted it | "Out of the bowl came a long sliding groan, and the griffin…" The groan already comes from the bowl | No |
| R3 | l.16 | Style / Logic (created by I1) | "Quilted cloth wound both legs to the top of the thigh. Over each shin a greave was strapped from mid-thigh to instep," | "thigh" in adjacent sentences, and a greave "over each shin" that starts at mid-thigh | "Quilted cloth wound both legs to the groin. A greave was strapped over each from mid-thigh to instep," | No |
| R4 | l.258 (Prima) | Style (my C4 string kept a phrase) | "They say so at the vats." | "say so" ×4 in the chapter: Prima l.108 and l.258, Valens l.166, Felix l.196 | "They talk of it at the vats." This leaves one per speaker. "talk of it" is 0 in Ch.1–27, the voice-bank and the bible | No |

Also checked and passed (no change):
- "hook" family ×3 in three senses, 4,000+ words apart: l.120 hooked out, l.208 unhooked, l.370 hooked on two fingers.
- "chanting" is new to the book.
- "dragged the" is a common verb, with no frame.
- "What was your answer?" is unique.
- "the fountain" at l.108 is the literal place.
- l.36's "whoever had made it" is the griffin hunting a noise. It is not the closed maker-conjecture frame.

**R1 is why the floor holds.** It is the same class of item that held Ch.22 cycle 2 and Ch.27 cycles 2–3 at 8.0: one clause-level speech habit / cross-chapter echo, which the book treats as law. R2–R4 are hygiene. They do not hold the floor, but two of them were planted by this evaluator's own swaps, so they go in now and not later.

### 3. Scores (cycle 1, the page as it stands; max +0.5 vs cycle 0)

| Dimension | Cycle 0 | **Cycle 1** | Evidence / cap |
|---|---|---|---|
| Originality | 9.0 | **9.0** | Unchanged. The seated champion (l.336–340); the strap-tying mercy (l.330–332); Albucius's bear; "That fat's better than burned." |
| Theme | 8.5 | **8.5** | Unchanged. Recedes by design; "haul him home by the ear" (l.80) is still stated outright |
| Characters | 8.0 | **8.0** | Census clean. Spoken reuses gone ("What was your answer?", "My boy,"). Felix's habit is at 2. **Held by R1:** Grata's gossip chain is 3× book-wide and a hidden 2nd use of Ch.20 l.579, and the fountain metonymy is still shared. After R1 → **8.5** |
| Prose & Voice | 8.0 | **8.5** (+0.5) | Cycle-0 holds are cleared: the palm trusts its image (l.368), the chaos device is unlabelled (l.308), and "new to me" and the And-opener are gone. Stopping sentences stand: l.10 "…and nobody caught it."; l.304 the bowl nudged "a fingernail's breadth"; l.336–338. The ugly sentence is l.86. Voice under pressure: l.348–352. R2–R4 required before finalize, but they do not hold the score |
| Pacing | 8.5 | **8.5** | Unchanged. 6,603 words; S5 runs strap → sandal at speed; the ledger is matched |
| Emotion | 9.0 | **9.0** | The anchor is untouched (l.336–340). "My boy," (l.358) sharpens the last line's irony: Felix never hears it |
| Immersion | 9.0 | **9.0** | The greaves are corrected (l.16, l.184). R3 tidies the kit sentence |
| **FLOOR** | 8.0 | **8.0** | Characters |
| **AVERAGE** | 8.57 | **8.64** | (9.0+8.5+8.0+8.5+8.5+9.0+9.0)/7 |

**Casual Reader: 9.0** (unchanged; the fixes touch nothing a casual reader notices).

**CVI-Launch: 9.4.** Inputs: pacing 8, anchors 10, casual 9, shareability 7.5, pitch 10, closeness 10, giving 8.9; plus 0.5 for a strong anchor.

**CVI-Legacy: 6.8.** Inputs: 9.0×.30 + 8.5×.25 + 3×.20 + 6×.15 + 5×.10.

**Anti-AI:**
- 8 of 20 patterns, which is the clean band. #6 is gone, and #11 is down to 3 (0.45/1k): l.22, l.60, l.208.
- After R1–R4 the patterns stay at 8.

**Pacing gate: OK.** The ledger row is matched, and the contrast with Ch.27 and Ch.29 holds as tabled at cycle 0.

### 4. Fix script (tested)
`/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes28/apply_fixes_c1.py <chapter-28.md>`. It makes **4 replacements** (R1–R4). Each must match exactly once, or nothing is written. A re-run aborts safely; tested.

Tested on the scratch copy `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/eval28/books/the-hour-of-ash/`, starting from md5 d18ec64:
- `check_chapter.sh 28`: **ALL MECHANICAL GATES CLEAN**. Tic gate clean, voice-wear strict clean, SHAPE CLEAN.
- `--echoes 28`: **0** echoes, 0 command echoes, 0 spoken-line echoes.
- Body **6,561** words; dialogue **31.0%**. `short-punch` → `dialogue` unchanged.
- After the script: "had it from" 0 in Ch.28; "right round" 1; "say so/says so" 3, one per speaker; "thigh" 2, 300 lines apart.
- Result md5: **`493621cce8584454710f8a15985afab3`**.
- Untouched: the opener, the anchor (l.336–340), the palm, the last line, and every cycle-0 replacement.

**Projected after R1–R4:**

| Dimension | Projected |
|---|---|
| Originality | 9.0 |
| Theme | 8.5 |
| Characters | 8.5 |
| Prose | 8.5 |
| Pacing | 8.5 |
| Emotion | 9.0 |
| Immersion | 9.0 |

That gives **Floor 8.5 / Average 8.71**, Casual 9.0 → **PASS** at cycle 2.

Cycle 2 needs only:
1. Confirm md5 `493621cc…`.
2. Re-read l.16, l.36, l.46 and l.258 in place.
3. Re-run the gates.

### 5. Bookkeeping for finalize (bible re-sync, from the page after R1–R4)
- **Cycle-0 sync list (above) stands**, with these corrections:
  - **PRIMA:**
    - "hooks the twin's strap out", not "fishes". She still "fished inside her neckline" for the sherd.
    - "They talk of it at the vats." Not "The fountain says so", and not "They say so at the vats".
    - Treading: the intro, plus the one stop and "She trod again, harder.", and nothing else.
    - "dragged the stained cloth clear".
    - Mara's question to her: "What was your answer?"
  - **GRATA:**
    - "and the fuller's girl was the first he told."
    - "because the trainer had eaten a bowl of her chickpeas and said".
    - "hitched Aelia up her shoulder" is CUT.
    - WATCH: the gossip chain "had it from" is rested (Ch.20 l.579 is its only use). "the fountain" as gossip belongs to Prima in Ch.28.
  - **VALENS:** "Wash that."; "My boy."
  - **ALBUCIUS:** no napkin; "the shells picked off into a small white pile at his elbow" (no dish of eggs).
  - **FELIX (kit):**
    - Quilting "to the groin".
    - Greaves "from mid-thigh to instep" / "Bronze ones, past the knee."
    - "chanting Lupus".
    - "no crowd ever cried a baker's name" (relayed) and "no one will cry my name" are 2/2: SPENT.
  - **MARA:** CUT "For no reason at all", "I lay awake" (l.304), "new to me", "And you?".
- **At-risk after Ch.28: replace the writer-draft block.**
  - SPENT: "Mine." → "My boy."; "That wants washing." → "Wash that."; the sliding groan, now bare, with no trailing clause.
  - CUT log: every cycle-0 old string; plus R1 "had it from him first and the fountain had it from her by noon", R2 "that went right round the oval" / "that travelled the whole oval", R3 "to the top of the thigh. Over each shin", R4 "They say so at the vats." / "The fountain says so."; plus rejected drafts "What did you tell him?" and "from above the knee"; plus the palm's last two sentences.
  - WATCH: "right round" rested (Ch.4, Ch.28 l.310); "say so" 1 per speaker; "hook/hooked" 3 in Ch.28.
- **Project rules to record:**
  - V2: a charged one-word line is never re-spoken by another character.
  - L1: an unfinished mark is never given its cause by the narrator.
  - C4, corrected: a town metonymy used as gossip belongs to one speaker per chapter.
  - R1: the speech-habit census also counts the speaker's earlier chapters.
- **Header l.6:** body 6,561, dialogue 31.0%, revision "evaluator cycles 0–1".
- **ENTITY:** greaves to mid-thigh; quilting to the groin; Prima's source "the vats".

### PATH TO 8.5 (cycle 1)
- **Characters 8.0 → 8.5 requires:** R1, Grata's l.46 clause recast to "and the fuller's girl was the first he told." That is the only floor-holding item.
- **Required hygiene with it (not floor-holding):** R2, R3 and R4, since my own swaps planted two of them.
- Apply `apply_fixes_c1.py`, re-run `check_chapter.sh 28` and `--echoes 28`, then run cycle 2 as a confirmation pass.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

---

## Cycle 2
**Evaluator:** book-evaluator (independent) | **Date:** 2026-10-24 | **Text:** `manuscript/chapters/chapter-28.md` md5 **`493621cce8584454710f8a15985afab3`**. That is exactly the tested cycle-1 result, so `apply_fixes_c1.py` was applied verbatim (commit 6ce7ff0). Line numbers below are for this file.

**Measured on the real file:**
- `bash tools/check_chapter.sh 28`: **ALL MECHANICAL GATES CLEAN**. Style, grammar, rhythm (the same one advisory paragraph as cycle 1), show/tell, voice-wear strict, tic gate with gestures, metaphor. **SHAPE CLEAN**.
- `--echoes 28`: **0** echoes, 0 command echoes, 0 spoken-line echoes.
- Body 6,561 words; dialogue 31.0%.

### Verdict: **POLISH** (cycle 2). Floor **8.0** (Characters).
- Casual 9.0 ✓. Pacing OK ✓. Gates clean ✓.
- R1–R4 are all confirmed on the page.
- The orchestrator's question about "the fuller's girl" ×2 is ruled **natural; no change** (§2).
- **But this cycle ran the character bible's per-chapter lexical caps by hand, which cycles 0 and 1 did not.** Four caps fail. All four were on the page from cycle 0 and none was created by a fix. **This is my miss, not the editor's.**
  - One is a speech habit: Felix's "nobody" at 3. It has been on his WATCH since Ch.11.
  - Under cycle 0's own PATH TO 8.5 ("no speech habit over 2"), that holds Characters.
- The fix is a 5-replacement tested script. **Projected after it: Floor 8.5 / Average 8.71 → PASS at cycle 3.**

### 1. The four lines cycle 1 asked to re-read, in context
| Line | On the page | Ruling |
|---|---|---|
| l.16 | "Quilted cloth wound both legs to the groin. A greave was strapped over each from mid-thigh to instep, so high and stiff that he crossed the sand lifting his feet like a wading bird." | ✓ "each" takes "both legs" cleanly. "thigh" appears once in the paragraph. It agrees with l.34's strap "below the knee" and l.184's "past the knee". |
| l.36 | "Felix hopped clear. Out of the bowl came a long sliding groan, and the griffin tipped upward at the benches, hunting for whoever had made it." | ✓ "right round" is now ×1 (l.310). The groan is bare, with no "new to me" and no trailing clause. "the bowl" as the arena (l.36, l.332) sits beside the hare bowl: WATCH only. |
| l.46 | "…and the fuller's girl was the first he told." … "and the fuller's girl says he's to be a Thracian, whatever that means to her." | ✓ "had it from" 0; Grata's "fountain" 0. Prima's "He told me first." (l.104) corroborates it. The double is ruled in §2. |
| l.258 | "Your husband was Lupus," she said. "They talk of it at the vats. Nine times, and the emperor's own sword." | ✓ "say so" now 1 per speaker (l.108 Prima, l.166 Valens, l.196 Felix). Prima's "the vats" ×2 in the scene (l.254, l.258) is her workplace, two beats apart with the walk home between: subject matter, not habit. |

### 2. Ruling: "the fuller's girl" ×2 in Grata's l.46 speech, natural; no change
- **The count did not change.** Cycle 0's census already had this row ("Grata | 'the fuller's girl' | 46 ×2 | 2 | OK"). R1 recast the first clause ("had it from him first" → "was the first he told") but did not add a mention or move one.
- **The structure did not change either.** Both mentions were already subject-first before R1.
- **The repeat is necessary.** About 70 words and five subjects come between the two mentions (the stable, the blanket, the bowl, the duumvir's games, the painter's notice). A bare "she says he's to be a Thracian" would leave the reader hunting for the referent in a flood that has already moved on.
- **The tag needs the noun.** "whatever that means to her" only lands if "her" is the girl named a beat before.
- **It is Grata's voice, not a habit.**
  - She names people by trade or role: "the bald one", "the painter", "a cousin of mine", and on the morning of the games "the trainer" and "the lanistas".
  - Coming back to the girl twice is the gossip's grievance: the girl knew first, and the girl has the details.
  - Under the rule recorded in `chapter-27-eval.md`, a speaker repeating the noun of her subject is subject matter, not habit.
- **Book-wide it is 2/2.** "fuller's girl" occurs nowhere in Ch.1–27, so there is no cross-chapter echo. It is now rested for Grata: no third use in her mouth.
- **No fix is supplied.** A variant ("that girl at the fullery", "she") would either be a new string or blur the referent. That is the "fix that creates a finding" the brief warns against.

### 3. New findings: bible caps checked by hand (all present since cycle 0)
Cycles 0 and 1 ran the gate, the echo scan and the narrated-state and speech-habit census. Neither ran the bible's per-chapter **lexical caps**, which `tic_report.py` does not measure. Run now, against the page at md5 493621cc:

| ID | Location | Problem type | What happens now | Why it fails | Revision direction (exact, in script) | Project rule? |
|---|---|---|---|---|---|---|
| S1 | l.372 (Felix) | Character (speech habit on WATCH) | "…in sheep towns where nobody can tell one fighter from another, and no one will cry my name in this town again." | Felix's "nobody" has been on WATCH since Ch.11 (6 there; Ch.20 spoken "Nobody…" openers 4, Felix 2). Ch.28 has 3: l.188 "Nobody else can wear them.", l.214 "She'd show nobody that…", l.372. The sentence also pairs "nobody … and no one …", the same shape as the narration at l.64. **This holds the floor**: cycle 0 defined Characters 8.5 as "no speech habit over 2". | "…in sheep towns where they can't tell one fighter from another, and no one will cry my name in this town again." Felix "nobody" → 2. "they can't tell" is 0 in Ch.1–27. | Yes (below) |
| S2 | l.64 (narration) | Style (bible WATCH) | "Nobody in the house had believed it, and no one asked him again." | The "Nobody had [verb]" narration frame is WATCH, ≤1 per chapter from Ch.25 (Ch.24 had 3). l.64 and l.134 ("against a day nobody had named") make 2. l.64 is also the "Nobody…, and no one…" pair. | "Nobody in the house believed it, or asked him again." The frame → 1 (l.134 stays: the Laws scan cleared it at cycle 0). The pair → 0. The simple past matches "Felix said" in the sentence before. | No |
| S3 | l.352 (narration) | Style (bible cap) | "nut shells, crusts, a sandal from somewhere low down that tumbled end over end" | Narration "somewhere" is capped at 2 per chapter (the Ch.15 rule, checked at Ch.23). Ch.28 has 3: l.10, l.30, l.352. The sandal's source is already given ("It started with the men below… whatever they had in their hands"). | "nut shells, crusts, a sandal that tumbled end over end". "somewhere" → 2. A pure cut. | No |
| S4 / S5 | l.180, l.44 (narration) | Style / Character (bible cap; a narrated trait doubled) | l.44 "Grata was round her marble and out to us before the dun had come to a stop." · l.180 "I heard her start on him before he had sat:" · l.354 "Before anybody had cleared the sandal away, the horns were sounding…" | The race frame "before [X] had" is capped at ≤1 per chapter after Ch.20 (from Ch.19, where 3 were cut). Ch.28 has 3 races. Two of them clock **Grata's speed** with the same frame, so a trait of hers is narrated twice through one device. | l.180 → "I heard her start on him:". l.44 → "…out to us as the dun came to a stop." (she is already there when it stops, so the speed is still implied). l.354 stays: it is the arena's indifference, close to the anchor. Race frame → 1. | No |

**Class rulings, so cycle 3 does not re-argue them:**
- **The race frame** counts a narrated contest between two agents or events. l.308's "Ray salting it before he had tasted it" is one man's habit, and the habit is the joke, so it is **not counted**. For the record, Ch.21, 24 and 26 were finalized at 2 by the same regex. The ≤1 cap had stopped being checked after Ch.20, and Ch.28 brings it back.
- **Felix's other absolutes are within cap:** "never" 2 (l.172, 218), "everybody" 2 (l.214, 222), "whole" 2 (l.192, 226).
  - "keep" ×3 (l.206, 214, 226) is used in three senses: hold a position, retain, keep off. It is a verb, not a habit.
  - "She'll come… She'll be there… and she'll see." (l.214) is a boy's insistence in speech, not a rhetorical anaphora triad. Only two of the three are sentence-initial.
- **Spoken "Nobody…" openers:** after S1 there are 4 across three speakers (Mara l.92, l.110; Felix l.188; Nicanor l.236 answering "Who'll kill him?"). Only two are line-initial. WATCH; no owner over 2.
- **Valens's "feet" ×4** (l.200 "can't see your feet", l.238 "on his feet", l.290 "one more pair of feet", l.298 "couldn't feel my feet") is the chapter's planned motif (outline: the feet at Corinth): four idioms in four scenes. Not a habit. Rest it in Ch.29.
- **"Bring Lucius."** (l.278) against Ch.27 l.62's "Bring the boy's hat." is a common two-word imperative in a different situation. INVESTIGATE only; rest the "Bring [the boy…]" order in Ch.29.
- **l.30's "the two notes you whistle at a dog"** is a definite description in the generic present, not a comparison. The present-simile gate (cap 1) counts l.16's vinedresser simile, and that one alone. No change.
- **Other bible caps checked and passed:**
  - "[noun] nobody had [verb]ed" 1 (≤2); sentence-initial narration "Nobody" 1 (≤1)
  - "the one / the only" 0 (≤3); "so that" 2 (WATCH >4); "the size of a" 1 (≤1)
  - "[S]omebody had [verb]" inference 0 (≤1); narrated non-answer 1 ("If he had an answer, he kept it.", ≤1)
  - "I could have…" 1 (≤1); spoken "Then…" 1 (≤2); "And…" rejoinders 2 (≤4)
  - anadiplosis 1 ("They circled. They circled…", ≤1); haul in a non-rope sense 1 (≤1)
  - in-law as joke-butt 1 (≤1); `to the (knee|thigh…)` 0 (≤2)
  - body-part rulers 2 ("a fingernail's breadth", "a dark finger's length"; WATCH ≤4)
  - Mara's ledger: "And…" 1, statement + dry fragment 2 (at the Ch.28 cap), re-ask 1
  - Lucius "fist" 0
  - Ch.27's rest list (jenny, oyster stakes, bars of sun, pick strokes) 0

### 4. Fix script (tested)
`/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes28/apply_fixes_c2.py <chapter-28.md>`. It makes **5 replacements** (S1–S5).
- It refuses any input whose md5 is not `493621cc…`.
- Each replacement must match exactly once, or nothing is written.
- A re-run aborts safely (tested).

Tested on the scratch copy `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/eval28/books/the-hour-of-ash/` (Ch.1–27 byte-identical to the repo; repo `tools/`):
- `check_chapter.sh 28`: **ALL MECHANICAL GATES CLEAN**. Tic gate clean, voice-wear strict clean, SHAPE CLEAN. The rhythm advisory is unchanged.
- `--echoes 28`: **0** echoes, 0 command echoes, 0 spoken-line echoes.
- Body **6,549** words; dialogue **31.0%**. `short-punch` → `dialogue` is unchanged.
- **Counts after the script:**
  - race frame 1 (l.354); narration "somewhere" 2
  - "Nobody had [verb]" 1 (l.134); Felix "nobody" 2
  - spoken "nobody" 5 (Mara 2, Felix 2, Nicanor 1); "Nobody…, and no one…" 0
- **Replacement strings checked:**
  - None of "they can't tell", "or asked him", "as the dun came" or "start on him:" occurs in Ch.1–27, the voice-bank or the bible's CUT lists.
  - No earlier pass's cut is restored.
  - No gesture, sit, tread or "whole" is added.
  - The opener, the anchor (l.336–340), the palm, the last line and every cycle-0/1 replacement are untouched.
- Result md5: **`5b980701f4000d3f2c7ce7d7744f4393`**.

### 5. Scores (cycle 2, the page as it stands; max +0.5 vs cycle 1)
| Dimension | Cycle 1 | **Cycle 2** | Evidence / cap |
|---|---|---|---|
| Originality | 9.0 | **9.0** | The seated champion, "every soul but one was up. / Valens sat. Lucius sat on his knee." (l.336–338); the strap-tying mercy (l.330–332); "A sniff, he tells me. Two hundred sesterces of bear." (l.156) |
| Theme | 8.5 | **8.5** | Recedes by design; carried by acts ("I'd be one more pair of feet on that sand. I'll watch.", l.290). Not 9.0: "haul him home by the ear" (l.80) is stated outright |
| Characters | 8.0 | **8.0** | R1 is confirmed: Grata's gossip chain is gone, and "the fountain" as gossip is Prima's alone (l.104). The census is clean; the spoken reuses are gone ("What was your answer?", "My boy,"). **Held by S1:** Felix's WATCH word "nobody" at 3 (l.188, 214, 372). S4/S5 also clock Grata's speed twice with one frame. After S1–S5 → **8.5** |
| Prose & Voice | 8.5 | **8.5** | The stopping sentences stand: l.10 "…into the noon, and nobody caught it."; l.304, the bowl nudged "a fingernail's breadth. The humming stopped. He slept on."; l.336–338. Ugly sentence l.86. Voice under pressure l.348–352. #11 at 3 (0.46/1k). S2–S4 are bible-cap hygiene, the same class as cycle 1's R2–R4: required, but not holding the score |
| Pacing | 8.5 | **8.5** | Unchanged. The ledger row is matched; S5 runs strap → sandal at speed; the contrast with Ch.27 and Ch.29 holds |
| Emotion | 9.0 | **9.0** | The anchor is untouched; "My boy," (l.358) goes unheard by Felix, which sharpens "You were sitting down." |
| Immersion | 9.0 | **9.0** | The greaves are correct (l.16, l.184); the stantes missi (l.350); "less forty, greaves" (l.144) |
| **FLOOR** | 8.0 | **8.0** | Characters |
| **AVERAGE** | 8.64 | **8.64** | (9.0+8.5+8.0+8.5+8.5+9.0+9.0)/7 |

**Casual Reader: 9.0** (unchanged; none of S1–S5 is visible to a casual reader). **CVI-Launch 9.4** (8.9, plus 0.5 for the anchor). **CVI-Legacy 6.8**. **Anti-AI:** 8/20, clean band. S1–S5 add no pattern, and S3 removes a small explanatory clause.

**Projected after `apply_fixes_c2.py`:** Originality 9.0 · Theme 8.5 · **Characters 8.5** · Prose 8.5 · Pacing 8.5 · Emotion 9.0 · Immersion 9.0 → **Floor 8.5 / Average 8.71**, Casual 9.0 → **PASS** at cycle 3.

Cycle 3 needs only:
1. Confirm md5 `5b980701…`.
2. Re-read l.44, l.64, l.180, l.352 and l.372 in place.
3. Re-run the gates.

The census and the bible caps above are now exhaustive, with rulings recorded, so cycle 3 is a confirmation pass.

### 6. Character-bible re-sync list (reconciled against the page AFTER `apply_fixes_c2.py`; replaces the cycle-0 and cycle-1 lists)
The bible's Ch.28 blocks are all still **WRITER DRAFT**. Finalize replaces each one from the final page. Every string below was checked against the scratch copy, md5 5b980701.

- **MARA (Ch.28 block, l.843 on):**
  - "nothing in all my time in that town had seemed so sure" → "nothing had ever seemed surer".
  - "I was standing too, without having got up." → "I was standing too." The body rebels are now the grit in the palms (l.360) and dressed before he is back (l.248).
  - "To my eye it was no wax of a man hiding anything." → "The wax looked honest to me."
  - Speech counts:
    - "And…" openers 1: "And you let him."; "And you?" is CUT, and Prima is asked "What was your answer?".
    - Statement + dry fragment **2** (l.84 "…with him," … "The sherd."; l.210 "The girl at the fullery," … "Prima."): AT CAP.
  - Memory: not "none". One triggered recall, the eyebrow (l.64, "Nobody in the house believed it, or asked him again."), picked up at l.70. The Gloria rice is unlabelled ("I thought of my cousin Gloria's…").
  - CUT: "For no reason at all", "I lay awake" (l.304), "new to me", "And you?", "a sandal from somewhere low down", "Nobody in the house had believed it, and no one asked him again.", "before he had sat", "before the dun had come to a stop".
- **VALENS (l.1707 on):**
  - "the herald has it ahead of the thraeces. Then it's Lupus's boy on the sand." → "…ahead of the thraeces, and it's Lupus's boy on the sand." It is followed by "He sat on the bed and started on his boot laces."
  - "They don't call heralds." / "Bring Lucius." are one line: "The women will know me. They don't call heralds. Bring Lucius."
  - **"Mine." → "My boy,"** said to the bean woman's **"You know that bird?"**, not "That bird … Was he anything of yours?".
  - The Albucius misreading as on the page: "He wants more. He's looked the boy over and he knows what he's got. He'll take my money once the games are over and find a reason to keep him. Or he'll put him in with someone who can kill him and sell the duumvir the blood. You heard him. The duumvir pays him for the dead." "The giver pays more for a corpse…" is CUT.
  - "That wants washing." → "Wash that."
  - First fight: "I couldn't feel my feet," he said. "Walking out to my mark." ("Not once," is CUT.)
  - Kirrha: "He's free. I said it at Kirrha, with the Cilician listening." ("there on the quay" is CUT.)
  - **Strike** "pays Grata's boy two coppers unasked" (audit CRIT-002).
  - Add: "The dun's cracked a hoof," … "Lie down."; stall to stall with the bucket; the dry knee; boots 2 (l.274, l.288 "toes to the wall").
  - Counts: hand on the boy 3 (l.32, 312, 340); seated outside the anchor 3 (l.66, 242, 274); "feet" 4 as the chapter's motif (rest in Ch.29).
- **FELIX (l.2692 on):**
  - "I never stumbled once" → "I never tripped on a word of it".
  - "Grata would." → "Course she did."
  - "Because I'm too thin to hold the board up." → "Because my arms won't hold the board up."
  - "laughed till he had to sit" → "he laughed, with the whole yard watching."
  - "Nicanor told me all that my first day." → "I had all that my first day."
  - "Never. He gave me…" → "Robbed me? He gave me what he promised. He never even asked me for a paper."
  - "Nicanor says you've not come to the sand since the bear. Not once in more than two summers." → "You've not been to the sand since the bear, Nicanor says. Two summers and more. Not even to look. Why's that?"
  - "they'd cry your name … I'd spend the whole bout" → "they'd be chanting Lupus before I was halfway to my mark … and I'd spend the bout hunting the benches for you".
  - The after-bout burst as on the page: "You saw him? Bent right over in front of me, neck out, and all of them up there begging me to take it! His ear was mine for the taking. Nicanor says I'm a fool, and I'll fight out the rest of my three years in sheep towns where they can't tell one fighter from another, and no one will cry my name in this town again." / "Somebody threw his sandal at us."
  - Kit: quilting "to the groin"; greaves "from mid-thigh to instep" / "Bronze ones, past the knee."
  - The palm ends "…and on the right two fronds, and then nothing." "Its maker had been called out…" is CUT.
  - Counts:
    - "nobody" **2** (WATCH continues); "never" 2; "everybody" 2; "whole" 2.
    - "cry… name" 2 (l.122 relayed, l.372): SPENT.
    - Single questions only ("Did she show you?" / "Robbed me?" / "Why's that?" / "You saw him?").
- **GRATA (l.3281 on):**
  - "my husband's no use on a road and my boy's no use anywhere" → "but my husband's no use on a road."
  - "he did it in the dark, I give him that" → "He left your stable mucked out, in the dark."
  - Add "He swore himself in the forum, the whole oath, and the fuller's girl was the first he told." and "the fuller's girl says he's to be a Thracian, whatever that means to her".
  - Add "She lifted Aelia out of the sling and settled her on her own shoulder." / "She was rocking Aelia, awake now and staring at her earrings."
  - The morning flood: "because the trainer had eaten a bowl of her chickpeas and said the lad would be down inside three passes".
  - **Strike** "Her boy appears (bare feet, two coppers)".
  - "no question" → one: "For you?" (l.56).
  - CUT: "hitched Aelia up her shoulder"; "had it from him first and the fountain had it from her by noon"; "had it from the trainer, who'd had…".
  - WATCH: "had it from" rested (Ch.20 l.579 its only use); "the fuller's girl" 2/2, rested; no race frame on her in Ch.28.
- **PRIMA (l.5729 on):**
  - Rhythm: "keeps treading while she talks; stops only once" → treads at the introduction (l.96), then "She stopped treading and stood in the gray water." … "She trod again, harder." (l.108), and nothing else. Do not write it as a rule.
  - Physicality: "fishes a twin's strap out of the dirt without breaking step" → "leaned across, hooked the strap out of the dirt by one end, wiped it on her hip and returned it." She still "fished inside her neckline" for the sherd.
  - On the page:
    - "dragged the stained cloth clear"
    - "I'm to marry the baker's nephew, from the Nola Gate bakery,"
    - "Same words he gave the magistrate's man. Twice, so I'd have it right."
    - "They talk of it at the vats. Nine times, and the emperor's own sword." (not "The fountain says so" or "They say so at the vats")
    - Mara's question "What was your answer?"
  - "the fountain" as gossip is hers alone in Ch.28 (l.104). "the vats" 2 in the fountain scene: rested.
- **ALBUCIUS (l.5756 on):**
  - Physicality: "a dish of eggs … rubs his fingers clean on a napkin" → "Albucius was eating eggs." / "with the shells picked off into a small white pile at his elbow" / "ate half an egg". No dish, no napkin.
  - "I'd have wagered on today." → "I'd have bet on today."
  - "Sit, the pair of you, there's the bench." → "Sit. There's the bench. You'll not mind if I eat. I've had a bear off its food since the Ides and a slave who swears it's sulking, and I was up with it till the cocks."
  - "My trainer wrote the name in for him." → "Nicanor wrote the name in for him."
  - "Once the games are done, come back. … isn't worth what one is who hasn't … what's in that cloth." → "Come back once the games are done, and bring your cloth. A tiro who's been out once and lived, the price comes down on him, and I'll sell him back cheaper than what's in it."
  - Add "Is it eating?" / "A sniff." / "Lupus, I'll tell you this because Nicanor says you're no fool."
  - "he tells me" 2: AT CAP.
- **NICANOR (l.5604 on):**
  - "Forty he's had off the lad…" → "Forty he's had off him for a pair of greaves that cost the smith thirty-five."
  - "he'll sell the lad back afterward cheaper than today" → "he'll sell him back after, cheaper than today."
  - "(chickpeas, paid)" → Grata's report: "he'd pay for them because she wasn't the duumvir".
  - "laughed till he had to sit" → "he laughed, with the whole yard watching" (Felix's report).
  - Add "He squinted at the lamp I had trimmed."
- **RUSTICUS (l.5781):**
  - The wife sells eggs "in the forum", not by the Nucerian gate.
  - "a field somewhere up the Nola road" stands (l.10).
- **LUCIUS (l.3381):** add "During the hunt he wet himself, and Valens shifted him to the dry knee." The rest matches the page.
- **AELIA (l.3448):** matches the page.
- **Walk-ons (l.4763):**
  - Bean woman: "She sells eggs in the forum."; her line to Valens is "You know that bird?".
  - Duumvir: strike "his toga very white" (the white toga is closed); the page has "gray-haired, a slave at his side holding a cup".
  - **Strike "Grata's boy"** (CRIT-002).
- **At-risk after Ch.28 (l.8009): replace the writer-draft block.**
  - SPENT corrections:
    - "Mine." → "My boy."; "That wants washing." → "Wash that."
    - the sliding groan, bare; the unfinished palm, "and then nothing.", no cause given
  - SPENT additions: "What was your answer?", "Course she did.", "Robbed me?", "chanting Lupus", "You know that bird?", the dry knee, "They talk of it at the vats.", "from all sides together", "the fuller's girl was the first he told".
  - CUT log:
    - every cycle-0 old string
    - R1–R4 old strings
    - S1–S5 old strings: "where nobody can tell one fighter from another", "Nobody in the house had believed it, and no one asked him again.", "a sandal from somewhere low down", "start on him before he had sat", "before the dun had come to a stop"
    - the rejected drafts "What did you tell him?" and "from above the knee"
    - the palm's last two sentences
  - WATCH for Ch.29:
    - race frame 1 (cap ≤1; enforce it again); narration "somewhere" 2 (cap); "Nobody had [verb]" 1 (cap)
    - Felix "nobody" 2, still on WATCH; spoken "Nobody…" openers 4 across three speakers
    - "right round" rested; "say so" 1 per speaker; "hook" 3
    - Prima "the vats" 2; "the bowl" for the arena 2 beside the hare bowl
    - Valens's "feet" 4 and "Bring [the boy…]" (Ch.27/28): rest both
- **Project rules to record:**
  - V2: a charged one-word line is never re-spoken by another character.
  - L1: an unfinished mark is never given its cause by the narrator.
  - C4: a town metonymy used as gossip belongs to one speaker per chapter.
  - R1: the speech-habit census also counts the speaker's earlier chapters.
  - **S1 (new, evaluator process): the cycle-0 census runs the bible's per-chapter lexical caps and each character's WATCH words by hand**, because `tic_report.py` does not measure them: the race frame, narration "somewhere", "Nobody had [verb]", "the one / the only", and so on. Ch.28 lost cycle 2 because cycle 0 counted only the gate, the states and the speech habits.
- **Header l.6:** body 6,549, dialogue 31.0%, revision "evaluator cycles 0–2".
- **ENTITY:** greaves to mid-thigh; quilting to the groin; Prima's source "the vats".

### PATH TO 8.5 (cycle 2)
- **Characters 8.0 → 8.5 requires:** S1, Felix's l.372 "nobody" → "they can't tell". That takes his WATCH word to 2 and is the only floor-holding item.
- **Required with it (not floor-holding):** S2 (the "Nobody had" frame), S3 ("somewhere"), and S4/S5 (the race frame, and Grata's speed clocked twice).
- Apply `apply_fixes_c2.py` and confirm md5 `5b980701f4000d3f2c7ce7d7744f4393`. Re-run `check_chapter.sh 28` and `--echoes 28`, then run cycle 3 as a confirmation pass.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
