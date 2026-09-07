# Getting started

From an empty fork to a finished chapter. Budget an hour for setup and your first
chapter; a full book is days-to-weeks of sessions, not one sitting.

## 1. What you need

- **Claude Code** — the CLI, the desktop app, or [claude.ai/code](https://claude.ai/code)
  on the web. The pipeline runs in all three; the web version is what this repo's hooks
  are tuned for.
- **Python 3** with `pyyaml` (for the tools), plus `reportlab` + `pillow` and
  **Ghostscript** if you intend to build print PDFs. The SessionStart hook installs these
  in a fresh web container automatically.
- Optional: a **Gemini** and/or **xAI** API key for cross-model second opinions.
- Nothing else. There is no service to sign up for, no vector database, no local model.

## 2. Fork and configure

```bash
git clone <your fork> Books && cd Books
```

Open **`.claude/pipeline.conf`** and make two decisions:

```sh
WORKFLOW_LAW="main-only"   # or "off" if you want normal branches + PRs
AGENT_SOURCE="repo"        # keep this — it makes your fork self-contained
```

`main-only` is how this repo has always run: everything commits straight to `main`, and
hooks actively prevent branches and PRs. It suits a solo author writing prose, where
branches only fragment a manuscript. **If more than one person will work on the repo, or
you want review before merge, set it to `off`** — nothing else in the pipeline depends on
it. Details in [WORKFLOW-AND-HOOKS.md](WORKFLOW-AND-HOOKS.md).

Then clear out the example content when you're ready: the `books/` folder here holds real
books. Delete the ones that aren't yours, keep `books/_template/` and
`books/_series-template/`.

### If you use Claude Code on the web

Paste `setup-script.sh` into your environment's setup-script field. It runs at session
start and installs the build toolchain. The 12 agents come from the repo itself
(`.claude/agents/`), which is also the **only** place they can be dispatched by name from
— the agent registry is built from the clone before hooks run.

## 3. Scaffold a book

```bash
bash tools/new-book.sh the-glass-road "The Glass Road"
```

That creates `books/the-glass-road/` from the template: `STATE.yaml`, `CLAUDE.md`,
`character-bible.md`, the standard folders, and this book's own copies of
`style_check.py` / `grammar_check.py`.

For a series, create the series first — see [SERIES.md](SERIES.md):

```bash
bash tools/new-series.sh emberfall "The Emberfall Cycle" emberfall-book-1 "A Crown of Cinders"
```

## 4. Fill in what only you know

Before any agent runs, edit **`books/the-glass-road/STATE.yaml`**:

- `project.premise` — one sentence. This is the seed, not the contract; the premise forge
  will push on it.
- `project.genre` / `subgenre` / `comp_titles` — these drive genre-adjusted thresholds
  everywhere downstream. Getting the genre wrong mis-tunes every gate in the pipeline.
- `word_floor.manuscript_min_words` — the hard floor for the finished book.
- `adaptation.mode` — `genesis-from-idea` (nothing written yet) or `revise-existing-draft`
  (you have prose; stage it in `research/`).
- `guardrails` — settled decisions no agent may violate.
- `open_author_decisions` — things you have *not* settled. Agents ask instead of inventing.

Also edit `books/the-glass-road/CLAUDE.md` — the per-book playbook a future session reads
first. Fill in canon guardrails and delete what doesn't apply.

> **The single most common failure** is a book folder whose `STATE.yaml` still says
> "TEMPLATE DEFAULT". Everything downstream reads that file; a stale one sends the
> architect off in the wrong direction with total confidence.

## 5. Run it

Two ways to drive the pipeline. Both use the same agents.

### Autopilot

```
Run the book-orchestrator on books/the-glass-road
```

The orchestrator runs research → premise forge → foundation → voice DNA → chapter loop →
evaluation → revision → delivery, and pauses at exactly three checkpoints (after the
foundation, after the full manuscript, after the editorial package). Best for a book you
want built end-to-end with limited supervision.

### Manual, phase by phase (recommended for your first book)

```
Run book-researcher on books/the-glass-road
Run book-architect on books/the-glass-road          # foundation + outline
Run book-architect in voice mode on books/the-glass-road   # voice-dna + character-bible
Write chapter 1 of books/the-glass-road              # then the loop: dialogue-polish,
                                                     # hook-craft, disruptor, evaluate
```

You see each artifact before the next one is built on top of it. Since the outline is
what the whole book is hung on, reviewing it before 90,000 words are written on top of it
is worth the extra hour.

## 6. The chapter loop

For every chapter, in order — never start chapter N+1 before N is finalized, because the
writer of N+1 reads the *finalized* N for continuity:

| Step | Agent | What it does |
|---|---|---|
| A | `book-writer` | Writes the chapter from the outline beat |
| B | `dialogue-polish` | Dialogue-only pass; cover-the-name test |
| C | `hook-craft` | The opening hook and closing pull |
| D | `book-disruptor` | Breaks up the smoothness; anti-AI disruption |
| E | *(bash)* | Mechanical preprocess — em-dash, adverb, pattern counts |
| F | `book-evaluator` | Genesis Score, reader simulation, anti-AI scan |
| G | *(gate)* | Floor ≥ 8.5 and Casual ≥ 8.5, else `book-editor` polish loop |

Every 3–5 chapters, `entity-tracker` reconciles `ENTITY_STATE.yaml` and
`continuity-guardian` audits. Then:

```bash
python3 books/the-glass-road/tools/style_check.py
python3 books/the-glass-road/tools/grammar_check.py
git add -A && git commit -m "finalize chapter 3"
```

Commit per chapter. It is the only reliable undo a manuscript has.

## 7. Finish

```
Run book-packager on books/the-glass-road
```

Editorial package (logline, synopsis, query letter, cover brief) plus production files.
For print and ebook builds and the IngramSpark upload path, see
[PUBLISHING.md](PUBLISHING.md).

## Where the time actually goes

Setup and scaffolding are minutes. The real cost is the chapter loop: each chapter runs
several agents and often two or three polish cycles to clear 8.5, and the anti-inflation
rule caps improvement at +0.5 per cycle, so 7.5 → 8.5 takes at least two cycles **by
design**. Budget for that instead of fighting it — that constraint is what stops the
system from grading its own homework generously.
