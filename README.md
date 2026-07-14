# Books — one repo for every book, one shared pipeline

This is the consolidated home for all of Terry's books. **The writing pipeline lives once
at the repo root and every book uses it directly** — no per-book copies, no separate
pipeline repo to keep in sync.

See **`CLAUDE.md`** for the full working guide (read it every session), and
**`PROJECT-STATUS.md`** for the consolidation log, decisions, and outstanding manual steps.

## Layout

```
.claude/        the pipeline — 12 book-* agents, /gemini + /grok commands, hooks, settings
tools/          shared tools — apodictic (structural editor), gemini_review.sh, grok_review.sh, new-book.sh
books/
  _template/    scaffold a new book copies from (not a book)
  <name>/       one folder per book (e.g. the-gift/, the-replaced/, the-hour-of-ash/)
  saeren/       a SERIES: saeren-chronicles/ + -book-2/ + -book-3/ + shared epub tooling
  land-of-the-guardians/   the Ne'veran 4-book saga (see its own README)
```

Each book folder is self-contained (`STATE.yaml`, `foundation.md`, `outline.md`,
`voice-dna.md`, `research/`, `manuscript/`, `evaluations/`, `feedback/`, per-book
`tools/style_check.py`). Its `STATE.yaml` is the source of truth for that book.

## Workflow Law

Work **only on `main`.** No other branches, no PRs. Commit and push straight to `main`.

## Starting a new book

```
bash tools/new-book.sh <slug> "<Book Title>"
```

Creates `books/<slug>/` from `books/_template/`, ready for source material and the
architect pass. Then commit & push to `main`.

## The update rule (why the pipeline is shared)

The pipeline is edited in **one place — the root `.claude/` + `tools/`** — so every book
inherits every improvement automatically. Anytime you improve an agent, command, gate, or
a shared list (anti-AI patterns, craft rules, structural-variety options), change it at the
root and push. Don't strand an improvement inside a single book.

**One exception:** each book's `tools/style_check.py` ALLOWLIST is book-specific and stays
in the book folder (seeded from `books/_template/`).

## Notes

- `new_book_repo.sh` is **legacy** — it built a standalone one-book repo under the old
  model. Kept for reference; use `tools/new-book.sh` instead.
- `setup-script.sh` is the environment SessionStart installer (build deps + Opus default).
  Because the pipeline now lives in this repo's root `.claude/`, Claude Code loads it
  directly; the script no longer needs to clone a separate pipeline repo.
- The `gemini_review.sh` / `grok_review.sh` prompts still carry some Saeren-specific series
  context in their prompt text — generalise per book when you use them elsewhere.
