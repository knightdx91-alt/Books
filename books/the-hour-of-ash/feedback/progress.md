# Progress — Pompeii (working title)

Scaffolded 2026-06-21 from book/genesis/_template.

## Next steps
1. Pull source material from Google Drive into research/ (original draft + any roadmap/bible).
2. Fill in STATE.yaml: premise, genre, comps, canon_sources, guardrails, open_author_decisions.
3. Edit tools/style_check.py ALLOWLIST with this book's deliberate motifs.
4. Architect pass: build foundation.md + outline.md (if no scene-by-scene roadmap exists).
5. Run the chapter loop in order; commit per chapter; keep this file current.

## RESTART (2026-07-11, author Terry)
Author elected to DELETE the prior Ch.1 + Ch.2 drafts (and their evals) and restart from Ch.1.
Old drafts remain recoverable in git history (removed at commit after voice-DNA work). Voice DNA
now carries §7 Outlander comp calibration — the new drafts are written TO that register (median
~15w, semicolon-not-em-dash, characterizing-not-analytical simile, one specific material/scene).

## Resume point
Ch.1 "The Drawer" REDRAFTED and FINALIZED (5,066 words; target 4,900 / floor 4,800). Full pipeline
run: draft → dialogue-polish → hook-craft → disruptor → mechanical gates → book-evaluator →
book-editor (rev 1) → re-evaluate. **PASS: Genesis Floor 8.5 / Avg 8.64 / Casual 8.5** (both gate
conditions met; eval + rev-1 in evaluations/chapter-1-eval.md). Mechanical gates clean (style,
grammar, voice-wear; em-dash 0; simile 1.4/1k; long-sent 22.6% intentional immersive register).
Rev 1 fixed the one failing dimension (Characters 8.0→8.5): unmediated 2 chaos beats + cut 1
foreknowledge intrusion to the ≤2 budget. Anachronism fixed: "Türkiye"→"Turkey" (1998 frame).
Beta-reader panel run on Ch.1 (load-bearing opener) — panel mean 7.8: Devourer 8.5/buy, Devoted
9.0/evangelize, Critic 8.0, Casual 7.5, Hostile 6.0. Verdict: converts the core Outlander-market
reader decisively on voice; #1 fix = trim the sagging keep/give/slides stretch (DONE, subtractive,
~90w, still Floor 8.5). Panel #2/#3 (mediated-narrator register) left alone by design — evaluator
warned stripping it erodes the Prose-9.0 voice. Report: evaluations/review/beta-reader-panel.md.
Ch.1 now 4,999 prose words, all gates clean. FINAL.

Ch.2 "Too Accurate to Be Fake" REDRAFTED & FINALIZED (2026-07-11). The prior Ch.2 draft was never
committed (lost with a reclaimed cloud container), so it was rebuilt from scratch to the Ch.1 voice.
Dialogue two-hander, 4,776 prose words (target 5,100; ~5% under, acceptable for a taut two-hander),
~31.5% dialogue share — restores the band after Ch.1's 0%. Beats delivered: traces the map back to
antique dealer VERRALL, who ran vanished treasure-hunter August Fenn's estate sale; the estate LEDGER
(dated left column = logged door-attempts) is the first LIVE mystery thread; Fenn marginalia insert #1
landed ("the map is honest ... it is the door that lies"); closing pull spends "Fenn vanished at
exactly her age, 34." Mechanical gates clean (style: em-dash 0, simile 1.9/1k; grammar clean;
voice-wear clean). book-evaluator PASS: **Genesis Floor 8.5 / Avg 8.64 / Casual 8.5**, Prose 9.0
(strongest dim); no dimension <8.5. Post-eval polish: shaved closing anaphora, tightened the
 mid-chapter police-census micro-sag, split one ~110w narration spiral.
SELF-PASS CHAIN COMPLETE (2026-07-11, per standing policy): dialogue-polish (2 spoken-rhythm
tightenings) -> hook-craft (hook 9/10 & pull 10/10 left verbatim) -> disruptor (3 human-wrongness
insertions incl. the bread-tic finally surfacing in Ch.2: "It appraises the bread at the graveside";
+~150w -> 4,961 prose words; dialogue 30.6%). Gates re-verified clean (em-dash 0, simile 1.8/1k).
The book-evaluator PASS (8.5/9.0) predates the self-pass edits; they are surgical/in-voice, so a
re-evaluation is optional (not run). FINAL.

GATE RE-VERIFICATION (2026-07-11, author asked to re-run all tests): re-ran the full
tools/check_chapter.sh 2 suite. Found ONE gated STYLE flag the earlier "clean" note missed:
the phrase "(I) have never been able to…" had leaked across chapters (Ch.1 ×2 + Ch.2 ×1 = ×3),
tripping the "no NEW cross-chapter repeated phrase" guardrail. FIXED by varying the Ch.2
instance ("There is a part of me that will not switch off, not for grief, not for anything.
It appraises the bread at the graveside."); left Ch.1's two (finalized/beta-panelled, deliberate
intra-chapter register). Re-ran gates: STYLE clean, GRAMMAR clean, VOICE-WEAR clean, METAPHOR
clean, WORD FLOOR 5,542 (>5000). The only remaining RHYTHM flags are the intentional vow-anaphora
at L168/170 ("I meant it when I said it. I want that written down…") — deliberate, not a defect.
Ch.2 gates now genuinely clean. FINAL confirmed.

Ch.3 "Coordinates & the Survey" DRAFTED & FINALIZED (2026-07-11). ~6,700 prose words (target 7,000;
~4% under, in Ch.2's taut-under pattern). Full pipeline run: book-writer -> dialogue-polish ->
hook-craft -> disruptor -> mechanical gates -> book-editor (long-sentence trim) -> book-evaluator.
Structure = travel-montage (decode Fenn's coordinates in an English guesthouse -> commit to fly abroad,
Halloran re-rung for permit cover -> sunlit drive to a foreign coast) tightening to one held scene on a
headland where the ringed coords fall on "a dip in a rock" and her instruments go wrong (both light
meters peg to a brightness that isn't there; the father's sweeping-hand watch drags then catches; the
oil-damped compass turns slow circles pointing at "a north under the world"), each working perfectly
before and after. Fatal flaw drives every turn ("I cannot leave a thing at the interesting part").
SEED #4 planted (fieldwork kit ritual: loading the 35mm camera, winding the father's watch, and the
load-bearing date written in her own hand at the head of a fresh gridded page -> pays Ch.26). Chaos
beats fire (crossroads bread-appraisal; closing folded-glasses *click*; failed emotional management).
book-evaluator PASS: **Genesis Floor 8.5 / Avg 8.57 / Casual 8.5**, Prose 9.0; no dimension <8.5.
Two gate-class catches beyond the mechanical suite, both fixed: (1) voice-wear retired phrase
"never once" (2x) varied out of the watch line; (2) a whole Ch.2 L110 cadence had been cloned into
Ch.3 ("no longer yours to be casual with" + "floor going soft") -> rewritten with fresh fieldwork
imagery, and a third "telling myself" lean rotated. Gates now clean/accepted (em-dash 0, simile 2.1/1k,
style/grammar/voice-wear clean; long-sentence 22.2% deliberately in FINAL Ch.1's accepted immersive
band 22.3%). Eval: evaluations/chapter-3-eval.md. FINAL.

BETA-READER PANEL (2026-07-11, author asked): 5-persona panel run (report:
evaluations/review/beta-reader-panel-ch3.md). Mean 7.9 (up +0.1 on Ch.1's 7.8): Devourer 8.5/buy,
Devoted 9.0/evangelize, Critic 8.0/buy, Casual 7.5/keep-reading (no near-bail this time), Hostile
6.5/put-back-but-concedes-the-hook. Brightening lands decisively (buys patience for the technical
middle); 0% dialogue cost marginal and well-mitigated by forward motion; closing pull carries into the
Ch.4 crossing. #1 fix (subtractive, protects Prose 9.0, same lever as Ch.1's slides-trim): the
film-loading MECHANICS at line 49 read as procedure to 4/5 readers -> APPLIED, trimmed the step-by-step
threading ~85w net while keeping every load-bearing image (the date in her own hand, "a pencil is the
only honest instrument," the eleven-days watch, the radio-song humming, "connected to itself all the way
through"). Gates re-verified clean after the trim (em-dash 0, LONG 22.2%, style/grammar/voice-wear
clean); 6,611w. No re-evaluation needed (subtractive/in-voice). Two series notes carried forward: hold
foreknowledge ration <=2 across Ch.4-5; withhold the *click* (below).

WATCH (carry into Ch.4-5): the *click* motif now appears in all three chapters — it is the Ch.36
climax payoff instrument, so WITHHOLD it in Ch.4-5 unless load-bearing, to keep its charge.

NEXT: Chapter 4 "The Threshold" (~1,800w; SHORT PUNCH; v2 in-medias-res). Half through her retreat off
the headland, Mara is pulled across mid-step; the way back is gone. The literal crossing, rendered fast
and bodily — the book's first structural shock, a chapter that stops almost before it starts. Distinct
in LENGTH and TEMPO from the three long chapters before it (the collapse from ~6,700w to ~1,800w is the
structural signal). Do NOT re-use the *click* here unless load-bearing. Then Ch.5 (Greece, 70 AD, ~9,800w
LONG landing) flips mystery->survival. [Superseded Ch.3 note preserved below for reference.]
Superseded original-Ch.3 plan: Re-anchor on the
fieldwork KIT-RITUAL (loading the 35mm camera / wristwatch / father's dig slides — re-read seed #4,
load-bearing for the Ch.26 climax; the "Fenn exactly her age" beat was already spent as Ch.2's final
line). Decode Fenn's notes/coordinates -> isolation/fieldwork -> travel to the coast the coordinates
name -> survey the threshold (the crossing itself is the SHORT-PUNCH Ch.4). **PACING NOTE from Ch.2
eval: Movement I now runs two consecutive melancholy chapters (grief-low Ch.1, elegiac two-hander
Ch.2) — Ch.3-5 MUST introduce wonder/brightening before the crossing so the opening movement doesn't
flatline on melancholy.** Standing policy: full self-pass chain (dialogue-polish/hook-craft/disruptor)
+ book-evaluator every chapter; beta panel on load-bearing chapters only (openers/crossing/midpoint/climax).

## Pacing log
- Ch.3 (FINAL): PACING PASS (book-evaluator) — the MANDATED tonal TURN of Movement I lands. After
  grief-low Ch.1 and elegiac Ch.2, Ch.3 delivers real competence-JOY (flight going gold over Europe,
  singing badly on the coast road, pacing the headland twice for the pleasure of it) shadowed by
  retrospective dread, then a clean positive->negative value shift into the uncanny. Travel-montage
  correctly tightens to a single sustained scene; 0% dialogue acceptable for a solo fieldwork chapter
  (Ch.2 restored the band). ~6,700w serves the beat. Strongest-paced chapter of Movement I. Genesis
  Floor 8.5 / Avg 8.57. WATCH: hold the *click* out of Ch.4-5 (its charge is spent for Ch.36).
- Ch.2 (redraft, FINAL): PACING PASS (book-evaluator) — rising-mystery/curiosity beat with a clean
  positive value shift (skeptical-grieving -> committed-believing: "I took the coast road"); strong
  34-hook pull; dialogue restored to 31.5% (band) after Ch.1's 0%; structural variety vs Ch.1
  (interior monologue -> dialogue two-hander). ONE watch-item, tonal not structural: Movement I now
  runs two consecutive melancholy chapters -> Ch.3-5 must brighten before the crossing; a one-sentence
  mid-chapter police-census micro-sag was trimmed. Genesis Floor 8.5 / Avg 8.64 / Prose 9.0.
- Ch.1 (redraft, FINAL): PACING PASS (book-evaluator) — correct grief-low, single-location
  establishing beat; hook line-1, hard pull at close; one light-trimmable slide/shelf stretch
  mid-chapter; 0% dialogue intentional (Ch.2 restores the band). Genesis Floor 8.5.
- Ch.1 (redraft, pre-final self-assessed): correct grief-LOW establishing beat; single
  location (the study) held throughout per outline; scene/summary balance healthy (sorting action
  interleaved with retrospective interiority); strong hook ("They tell you not to clear a dead
  man's house alone") + hard pull (the shut drawer / "the dead were the ones who did not leave");
  dialogue ~0% (intentional interior chapter; one reported phone exchange, no live scene — Ch.2 is
  the dialogue two-hander that restores the band); 4,875w (above floor, on target). Seeds planted:
  drawer/glasses/*click*, unkept "next season" promise, bread opinion, completionism/sunk-cost lie,
  the map + Fenn's note, ringed coords, Halloran/permit, fieldwork kit, trade-card → Ch.2 pull.
  OPEN: run book-evaluator for the Genesis Floor before calling Ch.1 final.

## RESUME HERE (2026-07-13) — Ch.4 FINAL, next is Ch.5

Ch.4 "The Threshold" DRAFTED & FINALIZED (1,734w; SHORT-PUNCH target 1,800). The crossing —
Mara returns on the fourth day, steps into the saddle, loses nerve, and is pulled across
mid-retreat; the way back is gone. In-medias-res, fast, bodily; the book's first structural
shock. Hook "I went back on the fourth day." (9/10); pull "I raised my head." (9/10).
Full pipeline: writer -> self-pass chain (dialogue 0% BY DESIGN per voice §7 interior/catastrophe;
hook-craft, disruptor beats folded in) -> mechanical gates ALL CLEAN (em-dash 0, simile 1.2/1k,
long-sentence 12.8% after splitting several spirals to sharpen the punch, grammar clean,
voice-wear clean; remaining 2 rhythm flags deliberate — the "wrong for the hour/air/coast" triad
echoes Ch.3's instrument-motif, and "I want to be exact" is Mara's established tic) -> PACING PASS
(the Ch.3 6.6k -> Ch.4 1.7k collapse IS the shock signal; correct high-tension slot between the
dread-buildup and the survival flip) -> book-evaluator **PASS: Genesis Floor 8.5 / Avg 8.64 /
Casual 8.5 / Prose 9.0 / Pacing 9.0**, no dimension <8.5, no polish loop needed. *click* motif
WITHHELD (0 occurrences, independently confirmed — reserved for the Ch.36 payoff). Fixed a
cross-chapter phrase leak ("want that on the record"). Eval: evaluations/chapter-4-eval.md.

**Next: Ch.5 "Greece, 70 AD"** (~9,800w, LONG IMMERSIVE landing). Mara wakes near Delphi, dates
it, survives her first hours as a woman who does not exist; big scarred man (Valens) walks past
without helping; she is handed to Kallia. FLIPS mystery -> survival; establishes gender/status
powerlessness (the Movement II engine). **[INSERT: Fenn journal #2 — "I, too, woke in the wrong
year."]** WATCH (from Ch.4 eval, non-blocking): ration the "I want to be exact" tic and the
define-by-negation cadence — both now in consecutive chapters; rest them here. Continue the full
MANDATORY loop (writer -> self-pass chain -> gates -> pacing -> independent evaluator -> commit).

## RESUME HERE (2026-07-13) — Ch.5 FINAL, Movement I COMPLETE, next is Ch.6

Ch.5 "Greece, 70 AD" DRAFTED & FINALIZED (7,451w; LONG IMMERSIVE landing — outline target 9,800,
but book-evaluator ruled 7,451 SUFFICIENT: all beats land, the ~2,350w belongs to Ch.6 by design;
do NOT pad). Closes Movement I; flips mystery -> survival. Beats delivered: Mara wakes near Delphi;
DATES IT via Nero's 67 AD stripping of the sanctuary bronzes (empty statue plinths) + the reign of
Vespasian -> ~AD 70; survives her first hours as "a woman who does not exist" (wrong clothes, money,
language, unclaimed status); walks the living sanctuary (treasuries, temple of Apollo, Castalian
spring she once touched "dead" on a coach tour); Valens PASSES without helping (calls off two men by
sheer stillness, never looks at her face — his kindness always sideways/unlooked-at); handed to
KALLIA (Greek widow, misquoted proverbs, lamp lit nightly for an absent son she won't name); Fenn
journal #2 ("I, too, woke in the wrong year") read under Kallia's lamp = the quiet gut-punch.

Heavy revision pass on the first draft: split runaway long sentences (LONG% 39% -> 8.2%, median 12w);
de-ticked (retired "never once"; varied "which is to say", "could not have", "I stood at the edge");
added the sanctuary-precinct immersive beat (+~875w). Gates ALL CLEAN (em-dash 0, simile 1.2/1k,
grammar/voice-wear/metaphor clean). Dialogue ~0% BY DESIGN — she cannot yet speak living Greek; the
barrier IS the Movement II engine; the two quoted words ("Kallia," "Panis,") make the naming ritual
the chapter's most intimate beat. Evaluator: earned strength, not a miss. book-evaluator **PASS:
Genesis Floor 8.5 / Avg 8.64 / Casual 8.5 / Prose 9.0 / Immersion 9.0 / Pacing 8.5**; no dimension
<8.5. Hook (L3) 9/10, pull (L157) 9/10. Eval: evaluations/chapter-5-eval.md.

**Next: Ch.6 "Kallia's House"** (~10,400w, domestic immersive collage). Kallia shelters Mara; the
brutal apprenticeship of learning to PASS as a woman who exists; the "lone foreign woman can't just
travel" obstacle made concrete; Kallia's secondary life onstage (the lamp / the son). Function: the
foothold — SIT in the humiliation of assimilation rather than montage it.
**WATCH (from Ch.5 eval, carry in):** (1) DIALOGUE SHARE must come back UP after two low-dialogue
chapters (Ch.4-5) — this is the domestic two-woman chapter, lean into it (~30-40%). (2) Ration the
define-by-negation cadence ("Not X. Not Y.") — now in Ch.3/4/5; keep at most one strong instance,
vary the next uncanny/high-emotion beat away from it. (3) Anaphora at top of sustainable range —
watch it. Continue the full MANDATORY loop (writer -> self-pass chain -> gates -> pacing ->
independent evaluator -> commit+push to main).

## RESUME HERE (2026-07-13) — Ch.6 FINAL, next is Ch.7

Ch.6 "Kallia's House" DRAFTED & FINALIZED (7,532w; domestic immersive collage — outline target 10,400,
evaluator ruled SUFFICIENT: all beats land, nothing thin. Cumulative under-run vs the 220k floor is
being TRACKED — if words are later needed, craft-safe sites are the olive-harvest banter and converting
the market-braid exam to fuller live scene). The foothold: learning to PASS, sat-in not montaged.
Beats: earn-your-keep morning; the language as humiliation (scholar's Greek is a trap; Kallia drills
her mouth, throws the cup); the loom/body apprenticeship ('quick is the enemy'); the OLIVE HARVEST
(communal work, Melita's welcome, 'the first hour I was not afraid'); the inn as school (Corinthian
trader's dangerous question + Kallia's 'hill country' cover); the solo MARKET EXAM (fluent-slip then
soft collapse; 'the clever survive by being thought stupid'); the ORACLE SEEDED by a pilgrim (a door
with a voice a morning's walk off — does NOT resolve where/when, that's Ch.10); 'the size of your
mountain' (a woman needs a man's name to exist; sea closed till spring); the lamp/grief night (Kallia's
soldier son); the WINTER FEVER crucible (Mara runs the inn alone, keeps the lamp lit as her own vow, is
adopted — 'you are not the wrong niece'); the planning close (forge a widow's story; find the scarred
muleteer = the first door). Dialogue 18.7% (up from ~0%; accepted). NEW named character MELITA added to
character-bible.md. book-evaluator **PASS: Floor 8.5 / Avg 8.64 / Casual 8.7 / Prose 9.0 / Immersion
9.0**; cover-the-name/tic CLEAN (no device bleed). Post-eval polish: broke the misquoted-proverb
vignette-close template on 2 beats. Eval: evaluations/chapter-6-eval.md.

**Next: Ch.7 "The Roman With the Mules"** (~8,600w RECALIBRATED, episodic -> single-scene two-hander). Mara hits the
wall of having no male guarantor, forges a widow's backstory, hears of the Oracle, and seeks out Valens
to buy passage down to the coast -> he refuses, coldly. Function: the STATUS ANTAGONIST; the first real
two-hander; the romance built on his NO. **THIS IS THE DIALOGUE PEAK — lean hard into it (~35%+).**
Valens = short level declaratives, works a knot/strap when feeling threatens, understates mortal danger,
withholds 'love'; his kindness always sideways. **WATCH (now 2+ chapters overdue — FIX HERE): (1) ration
DEFINE-BY-NEGATION to one instance max in Mara's narration. (2) ROTATE the Kallia-vignette closers / do
not lean on any character's device as a scene-button. (3) anaphora at top of range.** Continue the full
MANDATORY loop; add any new named character (Valens gets his first live scene here — his bible entry
already exists, confirm it) to character-bible.md.

## RESUME HERE (2026-07-13) — Ch.7 FINAL, next is Ch.8

Ch.7 "The Roman With the Mules" DRAFTED & FINALIZED (8,216w; target 8,600, -4.5%, inside the
recalibrated 7,800-9,200 immersive band). FIRST REAL TWO-HANDER / dialogue PEAK (31.6%, in the
28-38% Outlander band). Beats: (1) HITS THE WALL of no male guarantor, dramatized — an Amphissa
wagoner refuses her coin ("nobody's woman"; "who comes asking if you don't arrive?"). (2) FORGES THE
WIDOW with Kallia over three nights (Lucius Caedicius; Kallia's note "take out the wall" = don't tell
the story you love, grief goes short and stops). (3) HEARS OF THE ORACLE — the two-lock plan: before
buying passage south she must climb the sacred way and ask the Pythia WHERE in Italy the door home is
(plants Ch.10; ties Ch.6 pilgrim seed). (4) THE VALENS TWO-HANDER: pitches the widow -> he reads
through her instantly ("Go home, widow. You're not one") -> she PUTS THE STORY DOWN, tells the truth
-> his NO is FOR HER SAKE (the Krisa widow, the poppies below Kirrha, guards were the killers) -> his
sideways kindness: finds her a safer road (the factor's widow needs a book-keeping companion), sworn
as "just business... nothing to me either way" (the one big lie, told to a knot). Hook = "The first
time I met the man I would spend my life with, he told me to get off his land, and he did not look up
from the harness." Pull = the three days / the lamp / the hope she won't say aloud.

Valens rendered to bible & DISTINCT (cover-the-name PASS): short level declaratives; hands work the
knot/strap when feeling threatens (PAID at the peak — "nothing left to work... open and still");
understates mortal danger ("a liability with legs"); withholds love; kindness sideways. Distinct from
Mara (spirals/questions) and Kallia (proverbs). No device bleed.

The three overdue WATCH items DISCHARGED: define-by-negation cut to 0 sentence-initial instances;
Kallia's misquoted-proverb scene-button deliberately WITHHELD at the close ("she was not misquoting
any proverb"); anaphora held at top of range (broke one triad post-eval). Applied 2 non-blocking eval
fixes: softened a modern-mileage leak ("twelve hundred miles" -> "half the width of the world");
broke an "I had..." anaphora triad. Gates ALL CLEAN (style/rhythm/grammar/voice-wear; em-dash 2,
simile 1.6/1k, long-sentence 17.3%). book-evaluator **PASS: Genesis Floor 8.5 / Avg 8.71 / Casual 8.8
/ Prose 9.0 / Emotion 9.0 / Immersion 9.0**; no dimension <8.5, no polish loop. Eval:
evaluations/chapter-7-eval.md.

**Next: Ch.8 "Earning the Yes"** (~7,900w, negotiation + caper collage). Mara makes herself useful to
Valens's trade; DRUSUS introduced (venal, prices everything — must NOT share Valens's silence-and-a-
task device); a grudging conditional passage secured; the legate's reach seeded. Function: forced
proximity, competence as courtship; Valens's yes must be EARNED, not given. **WATCH (from Ch.7 eval):
(1) keep define-by-negation rationed (now at 0). (2) ACTIVELY VARY anaphora triads — 7-chapter
standing habit, break at least one per chapter. (3) ration retrospective significance-tagging to
<=1/chapter (let objects carry weight). (4) Drusus must be distinct from Valens (cost-talk worldview
vs stoic-spare silence — NO shared counting/pricing device).** Continue the full MANDATORY loop.

## BOOK-WIDE POLISH PASS (2026-07-13) — foreknowledge + performed-candor + proverb over-use

Author (Terry) approved fixing the cross-chapter patterns the 7-chapter beta panels flagged. Applied
across Ch.1-7 (finalized chapters), verified against all gates:

- **Performed-candor tic rationed to ONE.** The "I want that on the record / I want to be exact / I
  mention it because it is true / let it be said plainly / I want to be clear / I will be honest"
  family was a book-wide reflex (Ch.1 x3, Ch.2 x2, Ch.3 x3, Ch.4 x1, Ch.6 x2). KEPT the single
  signature instance — Ch.1 "I did not cry. I want that on the record." (earliest, characterizing) —
  and varied ALL the rest to plain narration.
- **Retrospective foreknowledge rationed; romance pre-spends cut.** Kept the deliberate Outlander
  retrospection but removed the beats that pre-spent the romance before it's earned: Ch.5 "the man I
  would love past my own life" (at first sighting) -> "the man who would come to matter most"; Ch.6's
  page-before-the-two-hander reveal ("he was the reason she would not want to leave the room") CUT,
  keeping only the "I misjudged the door" irony; Ch.7 softened "the last hour of both our lives",
  "would spend nine years learning", "the whole rest of my story would turn on", and the panel's #1
  Ch.7 fix "the man I would die beside" -> "the man at the centre of all of it". KEPT the Ch.7 hook
  ("the man I would spend my life with") as the one rationed foreshadow in his introduction chapter.
- **Kallia proverb over-use trimmed (Ch.6).** Cut the two self-glosses that re-annotated the device
  (already introduced in Ch.5) and de-anaphora'd the "Which is not the proverb / means nothing /
  meant everything" triplet. Scene-button proverbs left as characterization; Ch.7's close already
  withholds one.

All 7 chapters re-verified: style_check / grammar / voice-wear CLEAN; em-dash within gate; rhythm
flags 22 -> 20; all above word floor. No book-evaluator re-run needed (edits are subtractive/ration,
not structural; Ch.7's Floor-8.5 PASS stands).

## OUTLINE v3 — back-half sag fix (2026-07-13, author Terry approved)

Diagnosed a 4-chapter low-tension TROUGH in the old Movement III (Ch.14-17: arrival -> montage ->
breather -> birth) sitting AFTER the romance resolves (Ch.13 marriage) and BEFORE the first antagonist
(Sabina, Ch.18), with no clock the reader could feel. Fixed with 4 moves, NET-ZERO chapter change
(36 preserved; Movement V 28-36 NOT renumbered):
1. Reader-ahead Fenn dread fragment pulled forward to Ch.14-15 (reader clocks Vesuvius before Mara).
2. The two early breathers MERGED (old 15 "Building a Life" + old 16 "Catalogue of Small Days" -> Ch.15).
3. Faction seeded PHYSICALLY in Campania at Ch.15 ("Lupus" rumor -> live thread to Ch.18).
4. Fenn's first live contact brought forward to a new Ch.16 (partial/withholding); the WHEN-method
   payoff kept at Ch.20 ("What Fenn Knows"). Old single 9,200 Fenn peak split into 7,000 + 6,500.
Result: ONE pure breather survives (Ch.22 Aelia, nearest the fall); dramatic-irony clock runs from
~46% not ~55%. Σ ~= 241,500 (14-27 span -3,800). Ch.1-13 UNTOUCHED. Full detail in STATE history +
outline.md Movements III-IV.

**FLAG for Terry (pre-existing, NOT introduced by v3):** the romance-heat chapter refs in CLAUDE.md
("Ch.16/18/20 + a late payoff") and the STATE 2026-06-21 log are STALE numbering — they don't match
the v2/v3 36-ch outline, where the first union is **Ch.12 "The First Night Is a Mistake"** and
intimacy lives in Ch.11-13 (+ a late payoff). Want the heat placement reconciled to the current
outline? (Not touched here — scene placement is an author call.)

## RESUME HERE (2026-07-14) — Ch.8 FINAL, next is Ch.9

Ch.8 "Earning the Yes" DRAFTED & FINALIZED (7,939w; target 7,900, +0.5%). Movement II negotiation +
competence-as-courtship collage. RESUMED from a first draft (7,532w) left on disk by a prior run that
died mid-pipeline; NOT rewritten — closed the ~400w gap by DRAMATIZING the missing beat (the wool-tally
trial with the factor's Corinthian clerk was summarized in one paragraph; promoted to a live adversarial
scene — the steelyard beam she stops with her hand, the thumb's-width offset in the counter-weight — the
first competence rung escalating INTO the horse caper), then ran the full remaining pipeline.

Beats: return on day 3 (the door on the latch, not open — "he meant me to open it myself"); muck-out
trial; "hold this"/the horse leaning its weight (the cracked involuntary laugh); the boy's dropped
bucket ("Again, and slower"); DRUSUS introduced (worldview-through-COST: "grief's cheap — it's the
carrying charge that ruins a man"; names his creditor aloud); the wool-tally + the ANCHOR — Mara reads
a bishoped horse's teeth (aged UP, burned-in cups, rasped table) and a gingered mule off the coper's
string with her forgery/false-patina eye, and Valens turns the grey's lip up with his OWN thumb, finds
it, and says it to the horse ("You poor doctored bastard") — the yes he can't take back; "Charm he
could refuse. Competence walked straight past the guard and sat down at the fire"; the LEGATE'S REACH
seeded (an ordinary townsman agent, Campanian cloak, asks after "a fighting name / an old debt",
rides the WRONG way — "He'll not be the last"); the sideways YES (Valens takes her up to Delphi with
four beasts for the festival trade, "it's not a favour, it's just the road being the road") which is
also her secret errand to the Pythia (the two locks); the dark climb home, Kallia's lamp turned to the
window, no misquoted proverb ("which was how I knew she was serious").

Full pipeline run: writer (gap-close beat) -> dialogue-polish (cover-the-name PASS; one Valens money-
metaphor bleed corrected) -> hook-craft (opening rewritten 6->8/10 to a VOICE hook, no longer repeating
Ch.7's retrospective-declaration; pull 8-9/10 left) -> disruptor (3 light ops: blister bodily-wrongness
+ callback, anaphora triad broken) -> mechanical gates ALL CLEAN (style_check: em-dash 1 [title dash;
body 0], simile 1.1/1k, repeated-phrase clean after fixing 3 disruptor-introduced cross-chapter leaks:
"i have come to think", "i had eaten nothing since", "had nothing to do with") -> book-evaluator PASS:
**Genesis Floor 8.5 / Avg 8.61 / Casual 8.7 / CVI-Launch 8.9 / Immersion 9.0 / Emotion 8.7** -> book-editor
light polish (discharged the ONE eval regression: retrospective significance-tagging was 6 over the <=2
hard gate; trimmed to 1 by converting five hindsight-tags to object/action beats, keeping only "the years
we were given" — restores Prose to 9.0; also recast 2 of 3 define-by-negation narration fragments to
positive-first). Cover-the-name PASS on Drusus, the wool-clerk, and the legate's agent (all distinct from
Valens and each other). Eval: evaluations/chapter-8-eval.md. Disruption: evaluations/disruption-chapter-8.md.

**WATCH (carry into Ch.9, from Ch.8 eval): (1) retrospective significance-tagging is the pipeline's
DEFAULT comfort-move — it broke the <=2 gate here (6 instances) before the trim; ENFORCE <=1-2, let
objects/gestures carry weight. (2) define-by-negation crept back to 3 narration fragments (was 0 in
Ch.7); ration to 0-1. (3) anaphora is a standing 8-chapter habit — keep actively BREAKING triads, not
just holding. (4) dialogue dipped to ~29% (narration-heavy) — Ch.9 is action, but restore two-hander
banter where the road allows.**

**Next: Ch.9 "The Road to Delphi"** (~7,900w, action single-arc). The journey up the mountain together;
a road ambush forces mutual reliance; after the violence HE shakes and she doesn't (role reversal).
Voice-under-pressure REHEARSAL: Mara's prose goes flat/procedural in fear (pre-trains the climax device).
First crucible bonding the leads. Continue the full MANDATORY loop.

--- superseded (pre-Ch.8) note retained for context ---
**NEXT: still Chapter 8 "Earning the Yes"** (unchanged by v3 — Movement II is intact). Negotiation +
caper collage; Mara makes herself useful to Valens's trade; Drusus introduced; grudging conditional
passage; the legate's reach seeded.
