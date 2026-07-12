# CLAUDE.md — Books (consolidated book monorepo)

Guidance for Claude Code working in this repository. **Read this first, every session.**

## What this repo is

**One repo for all books.** The shared writing pipeline lives at the repo root; each
book lives in its own folder under `books/`. There is exactly one copy of the pipeline
and every book uses it — no per-book duplication.

```
/                       ← repo root
├── .claude/            ← the pipeline: 12 book-* agents, /gemini + /grok commands, hooks
├── tools/              ← shared tools: apodictic (structural editor), gemini/grok review scripts
├── books/
│   ├── _template/      ← scaffold a new book copies from (NOT a book)
│   ├── the-gift/       ← a single book
│   ├── saeren/         ← a SERIES folder (multiple book subfolders + shared tooling)
│   │   ├── saeren-chronicles/            (book 1)
│   │   ├── saeren-chronicles-book-2/     (book 2)
│   │   └── saeren-chronicles-book-3/     (book 3)
│   ├── land-of-the-guardians/            ← the Ne'veran 4-book saga (see its README)
│   └── ... one folder per book/series
├── new_book_repo.sh    ← LEGACY (old one-repo-per-book model; kept for reference)
└── setup-script.sh     ← environment SessionStart installer
```

## ⚖️ WORKFLOW LAW — READ EVERY SESSION (non-negotiable)

**We work ONLY on `main`. ALWAYS. This is Law.** No other branch, ever. No PRs (not even
drafts). Everything commits and pushes straight to `main`. If a session starts on some
other branch (e.g. `claude/...`), push your work to `main` directly. The only exception
is when the author (Terry) explicitly says otherwise for a task.

Git identity: `git config user.email noreply@anthropic.com && git config user.name Claude`

**This is enforced, not just documented:**
- The **SessionStart** hook (`.claude/hooks/session-start.sh`) detects a session that
  starts on any non-`main` branch, switches to `main` (carrying uncommitted work across
  via stash), and **deletes the stray branch** automatically.
- A **PreToolUse** guard (`.claude/hooks/enforce-main-law.sh`) blocks any command that
  creates a branch (`git checkout -b`, `git switch -c`, `git branch <name>`) or opens a PR
  (`gh pr create`, the `create_pull_request` MCP tool) before it can run.

## Working on a book

1. **Pick the book folder** under `books/<name>/` (for a series, the specific book
   subfolder, e.g. `books/saeren/saeren-chronicles-book-2/`).
2. **Read its `STATE.yaml` first**, then `feedback/progress.md` (if present). STATE.yaml
   is the source of truth for that book's premise, canon, gates, and resume point.
3. Run the pipeline agents/commands against **paths inside that book folder**. The
   pipeline itself is shared from the root `.claude/` + `tools/` — you never copy it in.
4. A book folder typically holds: `STATE.yaml`, `foundation.md`, `outline.md`,
   `voice-dna.md`, `research/`, `manuscript/chapters/`, `evaluations/`, `feedback/`,
   `delivery/`, and a per-book `tools/style_check.py` (its ALLOWLIST is book-specific).

## Starting a new book

Run: `bash tools/new-book.sh <slug> "<Book Title>"`
→ creates `books/<slug>/` from `books/_template/`, ready for source material + the
architect pass. (No new repo, no GitHub step — it's just a folder in this repo.)

For a new book **inside an existing series**, create the subfolder under that series
folder and copy `books/_template/` into it.

## 🔧 Pipeline is shared — improvements flow to the root (THE UPDATE RULE)

The pipeline (the `book-*` agents, `/gemini` + `/grok`, APODICTIC) is edited in **one
place: this repo's root `.claude/` + `tools/`.** Every book already uses it directly.

**UPDATE RULE:** anytime you make the pipeline better — a new agent/tool, a tweak to an
agent/command/gate, or a better entry to a shared list (anti-AI pattern, craft-mistake
rule, structural-variety option) — edit it at the **root** and commit, so every book
inherits it immediately. Do NOT strand an improvement inside a single book's folder.

**The one exception — per-book, stays per-book:** each book's
`books/<name>/tools/style_check.py` **ALLOWLIST** is book-specific (deliberate motifs
differ). Those stay in the book folder, seeded from `books/_template/`. If you improve the
*template's* allowlist logic (structure, not a book's specific motifs), change
`books/_template/`.

## Structural-variety rule (baked into book-architect)

Books must NOT all converge on ~20 chapters of ~5,000 words in three visible acts with
turning points on the exact quarter-marks — that uniformity is a machine-made tell. The
architect **selects a macro-structure per premise** (Section 0.5 of `book-architect.md`).
Improve that logic at the root so every future book inherits it.

## How the pipeline is installed each session

`setup-script.sh` (pasted into the web Environment's setup script) runs at SessionStart:
installs build deps (reportlab/ghostscript/language-tool) and defaults sub-agents to Opus.
Because the pipeline now lives in THIS repo's root `.claude/`, Claude Code loads it
directly — no cloning a separate pipeline repo. Update the script only if the install
mechanism changes; update the root `.claude/`/`tools/` for everything else.
