# Evaluation: Chapter 5 — Verin's Cottage
**Evaluator:** book-evaluator | **Date:** 2026-10-20
**File:** `manuscript/chapter-05.md` (3,738 words; outline target 3,500; source [pp.17–25] L259–284)
**Lens:** Commercial fantasy with harem-romance elements. Engagement: Self-Insertion (primary), Empathy (secondary), Fascination (tertiary). Judged on the author's terms (2026-10-20). This is a faithful revise/expand of `Sygl_Complete.txt` and should read lighter, warm and playful, like the original script. Amelia is open, confident and affectionate, and her grief is real but brief. Bal is a plain-spoken sixteen-year-old. The register is American. The author's dialogue is the base, polished into natural speech. Nothing here recommends darker themes, new subplots or literary embellishment.

## HEADLINE
**CVI-Launch:** 8.2 | **CVI-Legacy:** 5.9 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.4
**Engagement Type:** Self-Insertion (primary), Empathy (secondary), Fascination (tertiary)
**Divergence Alert:** None (CVI-Launch − Floor = 0.7).
**Verdict:** POLISH. One dimension holds the floor: Prose, and only because of the mechanical Pattern #11 cap. There are 4 explanatory extensions in 3,738 words, which is 1.07/1K against a commercial ceiling of 0.8/1K. There is also one dialogue formatting slip (L241). Without the cap, every dimension sits at 8.5. Seven of the fixes are cuts or one-line edits. One restores an author line. None adds plot.

## Mechanical gates (scratch layout `ev5/manuscript/chapters/chapter-1..5.md`)
- `voice_wear_check.py`: **clean** (strict). No retired phrases, no device over cap, no self-repetition.
- `tic_report.py --gate`: **clean**. No auto-recurrence. Gesture beats in ch.5: only "lips pressed" ×1 is classified, and every class is far under cap.
- `tic_report.py --echoes 5`: 9 second uses. All are generic or source wording ("in the first place", "three thousand years", "Mrs. Brown's office", "to the Heir's School"). None is gated.
- `style_check.py --dir manuscript`: Ch.5 simile 2.1/1k, adverb 12.3/1k, em-dash **0**. No distinctive repeated phrase. **Clean.**
- `grammar_check.py --file`: 0 errors. It did **not** catch the L241 double-quote slip (see R1).
- "the way [x]" as a simile: 0. The two hits are "the rest of the way" and "all the way back". Filter words: "really" ×3 (L83 Verin dialogue, L97 source narration, L229 Amelia dialogue), "just" ×2 (both in dialogue, one of them in the source line "Just makes you more interesting"). Acceptable.

## Source-fidelity check (outline beats, in order)
| Beat | Status |
|---|---|
| Six a.m., **Pierre wakes Bal** and passes on Mrs. Brown's instructions (things → kitchen → office) | Present (L3–11). This follows the decision. Small extra detail: "Pierre was older than Bal" (L5) is not in the decision. It is harmless, but it is an invented fact (R8). |
| Blueberry muffin, last of it stuffed in as they enter | Present (L17–27). Amelia on the counter and "much better than supper was" are invented texture, warm, and call back to the Ch.3/4 cook. |
| Verin: faded but well-kept red robes, kind blue eyes, grandfatherly, "Sarah", the other children in their rooms, "don't take long saying your goodbyes" | Present, near-verbatim (L31–45) |
| "How do I explain Amelia…"; the tap; brand gone; "Familiars can choose whether or not to show the brand…"; "Verin knows not to ask too many questions" | Present, near-verbatim (L47–59). "He's been at this for years" is a fair polish of "doing this a long time". |
| Hug; "keep him out of trouble"; crossed fingers behind her back | Present (L61–69) |
| Portal 12×8 on the main walkway; buggy, dark forest, lantern on a metal arm; travel by cart; diverting enchantment; originators excepted | Present (L73–87). The late-evening light on the far side ("though on this side the sun was barely up", L75) quietly sets up Verin's later "how late it's gotten". That is good, source-consistent expansion. |
| Deathly quiet ride; dream of the school; curious kid; blood mages secretive and never claimed; she is lost in thought; he takes her hand and she keeps it; ten miles | Present (L93–111) |
| Cottage, burning fire pit, "This is my home", horse to the trough, Verin's uniform speech ("your sygl will appear on your clothes"), stew, Thistle | Present, near-verbatim (L113–125) |
| Inside: the hearth and pot, two bedrolls, two parcels; lip-biting; "Are you okay?"; "Can I feed from you?" with full reason; "You're my familiar, and hopefully my friend"; "I am a vampire"; "Nah… Just makes you more interesting"; the shy hug | Present, near-verbatim (L129–157) |
| Originators' idea for multiple schools; he files it away; girlfriend lines; "Well, maybe not the vampire part"; "You."; she blushes | Present (L159–175). Her hair tucked behind her ear is dropped, which is correct under the stage-business ration. |
| Verin's briefing: gates, inner courtyard, raised podium (now "stage"), line behind originator, dorms, "only time you see them"; Amelia trying not to laugh; schedule from the Lead Mage; mixed sygls; "Anything else…" | Present (L177–193). One small drift: the source has "Bal glances sideways at Amelia **and grins**". The draft drops Bal's grin and adds "Bal kept his eyes off Amelia" (L183), which runs against the source beat (R4). |
| "Morning comes early"; logs; snoring | Present (L195–199) |
| Bowls at the trough; Thistle; the sky line; "How long were you in that place?" | Present (L203–213) |
| **"Almost 3000 years… a long 3000 years."** | **Altered** (L215): "Every one of them long." The author's flat repetition is the memorable line. The polish drops it. Restore it (R5). |
| Bench; "won't try to take you away"; "my own stupidity and the fact I trusted them"; stone crafter, high priest of Naisura, peace offering, lost followers; places of power; eight high priests | Present, near-verbatim (L219–233) |
| Blood tear; he wipes it; "They chose their path. Now you are free. I can release you…"; "Thank you for offering… Who else can teach you blood magic?"; tongue out **once** | Present (L235–247). The tongue appears once only. **Formatting slip at L241** (R1). |
| "if you're my familiar I've got to take care of you"; eyes brighten; "Are you sure?"; bite; **unusually high pain tolerance**; the sucking sounds; Bal talks about school and the laborer life; she licks; holes close; "two holes in your wrist"; hand held out; "eager for the new day" | Present and canon-correct (L249–281). The sygl is on the palm (L101, L271). The final line is verbatim. |

No invented plot, characters, habits or backstory. Additions are texture only: Amelia on the counter, "Sarah" as a first name Bal never knew, the potatoes thought, the thumb smear, the warmer fingers, the owl. Tone matches the author's direction: light and affectionate, with the grief told in an even voice and over in one tear. "Master" does not appear in this chapter, which is fine. Register is American ("pajama", "color", "gotten", "figure out").

## Genesis Score

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | Dramatic irony in the diverting enchantment: "The only exceptions are the originators themselves" is said to an originator (L87). A goddess-familiar eats stale muffins on the kitchen counter, "swinging her heels against the cupboard doors" (L19). A vampire's single tear turns out to be blood (L235). The healing lick (L269–271). | Commercial lane needs 1 fresh element. It has 3, all from the source. |
| Theme | 8.5 | "Wanted for who you are" is acted out, never stated. He offers to release her (L241). She chooses to stay: "Who else is going to teach you blood magic?" (L245). He reframes care as duty: "it's my job to look after you" (L251). Texture is well over 30% non-thematic: Pierre's yawn, the carrot in Verin's bowl, Thistle blowing at him, the potatoes. | None |
| Characters | 8.5 | Cover-the-name passes. Verin's older cadence: "I'm afraid", "Well." / "Not properly, anyway", "if you've any questions for them" (L77, L185). Pierre is half asleep: "She said that part too." / "Don't make me come back up." (L11–13). Amelia teases ("I wouldn't dream of it", L23). Bal is plain and direct ("Nah… Just makes you more interesting"). Chaos for a commercial book: irrelevant thought (potatoes, L101); the body rebels on Amelia's side (the blood tear and the blush, L175, L235); failed management (her shoulders shaking at the briefing, L187). Pierre and Verin each get a moment of their own. | No tic. "Master" is absent. Gesture gate clean. One watch item: the "don't look at Amelia or they'll laugh" beat appears 3× (L89, L183, L187). The gate does not count it. The source has it once, at the briefing (R4). |
| Prose & Voice | **7.5** | Underlines: "He didn't wipe his thumb on anything." (L239, the stopping sentence); "In sixteen years it had not occurred to him that Mrs. Brown had a first name." (L39); "Amelia blushed. Bal hadn't known she could." (L175); "Her fingers were warmer than they had been in the buggy, almost as warm as his own." (L277), which pays off "her cool hand resting in his warm one" (L111) without comment. Rough sentence: "There must be somebody who did the potatoes." (L101). Voice under pressure: the betrayal story drops into short, even sentences ("And I went.", L229). | **CAP 7.5, Pattern #11 hard check:** 4 explanatory extensions in 3,738 words = 1.07/1K, over the commercial 0.8/1K. (a) L31 "Somebody looked after those robes." (b) L89 "He suspected that if he did, he would laugh." (c) L235 "…Bal saw that it was red. It was blood." (d) L263 "It was a strange thing to sit and listen to, so he started talking instead." Borderline, not counted: L15 "which was a skill you picked up in a room full of sleeping boys". Also the L241 quote slip. Without the cap this scores 8.5. |
| Pacing | 8.5 | Six sections of different shape (dorm, office, portal, ride, cottage, bench), and their speeds vary: quick office comedy, slow silent ride, intimate talk, then a still bench. Value shift: leaving home with a hidden goddess → she is fed, at full strength, and chooses to stay. The hook loads the next chapter: "four gods standing on it who expected her place to be empty again" (L279), which matches the outline's "tomorrow the gods". | Verin's briefing (L177–193) is exposition, but it is source content and Amelia's suppressed laughter keeps it alive. 3,738 words against a 3,500 target is fine. |
| Emotion | 8.5 | The outline anchor lands: the wiped tear, and then the smear he keeps (L237–239). Small talk over a bite works in both the kitchen and the stew. Surprise: Amelia shaking with suppressed laughter at "the only time you ever see them" (L187), and the tongue straight after the betrayal story (L247). Body rebel: a blood tear she doesn't choose, and a blush "Bal hadn't known she could". Techniques: physical, humor, subtext (the warmth of her hands), dramatic irony. | Pattern #14 is mild in "Her voice was quiet and very even" (L229). That matches the author's brief grief, so it is not penalized. |
| Engagement (Dim 7, Self-Insertion) | 8.5 | The wish-fulfilment is warm and earned. A goddess asks *permission* to feed. She holds his hand for ten miles. "You." makes her blush. She chooses him over freedom. | None |
| **FLOOR** | **7.5** | | Prose (mechanical cap) |
| **AVERAGE** | **8.4** | | Gap 0.9 |

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8/10 | Brisk start (Pierre to Verin in under 700 words), clean section breaks, a real end hook |
| Tomorrow Test | 3+ anchors → 9 | IMAGE: the blood tear and the smear left on his thumb. IMAGE: crossed fingers behind her back. QUOTE: "Nah. Just makes you more interesting." / "Who else is going to teach you blood magic?" |
| Casual Reader | 8.5/10 | Likes both leads. The feeding scene is sweet rather than scary. Would keep going for the ceremony. |
| Shareability (quote/plot/emotional) | 3/2/3 → 5.7 | Quote: "Just makes you more interesting." Plot: eight high priests died to cage her. Emotional: the blood tear. MAX 6×0.6 + AVG 5.33×0.4 = 5.7 |
| Concept Pitch | yes | An orphan frees a caged vampire goddess, she becomes his familiar, and he takes her to god-run school |
| Human Closeness | yes | Almost all two-person intimacy |

CVI-Launch = 0.2(8)+0.2(9)+0.2(8.5)+0.2(5.7)+0.1(10)+0.1(10) = **8.2**. The Tomorrow-Test +0.5 is not applied, to stay comparable with the Ch.1–4 reports. With it, the figure is 8.7.
CVI-Legacy (default weights) = 0.3(8.5)+0.25(8.5)+0.2(1)+0.15(4)+0.1(4) = **5.9**.

## Anti-AI Scan (20 patterns; commercial clean = 0–8)
1 Forced symmetry: Clear. 2 Empty poetic vocab: Clear. 3 Rule of three: **minor**, 2 (L61 "soap and starch and… ink"; L133 "laugh and tease and turn into a cloud of bats"), both concrete. 4 Em dashes: Clear (0). 5 Empty metaphors: Clear ("spilled flour across a dark table" is concrete). 6 "And" openers: **minor**, 2 (L229 "And I went.", L247 "And she stuck her tongue out at him."). Both are earned. 7 Pseudo-philosophical closings: Clear. 8 Parallelism: Clear. 9 Smooth transitions: Clear. 10 Described emotion: Clear ("eager" is source). 11 Explanatory extension: **FOUND, 4, 1.07/1K (strong)**: L31, L89, L235, L263. 12 Binary negation: Clear. 13 Precision flex: Clear (twelve by eight is source, and it is hedged "if Bal had to guess"). 14 Emotional control demo: **minor**, 1 (L229). 15 Authoritative description: Clear. 16 Philosophical asides: Clear (L15 is borderline). 17 Clean dialogue: **watch**. Exchanges are orderly; Amelia "broke off halfway through a sentence" (L171) is the only break. This is acceptable for the register. 18 Echo chamber: Clear. 19 Graduated reveal: Clear (the shape is journey → bench). 20 Temperature report: Clear.
**Total: 5 patterns → clean for commercial.**

## Character Chaos Check (Bal)
- Irrelevant thought: present (kitchens and potatoes, L101)
- Cognitive distortion: absent (not required)
- Unprompted memory: absent. Not a defect, and there is no fixed cadence.
- Failed emotional management: mild (the laugh "so loudly that Thistle lifted his head", L249)
- Voice under pressure: not tested. This is a low-stakes chapter by design.

## Secondary Character Chaos
- Amelia: has her own moments (lip-biting nerves, the blood tear, the suppressed laughter, the blush)
- Verin: has his own moment (the carrot, the grunt, "Well. Not properly, anyway")
- Pierre: has his own moment (the yawn that makes him start over)
- Mrs. Brown: the hard, quick hug, with Bal "too surprised to finish the job"

## Cross-chapter pattern check
- **Closing image echo:** Ch.4 ends with Bal looking back at the rug beside the bed and the waiting pack. Ch.5 L15 repeats the same look-back at the rug "square beside the third bed". That is two rug look-backs in a row (R6).
- Dialogue polish level is consistent with Ch.1–4. Amelia's teasing register holds.

## The Tomorrow Test
**What the reader remembers:** the red tear, and Bal not wiping his thumb.
**Anchor type:** BOTH. IMAGE: the tear and the crossed fingers. QUOTE: "Just makes you more interesting."
**Verdict:** ANCHOR EXISTS. The type differs from Ch.4's anchors (photo, fist), so there is no repetition.

## Reader Reports
**Devourer:** Moves fast. Might skim the briefing but gets pulled through by Amelia shaking over her stew. The final paragraph's four gods make the next chapter a must. No stopping point.
**Critic:** Underlines the thumb line, the first-name line and the warm-fingers payoff. Notices the over-explained beats: "It was blood.", "Somebody looked after those robes." Trips on L241's two back-to-back quotations.
**Hostile:** Asks why Amelia "went very still" at the originator exception (L89). The joke is unclear and duplicates the briefing gag. Notes that Pierre being "older" is unsupported. Finds "with his other arm halfway up" (L61) confusing, since no arm was up yet. Finds no canon breaks: palm sygl, pain tolerance and brand on the forehead all hold.
**Casual:** Charmed. The muffin-eating goddess, the hand-holding, "Can I feed from you?" asked shyly. Would buy. The tone is cozy.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|---|---|---|---|---|---|
| Pattern #11 extensions | | X | X | | SHOULD FIX (mechanical cap, so it blocks) |
| L241 double-quote slip | X | X | X | | IMPORTANT |
| Laugh-suppression beat ×3 / L89 unclear | | X | X | | SHOULD FIX |
| "Every one of them long" drops the author line | | X | | | INVESTIGATE (source fidelity: fix) |
| Rug look-back repeats Ch.4 close | | X | | | INVESTIGATE |
| L61 "other arm" confusion | | | X | | INVESTIGATE |

## Revision Recommendations (Ranked, surgical, no plot added)

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|----------|-------------|-----------------|-------------|-------------------|--------------|
| R1 | L241 | Style / Logic | `"They chose their path," Bal said. "Now you're free." "I can release you from the bond…` | Two adjacent quotations for one speaker with no tag. This is a formatting error. | Merge: `"They chose their path," Bal said. "Now you're free. I can release you from the bond, if you want. I know being bonded to a mage who hasn't had a single day of training probably isn't what you expected."` | No |
| R2 | L235 | Style (#11) | "…in the window's light Bal saw that it was red. It was blood." | It restates its own reveal. | "…and in the window's light Bal saw that it was blood." | No |
| R3 | L31 | Style (#11) | "…the buttons all matched. Somebody looked after those robes." | It tells what the details already showed. | Cut "Somebody looked after those robes." | No |
| R4 | L89, L183 | Style (#11) / Character / Source | L89 "Bal felt Amelia go very still beside him. He didn't look at her. He suspected that if he did, he would laugh." L183 "Bal kept his eyes off Amelia." | Explains itself, and triples the source's single laugh beat. L183 contradicts the source ("Bal glances sideways at Amelia and grins"). | Cut the whole L89 paragraph. At L183, cut "Bal kept his eyes off Amelia." At L187, make it "Bal glanced sideways at Amelia and grinned. She had her lips pressed…" | No |
| R5 | L215 | Source fidelity (dialogue) | "Almost three thousand years." … "Every one of them long." | Drops the author's memorable flat repetition. | `"Almost three thousand years," Amelia said. "A long three thousand years."` (keep "She was still looking up." if wanted) | No |
| R6 | L263 | Style (#11) | "It was a strange thing to sit and listen to, so he started talking instead." | Explains the motive. The source simply has him listen, then talk. | "He listened to it for a little while. Then he started talking." | No |
| R7 | L15 | Pacing / Continuity | "At the door he glanced back. The rug lay square beside the third bed on the left." | Repeats Ch.4's closing look-back at the rug. | Cut both sentences. Optionally trim "which was a skill you picked up in a room full of sleeping boys" to "He dressed without a sound and shouldered the pack…" | No |
| R8 | L5, L61, L265 | Logic / Canon | "Pierre was older than Bal"; "with his other arm halfway up"; "he had more or less given up on it" | An unsupported invented fact, an impossible "other" arm, and an unclear "it". | L5: "Pierre was another of the orphans, and some mornings he helped Mrs. Brown…". L61: "with his arms halfway up". L265: "given up on school". | No |

### Fix order: R1 → R4 → R8 (logic/source) → R2, R3, R6, R7 (prose) → R5 (dialogue fidelity)

## Strengths to PRESERVE
- The thumb smear and "He didn't wipe his thumb on anything."
- Cool hand in the buggy → "almost as warm as his own" after feeding, left unexplained.
- "Sarah" and the first name Bal never knew.
- The far-side evening light through the portal.
- Pierre's yawn, Verin's carrot, Thistle blowing at him: texture with no agenda.
- The final paragraph's hook into the claiming.

## PATH TO 8.5
- **Prose 7.5 → 8.5 requires:** Pattern #11 at or below 0.8/1K and a clean L241. Apply R2, R3, R4 (L89 cut) and R6. That leaves 0 counted extensions (only the L15 borderline remains, and R7 trims it). Apply R1. Nothing else is needed: the stopping sentence (L239), a rough sentence (L101) and the voice shift in the betrayal story are already present. After these edits Prose re-scores at 8.5 and the floor becomes 8.5.

## VERDICT
**POLISH** (Floor 7.5; Casual 8.5). One editor pass of the eight surgical edits above should clear the gate at 8.5. No new plot or characters, and no change of tone.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
