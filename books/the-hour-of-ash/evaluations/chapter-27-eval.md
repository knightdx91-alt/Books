# Evaluation: Chapter 27 — Cumae (run 2) · Chronological walk, Puteoli → the hot ground → Avernus → the Sibyl's cave → the road back
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-24 | **Cycle:** 0
**Text evaluated:** `manuscript/chapters/chapter-27.md`, md5 `b7d112dd7d6ba23fcfd6648b6ca99e42`. This is the page after writer → dialogue-polish → hook-craft (no edits) → disruptor → continuity repair (CRIT-1…6, WARN-1…15, INFO-14/16, all logged). Nothing the repair fixed is re-raised. The coordinator's entity items CH27-1, CH27-2 and CH27-3 are folded into the fix set (F1–F3).

**Measured on the real file** (from the book folder):
- `bash tools/check_chapter.sh 27`: ALL MECHANICAL GATES CLEAN (style, grammar, rhythm, show/tell, voice-wear strict, tic gate incl. gestures, metaphor, SHAPE CLEAN).
- **`python3 tools/tic_report.py --echoes 27`: 83 echoes** (82 cross-chapter phrases plus 1 pronoun-swapped). Only the first 60 print, because the tool truncates. The 5c scan does not fail the exit code, so "ALL CLEAN" hides it. The book's standard is **0 before the evaluator runs** (CLAUDE.md loop step E; Ch.24, 25 and 26 all arrived at 0). The repair log took it 89 → 83 and stopped. 0 command echoes, 0 spoken-line echoes.
- `--gate`: clean. Shape **7,681** words (101% of 7,600). 3 breaks / 4 sections. Dialogue **36.1%** (band 35–45). Median sentence 17, mean 21.1, 12.7% over 40 words. Simile 25 (fig 3.9/1k, under the 4.0 gate). **Em-dash 1** (l.388 "when you first—"; the header says 0). And-chains 3/9. Credential asides 0. Negation pivots 0.
- Shape: `I-statement` (51 words) → `long-fade` (52-word last sentence), matching ledger row 27.

**Read against:** the book's CLAUDE.md; STATE.yaml guardrails, retired reflexes, AUTHOR-CP2-2, CP4-2, CP5-0b and CP5-1; outline ledger row 27 and `## Chapter 27` (beats, writer warnings, beat subversion), plus the Ch.26 and Ch.28 cascades; foundation §Fenn, §doors and anchor rows 26/27/30/35; voice-dna §0 and §1 (dialogue conventions: no adverbs in tags), §3b and §4; character-bible ("Voices from lives, not rules"; FENN with the idiom pool, the Ch.25/26/27 blocks and SPENT narrated states; At-risk after Ch.25, 26 and 27 and the at-risk table); chapter-25 (all of Fenn's crossing and door material); chapter-26; the dialogue, hook and disruption reports; `continuity/chapter-27-audit.md` with its repair log; `chapter-26-eval.md` for the bar.

**Genre profile:** commercial historical romance / time-slip (comp *Outlander*). Anti-AI band commercial (0–8 clean). #11 cap: >6 instances or >0.8/1k. Dimension 7 = **IMMERSION**. Engagement (STATE): empathy 55 / fascination 30 / self-insertion 15.

*(l.N = line number in the evaluated file, md5 b7d112dd.)*

---

## HEADLINE
**CVI-Launch:** **9.4** (8.9 + 0.5 for a strong anchor) | **CVI-Legacy:** **7.1** | **Genesis Floor:** **8.0** | **Genesis Average:** **8.64** | **Casual Reader:** **9.0**

**Engagement type (this chapter):** Empathy 55 (an old man's palm on a dead wall; "Of you."; the coat he can still feel) · Fascination 35 (a door can die; the mentor doesn't know what he is teaching) · Self-insertion 10.

**Divergence alert:** none (9.4 vs 8.0 = 1.4).

This is the best Fenn on the page so far. The beat subversion lands completely: the place of power is dead, and the lesson is the man. The Floor sits on hygiene, not structure:
1. **83 unvaried cross-chapter echoes.** The book standard is 0.
2. **A replayed Ch.25 exchange.** Ch.25 l.172–174 has "I crawled it on my knees." / "Course you did. I went in on my belly". Ch.27 l.142–146 has Fenn ask again ("How'd you go in, belly down?") and get the same contrast. This is a logic slip and a spoken-beat reuse (coordinator CH27-3).
3. **Eros's door is made cold** ("It was cold on the last Kalends"; Mara likens the beef-cold Cumae door to it), against Ch.19's faint coolness (CH27-1).
4. **The narrated-trait census fails four times:** the keeper's sea-gaze is 3 inside ~250 words; Fenn's delight is noted 4×; his stick 8×; Lucius absorbed in watching 6×.
5. **Smaller items:** Fenn's "guy" 7×; Mara's "And…?" question run, an anaphora triad in speech; two adverbial tags ("gravely", "with great bitterness"); a Richie Allen stat line that is a three-item list; Fenn re-telling the Ch.25 landing in the Ch.25 frame ("Next thing… snow to here").

Every item is clause-level. No beat needs rewriting.

**Gate:** Floor 8.0 < 8.5 → **POLISH** (Casual 9.0 ✓, pacing ✓; the mechanical exit code is clean, but the echo standard is ✗). The tested fix set below projects **Floor 8.5 / Average 8.79**.

---

## PACING VS NEIGHBOURS (gate item, judged)

| | Ch.26 | **Ch.27** | Ch.28 (planned) |
|---|---|---|---|
| Shape | Collage, 7 breaks | **Chronological walk, 3 breaks** | In medias res (bout → backfill → bout) |
| Length | 5,195 | **7,681** (101%; 7,526 after the fix set) | 7,000 |
| Gear / median | mid / 15 | **high / 17** | low |
| Dialogue | 12% | **36.1%** (36.1% after fixes) | 25–35% |
| Reading speed | letters brisk, domestic slow | **"a slow walk; still in the cave"** | fast bout, measured backfill, fast end |
| Slot | deepen Fenn; the refusal shown | **the cautionary mirror at full strength** | a secondary's own life; theme recedes |

- **The contrast is right on both sides.** A short, letter-borne, low-dialogue collage (12%) hands off to a long walked chapter in which Fenn is finally present and talking (36%). That in turn hands off to a fast, low-gear arena chapter. No two neighbours share an approach, a length band or a dialogue band.
- **The reading speed the outline asks for is delivered.**
  - The road (S2, ~2,500 words) is a slow walk. Fenn's comedy carries it, with a turn every ~400 words: the boom, the lemon meringue, the string, the oysters, Kirk Douglas, the ducks, the Zippo.
  - The cave (S3, ~3,076 words) is genuinely still. The blind passage runs from "X marks the spot" to the coat with no exit and no cut.
  - S4 (the bone, the diamond) is the speed peak. The fade decelerates on purpose.
- **Value shift, two axes:**
  - **Mara:** "one night of it unanswered", a door "that kept its own time and not his" (l.72), becomes "here it was, and he was right about it, and it was a wall" (l.378).
  - **Fenn:** young on the window ledge and sliding into home, then "the youth drained out of Fenn between one bend of the path and the next" (l.464).
- **The Devourer's soft spot** is S2's middle (oysters → Avernus → lunch, ~900 words) before the Zippo. It is texture, not a sag, because Fenn's lines keep landing.
- **Handoff:** Ch.28's news waits at home. Felix is never mentioned (guard ✓). The planted question ("Write me… And if it isn't?") is QUESTION PLANT and not Ch.26's GUT PUNCH ✓.

**PACING: OK.**

---

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | **9.0** | Four elements:<br>(1) The mentor's place of power is a dead door, and he shows it off with pride: "That it was here! … Carter finds King Tut, and does he sit on it? He sends for somebody to come look." (l.376)<br>(2) The automat mutation, triggered by sulphur crystals: "Lemon meringue," (l.116) → "In his room, a year ago, it had been coconut cream. I let him have the lemon." (l.126)<br>(3) A baseball diamond scratched in the Sibyl's dust, with the Corycian knucklebone as third base (l.420–426).<br>(4) The cave keeper whose bees "made for Misenum" (l.254), against Fenn's "I went there once myself… For the pay." / "You came back, at least." (l.260–262). | none |
| Theme | **9.0** | "What waiting for another life costs" is carried by acts and objects and never stated:<br>- "I'd check the hill in the morning before I checked the weather." (l.382)<br>- "You sit up with a sick friend, don't you? After that, once a year." (l.368)<br>- "Soon as I'm back I'm writing it up for the Geographic" (l.376)<br>- Mara's own waiting is mirrored: the satchel packed, tipped out and packed again "as I always did when I was a day from Pompeii" (l.56).<br>Texture is well over 30%: the sulphur scrapers, the oyster stakes, the sailor at his third letter, the coins gone green, the keeper's pot lid. | not 9.5: the coat story and the rope-walk room both point the same way within ~600 words. Each earns its place. |
| Characters | **8.0** (uncapped 9.0) | **Fenn** is fully alive:<br>- "it's like eating something that's still making up its mind" (l.150)<br>- "I'm no great shakes on people, but I know that much." (l.162)<br>- "As a doornail… Door. Nail. No?" / "Tough room… Half the house. I've played worse." (l.348–352)<br>- tired fragments on the way back ("Long day." / "My feet.", l.466–470)<br>- "the left one went on going after the right had stopped" (l.364)<br>**Valens** reads ground literally ("It's resting the near hind", l.52; "She bites. Not hard.", l.78; "Hold that.", l.82) with no comparison and nothing remarked on.<br>**The keeper** has his own grief, the swarm.<br>**Lucius** stops on the bag.<br>**Mara's chaos is 4/4 inhabited** (below). | **Hand rule** (census below), four failures:<br>- keeper's sea-gaze 3 inside ~250 words<br>- Fenn's delight 4<br>- Fenn's stick 8<br>- Lucius absorbed 6<br>**Lexical:** Fenn's "guy(s)" 7.<br>**Nameable-rule test:** Mara's "And…?" interrogation run (6, with a triad at l.380/384/388).<br>**Spoken-beat reuse / logic:** the Ch.25 knees/belly exchange replayed (l.142–146).<br>→ **cap 8.0**, the same practice as Ch.24–26. |
| Prose & Voice | **8.0** | **Stopping sentences:**<br>- "until the hill was full of a small bone falling." (l.408)<br>- "He kept his hand there anyway, a while past knowing and then a while past that" (l.324)<br>- "There was another one. That had been the whole of my night's hope, a door that was not his door, and here it was, and he was right about it, and it was a wall." (l.378)<br>- "I took it while his thumb was still trying." (l.218)<br>**Underlines:** "a man on the corner of Broad and somewhere in a wind, determined." (l.214); "his face did not change much, but it changed." (l.248); "the straw had been in them since the cold months, possibly the year before." (l.56).<br>**Ugly sentence:** "He gave me the look across her back that I had had from him…" (l.86); "The bread was dry and we ate it anyway." (l.184).<br>**Voice under pressure:** the boom drops her into body and command ("I had the rope off his wrist… without having decided to move." / "Fenn! Get off it!", l.108–110). At "Then why bring me?" the prose clips ("That was sharper than I meant", l.370). | not 8.5 at cycle 0:<br>- **83 unvaried echoes** (book standard 0)<br>- adverb / emotion tags "said Fenn gravely" (l.256) and "with great bitterness" (l.258), against voice-dna §1<br>- the "And…?" triad (Pattern #8)<br>- Fenn's Richie Allen line opens as a list<br>- Ch.25's landing re-told in its own frame (l.394 "Next thing I'm… in snow up to here" ← Ch.25 l.174 "Next thing, I'm on all fours in snow… snow to here")<br>- l.12 explains the Jupiter callback (#11)<br>- "August, you're frying" reads as a vocative to himself (l.340) |
| Pacing | **8.5** | See PACING VS NEIGHBOURS. The bone's clatter (l.408) and the slide (l.442) are the speed peaks. The blind passage (l.316–400) is the designed stillness. | not 9.0: S2's middle stretch before the Zippo |
| Emotion | **9.0** | **The anchor lands:** "I stood behind him with my daughter asleep against me and watched a man of nearly seventy wait for a wall to turn cold. No cold came; I saw it in the way his fingers lay, easy, no answer in them." (l.324).<br>**Surprise as designed:** Fenn on the window ledge versus "You walk like somebody's grandmother." / "I'm somebody's mother… Twice. The newer one's strapped to my front." (l.292–294); the slide into home.<br>**Body rebel:** l.108.<br>**Techniques:** humour in grief (the doornail), dramatic irony (the carbon: "That, he had no notion of.", l.400; "Once we're back… on top of the TV", l.232), withholding ("did not undo the buckle"), objects (Zippo, coat), memory mutation, and "It's the one I wanted." / "Of a lighter that won't light." / "Of you." (l.224–228). | none |
| Immersion | **9.0** | The Solfatara's sulphur scrapers traced to Pompeii's fullers (l.98); the hollow boom; the Lucrine oyster stakes on the sandbar road; the silted Portus Julius on Avernus (l.172–174); Aornos; the Cumae dromos with pick strokes, trapezoidal section, side galleries and smoke-black chamber (l.268–312); the votives and the green coin-crack; a fleet sailor carving his name; Neapolitan Greek dropping its endings; Pithekoussai / Aenaria; Tarquin and the books. 1960s Philadelphia: the Boyd, the Spectrum, Wanamaker's, Richie Allen 1964. | not 9.5: the light galleries face the sea, which is the **left** of a visitor walking in from the entrance, and the page says "right-hand" (l.270) and "on your right" (l.274). "a century late" (l.174) is Fenn's hyperbole and is left alone. |
| **FLOOR** | **8.0** | Characters, Prose | |
| **AVERAGE** | **8.64** | (9.0 + 9.0 + 8.0 + 8.0 + 8.5 + 9.0 + 9.0) / 7 | |

### Narrated-trait census: EXHAUSTIVE, cycle 0 (spec: >3 notes of one state, or 3 inside ~500 words, fails)
**Class rulings, fixed here so later cycles do not re-litigate them:**
- The Zippo business at l.204–230 is ONE designed frame (outline beat 1), not "the lighter in hand".
- l.322–324 (palm, waiting) is the anchor, one beat.
- Lucius's four single words (Smoke / Duck / Bone / Again) are design.
- The satchel's five appearances are five different functions (pack, camera, fatigue, carbon, bone), so it is an object thread and not a state.

| Character | State | Lines | Count / spacing | Verdict |
|---|---|---|---|---|
| Fenn | delight / grin | 112 delighted · 204 grinning · 348 the grin in his voice · 434 delighted | **4** | **FAILS** → C2 → 3 |
| Fenn | the stick | 86 · 88 swinging · 128 with the stick · 138 thistle · 178 pointed · 242 planted · 420 drew · 502 on the stones | **8** | **FAILS** → C3–C5 → 5 (possession 86, three active uses 138/178/420, fade 502) |
| Fenn | hat handled | 204 pushed back, off and replaced · 242 brim pulled down · 274 tipped · 376 clapped on (states 14/86/286/442 not counted) | 4 | **FAILS** (marginal) → C5 → 3 |
| Fenn | jenny's rope on his wrist | 88 "the jenny's rope looped over his wrist" · 108 · 502 "the jenny's rope looped over his wrist" | 3; 88 and 502 are verbatim in-chapter | → C3 (88 recast) |
| Fenn | tremor | 210 · 364 | 2 | OK |
| Fenn | laughs | 390 · 442 | 2 | OK |
| Fenn | walking backward | 274 · 278 | one beat, same words twice | → P7/P8 |
| Fenn | SPENT Ch.25 states (talking on, break-offs, object-looks, taking in news, "slowly") | 188 stared at the Pentax (the trigger itself, not displacement) | 0 genuine | OK |
| Fenn | "guy(s)" in speech | 30 · 124 · 162 ×2 · 208 · 288 · 426 | **7** | **WATCH → trim** C9–C13 → 3 |
| Keeper | eyes on the sea | 246 staring out to sea · **254 his gaze kept to the sea** · **258 to the sea** | **3 inside ~250 words** | **FAILS** → C1 → 2 |
| Keeper | pot lid | 246 · 254 · 456 | 3, spread | OK |
| Lucius | absorbed watching | 36 intent on the harbor · 156 the fly · 184 the ducks · 264 gazing at the doorway · 306 watched the man in the window · 424 looked hard at the lines (410 listening, other sense) | **6** | **FAILS** → C6–C8 → 3 (184, 264, 424) + 410 |
| Lucius | "fist" (narration) | 36 · 76 · 84 · 184 · 264 · 436 | 6 | WATCH → E58 → 5 (Ch.26 ran 5) |
| Lucius | grips Mara's skirt | 76 · 264 | 2 | OK |
| Aelia | asleep | 184 · 324 · 392 (290 in speech) | 3 narrated, spread | OK |
| Aelia | wakes / feeds | 238 · 484 | 2 | OK |
| Valens | looks at Mara | 86 | 1 | OK |
| Mara | fatigue | 280 strap/feet/satchel · 306 leg · 404 "I wanted to sit too." | 3, spread (the designed surprise) | OK |
| Mara | "And…?" question openers | 346 · 358 · **380 · 384 · 388** · 498 | **6; 380/384/388 a triad** | **FAILS** (nameable + #8) → C14–C16 → 3 (358, 380, 498) |
| Mara | the "before I decided" reflex | 108 "without having decided to move" · 194 "before I had settled what to do about it" | 2 | → P6 → 1 (108 kept: it is the body rebel) |
| Jenny | bites | 78 · 264 | setup and payoff | OK |

### Nameable-rule test (AUTHOR-CP5-0b)
- **Fenn:** the risk is lexical ("guy"), now trimmed. His refusal to be told the future ("Don't. Not one word about it", l.194) appears once and is his life (card: "asks questions and refuses the answers"). **Pass after C9–C13.**
- **Mara:** the "And…?" interview run fails. **Fixed.**
- **Valens:** no comparison and nothing remarked. **Pass.**
- **Keeper:** the sea-gaze fails. **Fixed.**
- **Lucius:** pass after the attention trim.

---

## CVI-Launch Breakdown (Commercial Assessment)
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8/10 | A long chapter (7.7k), but 36% dialogue and Fenn every 300 words. The slow walk is deliberate, and the cave is the hold. |
| Tomorrow Test | 4 anchors → 10 | IMAGE: the palm on the dead rock; the Zippo that won't catch, shot anyway; the bone clattering down the gallery. QUOTE: "it's like eating something that's still making up its mind" / "Door. Nail. No?" |
| Casual Reader | 9/10 | See the reports. |
| Shareability (quote/plot/emotional) | 4/2/4 → 8/4/8 → MAX 8 × 0.6 + AVG 6.67 × 0.4 = **7.5** | "a door can die" / the old man's hand / the coat |
| Concept Pitch | yes (10) | "A woman lost in ancient Rome meets the only other time-traveller, an old American who has spent thirty-five years waiting at doors, and he takes her to see one that died." |
| Human Closeness | yes (10) | A mother, her children and a lonely old man, all day |

**CVI-Launch = 0.2(8) + 0.2(10) + 0.2(9) + 0.2(7.5) + 0.1(10) + 0.1(10) = 8.9, + 0.5 strong anchor = 9.4.**

**CVI-Legacy (default weights)** = Originality 9.0 × .30 + Theme 9.0 × .25 + Cultural vocabulary 3 × .20 + Re-readability 7 × .15 + Identity 5 × .10 = 2.70 + 2.25 + 0.60 + 1.05 + 0.50 = **7.1**.

Re-readability is high: "Once we're back… on top of the TV", "If I am still here, my friend", "Write me… Just that it's cold" and "You say that every year" all turn on re-read, with Ch.35 in hand.

---

## Anti-AI Scan (20 Patterns) — 7,681 words; commercial band (0–8 clean)
1. Forced symmetry: **Found, 1** (minor). "It's the one I wanted." / "Of a lighter that won't light." / "Of you." (l.224–228) is earned.
2. Empty poetic vocabulary: Clear.
3. Rule of three: **Found, 4** (0.5/1k, moderate). l.280 strap/feet/satchel; l.338 "small, flat, a little worn"; l.218 "the stalk, the cupped hands, the thumb"; l.274 barker. All have varied syntax; none is an anaphora triad.
4. Em-dashes: 1 (l.388). Clear.
5. Empty metaphors: Clear.
6. "And" openings: **Found, 6 in Mara's speech** (0.8/1k, moderate). See Pattern #8. → 3 after C14–C16.
7. Pseudo-philosophical closings: **Found, 1** (minor). The S1 close, l.72 "I had seen good pieces come apart in the hands of people who could not leave them be." It is past-facing experience from her trade, not a universal, and it is kept. The chapter close is an image ✓.
8. Excessive parallelism: **Found, 1.** "And you lived where…?" / "And after?" / "And before…" (l.380–388), an anaphora triad in speech (retired reflex). → C14–C16.
9. Overly smooth transitions: Clear. The breaks cut hard.
10. Described emotions: **Found, 4** (0.5/1k). "gravely" (l.256), "with great bitterness" (l.258), "delighted" ×2. → P1, P2, C2.
11. Explanatory extension: **Found, 3** (0.4/1k, minor; under the cap of 6 / 0.8). l.12 "here was his Jupiter, cast from a stool…" explains the callback; l.210 "as smokers did on windy corners"; l.404 "since that was why it had come". → P3 cuts the first.
12. Binary negation opener: Clear ("Nothing killed it." asserts; it does not define by negation).
13. Precision flex: Clear ("eleven or twelve ducks" is deliberately loose).
14. Emotional control demonstration: **Found, 1** (minor). "did not undo the buckle" (l.400) is withholding, not managing.
15. Authoritative description: **Found, 1** (minor). The corridor (l.268–270) is confident but breaks with "Who cut it?" / "Who can say?".
16. Philosophical asides: **Found, 1** (minor). Fenn: "Nobody ever went digging for the stuff they kept." (l.278) is racket cynicism in character, not wisdom. Kept.
17. Clean dialogue: **Found, 1** (minor). The S3 interview run (When? / Why? / Did you keep coming? / Then why bring me?) is broken by the doornail joke and Lucius's laugh.
18. Thematic echo chamber: Clear.
19. Graduated reveal: Clear (walk → long fade, per the ledger).
20. Emotional temperature report: Clear.

**Total: 10 patterns present, most at minor weight** (commercial band "watch" 9–11). After the fix set, #6, #8 and #10 drop to trace and the total falls to about 7 (clean).

## Laws scan
- **NO FORESHADOWING:** clean. "Once we're back" and "If I am still here" are character belief and the reader's irony, never narration. No narrator line touches 79. The steam is texture ("the steam standing up behind us… until the hill shut it off", l.128). Lucius's "Smoke" is a child's word for steam (INFO-12 of the audit concurs).
- **The mountain never named; "Margaret" never said; no tomb:** clean. Grep shows 0 for Vesuv / mountain / Margaret / tomb.
- **No "don't end up like me", no "in (all) the years since", no closing aphorism:** clean ("Every winter since" is past-facing).
- **Fenn never lists:** two near-lists remain. The Richie Allen stat line ("Third base, nineteen sixty-four, rookie of the year", l.426) → C17. The Ischia names (l.288) are an and-chain of what people call the place, which is his pattern-mind on its subject; kept.
- **Retired reflexes:** one anaphora triad in speech (C14–C16). No define-by-negation. No performed candour. No device as a button: "Not hard, says the gladiator" closes a beat, not a scene.
- **No spoken line reused:** the tool finds none. By hand there are three borrowings:
  - the knees/belly exchange (Ch.25 l.172–174 → l.142–146) → F1
  - "Next thing… snow to here" (Ch.25 l.174 → l.394) → C18
  - "Jupiter sitting" (Ch.26 letter → l.10). This is a deliberate in-person callback; its wording is varied by P4.
- **Closed / spent lists:**
  - "a sap" and "swell" are at 2/2. F1 returns "a sap" to 1.
  - "Horn and Hardart" was at 2/2 and a flagged echo. E27 says "the automat", which holds it at 1/2.
  - "kid" 1, "okay" 1, "fellow" 1, "anyhow" 1: all within the WATCH caps.
  - Ch.26 CUT strings: none restored (checked: "with the bone in his fist", "Luckies", "the big fellow", "talked American", "very carefully": 0).
  - Ch.26 guards (1)–(13): all hold.
- **Doors canon:**
  - **CH27-1 (coordinator):** l.342–344 ("Like Eros's" / "Like Eros's, only colder") and l.488–496 ("Still cold?" / "It was cold on the last Kalends." / "Just that it's cold.") make Eros's resting door cold. Ch.19 is faintly cool → F2a–F2d. The dead door stays "warm like a wall's warm". Cumae alive was colder than Eros's ever is, and Fenn now says so himself ("Eros's is a little one. This was a beauty.").
  - **Ch.25 cascade:** Ch.25 l.258 still reads "Shut tight. Warm in the sun, like everything else on that road." of Eros's door in 62. By the law Ch.27 states, that describes a dead door, and Fenn then waited on it for seventeen years. The continuity repair fixed l.314 and missed this line. → **X1** (finalized chapter; orchestrator's call; tested).

---

## Character Chaos Check (Primary — Mara)
- **Irrelevant thought: present.** The sulphur browning Grata's bronze crescent and "Grata would demand to hear who had let her good bronze go brown as a bad tooth" (l.104); the fuller's sulphur traced to its source (l.98).
- **Cognitive distortion: present.** The night's hope for a door "whose rhythm owed nothing to tables worked backward from a schoolbook" (l.72). This is the refusal's fig leaf in action.
- **Unprompted memory: present, triggered and returning.** Lucius bearing the bone "the way the Delphi priests bore the god's things in procession" (l.454).
- **Failed emotional management: present.** "That was sharper than I meant, and Lucius startled at the sound." (l.370).
- **Voice under pressure: demonstrated.** At the boom (l.108–110) and at the wall (l.378, the and-chain collapse of hope).

## Secondary Character Chaos
- **Fenn:** has his own moments, many: the automat mutation, the coat he can still feel, "the left one went on going", Kirk Douglas "bawled like a baby… and don't you tell him that".
- **Valens:** his own moment. The hoof, the hat, and "Is it the door… that he wants to show you?" (l.58). The satchel goes unremarked: "If he made anything of the satchel he kept quiet about it" (l.70).
- **The keeper (walk-on):** his own moment, the swarm and "What does a bee want with Misenum?".
- **Lucius:** his own moment. He stops on the bag and waits "to be told what that had been" (l.436).

---

## The Tomorrow Test
**What the reader remembers:** an old man's hand spread on a wall in the dark, waiting for it to turn cold, "a while past knowing and then a while past that". Then the same man sliding into home plate in the Sibyl's dust with his hat gone.
**Anchor type:** BOTH (image: the palm, the Zippo shot while the thumb is still trying, the bone falling down the gallery; quote: "still making up its mind", "Door. Nail. No?").
**Verdict:** ANCHOR EXISTS. It is not a repeat of the Ch.26 type (a document read aloud).

**Shareability:** "He takes her to see a door that died, and he's proud of it." / "He tries to light a lighter that hasn't worked in thirty-five years so she can take his picture."

---

## Reader Reports
### The Devourer
- Hooked by line 10 (Fenn holding the baby up: "the whole of Jupiter… like a shaving brush").
- Speeds through the boom and the meringue, slows over oysters → Avernus → lunch, and is caught again by "Is that a camera?".
- S3 does not let go, and the bone down the gallery is a pure page-turn.
- Would finish. Would not stop anywhere.
- Minor: the road is long before the cave.

### The Critic
- Underlines l.324 ("a while past knowing…"), l.378 ("and it was a wall") and l.408 ("a small bone falling"), plus "In his room, a year ago, it had been coconut cream. I let him have the lemon."
- Admires that the lesson is never spoken.
- Disappointed by: "said Fenn gravely" (a tag adverb in a book that otherwise refuses them); Mara's three stacked "And…?" questions in a row (l.380–388); the Jupiter callback explained (l.12); and, on a careful read, phrases that have appeared in earlier chapters (83 by the tool).

### The Hostile
- "Fenn asks how she went in, and she already told him, in his own room, a year ago (Ch.25)."
- "Eros's door is 'cold on the last Kalends', but Mara felt it faintly cool in full sun. And in Ch.25 Fenn found it 'warm in the sun, like everything else', which by this chapter's own law means dead."
- "Fenn slept a week at the cave mouth, but in Ch.25 he 'hiked up there first thing'."
- "'August, you're frying' — is he talking to himself?"
- "The windows face the sea; walking in, the sea is on your left."
- "If the live door silenced footsteps along the whole corridor (l.356), why wasn't the Sibyl's cave known as the silent cave?" (INFO only: this can stand as the legend's seed.)

### The Casual Reader — 9.0
- Buys at the airport on the strength of Fenn.
- They LIKE him instantly ("people tell me I'm no good at my job").
- They feel the ache without being told: the lighter, the coat, "Write me… Just that it's cold."
- They would tell a friend "there's this old guy…". The cave sags nowhere for them.
- No vibes problem.

### The Devoted Reader (active)
- Will notice:
  - "home" said only as home plate
  - the carbon withheld in the satchel (pays off at Ch.35)
  - the Zippo frame against Ch.35's single catch
  - "If I am still here, my friend." / "You say that every year."
  - the Ch.26 "Jupiter" in person
- Will write the Reddit post about the coat.
- Would also catch the replayed Ch.25 exchange and the Eros's-door temperature drift. Both are fixed by F1 and F2.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| Ch.25 knees/belly exchange replayed (l.142–146) | | ✓ | ✓ | | ✓ | SHOULD FIX (logic; fixed first) |
| Eros's door made cold / Ch.25 l.258 warm (door law) | | | ✓ | | ✓ | SHOULD FIX (canon) |
| Coat week vs Ch.25 "first thing" | | | ✓ | | ✓ | INVESTIGATE → F3 |
| 83 cross-chapter echoes | | ✓ | ✓ | | ✓ | SHOULD FIX (book standard) |
| Census failures (keeper gaze, Fenn delight/stick, Lucius watching) | | ✓ | ✓ | | | SHOULD FIX |
| "And…?" triad; tag adverbs; Richie Allen list | | ✓ | | | | INVESTIGATE (fixed: cheap) |
| Gallery side (left, not right) | | | ✓ | | ✓ | INVESTIGATE → F6 |
| S2 middle long | ✓ | | | | | INVESTIGATE (no change: texture) |

---

## Revision Recommendations (Ranked) — ONE fix set, all tested
Script: `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes27/apply_fixes.py <chapter-27.md> [<chapter-25.md>]`. It runs **104 replacements** on Ch.27 (+1 optional on Ch.25). Each must match exactly once or the script aborts and writes nothing; a re-run aborts safely.

**Tested on a scratch copy** of the book folder (`…/scratchpad/eval27/`):
- `bash tools/check_chapter.sh 27`: **ALL MECHANICAL GATES CLEAN**.
- `--gate`: clean.
- **`--echoes 27`: 0 echoes**, 0 command echoes, 0 spoken-line echoes (from 83).
- `check_chapter.sh 25` (with X1): clean. `--echoes 25`: 0.
- Ch.27-only mode (no X1) is also clean, with 0 echoes.
- Shape is **7,526** words (99% of target), dialogue **36.1%**, median 17, `I-statement` → `long-fade` unchanged.
- Result md5s: Ch.27 `6441a8e8c82e78d686d560e2574895d8`, Ch.25 `d2ceac85d25f8765e6a260da1027f48d`.

**How the replacement strings were checked:**
- Against Ch.1–26 and the bible's CUT/SPENT lists and closed frames ("planted himself" and "snow coming" were rejected as Lucius/Valens echoes and replaced).
- Several first drafts tripped the gate and are **not** in the script: "loosened my tunic at the throat" (a Ch.25 self-repeat), "every one of them", "most of what", "opened his hands", "at our backs", "stepped into the", "took it away", "a good while", "till the sun", "through his teeth", "near the bottom".
- No earlier pass's cut is restored.
- The opener and the palm-on-rock anchor are untouched. The close is touched only by echo-only word swaps (E12–E14).

| ID | Location | Problem type | What happens now | Why it fails | Revision direction (exact, in script) | Project rule? |
|---|---|---|---|---|---|---|
| F1 | l.142–146 | Logic / Voice | "How'd you go in, belly down?" / "Kneeling. Sideways…" / "On your knees, for crying in the sink. Me, I crawled it flat like a sap…" | Ch.25 l.172–174 already played this exact exchange; Fenn asks what he was told (CH27-3) | End Fenn's speech at "…like I owed it a letter." and cut the two lines (−33 quoted; "a sap" returns to 1/2) | Yes: no in-person beat replays a Ch.25 exchange |
| F2a–d | l.342–344, 490–496 | Continuity | "Like Eros's," / "Like Eros's, only colder." / "Still cold?" / "It was cold on the last Kalends." / "Just that it's cold." | Eros's resting door is faintly cool (Ch.19); the beef-cold comparison attaches to it (CH27-1) | "Eros's is only cool," I said. / "Eros's is a little one. This was a beauty. …" / "Still cool?" / "It was cool on the last Kalends." / "Just that it's cool." | Yes: Eros's door is "cool" every time until the plan escalates it |
| F3 | l.394 | Continuity | "I slept up at that mouth in it a week… The day I went in I shucked it" | Ch.25 l.170 "I hiked up there first thing" (CH27-2) | "I sat at that mouth in it for hours, waiting on the cold…" / "When I did go in I shucked it" (the sunup breath stays; he arrived at dawn) | No |
| X1 | **Ch.25** l.258 | Continuity (cascade) | "Shut tight. Warm in the sun, like everything else on that road." | By the Ch.27 law, warm = dead; Fenn then waits 17 years on it | "Shut tight. Cool under my hand with the sun on it, and not a breath out of it." (tested; finalized chapter, orchestrator's call) | — |
| F4 | l.340 | Logic (clarity) | "August, you're frying out on that terrace" | Reads as a vocative to August Fenn | "In August you're frying out on that terrace" | No |
| F5 | l.310 | Logic | "Come on, it's at the bottom," | The door is short of the room | "Come on, it's down this end," | No |
| F6 | l.270, 274 | Immersion | "Along the right-hand wall…" / "on your right the windows" | The galleries open west to the sea, which is the visitor's left; the light paragraph also carries 5 echoes | Left-hand / on your left. The paragraph is recast: "driven through to the cliff face… and each let the afternoon in. It came low… and fell across the floor… so bright the pick strokes stood out in it like writing;" | No |
| C1 | l.254 | Character (census) | "His palm came out for the coins; his gaze kept to the sea." | Keeper's sea-gaze 3 inside ~250 words | "His palm came out for the coins." | No |
| C2 | l.434 | Character | "Fenn asked me, delighted." | Fenn's delight 4 | "Fenn asked me." | No |
| C3–C5 | l.88, 128, 242 | Character | "swinging the stick, the jenny's rope looped over his wrist… Our street climbed"; "walked ahead with the stick"; "with his stick planted and his hat brim pulled down" | Stick 8, hat 4; 88 and 502 repeat "the jenny's rope looped over his wrist" verbatim; "climbed" ×2 | "the jenny's rope round his wrist… Our street rose between garden walls"; "Fenn walked ahead and then dropped back"; "He admired it until she was done." | No |
| C6–C8 | l.36, 156, 306 | Character | ", intent on the harbor" / "A fly on the jenny's neck had Lucius's attention…" / "and watched the man in the window" | Lucius absorbed 6 | Cut all three | No |
| C9–C13 | l.30, 162, 208, 286–288 | Voice (lexical) | "guy" ×7 | One word doing all of Fenn's people (nameable) | "whoever drew it"; "I've seen men built like that"; "Like the Marlboro man." (new period reference, 1/2); "his white hair on end" + "straight down there's a fisherman asleep" | Yes: Fenn "guy" ≤3 per chapter |
| C14–C16 | l.346, 384, 388 | Style #6/#8 | "And it's dead." … "And after?" / "And before, when you first—" | 6 "And…?" openers; triad 380/384/388 | "It's dead." / "After it died?" / "Before Cumae, when you first—" | No |
| C17 | l.426 | Character (Fenn never lists) | "Third base, nineteen sixty-four, rookie of the year, the only guy…" | Three-item stat list | "He played third in sixty-four and got rookie of the year, the only guy…" | No |
| C18 | l.394 | Voice (spoken reuse) | "Next thing I'm crawling around Phocis in my shirtsleeves in snow up to here, and it's forty-one." | Ch.25 l.174 "Next thing, I'm on all fours in snow… snow to here" | "Then it's forty-one, and I'm in my shirtsleeves in Phocis with snow falling on me." | No |
| P1–P2 | l.256, 258 | Style (voice-dna §1) | "said Fenn gravely." / "said the keeper to the sea, with great bitterness." | Tag adverb; emotion told in a tag | "said Fenn." / "said the keeper to the sea." | No |
| P3–P4 | l.10, 12 | Style #11 / reuse | "the whole of Jupiter sitting up there…"; "here was his Jupiter, cast from a stool in his room on a night of rain, sticking up at the gulls." | Explains his own callback; "Jupiter sitting" is the Ch.26 letter's wording | "the whole of Jupiter up on top like a shaving brush"; end at "…would lay down." | No |
| P5 | l.72 | Style | "within five minutes of first hearing my voice" | Echoes the outline's Ch.25 subversion ("first five minutes"); "Five minutes" ×2 in chapter | "the same afternoon he first heard my voice" | No |
| P6 | l.194 | Style (reflex) | "drew it back before I had settled what to do about it." | 2nd "before I decided" frame in chapter | "drew it back." | No |
| P7–P8 | l.274, 278 | Style / echo | "walking backward, and spread his arms" … "He walked backward out of the light. 'That's the whole racket, kid." | Same words twice in one beat; Ch.5 echo | "…swung round to face us and went on backward with his arms spread wide." … "He backed away out of the light. 'That's the racket, kid." | No |
| E1–E67 | throughout | Style (echo scan) | 83 cross-chapter 2nd uses (e.g. "a little before", "between his knees", "from the doorway", "small and yellow", "the morning before", "tell your mister", "through his nose", "the neck of my tunic") | Book standard: 0 before the evaluator (Ch.24–26 = 0) | One-word or one-clause swaps, each tested; full list in the script (e.g. "short of the room", "up on his knee… inside the rim of the hoof", "from the entrance", "lit yellow down the mole", "I'd check the hill mornings…", "Don't tell Valens about the slide.", "He laughed at himself a little.", "opened my tunic for her") | **Yes (pipeline):** check_chapter step 5c should FAIL on echoes > 0 and tic_report should print all of them, not the first 60 |

### Fix order: Logic/Character (F1–F5, X1, C1–C18) → Structural (none) → Connective (F6) → Prose (P1–P8, E1–E67) → Factual (F6 orientation)

### Bookkeeping for finalize (not page edits)
- **Bible re-sync of the Ch.27 SPENT lines changed by the fix set:**
  - "Just that it's cold" → "cool"
  - "I mean to watch your face when you've got nothing to argue with"
  - "It's never the stuff they kept" → "Nobody ever went digging for the stuff they kept"
  - "If I'm still here" → "If I am still here"
  - "Don't tell Valens about the slide."
  - "I'd check the hill mornings before I checked the weather"
  - the coat as "sat at that mouth… for hours"
  - "for crying in the sink" and Fenn's "a sap" no longer on the page
  - Horn & Hardart held at 1/2
  - "the Marlboro man" period reference 1/2
  - Fenn's "guy" 3
- **The bible's Ch.27 Fenn block** still quotes the cut wick line, "walks the way he talked" and the notebook clause.
- **ENTITY:** Eros's door "cool at the last Kalends"; the Cumae door's live cold stated as greater than Eros's ("Eros's is a little one"); Ch.25 l.258 re-quote if X1 is applied.
- **Header:** em-dash is 1, not 0.

## Strengths to PRESERVE
- The opening claim (l.8) and the long fade, whose words are untouched except the echo swaps.
- The Zippo frame, l.204–232: the grass stalk, "a man on the corner of Broad and somewhere in a wind", "I took it while his thumb was still trying", "Of you.", "on top of the TV where the company can see it".
- "Lemon meringue," → "I let him have the lemon."
- The keeper and his swarm; "I went there once myself… For the pay." / "You came back, at least."
- The anchor paragraph l.322–324, verbatim.
- "As a doornail… Door. Nail. No?" / "Tough room."
- "I can hear my feet." / "Warm like a wall's warm".
- "That it was here!" and Carter / King Tut.
- "There was another one… and it was a wall." (E48 changes only "There was" → "There had been".)
- The coat and the carbon withheld ("That, he had no notion of.").
- "until the hill was full of a small bone falling".
- "That's home," as home plate, the only "home" he gives this century.
- The slide.
- "Write me… And if it isn't?" / "It will be,".

---

## PATH TO 8.5
- **Characters 8.0 → 8.5 requires:** the census under cap and no replayed Ch.25 beat.
  - Apply F1 (cut the knees/belly replay), C1 (keeper gaze), C2 (delight), C3–C5 (stick and hat), C6–C8 (Lucius watching), C9–C13 ("guy" 7 → 3), C14–C16 (Mara's "And…?" triad), C17 (the stat-line list) and C18 (the Ch.25 landing frame).
  - All are cuts or one-clause recasts. Fenn's comedy, the keeper's swarm and Lucius's four words are untouched.
  - After the fix set every state in the census table is ≤3 and none is 3-in-500. The nameable-rule test passes for Fenn, Mara and the keeper.
- **Prose 8.0 → 8.5 requires:** the book's hygiene standard met and the craft slips gone, since the stopping sentences already qualify (l.324, l.378, l.408).
  - Apply E1–E67 (echo scan 83 → 0).
  - Apply P1–P2 (no tag adverb or emotion tag), P3–P4 (the Jupiter callback trusted, not explained), P5–P8 (plan echo, the decided-reflex, the doubled "walked backward").
  - The anchor and the protected passages keep their words.

**Projected after the fix set:** Originality 9.0 · Theme 9.0 · Characters 8.5 · Prose 8.5 · Pacing 8.5 · Emotion 9.0 · Immersion 9.0 (F6 corrects the orientation; it stays at 9.0 under the +0.5 rule) → **Floor 8.5 / Average 8.79**, Casual 9.0. Each dimension moves no more than +0.5.

## VERDICT
**POLISH.** Floor 8.0 (Characters, Prose) < 8.5. Casual 9.0 ✓. Pacing OK ✓. The mechanical exit code is clean, but the echo standard is ✗ (83).

Apply `apply_fixes.py` to `manuscript/chapters/chapter-27.md` (and, at the orchestrator's discretion, to `chapter-25.md` for X1), re-run `check_chapter.sh 27` and `--echoes 27`, then re-evaluate (cycle 1).

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

---

## Re-evaluation — cycle 1
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-24 | **Cycle:** 1
**Text evaluated:** `manuscript/chapters/chapter-27.md`, md5 `6441a8e8c82e78d686d560e2574895d8`. *(l.N below = line numbers in this file.)*

### Did the sets land as tested?
- **Ch.27** md5 `6441a8e8…` = the cycle-0 scratch result (`…/scratchpad/eval27/manuscript/chapters/chapter-27.md`). All 104 replacements landed; nothing else changed.
- **Ch.25** md5 `d2ceac85…` = the scratch result. X1 is on the page at l.258: "Shut tight. Cool under my hand with the sun on it, and not a breath out of it."
- **Measured on the real files:**
  - `check_chapter.sh 27` and `check_chapter.sh 25`: ALL MECHANICAL GATES CLEAN.
  - `tic_report.py --gate`: clean.
  - `--echoes 27`: **0**, with 0 command echoes and 0 spoken-line echoes.
  - Shape 7,527 words (99% of 7,600). Dialogue 36.1%. Median 17. Simile 22 (fig 3.7/1k). Em-dash 1 (l.382).
- **Coordinator items resolved on the page:**
  - **CH27-3:** the knees/belly replay is gone. l.142 ends "…like I owed it a letter." Fenn's "on your belly" at l.388 is his own crossing, which agrees with Ch.25.
  - **CH27-1:** Eros's door is "only cool" (l.336), "Still cool?" / "It was cool on the last Kalends." (l.484–486) and "Just that it's cool." (l.490). It is never cold. The live Cumae door is ranked above it ("Eros's is a little one. This was a beauty.").
  - **CH27-2:** "I sat at that mouth in it for hours… your breath smoked up there at sunup" (l.388) agrees with Ch.25 l.170 "I hiked up there first thing, in the cool".
- **CUT strings stay cut.** Grep shows 0 hits for every cycle-0 cut and for the Ch.25 and Ch.26 CUT strings. The cycle-0 cuts checked include: "for crying in the sink", "a sap", "gravely", "with great bitterness", "here was his Jupiter", "Jupiter sitting", "within five minutes", "before I had settled", "guy asleep", "billboard", "walking backward", "the whole racket", "intent on the harbor", "the fly", "the man in the window", "Like Eros's", "only colder", "Still cold", "slept up at that mouth", "Next thing", "snow up to here", "belly down", "Kneeling. Sideways", "his gaze kept", "brim pulled", "planted", "And it's dead", "And after", "And before", "Third base, nineteen". The banned words are also absent: Margaret, Vesuv-, mountain, tomb, Felix, arena, "years since"/"in all the years", "don't end up".
- **Nothing was planted by the swaps.** I read all six new strings in context and none echoes, reuses a frame or rebuilds a triad:
  - "Like the Marlboro man." is a period reference (1/2), a 1954 campaign, so it is fine for 1968.
  - "whoever drew it"
  - "In August you're frying"
  - "it's down this end"
  - "on your left"
  - "Then it's forty-one, and I'm in my shirtsleeves in Phocis with snow falling on me."

### Census re-check (same classifications as cycle 0)
| Character | State | Cycle-1 lines | Count | Verdict |
|---|---|---|---|---|
| Fenn | delight / grin | 112 delighted · 198 grinning · 342 grin in his voice | 3, spread | OK |
| Fenn | the stick | 86 possession · 138 thistle · 172 pointed · 414 drew · 496 fade | 5 (possession + 3 uses + fade, the cycle-0 ruling) | OK |
| Fenn | hat handled | 198 · 268 tipped · 370 clapped on | 3 | OK |
| Fenn | jenny's rope on wrist | 88 "round his wrist" · 108 · 496 "looped over his wrist" | 3, no verbatim pair | OK |
| Fenn | "guy(s)" | 124 · 156 · 420 | 3 | OK (the cap) |
| Fenn | tremor | 204 · 358 | 2 | OK |
| Keeper | eyes on the sea | 240 · 252 | 2 | OK |
| Keeper | pot lid | 240 · 248 (speech) · 450 | 3, spread | OK |
| Lucius | absorbed watching | 178 ducks · 258 doorway · 418 lines (404 listening) | 3 | OK |
| Lucius | "fist" | 36 · 76 · 84 · 258 · 430 | 5 (the cycle-0 target) | OK |
| Mara | "And…?" openers | 352 · 374 · 492 | 3, spread, no triad | OK |
| Mara | "before I decided" | 108 (the body rebel) | 1 | OK |
| Mara | fatigue | 274 · 300 · 398 | 3, spread | OK |
| Aelia | asleep / wakes | 178 · 318 · 386 / 232 · 478 | 3 / 2 | OK |

Every cycle-0 state is now at or under its cap, and no fix pushed a state over.

**Not counted at cycle 0, and found now: Fenn's word-doubling, a nameable habit.** There are nine doubled phrases in his speech:
- l.112 "All right, all right"
- l.138 "Sure. Sure you were."
- l.196 "Do me… do me, would you?"
- l.210 "Hold on, hold on, it works, it works sometimes"
- l.246 "It is, it is" (in his courtly Greek, where it is off-voice besides)
- l.268 "Step right up, step right up"
- l.412 "C'mere, come here"
- l.432 "Safe… Safe at home"
- l.446 "One more… One more inning"

Seven of these fall between l.112 and l.268, about 1,600 words. Ch.25's final page already has "Hey, hey", "cold, cold" and "it goes, it goes", so the habit runs across chapters. A reader could state the rule ("he says everything twice"), so it fails the nameable-rule test. The cycle-0 census should have caught it. I am raising it now and not later.

Two smaller repeats were also missed at cycle 0:
- the arm thrown out twice in 12 lines with the same verb (l.358 "He threw his hands out" / l.370 "He threw out an arm at the whole hill")
- "in Greek" twice in two sentences (l.422 / l.424)

### Nameable-rule test
- **Mara:** passes (the "And…?" run is fixed).
- **Keeper:** passes.
- **Lucius:** passes.
- **Valens:** passes. He reads ground literally ("It's resting the near hind", "She bites. Not hard.", "Hold that."), with no comparison and nothing remarked on.
- **Fenn:** passes on "guy", listing and the spent Ch.25 states. **Fails on doubling** → fixes D1–D7.

### Laws and closed frames (re-checked)
- **No foreshadowing:** clean. "Once we're back" and "If I am still here" are character belief, never narration.
- **Nobody names the mountain**, nobody says "Margaret", and there is no tomb.
- **No lists:** the Richie Allen line is now narrative ("He played third in sixty-four and got rookie of the year…").
- **Retired reflexes:** no anaphora triad, no negation opener, no closing aphorism.
- **Idiom pool, all within ≤2 book-wide:** no dice 1, get a load of 1, no great shakes 1, no kidding 1, you're the doctor 1, swell 2/2 (SPENT), buddy 2/2 (SPENT), kid 1, okay 1, fellow 1, anyhow 1, Mom 1. Horn & Hardart is held at "the automat".
- **"home":** Fenn says it twice. "That's home" is home plate (l.416). "Back home, at the mouth, I mean" (l.384) is 1968, which the bible allows: he never calls anywhere in *this* century home. Mara's "only I wanted to go home" (l.440) means Puteoli. That is a quiet, earned beat and should be kept.

### Scores — cycle 1 (+0.5 max per dimension)
| Dimension | C0 | **C1** | Evidence / cap |
|---|---|---|---|
| Originality | 9.0 | **9.0** | Unchanged: the dead door shown with pride, the lemon-meringue mutation, the diamond in the Sibyl's dust, the keeper's swarm. |
| Theme | 9.0 | **9.0** | Unchanged: "I'd check the hill mornings before I checked the weather." (l.376); "You sit up with a sick friend, don't you?" (l.362). |
| Characters | 8.0 | **8.0** | All cycle-0 failures are closed: F1, the census, "guy" 3, the "And…?" run, the stat list, the Ch.25 landing frame. Held at **8.0** by Fenn's doubling (9 in the chapter, a cross-chapter habit) under the nameable rule, the same cap practice as Ch.24–26 and cycle 0. Everything else is at 8.5+, and Fenn otherwise is the book's best: "it's like eating something that's still making up its mind" (l.146), "the left one went on going after the right had stopped" (l.358). |
| Prose & Voice | 8.0 | **8.5** | The hygiene standard is met: 0 echoes, no tag adverbs, no "And…?" triad, the Jupiter callback trusted (l.12), the backward-walk doubling recast (l.268/272). The stopping sentences stand: "until the hill was full of a small bone falling." (l.402); "a while past knowing and then a while past that" (l.318); "There had been another one… and it was a wall." (l.372). Ugly sentence: "The bread was dry and we ate it anyway." (l.178). Voice under pressure: l.108–110 and l.364. #11 is at 2 (l.204, l.398), under the cap. |
| Pacing | 8.5 | **8.5** | 7,527 words (99%), 36.1% dialogue, the same handoffs (Ch.26 collage at 12% → walk at 36% → Ch.28 bout). The cave stillness runs l.310–394. Not 9.0: S2's oysters → lunch stretch. **PACING OK.** |
| Emotion | 9.0 | **9.0** | The anchor paragraph is verbatim (l.318). "Of you." (l.222). The coat (l.388–392) against the carbon withheld (l.394). |
| Immersion | 9.0 | **9.0** | F6 fixed the orientation ("Along the left-hand wall", l.264; "on your left the windows", l.268): the sea is west, and the sea is on the left walking in. Held at 9.0, with no comp case made for 9.5. |
| **FLOOR** | 8.0 | **8.0** | Characters |
| **AVERAGE** | 8.64 | **8.71** | (9.0 + 9.0 + 8.0 + 8.5 + 8.5 + 9.0 + 9.0) / 7 |

- **Casual Reader: 9.0.** The doubling would not stop this reader. It costs the Critic and the Devoted Reader, who hear the habit, and it fails the book's law.
- **CVI-Launch: 9.4.** 0.2(8) + 0.2(10) + 0.2(9) + 0.2(7.5) + 0.1(10) + 0.1(10) = 8.9, + 0.5 for a strong anchor.
- **CVI-Legacy: 7.1.** Originality 9.0 · Theme 9.0 · Vocabulary 3 · Re-read 7 · Identity 5, at default weights.
- **Anti-AI:** 8 patterns present at minor weight, plus traces (#6 at 3 "And" openers in speech; #10 "delighted" once). This is the commercial clean band. #8 is cleared.

### Fix set — cycle 1 (TESTED)
Script: `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes27b/apply_fixes.py <chapter-27.md>`. It makes **9 replacements** on the md5 `6441a8e8…` page. Each must match exactly once or the script aborts and writes nothing. A re-run aborts safely; this was tested.

**Tested on a fresh scratch copy** of the book folder (`…/scratchpad/eval27b/`):
- `check_chapter.sh 27`: **ALL MECHANICAL GATES CLEAN**.
- `--gate`: clean.
- `--echoes 27`: **0**, with 0 command and 0 spoken-line echoes.
- Shape 7,502 words, dialogue 36.0%.
- Result md5 `efbfc81a78a19b51537d0918475f9706`.
- A first draft of G2 ("said Fenn, and pointed") tripped the tic gate ("said fenn and" 3× book-wide). It was replaced with "said Fenn, pointing." and re-tested.

| ID | Location | Problem type | Now | Why | Revision (exact, in script) | Project rule? |
|---|---|---|---|---|---|---|
| D1 | l.112 | Character (nameable) | "All right, all right, I'm coming." | Doubling 9× | "All right, I'm coming." | Yes: Fenn's doubled phrases ≤1 per chapter (a formula like "Step right up", an umpire's call or a quotation is not counted) |
| D2 | l.138 | Character | "Sure. Sure you were." | Doubling | "Sure you were." | — |
| D3 | l.196 | Character | "Do me," … "do me, would you?" | Doubling | "Do me," Fenn said, "would you? One, …" | — |
| D4 | l.210 | Character | "Hold on, hold on, it works, it works sometimes" | Doubling twice in one line | "Hold on, it works, it works sometimes" (the self-correction stays: it is the frame's point) | — |
| D5 | l.246 | Character / Voice | "It is, it is," said Fenn. | Doubling, and in his formal Greek | "It is," said Fenn. | — |
| D6 | l.412 | Character | "C'mere, come here, buddy" | Doubling | "C'mere, buddy," | — |
| D7 | l.446 | Character | "One more," he said. "One more inning, come on, Mom," | Doubling | "One more inning," he said. "Come on, Mom," ("I gave them one more." still answers it) | — |
| G1 | l.370 | Character (gesture) | "That it was here!" He threw out an arm at the whole hill. "One right here…" | "threw" an arm twice in 12 lines (l.358) | "That it was here! One right here…" (one speech; the hat clapped on still gives him his body) | No |
| G2 | l.424 | Style | "Run!" said Fenn in Greek, and pointed. | "in Greek" twice in two sentences (l.422) | "Run!" said Fenn, pointing. (Lucius running shows he understood) | No |

**Kept on purpose (four, each doing a different job):**
- "it works, it works sometimes": the correction
- "Step right up, step right up": the barker's formula
- "Safe … Safe at home": the call, then the crowd
- "Not hard … Not hard, says the gladiator": quoting Valens

**Projected after fixes27b:** Characters **8.5** (+0.5; the census and the nameable test are both clean) → **Floor 8.5 / Average 8.79**, Casual 9.0, pacing OK.

### PATH TO 8.5
- **Characters 8.0 → 8.5 requires** Fenn's doubling cut to the four that do work: apply D1–D7, plus G1 for the doubled arm-throw. No other change. Fenn's comedy, the Zippo frame and the anchor keep their words.

### Bookkeeping for finalize (carry to the PASS cycle; not page edits)
- **Header comment (l.6) is stale.** It reads shape 7,681, Em-dash 0, median 18, sections 983/2,502/3,076/1,411 and dialogue 36.1%. Refresh it from the final measures and log the cycle-0 and cycle-1 sets.
- **Bible:** the Ch.27 Fenn block still quotes cut and changed strings. These include: "walks the way he talked", the wick line, "slept in it a week", "the notebook went in the pocket" (the page has "cigarettes in the pocket"), "I'd check the hill in the morning", "Third base, nineteen sixty-four…", "Hold on, hold on…", "for crying in the sink", "a sap 1 (→ 2/2)", and "fellow 1" (still 1). The full sync list is due at PASS.
- **New guard for Ch.28+:** Fenn's doubled phrases ≤1 per chapter (book-wide habit: Ch.25 3, Ch.27 9 → 1 after the fixes).

### VERDICT
**POLISH.** Floor 8.0 (Characters) < 8.5. Casual 9.0 ✓. Pacing OK ✓. Gates clean ✓, with echoes at 0.

Apply `fixes27b/apply_fixes.py` to `manuscript/chapters/chapter-27.md`, re-run `check_chapter.sh 27` and `--echoes 27`, then re-evaluate (cycle 2). Expect a short cycle: one dimension and nine clause-level edits.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

---

## Re-evaluation — cycle 2
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-24 | **Cycle:** 2
**Text evaluated:** `manuscript/chapters/chapter-27.md`, md5 `efbfc81a78a19b51537d0918475f9706`. *(l.N = line numbers in this file.)*

### Did the cycle-1 set land, and did it plant anything?
- **Landed exactly.** The md5 equals the cycle-1 scratch result (`…/scratchpad/eval27b/`), so D1–D7, G1 and G2 are on the page and nothing else changed.
- **Measured on the real file:** `check_chapter.sh 27` ALL MECHANICAL GATES CLEAN. `--gate` clean. **`--echoes 27`: 0**, with 0 command echoes and 0 spoken-line echoes. Shape 7,502, dialogue 36.0%, median 17, simile 22 (fig 3.7/1k), em-dash 1 (l.382).
- **Planted nothing.** All nine edits were read in context:
  - G2 "said Fenn, pointing." makes Fenn's second pointing in the chapter (l.172 is the first). That is 2, which is fine.
  - D3 "Fenn said, \"would you?" makes "would you" 2 (with l.112).
  - D7's "Come on, Mom" is counted in the "Come on" census below. It is one of three uses, but it was not the one planted, because "Come on" at l.286 and l.304 were already on the page.
- **Doubling, measured on the page with the cycle-1 exclusions (formula, umpire's call, quotation, onomatopoeia):** 1 counted ("it works, it works sometimes", l.210). The raw count is 4 (l.210, 260, 268, 432), plus "slap, slap" (a sound).

### Census — narrated states (cycle-0 classifications, re-run)
Every row of the cycle-1 table holds; only speech lines changed. Fenn's delight is at 3, stick 5, hat 3, rope 3, "guy" 3, tremor 2, squint 2 (208, 286), leaning 2 (282, 384), laughing 2 (384, 436) and shouting 2 (298, 430). The keeper's sea-gaze is 2 and his pot lid 3, spread. Lucius's watching is 3 and "fist" 5. Mara's "before I decided" is 1, fatigue 3, spread, and her watching 3, spread (318, 440, 496). Aelia: 3 / 2. Fenn's arm thrown is 1 (G1). "in Greek" is 4 in narration, spread (118, 298, 308, 422), and functional. **No narrated-state failures.**

### Census — speech habits, EVERY speaker, one pass (new spec: >2 of one habit fails)
**Classification rules, fixed here so later cycles do not re-litigate them:**
- A *habit* is a discourse marker or interjection used as an opener (So / And / Come on / Now / Hey / Look), a stock exclamation (No kidding / No dice / Nope), a vocative or courtesy tag, a pet intensifier or a pet construction, a doubled phrase, or a recurring question shape.
- Pronoun-copula openers ("That's…", Valens's "It's…") are grammar, not habit. Each of Fenn's seven "That's" lines judges a different thing.
- Formulas (the barker's "No refunds" / "Step right up"), an umpire's call, a quotation and onomatopoeia are excluded from the doubling count, as at cycle 1.
- A walk-on repeating the noun of his grief (the keeper's "Misenum") is his subject, not a habit.

| Speaker | Habit | Lines | Count | Verdict |
|---|---|---|---|---|
| Fenn | hyperbolic "you could [do X with it]" as his measure of things | 112 Spectrum · 124 spoon · 334 side of beef · 350 set a watch · 388 anchored a destroyer (124 "you could look your slice over" is literal, not counted) | **5** | **FAILS**: a nameable rule ("he sizes everything by what you could do with it") → S1–S3 → 2 (beef, destroyer) |
| Fenn | intensifier "the whole …" | 10 of Jupiter · 112 floor · 268 deck · 272 fortune · 334 hill | **5** | **FAILS** → S1, S4, S5 → 2 (Jupiter, hill) |
| Fenn | "So she…" retort that turns Mara's objection into a joke | 30 "So she won't mind company" · 174 "So much for that" · 286 "So she'll love it later" | **3** (30 and 286 are the same joke template) | **FAILS** → S7 → 2 |
| Fenn | "Come on" | 286 · 304 · 446 | **3** | **FAILS** → S8 → 2 |
| Fenn | courtly "sir" to Valens | 44 · 48 · 54 (within ~150 words) | **3** | **FAILS** → S9 → 2 |
| Fenn | doubled phrases | counted 1 (210) / raw 4; 260 and 268 form a doubled pair 8 lines apart | 1 | OK by rule. S10 cuts "step right up" once anyway: raw 3, and the cluster is broken |
| Fenn | "No [noun]" stock tag | 160 No kidding · 384 No dice (268 "No refunds" is barker formula) · 320 "Nope" (different form) | 2 | OK |
| Fenn | "would you" tag | 112 · 196 | 2 | OK |
| Fenn | "[X] would." retort | 164 "Who would." · 472 "He would." | 2 | OK |
| Fenn | vocatives | kid 1 · buddy 1 · Mom 1 · folks 2 · my friend 1 | each ≤2 | OK |
| Fenn | "guy" | 124 · 156 · 420 | 3 | OK (the project cap is 3) |
| Fenn | idiom pool | no dice, get a load of, no great shakes, no kidding, you're the doctor, kid, okay, fellow, anyhow, Mom: 1 each; swell 2/2; buddy 2/2 | — | OK |
| Fenn | "like" comparisons in speech | ~12, from varied sources (pop culture, trade, domestic, Navy) | — | Voice, not a single template. OK |
| Mara | two-part question (question + fragment clarifier) | **352 "And you? That morning?" · 356 "Why? What killed it?" · 360 "Did you keep coming? After?"** · 368 "Show me what? That it's dead?" (364 is a re-ask under pressure, a different shape) | **4, in 5 consecutive lines** | **FAILS** (3 inside ~500 words; #8 in speech) → S11–S12 → 2 (356, 368) |
| Mara | "And…?" opener | 352 · 374 · 492 | **3** | **FAILS** under the new spec (cycle 1 passed it at the old cap) → S11 → 2 |
| Mara | re-asked question | 24/32 "What's at Cumae?" · 364 "why bring me" | 2 | OK |
| Mara | "…too" | 270 · 284 | 2 | OK |
| Mara | statement + dry fragment ("Long before me." / "To a king." / "Twice.") | 158 · 270 · 288 | 3, spread over ~130 lines | Syntax, which the law allows as voice; not one fixed phrase. OK (watch) |
| Valens | imperatives / ground-literal declaratives | "Bring the boy's hat." · "Hold that." · "It's resting… It's favored…" · "It's one day." | ≤2 per form | OK |
| Keeper | "Misenum" | 248 · 252 ×2 · 452 | his grief's subject | OK by rule. The utterance-doubling at 252 happens once |
| Keeper | "month" | 244 · 452 | 2 | OK |
| Lucius | single words (Smoke / Duck / Bone / Again) | design (cycle 0) | — | OK |
| Scrapers / sailor | one line / none | — | — | OK |
| Narrator | "whole" | 144 · 280 · 372 · 422 · 436 | 5 in 7.5k words, spread | Not a speech habit, and the gate is clean. OK |

### Nameable-rule test
- **Valens, the keeper, Lucius:** pass.
- **Fenn:** fails on the "you could" measure and "the whole", and is at 3 on the "So" retort, "Come on" and "sir".
- **Mara:** fails on the run of two-part questions at l.352–368 and is at 3 on "And…?".

All of these are clause-level fixes.

### Scores — cycle 2 (+0.5 max per dimension)
| Dimension | C1 | **C2** | Evidence / cap |
|---|---|---|---|
| Originality | 9.0 | **9.0** | Unchanged: the dead door shown with pride (l.370), the lemon-meringue mutation (l.116/126), the diamond in the Sibyl's dust (l.414), the keeper's swarm (l.248–256). |
| Theme | 9.0 | **9.0** | Unchanged: "I'd check the hill mornings before I checked the weather." (l.376); "You sit up with a sick friend, don't you?" (l.362). |
| Characters | 8.0 | **8.0** | The doubling is closed (1 counted, l.210) and the narrated-state census is clean. Held at **8.0** by the speech-habit census: Fenn's hyperbolic "you could" 5 and "the whole" 5, both nameable; "So" retort / "Come on" / "sir" at 3 each; Mara's two-part questions 4 in 5 consecutive lines and "And…?" 3. The cap practice is the same as Ch.24–26 and cycles 0–1. Everything else is 8.5+: "it's like eating something that's still making up its mind" (l.146); "the left one went on going after the right had stopped" (l.358). |
| Prose & Voice | 8.5 | **8.5** | Holds: 0 echoes; stopping sentences at l.318, l.372 and l.402; ugly sentence at l.178; voice under pressure at l.108–110 and l.364. #11 at 2. |
| Pacing | 8.5 | **8.5** | 7,502 words (99%), dialogue 36.0%, handoffs unchanged (Ch.26 collage 12% → walk 36% → Ch.28 bout). **PACING OK.** |
| Emotion | 9.0 | **9.0** | The anchor (l.318) is verbatim; "Of you." (l.222); the coat against the carbon (l.388–394). |
| Immersion | 9.0 | **9.0** | Gallery orientation correct (l.264/268). The Solfatara, Avernus and the dromos are unchanged. |
| **FLOOR** | 8.0 | **8.0** | Characters |
| **AVERAGE** | 8.71 | **8.71** | (9.0 + 9.0 + 8.0 + 8.5 + 8.5 + 9.0 + 9.0) / 7 |

- **Casual Reader: 9.0.** None of these habits would stop this reader.
- **CVI-Launch: 9.4.** 0.2(8) + 0.2(10) + 0.2(9) + 0.2(7.5) + 0.1(10) + 0.1(10) = 8.9, + 0.5 for a strong anchor.
- **CVI-Legacy: 7.1.** Default weights: 9.0 × .30 + 9.0 × .25 + 3 × .20 + 7 × .15 + 5 × .10.
- **Anti-AI:** 8 patterns at minor weight, in the commercial clean band. After the fixes, #6 drops to 2 "And" openers in speech and #8 has no speech parallel run.

### Fix set — cycle 2 (TESTED)
Script: `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes27c/apply_fixes.py <chapter-27.md>`. It makes **11 replacements** on the md5 `efbfc81a…` page. Each must match exactly once or the script aborts and writes nothing; a re-run aborts safely (tested).

**Tested on a fresh scratch copy** of the book folder (`…/scratchpad/eval27c/`):
- `check_chapter.sh 27`: **ALL MECHANICAL GATES CLEAN**.
- `--gate`: clean.
- **`--echoes 27`: 0**, with 0 command and 0 spoken-line echoes.
- Show/tell row: 7,499 words, dialogue 35.8% (band 35–45). Shape_check: 7,481, 3 breaks, I-statement → long-fade, unchanged.
- Result md5 **`1214428ba546532d04def00db9f0f2e3`**.

**Rejected drafts (gate- or hand-caught):**
- "What did you do, that morning?": echo, Ch.5.
- "Where did you go, that morning?": "where did you" / "did you go" reach 3× book-wide.
- "there's room for the Spectrum under here": rebuilds Fenn's own "there's room for two in here" (l.286) frame.

| ID | Location | Problem type | Now | Why | Revision (exact, in script) | Project rule? |
|---|---|---|---|---|---|---|
| S1 | l.112 | Character (speech habit) | "The whole floor's hollow, you could put the Spectrum under here and have room left over for the ice," | "you could" 5; "whole" 5 | "The floor's hollow, the Spectrum would fit under here, ice and all," | Yes: no speaker carries more than 2 of one speech habit (opener, exclamation, tag, pet construction, question shape) |
| S2 | l.124 | Character | "a lemon meringue you could've stood a spoon up in," | "you could" | "a lemon meringue so stiff it would hold a spoon upright," | — |
| S3 | l.350 | Character | "the same cold, you could have set a watch by it, and then one morning" | "you could" | "the same cold, and then one morning" | — |
| S4 | l.268 | Character | "shuffles the whole deck," | "whole" | "shuffles the deck," | — |
| S5 | l.272 | Character | "he pays the whole fortune for the last few." | "whole" | "he pays the full price for the last few." | — |
| S7 | l.286 | Character | "So she'll love it later." | The "So she…" retort ×2 (with l.30), "So" opener 3 | "She can love it later." | — |
| S8 | l.304 | Character | "Come on, it's down this end," | "Come on" 3 | "It's down this end," | — |
| S9 | l.48 | Character | "He shall ride, sir. I will hire an ass." | "sir" 3 in ~150 words | "He shall ride. I will hire an ass." | — |
| S10 | l.268 | Character | "Step right up, step right up, ladies and gentlemen," | Raw doubling 4, with a doubled pair 8 lines from l.260 | "Step right up, ladies and gentlemen," | — |
| S11 | l.352 | Character / Style #8 | "And you? That morning?" | Two-part question run (352/356/360/368); "And…?" 3 | "What then, that morning?" | — |
| S12 | l.360 | Character | "Did you keep coming? After?" | Two-part run | "Did you keep coming after?" | — |

**Untouched:** the opener, the anchor paragraph, the Zippo frame, "Door. Nail. No?", the coat, the slide and the long fade.

**Projected after fixes27c:** Characters **8.5** (+0.5: both censuses and the nameable test clean) → **Floor 8.5 / Average 8.79**. Casual 9.0. Pacing OK.

### PATH TO 8.5
- **Characters 8.0 → 8.5 requires:** apply S1–S12. That alone does it; nothing else on the page holds the floor.

### Carry to the PASS cycle (bookkeeping, not page edits)
- Everything listed in cycle 1's "Bookkeeping for finalize" still stands: the l.6 header refresh, the Ch.27 Fenn block re-sync and the CUT strings.
- **Add to the bible at PASS:**
  - Fenn's speech-habit ledger for Ch.27: "you could" 2, "whole" 2, "So" 2, "Come on" 2, "sir" 2, doubling 1, "guy" 3.
  - Mara's: "And…?" 2, two-part questions 2.
  - The CUT strings from S1–S12.
- **New guard:** the per-speaker speech-habit cap (≤2 per habit per chapter). Fenn's hyperbolic "you could" is at-risk book-wide.

### VERDICT
**POLISH.** Floor 8.0 (Characters) < 8.5. Casual 9.0 ✓. Pacing OK ✓. Gates clean ✓, with echoes at 0.

Apply `fixes27c/apply_fixes.py` to `manuscript/chapters/chapter-27.md` and confirm md5 `1214428b…`. Re-run `check_chapter.sh 27` and `--echoes 27`, then re-evaluate (cycle 3). The census is now exhaustive for narrated states and speech habits, so cycle 3 should only need to verify.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

---

## Re-evaluation — cycle 3
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-24 | **Cycle:** 3 of 5
**Text evaluated:** `manuscript/chapters/chapter-27.md`, md5 `1214428ba546532d04def00db9f0f2e3`. *(l.N = line numbers in this file.)*

### Did the cycle-2 set land?
- **Landed exactly.** The md5 equals the cycle-2 scratch result (`…/scratchpad/eval27c/`). All 11 strings are on the page:
  - S1 (l.112), S2 (l.124), S3 (l.350), S4 (l.268), S5 (l.272), S7 (l.286), S8 (l.304), S9 (l.48), S10 (l.268), S11 (l.352), S12 (l.360).
  - Nothing else changed.
- **Measured on the real file:**
  - `check_chapter.sh 27`: ALL MECHANICAL GATES CLEAN.
  - `tic_report.py --gate`: clean.
  - **`--echoes 27`: 0**, with 0 command echoes and 0 spoken-line echoes.
  - Show/tell row: 7,499 words, dialogue 35.8%. Metaphor row: 7,481, fig 3.7/1k, simile 22, median 17. Shape CLEAN.

### Did the set plant anything? Yes: two items, both inside S1/S2 (l.112–124)
Each item was checked by hand under the cycle-2 rules: a habit is a pet construction or a recurring shape, and the cap is >2 per chapter. No class was reclassified.

1. **S1 and S2 swapped the marker and kept the habit.** Cycle 2 named the failing habit as the nameable rule *"he sizes everything by what you could do with it"*. "you could" was only its marker. S1 and S2 removed the words and kept the sizing:
   - l.112 "the Spectrum would fit under here, ice and all" is still the capacity hyperbole.
   - l.124 "so stiff it would hold a spoon upright" is the "you could stand a spoon in it" idiom re-worded.
   - **The "you could" construction is now 2** (l.334 side of beef; l.388 destroyer), which is the cap.
   - **The capacity-sizing hyperbole is still 4** (112, 124, 334, 388), and 112 and 124 are about 250 words apart in consecutive Fenn speeches. The rule is still nameable, and the reader still hears it where it was loudest. *A fix that creates a finding is not a fix*, and a fix that re-words a habit is not a fix either.
2. **S1 planted a tag pair.**
   - "ice and all" (l.112) pairs with "stamp and all" (l.142), 30 lines later, in the same voice.
   - With "the chin and everything" (l.160), that makes **3 general-extender tags in Fenn's speech in ~550 words**. This is a pet construction and fails >2.
   - The barker's "and so on and so forth" (l.308) is formula and is excluded, as cycle 2 excluded "Step right up" and "No refunds".
   - Cycle 2's S1 source line read "room left over for the ice", so the pair did not exist before S1.

Every other S-string reads clean in context:
- "She can love it later." makes "So" 2 (l.30, l.174).
- "It's down this end," is a pronoun-copula opener, which counts as grammar.
- "What then, that morning?" is one question, not question + fragment, so the two-part count is 2 (l.356, l.368).
- "Did you keep coming after?" is one question.
- "the full price" and "shuffles the deck" are fine.

### Census re-check (cycle-0 and cycle-2 classifications, unchanged)
**Narrated states:** every row holds, because S1–S12 touched only speech.
- Fenn: delight 3 (112, 198, 342), stick 5 (86, 138, 172, 414, 496; the cycle-0 ruling), hat 3, rope 3, tremor 2, squint 2, leaning 2, laughing 2, shouting 2, arm thrown 1.
- Keeper: sea-gaze 2, pot lid 3 spread.
- Lucius: watching 3, "fist" 5.
- Mara: "before I decided" 1, fatigue 3 spread, watching 3 spread.
- Aelia: 3 / 2.
- **No narrated-state failure.**

**Speech habits:**

| Speaker | Habit | Count now | Verdict |
|---|---|---|---|
| Fenn | "you could" construction | 2 (334, 388) | OK |
| Fenn | capacity-sizing hyperbole (the cycle-2 nameable rule) | **4** (112, 124, 334, 388) | **FAILS** → T1–T2 → 2 |
| Fenn | general-extender tag ("X and all" / "and everything") | **3** (112, 142, 160) in ~550 words | **FAILS** (planted by S1) → T1 → 2 |
| Fenn | "the whole" | 2 (10, 334) | OK |
| Fenn | "So" retort | 2 (30, 174) | OK |
| Fenn | "Come on" | 2 (286, 446) | OK |
| Fenn | "sir" | 2 (44, 54) | OK |
| Fenn | doubled phrases | 1 counted (210) | OK |
| Fenn | "guy" | 3 (124, 156, 420) | OK (project cap 3) |
| Fenn | "No [noun]" / "would you" / "[X] would." / vocatives / idiom pool | each ≤2 | OK |
| Mara | "And…?" | 2 (374, 492) | OK |
| Mara | question + fragment | 2 (356, 368) | OK |
| Mara | statement + dry fragment | 3, spread over ~130 lines | watch (syntax), as at cycle 2 |
| Valens / keeper / Lucius / scrapers / sailor | — | — | OK, as at cycle 2 |

### Scores — cycle 3 (+0.5 max per dimension)
| Dimension | C2 | **C3** | Evidence / cap |
|---|---|---|---|
| Originality | 9.0 | **9.0** | Unchanged: the dead door shown with pride (l.370); "Lemon meringue," → "I let him have the lemon." (l.116/126); the diamond in the Sibyl's dust (l.414); the keeper's swarm (l.248). |
| Theme | 9.0 | **9.0** | "I'd check the hill mornings before I checked the weather." (l.376); "You sit up with a sick friend, don't you?" (l.362). |
| Characters | 8.0 | **8.0** | Every cycle-2 marker count is at or under cap, and the narrated census is clean. Held at **8.0** by the sizing habit, which survives re-wording at 4 with a back-to-back pair at l.112/124, and by the general-extender tag at 3 that S1 planted. This is the same cap practice as cycles 0–2. Everything else is 8.5+: "it's like eating something that's still making up its mind" (l.146); "the left one went on going after the right had stopped" (l.358). |
| Prose & Voice | 8.5 | **8.5** | Holds: 0 echoes; stopping sentences at l.318, l.372 and l.402; ugly sentence at l.178; voice under pressure at l.108–110 and l.364. |
| Pacing | 8.5 | **8.5** | 7,499 words (99%), dialogue 35.8% (band 35–45), handoffs unchanged. **PACING OK.** |
| Emotion | 9.0 | **9.0** | The anchor (l.318) is verbatim; "Of you." (l.222); the coat against the carbon (l.388–394). |
| Immersion | 9.0 | **9.0** | Unchanged. |
| **FLOOR** | 8.0 | **8.0** | Characters |
| **AVERAGE** | 8.71 | **8.71** | |

- **Casual Reader: 9.0.** None of this would stop this reader.
- **CVI-Launch: 9.4.** 0.2(8) + 0.2(10) + 0.2(9) + 0.2(7.5) + 0.1(10) + 0.1(10) = 8.9, + 0.5 for a strong anchor.
- **CVI-Legacy: 7.1.** Default weights.
- **Anti-AI:** 8 patterns present at minor weight. This is the commercial clean band.

### Fix set — cycle 3 (TESTED)
Script: `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes27d/apply_fixes.py <chapter-27.md>`. It makes **2 replacements** on the md5 `1214428b…` page. Each must match exactly once or the script aborts and writes nothing. A re-run aborts safely; this was tested.

**Tested on a fresh scratch copy** of the book folder (`…/scratchpad/eval27d/`):
- `check_chapter.sh 27`: **ALL MECHANICAL GATES CLEAN** (voice-wear strict clean; shape CLEAN).
- `--gate`: clean.
- **`--echoes 27`: 0**, with 0 command and 0 spoken-line echoes.
- 7,490 words (show/tell row), dialogue 35.8%. Metaphor row: 7,472, fig 3.9/1k (gate 4.0), simile 23, median 17.
- Result md5 **`e3e00dd1b2e9d90078db3e6611acf78e`**.

| ID | Location | Problem type | Now | Why | Revision (exact, in script) | Project rule? |
|---|---|---|---|---|---|---|
| T1 | l.112 | Character (speech habit, planted) | "The floor's hollow, the Spectrum would fit under here, ice and all, and the bath keeper…" | Capacity sizing (4 with 124/334/388) re-worded, not cured; "ice and all" pairs with l.142 "stamp and all" (general extenders 3) | "The floor's hollow, it booms like the Spectrum when the Flyers score, and the bath keeper…" (the Spectrum becomes a sound comparison for the boom; the Flyers played there from Oct 1967, before Fenn's July 1968 crossing) | Yes: a habit fix must remove the habit, not its marker words |
| T2 | l.124 | Character | "a lemon meringue so stiff it would hold a spoon upright, with the meringue on top a mile high" | The 2nd capacity hyperbole in ~250 words | "a lemon meringue with the meringue piled a mile high" ("a mile high" carries the pie; "a mile" is 2 in his speech with l.436 "Safe by a mile") | — |

After T1–T2:
- capacity sizing 2 (beef, destroyer; both "you could")
- "and all" 1
- general extenders 2
- Fenn's "like" comparisons in speech 8 (varied sources; voice)

Nothing else is touched: the opener, anchor, Zippo frame, doornail, coat, slide and fade keep their words.

**Projected after fixes27d:** Characters **8.5** (+0.5) → **Floor 8.5 / Average 8.79**. Casual 9.0. Pacing OK.

### PATH TO 8.5
- **Characters 8.0 → 8.5 requires:** apply T1–T2. Nothing else on the page holds the floor. The cycle-4 evaluation should be a verification only: md5 `e3e00dd1…`, gates, and a re-read of l.112–160.

### Carry to the PASS cycle (bookkeeping, not page edits)
Everything from the cycle-1 and cycle-2 carry lists still stands. Add:
- The bible's Ch.27 lemon-meringue quote (character-bible.md ~l.1834, "you could…") is stale.
- The Spectrum is now "booms like the Spectrum when the Flyers score". The Flyers are a new period reference (1/2).
- CUT strings from S1/S2/T1/T2: "would fit under here", "ice and all", "so stiff it would hold a spoon upright", "room left over for the ice", "stood a spoon up".
- New guard: Fenn's capacity-sizing hyperbole ≤2 per chapter, whatever the wording.

### VERDICT
**POLISH.** Floor 8.0 (Characters) < 8.5. Casual 9.0 ✓. Pacing OK ✓. Gates clean ✓, with echoes at 0.

Apply `fixes27d/apply_fixes.py`, confirm md5 `e3e00dd1…`, re-run `check_chapter.sh 27` and `--echoes 27`, then re-evaluate (cycle 4 of 5).

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
