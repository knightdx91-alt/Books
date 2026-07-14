# CLAUDE.md — The Replaced

Per-book playbook. A fresh Claude Code session should read this first, then continue.
(This is a copy of the template; fill in the <…> placeholders for this book.)

## What this is
A genesis project to revise/expand an existing draft into a finished book, using the
adapted **Best Seller Studio** pipeline. We work only on `main`. Commit and push to `main`.

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
book/genesis/the-replaced/
├── STATE.yaml                 # READ FIRST — project state, word/style gates, canon
├── research/                  # staged source: original-draft.txt + roadmap/bible/etc.
├── manuscript/chapters/       # chapter-1.md ... chapter-N.md (the book)
├── evaluations/               # per-chapter eval reports + continuity audits
├── feedback/progress.md       # exact resume point
└── tools/style_check.py       # style gate (edit ALLOWLIST for this book's motifs)
```

## How to continue
1. `cd book/genesis/the-replaced` and read `STATE.yaml` and `feedback/progress.md`.
2. `ls manuscript/chapters/` and `git log --oneline` to find the last finalized chapter.
3. Produce the next chapter IN ORDER. Locate its material in `research/original-draft.txt`
   and REVISE/EXPAND to the roadmap beats — do not invent from scratch. Match the locked
   Ch.1 voice if one exists. Run each chapter through: write → dialogue-polish → hook-craft
   → disruptor → evaluate → quality gate.
4. Commit per chapter: `git add -A && git commit -m "genesis: finalize chapter N"`.

## Quality gates (both must pass before a chapter is "done")
- **Genesis Floor ≥ 8.5** (book-evaluator); below → book-editor polish loop (max 5).
- **Style check** — `python3 tools/style_check.py` clean: simile ≤4/1k, em-dash ≤~10/1k,
  no NEW cross-chapter repeated phrase (add deliberate motifs to ALLOWLIST), tics under ceiling.

## Word floor
Finished book ≥ `manuscript_min_words` (see STATE.yaml). Verify:
`wc -w manuscript/chapters/chapter-*.md`. If short, expand the thinnest chapters.

## Canon guardrails (settled author decisions — never violate)
- **Read `research/spine-locked.md` first** — the author-locked story spine. The
  architect BUILDS ON it; never overwrite it.
- **Shape:** braided **three-timeline** SF mystery, **STANDALONE** puzzle-box.
  Threads: **Mark** (1,000ya, CIA founder, the ORIGIN, the LAST truly biological POV) /
  **the Boy** (500ya, ark-ship **Hope**, restoration seed, a COPY) / **Darin Markson**
  (now, gains **root**, the LEVER, also a COPY). Converge in the present as Hope returns.
- **Reveal stack (fair-play — plant across all three timelines):** (1) surface = alien
  invasion swapping people for doppelgangers; (2) world reveal = the invasion is a
  **RESCUE** (truly-Other aliens copy people to save them from a coming extinction;
  Hope's restoration would UNDO it); (3) personal reveal = the hero is a **COPY** (both
  Darin AND the Boy) → restoration is self-negating.
- **Extinction (proposed, adjustable):** the nanotech's own runaway conversion consumes
  all biological matter — disease and cure are the same tech.
- **Aliens:** genuinely Other, kept mostly UNSEEN — revealed by consequence, not
  exposition. Not conquerors; an old "rescue" civilization.
- **Theme:** is a perfect copy that remembers being you still you — and is "true
  humanity" worth extinction? Authenticity vs. survival.
- **Cross-book:** keep DISTINCT from `books/all-the-worlds-she-keeps/` (cozy portal romance) — this is
  cold hard-SF paradox. Per-timeline POV voices must NOT rhyme.

## Open author decisions (ask, don't invent)
- Confirm/adjust the **(proposed)** items in `spine-locked.md` (the extinction's nature).
- **Title:** RESOLVED → "The Replaced" (author-chosen 2026-07-14; was working "Nanobot",
  author pages said "Nanobot Trio").
- Architect to INVENT/PROPOSE: the aliens' name & how much is shown; the rules & LIMITS
  of "root"; fair-play clue seeding across timelines; the refusers'/Hope's launch
  history; the Boy's creators aboard.

## Status (update as you go)
- Phase 1. **Spine DEVELOPED & LOCKED** (`research/spine-locked.md`); STATE comps +
  engagement types set. **READY for the architect pass** (foundation.md + outline.md +
  voice-dna.md) — not yet run. Resume: `feedback/progress.md`.
