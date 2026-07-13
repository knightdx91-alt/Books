# CLAUDE.md — Pompeii (working title)

Per-book playbook. A fresh Claude Code session should read this first, then continue.
(This is a copy of the template; fill in the <…> placeholders for this book.)

## What this is
A **genesis-from-idea** project: build a NEW long Outlander-style time-slip historical
romance from the author's story bible (`research/story-bible.md`), using the adapted
**Best Seller Studio** pipeline. There is NO original draft — architect builds
foundation + outline + voice-dna from the bible, then the chapter loop writes.

Git identity (so commits show verified):
```
git config user.email noreply@anthropic.com
git config user.name Claude
```

## Install the agents (fresh environment)
```
git clone https://github.com/felipelobomotta-blip/best-seller-studio /tmp/bss
cp /tmp/bss/agents/*.md ~/.claude/agents/
# Also install 4 skill-based roles as agents (add tools/model frontmatter):
#   entity-tracker, continuity-guardian (skills/optional/*/SKILL.md)
#   dialogue-polish, hook-craft        (skills/deprecated/*/SKILL.md)
# Frontmatter to prepend to each:
#   ---
#   name: <name>
#   description: <from SKILL.md>
#   tools: Read, Write, Edit, Grep, Glob, Bash
#   model: opus
#   maxTurns: 40
#   ---
```
Note: in some environments the Agent tool can't dispatch these named subagents. If so,
run ONE general-purpose agent that performs each role itself by reading ~/.claude/agents/*.md.

## Project layout
```
book/genesis/<slug>/
├── STATE.yaml                 # READ FIRST — project state, word/style gates, canon
├── research/                  # staged source: original-draft.txt + roadmap/bible/etc.
├── manuscript/chapters/       # chapter-1.md ... chapter-N.md (the book)
├── evaluations/               # per-chapter eval reports + continuity audits
├── feedback/progress.md       # exact resume point
└── tools/style_check.py       # style gate (edit ALLOWLIST for this book's motifs)
```

## How to continue
1. `cd book/genesis/<slug>` and read `STATE.yaml` and `feedback/progress.md`.
2. `ls manuscript/chapters/` and `git log --oneline` to find the last finalized chapter.
3. Produce the next chapter IN ORDER. Build from the outline beats — match this book's voice.
   Run each chapter through: write → dialogue-polish → hook-craft → disruptor → **pacing
   check** → evaluate → quality gate.
4. Commit per chapter: `git add -A && git commit -m "genesis: finalize chapter N"`.

## Quality gates (ALL must pass before a chapter is "done")
- **Genesis Floor ≥ 8.5** (book-evaluator); below → book-editor polish loop (max 5).
- **PACING CHECK — required after EVERY chapter.** Before a chapter is finalized, assess its
  pacing and its pacing *in context of the chapters around it*:
  - scene-vs-summary balance; does any stretch sag or rush?
  - dialogue share within the genre band (~30–45%; target ~35%);
  - the emotional "W" — is this chapter's beat the right high/low for its slot in the arc
    (see foundation.md CALIBRATION), or are we stacking too many same-energy chapters?
  - tension/forward pull: does it open with a hook and end with a pull (hook-craft)?
  - chapter length vs. neighbors — VARIANCE IS BY DESIGN (this book runs 1,600–9,200w after the 2026-07-13 recalibration; see
    outline.md Macro-Structure). Do NOT enforce "no chapter >2× another." Instead check the
    length serves the beat: brisk modern frame, swelling immersive Greece/Campania chapters,
    deliberately collapsing chapters through the ash. Flag only length that fights its beat
    (a sag in a should-be-taut scene, padding in a punch chapter), not length that carries it.
  - Log the verdict in `evaluations/` (a one-line pacing note per chapter is fine) and in
    `feedback/progress.md`. If pacing is off, fix via book-editor/disruptor BEFORE finalizing.
- **Style check** — `python3 tools/style_check.py` clean: simile ≤4/1k, **em-dash ≤4 per
  chapter (absolute)**, no NEW cross-chapter repeated phrase (add deliberate motifs to
  ALLOWLIST), tics under ceiling. Log frequent flags in `feedback/style-flags.md`.

## Word floor
Finished book ≥ `manuscript_min_words` (see STATE.yaml). Verify:
`wc -w manuscript/chapters/chapter-*.md`. If short, expand the thinnest chapters.

## Canon guardrails (settled author decisions — never violate)
- **Comp/tone:** Outlander — sweeping, romantic, immersive, historically grounded "to a point."
- **AUTHENTICITY DIAL — "best of both" (see STATE.yaml for full text). Apply when drafting the
  Roman chapters:** SENSORY/TEXTURAL DETAIL cranked to ~8+ (real, specific, period-correct
  material — carbonized bread, Pliny's black-noon sky, garum, insulae, lamps — the immersion
  engine AND the marketing hook); HARSHNESS/PACE/COMFORT held at Outlander ~7 (1st-c Rome's
  slavery/gender-powerlessness/brutality stays real and present but never grinds the romance or
  pace down — soften edges, escapism wins ties). Authentic-FEELING and still escapist; NOT a
  purist reconstruction.
- **Scope:** ONE long standalone (~260k target / 220k floor) running through the eruption + final choice.
- **History:** Flavian era. Arrive ~70 AD (Vespasian); ~9-year span; **Vesuvius erupts 79 AD under Titus.** NOT Nero (died 68). Keep the political backdrop accurate.
- **The map:** purports to lead to the lost **Library of Alexandria**; real secret = a door through time. From the estate sale of a vanished self-proclaimed treasure hunter (left notes + coordinates).
- **Mechanism:** coordinates open a time-door; she lands in **Greece (Delphi)**; the **Oracle** tells her WHERE the door home is (Pompeii) but NOT WHEN; she learns the "when" later.
- **Greece first:** a lone foreign woman in antiquity can't just travel — real obstacle, not hand-waved.
- **Love interest:** disgraced **ex-gladiator** accused of an affair with the emperor's wife; they marry + have children over years.
- **Climax:** family can't pass to the future; **stay vs. leave** as Vesuvius erupts.
- **Romance heat:** explicit when it occurs but OCCASIONAL/earned (NOT erotica, no per-page quota). ~3-4 on-page scenes across the arc (Ch.16/18/20 + a late payoff), none after the eruption begins. See STATE.yaml `resolved_author_decisions` for the exact wording.
- **magic spelling:** n/a (this is historical, not invented-magic — the only "magic" is the time-door).

## Open author decisions (ask, don't invent)
- Protagonist name + modern era; father OR grandfather as the archaeologist.
- Ex-gladiator's name + scandal specifics; how she learns WHEN the door opens.
- Treasure-hunter mystery payoff; final choice outcome (stay or go = the ending).

## Status (update as you go)

> ### ▶ NEXT SESSION — START HERE: draft Chapter 7 "The Roman With the Mules" (~8,600w · first real two-hander)
> **Ch.1-6 all FINAL, all Floor 8.5 PASS.** Ch.6 "Kallia's House" (2026-07-13): 7,532w domestic collage,
> **Floor 8.5 / Avg 8.64 / Casual 8.7 / Prose 9.0 / Immersion 9.0**. The foothold — learning to PASS.
> Cover-the-name/tic CLEAN (no device bleed). NEW char MELITA in character-bible.md. Dialogue 18.7%.
>
> **Ch.7 = the status antagonist + the NO:** Mara hits the wall of having no male guarantor, forges a
> widow's backstory, hears of the Oracle, and seeks out VALENS (the scarred freed muleteer) to buy
> passage to the coast. He refuses, coldly. The romance is built on his NO. **THIS IS THE DIALOGUE PEAK
> — lean hard (~35%+); it is the first real two-hander.** Valens: short level declaratives, works a
> knot/strap when feeling threatens, understates mortal danger, withholds 'love', kindness always
> sideways (his bible entry exists — confirm/extend it on his first live scene).
> **WATCH — now 2+ chapters overdue, FIX IN Ch.7: (1) ration DEFINE-BY-NEGATION to one instance max in
> Mara's narration. (2) do NOT lean on any character's device as a scene-button (rotate the closers).
> (3) anaphora at top of range.**
> **LENGTH POLICY (author, 2026-07-13 — RECALIBRATED):** Ch.5-6 land ~7,500 (complete; do NOT
> retro-expand — padding = AI filler). The whole immersive band was rescaled DOWN to a UNIFORM
> 7,800-9,200 so 5/6 don't look short and no density seam opens. **Ch.7 target is now 8,600w** (not
> 9,800). Write each chapter to its NEW outline target within ~5%. Recalibrated Σ ~245k, +25k over the
> 220k floor. See STATE.yaml LENGTH POLICY + outline.md Σ BUDGET CHECK.
>
> --- prior START HERE (Ch.6, now done) retained below for context ---
> ### ▶ (done) draft Chapter 6 "Kallia's House" (~10,400w · domestic immersive collage)
> **Movement I is COMPLETE — Ch.1-5 all FINAL, all Floor 8.5 PASS.**
> **Ch.5 "Greece, 70 AD" is now FINAL** (2026-07-13): 7,451w LONG IMMERSIVE landing, **Genesis Floor
> 8.5 / Avg 8.64 / Casual 8.5 / Prose 9.0 / Immersion 9.0 / Pacing 8.5**, no dimension <8.5. Closes
> Movement I; flips mystery -> survival. Mara wakes near Delphi, DATES IT via Nero's stripped bronzes +
> Vespasian, survives as "a woman who does not exist", Valens passes without helping, handed to Kallia,
> Fenn journal #2 under the lamp. Dialogue ~0% ruled an EARNED strength (language barrier = the engine).
> All gates clean (em-dash 0; long-sentence 8.2% after a heavy split pass).
>
> **Ch.6 = the foothold:** Kallia shelters Mara; the brutal apprenticeship of learning to PASS as a
> woman who exists; the "lone foreign woman can't just travel" obstacle made concrete; Kallia's lamp/son
> onstage. SIT in the humiliation of assimilation, do not montage it. **WATCH (from Ch.5 eval): (1)
> bring DIALOGUE SHARE back up (~30-40%) after two low-dialogue chapters — this is the two-woman
> domestic chapter, lean in. (2) Ration the define-by-negation cadence (now in Ch.3/4/5) — one strong
> instance max. (3) Anaphora at top of its range.**
>
> --- prior START HERE (Ch.5, now done) retained below for context ---
> ### ▶ (done) draft Chapter 5 "Greece, 70 AD" (~9,800w · LONG IMMERSIVE landing)
>
> **Ch.5 = the landing:** Mara wakes near Delphi, dates it, survives her first hours as a woman who
> does not exist; a big scarred man (Valens) walks past without helping; she is handed to Kallia.
> FLIPS mystery -> survival; establishes the gender/status powerlessness that is the Movement II
> engine. The long immersive counter-weight to Ch.4's punch — crank the authenticity dial (sensory ~8,
> harshness ~7). **[INSERT: Fenn journal #2 — "I, too, woke in the wrong year."]**
>
> --- prior START HERE (Ch.4, now done) retained below for context ---
> ### ▶ (done) draft Chapter 4 "The Threshold" (~1,800w · SHORT PUNCH)
> **Ch.3 "Coordinates & the Survey" is now FINAL** (2026-07-11): ~6,700w, **Genesis Floor 8.5 / Avg
> 8.57 / Casual 8.5**, Prose 9.0, PACING PASS (the mandated tonal TURN — competence-joy under dread —
> lands; strongest-paced chapter of Movement I). Full pipeline run (writer -> dialogue-polish ->
> hook-craft -> disruptor -> gates -> book-editor long-sentence trim -> book-evaluator). Seed #4
> (fieldwork kit ritual, incl. the date in her own hand) planted -> pays Ch.26. Instruments-go-wrong
> uncanny landed. em-dash 0; long-sentence 22.2% in Ch.1's accepted immersive band. Fixed a Ch.2->Ch.3
> cadence clone + retired phrase 'never once'. **WATCH: the *click* motif is now in all 3 chapters —
> WITHHOLD it in Ch.4-5 (it's the Ch.36 payoff instrument).**
>
> **Ch.4 = the crossing:** half through her retreat off the headland, Mara is pulled across mid-step;
> the way back is gone. In-medias-res, fast, bodily; the book's first structural SHOCK — a chapter that
> stops almost before it starts. The collapse from ~6,700w to ~1,800w IS the structural signal; keep it
> taut. Then Ch.5 (Greece 70 AD, ~9,800w LONG landing) flips mystery -> survival.
>
> --- prior START HERE (Ch.3, now done) retained below for context ---
> ### ▶ (done) draft Chapter 3 "Coordinates & the Survey" (~7,000w)
> **Ch.2 "Too Accurate to Be Fake" is now REDRAFT FINAL** (2026-07-11): dialogue two-hander, 4,776w,
> **Genesis Floor 8.5 PASS** (Avg 8.64, Casual 8.5, Prose 9.0). Antique dealer Verrall / vanished
> hunter August Fenn's estate ledger; Fenn marginalia insert #1 landed; "Fenn vanished at 34 = Mara's
> age" spent as the pull. Gates clean (em-dash 0). PACING WATCH: Movement I now has two consecutive
> melancholy chapters — **Ch.3-5 must introduce wonder/brightening before the crossing.**
>
> Blueprint COMPLETE (foundation.md + outline.md [36 ch v2] + voice-dna.md, now incl. §7 Outlander
> comp calibration), all author decisions resolved (see STATE.yaml). **Cadence: ONE chapter at a
> time, then the author reviews** before the next.
>
> **2026-07-11 RESTART (author Terry):** the prior Ch.1 & Ch.2 drafts were DELETED and the book
> restarted from Ch.1 (old drafts recoverable in git history). Ch.2 must be REDRAFTED.
>
> **Done & committed:**
> - Ch.1 "The Drawer" — REDRAFT FINAL, 5,066w, **Genesis Floor 8.5 PASS** (Avg 8.64, Casual 8.5).
>   Single-location grief chapter; stuck drawer + glasses *click*, unkept "next season" promise,
>   bread opinion, completionism, the map + A. Fenn's note, Halloran/permit, fieldwork kit, trade-card
>   pull to Ch.2. Written to voice-DNA §7. em-dash 0. (Rev 1 lifted Characters 8.0→8.5.)
>
> **MANDATORY chapter loop (author Terry, EVERY chapter — no skipping):**
> book-writer → **dialogue-polish → hook-craft → disruptor** (all three, every time) →
> **update `character-bible.md`** if the chapter introduced a new named character (distinctness
> signature + DISTINCTNESS GUARANTEE; obey the TIC BUDGET — ≤2–3 tic-bearers total = Fenn + Kallia;
> no second character borrows the narrator's catalogue/condition device) →
> mechanical gates (style_check + grammar_check + voice_wear_check clean; em-dash ≤4) →
> **independent book-evaluator Genesis Score (Floor ≥8.5 + PACING)** → book-editor polish loop if
> any dimension <8.5 → re-evaluate → commit + push to main + update ALL trackers per chapter.
> Optional extra on load-bearing chapters (openers/crossing/midpoint/climax): beta-reader panel.
>
> **STRUCTURE ADOPTED (2026-07-06): v2 — 36 chapters, 5 Movements, slow-burn-to-eruption,
> VARIED chapter length 1,600-12,000w (Sigma 273k).** See outline.md Macro-Structure. Old 45-ch
> outline archived as outline-v1-45ch.md.bak. Chapter length is a structural signal now — do NOT
> flatten it (pacing gate updated to allow the variance).
>
> **STANDING NOTE for Ch.3 "Coordinates & the Survey" (v2 = old Ch.3+4 FUSED; target ~7,000w):**
> the outline's original Ch.3 anchor ("Fenn exactly her age") was spent as Ch.2's final line.
> **Re-anchor Ch.3 on the fieldwork kit-ritual** (loading the 35mm film camera, the wristwatch,
> the father's dig slides — re-read seed #4, load-bearing for the climax) and let the spent
> photo's dread COLOR the note-reading. v2 Ch.3 now runs decode notes/coordinates → isolation/
> fieldwork → travel to the site → survey the threshold (the crossing itself is the SHORT-PUNCH
> Ch.4, ~1,800w). Match the Ch.1/Ch.2 voice exactly.
>
> **Resume:** `cd book/genesis/pompeii`; read STATE.yaml + feedback/progress.md + the Ch.2 eval;
> reread chapter-1.md & chapter-2.md for voice; then write chapter-3.md.

--- history ---
- Scaffolded; bible staged as canon; all decisions resolved; architect built the 45-ch blueprint.
- v2 re-architecture: 36 ch, 5 Movements, slow-burn-to-eruption, varied length.
- 2026-07-11: voice-DNA §7 Outlander comp calibration added; RESTART — deleted prior Ch.1/2;
  Ch.1 redrafted & finalized (Floor 8.5). Standing policy: full self-pass chain + evaluator every ch.

## Other active books in this repo (each on its own branch — for cross-project awareness)
> This session set up several books, each as `book/genesis/<slug>/` on its own branch with the
> same pipeline + pacing gate. Switch branches to work on another.
- **rosalia** (branch `claude/elegant-wright-yyt925`) — vampire/shifter epic-romance; 29-ch ~150k blueprint done; chapter loop not started.
- **pompeii** (branch `claude/pompeii-story`, THIS) — Outlander-style time-slip; Ch.1-2 written.
- **finding-lady-death** (branch `claude/death-and-remembrance`) — paranormal romance; 20-ch ~96k blueprint done; loop not started.
- **the-gift** (branch `claude/the-gift`) — sci-fi antihero thriller; 21-ch ~103k blueprint done; loop not started; pick a company name (Helix Vanguard rec.).
- **son-of-none** (branch `claude/son-of-none`) — empty; awaiting the author's "Son of None" file/idea.
- **the-long-goodnight** (branch `claude/the-long-goodnight`) — empty placeholder.
- (saeren-chronicles is the original, on `main`.)
