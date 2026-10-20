# Evaluation: Chapter 9 — The Familiar Class
**Evaluator:** book-evaluator | **Date:** 2026-10-20 | **Draft:** R1 (3,513 words of text; target 3,400)

## HEADLINE
**CVI-Launch:** 8.7 (8.2 plus 0.5 for a strong anchor) | **CVI-Legacy:** 6.0 | **Genesis Floor:** 8.5 | **Genesis Average:** 8.5
**Engagement type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence alert:** none. Launch is above Legacy, the same profile as Ch.6–8.

**VERDICT: PASS** (Floor 8.5, Casual 9.0). This is the book's best comic set piece so far. Five small surgical fixes follow (F1–F5). F1 and F2 should go in before commit. None of them adds plot, and none needs re-scoring.

---

## Mechanical gates
Run on a scratch copy of Ch.1–9 in `manuscript/chapters/`.
- `voice_wear_check.py`: **clean.** No retired phrases, no device over its cap, no strict self-repetition.
- `tic_report.py --gate`: **clean.** No auto-recurrence. Ch.9 rhythm: and-chains 0, negation pivots 0, "So" openers 0. No gesture class reaches its cap in Ch.9, and none is rising across the book.
- `style_check.py --dir`: **clean.** Simile density 2.0/1k, adverbs 6.5/1k (the book's lowest), em dashes 0. There is no distinctive cross-chapter repeated phrase. "and cold and every" (Ch.2 L75 / Ch.9 L136) is generic and informational only.
- `grammar_check.py --file`: 0 errors.
- "the way [x]": 0. "as if / as though": 1 (L224).
- **"Master"** appears 3 times (L124, L148, L170). All three are the source's own lines, in the source's places, and no joke is built on repeating the word. Allowed.
- Filter words: none of just / seemed / really / slightly / suddenly / visibly. "nodded" / "shrugged" / "grinned": 0.

## Source fidelity (L341–362: "The next morning after eating a hearty breakfast" to "Bal was almost glad when it became time for lunch.")
- **Every beat is present, in source order:** the breakfast of eggs, bacon, toast and oatmeal; all classes shared except Rune working; the walk to the back of the school; "Not seeing Amelia, Viridia asked"; Bal's account of why Amelia is away, and "I prefer handling my own problems"; "I get that"; the classroom on the far right with an outside door (and the reason for it); twenty desks in rows of five; Mr. Porter's name on the board; the back-corner desks; Porter feeding cheese to a large raven; his fifties, balding grey hair, tweed, glasses catching the light from the two windows onto the forest; "Why do you need a familiar?"; nobody answers; the lecture (companionship, carrying load, messages, could save your life, Huginn, close to fifteen years, saved his life twice, a different perspective); "not leave this class"; Tyler's question; "I misspoke … the forest"; how bonding works; "There must be balance"; the silver rings; the chatter and the throat-clear; what the rings do; "Students have died in there"; Bal sets his ring down and raises his hand; Porter's narrowed eyes; the question; Viridia's anticipation; Porter's anger; "rules do not apply to you"; "a rodent perhaps? or a toad?"; Bal's laugh; "Show us your mastery"; the palm raised, the push through the sygl; **Amelia on the desk, legs crossed, brand on her forehead, "You called, Master?"**; Viridia doubled over at Porter's pale face; "Lady Amelia"; the students scattering; "What are you doing here?"; the slow turn and "Are you implying that I need permission from you to go anywhere I wish?"; Porter sweating and waving his hands; "grace us with your presence"; "This is the familiar class, is it not?"; "My Master called for me, so I came"; "But you're… and he's a…"; Amelia strolling up to him; "Think your next words through very carefully"; Bal stepping in (someone/hurt, Porter/killed); no honorific; "Okay, Master!" with a smile, a wave and a vanish; everyone breathes out except the two of them; the wary looks; "across the castle by dinner"; Porter's stammered instructions; the outside door; "don't come back until you've bonded something"; Viridia's whisper about Warfare; Huginn sent after the class; "Ahm… uhm", the excusal and "welcome to stay"; "I'd like to stay… after today at least"; the library request; the directions (second floor, right, second door on the left); curiosity plus a plan to help her revenge, "besides converting followers"; doing the research himself; the librarian; the Naisura–Kenmei war and the command tent sealed in stone and buried; very little on Amelia; she doesn't play by their rules; pieces on a game board, everyone expendable but themselves; Bal had looked up to the originators; "made Bal sick"; the clock; books set aside; the detour for the rune kit; Mr. Winters, short and skinny; the purpose of the class; copying the runes he didn't know; the compliment on the avoidance rune, essential for night travel in unfriendly territory; "almost glad… Almost because he enjoyed learning the new runes."
- **Dialogue rule is honoured.** Every line keeps its speaker, meaning and position. The polish is natural and American: Tyler's reported question becomes "We can't leave the class? Like, ever?"; "until you have bonded" becomes "before you have bonded"; "I was just curious what got you to grace us" becomes "I was only curious what led you to grace us… that's all"; "Ahm.. uhm" becomes "Ah. Um." The source's reported lines ("don't come back until…", "see you in Warfare") are turned into short direct speech without changing their meaning.
- **Additions, all texture and none of it plot:** the paper borrowed at breakfast (it follows Ch.7 L185's ordering rule); the schedule comparison; "Did ravens even like cheese?"; the cheese in wax paper; "Twenty faces, and Huginn's"; Tyler behind his chair; Huginn going still; the dog that turned out to be a bear; the spare ring left on the desk; the librarian's pencils; the brass catch on the kit. The thought linking the buried tent to the temple Naisura's high priest built (L222) is inferred from Ch.5 L227 and adds no lore. Two additions are worth questioning: F1 (the buried-tent image is darker than the chapter) and F2 (Viridia's Rune working "this afternoon" is new information that clashes with the schedule).
- **The opening (breakfast, not Huginn) is the right call.** The source opens on breakfast ("The next morning after eating a hearty breakfast… with Viridia"), and Ch.8 closes on "a bell… waiting for morning". Opening on that morning picks up the thread with no seam, and it is what "more like my original script" asks for. The outline's "Opening: Huginn and the cheese" was a ledger choice, not a source requirement, and Huginn still gets a strong first entrance at L46–50. **The outline ledger should be updated** to "Opening: breakfast with Viridia (borrowed paper)" so the Anti-Predictability Ledger stays accurate. The only cost is about 550 words before the classroom; F5 covers it.

## Genesis Score

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | A summoned goddess sits cross-legged on a schoolboy's desk to answer a teacher's "a rodent, perhaps? Or a toad?" The execution adds fresh comic angles: "Twenty faces, and Huginn's." (L114); "Up front, Huginn opened his beak, shut it again, and stood perfectly still." (L132); "the kind of looks you might send a dog that had turned out to be a bear" (L174) | none (commercial: 1+ fresh element) |
| Theme | 8.5 | Belonging and the gods' indifference, carried by the source's library beat without being stated: "The originators looked at their followers as pieces on a game board… Everyone's life could be spent except their own." (L226); "He had wanted one so badly." (L230). Plenty of texture that isn't thematic: the cheese, the pencils, the kettle noise, the toast | none |
| Characters | 8.5 | Amelia, imperious and delighted, turns on a dime: "By the time it had finished coming round, the innocence was gone from her face" (L136) and then "the cold was gone from her. She was beaming." (L168). Porter is humbled but stays a person: "His hand went to the knot of his tie… 'You are welcome to stay, of course,' he added quickly." (L190). Viridia: "her chin on her folded hands, waiting, enjoying herself enormously" (L100); "Her mouth kept trying to get away from her at the corners." (L174). Bal is plain-spoken and sixteen: "I'll stay, if you don't mind." Cover-the-name passes | No tics. Gesture classes all under cap. Chaos 3/4, inhabited: an irrelevant thought (ravens and cheese, L50); failed management (Bal's laugh, "Bal couldn't help it", L104, and "doing his best to keep a straight face, and losing", L150); a memory triggered by the scene that comes back to it (the roof and the stump, L230–232, which returns to the book in front of him). No chaos device is on a fixed cadence: Ch.8's stump memory was at a fireside, this one is in print |
| Prose & Voice | 8.5 | Stopping sentence: "He had wanted one so badly. He had sat on a roof and pushed magic through a stump for years on the hope of it." (L230). Underlines: "Mr. Porter's mouth opened and stayed open, empty. It was a good choice." (L162); "He was the color of the chalk." (L128); "Bal watched him go looking for the end of that sentence and find nothing anywhere that would not get him killed." (L154); "holding up a silver ring and waiting for something to come" (L258). Ugly sentence: "the half the household enchantments book had covered in two lines" (L78, see F3). Voice under pressure: the confrontation drops into short, clipped beats (L136–162) | #11 at 1 instance (L128, 0.3/1k), under the cap |
| Pacing | 8.5 | A comic set piece (about 1,900 words) and then a quiet library-and-runes coda, as the outline specifies. Speed varies: the summon and the confrontation run in short paragraphs (L112–162); the library slows down (L208–238). Value shifts: Porter's contempt flips to fear; Bal's reverence for the originators flips to disgust. Hook: Viridia "still somewhere out in that forest" (L258) leads into Ch.10's bloodwolf | The breakfast and walk run about 550 words before the classroom (F5). Not a cap |
| Emotion | 8.5 | Anchor: "You called, Master?" with the goddess on the desk, then Porter going chalk-white (L120–128). Surprise: the menace switches off into "Okay, Master!" and a little wave (L168–172); Viridia laughs at the teacher, not the goddess (L128). Body rebel: Bal's laugh, Viridia's "sound like a kettle", Porter's sweat at the hairline. The library's "It made him feel sick" is the source's own line, earned by the stump memory just before it | none |
| Engagement (Dim 7) | 8.5 | Self-insertion wish-fulfilment at full strength: the sneering teacher asks for your toad and gets a goddess who calls you Master and then leaves when you tell her to. Empathy holds through the library's lost reverence | none |
| **FLOOR** | **8.5** | | |
| **AVERAGE** | **8.5** | | |

Trajectory: Ch.1–8 each scored 8.5, and Ch.9 holds 8.5. Commercially this is the strongest chapter yet.

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8.0 | The set piece is fast and the hook is clean. A slow breakfast run-up and a quiet coda |
| Tomorrow Test | 3 anchors (9) | IMAGE: Amelia cross-legged on the desk, "You called, Master?" IMAGE: Porter "the color of the chalk" and Huginn frozen. QUOTE: "Is it a rodent, perhaps? Or a toad?" |
| Casual Reader | 9.0 | The airport reader laughs out loud here. A bully-teacher payoff with a goddess delivering it |
| Shareability (quote/plot/emotional) | 4/4/2 (7.5) | Quote: "Think your next words through, very carefully." Plot: "the teacher asks if his familiar is a toad and he summons a goddess" |
| Concept Pitch | yes (10) | |
| Human Closeness | partial (5) | A classroom scene. The closeness is in Bal, Viridia and Amelia's complicity, not in intimate talk |
| Raw | 8.2 | +0.5 strong anchor = **8.7** |

CVI-Legacy: Originality 8.5×.3 + Theme 8.5×.25 + Vocabulary 2×.2 + Re-read 4×.15 + Identity 3×.1 = **6.0**.

## Anti-AI Scan (20 patterns; commercial clean threshold 0–8)
1 Forced symmetry: clear. "By someone… By hurt…" is from the source.
2 Empty poetic vocabulary: clear.
3 Automatic rule of three: clear. The source supplies the lists (breakfast, the lecture).
4 Em dashes: clear (0).
5 Empty metaphors: clear.
6 Dramatic "And" openings: minor, 1 (L226, "And the rules were not kind ones.").
7 Pseudo-philosophical closings: clear. The chapter ends on an image, not a maxim.
8 Excessive parallelism: minor, 1 ("The eggs were good and the bacon was better", L24).
9 Overly smooth transitions: clear. Scene breaks are hard cuts.
10 Described emotions: minor, 2 ("enjoying herself enormously", L100; "It made him feel sick", L232, which is from the source).
11 Explanatory extension: minor, 1 ("It wasn't Amelia who had set her off. It was Mr. Porter, and no wonder.", L128). Well under the cap.
12 Binary negation opener: minor, 1 (the same L128, which is the source's own logic).
13 Precision flex: clear. The numbers (twenty desks, rows of five, fifteen years, twice) are all from the source.
14 Emotional control demonstration: clear. Management fails on the page (L104, L150).
15 Authoritative description: clear. Bal guesses ("if the book was right", "Did ravens even like cheese?").
16 Philosophical asides: clear. "Everyone's life could be spent except their own" is the source's line.
17 Clean dialogue: minor. Breakfast is orderly turn-taking. The classroom has interruption and broken lines ("But you're," he began. "And he's a…").
18 Thematic echo chamber: clear.
19 Graduated reveal: clear. Set piece, then coda; not the normal-anomaly-escalate shape.
20 Emotional temperature report: clear.
**Total: 6 minor patterns, none dense.** CLEAN for Commercial Fiction.

## Character Chaos Check (Bal)
- Irrelevant thought: present (ravens and cheese, L50; the spare ring, L198).
- Cognitive distortion: absent (not needed at 3/4 for commercial).
- Unprompted memory: present and triggered (the roof and the stump, L230), returning to the book.
- Failed emotional management: present (the laugh, L104; the straight face, L150).
- Voice under pressure: demonstrated, though the pressure here is comic.

## Secondary Character Chaos
- Viridia: has her own moments (the paper bargain, the kettle laugh, her mouth getting away from her).
- Mr. Porter: has his own moment (the tie knot, saying instructions twice, minding but saying it is "more than okay").
- Huginn and Tyler: texture with personality.
- Amelia: has her own moment (the switch from cold to beaming).

## The Tomorrow Test
**What the reader remembers:** the goddess appearing cross-legged on the desk asking "You called, Master?", and the teacher who had asked for a toad going chalk-white.
**Anchor type:** BOTH (image and quote). It is a different type from Ch.8's quiet hand-holding anchor, so there is no pattern repetition.
**Verdict:** ANCHOR EXISTS.

**Shareability:** "He's told to show his familiar, the teacher sneers 'a rodent? a toad?', and he summons the goddess." This is the book's most textable moment so far.

## Reader Reports
**The Devourer:** Skims breakfast and races through the classroom. The summon is the payoff they were waiting for since Ch.4. They might slow in the library, but the buried-army detail and "He had wanted one so badly" keep them going, and the last line points them to Viridia's bonding. Would not stop.
**The Critic:** Underlines "It was a good choice," "Twenty faces, and Huginn's," and the stump sentence. Notes the clumsy "the half the household enchantments book had covered in two lines" and the odd "floor two."
**The Hostile:** Viridia says her Rune working is "this afternoon", but the afternoon is Warfare and Crafting, which she shares with Bal (L18). Ch.8 left the schedule on the coffee table, and here it is in his back pocket (trivial; he picked it up in the morning). Could Bal see sweat at Porter's hairline from the back row (L140)? Plausible.
**The Casual Reader:** Loves it. The bully teacher gets his comeuppance, the goddess is funny and scary, and the friend laughing in the back row makes the reader part of the gang. Would tell a friend. 9/10.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|-------|----------|--------|---------|--------|----------|
| "this afternoon" schedule clash (L18) | | | x | | INVESTIGATE (fix: it is invented information) |
| Buried-tent image darker than the chapter (L220) | | x | | x (tone dip) | SHOULD FIX (author tone direction) |
| Clumsy phrasing at L78 and L204 | | x | | | INVESTIGATE |
| Slow run-up before the classroom | x | | | | INVESTIGATE |

## Revision Recommendations (ranked; nothing here adds plot)

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|----------|-------------|-----------------|-------------|-------------------|--------------|
| F1 | L220 | Style / tone | "Somewhere under a field, if the book was right, a tent was still standing in the dark with the earth packed in around it, and whoever had been inside it when the stone closed." | This is a buried-alive image the source doesn't have. It is literary embellishment that darkens a light chapter, against the author's "no darker themes" direction | Cut L220 entirely. "Bal read that part twice." (L218) can go straight into L222 ("He thought of a temple behind an orphanage…"), which keeps the harmless link to Ch.5 | Yes: no grim elaborations of reported history beyond the source |
| F2 | L18 | Logic / invented information | "Rune working, different. I've got it this afternoon." | The afternoon is Warfare then Crafting, both shared, so this contradicts the schedule. The source never says when her rune class is | Cut "I've got it this afternoon." The line becomes: She tapped the second line of his. "Rune working, different." | No |
| F3 | L78 | Style (clarity) | "Most of the lecture was about the half the household enchantments book had covered in two lines: …" | It is hard to parse ("the half the… book") | "Most of the lecture was on the part the household enchantments book had covered in two lines: …" | No |
| F4 | L204 | Style (American register) | "The library was upstairs on floor two, as Amelia had said." | "floor two" is unidiomatic, and the source says "second floor" | "The library was on the second floor, as Amelia had said." | No |
| F5 | L6 and L10 (optional) | Pacing | "and Bal had to borrow the paper to order it." / "Write small," she said. "I want the rest of that page back." | "the paper" reads as if a specific sheet is meant. The breakfast run-up is long but warm | L6: "borrow paper". Optionally drop the sentence "He wrote small, tore the unused half off and handed it back, and laid his half on the plate." (L12) to shorten it by about 25 words. Keep the "Write small" joke, since it is playful and fits the brief | No |

**Outline housekeeping:** set Ch.9's ledger "Opening" to "breakfast with Viridia" (source order), so the shape ledger matches the text.

**Continuity note for Ch.10:** this chapter's last paragraph already uses the source's "eager to see Viridia and find out how her familiar bonding went" (as wondering whether she is still in the forest). Ch.10 should open on the dining hall or Viridia salting her nuggets, as its outline says, and not repeat "hurried… eager to see Viridia".

### Fix order: F2 (logic), then F1 (tone), then F3–F5 (prose)

## Strengths to PRESERVE
- The whole summon-and-confrontation block, L112–174, word for word.
- Huginn's reactions (L64, L114, L132): they make the teacher's humiliation funny rather than cruel.
- "It was a good choice." (L162). "By someone, he meant Mr. Porter. By hurt, he meant killed." (from the source).
- The stump sentence in the library (L230). It ties the coda to Ch.1 without new backstory.
- The ending image of Viridia in the forest holding up a ring.

## VERDICT
**PASS.** Genesis Floor 8.5, Average 8.5, Casual 9.0. Apply F1 and F2 before commit, and F3–F5 at the editor's discretion. No re-score needed.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
