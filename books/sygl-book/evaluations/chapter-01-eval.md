# Evaluation: Chapter 1 — The Roof and the Flicker
**Evaluator:** book-evaluator | **Date:** 2026-10-20
**Text evaluated:** `manuscript/chapter-01.md` (3,471 words; outline target 3,800). Source span: `Sygl_Complete.txt` L4–L14 (through "Hello?" he asks).
**Lens:** commercial fantasy (harem-romance elements), faithful revise/expand of the author's script. Judged on its own terms: light, warm, playful; fidelity to source is a requirement. Engagement: Self-Insertion 55 / Empathy 35 / Fascination 10 (STATE.yaml).
**Trajectory:** the 2026-06/07 scores (8.5 pass) were for a different, superseded text and were voided by the 2026-10-20 re-plan. This is a first score of the new text, not a regression.

## HEADLINE
**CVI-Launch:** 7.7 | **CVI-Legacy:** 5.9 | **Genesis Floor:** 7.5 | **Genesis Average:** 7.9
**Engagement Type:** Self-Insertion (primary), Empathy (secondary)
**Divergence Alert:** none (Launch 7.7 vs Floor 7.5). Legacy is low, which is normal for the comp lane (Cradle / HWFWM); it is not a revision target.
**Gate:** FAIL the 8.5 gate (POLISH band). Bottlenecks are Pacing (opening order) and Dim 7 Discovery, both fixable by restoring the source's own sentence order, plus a handful of line fixes.

## Mechanical gates (run by evaluator)
- `style_check.py --dir manuscript`: clean. Ch.1 simile 0.6/1k, adverb 10.1/1k, em dash 0.
- `grammar_check.py --file manuscript/chapter-01.md`: clean, 0 errors.
- `tic_report.py --gate` and `voice_wear_check.py`: **could not run on this book.** Both look for `manuscript/chapters/` and report "no chapters found"; the book uses the flat `manuscript/chapter-NN.md` layout (STATE.yaml `manuscript_path`). The tic gate has therefore NOT actually been passed for Ch.1–3 despite STATE saying "gates clean". Manual gesture count below. Pipeline fix needed at the root (accept `--dir`/flat layout), not a chapter issue.
- Manual gesture-class count: heart/pulse check-ins 2 (L69, L109), swallow 1 (L135), grin 1 (L91), laugh 1 (L89), glance/frown 1 each, stump-rub 1 (L15). All under cap 4. "the way" simile: 1 (L35; cap 2).
- Word-level repetition (not gated, but noticeable at reading speed): **warm ×7**, **slate ×9**, **smooth ×5**, **steady/steadily ×5**, **nobody ×6**, solid ×4.
- Dialogue: 66 of 3,471 words (1.9%). Unusual for the genre, but faithful: the source chapter has almost no dialogue before Amelia. Not penalized.

## Genesis Score

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.0 | The stump as a magic channel he deliberately uses "in case a sygl might one day appear there, stump or no stump" (L85); a roof that is solid from outside and absent from inside, entered by bedside rug (L101–103). Commercial needs 1 fresh element: present. | Familiar orphan-school frame and Latinate spell names keep it from 8.5 at chapter level (Ch.2's myth-goddess is the real hook). |
| Theme | 8.0 | Planted without statement: the unclaimed boy ("He had come to Saint Andre's as a baby, and the stump had come with him", L19); Fredrick's "Somebody ought to be reading them who'll use them properly" (L59); "he had always wanted to find his own way of doing things" (L25, source). Plenty of non-thematic texture (pigeons, cabbages, sock on the ceiling). | One told line: "Bal never forgot that he'd been handed more than they had" (L21) nudges toward virtue-labelling. |
| Characters | 8.0 | Bal is vulnerable (no hand, barred from school) and likeable without being a competence cascade; humor is his own ("He'd decided that counted", L67). Fredrick has an independent moment (refusing to sell the books, L59). Chaos 3/4 (irrelevant thought: apple gone brown L39, cheese sandwiches L135; failed management: "couldn't think of anything to do except hold on" L105; triggered memory: Fredrick, L49, returns to scene). Mediated, not inhabited. | Invented quirk for Fredrick ("a habit of humming tunelessly whenever he read", L51) violates the no-invented-quirks rule; mediated chaos holds at 8.0. |
| Prose & Voice | 8.0 | Underlines: "become the second story the staff told about the roof" (L43); "Bal had sat there with the apple halfway to his mouth until it went brown." (L39); "with nothing holding him up but a bedside rug and a second-year spell" (L103); "Bal swallowed, and wished he'd brought a better plan than two cheese sandwiches." (L135). Voice changes under pressure: the flight's polysyndeton run "and he did not look down, and then he did look down" (L97) then clipped "He got hold of himself." (L107). Warm and plain, matches the requested register. | Stock cliché "let out a breath he hadn't known he was holding" (L89); word repetition (warm ×7, steady ×5, smooth ×5); no true close-the-book sentence yet, so held at 8.0. |
| Pacing | 7.5 | Ending hook is strong ("Hello?" after the whisper, L129–137). Value shift clear: alone on a roof → inside a sealed temple with someone there. Good speed variation in the flight. | **The first ~1,100 words are static description** (L5–L25: slates, pigeons, orphanage architecture, golden doors, sygl primer) before "about to attempt something that could kill him" (L27), which then immediately reverses into ~1,000 words of backstory (L31–L69). The source puts the dead boy in sentence 3; the rewrite inserted a sensory paragraph that pushes it to paragraph 3. |
| Emotion | 8.0 | Anchor lands: the carpet rising "a few inches before it stopped and hung there" (L87) and passing through the roof "as though they were mist" (L103). Emotional surprise: gallows humor at the moment of danger (L43, L135). Body rebel: "he laughed, a short surprised sound" (L89). Investment via loss: "he missed him already" (L61). | Fredrick farewell feeling is stated ("It was the kindest thing anyone had done for Bal in a long while", L61) rather than carried by an object/action; holds at 8.0. |
| Dim 7: Discovery / Opening | 7.5 | Bookstore browse (first 3 sentences): MAYBE. Sentences 2–3 are slate tiles and warm sun, no question raised. Amazon first page: SAMPLE (off-limits roof, a dead boy, golden doors nobody can open arrive by page 1's end). BookTok pitch: SHAREABLE/VIRAL for the lane ("a one-handed orphan flies a rug into a sealed temple and finds the vampire goddess everyone calls a myth; he regrows his hand on her blood"). No 2-of-3 negative, so not CRITICAL. | Opening three sentences carry no hook; the source's own third sentence (forbidden roof, a boy died) is the hook and has been displaced. |
| **FLOOR** | **7.5** | | |
| **AVERAGE** | **7.9** | | Pacing and Discovery share the bottleneck; both stem from the same opening-order problem. |

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 7/10 | Chapter is short and ends on a voice in the ear; slow first third. |
| Tomorrow Test | 3 anchors → 9 | IMAGE: rug hanging a few inches up; IMAGE: falling through a roof that isn't there; QUOTE: "Because it's magic." (source line). |
| Casual Reader | 7.5/10 | Likes Bal; would wait for the carpet but may skim pages 1–2. |
| Shareability (quote/plot/emotional) | 2/3/1 → 5.2 | Plot: "the roof isn't there from inside." |
| Concept Pitch | yes (10) | See BookTok above. |
| Human Closeness | partial (5) | Only Fredrick in this chapter; Amelia arrives Ch.2. |
| **CVI-Launch** | **7.2 + 0.5 anchor = 7.7** | |

**CVI-Legacy (default weights):** Originality 8.0×.30 + Theme 8.0×.25 + Cultural vocab 3×.20 ("sygl") + Re-read 4×.15 + Identity 3×.10 = **5.9**. Expected for the lane.

## Anti-AI Scan (20 Patterns) — commercial thresholds (clean 0–8, watch 9–11)
1. Forced symmetry: Found, minor (1; 0.3/1k). "Nobody to stop him. Nobody to see him fall, either" (L75).
2. Empty poetic vocabulary: Clear.
3. Automatic rule of three: **Found, strong (~8; 2.3/1k).** "the wind, a pair of pigeons…, and the small scrape" (L5); "Nobody shouting…, no bell…, no one asking" (L5); "the walls…, the windows…, every staircase" (L9); "Green spirals, blue ripples, little forks of white light" (L19); "A floor of pale stone. A row of tall pillars. The warm orange glow" (L35); "borrowed…, and carried…, and explained" (L43); "a primer…, a thin volume…, a battered guide" (L63); "spread over the paving and climbed the pillars and pooled gold" (L111). Worst fingerprint in the chapter.
4. Em dashes: Clear (0).
5. Empty metaphors: Clear.
6. Dramatic "And" openings: Found, moderate (4; 1.2/1k). L35, L43, L63, L123.
7. Pseudo-philosophical closings: Clear ("It was still something to hope for" is source).
8. Excessive parallelism: Found, minor (2). "had sounded clever until…" ×2 (L47, deliberate comic); "A carpet had edges… A carpet could be sat on." (L47).
9. Overly smooth transitions: Clear (the "It had started a few days earlier" flashback hinge is source-shaped).
10. Described emotions: Found, minor (2). "he missed him already" (L61); "less comforting than he'd hoped" (L75).
11. Explanatory extension: Found, minor (2; under commercial cap of 6). "a small insistent prickle that no amount of rubbing ever quite reached" (L17); "A knot. A cork in a bottle." (L79, restating "blockage").
12. Binary negation opener: Clear (L111 "There was no smoke… no smell of burning wood, either, only…" is borderline).
13. Precision flex: Found, minor (3). "page eighty-one" (L67); "exactly one" ladder (L43); "about a hundred times" (L43). Light and comic, but watch it as a habit.
14. Emotional control demonstration: Found, moderate (3). "He got hold of himself." (L107); "sat there for a long minute… waiting for his heart to come back down" (L109); "His legs were shaky, but they held." (L115). Three notice-manage-continue beats inside ~250 words.
15. Authoritative description: Clear (good gaps: "might have been birds or might have been bats", "a cup or a crescent moon", the statue's face unseen).
16. Philosophical asides: Clear.
17. Clean dialogue: Found, minor. The Fredrick exchange is orderly turn-taking (L55–59).
18. Thematic echo chamber: Clear.
19. Graduated reveal: Found (shape: normal → anomaly → escalate → close on tension). This is the source's shape here; track in Ch.2–3.
20. Emotional temperature report: Found, moderate (4). Heart thudding (L69), stomach (L97), heart (L109), legs (L115).
**Total: 11 patterns present → WATCH band** for commercial fiction. Deductions are mostly minor; #3 and #14/#20 carry the weight.

## Character Chaos Check (Bal)
- Irrelevant thought: present (apple browning L39; cheese sandwiches L135; matrons noticing the rug L119)
- Cognitive distortion: absent
- Unprompted memory: present and properly triggered (Fredrick surfaces through the books and returns to the plan, L49–65). Not a fixed-cadence device yet; watch in Ch.2–3.
- Failed emotional management: present, brief (L105), then managed three times in a row (see #14)
- Voice under pressure: demonstrated (L97 run-on vs L107 clipped)

## Secondary Character Chaos
- Fredrick: has his own moment (refuses to sell the books; "Somebody ought to be reading them who'll use them properly"). Not a prop. But his humming habit is an invented quirk; remove it.

## Source Fidelity Check
All source beats present and in order: roof off-limits / the boy who fell; 1700s, three stories, long lane; mausoleum behind; stump itches; no hand so no sygl; can still do magic, others can do none (L21, matches decision); sygl as guide/affinity; factions; "find his own way"; "could kill him"; flicker a few days ago after lunch; ladder not tall enough, can't jump, so magic; carpet as safest idea; books from a boy who left for a Sygldry school (Fredrick, a friend: matches decisions); self-study only; *Sygldry Year 2*; kneel, left wrist on carpet; *Levimotorcorpus*; blockage in the wrist; "silly but… something to hope for"; gold and sky blue carpet rises a few inches then stops; backpack; cross-legged; faster than expected; no roof; solid concrete; two braziers; statue; *Locos cantis*; Greek temple, open roof, sun; "Because it's magic" whispered; whirls, sees nothing; "Hello?" Spelling: sygl/sygls throughout, mausoleum, no "sigil". Tense past, POV Bal only. Tone warm and playful, as requested.

Contradictions / drift found:
1. **Logic/canon: "A sygl needed a palm to sit in, and he didn't have a palm." (L19).** Bal has a right palm. Canon puts his sygl on the LEFT palm (foundation §0; conversions cut "both left palms"; the chapter itself gives Fredrick his sygl "on his left palm", L51). As written it is false on its face.
2. **Logic (internal): L21 says his magic is weaker "because pushing power out through an arm with nothing at the end of it was a lot of effort"**, but L85 says magic leaves his good right hand "with far less fuss, even without a sygl". The source's reason for weakness is the missing sygl, not the missing hand. L21 should match.
3. **Continuity vs source L228: "Fred, you could sell these. Some of them are barely used." (L57).** The source says the books "were old", and this chapter describes them as dog-eared and "its spine cracked white from use" (L63). Bal's line contradicts both.
4. **Invented quirk:** Fredrick's "habit of humming tunelessly whenever he read" (L51). STYLE_CONSTRAINTS §7 / STATE guardrail: no invented quirks. (His terra sygl, height and being a year older are unsupported but harmless descriptive detail; they do not contradict anything. The quirk is the violation.)
5. **Minor surface:** source says "solid concrete" (kept, L107), but the same floor becomes "pale stone", "paving" and "flagstones" (L35, L111, L123). Pick concrete-and-stone language that doesn't contradict (e.g. "pale stone" once, drop "flagstones").
6. **Housekeeping (not a chapter fault):** outline Ch.1 lists source L4–12 and puts *Locos cantis*/the voice in Ch.2; the chapter now runs to "Hello?" (L14) and Ch.2 opens after it. The two chapters agree with each other; update the outline header so later passes don't double it.
- Pain tolerance, palm placement elsewhere, other orphans without magic, Fredrick a friend, Sygldry as general term: no other contradictions.

## The Tomorrow Test
**What the reader remembers:** the bedside rug hanging a few inches off the slates, steady, and then sinking through a roof that isn't there; and the whisper "Because it's magic."
**Anchor type:** BOTH (image + quote)
**Verdict:** ANCHOR EXISTS

## Shareability
"He flew a bedside rug at a building nobody could open, and the roof just wasn't there." Plot-type. Modest; Ch.2's bats and "They have made me a myth" will carry the book's early shareability.

## Reader Reports
**The Devourer:** Would skim L5–L13 (slates, pigeons, architecture, the crowbar Saturday) and L23 (sygl primer), wake up at "something that could kill him" (L27), sag again through the practice-sock paragraph, then race from L73 to the end. Stays because of the hook and the short length.
**The Critic:** Underlines "become the second story the staff told about the roof" and the brown apple. Winces at "let out a breath he hadn't known he was holding" (L89), the triplet habit, and "warm" seven times. Notes the voice is pleasant but rarely surprising at sentence level.
**The Hostile:** "He didn't have a palm" — yes he does, he has a right hand (L19). Why is his magic weak "because of the arm" if the right hand works fine (L21 vs L85)? Why are dog-eared, spine-cracked books "barely used" (L57 vs L63)? Concrete or flagstones? Also: "A month ago he wouldn't have known where to begin" (L49) sits oddly beside his having mastered first-year levitation alone "in the spring" (L67).
**The Casual Reader:** Likes Bal immediately (the stump, the hope, the jokes). Page 1 is a nice day on a roof; would want something to happen sooner. Keeps going once the carpet lifts; the whisper ending sells Chapter 2. Score 7.5: would probably buy, not instantly.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|-------|----------|--------|---------|--------|----------|
| Slow, static first ~1,100 words / hook displaced | X | | | X | SHOULD FIX (Casual-flagged → treat as IMPORTANT) |
| Logic slips (palm, arm-vs-hand, "barely used") | | X | X | | SHOULD FIX |
| Cliché breath line + triplets + word repetition | | X | | | INVESTIGATE |
| Invented quirk (humming) | | X | X | | SHOULD FIX (project rule) |
| Three successive "got hold of himself" beats | X | X | | | SHOULD FIX |

## Revision Recommendations (Ranked)
All fixes are trims, reorders or rewordings of existing material. No new plot, characters, subplots or darker tone.

| Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|----------|-------------|-----------------|-------------|-------------------|--------------|
| L19 | Logic | "A sygl needed a palm to sit in, and he didn't have a palm." | False: he has a right palm; canon sygl is on the left palm. | Replace with: "A sygl came up in the left palm, and he didn't have a left palm." | Yes (palm = left palm, everywhere) |
| L21 | Logic | "It was not as strong as it would have been with a sygl, because pushing power out through an arm with nothing at the end of it was a lot of effort for a little result" | Contradicts L85 (right hand works easily) and the source (weakness = no sygl). | Cut the "because…" clause: "It was not as strong as it would have been with a sygl, but it was there, and it was his." Keep the arm-effort idea only at L79/L85 where it belongs to the stump specifically. | No |
| L57 | Continuity | "Fred, you could sell these. Some of them are barely used." | Contradicts source "the books… were old" and L63 "spine cracked white from use". | "Fred, you could sell these." (cut the second sentence) or "Fred, you could get something for these." | No |
| L51 | Character (invented quirk) | "with a terra sygl on his left palm and a habit of humming tunelessly whenever he read" | Invented quirk; violates no-quirks/no-tics law. | Cut "and a habit of humming tunelessly whenever he read". Keep the left-palm sygl (it usefully establishes palm placement). | Yes |
| L3–L7 | Pacing / Discovery | Sentence 1 (source), then a full sensory paragraph (L5: slates, sun, breeze, pigeons, scrape), then the off-limits/dead boy at L7. | The source's sentence 3 is the hook ("off limits, a boy had fallen off the roof… and died, but that never stopped Balthazaar"); the rewrite buries it. Bookstore browse scores MAYBE. | Restore source order: L3, then L7 ("None of the other children ever came up… It had never stopped him."), THEN a trimmed L5. Cut L5 to two sentences (keep the warm slate and "From up here the noise of the building fell away"; drop the triple "Nobody shouting…, no bell…, no one asking" or keep only one of them). | Yes (open on the source's own hook sentence) |
| L9, L13 | Pacing | Orphanage architecture triplet (walls/windows/staircase), delivery van/visitors; door-forcing catalogue (pushed/pulled/kicked, keyhole, charms, crowbar Saturday). | ~350 words of static setting before anything is at stake. | L9: keep "quite old… 1700s… decent shape… three stories… long lane that no one ever came down"; cut the walls/windows/staircase triplet and the van/visitors pair. L13: keep "tall and golden… impossible to open" and the crowbar Saturday (it's funny and pays off at L43); cut "hunted for a keyhole… library book". Net ~-120 words. | No |
| L5 opening line idea | Pacing | The rug Bal will fly is not seen until L73. | The reader has no object to hold through 1,100 words of setup. | In the trimmed L5, put the rolled bedside rug beside him on the slates (no new event: the source has him on the roof that day "about to attempt" it). One clause: "the bedside rug rolled under his arm". Then L27's "about to attempt something that could kill him" pays off an object the reader has been looking at. | No |
| L89 | Style (cliché) | "Bal let out a breath he hadn't known he was holding." | One of the most recognised stock lines in genre fiction; costs Prose credibility on the chapter's key beat. | "Bal breathed out. Then he laughed, a short surprised sound…" or fold into the laugh: "Bal laughed, a short surprised sound…" | Yes (ban the phrase book-wide) |
| L105–L115 | Style (#14/#20) | "He got hold of himself." / "sat there for a long minute… waiting for his heart to come back down" / "His legs were shaky, but they held." | Three notice→manage→recover beats in ~250 words; the landing feels managed rather than felt. | Keep "He got hold of himself." Cut L109 entirely (the long minute adds nothing after the bump). Change L115 to "Bal got to his feet." (drop "His legs were shaky, but they held."). | No |
| Whole chapter | Style (repetition) | warm ×7, slate ×9, smooth ×5, steady/steadily ×5, nobody ×6. | Audible at reading speed; flattens the temple arrival, where warmth matters most. | Keep "warm" at L5 and L111 ("soft, warm light") only; vary/cut at L79 ("The wool was warm from the sun"→"sun-hot"), L35 "warm orange glow"→"orange glow", L111 "faint warm scent"→"faint scent of something spiced", "pleasantly warm"→cut. "steady": keep L87, change L79 "low steady current"→"low current", L69 "steady as a table"→keep, L111 "low and steady"→"low", L133 "burning steadily"→"burning". | No |
| L3–L69 triplets | Style (#3) | ~8 automatic triplets (listed in scan). | Strongest machine-rhythm fingerprint here. | Break at least four: L5 (cut one of the three "no" items), L9 (cut; see above), L35 keep (it's the flicker, earns it), L63 reduce the book list to two plus *Sygldry Year 2*, L111 "spread over the paving and climbed the pillars and pooled gold" → "pooled gold in the hollows of the stone". | No |
| L49 | Logic (minor) | "A month ago he wouldn't have known where to begin. Then Fredrick left." | Sits oddly next to L67 (he mastered first-year levitation alone in spring). | "A month ago he wouldn't have had the spell. Then Fredrick left." | No |
| L61 | Emotion | "It was the kindest thing anyone had done for Bal in a long while, and he missed him already." | States the feeling the scene has already shown. | Keep the first clause (the voice owns it); replace "and he missed him already" with an existing object: "The garden string was still on the end of his bed." (string already established at L53; no new event). | No |
| L35/L107/L111/L123 | Continuity (minor) | Floor is concrete (source) then paving, flagstones. | Small inconsistency. | Keep "solid concrete" (L107, source). L123 "lay over the flagstones" → "lay over the floor"; L111 "spread over the paving" → cut (see triplet fix). | No |
| L21 | Theme (minor) | "Bal never forgot that he'd been handed more than they had." | Labels his virtue. | Cut the sentence; "they got on with their lives the same as anybody" already does the work. | No |

### Fix order: Logic/Character (L19, L21, L57, L51, L49) → Structural (L3–L13 reorder/trim, rug in L5) → Connective (L105–115) → Prose (L89, repetition, triplets, L61) → Factual (floor material, outline header).

Net word effect: about -250 to -300 words, taking the chapter to ~3,200. That is inside the outline's 1,300–5,000 band; the book total is what is enforced. If words must be kept, spend them in the temple arrival (L111–L127), which is the payoff and is currently the shortest-feeling section, using only source details (braziers, statue, Greek pillars, open roof, sun) at closer range. Do not add events.

## Strengths to PRESERVE
- The comic-dread voice: "become the second story the staff told about the roof" (L43); "He'd decided that counted." (L67); "wished he'd brought a better plan than two cheese sandwiches" (L135).
- The brown apple (L39): the best single image of the flicker.
- The sock/pillow/book/chair/rug practice ladder (L69) is earned expansion, faithful to "self study".
- The flight paragraph (L97) and "a bedside rug and a second-year spell" (L103).
- All source dialogue and spell words kept verbatim; the ending on "Hello?" matches the source exactly.
- Zero em dashes, clean grammar, POV discipline, correct spelling.

## PATH TO 8.5
- **Pacing 7.5 → 8.5 requires:** the hook in the first three sentences and an object in hand from page 1. Surgery: reorder L3/L5/L7 to the source's order (dead boy in sentence 3), plant the rolled rug in the trimmed L5, cut ~120 words of static architecture/door catalogue from L9/L13, cut L109. Test: the first "something is about to happen" signal should arrive within 150 words, not 1,100.
- **Dim 7 Discovery 7.5 → 8.5 requires:** Bookstore browse moving from MAYBE to BUY. That is the same L3–L7 reorder: "The roof… was the one place Balthazaar could go when he needed to be away from everyone. None of the other children ever came up. The roof was off limits, and had been since a boy fell from it a few years back and died." Three sentences, three questions (why away? why forbidden? why does he go anyway?). All source.
- **Prose 8.0 → 8.5 requires:** removing the stock breath line (L89), the four repetition clusters, and four automatic triplets; and one sentence that stops the reader. The best candidate already exists: sharpen L103's last clause so it ends the paragraph on the image: "He was inside it, high in the air above a stone floor, held up by a bedside rug and a second-year spell." Pair it with the clean L101 (source) for a one-two the Critic will underline.
- **Characters 8.0 → 8.5 requires:** cut Fredrick's invented humming (L51); let Bal's fear during landing be inhabited rather than managed (cut L109 and "His legs were shaky, but they held" so the prose stops reporting recovery).
- **Emotion 8.0 → 8.5 requires:** Fredrick's farewell carried by the garden string (L53→L61) instead of "he missed him already".
- **Originality / Theme 8.0:** will rise with the chapter's sharpened opening; no new material should be added for them (fidelity rule).

## VERDICT
**POLISH.** Genesis Floor 7.5 / Average 7.9; Casual 7.5. Above any hard floor, below the 8.5 gate. Every fix above is a trim, reorder or rewording of existing source-faithful material.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

## Revision applied (book-editor, 2026-10-20)
- Opening restored to source order: roof, off-limits, the boy who died in sentences 2–3; the rolled bedside rug now sits beside Bal on page 1. Slate/pigeon paragraph trimmed; walls/windows/staircase triplet, van/visitors and door catalogue (keyhole, charms) cut.
- Logic: "A sygl came up in the left palm, and he didn't have a left palm"; weak-magic "because… arm" clause cut; "barely used" cut (books now "old but a good lot"); "A month ago he wouldn't have had the spell."
- Fredrick's humming quirk cut; "handed more than they had" cut; "missed him already" replaced by the garden string still on the bed.
- "breath he hadn't known he was holding" → "Bal breathed out."; recovery minute (L109) and "legs were shaky" cut.
- Repetition thinned (warm 7→2, steady 5→2, smooth 5→0, slate 9→4); triplets broken at sygl colors, book list, braziers' light; "A knot. A cork in a bottle." cut; floor "flagstones/paving" removed; And-openers cut.
- American register: torch→flashlight, trousers→pants.
- Gates: style, grammar, voice_wear, tic_report --gate all clean (scratch layout). 3,206 words; em-dashes 0; "the way" 1.
