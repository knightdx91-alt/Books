# Evaluation: Chapter 7 — The Blood Dorm
**Evaluator:** book-evaluator | **Date:** 2026-10-20 | **Draft:** R1 (3,672 words vs 3,600 target)

## HEADLINE
**CVI-Launch:** 8.7 (8.2 + 0.5 strong-anchor bonus) | **CVI-Legacy:** 6.0 | **Genesis Floor:** 8.5 | **Genesis Average:** 8.5
**Engagement Type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence Alert:** none. Launch sits above Legacy, as expected for a warm commercial fantasy. Ch.6 had the same profile.

**VERDICT: PASS** (Floor 8.5, Casual 8.5). Below are five small line fixes (F1–F5) and two optional ones. F1 and F2 should go in before commit. None of them adds plot, and none needs re-scoring.

---

## Mechanical gates (scratch copy: ch.1–7 in `manuscript/chapters/`)
- `voice_wear_check.py`: **clean.** No retired phrases and no device over cap. The one self-repetition warning is informational.
- `tic_report.py --gate`: **clean.** No auto-recurrence. Ch.7 gesture classes are all under cap: shrug ×2 (both from the source), nod 0, head-shake 0. Negation pivots 0, and-chains 0.
- `style_check.py --dir`: **clean.** Simile 3.5/1k (cap 4), adverb 11.4/1k, **em-dash 0**, no distinctive cross-chapter repeated phrase. The informational repeat "a soft pop" also appears in Ch.5 and is not gated.
- `grammar_check.py --file`: 0 errors.
- Filter words: "just" ×5. Four are in dialogue, and three of those are the source's own Viridia line (L153). "really" ×1 is in dialogue. "began to" ×1 (L103, from the source).
- "the way [x]" similes: 0.

## Source fidelity (L304–325, "Anything special…" to the hostile stares)
- **Handoff.** The chapter opens at the pedestal, which is the outline's Opening. It does not repeat Ch.6's "Anything special / We'll talk more about it tonight." Correct.
- **Every beat is present, in order:** the pin-prick on the **left palm** and the blood drawing the sygl; the sliding wall and steps; no set rooms; "Lead Mage, which is you, or a High Priest, which is also you"; the couch; "Will we get more students?" / "once word gets out I'm back"; the official stuff (route, four classes, curfew exemption, library, make friends, "you like secrets right?… I'll reward you", "I can't wait" / "Me either", push magyk into the sygl); the hug and snap; the exploration (fireplace, couch, wing-backed chair, coffee table, bathroom, bedroom twice the size, five-person four-poster, dark rose on black, the chest); three doors on a thought; the kitchen (stove, two chests, spices, meat and vegetables); the library (smaller, empty shelves, five chairs, a fireplace, his disappointment); the mahogany dining room; kitchen and dining combined; made permanent; hunger; the courtyard grouped by sygl with a few brave mixers; "Hey you're that Blood guy right?"; the crackling pale-blue hair; the inheritance speech; the red carpet; the handshake; "years of hate"; "the elite of a class"; "petty politics… stupid"; "people just like us"; **"I'm not like most people"** (once); the hair joke and **the tongue** (once); the tables with their sygls; "Did you want to eat alone?" / "Not particularly"; the paper ordering; the pizza and the burger; the stolen slice and the grease; the forest rule; "You've already got a familiar"; "Mine's a special case"; "a Wolf or something?"; **"No, it's me"**; the choking and the water; the bangs and the brand; "technically a magical creature"; "what could he have that you'd want?"; "Don't ruin the good impression"; **"You'd be surprised"** (kept here); Bal changes the subject; "a beautiful vampire familiar" / "You think I'm beautiful?" / "I'd die to have skin like yours"; **"Okay, you can keep her"**; "What did she mean… you can keep me?" / "Honestly? I have no idea."; Viridia leaves; the hostile stares with no one bothering him.
- **Author decisions honoured.** Bal recognises Viridia from the buggy in one line plus a callback to the Ch.6 sweater question (L111). That is acceptable, because it answers a question Ch.6 raised. The tongue appears once. The sygl is on the palm, and the brand "matching the one in Bal's hand" is consistent.
- **Dialogue rule.** Every line keeps its speaker, meaning and position. The polish reads as natural American speech: "There going to have" becomes "They're all going to have", "Would could a mortal offer" becomes "What could a mortal offer", "suprised" becomes "surprised". One addition, "Bal," as a self-introduction (L141), is natural and adds no information. **"Master"** is used once (L271). That is allowed under the ruling and natural for a familiar, and it is not built into a joke.
- **Tone.** Light, warm and playful. Amelia is confident and teasing, and her protective flash is quick and then gone. Viridia is frank, funny and unimpressed by the gods. Bal speaks plainly. Nothing is darkened and no subplot is added.
- **Added texture, none of it plot:** the pack in the empty chest; the sneeze at the spice jar; the carrots with dirt on them; "Passing the salt would take a long arm"; the dirty-plates thought; the burned roof of the mouth; the Waves boy with his fork in the air; the Terra boy and the older boy on the walk back (this expands the source's "hostile stares"); the pedestal bookend. **One invented personal detail:** "Bal's cooking had never gone past toast" (L97). It is small, but it is a skill/backstory addition the source does not make (optional fix F7).
- **One fidelity/logic slip:** "The library's one floor up," said with a tip of the head toward the ceiling (L51). The source says "the second floor", meaning the school's. The dorm sits at the end of a corridor reached by going *down* stairs, so "one floor up" from the dorm is neither the source nor necessarily true (F2).

## Genesis Score

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | The dorm that answers a thought is source-given (a Hostile reader will think "Room of Requirement"). The execution is what's fresh: "as though they had always stood there and he had only now thought to look" (L83); the kitchen merge, "The wall between them went soft at the edges and was simply not there anymore" (L97); Viridia's deadpan vampire compliment played as a staring contest (L263–265) | none (commercial: 1 fresh element) |
| Theme | 8.5 | Outsiders finding each other, embodied and never stated. "The Blood table was the last of the five, nearest the back wall. It was empty." (L177), then Viridia sits at it. The orphan's room: "the whole of what he owned with room to spare all around it" (L73) | none |
| Characters | 8.5 | Viridia: "I'm Viridia Vizer. Heir of Raizen." / "Nah. They're people just like us." / "Of course… I'd die to have skin like yours." Amelia: the menace in "her red eyes were perfectly level" (L231), then "Amelia's mouth twitched first" (L265). Bal: "Bal only blinked at her." (L135); "Bal couldn't quite keep the smirk off his face." (L207) | No tics. Chaos 3/4 inhabited: irrelevant thought (the plates, L189; the spice sneeze, L87); a triggered memory that returns to the scene (twenty boys, L67; the orphanage cook, L199); failed management (the smirk; the burned mouth from eating too fast). Cover-the-name test passes for Viridia and Amelia |
| Prose & Voice | 8.5 | Stopping sentence: "He lowered the pack in, and it sat at the bottom looking very small, the whole of what he owned with room to spare all around it." (L73). Underlines: "Bal laughed out loud, alone, in his own kitchen." (L99); "the look of doors that were going to be there tomorrow" (L103); "Somebody had to do it. Somebody always did." (L189); "Passing the salt would take a long arm." (L93). Ugly sentence: "The kitchen had a stove in it and food in it, which was what kitchens were supposed to have, and he stood there pleased with it anyway." (L87) | #11 at 1 instance (0.3/1k), under cap. Voice under pressure is only lightly tested (Amelia's flash): the prose shortens ("Amelia stopped chewing."), which is enough for this register |
| Pacing | 8.5 | Three movements at different speeds: the brisk official list; the slow, sensory exploration; the quick-fire lunch banter with the choke as a jolt. Value shift: alone and unclaimed by the crowd ("has nobody tried to talk to you yet?" / "Nobody.") to a friend made, then a cooler walk back under stares | The hook is soft by outline design (the bookended prick, L291). The exploration runs about 1,100 words with no second person present, carried by wonder and the pack beat |
| Emotion | 8.5 | Anchor: the pack in the empty chest; "you can keep her." Surprise: the menace beat broken by a deadpan compliment that makes a goddess laugh hard enough to turn half the hall (L265). Body rebel: Viridia's choke and streaming eyes (L213–215); Bal's burned mouth (L199) | none. No intensity-words carry the peak; objects and actions do |
| Engagement (Dim 7) | 8.5 | Self-insertion wish-fulfilment lands: a private dorm that builds itself, a vampire goddess as a familiar, and the first friend's jaw dropping ("I hope I get to see your face when you meet my familiar", L207, paid off at L211). Empathy carries through the orphan details | none |
| **FLOOR** | **8.5** | | |
| **AVERAGE** | **8.5** | | |

Trajectory: Ch.1–6 each 8.5. Ch.7 holds 8.5 with no regression. Its prose high is the strongest underline set since Ch.6.

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8.0 | Lunch is a page-turner. The room tour is pleasant but leisurely for a Devourer |
| Tomorrow Test | 3+ anchors → 9 | IMAGE: the pack sitting small in the cedar chest. QUOTE: "Okay, you can keep her." QUOTE: "I'd die to have skin like yours." IMAGE: Viridia choking when Amelia pops in |
| Casual Reader | 8.5 | Cozy-magic-school comfort plus a funny new friend. Easy to like |
| Shareability (quote/plot/emotional) | 3/3/2 → 5.7 | Quote: "I'd die to have skin like yours." Plot: "his familiar is the goddess and she just pops in at lunch" |
| Concept Pitch | yes (10) | |
| Human Closeness | yes (10) | Friendship-making and familiar intimacy make up most of the chapter |
| Raw | 8.2 | +0.5 strong anchor = **8.7** |

CVI-Legacy: Orig 8.5×.3 + Theme 8.5×.25 + Vocab 2×.2 + Reread 4×.15 + Identity 3×.1 = **6.0** (Ch.6: 6.0).

## Anti-AI Scan (20 patterns; commercial clean threshold 0–8)
1 Forced symmetry: minor. "Waves with Waves, Terra with Terra" (L105). 0.3/1k
2 Empty poetic vocab: clear
3 Rule of three: minor. "the five chairs, and the empty hearth, and the long bare shelves" (L91); the door roll-call (L101). 0.5/1k
4 Em dashes: clear (0)
5 Empty metaphors: clear
6 Dramatic "And": "And lastly." (L55) is in dialogue. Clear
7 Pseudo-philosophical closing: clear. "Somebody always did" is character-specific (an orphan's thought), not coffee-mug
8 Excessive parallelism: minor. "No one said anything. No one bothered him." (L285, a source beat)
9 Smooth transitions: clear (scene breaks do the work)
10 Described emotions: minor. "He was a little disappointed." (L91, source wording)
11 Explanatory extension: 1. "as though they had always stood there and he had only now thought to look" (L83). 0.3/1k, under cap
12 Binary negation opener: clear
13 Precision flex: clear ("twenty other boys" is texture)
14 Emotional control demo: clear
15 Authoritative description: clear. Bal is wrong about the crackle ("not the sweater", L111) and unsure about the doors ("He couldn't have said what changed")
16 Philosophical asides: clear
17 Clean dialogue: minor. The lunch exchange is mostly turn-based, but the choke, the frozen stare and the fork-in-air Waves boy break it
18 Thematic echo chamber: clear (the spices, the carrot dirt, the plates are pure texture)
19 Graduated reveal: clear (exploration, then meeting; different from Ch.6's ceremony)
20 Temperature report: clear

**Total: 6 patterns present, all minor → clean (commercial).** The deduction is already reflected in the scores.

## Character Chaos Check (Bal)
- Irrelevant thought: present (the plates, L189; the spice sneeze)
- Cognitive distortion: absent (not required)
- Unprompted memory: present, triggered and returning (twenty boys → the bedroom; the orphanage cook → the pizza). It is not a fixed-cadence paragraph
- Failed emotional management: present (the smirk he can't hide; eating too fast)
- Voice under pressure: lightly tested (Amelia's flash). Sentences shorten

## Secondary Character Chaos
- **Viridia:** has her own moments (the choke; her blush and both hands waving at "I didn't mean it like that"; the deadpan she holds without blinking). A person, not a prop.
- **Amelia:** her own beat at "Amelia studied the pizza. 'You'd be surprised'" (L245). This is the source's private note, rendered without explanation.

## The Tomorrow Test
**What the reader remembers:** the boy's whole life sitting small at the bottom of a cedar chest; Viridia telling a vampire "I'd die to have skin like yours" and the goddess laughing until the hall turns around.
**Anchor type:** BOTH. Image anchors match the book's pattern of object-based anchors, but the type is varied by the quote anchor. **ANCHOR EXISTS.**

**Shareability:** "His familiar is the Blood goddess, and she pops in at lunch and steals his pizza."

## Reader Reports
**The Devourer:** Races through the official list and the lunch. Might skim the kitchen/library/dining tour (L85–103), but the instant rooms are fun enough. Would turn the page at the end. Stop risk: low.
**The Critic:** Underlines L73, L99, L103, L189. Notes one awkward pronoun (L107 "the front of it", F1) and an echoed "red on grey" (L13, F3). Notes "Room of Requirement" familiarity but accepts it as source.
**The Hostile:** "One floor up" when the dorm was reached by going down (F2). "Bal glanced at his own front" repeats Ch.6 L13's "Bal checked his own front" (F1). Would also ask why Viridia doesn't react to "Master". She is mid-laugh and still stunned, so it is acceptable.
**The Casual Reader:** Loves the cozy magic dorm, the pizza on a magic plate and the friend who sasses a goddess. Would keep reading: 8.5.
**The Devoted Reader (SFF):** Will catalogue the dorm rules (Lead Mage/High Priest permanence, the blood-key pedestal, paper ordering "after today any paper"). Re-read value: "You'd be surprised" gains weight later.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| "his own front" pronoun and cross-chapter echo (L107) | | x | x | | | SHOULD FIX |
| Library "one floor up" vs source "second floor" (L51) | | | x | | x | INVESTIGATE (fix: it is a source/logic slip) |
| Room tour slightly long | x | | | | | INVESTIGATE (keep) |
| "red on grey" doubled (L13) | | x | | | | INVESTIGATE |

## Revision Recommendations (Ranked; surgical, no plot added)

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|---|---|---|---|---|---|
| F1 | L107 | Style / Continuity | "Bal glanced at his own front. The blood sygl had come up on the front of it at some point during the claiming…" | "it" has no antecedent ("front… front of it"). It also echoes Ch.6 L13 "Bal checked his own front" | → "Bal glanced down at his sweater. The blood sygl had come up on the front of it at some point during the claiming…" | No |
| F2 | L51 | Logic / Source | "She tipped her head toward the ceiling. "The library's one floor up, because…"" | The source says "on the second floor" (the school's). The dorm is reached by going down, so "one floor up" from the dorm is unsupported | → delete "She tipped her head toward the ceiling." and make the line "The library's on the second floor, because I'm sure you're going to go hunting for it." | No |
| F3 | L13 | Style | "…until the whole sygl stood out red on the grey, the same shape as the one under his hand. It held there, red on grey. Then it sank…" | "red on grey" twice in two sentences reads as an accidental echo | → cut "It held there, red on grey." | No |
| F4 | L221 | Style (dialogue) | "What does that even mean?" … then "But how is that even possible?" | "even" twice in consecutive Viridia lines | → "But how is that possible?" | No |
| F5 | L283 | Style | "They stayed and talked a while longer…" (L277) … "Bal stayed at the empty table a while." | stayed/a while repeated within a few lines | → "Bal sat on at the empty table for a minute. Then he headed back to his dorm." | No |
| F6 (optional) | L153 | Style (dialogue) | "They're people just like us. They've got faults just like us. They just live longer…" | Three "just"s; source polish is allowed | → "They're people just like us. They've got faults like us. They just live longer than the rest of us." | No |
| F7 (optional) | L97 | Character (invention) | "But Bal's cooking had never gone past toast, and somewhere in this castle…" | A small invented skill/backstory fact (the source only says he chose not to cook) | → "But somewhere in this castle there was a dining hall, and he was curious to find it." | No |

### Fix order: F2 (logic/source) → F1 → F3–F5 → optional F6, F7

## Strengths to PRESERVE
- The pack in the cedar chest (L73), the emotional core of the exploration. Do not trim it.
- "Bal laughed out loud, alone, in his own kitchen." and the "doors that were going to be there tomorrow" passage.
- The staging of the menace-to-laugh turn (L229–267): "Amelia stopped chewing.", the level red eyes, the blush and waving hands, the held deadpan stare, "Amelia's mouth twitched first."
- The one-line buggy recognition with the sweater callback (L111).
- The pedestal bookend ending (L291), which hands off cleanly to Ch.8's couch scene without pre-empting it.

## PATH TO 8.5
Not required (Floor 8.5). To hold 8.5 through Ch.8, do not reuse the menace-then-laugh beat shape for Amelia's "I like her too" scene, and stage Ch.8's Viridia callback differently from this choke (the outline already notes this for a later chapter).

## VERDICT
**PASS** (Genesis Floor 8.5, Average 8.5, Casual 8.5). Apply F1–F5 before commit. All gates are clean.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
