# Evaluation: Chapter 19 — The Rule
**Evaluator:** book-evaluator | **Date:** 2026-10-20
**Text evaluated:** `manuscript/chapter-19.md` (2,490 words of prose by the tool count; target 2,600, range 2,300–3,000, so on spec).
**Read first:** STATE.yaml (decisions: the girls' choice is free; "We heard what you told Amelia in the pass", one line; the dialogue rule; no shared gestures; spell-repetition watch), book CLAUDE.md, project/STYLE_CONSTRAINTS.md, project/foundation.md (conversion mechanics §0; Magic ledger), character-bible.md, outline Ch.19, manuscript/chapter-18.md (ending), chapter-08.md (the conversion lesson), chapter-14.md, chapter-16.md, Sygl_Complete.txt L780–795, evaluations/chapter-18-eval.md.

## HEADLINE
**CVI-Launch:** 9.1 (8.6 + 0.5 strong anchor) | **CVI-Legacy:** 6.4 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.4
**Engagement Type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence Alert:** 1.6 gap (Launch over Floor). Not over 2.0. The chapter is commercially strong and is held down by a mechanical cap, not by its content.

**VERDICT: POLISH (FAIL at the 8.5 gate).** The content is right:
- Every source beat is present and in order.
- The girls choose in their own words, for their own reasons. Bal gives them four separate chances to say no: "only if they choose to", "you need to think carefully", "I don't want either of you to be unhappy", and "last chance".
- There is no coercion framing and no guilt.
- The ritual is clear and not gory.
- "We heard what you told Amelia in the pass" is used once, by Viridia, in the outline's position.
- The fade lands exactly on "Then let's go to bed."
- No spell is invented. The conversion follows the Ch.8 lesson (cut the left palm, send the blood in, push).

The floor is **Characters 7.5**, a gesture-cluster cap. The FULL hand count found six 500-word windows with 3+ of one class:
- a pencil-business cluster at the open
- three looks/watching clusters
- two sitting/posture clusters

It also found two other problems:
- **A gesture shared across characters:** Viridia's "bent so close… nearly touched" is Lora's Ch.14 beat.
- **A Lora blush that replaces the source's smile.** It is also her third blush in four chapters.

Every fix below is a cut or a word swap and adds no plot. With F1–F13 applied, the chapter projects to **Floor 8.5 / Casual 8.5: PASS.**

## Gate tools (scratch copy, Ch.1–19 at `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/ev19/manuscript/chapters/`)
- `voice_wear_check.py`: **clean.** No retired phrases and no device over cap. Two cross-chapter self-repetitions are WARN only.
- `tic_report.py --gate`: **clean.** Ch.19 has 0 and-chains, 0 negation pivots, 0 auto-recurrence, and adds nothing to the book-wide gesture table. The tool's classes do not cover posture, looking, or prop business, which is why the hand count below catches what it does not.
- `style_check.py --dir manuscript`: **clean.** Ch.19 has simile 0.4/1k, adverb 12.8/1k, 0 em dashes and no new repeated phrase.
- `grammar_check.py --file chapter-19.md`: 0 errors.

## FULL gesture hand count (word positions w from the first prose line; 500-word windows)
| Class | Instances (position) | 3+ in 500w? | Verdict |
|---|---|---|---|
| Smile/grin | Amelia "smiling a little" (w1398); "Her mouth curved" (w2090); "They grinned" (w2470) | no (max 2) | OK. All three are source beats. |
| Laughs | Lora "laughed" (w1115, source); Amelia's shoulders "might have been a laugh" (w1185) | no (2) | OK |
| Blush | Bal "ears went hot" (w1177); Lora "went pink to the edges of her freckles" (w1325) | no (2) | **Lora's pink recurs across chapters.** It appeared in Ch.16 ("Lora went pink"), was flagged in the Ch.17 and Ch.18 evals, and is back here. It also REPLACES the source beat, which is "Bal was glad to see Lora smiling". → F6 |
| Looks/watching/facing | (a) "still facing the flames" (w40); "turned her head… to find Viridia" (w150); "Bal checked Lora's face" (w205) | **YES, 3 in 165w** | **CAP** → F2 |
| | (b) "Bal looked to Amelia" (w662); "Her face was toward the fire again" (w666); "checked each other's faces" (w727); "gave the ceiling a long-suffering stare" (w1115) | **YES, 4 in 453w** | **CAP** → F3 |
| | (c) stare (w1115); "Amelia kept her face to the fire" (w1180); "She was looking straight at Bal" (w1230); "Lora blinked at her. Even Amelia came around from the fire" (w1290); "Over at the fire, Amelia was smiling" (w1398) | **YES, 5 in 283w** | **CAP** → F3 |
| | (d) "while the three of them watched" (w2020); "Amelia had watched it all" (w2070); "Her attention had moved to him" (w2280); "Both girls were watching him" (w2421); "traded a glance" (w2465) | **YES, 5 in 445w** | **CAP** → F4 |
| Amelia-at-the-fire orientation (a sub-class of looks) | w40, w666, w1180, w1290, w1398, plus "from the hearthrug" w2070 | 3 in 220w (w1180–1398) | The source has her looking at the fire twice. Six renderings make it stage business. Fixed inside F2–F4. |
| Sitting/posture | (a) "This one sat up a little straighter" (w1360); "come and sit on the tabletop" (w1420); "The girls sat shoulder to shoulder" (w1549); "once he sat" (w1575) | **YES, 4 in 215w** | **CAP** → F5 |
| | (b) "squeezed onto the couch" (w2169); "enough to sit there" (w2205); "She rose and stood" (w2225); "Lora sat bolt upright" (w2266); Hopper "lay down" (w2360) | **YES, 5 in 191w** | **CAP** → F5 |
| | Lora "sat up a little straighter" (L118) AND "sat bolt upright" (L194) | — | The same character makes the same posture move twice in one chapter |
| Freezing/stopping | "Lora's pencil stopped mid-stroke" (w85); "Lora's face went still" (w630) | no | OK |
| Eyes | "her eyelids came down" (w2090, source "closed her eyes") | no | OK |
| Chest/heart | "forehead… against his collarbone" (w2160) | no | OK |
| Hand holds / props | **Pencil:** "Bal's pencil skidded" (w5); "let the pencil roll" (w55); "Lora's pencil stopped" (w85); "the end of her pencil against her lip" (w211); "Lora's pencil had dropped… dragged a long grey line" (w385); "waved that away with the pencil" (w1036) | **YES, 5 in 380w** | **CAP.** Lora holds the pencil as a prop 4 times. → F1 |
| | Viridia's hand on Hopper (w400, w640); "held on hard" in the hug (w2335) | no | OK |
| Tilts / nods / shrugs | 0 / 0 / 0. The source's nods were converted into speech ("Yes." "Yes."), and the source shrug was dropped. | — | OK |
| "Bent so close… nearly touched" | Viridia, Ch.19 L172. Lora had the same beat in Ch.14 L32 ("bent so close to watch it that her glasses nearly touched the stone") | — | **Shared gesture across two characters** (author ruling: no two characters share a gesture) → F7 |
| Hopper asleep/dreaming | "One hind leg ran a little in a dream" (L34). Ch.18's last paragraph: "twitched in a dream." | — | The image repeats about 300 words of reading apart, across the chapter break. → F8 |
| "checked [X's] face(s)" | L24, L68 | — | A repeated construction. Fixed in F2/F3. |

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | Bal's domestic dread in the dark bedroom with the dagger: "Did the dorm clean up blood by itself, the way it put rooms where you wanted them, or would it be him on his knees with a rag and cold water?" (L138). The palms going *blank* before the new sygl rises: "both palms were bare, no blood and no sygl" (L160). Hopper claims Amelia's vacated spot "with a groan of deep contentment" (L200). | none |
| Theme | 8.5 | Blood given freely, as the girls' own choice. Each gives her own reason: Lora's father, Viridia's Hopper and "Miss Book Smart". Bal: "I care about both of you, and I would absolutely hate to lose you. But I don't want either of you to be unhappy." (L80). There is plenty of texture: "smelled of his own clean laundry" (L134); the rune "she had spent ten minutes on" (L44); "collar-small" Hopper (L34). | none |
| Characters | **7.5** | On merit 8.5. Lora hedges with people and is exact on her subject ("The teachers can't retaliate, can they?"; she wipes the blade and lays it "out of everybody's way", L154). Viridia covers feeling with a jab ("Especially Miss Book Smart here.") and is the one who breaks the silence with the overheard line. Amelia keeps her distance so a refusal "would hurt less if she had never been part of the asking" (L64, from the source). Bal handles a marvel with a practical worry (L138, on-card). Chaos (commercial): irrelevant thought ✓ (L138); distortion ~ ("It scared him a little how badly he wanted to hurry them", L78); triggered memory that returns to the scene ✓ (the lake and snake, L88; Thad's room, L80; the fingernail lesson, L136, which matches Ch.8); failed management ✓ ("His voice cracked halfway, and he had to start it again", L184). That is 3.5/4. | **Gesture caps:** 6 windows with 3+ of one class (pencil ×1, looks ×3, posture ×2). One shared gesture (Viridia's "bent so close", which is Lora's Ch.14 beat). Lora's blush recurs across chapters and displaces the source smile. |
| Prose & Voice | 8.5 | Underlines: "Lora kept her left hand open in her lap, palm up, and could not stop reading it." (L188, the close-the-book line); "Their hands were clear and white from the heel to the fingers. The only red on them was his, sinking into the cuts." (L160); "He was extremely pleased with that one." (L96); "He did not mention that he could have had another before he reached the door. The dorm would have made it for him gladly." (L212). Ugly sentence present ("Hopefully.", L54). Under pressure the voice shortens to one-line paragraphs ("He pushed it deeper.", "It went in."). American register is mostly good. | Register slips: "hearthrug" ×2 (L10, L178; Ch.18 was already fixed to "the rug by the hearth"); "trouser leg" (L154). Pattern #11 sits at 2 instances (0.8/1k), exactly at the commercial cap and not over it. |
| Pacing & Coherence | 8.5 | "decision, then ritual" as outlined. Value shift: the rule threatens them (−), then they are bound to the Blood and made priests (+). Speed variation: the slow offer, then a fast acceptance, a held breath in the dark bedroom, the ritual in one-line beats, and the warm fade. The hook is at L206 ("Bal discovered he was looking forward to breakfast"), and the chapter ends on the source's fade line. | none |
| Emotion | 8.5 | Anchor: "two white palms coming up dark with the blood sygl" ("faint at first, a shadow of a line, then another line beside it", L172–174), delivered through objects and actions. Emotional surprise: Bal worrying about blood in the wood grain at the most solemn moment (L138); Hopper's contented groan on the spot Amelia vanished from (L200); Viridia's "Hopper" reason before the real one (L112–116). Body rebel: Bal's ears go hot (L106), his voice cracks (L184), his hand is "not quite steady" (L152). Techniques: anticipation, humor in a solemn moment, tenderness, relief. | none |
| Engagement (Dim 7) | 8.5 | Self-insertion: two girls choose the narrator's world for good, then "Then let's go to bed." Empathy: Bal is afraid of losing them and refuses to hurry them. Fascination: the war declared overnight, and Porter walking into breakfast too late. | none |
| **FLOOR** | **7.5** | | Characters (gesture clusters, shared gesture, displaced source smile) |
| **AVERAGE** | **8.4** | (8.5×6 + 7.5) / 7 = 8.36 | The single-dimension bottleneck is Characters, and the cap is mechanical |

## CVI-Launch Breakdown (Commercial Assessment)
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8/10 | Short scenes, a decision that clicks fast, a tactile ritual, a fade |
| Tomorrow Test | 3 anchors (2 image + 1 quote) → 9 | The palms going white, then dark with the sygl; Hopper on Amelia's spot; "Then let's go to bed." |
| Casual Reader | 8.5/10 | The payoff chapter readers have waited for. Warm, funny and romantic, and the magic is easy to follow |
| Shareability (quote/plot/emotional) | 3/4/3 → 7.5 | "I've got an in with the Blood Lead Mage."; they convert to beat the rule the night before it lands; "If I'd lost you…" |
| Concept Pitch | yes (10) | |
| Human Closeness | yes (10) | The whole chapter is four people in one room |
| **CVI-Launch** | 8.6 + 0.5 (strong anchor) = **9.1** | |

**CVI-Legacy (default weights):** Originality 8.5×0.30 + Theme 8.5×0.25 + Cultural Vocabulary 3×0.20 + Re-readability 5×0.15 (the ring, the Ch.8 lesson paying off, the overheard pass) + Identity 4×0.10 = **6.4**.

## Anti-AI Scan (20 Patterns; commercial thresholds, 2.49k words)
1. Forced symmetry: Clear.
2. Empty poetic vocabulary: Clear.
3. Automatic rule of three: Found, 1 (0.4/1k). "Saturdays on the road, the bear, the snake, the stew" (L48). These are real Ch.16–18 events. Minor.
4. Em dashes: Clear (0).
5. Empty metaphors: Clear.
6. Dramatic "And" openings: Found, 1. "And Viridia would have to send Hopper away besides." (L46). Minor.
7. Pseudo-philosophical closings: Clear.
8. Excessive parallelism: Clear. The "Yes," / "Yes," pair is functional.
9. Overly smooth transitions: Clear.
10. Described emotions: Found, 4 (1.6/1k). "That surprised him" (L28); "It scared him a little" (L78); "Bal was glad to see it" (L118, from the source); "Bal discovered he was looking forward" (L206). Plain commercial register and on-voice. Moderate.
11. Explanatory extension: Found, 2 (0.8/1k), at the cap and not over it. "He had been half listening to the fire for so long that a voice coming out of it startled him." (L8); "would have hidden in a book until the conversation was over" (L118).
12. Binary negation opener: Clear.
13. Precision flex: Clear.
14. Emotional control demonstration: Found, 2. "He pulled himself back out of it." (L80); "He said the hard parts instead." (L78). Both serve the free-choice framing. Minor.
15. Authoritative description: Clear ("Viridia muttered something into his shirt that he did not catch").
16. Philosophical asides: Clear.
17. Clean dialogue: Found, mild. The offer runs as orderly Q&A, which is the source's own structure.
18. Thematic echo chamber: Clear.
19. Graduated reveal: Clear.
20. Emotional temperature report: Clear.
**Total: 6/20 present, mostly minor. CLEAN for commercial fiction (0–8).**

## Source Fidelity (L780–795) and Canon
Every beat is present and in source order:
- "tomorrow" and Porter's report to the originators (Mr. Winter is silently fixed to Mr. Winters)
- the bloodwolf and Raizen's motive, and "Kenmei didn't care"
- Porter's suggestion, Hopper, and "Can they do that?"
- the bond, and Lora's all-Waves family and Viridia's village
- "There is a way to circumvent the rule. But it is not something to take lightly."
- Amelia letting him handle it, with the source's reason
- the offer: choice, irreversible, families, how blood sygls are treated, "I don't want you to be unhappy"
- inheritance kept, maybe another gained; the ring; the waves magyk lost; the teachers can't retaliate
- "an in with the Blood Lead Mage"
- **"We heard what you told Amelia in the pass"**, said once, by Viridia, in the outline's slot
- Lora's and Viridia's own lines, "last chance", and the dagger
- three left palms cut together; two thin streams; the palms forced white; the blood reaching their centres; the cuts closing; the sygls darkening; "I can feel you now."
- the thanks, the priests, and the war declared before morning
- "one bedroom", and the fade at "Then let's go to bed."

What the chapter adds is all interior or texture:
- the dark-bedroom worry
- the memory of the Ch.8 fingernail lesson, which matches Ch.8 L61
- Hopper's business

Lora's father serving in Kenmei's army (L54) is from the source (L386).

Fidelity problems:
- **L110:** "I can't be sure how my father will feel" alters a bolded outline line ("I'm not sure…") for no gain. → F10
- **L30:** "socializing with students of other sygls" adds information to Amelia's line. The source has "with other students". → F11
- **L118:** the source's "Lora smiling" is replaced by a blush. → F6
- **INVESTIGATE (book level, not a fix here):** "It can't be done to anyone who doesn't want it" (L72) repeats established Ch.8 canon, so it is consistent. Keep an eye on Ch.29 (Toma converted through the elemental core) and the author's "no one was safe if Bal chose to convert them" line so the two read as compatible.

Magic ledger: the conversion is used once (Bal). No spell is invented. No repetition flag.

## Character Chaos Check (Bal)
- Irrelevant thought: present (L138, the blood in the wood and the dorm's cleaning).
- Cognitive distortion: faint (L78, wanting to hurry them).
- Unprompted memory: present and triggered: the lake (L88), Thad's room (L80), the fingernail lesson (L136). Each returns to the scene.
- Failed emotional management: present (voice cracks, L184; unsteady hand, L152).
- Voice under pressure: demonstrated (the ritual runs in short single-beat paragraphs).

## Secondary Character Chaos
- Lora: has her own moment (cleaning the blade, "could not stop reading" her palm).
- Viridia: has her own moment (the overheard line, Hopper as her cover reason, "no comeback").
- Amelia: has her own moment (distancing herself in case of a refusal, white knuckles, "I can feel you now").
- Hopper: texture with personality (the groan).

## The Tomorrow Test
**What the reader remembers:** two bleeding palms going blank white, then the blood sygl rising "a shadow of a line, then another line beside it"; and "Then let's go to bed," they said together.
**Anchor type:** BOTH. **Verdict:** ANCHOR EXISTS. The image type differs from Ch.18's (a flame, a map).
**Shareability:** "They converted the night before the rule could split them up, and Hopper took Amelia's spot."

## Reader Reports
- **Devourer:** Never stops. The decision is quick, the ritual is tactile, and the fade line is a payoff. Wants Ch.20 at once (breakfast).
- **Critic:** Underlines L188 and L160. Is disappointed by the stage-business density: everyone keeps looking at the fire, sitting, and holding pencils.
- **Hostile:** Notices that Viridia's nose-to-palm lean copies Lora's Ch.14 move, that Lora goes pink again, and the "hearthrug" and "trouser" Britishisms. Logic holds: the consent is explicit and repeated, and the mechanics match Ch.8.
- **Casual:** 8.5. Warm, romantic, a little funny. Wants to keep reading.
- **Devoted (inactive genre-wise):** Rewards include "the pass" call-back and the Ch.8 lesson paid off.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|---|---|---|---|---|---|
| Looks/posture/prop clusters | – | ✓ | ✓ | – | SHOULD FIX (gate cap) |
| Shared gesture (bent so close) | – | ✓ | ✓ | – | SHOULD FIX (author law) |
| Lora's repeat blush replacing the source smile | – | ✓ | ✓ | – | SHOULD FIX |
| Register (hearthrug, trouser) | – | ✓ | ✓ | – | SHOULD FIX |

## Revision Recommendations (Ranked; cuts and swaps only, no plot added)

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|---|---|---|---|---|---|
| F1 | L12, L16, L26, L90 | Character (prop cluster) | Pencil ×5 in 380w; Lora's pencil ×4 | 3+ of one class in 500w | L12: "What's going to happen tomorrow?" He let the pencil roll into the crease of the pad." → **"What's going to happen tomorrow?"** (cut the action). L16: cut "Lora's pencil stopped mid-stroke." L26: "Lora had the end of her pencil against her lip. She considered" → **"Lora considered"**. L90: "Lora waved that away with the pencil." → **"Lora waved that away."** Keep L8 and L44. | No |
| F2 | L10, L24 | Character (looks) | "She was still facing the flames." / turned her head / "Bal checked Lora's face" (3 in 165w) | Cluster (a) | L10: "Amelia hadn't left the hearthrug. She was still facing the flames." → **"Amelia hadn't moved from the rug by the hearth."** L24: "Bal checked Lora's face, ready for it to hurt." → **"Bal waited to see whether it would hurt her."** | No |
| F3 | L64, L68, L98, L106, L110, L114, L126 | Character (looks) | Clusters (b) and (c), 4–5 looks in under 460w | Cap | L64: cut "Her face was toward the fire again." L68: → **"Lora and Viridia looked at each other, then back at him."** (source wording). L98: "Viridia gave the ceiling a long-suffering stare." → **"Viridia rolled her eyes."** (source). L106: cut "Amelia kept her face to the fire."; begin **"Amelia's shoulders did something small…"**. L110: cut "She was looking straight at Bal, and"; → **"Her chin was up, and her voice did not hedge anywhere."** L114: cut "Lora blinked at her." L126: "Over at the fire, Amelia was smiling a little." → **"Amelia was smiling a little."** | No |
| F4 | L178, L196, L208 | Character (looks) + Style (register) | Cluster (d): watched / watched / attention / watching / glance; "hearthrug" | Cap; British register | L178: "Amelia had watched it all from the hearthrug, her knuckles white in her lap." → **"Amelia had not moved from the rug by the hearth, her knuckles white in her lap."** L196: "\"Bal.\" Her attention had moved to him." → **"\"Bal,\" she said."** L208: cut the whole line "Both girls were watching him. Hopper had gone back to sleep." | Yes ("hearthrug" → "rug by the hearth", American register) |
| F5 | L118, L142, L188, L190, L194, L200 | Character (posture) | Clusters of 4 and 5 sit/stand/lie beats; Lora "sat up straighter" and "sat bolt upright" | Cap; the same move twice | L118: cut "This one sat up a little straighter." L142: "…almost touching his once he sat." → **"…almost touching his."** L188: "for a while it was enough to sit there." → **"for a while nobody needed to say anything."** L194: "Lora sat bolt upright." → **"Lora made a small, astonished sound."** L200: "circled once on the spot where Amelia had stood, and lay down on it with a groan of deep contentment." → **"claimed the spot where Amelia had been with a groan of deep contentment."** Keep L190's "She rose" (source: "Amelia stands up"). | No |
| F6 | L118 | Character / fidelity | "Lora went pink to the edges of her freckles and did not mind it one bit. Bal was glad to see it." | The source has a smile. Lora's blush recurs across chapters (Ch.16, and was flagged in Ch.17–18). | → **"Lora was smiling at the teasing. Bal was glad to see it."** Keep the Warfare-class sentence. | Yes (Lora's blush is closed; use the source's own beat) |
| F7 | L172 | Character (shared gesture) | "Viridia bent so close over her own hand that her nose nearly touched it." | Lora's Ch.14 gesture ("bent so close… glasses nearly touched") | → **"Viridia held her hand up to the firelight."** | Yes (add "bent so close… nearly touched" to Lora's spent list) |
| F8 | L34 | Continuity / repetition | "One hind leg ran a little in a dream." | Repeats Ch.18's closing "twitched in a dream" | Cut the sentence. End at "and she went on sleeping." | No |
| F9 | L154 | Style (register) | "wiped the blade on her trouser leg" | British | → **"pant leg"** | No |
| F10 | L110 | Fidelity (dialogue) | "I can't be sure how my father will feel" | Alters a bolded outline line for no gain | → **"I'm not sure how my father will feel,"** | No |
| F11 | L30 | Fidelity (dialogue) | "socializing with students of other sygls" | Adds information to Amelia's line | → **"Ban all students from socializing with other students, except in class, or when they're off the grounds."** | No |
| F12 | L178 | Logic (minor) | "When the cuts closed, he had seen her lean toward them, hoping." | Bal "did not dare take his mind off either thread", so he could not have been watching her | → **"Now she was leaning toward them."**, then "Her eyelids came down…". This also removes a past-perfect look. | No |
| F13 | L184 | Fidelity (optional) | "If I'd lost you, I wouldn't have known what to do." | Acceptable under the dialogue rule. The source wording is warmer in the mouth. | Optional: **"I don't know what I would have done if I'd lost you."** | No |

### Fix order: F12 (logic) → F1–F8 (character) → F9–F11, F13 (style/fidelity)

## Strengths to PRESERVE
- The consent architecture: four separate no-exits, and the girls' reasons in their own words.
- The dark-bedroom worry (L134–138).
- The palms going bare and white, then the sygl rising (L160, L172–174).
- "Lora kept her left hand open in her lap, palm up, and could not stop reading it." (L188)
- The voice crack (L184), Hopper's groan, the breakfast hook (L206), and the fade line exactly as the source has it.

## PATH TO 8.5
- **Characters 7.5 → 8.5 requires:** no 500-word window with 3+ of one gesture class, no gesture shared across characters, and the source smile restored. Apply F1–F8 exactly. Then re-count:
  - pencil: 2 (w5, w385)
  - looks: max 2 per window (w150/w727/w1115 spread; w2020/w2465)
  - posture: max 2 (come and sit / girls sat; squeezed / rose)
  - smiles: max 2 (w1340 Lora, w1398 Amelia; w2090 and w2470 are out of window)

  Every other Characters criterion is already at 8.5. Chaos is 3.5/4 and inhabited (L138, L184), and the cast is distinct.
- All other dimensions are already at 8.5. F4 and F9 keep Prose clear of the register slips.

## VERDICT
**POLISH. Floor 7.5 / Average 8.4 / Casual 8.5. FAILS the 8.5 gate on Characters (gesture clusters).** With F1–F13 applied, it projects to Floor 8.5 / Casual 8.5: PASS.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

## Revision applied (book-reviser, 2026-10-20)
All of F1–F13 are applied as cuts or swaps. No plot, characters, habits or tics were added. The consent architecture, the dark-bedroom worry, the ritual, the palms, L188, the voice crack, Hopper's groan, the breakfast hook and the fade line are unchanged.

**Applied as quoted:**
- F1: the pencil business is cut. Only "Bal's pencil skidded" and the grey line through the rune remain.
- F2: "Bal waited for it to hurt her."
- F3: the source's "looked to each other, then back at him"; the fire-facing, "looking straight at Bal" and "blinked" beats are cut; "Amelia was smiling a little."
- F4: "Bal," Amelia said; the "Both girls were watching him" line is cut.
- F5: all quoted swaps.
- F6: "Lora was smiling at the teasing."
- F7: "Viridia held her hand up to the firelight."
- F8: the dream line is cut.
- F9: "pant leg."
- F11: "other students."
- F12: "Now she was leaning toward them."

**Varied because a quoted wording tripped a gate:**
- "rug by the hearth" tripped the style_check repeated-phrase flag (×3) and the voice_wear self-repeat (with Ch.18). L10 is now "Amelia hadn't stirred from the hearth." L178 is now "Amelia had not left the hearth." Both remove "hearthrug."
- "Viridia rolled her eyes" is a voice_wear self-repeat with Ch.10. It is now "Viridia let out a pained sigh."
- F10: "I'm not sure how" (Ch.16) and "I don't know how" (the tic gate) both fail. The line is now "I can't say how my father will feel." This drops the drift to "be sure."
- F13: the source's "I don't know what I would have done" trips the tic gate (the spoken refrains "i don't know" / "don't know what"). The line stays "If I'd lost you, I wouldn't have known what to do."
- "Lora and Viridia looked at each other" tripped the tic gate ("viridia looked at", ×3). It is now "looked to each other."

**Extra window fixes from the re-count:**
- "Bal leaned back" is cut.
- The tabletop is now "in front of him" (source wording).
- "stood with it a minute" is now "waited a minute in the dark with it."
- The last "facing him again" is cut.

**Re-count:** no 500-word window has 3+ of any gesture class. Looks max 2; posture max 2 (squeezed / rose); smiles 2 (Lora L118, Amelia L126); pencil 2; eyes 1. Em dashes 0. "the way" 1. Similes 0.4/1k. The chapter is 2,349 words, inside the 2,300–3,000 range.

**Gates (Ch.1–19):**
- style_check: clean
- grammar_check: clean
- voice_wear_check (scratch copy `scratchpad/ed19`): clean
- tic_report --gate: clean
