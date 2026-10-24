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

---

## Cycle 3
**Evaluator:** book-evaluator (independent) | **Date:** 2026-10-24 | **Text:** `manuscript/chapters/chapter-28.md` md5 **`5b980701f4000d3f2c7ce7d7744f4393`**. That is exactly the tested cycle-2 result, so `apply_fixes_c2.py` was applied verbatim (commit 12765d7). Line numbers below are for this file.

**Measured on the real file:**
- `bash tools/check_chapter.sh 28`: **ALL MECHANICAL GATES CLEAN** (style with foreshadow 0, grammar, rhythm with the same one advisory paragraph, show/tell, voice-wear strict, tic gate with gestures, metaphor, **SHAPE CLEAN**).
- `--echoes 28`: **0** echoes, 0 command echoes, 0 spoken-line echoes.
- Body 6,548 (shape) / 6,549 (metaphor table); dialogue 31%; `short-punch` → `dialogue`.

### Verdict: **POLISH** (cycle 3). Floor **8.0** (Prose, corrected).
- Casual 9.0 ✓. Pacing OK ✓. Gates clean ✓.
- **S1–S5 are confirmed on the page, and Characters reaches 8.5.**
- **The final bible sweep the brief asked for found eleven items that cycles 0–2 missed.** All were on the page from cycle 0; one (X4) sits in the string my own S2 wrote. Ten of them are SPENT or CLOSED **devices** from the at-risk list, not numeric caps: a held silence filled by traffic, "and stayed" ×2, the two-item look ×2, a relayed command echo, a gaze-arrival, a spent smell, a third "than before", a third narrated "not hard", and a memory paragraph that closes on a "Nobody…" verdict.
- Cycles 1–2 scored Prose 8.5 with these on the page. That was an overscore. The book has held Prose at 8.0 for exactly this class: Ch.14 (SPENT frames), Ch.20 (R1, the same held-silence-by-traffic device) and Ch.25 (the two-item look and command echoes were continuity CRITs). **Prose is corrected to 8.0** under the V3.4 correction clause (well over 3 cited items, below).
- The fix is **12 cuts and no new words** (`apply_fixes_c3.py`, tested). **Projected after it: Floor 8.5 / Average 8.71 → PASS at cycle 4**, which is a confirmation pass only.

### 1. The five lines cycle 2 asked to re-read, in context
| Line | On the page | Ruling |
|---|---|---|
| l.44 | "Grata was round her marble and out to us as the dun came to a stop." | ✓ No race frame. Her speed is still implied (she is already there). |
| l.64 | "At midwinter there had been a split eyebrow, and Felix said the dun had thrown her head. Nobody in the house believed it, or asked him again." | ✓ for S2's purpose ("Nobody had" frame 1, pair 0). **But see X4:** the second sentence is a SPENT memory close and restores Ch.26's cut verdict. My S2 string, my miss. |
| l.180 | "I heard her start on him: he was the trainer, she could tell a trainer…" | ✓ The colon takes the reported flood cleanly. |
| l.352 | "…nut shells, crusts, a sandal that tumbled end over end and dropped on the sand between them." | ✓ Narration "somewhere" is 2 (l.10, l.30). |
| l.372 | "…in sheep towns where they can't tell one fighter from another, and no one will cry my name in this town again." | ✓ Felix's "nobody" is 2 (l.188, l.214). The "nobody…, and no one…" pair is gone. |

### 2. Scope of the final sweep (so cycle 4 has nothing left to find)
Run against md5 5b980701, by hand and by script (`scratchpad/fixes28/capcount.py`, `ngrams.py`):
1. **Every numeric per-chapter cap in `character-bible.md`.** That is all 171 lines carrying "≤ / cap / per chapter / max", plus every WATCH, for every card on the page (Mara, Valens, Felix, Grata, Lucius, Aelia, Prima, Albucius, Nicanor, Rusticus, the walk-ons) and the narration.
2. **Every SPENT / CLOSED construction in the at-risk blocks, Ch.1 through Ch.27,** read in full and checked against the page. This is the class cycles 0–2 did not run.
3. **Every quoted bible string of 4+ words grepped against the page.** Result: every hit is a Ch.28 card quote. No CUT string from any chapter is restored.
4. **Every content 3-gram repeated inside the chapter**, judged.

### 3. New findings (all present since cycle 0)
| ID | Location | Problem type | What happens now | Why it fails | Revision direction (exact, in script) | Project rule? |
|---|---|---|---|---|---|---|
| X1 | l.82 | Style (SPENT device, zero tolerance) | "Out in the street a late cart passed, its load chinking, and a dog ran after it till it lost interest." It sits between Valens's "haul him home by the ear" and Mara's "He took his name with him." | Bible: "Measuring a held silence by something moving: SPENT … **0 more anywhere.** A held silence is left bare, or ended by speech". Restated after Ch.19 and Ch.20; Ch.20's R1 cut the same carts. The dog in a silence is also kin of the SPENT "dog barking once into a silence". | Cut the paragraph. Mara's line follows Valens's directly. | No (rule exists) |
| X2a | l.242 | Style (CLOSED construction) | "Valens stooped to it and stayed stooped." | Bible: '"and stayed": 2 in Ch.15, **CLOSED for the book**.' This is the exact Ch.15 shape ("slow, and stayed slow"). | "Valens stooped to it." The hare carries the gaze. | No |
| X2b | l.246 | Style (CLOSED construction; in-chapter double) | "…stretched up as far as they reached, and stayed so until somebody came." | A second "and stayed", about 80 words after X2a. | "…stretched up as far as they reached, until somebody came." | No |
| X3 | l.370 | Style (book-wide WATCH, NO TICS) | "the beard on his jaw looked darker than before." | Bible: '"than before" 2 (Ch.25 l.218, l.382)'. A third use puts the phrase at 3 book-wide. | "…looked darker." | No |
| X4 | l.64 | Style (SPENT memory close) / Continuity (Ch.26 CUT restored as verdict) | "Nobody in the house believed it, or asked him again." | (a) A memory paragraph closing on collective not-knowing is SPENT (Ch.6's "Nobody in the building ever learned his name."), and "a memory insert ends on an action or an object". (b) Ch.26 cut the narrator's verdict on this same lie ("The dun had never thrown her head at anybody in her life, and he knew I knew it." CUT, "the lie stands uncommented"). Supersedes my S2 string. | End the paragraph at "…Felix said the dun had thrown her head." Mara's "You knew about the eyebrow," (l.70) now carries the doubt. Sentence-initial narration "Nobody" goes to 0. | No |
| X5 | l.364 | Style (SPENT image) / #3 | "Inside it was cool, with a smell of oil, sand dust and wet stone." | Bible at-risk after Ch.5: '"smelled of wet stone" … spent at its earlier use' (Ch.3 l.105, the cave: "It carried a smell of wet stone"). In a cool passage it also rebuilds the Ch.3 cave pairing. It is a #3 triad as well. | "Inside it was cool, with a smell of oil and sand dust." | No |
| X6 | l.60 | Style (in-paragraph double) | "upside down, as he kept it, so that no dust…" / "He kept it in a crack…" | "kept it" twice in three sentences, about two different objects; l.86 "he kept it" makes 3 in 26 lines. | Cut ", as he kept it". The "so that" care detail stays (it pays off at "Keep your fingers off where the hare is."). | No |
| X7 | l.298–302 | Style (SPENT device) | "Nicanor yelled at me to stamp." / "Did you?" / "I stamped. The crowd laughed." | The command echoed as compliance is SPENT at 3 book-wide since Ch.9, and "**a relayed order counts**" (Ch.20 entry). The gate cannot see it because "Did you?" sits between the order and the echo. | "The crowd laughed." This shows compliance by its result, as the bible prescribes. Valens answers sideways, in his register. | No |
| X8 | l.354 | Style (SPENT frame) | "Her eyes went across me to Valens and the boy he held." | Gaze-arrival ("Then-her-eyes-went/came…") is SPENT, restated after Ch.19, whose cut string was "Then her eyes went past the girl to us". It is the same skeleton without the "Then". | Cut the sentence. Valens answering "My boy," shows whom she asked. | No |
| X9 | l.376 | Style (CLOSED device) | "He looked past Valens's shoulder at the scratched wall, and at Valens." | Two-item looked-at-X-and-at-Y form: "CLOSED … No further use anywhere". The precedent is Ch.25 CRIT-004, which cut "looked at the plant for some while, and at Valens". | "He looked past Valens's shoulder at the scratched wall." The last line turns to his father by itself. | No |
| X10 | l.346 | Style (CLOSED device, look verb) | "He considered the benches nearest him, and the sand, and bent toward…" | The same two-item form with "considered". Ch.25 CRIT-004 also cut "watched the Chaldean's mouth…, and mine". | "He considered the benches nearest him, and bent toward…". The duumvir reads his voters. | No |
| X11 | l.334 | Style (narrator tic forming) | "cracked it on the backs of Felix's thighs, not hard, then on Rusticus's" | "[blow], not hard," is the narrator's third use (Ch.5 l.31 the kick; Ch.21 l.30 the cuff). Ch.27's spoken "Not hard" ×3 makes 6 book-wide. Bible SPENT: '"not hard," for a grip (Ch.5)'. | Cut " not hard,". "and pushed at them with it" already says goading, not punishing. | **Yes:** "not hard" CLOSED book-wide (narration and speech) |

**Why Prose and not Characters:** X1–X11 are narration devices and lexis. None is a speech habit, a narrated-state count or a census row. **Why it holds the floor:** ten of the eleven are zero-tolerance SPENT/CLOSED entries, the class the book has always scored as law (Ch.14, Ch.20, Ch.25), not over-by-one hygiene like cycle 2's S2–S5.

### 4. Class rulings (checked, not changed; recorded so cycle 4 does not re-argue them)
- **Bend/stoop, bible "cap 2 per chapter" (written after Ch.10).** Since Ch.20 the evaluations measure this class with the gate's gesture regex (Ch.22 "bend 1"), and the gate counts Ch.28 at 1. Cycle 0 ruled the class OK. By hand there are 4 across 4 people (Prima l.112, Valens l.242, Rusticus l.330 (the plot event), the duumvir l.346), none clustered. **Not re-opened.** WATCH for Ch.29: no bend beat.
- **Narrator call-out pointers (proposed cap ≤1).** l.114 "I had scratched those capitals myself, in Valens's shed below Delphi, the winter we met." is one pointer, at the proposed cap. It gives provenance the scene needs: Felix "told me it, letter by letter" lands only if Mara made the letters (Ch.11 l.434 agrees). l.16 ("I had seen thraeces on that sand before") and l.248 ("I had heard the benches roar that name") are her knowledge at work in the scene, not a rhyme being announced.
- **"Twice this year."** (Nicanor, l.240) is not the CLOSED bare "Twice." reply. It carries a qualifier and new information. Cycle 0 kept it as a strength. "twice" is 7 in the chapter across five speakers and the narration (l.10 ×2, Prima 2, Felix 1, Mara relaying 1, Nicanor 1): WATCH.
- **"had gone blue"** (l.44) is not the CLOSED "had gone (quiet|still)". Colour changes are routine on finalized pages (Ch.27 l.200, l.306). WATCH: "had gone [colour]" 3 across Ch.27–28.
- **"The man with the (long) rod"** ×3 (l.28, l.334, l.346) is under the 6+ name-him rule. l.28 and l.334 mirror on purpose: he steps back to start the bout and steps in to break the stall.
- **"Valens gave the [X]…"** ×2 (l.144 "no glance at all", l.314 "more of his attention than the sand"): the census row (attention elsewhere, 3) was ruled at cycle 0. WATCH: the skeleton is now 2/2 in Ch.28; rest it.
- **In-chapter 3-grams judged as design or texture:** "the herald cried … the benches answered" (l.10 / l.316, the S4 hinge); "a man below us" (l.30 / l.326, the S1 / S5 rhyme); "the noise came" (l.332 / l.352, two constructions); "the door below the editor's box" ×2 (role-label landmark at its ≤2 cap).
- **Sequential looks in separate sentences** (l.376 "studied the hand on his arm. He looked past … at the scratched wall") are not the item-by-item form once X9 is applied. Each look has its own function: the touch, then the palm.
- **Other caps passed:**
  - "said to the [non-listener]" / group-address tag 1 (l.12 "to the bench at large")
  - "the way [a/the]" 2 in narration; "the size of a" 1; `to the (joint)` 1 (l.16 "almost to the shoulder"; cycle 2 said 0)
  - "so that" 2; "until" 3; "considered" 2 (deliberation pauses ≤3); "slowly" 2 (narration; Fenn's cap is his)
  - Grata "men" 1 (l.306 "grown men leave a show"); Grata social touches 0
  - Nicanor's rod once, his dry exaggeration once, no "Lupus"
  - "palm" 3 (one is the graffito); "fist" 3, Lucius's 0; "patch" 2
  - "every" 12 (1.8/1k, against Ch.26's WATCH at 3.7/1k); "whole" 7 with Felix at 2
  - "the bowl" for the arena 2; "the vats" as Prima's gossip source 1; body-part rulers 2
  - paragraph-final negations 6 → 5 after X4 (0.77/1k)
- **"cool" for the tunnel** (l.364): a live door is the book's cool thing (Ch.27 canon). An arena passage is plausibly cool and no door is implied. WATCH: no other "cool" passage before Ch.30.
- **"whoever had made it"** (l.36) was ruled at cycle 1. Not re-opened.

### 5. Scores (cycle 3, the page at md5 5b980701; max +0.5 up; correction clause applied down)
| Dimension | Cycle 2 | **Cycle 3** | Evidence / cap |
|---|---|---|---|
| Originality | 9.0 | **9.0** | The seated champion (l.336–338); the strap-tying mercy (l.330–332); "A sniff, he tells me. Two hundred sesterces of bear." (l.156) |
| Theme | 8.5 | **8.5** | Recedes by design; carried by acts ("I'd be one more pair of feet on that sand. I'll watch.", l.290). Not 9.0: "haul him home by the ear" (l.80) is stated outright |
| Characters | 8.0 | **8.5** (+0.5) | S1 confirmed: Felix's "nobody" 2. The census is clean and no speech habit is over 2 (Felix's doubled phrases 2, l.196 and l.222; Albucius's "he tells me" 2; Prima's "never" 2). The spoken reuses are gone. Nameable-rule test passes for every card. No X item is a character item |
| Prose & Voice | 8.5 | **8.0** (corrected −0.5) | Stopping sentences stand: l.10 "…and nobody caught it."; l.304, the bowl nudged "a fingernail's breadth"; l.336–338. Ugly sentence l.86. **Held by X1, X2a/b, X7, X8, X9, X10** (zero-tolerance SPENT/CLOSED devices) **and X3, X4, X5, X11**. Cycles 1–2 scored past them |
| Pacing | 8.5 | **8.5** | Unchanged. The ledger row is matched; S5 runs strap → sandal at speed; the contrast with Ch.27 and Ch.29 holds. X1 removes a beat inside the night talk, which tightens it |
| Emotion | 9.0 | **9.0** | The anchor is untouched (l.336–340). X9 lets "You were sitting down." arrive without his eyes being steered back to his father first |
| Immersion | 9.0 | **9.0** | The greaves (l.16, l.184); the stantes missi (l.350); "less forty, greaves" (l.144) |
| **FLOOR** | 8.0 | **8.0** | Prose |
| **AVERAGE** | 8.64 | **8.64** | (9.0+8.5+8.5+8.0+8.5+9.0+9.0)/7 |

**Casual Reader: 9.0.** Unchanged; no X item is visible to a casual reader. **CVI-Launch 9.4** (8.9, plus 0.5 for the anchor). **CVI-Legacy 6.8**. **Anti-AI:** 8/20, clean band. X5 takes #3 to 3 instances (l.22, l.136, l.352), and #11 stays at 3.

### 6. Fix script (tested)
`/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes28/apply_fixes_c3.py <chapter-28.md>`. It makes **12 replacements** (X1, X2a, X2b, X3–X11). **All are cuts**, so no new string enters the book.
- It refuses any input whose md5 is not `5b980701…`.
- Each replacement must match exactly once, or nothing is written.
- A re-run aborts safely (tested).

Tested on the scratch copy `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/eval28/books/the-hour-of-ash/` (Ch.1–27 byte-identical to the repo; repo `tools/`):
- `check_chapter.sh 28`: **ALL MECHANICAL GATES CLEAN**. Tic gate clean, voice-wear strict clean, **SHAPE CLEAN**. The rhythm advisory is the same single paragraph.
- `--echoes 28`: **0** echoes, 0 command echoes, 0 spoken-line echoes.
- Body **6,481** (shape) / 6,482 (metaphor table); dialogue **31%** (31.3% show/tell). `short-punch` → `dialogue` unchanged.
- **Counts after the script:**
  - "and stayed" 0; "than before" 0 in Ch.28 (book 2/2); narration "somewhere" 2; "Nobody had [verb]" 1 (l.134); sentence-initial narration "Nobody" 0
  - two-item looks 0; gaze-arrivals 0; command echoes 0; held silences filled by motion 0; narrated "not hard" 0
  - "kept" in narration 7, with "kept it" ×2 in different paragraphs; race frame 1 (l.354)
- **Replacement strings checked** (cuts only): each surviving join ("Valens stooped to it.", "until somebody came", "a smell of oil and sand dust", "looked darker.", "The crowd laughed.") occurs nowhere in Ch.1–27 or the voice-bank.
- The opener, the anchor (l.336–340), the palm, the last line and every cycle-0/1/2 replacement are untouched. The exception is S2's string, which X4 deliberately cuts.
- Result md5: **`4aca9f902c36ea683f80225e7f2e1b8f`**.

### 7. Character-bible re-sync list: corrections to the cycle-2 list (§6 above), reconciled against the page AFTER `apply_fixes_c3.py` (md5 4aca9f90)
The cycle-2 list stands, with these changes:
- **MARA:**
  - Memory, one triggered recall: "At midwinter there had been a split eyebrow, and Felix said the dun had thrown her head." (l.64), picked up at l.70. Replace cycle 2's quote of l.64.
  - Add to CUT: "Nobody in the house believed it, or asked him again." (S2's string); "Out in the street a late cart passed, its load chinking, and a dog ran after it till it lost interest."; "as he kept it"; "with a smell of oil, sand dust and wet stone"; "not hard," (the rod); "and the sand" (the duumvir); "Her eyes went across me to Valens and the boy he held."; "and at Valens" (the tunnel); "darker than before".
- **VALENS:**
  - First fight: "I couldn't feel my feet," he said. "Walking out to my mark. I looked down to see were they still on me. Nicanor yelled at me to stamp." / "Did you?" / "The crowd laughed." … "After, I had them back." Add "I stamped." to CUT.
  - At the bowl: "Valens stooped to it." Add "and stayed stooped" to CUT.
- **FELIX:** the tunnel: "Felix studied the hand on his arm. He looked past Valens's shoulder at the scratched wall." Beard: "looked darker".
- **LUCIUS:** the threshold fall: "the bowl kept off the stone by his two arms stretched up as far as they reached, until somebody came." Add "and stayed so" to CUT.
- **Walk-ons:**
  - Bean woman: "You know that bird?" she said. There is no gaze sentence before it.
  - Duumvir: "He considered the benches nearest him, and bent toward the man at his elbow."
  - The rod man: "cracked it on the backs of Felix's thighs, then on Rusticus's".
- **At-risk after Ch.28:**
  - SPENT: the north tunnel "cool, with a smell of oil and sand dust"; Valens's first fight now has "stamp" as the order only.
  - CUT log: add the X1–X11 old strings above.
  - WATCH for Ch.29:
    - no bend beat
    - "had gone [colour]" 3 across Ch.27–28
    - "Valens gave the [X]…" skeleton 2/2
    - "twice" 7
    - "than before" 2/2 book-wide, SPENT
    - "cool" passages before Ch.30
    - narrator pointer at 1 (l.114)
- **Project rules to record:**
  - X11: "not hard" CLOSED book-wide (narration and speech).
  - **Evaluator process (extends cycle 2's S1):** the cycle-0 bible sweep reads the at-risk SPENT/CLOSED constructions in full, not only the numeric caps. Ch.28 lost cycle 3 to ten zero-tolerance devices nobody grepped for.
  - **Gate proposal (UPDATE RULE, root `tools/tic_report.py`):**
    - `\band stayed\b` (CLOSED)
    - the two-item look `\b(looked|watched|considered|studied)\b[^.]{0,80}, and (at )?(the |\w+'s )?\w+\.`
    - a one-sentence narration paragraph between two quotes whose subject moves (cart / dog / shadow / drip)
    - a relayed order ("told / yelled at / bid [me] to X") followed within 3 lines by "I X-ed"
- **Header l.6:** body 6,481, dialogue 31%, revision "evaluator cycles 0–3".
- **ENTITY:** no change from cycle 2's list.

### PATH TO 8.5 (cycle 3)
- **Prose 8.0 → 8.5 requires:** the page free of SPENT/CLOSED devices.
  - Apply `apply_fixes_c3.py` (X1–X11, cuts only) and confirm md5 `4aca9f902c36ea683f80225e7f2e1b8f`.
  - Re-run `check_chapter.sh 28` and `--echoes 28`.
- **Cycle 4 is a confirmation pass:**
  1. Confirm the md5.
  2. Re-read l.60, 64, 80–84, 242–246, 300, 332, 344, 352–354, 362, 368 and 374 in place (post-fix numbering).
  3. Re-run the gates.
- The sweep in §2 is exhaustive and its rulings are recorded in §4. Nothing outside X1–X11 is open.
- **Projected after the script:**

| Dimension | Projected |
|---|---|
| Originality | 9.0 |
| Theme | 8.5 |
| Characters | 8.5 |
| Prose | 8.5 |
| Pacing | 8.5 |
| Emotion | 9.0 |
| Immersion | 9.0 |

That gives **Floor 8.5 / Average 8.71**, Casual 9.0 → **PASS**.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

---

## Cycle 4
**Evaluator:** book-evaluator (independent) | **Date:** 2026-10-24 | **Text:** `manuscript/chapters/chapter-28.md` md5 **`4aca9f902c36ea683f80225e7f2e1b8f`** ✓. This is exactly the tested cycle-3 result, so `apply_fixes_c3.py` (12 cuts) was applied verbatim (commit df98174). This is a confirmation pass, scoped as cycle 3 prescribed: the §2 sweep is binding, and only a defect created BY a cycle-3 cut may be raised. **None was found.**

**Measured on the real file (book folder):**
- `bash tools/check_chapter.sh 28`: exit 0, **ALL MECHANICAL GATES CLEAN**. That covers style (foreshadow 0), grammar (0 errors), rhythm, show/tell, voice-wear strict, the tic gate with gestures, the echo scan, the **new step 5d CLOSED LEDGER** ("clean, 5 closed constructions checked"), metaphor and **SHAPE CLEAN**.
  - Rhythm: the advisory is the same single paragraph as in cycles 1–3 (l.62, Lucius on the clean patch).
  - Gesture: "jaw ×2" is still the cycle-0 false positive. Both hits are the beard (l.168, l.368).
- `python3 tools/tic_report.py --echoes 28`: **0** echoes, 0 command echoes, 0 spoken-line echoes.
- Body **6,481** (shape) / 6,482 (metaphor table). Dialogue **31%** (31.3% show/tell). 4 breaks. Median sentence 11. 8 similes. Em-dash 0. And-chains 3. Opens `short-punch` ("The crowd roared for the wrong man.") and closes `dialogue`, which matches ledger row 28.
- One note: the cycle-3 re-read list gave "l.242–246". On this file the two "and stayed" sites are **l.240 and l.244**. That is my numbering slip. The other numbers are right.

### 1. The twelve cuts, re-read in place
| Cut | Line now | On the page | Ruling |
|---|---|---|---|
| X6 | l.60 | "The hare bowl sat high up, upside down, so that no dust could settle where the hare ran. The sherd with his name on it was gone. He kept it in a crack behind the shelving…" | ✓ Grammatical. "so that" still carries Felix's care. "He kept it" now has one referent, the sherd in the sentence before. No new double: "kept it" is 2, in different paragraphs (l.60, l.84), as cycle 3 ruled. |
| X4 | l.64 | "At midwinter there had been a split eyebrow, and Felix said the dun had thrown her head." | ✓ The insert is a single sentence and closes on Felix's lie, an action. It is triggered by the empty corner and returns to the scene at l.66. "You knew about the eyebrow," (l.70) carries the doubt, so the lie stands uncommented, as Ch.26 ruled. The eyebrow is clearly Felix's. |
| X1 | l.80–84 | "…haul him home by the ear." / "He took his name with him," I said. "The sherd." / Valens rolled toward the curtain… | ✓ Mara's line now answers Valens's directly. It reads as her evasion, and the exchange is tighter. The silence after it is left bare ("If he had an answer, he kept it."), as the bible prescribes. No orphaned referent. |
| X2a | l.240 | "Lucius came to his father's knee and tipped the bowl up for him to see the hare. Valens stooped to it. Painted in brown slip, the hare ran…" | ✓ "it" = the bowl. The hare sentence takes the gaze. |
| X2b | l.244 | "…went down flat, the bowl kept off the stone by his two arms stretched up as far as they reached, until somebody came." | ✓ "until" reads naturally on the held arms. The duration is kept without the closed frame. "until" is still 3 in the chapter (l.244, l.350, l.362), as ruled. |
| X7 | l.296–300 | "…Nicanor yelled at me to stamp." / "Did you?" / "The crowd laughed." He shifted his head on the bolster. "After, I had them back." | ✓ Valens answers sideways, and the compliance is shown by its result. This is his register, and it is the best Valens line in the night talk now. "laughed" is still 3 across three laughers (l.30, l.190, l.300), unchanged by the cut. |
| X11 | l.332 | "…cracked it on the backs of Felix's thighs, then on Rusticus's, and pushed at them with it." | ✓ Clean. "and pushed at them with it" still reads as goading. |
| X10 | l.344 | "The duumvir sat there in the shade of the canvas, gray-haired, a slave at his side holding a cup. He considered the benches nearest him, and bent toward the man at his elbow." | ✓ "He" resolves to the duumvir, the sentence subject, exactly as before the cut. The single comma before the second predicate is the book's own rhythm and pre-dates the cut. |
| X8 | l.352–356 | "Beside me the bean woman sat and began gathering up her beans." / "You know that bird?" she said. / "My boy," said Valens. | ✓ Without the gaze line she speaks beside Mara, and Valens answers across her. That is truer to him: he claims the boy before Mara can. Who is asked stays clear. |
| X5 | l.362 | "Inside it was cool, with a smell of oil and sand dust." | ✓ No triad and no wet stone. "smell" is 3 in the chapter, about three different things (l.94, l.306, l.362). |
| X3 | l.368 | "His hair was black with sweat and plastered flat, and the beard on his jaw looked darker." | ✓ The comparative now borrows its ground from the sweat in the same sentence. No orphaned "than". The closed ledger regex `\bthan before\b` is clean. |
| X9 | l.374–376 | "Felix studied the hand on his arm. He looked past Valens's shoulder at the scratched wall." / "When they were all up shouting, I looked for you," | ✓ The look lands on the wall where the palm is, and the line turns to his father by itself. "looked … looked" across the paragraph break was already on the page before the cut and was ruled under §4 (sequential looks). The cut created no new pair. |

**Defects created by the cuts: 0.** No fix script is issued for cycle 4.

**Whole-page reconciliation:** every quoted "on the page" string in the cycle-2 §6 list and cycle-3 §7 corrections was grepped against this file, 79 strings in all. Each occurs exactly once. "in the forum" occurs 3 times, all different speakers and contexts, as ruled. Every CUT string from cycles 0–3 occurs 0 times, 22 strings in all, including "Mine.", "And you?", "and stayed", "than before", "not hard", "wet stone", "Her eyes went", "I stamped", "late cart", "as he kept it" and "believed it".

### 2. Scores (cycle 4, the page at md5 4aca9f90; max +0.5 vs cycle 3)
| Dimension | Cycle 3 | **Cycle 4** | Evidence / cap |
|---|---|---|---|
| Originality | 9.0 | **9.0** | The seated champion (l.334–336); the strap-tying mercy (l.328–330); "A sniff, he tells me. Two hundred sesterces of bear." (l.154) |
| Theme | 8.5 | **8.5** | Recedes by design. Carried by acts: "I'd be one more pair of feet on that sand. I'll watch." (l.288). Not 9.0: "haul him home by the ear" (l.80) is stated |
| Characters | 8.5 | **8.5** | The census and the speech-habit counts are unchanged and clean. X7 and X8 sharpen Valens: he answers sideways (l.300) and claims the boy first (l.356). Nameable-rule test passes for every card |
| Prose & Voice | 8.0 | **8.5** (+0.5) | **X1–X11 confirmed gone.** The page carries no SPENT/CLOSED device: 5d ledger clean, plus the hand sweep of the held-silence and relayed-order classes the ledger cannot see. Stopping sentences: l.10 "…into the noon, and nobody caught it."; l.302 "a fingernail's breadth. The humming stopped. He slept on."; l.334–336 "every soul but one was up. / Valens sat." Ugly sentence l.84 "I slept some and not much and then it was morning." Voice under pressure l.346–350. #11 at 3 (0.46/1k). Not 9.0: the backfill (S2–S3) is measured, not stopping |
| Pacing | 8.5 | **8.5** | Ledger matched, and the contrast with Ch.27 and Ch.29 holds. X1 tightens the night talk. Not 9.0: the ~4,400-word hold on the bout |
| Emotion | 9.0 | **9.0** | The anchor is intact (l.334–338). The last line lands with no steered gaze (l.374–376). Body rebel: grit in her palms (l.358) |
| Immersion | 9.0 | **9.0** | The greaves (l.16, l.182); stantes missi (l.348); "less forty, greaves" (l.142) |
| **FLOOR** | 8.0 | **8.5** | |
| **AVERAGE** | 8.64 | **8.71** | (9.0 + 8.5 + 8.5 + 8.5 + 8.5 + 9.0 + 9.0) / 7 |

- **Casual Reader: 9.0.** Unchanged: a boy alone on the sand, a father who will not stand, and a last line that hurts.
- **CVI-Launch: 9.4** (8.9, plus 0.5 for the anchor). **CVI-Legacy: 6.8.** Divergence 0.9, no alert.
- **Anti-AI:** 8/20, clean band for commercial fiction. #3 stays at 3 instances (l.22, l.136, l.350) now that the X5 triad is gone. #11 at 3.
- **Tomorrow Test:** ANCHOR EXISTS, IMAGE: the one seated man in a standing bowl, the boy on his knee. **QUOTE:** "You were sitting down."

### 3. VERDICT: **PASS** (cycle 4)
- Floor **8.5** ≥ 8.5 ✓
- Casual **9.0** ≥ 8.5 ✓
- PACING OK ✓
- Mechanical gates clean, including 5d ✓

The chapter is final at md5 `4aca9f902c36ea683f80225e7f2e1b8f`. Finalize changes only the l.6 header and the bookkeeping below.

### 4. FINAL consolidated character-bible re-sync list (reconciled against the page at md5 4aca9f90; supersedes the cycle-0/1/2 lists and the cycle-3 corrections)
All Ch.28 blocks are still **WRITER DRAFT**. Finalize replaces each one from the page. Line numbers below are this file's.

**MARA**
- "nothing had ever seemed surer" (l.246); "I was standing too." (l.334); "The wax looked honest to me." (l.142).
- Speech:
  - "And…" openers 1: "And you let him." (l.78).
  - Prima is asked "What was your answer?" (l.122).
  - Statement + dry fragment **2, AT CAP**: "He took his name with him," I said. "The sherd." (l.82); "The girl at the fullery," I said. "Prima." (l.208).
- Memory, one triggered recall: "At midwinter there had been a split eyebrow, and Felix said the dun had thrown her head." (l.64). It is picked up by "You knew about the eyebrow," (l.70). The lie stands uncommented. The Gloria rice is unlabelled (l.306).
- Body rebels: grit printed in both palms (l.358); dressed before he is back from the stable (l.246).
- CUT: "For no reason at all"; "I lay awake" (night before); "new to me"; "And you?"; "a sandal from somewhere low down"; "Nobody in the house had believed it, and no one asked him again."; "Nobody in the house believed it, or asked him again."; "before he had sat"; "before the dun had come to a stop"; "Out in the street a late cart passed, its load chinking, and a dog ran after it till it lost interest."; "as he kept it"; "with a smell of oil, sand dust and wet stone"; "not hard," (the rod); "and the sand" (the duumvir); "Her eyes went across me to Valens and the boy he held."; "and at Valens" (the tunnel); "darker than before"; "I was standing too, without having got up."; "To my eye it was no wax of a man hiding anything."; "nothing in all my time in that town had seemed so sure".

**VALENS**
- "…ahead of the thraeces, and it's Lupus's boy on the sand." He sat on the bed and started on his boot laces. (l.272)
- "The women will know me. They don't call heralds. Bring Lucius." (l.276)
- **"My boy," said Valens.** (l.356), answering the bean woman's "You know that bird?" (l.354). "Mine." is CUT.
- The Albucius misreading as on the page: "He wants more. He's looked the boy over … The duumvir pays him for the dead." (l.160). "The giver pays more for a corpse…" is CUT.
- "Wash that." (l.372). "That wants washing." is CUT.
- First fight (l.296–300): "I couldn't feel my feet," he said. "Walking out to my mark. I looked down to see were they still on me. Nicanor yelled at me to stamp." / "Did you?" / "The crowd laughed." … "After, I had them back." CUT: "Not once,"; "I stamped.".
- Kirrha: "He's free. I said it at Kirrha, with the Cilician listening." (l.80). "there on the quay" is CUT.
- At the bowl: "Valens stooped to it." (l.240). "and stayed stooped" is CUT.
- Add: "The dun's cracked a hoof," … "Lie down." (l.248); stall to stall with the bucket (l.58); the dry knee (l.312); boots 2 (l.272 laces, l.286 "toes to the wall").
- **Strike** "pays Grata's boy two coppers unasked" (CRIT-002).
- Counts:
  - hand/arm on the boy 3 (l.32, l.310, l.338)
  - seated outside the anchor 3 (l.66, l.240, l.272)
  - attention elsewhere 3 (l.142, l.312, l.338)
  - "feet" 4 as the chapter's motif (rest in Ch.29)
  - "Valens gave the [X]…" 2/2 (l.142, l.312): rest

**FELIX**
- Oath: "I never tripped on a word of it" (l.170). "Course she did." (l.174). "Because my arms won't hold the board up." (l.194). "…he laughed, with the whole yard watching." (l.190). "I had all that my first day." (l.200).
- "Robbed me? He gave me what he promised. He never even asked me for a paper." (l.216)
- "You've not been to the sand since the bear, Nicanor says. Two summers and more. Not even to look. Why's that?" (l.216)
- "…they'd be chanting Lupus before I was halfway to my mark … and I'd spend the bout hunting the benches for you" (l.224)
- The after-bout burst as on the page (l.370), ending "…in sheep towns where they can't tell one fighter from another, and no one will cry my name in this town again." / "Somebody threw his sandal at us."
- The tunnel (l.374): "Felix studied the hand on his arm. He looked past Valens's shoulder at the scratched wall."
- Beard: "the beard on his jaw looked darker" (l.368).
- Kit (l.16, l.182): quilting "to the groin"; greaves "from mid-thigh to instep" / "Bronze ones, past the knee."
- The palm (l.366) ends "…and on the right two fronds, and then nothing." No cause is given. "Its maker had been called out…" is CUT.
- Counts:
  - "nobody" 2 (WATCH continues); "never" 2; "everybody" 2; "whole" 2
  - "cry/cried… name" 2 (l.120 relayed by Prima, l.370): SPENT
  - Single questions only ("Did she show you?" / "Robbed me?" / "Why's that?" / "You saw him?")
- CUT: "where nobody can tell one fighter from another"; "darker than before"; "and at Valens"; the cycle-0/1 old strings in the cycle-2 list.

**GRATA**
- "but my husband's no use on a road." / "He left your stable mucked out, in the dark." / "He swore himself in the forum, the whole oath, and the fuller's girl was the first he told." / "the fuller's girl says he's to be a Thracian, whatever that means to her" / "She lifted Aelia out of the sling and settled her on her own shoulder." (all l.46)
- "She was rocking Aelia, awake now and staring at her earrings." (l.52)
- One question: "For you?" (l.56).
- The morning flood (l.304): "…because the trainer had eaten a bowl of her chickpeas and said the lad would be down inside three passes…"
- The arrival (l.44): "out to us as the dun came to a stop". No race frame on her.
- **Strike** "Her boy appears (bare feet, two coppers)".
- CUT: "hitched Aelia up her shoulder"; "had it from him first and the fountain had it from her by noon"; "had it from the trainer, who'd had…"; "before the dun had come to a stop"; "before he had sat".
- WATCH: "had it from" rested; "the fuller's girl" 2/2, rested.

**PRIMA**
- Rhythm: treads at the introduction, then "She stopped treading and stood in the gray water." … "She trod again, harder." (l.106), and nothing else. Do not write it as a rule.
- Physicality: "hooked the strap out of the dirt by one end, wiped it on her hip and returned it" (l.118); "fished inside her neckline" for the sherd (l.112); "dragged the stained cloth clear" (l.126).
- Speech:
  - "Same words he gave the magistrate's man. Twice, so I'd have it right." (l.106)
  - "I'm to marry the baker's nephew, from the Nola Gate bakery," (l.120)
  - "They talk of it at the vats. Nine times, and the emperor's own sword." (l.256)
- In the arena (l.334): palm pressed to her tunic where the sherd lay, mouth closed.
- "the fountain" as gossip is hers alone in Ch.28. "the vats" 2: rested.

**ALBUCIUS**
- "Albucius was eating eggs." / "with the shells picked off into a small white pile at his elbow" (l.134); "ate half an egg" (l.146). No dish, no napkin.
- "I'd have bet on today." / "Sit. There's the bench. You'll not mind if I eat. I've had a bear off its food since the Ides and a slave who swears it's sulking, and I was up with it till the cocks." (l.136)
- "Nicanor wrote the name in for him." (l.140)
- "Come back once the games are done, and bring your cloth. A tiro who's been out once and lived, the price comes down on him, and I'll sell him back cheaper than what's in it." (l.146)
- "Is it eating?" (l.150); "A sniff." / "Lupus, I'll tell you this because Nicanor says you're no fool." (l.154)
- "he tells me" 2: AT CAP.

**NICANOR**
- "Forty he's had off him for a pair of greaves that cost the smith thirty-five." / "he'll sell him back after, cheaper than today." (l.230)
- "He squinted at the lamp I had trimmed." (l.234); "Twice this year." with the rod tap on the lintel (l.238).
- Through Grata: "he'd pay for them because she wasn't the duumvir" (l.178). Through Felix: "he laughed, with the whole yard watching" (l.190). Through Valens's memory: "Nicanor yelled at me to stamp." (l.296, the order only).
- Rod once, dry exaggeration once, no "Lupus".

**RUSTICUS:** his wife sells eggs "in the forum" (l.12); "a field somewhere up the Nola road" (l.10); the greave tie (l.328).

**LUCIUS:** add "During the hunt he wet himself, and Valens shifted him to the dry knee." (l.312). Also the threshold fall: "the bowl kept off the stone by his two arms stretched up as far as they reached, until somebody came." (l.244). "and stayed so" is CUT.

**AELIA:** matches the page.

**Walk-ons**
- Bean woman: "She sells eggs in the forum." (l.12). She asks "You know that bird?" (l.354) with no gaze sentence before it, and chants "at her husband's niece's husband" (l.334).
- Duumvir (l.344): "gray-haired, a slave at his side holding a cup"; "He considered the benches nearest him, and bent toward the man at his elbow." Strike "his toga very white".
- The rod man (l.332): "cracked it on the backs of Felix's thighs, then on Rusticus's, and pushed at them with it."
- The tunnel porter, the Gaul with the net, the slow-eating boy (l.362).
- **Strike "Grata's boy"** (CRIT-002).

**At-risk after Ch.28: replace the writer-draft block**
- SPENT:
  - "My boy." (Valens); "Wash that."
  - "What was your answer?"; "Course she did."; "Robbed me?"; "chanting Lupus"; "You know that bird?"
  - the dry knee
  - "They talk of it at the vats."
  - "from all sides together"
  - "the fuller's girl was the first he told"
  - the sliding groan, bare
  - the unfinished palm ("and then nothing.", no cause)
  - the north tunnel "cool, with a smell of oil and sand dust"
  - Valens's first fight: "stamp" as the order only, answered by "The crowd laughed."
  - "cry/cried… name" (Felix)
  - "than before" 2/2 book-wide
- CUT log: every cycle-0 old string; R1–R4; S1–S5; X1–X11 old strings (as listed under MARA / VALENS / FELIX / LUCIUS above); the rejected drafts "What did you tell him?" and "from above the knee"; the palm's last two sentences.
- WATCH for Ch.29:
  - race frame 1 (cap ≤1); narration "somewhere" 2 (cap); "Nobody had [verb]" 1 (l.132, cap); sentence-initial narration "Nobody" 0
  - Felix "nobody" 2; spoken "Nobody…" openers across three speakers
  - "right round" rested; "say so" 1 per speaker; "hook" 3
  - Prima "the vats" 2; "the bowl" for the arena 2 beside the hare bowl
  - Valens's "feet" 4 and "Bring [the boy…]" (Ch.27/28): rest both
  - no bend beat; "had gone [colour]" 3 across Ch.27–28; "Valens gave the [X]…" 2/2
  - "twice" 7; "cool" passages before Ch.30; narrator pointer at 1 (l.114)
  - "kept it" 2 (l.60, l.84); "laughed" 3

**Project rules to record**
- V2: a charged one-word line is never re-spoken by another character.
- L1: an unfinished mark is never given its cause by the narrator.
- C4: a town metonymy used as gossip belongs to one speaker per chapter.
- R1: the speech-habit census also counts the speaker's earlier chapters.
- S1: the cycle-0 census runs the bible's per-chapter lexical caps and WATCH words by hand.
- X11: "not hard" CLOSED book-wide (narration and speech). It is already in `closed_ledger.tsv`.
- Evaluator process: the cycle-0 sweep reads the at-risk SPENT/CLOSED constructions in full.
  - `closed_check.py` (step 5d, commit fb4452f) now mechanises "and stayed", the two-item look, the eyes-arriving beat, the wet-stone smell, "than before" and "not hard,".
  - **Still unmechanised:** (a) a one-sentence narration paragraph between two quotes whose subject moves (the held-silence-by-motion device, X1); (b) a relayed order followed within ~3 lines by its "I X-ed" compliance (X7).
  - Also: the ledger's two-item-look regex requires "looked at X, and at Y". It would not have caught X10 ("considered the benches nearest him, and the sand,") or X9 ("looked past … at the wall, and at Valens"). Widen it at the root when next touched.

**ENTITY:** greaves to mid-thigh; quilting to the groin; Prima's source "the vats". No change from the cycle-2 list.

**Header l.6, the exact replacement line:**
```
<!-- Word count: shape 6,481 / body 6,482 | Revision: evaluator cycles 0–4 (PASS at cycle 4; continuity repair + C/I/R/S/X fix sets) | Issues addressed: 7 CRIT + 18 WARN + 3 INFO (continuity) + evaluator cycles 0–3 | Date: 2026-10-24 | Dialogue 31% (show/tell 31.3%, band 25-35) | Breaks 4 | Median sentence 11 (gear low) | Opens short-punch ('The crowd roared for the wrong man.'), closes dialogue (Felix: 'You were sitting down.') | Em-dash 0 | And-chains 3 | Echoes 0 | check_chapter.sh 28 ALL MECHANICAL GATES CLEAN (incl. 5d closed ledger) | Anchor: Valens in the top ring, Lucius on his knee, the one man sitting while the whole bowl stands -->
```
(Editing l.6 changes the file's md5. The body text stays at the evaluated md5 4aca9f90 apart from that comment line.)

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
