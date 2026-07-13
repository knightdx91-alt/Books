# CLAUDE.md — The Long Goodnight

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
- **Names:** Xavier Steadman (protagonist; "Troy" only in the pre-canon OCR draft),
  Selena (late wife), Anna Holmes, George Holmes / Holmes General Store, Derek Vance
  (the ex / stalker; "Chris" only in the draft), Caleb Ruiz (red-herring). The
  handwritten draft in `research/` is pre-canon SOURCE, never canon.
- **Voice:** Xavier's numb, past-tense grief-register; grief rendered by absence
  (Selena named sparingly/obliquely); anti-swoon — never a beauty-inventory of Anna.
- **POV (amended 2026-07-13):** strict single third-limited Xavier ONLY, plus 3–4
  concealed-antagonist "Watcher" interludes (the sole non-Xavier POV) under hard
  concealment rules — never named/self-described, withhold-never-lie, no single-
  suspect tell before its fair-play window, a deliberately un-matchable 4th voice,
  first interlude no earlier than post-Ch9. Full rules: outline.md POV lock +
  voice-dna.md Watcher card + chapter-outline.md interlude map.
- **Mystery:** whodunit; reader's suspect pool = Derek vs Caleb (Xavier is a suspect
  in the TOWN's eyes only). Necklace = fair-play clue (the one Anna threw back at
  Derek); plant early, pay off Ch27. Derek must read LIKEABLE; "he left town" pull.
- **Locked opening:** Ch1 & Ch2 are PASS-gated (Floor 8.5, r2 eval). Match their
  voice; do not regress them.
- **Style gate note:** `tools/style_check.py`'s default simile counter (4.0/1k)
  tallies ALL comparisons; voice-dna §4's ≤4 budget targets only EXPLANATORY/decode
  similes. Ch1's ~6/1k mechanical reading is a known false positive, evaluator-cleared.

## Open author decisions (ask, don't invent)
- Migrate `chapters/*.md` → `manuscript/chapters/` for pipeline consistency, or keep
  the current `chapters/` location? (Currently kept as-is.)
- Whether to draft a benchmark Interlude I before continuing the main chapter loop.

## Status (update as you go)
- Ch1 & Ch2 drafted, polished, and RE-SCORED → both PASS (Floor 8.5). Watcher-POV
  amendment adopted and propagated to all canon docs. Resume: `feedback/progress.md`.
