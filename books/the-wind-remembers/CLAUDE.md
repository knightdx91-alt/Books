# CLAUDE.md — The Wind Remembers

Per-book playbook. A fresh Claude Code session should read this first, then continue.
Filled in for this book 2026-09-02 from the author's handwritten planning pages.

## What this is
A **genesis-from-notes** project: the author supplied two handwritten planning pages, not
prose. There is NO draft to revise. The notes are binding canon; everything else is the
architect's to build. We work only on `main`. Commit and push to `main`.

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
books/the-wind-remembers/
├── STATE.yaml                 # READ FIRST — project state, word/style gates, canon
├── research/source-notes.md   # the author's handwritten pages, transcribed = CANON
├── research/notes-scans/      # page-1.jpg, page-2.jpg — the original photographs
├── character-bible.md         # cast VOICE/distinctness — ADD every new named character here (tic budget)
├── manuscript/chapters/       # chapter-1.md ... chapter-N.md (the book)
├── evaluations/               # per-chapter eval reports + continuity audits
├── feedback/progress.md       # exact resume point
└── tools/style_check.py       # style gate (edit ALLOWLIST for this book's motifs)
```

## How to continue
1. `cd books/the-wind-remembers` and read `STATE.yaml` and `feedback/progress.md`.
2. `ls manuscript/chapters/` and `git log --oneline` to find the last finalized chapter.
3. Nothing is blueprinted yet — the **architect pass has not run**, and it is blocked on
   the author's three open questions below. Once it has, produce chapters IN ORDER against
   `outline.md`, holding to the wheel canon in `STATE.yaml`. Run each chapter through: write → dialogue-polish → hook-craft
   → disruptor → evaluate → quality gate.
4. Commit per chapter: `git add -A && git commit -m "genesis: finalize chapter N"`.

## Quality gates (both must pass before a chapter is "done")
- **Genesis Floor ≥ 8.5** (book-evaluator); below → book-editor polish loop (max 5).
- **Style check** — `python3 tools/style_check.py` clean: simile ≤4/1k, em-dash ≤~10/1k,
  no NEW cross-chapter repeated phrase (add deliberate motifs to ALLOWLIST), tics under ceiling.
- **Motif cap (author standing rule)** — no signature narrative tic-phrase may recur more than
  **3 times across the whole book**. ALLOWLIST is a *capped* registry, not an exemption:
  declaring a motif does NOT license unlimited use. Entries are `"phrase"` (cap 3) or
  `("phrase", N)` to raise the cap for a genuinely load-bearing image (keep overrides rare/small).
  The gate FAILS if any motif exceeds its cap.

## Word floor
Finished book ≥ `manuscript_min_words` (see STATE.yaml). Verify:
`wc -w manuscript/chapters/chapter-*.md`. If short, expand the thinnest chapters.

## Canon guardrails (settled by the notes — never violate)
Full text in `research/source-notes.md`; the load-bearing rules:
- **Mandy** is the FIRST reincarnation of **Elizabeth**, a high-society Victorian
  Englishwoman who called the wind and died doing it in a moment of crisis. Mandy does
  not know she is an old soul — only that she is drawn to the period without knowing why.
- **Knight** is an old soul out of the **medieval** period. His distinguishing trait is
  **implacable will**: once committed, nothing on earth stops him while he still breathes.
- Every old soul has exactly **one** thing that sets it apart (Mandy: the wind).
- **Memories unlock only by USING the gift that put you on the wheel.** After that they
  trickle back **through dreams**, faster the more the soul embraces its past. Return is
  not always pleasant — a violent death is re-lived.
- A **"hand"** (a watcher easing a soul's transition) is assigned ONLY for a soul's FIRST
  reincarnation, and only mature souls are given the duty. The hand begins with no name,
  no face, not even a gender — only a vague sense of **where**.
- The wheel keeps protector and ward close in age: **Knight was three when Mandy was
  born**, felt the world shift at her first breath, a pull **west**, and that he had time.
- **Opening shape:** Ch.1 = Elizabeth's Victorian life through her death. Ch.2 = time-skip
  to Mandy as a child outside a run-down abandoned house, storm-feeling but no storm; she
  calls the wind for the first time and dismisses it as the weather; sun, then they run
  laughing to her house out of the sprinkling rain. Then skip to Mandy in her twenties.
- Flashbacks go to the leads' **first** lives specifically.

## Open author decisions (ask, don't invent)
Three are the author's own side-note questions, and the last is the book's spine:
- **What is the overarching conflict?** Author's working idea: someone who can **sever a
  soul's connection to the wheel**, with **Balance** at stake. Blocks the outline.
- **Why is a soul reborn?** The metaphysics the ending must pay off.
- **What determines how often a soul is reborn?**
- Mandy's present-day job: **hotel** (as first written) or **museum curator** (the
  author's own later preference). The notes lean museum.
- Standalone or series opener? Romance heat level? Does Knight's assignment as her hand
  end once she remembers — and does the wheel reassign him?

## Status (update as you go)
- **2026-09-02 — source staged, architect NOT run.** `research/source-notes.md` holds the
  transcribed handwritten pages; scans in `research/notes-scans/`. No `foundation.md`, no
  `outline.md`, no `voice-dna.md`, no chapters. `comp_titles` is empty (researcher pass
  pending). The architect is blocked on the open decisions above.
- Before drafting: seed `tools/style_check.py` ALLOWLIST with this book's motifs —
  **wind imagery above all**, or the repetition gate will fire on the book's central image.
