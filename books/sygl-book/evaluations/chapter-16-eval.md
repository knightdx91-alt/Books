# Evaluation: Chapter 16 — Whitehaven Road
**Evaluator:** book-evaluator | **Date:** 2026-10-20
**Text evaluated:** `manuscript/chapter-16.md` (4,816 words of prose). Target 4,800 (range 4,400–5,200). On spec.
**Read first:** STATE.yaml (decisions, incl. the Ch.21 heart-ring payoff), CLAUDE.md, project/STYLE_CONSTRAINTS.md, project/foundation.md (Magic ledger), character-bible.md (Verin, the librarian, Hopper, Heath, Lora, Viridia, Ms. Summers), outline Ch.16, chapter-15.md, chapter-14.md (L148), chapter-01.md (the hall), Sygl_Complete.txt L715–745, evaluations/chapter-15-eval.md.

## HEADLINE
**CVI-Launch:** 9.1 (8.6 + 0.5 strong anchor) | **CVI-Legacy:** 6.3 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.3
**Engagement Type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence Alert:** CVI-Launch 9.1 vs Floor 7.5 (1.6 gap, under 2.0): the commercial pull is strong; the floor is mechanical (gesture caps + one continuity error).

**VERDICT: POLISH.** On merit this is an 8.5 chapter, and the best action chapter so far. The fight is lived from inside Bal's circling ("Bal circled. Parry. Stab. Parry."). It is justified and not gory: the deaths happen off-centre ("he did not get up", "The screaming stopped"). There is no self-dread. Pain tolerance is canon ("He had always been able to take a lot of hurt"). Amelia holding herself back is the anchor, and "I feel useless" is answered warmly, close to the author's words. Every source beat L715–745 is present and in order. Amelia's "I do not like this" / "He is already hurt", which happen in Viridia's POV in the source, are moved into Viridia's firewood report. That keeps the POV on Bal and keeps both lines. The floor sits at 7.5 for four reasons:
1. **A continuity error.** Verin, the escort mage from Ch.5–6, turns up in the school library (L14).
2. **Gesture clusters** that cap Characters at 7.5: look-beats 6 in about 400 words around the log; three sitting clusters; Amelia's perch-and-swinging-foot carried straight on from Ch.15; a blush class that recurs across chapters.
3. **The heart ring.** The writer's "not his to take" (L248) is an invented motive, and it contradicts the looting on the same page. The closing thought (L360) works out the paired ring stopping. That takes the Ch.21 realization early, against the source's "he didn't know why", and closes a warm chapter on a note of dread.
4. **The anchor image repeats Ch.14.** In both, Amelia goes so still that nothing on her stirs.

Every fix below is a cut or a word swap. None adds plot. With F1–F13 applied the chapter projects to **Floor 8.5 / Casual 8.5: PASS.**

## Gate tools (scratch copy, Ch.1–16 at `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/ev16/manuscript/chapters/`)
- `voice_wear_check.py`: **clean** (no retired phrases, no device over cap; the one self-repetition is reported as WARN and is not strict).
- `tic_report.py --gate`: **clean**. Ch.16 has no gesture classes in the tool's table and no auto-recurrence; and-chains 2 (cap 9), negation pivots 0.
- `style_check.py --dir manuscript`: **clean** (simile 2.7/1k, em dash 0, no new distinctive repeated phrase).
- `grammar_check.py --file chapter-16.md`: 0 errors.
- The gesture clusters below are judgement calls on classes the tool does not classify (look, sit/perch, foot-swing, blush, stillness).

## Source fidelity (L715–745)
Every outline beat is present, in order: the week of homework (L8–10) ✓; Amelia nervous and both girls saying "part of the team" (L20–32) ✓; Zoran lending weapons (L34–40) ✓; Lora's own never-dulling rapier from her father after the tournament (L52–56) ✓; "I am my own weapon…" (L62) ✓; Ms. Summers told, her usual escort team (L66–72) ✓, and "Mind the river" matches the source's L748 ("on the bank of the river"; Lora's pocket notes) ✓; twenty miles, Whitehaven, the pass, the ley line (L14, L78) ✓; meat pies, "four maybe five hours", paying for themselves (L80–90) ✓; the collar at the town limit (L92–96) ✓; Hopper ranging, the sick raven (L98) ✓; growl, porcupine bristles, seven men, the pitted chain shirt with dried blood, two crossbows (L104–112) ✓; "Your weapons, if you please" (L114) ✓; the silver ring, the whispered plan, Terra worry, Kenmei's domain, weapons hiding palms (L118–128) ✓; ground shakes, bolt off Hopper, scream (L134–140) ✓; rapier strategy (L144–146) ✓; Viridia and the axeman, Hopper saves her (L148) ✓; Lora's three (L152) ✓; stumble, then the back gash, then Lora's offer, then the forearm cut (L154–164; same causal order as the source) ✓; "Do not interfere" (L166) ✓; the threat (L172) ✓; the girls' worried faces (L176–178) ✓; high jab and slash, knees, rapier through the right knee (L182) ✓; Hopper finishes it (L190–192) ✓; shirt off, the hole to sew (L198) ✓; Lora pushes him onto the fallen tree, salve and bandage (L200–204) ✓; "hardest thing", "Thank you for not jumping in… You too Lora", "I have to be able to protect myself… proud", "I'd much rather I got hurt", "you did good" (L210–232) ✓; the heart ring and its mechanics, too expensive for a bandit (L238–246) ✓; camp two miles on, the buried fire pit found by Amelia (L254–258) ✓; firewood, "didn't expect we'd fight so soon", "menace", "heart attack", "muttering about mistakes" (L262–278) ✓; the fight felt long, he'd rather be hurt, lucky about the crossbows (L280–282) ✓; the paired bedrolls (L288–290) ✓; bread, jerky, cheese (L292) ✓; arrow-repelling shirts, one charge per rune (L296–300) ✓; Lora's drill, patient (L304–308) ✓; the walk, "I feel useless", Bal's answer kept near-verbatim (L318–342) ✓; Hopper on guard, chuff, her hand (L350–362) ✓.

**The heart ring against the source.** The source says only that they "check the bandits for any valuables" and that the ring the leader "wore on his right hand" was "the only real thing of note". Later, "Seeing that heart ring on the Bandit's hand kept bugging him and he didn't know why." Leaving the ring on the hand is therefore **consistent** with the source, and it does not disturb the Ch.21 payoff: the paired wearer feels Heath's heart stop either way. Two parts are not consistent:
- "It was not his to take." (L248) gives Bal an **invented moral motive**. It also clashes with the same scene, where they go "through the bandits for anything worth taking" and find "a few coins" (L234–236). If coins are fine to take, the ring is too, so the line reads as a writerly flourish. → F2.
- L360 "And of the other one, somewhere, on somebody's finger, that had stopped beating" has Bal **work out the pairing mechanism tonight**. The source has him not knowing why it bothers him, and the author's ruling saves the realization for Ch.21. It also closes the warm, brave chapter on a faint chill, and the outline's hook is the pass at morning. → F3.
- Small slip: the source puts the ring on the leader's **right** hand. L238 says "the hand that had held the sword". Make it "his right hand".

**Additions (texture, no plot):** Lora's rain questions; the squirrel on the ley line; Zoran's "Bring them back clean"; Hopper leaning on Amelia; the flaky pies; Lora sewing kit; Viridia "anything, as long as it wasn't brown"; the stance correction. None adds plot. Two edge toward invented traits: "Lora had a needle in her pack, **of course**" (implies a standing always-prepared trait; STATE removed "Lora reorganizing supplies") → F12. Viridia's "not brown" is a one-off joke, not a preference that recurs. Leave it, but it must not come back.

**Continuity / canon errors:**
- **L14 "Verin found him a book on ley lines."** Verin is the escort mage and driver from Ch.5–6 (character-bible L333). He is not at the school. The library's on-page figure is THE LIBRARIAN (Ch.9, bible L435). → F1 (CRITICAL logic).
- **L216 "She had spent nearly three thousand years locked in the dark."** In Ch.1 the hall is lit by two large braziers (ch-01 L109), and Ch.14 uses "locked away for close to three thousand years". "In the dark" is wrong on the facts, and as a narrator's aside it explains the moment. → F10.
- **L60 "The offer honestly surprised her."** This is inside Amelia's head, which breaks close-third-on-Bal. → F11.

## Magic-repetition note
There are **no blood spells** in this chapter, which matches the source: the fight is steel, a wolf and an enchanted ring. Effects on page: Viridia's ring shakes the ground (a source item, its single use here); Hopper's size collar (Ch.13 item, source); Lora's salve (alchemy, not a spell). Nothing is invented and nothing repeats. Ledger housekeeping: foundation.md's Magic ledger has no row for **Viridia's earth-shaking ring**. Add it (Viridia / source ~1 / Ch.16) so later uses are counted. No flag to the author is needed.

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | Execution-level freshness on a stock ambush: the squirrel on the ley line ("Whether it needed bigger nuts.", L16); the palm problem turned into tactics ("a hand holding a weapon did not show you its palm", L128); the source's other-POV lines moved into Viridia's firewood report (L278) rather than lost; the wolf choosing Amelia over its owner ("Well. I see where I rank.", L50). | none |
| Theme | 8.5 | Protecting your own against letting them protect themselves runs through both halves. It is never stated by the narrator. The source's own lines carry it: "Do not interfere" (L166), "I have to be able to protect myself" (L224), "I feel useless" (L326). Plenty of plain texture (pies, the brown shirt, bigger nuts). | none |
| Characters | **7.5** | On merit 8.5. Lora commands once she has a job ("Sit," she ordered. "And don't talk.", L202; the stance drill, L306). Viridia is wry and physical ("laid a branch across his arms with some force", L274). Amelia's restraint is the chapter's spine. Hopper has her own choices (Amelia, the jerky). Chaos (commercial 2–3/4): irrelevant thought ✓ (squirrel); failed emotional management ✓ (Amelia, "every bit of will", and Bal's surprised laugh when the pain goes, L226); memory ✗ (absent is fine); distortion ✗. | **Gesture-class cap:** look-beats 6 in about 400 words (L206–248); three sit/perch clusters (L10–20, L70–90, L200–230); Amelia perch + swinging foot continued from Ch.15 L116 (also Ch.2, Ch.5); blush class recurring (Ch.10, 12, 14, 16). See the hand count. |
| Prose & Voice | 8.5 | Underlines: "It was cold first. Then it was very hot." (L156). "Viridia was a lump with blue hair coming out of one end." (L348). "which he held out for her, stiff as a pair of shelf brackets" (L264). "There was no sense in walking into that sword to prove it." (L186). Close-the-book sentence: the stillness gust (L178), though it repeats Ch.14 (F8), so the replacement line must carry this. Under pressure the voice changes: "Bal circled. Parry. Stab. Parry." (L150) and the single-line paragraphs L154–166. Ugly sentence present: "Amelia's place beside him was empty, with no noise at all." (L256). American register throughout ("Me neither", "Up", "I'd just have to buy the materials"). Pattern #11 instances: 3 (0.6/1k), under the commercial cap. | none (provided F8 replaces the anchor sentence with one of equal force) |
| Pacing & Coherence | 8.0 | Speed variation is very good: a slow week, the road, the fight cut into short paragraphs, a long exhale at the log, a quiet walk. Value shift: eager (+) → ambush and wounds (−) → "I want you here because I like you" (+). Scene breaks about every 450 words. The hook lands on the pass ("They would be in it an hour after first light.", L360). | **Internal contradiction:** Verin in the library (L14). The hook is diluted by the ring coda (L360). |
| Emotion | 8.5 | Anchor: Amelia with clasped hands while he bleeds (L178), then "I think that was the hardest thing I've ever done" (L214). Emotional surprise: Bal laughs because the pain left (L226), and "Can a vampire have a heart attack?" lands inside worry (L274). Body rebel: "her eyes shut, and opened again" mid-sentence (L326). Techniques: physical, humor-in-danger, restraint, anticipation. Warm, with no dread. | none (with F3 removing the chill) |
| Engagement (Dim 7) | 8.5 | Self-insertion: the hero takes the boss alone so his girls stay safe, and they stay out because he asked. Empathy: a goddess who can't help and hates it. Fascination: a bandit with a noble's paired ring. | none |
| **FLOOR** | **7.5** | | Characters (gesture-class cap) |
| **AVERAGE** | **8.3** | (8.5×5 + 7.5 + 8.0) / 7 = 8.29 | |

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8.5/10 | First real fight, short paragraphs, breaks about every 450 words, ends on the pass. |
| Tomorrow Test | 3 anchors → 9 | IMAGE: Amelia clasping her own hands on the road. IMAGE: rapier through the knee from his knees. QUOTE: "I don't need you here for what you can do for me. I want you here because I like you." |
| Casual Reader | 8.5/10 | Brave, warm, funny ("I see where I rank"); the hero bleeds for the girls and they love him for it. |
| Shareability (quote/plot/emotional) | 3/3/4 → 7.0 (MAX 8×0.6 + AVG 6.7×0.4) | "I want you here because I like you" / the ambush and the ring / a goddess who has to stand and watch. |
| Concept Pitch | yes (10) | |
| Human Closeness | yes (10) | The log scene, the firewood talk, the walk. |
| **Total** | 0.2×(8.5 + 9 + 8.5 + 7.0) + 0.1×10 + 0.1×10 = 8.6; +0.5 strong anchor = 9.1 | |

CVI-Legacy (default weights): Originality 8.5×0.3 + Theme 8.5×0.25 + Cultural Vocabulary 3×0.2 + Re-readability 5×0.15 (the ring rewards a re-read after Ch.21) + Identity 3×0.1 = 6.3.

## Anti-AI Scan (20 patterns; commercial clean threshold 0–8)
1. Forced symmetry: minor, 1 ("It was cold first. Then it was very hot.", earned).
2. Empty poetic vocabulary: clear.
3. Automatic rule of three: minor, 1 ("They had longswords. They had axes. Two carried crossbows").
4. Em dashes: clear (0).
5. Empty metaphors: clear.
6. Dramatic "And" openings: minor, 1 (L360 "And of the other one", removed by F3).
7. Pseudo-philosophical closings: minor, 2 ("It was not his to take.", L248; the ring coda, L360). F2/F3 remove both.
8. Excessive parallelism: minor, 1 ("Three men had her surrounded. Then two did. Then one", functional).
9. Overly smooth transitions: clear.
10. Described emotions: minor, 1 ("The offer honestly surprised her", F11).
11. Explanatory extension: 3 (0.6/1k), under the commercial cap: L178 "as if somebody had asked her to wait there and she was waiting"; L128 "a hand holding a weapon did not show you its palm"; L136 "like a wagon bed going over a rut, and kept on bucking".
12. Binary negation opener: minor, 1 ("Not her hands. Not her skirt.", replaced by F8).
13. Precision flex: clear.
14. Emotional control demonstration: minor, 1 (L158), and it is canon (pain tolerance).
15. Authoritative description: clear (the ley-line paragraph admits "How much bigger, the paragraph didn't say").
16. Philosophical asides: clear.
17. Clean dialogue: clear (Lora cuts Bal off at "No", L88; the fight lines are broken).
18. Thematic echo chamber: clear (bigger nuts, flaky crust, brown shirts).
19. Graduated reveal: clear (road → fight → camp → walk is the source's own shape).
20. Emotional temperature report: clear.
**Total: 9 patterns touched, all minor; 7 after F2/F3/F8/F11. Inside the clean band for commercial fiction.**

## Gesture Hand Count (full; the window is any 500 words)
| Class | Instances (line @ word offset) | Max in any 500w | Verdict |
|---|---|---|---|
| **Look / watch / glance / study** | L206 @2892 "watching him"; L212 @2915 "Amelia watched Lora's hands"; L212 @2923 "She watched for some time"; L222 @2985 "Lora glanced up"; L226 @3034 "He glanced at his arm"; L248 @3285 "Bal studied the ring" | **6 in ~400w** | **OVER: F4** |
| **Look (second cluster)** | L32 @449 "Amelia looked from one…"; L36 @520 "Zoran studied him"; L48 @698 "without a glance" | **3 in 250w** | **OVER: F5** |
| Look (fight) | L152 @2240 "could not keep watching"; L162 @2337 "He looked toward her voice" (source); L180 "Bal took in all three" | 3 in ~320w | Borderline. The source's distraction beat must stay; F5's sibling fix: L152 "and Bal could not keep watching, because that sword was coming again" → "and then that sword was coming again." (optional F5b) |
| **Sit / perch** | L10 @130 "sat them down"; L16 @272 "Bal sat with it a while"; L20 @338 "she perched" | **3 in 210w** | **OVER: F6a** |
| **Sit (Hopper)** | L70 @1003 "the wolf sitting on her step"; L90 @1274 "Hopper sat at Amelia's feet"; (L102 "good for sitting", not a gesture) | 2–3 in 500w | **OVER in spirit: F6b** |
| **Sit (the log)** | L200 @2835 "pushed him down onto a fallen tree"; L202 "Sit"; L208 @2906 "She came, and sat, very straight"; L230 @3107 "Hopper … sat beside the log" | **4 in ~270w** | **OVER: F6c** (all source-driven; reword two) |
| Sit (camp) | L298 "Lora sat straight up"; L310 "Amelia sat across the fire"; L352 "Hopper sat" | 2 in any 500w | under cap |
| **Amelia perch + swinging foot** | L20 "perched"; L32 "Her foot had stopped swinging". The same pairing closes Ch.15 L116 ("perched on it, swinging one foot"); foot-swinging also Ch.2 L183, Ch.5 L19 | 1 per chapter, **chapter after chapter** | **Recurring device: F7** |
| **Blush** | L30 "went pink"; L32 "went pinker still" (Lora); L8 "cheeks red from the cold" is weather, not a blush | 2 in 45w, but the class recurs Ch.10, Ch.12 ("only turned her pinker"), Ch.14, Ch.16 | **Recurring class + echo of Ch.12: F9** |
| **Freeze / stillness** | L22 "Lora stopped with her pencil in the air"; L32 foot stopped; L178 "She was not moving at all … did not find one thing on her to stir" | 2 in 500w | Under the count, but **L178 repeats Ch.14 L148** ("nothing in her stirred … as if the hearth had always had a statue"), Amelia's total stillness used as the anchor two chapters running: **F8** |
| **Hand hold (Bal–Amelia)** | L218 "reached over for her hand. Hers held on"; L312 "held out his hand … She took it"; L318 "kept hold of her hand"; L324 "her hand was in his"; L358 "Amelia's hand found his"; L362 "holding on to her" | **4 beats in ~110w (L312–324)** | **OVER: F13** (cut the restatement at L324) |
| Smile/grin | L192 "If a wolf could grin" (source) | 1 | clean |
| Laugh | L226 laughed; L272 chuckled; L278 She laughed | 2 in 500w (L272/L278) | clean (source has all three) |
| Eyes | L174 across his eyes; L126 lids; L326 eyes shut | 1–2 | clean |
| Chest / heart | L94, L106 (Hopper's body), L200 hands on his chest; the "heart" hits are the ring and "heart attack" (source nouns) | 1 gesture | clean |
| Nod / shrug / head shake | 0 | — | clean (the source's "Bal nodded" and "shakes her head" are rendered otherwise) |

## Character Chaos Check (Bal)
- Irrelevant thought: present (the squirrel, L16).
- Cognitive distortion: absent (fine for commercial).
- Unprompted memory: absent (fine; no cadence device).
- Failed emotional management: present (the laugh when the pain goes, L226).
- Voice under pressure: demonstrated (L144–166 fragments; "He meant all three girls. There was no breath to spare for saying so.").

## Secondary Characters
- Lora: her own moment. A commander with a job to do (L200–204, L304–308), plus her rain-watching week.
- Viridia: her own moment. Loses her spear, then tells the fight her way (L274–278).
- Amelia: her own moment, the chapter's anchor and the walk.
- Hopper: her own moment (Amelia over Viridia; the guard chuff).
- Zoran, Ms. Summers: function plus one human touch each (fine for walk-ons).
- Heath (unnamed): "if you please" courtesy before threats, as the bible says.

## The Tomorrow Test
**What the reader remembers:** the goddess standing on the road with her hands clasped, not going to him, and later "I feel useless."
**Anchor type:** BOTH (image + quote).
**Verdict:** ANCHOR EXISTS. Note that the *wording* of the image must change (F8), because "nothing on her stirred" is Ch.14's anchor language.

## Shareability
"He takes the boss alone and tells the girls not to interfere, and the vampire goddess has to just stand there." Shareable.

## Reader Reports
**The Devourer:** Nothing to stop on. The week runs quickly, the growl lands at about 1,500 words, and the fight is fast and easy to follow. A slight drag around the log, where everyone keeps looking at everyone. The final ring paragraph makes them think "ooh, setup", but it blunts "the pass at first light".
**The Critic:** Would underline "It was cold first. Then it was very hot." and "stiff as a pair of shelf brackets". Would notice that Amelia's stillness echoes the card scene in Ch.14, and that she is perched with a swinging foot again. Would find "It was not his to take" pious next to "A few coins".
**The Hostile:** "Verin? The coach driver works in the library now?" They also flag "locked in the dark" (the hall had braziers), and "The offer honestly surprised her" in a Bal-only book. And if Bal works out the paired ring tonight, why is it a realization in Ch.21?
**The Casual Reader:** Loves it: the wolf picking Amelia, the pies, the hero bleeding for his girls, "I want you here because I like you." They would keep reading. Nothing here is a vibes problem.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|---|---|---|---|---|---|
| Verin in the library (L14) | | | ✓ | | INVESTIGATE (but a hard continuity error: fix) |
| Look/sit clusters at the log | ✓ | ✓ | | | SHOULD FIX (and a mechanical cap) |
| Anchor repeats Ch.14 stillness; perch/foot recurring | | ✓ | | | INVESTIGATE (cap-relevant) |
| Ring coda: early payoff, cool close | ✓ | ✓ | ✓ | | IMPORTANT |
| "Not his to take" against the coins | | ✓ | ✓ | | SHOULD FIX |
| "locked in the dark", POV slip | | | ✓ | | INVESTIGATE |

## Revision Recommendations (Ranked; surgical, no plot added)

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|---|---|---|---|---|---|
| F1 | L14 | Logic/Continuity | "Verin found him a book on ley lines" | Verin is the Ch.5–6 escort mage, not at the school; the library has the librarian (Ch.9) | → "The librarian found him a book on ley lines" | No |
| F2 | L238, L248 | Character/Source | "on the hand that had held the sword" / "Bal studied the ring. Then he let it stay on the dead man's hand. It was not his to take." | Invented moral motive that contradicts the coins they took; also a look beat; source says right hand | L238 → "Their leader wore a ring on his right hand." L248 → "Bal left it on the dead man's hand." | No |
| F3 | L360 | Pacing/Source | "He thought of the ring, two miles back, on a hand that had gone still. And of the other one, somewhere, on somebody's finger, that had stopped beating." | Works out the pairing early (source: "didn't know why"; author ruling puts it in Ch.21); a chill at a warm close; dilutes the pass hook | Cut both sentences. The paragraph ends "…The woods were beyond it." L268 already has the ring "still bothering him" | Yes: payoffs ruled for a later chapter are not pre-reasoned earlier |
| F4 | L212, L226 | Character (gesture) | "Amelia watched Lora's hands working on his arm. She watched for some time before she answered." / "He glanced at his arm. The salve smelled…" | Look-beats 6 in ~400w | L212 → "Lora's hands went on working at his arm. It was some time before Amelia answered." L226 → "The salve smelled of crushed mint…" (drop the glance). With F2 this leaves 2 | No |
| F5 | L36 | Character (gesture) | "Zoran studied him until Bal began composing a second, better way of asking." | Third look in 250w | → "Zoran said nothing for so long that Bal began composing a second, better way of asking." (Optional F5b, L152: "Then one, and then that sword was coming again.") | No |
| F6 | L16, L70, L208, L230 | Character (gesture) | "Bal sat with it a while." / "the wolf sitting on her step" / "She came, and sat, very straight." / "Hopper came down from the trees and sat beside the log." | Three sit clusters | L16 → "Bal read it twice." L70 → "at the wolf on her step". L208 → "She came and took the space, very straight-backed." L230 → "…and lay down beside the log." | No |
| F7 | L20, L32 | Character (recurring gesture) | "she perched on the end of the old red couch" / "Her foot had stopped swinging." | Ch.15 closes on the same perch and swinging foot; foot-swing also Ch.2, Ch.5 | L20 → "she was on the end of the old red couch"; cut "Her foot had stopped swinging." | Yes: Amelia's foot-swing is spent; do not reuse |
| F8 | L178 | Style/Character (cross-chapter image) | "She was not moving at all. Not her hands. Not her skirt. A gust ran along the road and past her and did not find one thing on her to stir." | Ch.14 L148's anchor is the same Amelia statue-stillness ("nothing in her stirred") | Replace those four sentences with: "She had come one step off the road toward him and no farther, and her two hands were holding each other back." (the source's "having to hold herself back"; it keeps the anchor and the close-book force) | Yes: Amelia's total stillness is spent |
| F9 | L30, L32 | Character (recurring class) | "and then went pink and added" … "so warmly that Lora went pinker still" | Two blushes in 45w; "pinker" echoes Ch.12; the class recurs Ch.10/12/14 | L30 → "and then added, quickly, 'If you want to be.'" L32 → "so warmly that Lora went pink." | No |
| F10 | L216 | Continuity/Exposition | "She had spent nearly three thousand years locked in the dark." | The hall had braziers (Ch.1); a narrator gloss | → "She had spent close to three thousand years locked away." (Ch.14 wording) or cut | No |
| F11 | L60 | Voice (POV) | "The offer honestly surprised her." | Inside Amelia's head | → "The offer seemed to surprise her." | No |
| F12 | L292 | Character (invented trait) | "Lora had a needle in her pack, of course," | Implies a standing always-prepared quirk | Cut "of course," | No |
| F13 | L324 | Character (gesture) | "cold and very quiet, and her hand was in his." | 4 handhold beats in ~110w (L312–324) | Cut ", and her hand was in his" → "It was a good night for it, cold and very quiet." | No |

Optional: L48 "Bal knew Hopper only from Viridia's stories. He had not met her." → cut the second sentence (redundant).

### Fix order: F1 (logic) → F2/F3 (source/character) → F4–F9, F12, F13 (gesture caps) → F10/F11 (canon/POV).

## Strengths to PRESERVE
- The fight's rhythm (L144–192): "Bal circled. Parry. Stab. Parry." Bal's preferred position comes before the girls, which keeps it justified and not gory.
- Moving Amelia's "I do not like this" / "He is already hurt" into Viridia's report (L278). This is POV-clean and loses nothing.
- Lora's "Sit… And don't talk", and the drill; the shelf brackets; the lump with blue hair.
- The walk speech close to the author's words; "I don't need you here for what you can do for me. I want you here because I like you."
- The ring left on the hand (consistent with the source and with Ch.21) and the ring "still bothering him" at L268. That is the right amount of foreshadowing.

## PATH TO 8.5
- **Characters 7.5 → 8.5 requires:** the gesture caps cleared. F4 (log looks), F5 (Zoran), F6 (three sit clusters), F7 (perch/foot), F8 (stillness anchor reworded), F9 (blush), F12, F13. Each is a cut or a swap of a few words. After them no class reaches 3 in any 500 words, and no Amelia gesture carries over from Ch.14/15.
- **Pacing & Coherence 8.0 → 8.5 requires:** F1 (Verin → the librarian) and F3 (cut the ring coda so the chapter ends on the pass and her hand).
- Prose holds 8.5 only if F8's replacement line is used (or one of equal force), because the current close-book sentence is a Ch.14 echo.

## VERDICT
**POLISH.** Genesis Floor 7.5 (Characters), Average 8.3; Casual 8.5. With F1–F13 the chapter projects to Floor 8.5 / Casual 8.5 → PASS on re-check.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

## Revision applied (2026-10-20, book-editor, r1)
- **F1** Verin → "The librarian found him a book on ley lines."
- **F2** Ring on the leader's right hand (worded "On their leader's right hand was a ring." because "his right hand" tripped tic_report's 3x book-wide phrase gate and "on the right hand" tripped voice_wear self-repeat); "Bal left it on the dead man's hand." (no motive).
- **F3** Ring coda cut; the paragraph ends "The woods were beyond it."
- **F4** Log looks: "Lora's hands went on working at his arm. It was some time before Amelia answered."; "He glanced at his arm." cut.
- **F5 / F5b** Zoran "said nothing for so long that…"; "Then one, and then that sword was coming again."
- **F6** "Bal read it twice."; "the wolf on her step"; "She came and took the space, very straight-backed."; Hopper "lay down beside the log."
- **F7** "she was on the end of the old red couch"; foot-swing line cut.
- **F8** Stillness sentences replaced with "She had come one step off the road toward him and no farther, and her two hands were holding each other back."
- **F9** "and then added, quickly, 'If you want to be.'" / "Lora went pink."
- **F10** "close to three thousand years locked away."  **F11** "The offer seemed to surprise her."  **F12** "of course," cut.  **F13** ", and her hand was in his" cut.
- Optional: "He had not met her." cut.
- Extra gesture-window fixes after recount: "didn't mind everybody looking at her" → "didn't mind the attention" (3 looks in ~350w at L32–56); "She stopped to stare at nothing" → "She stopped" (stare + "looked" + "watching" in 20w).
- Recount: no gesture class 3+ in any 500 words; em dashes 0; "the way [x]" 0; similes under 4/1k.
- Gates: style_check clean; grammar_check 0 errors; voice_wear_check clean (strict); tic_report --gate clean (scratch copy Ch.1–16 at /tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/ed16/).
- Not done here: Magic-ledger row for Viridia's earth-shaking ring in project/foundation.md (outside this edit's file scope).
