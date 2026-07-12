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
