# Books — a complete novel-writing pipeline for Claude Code

One repo, many books, **one shared pipeline**. Twelve specialist agents take a premise
through research, structure, voice, drafting, revision and continuity auditing to a
publish-ready manuscript — with mechanical gates that a language model can't talk its way
past, and a print/ebook path that ends at an IngramSpark upload.

It is in production use: the books in `books/` were written with it, and four of them are
finished, formatted and upload-ready in `completed-books/`.

## Quick start

```bash
git clone <this repo> Books && cd Books
bash tools/install.sh      # Python deps + the 12 agents (the web hook does this for you)
bash tools/doctor.sh       # verify — names anything missing
bash tools/new-book.sh the-glass-road "The Glass Road"
# fill in books/the-glass-road/STATE.yaml (premise, genre, comps, word floor)
```

Then, in Claude Code:

```
Run the book-orchestrator on books/the-glass-road
```

Full walkthrough: **[docs/GETTING-STARTED.md](docs/GETTING-STARTED.md)**.

## Documentation

| Doc | For |
|---|---|
| [GETTING-STARTED.md](docs/GETTING-STARTED.md) | Setup → your first chapter |
| [PIPELINE.md](docs/PIPELINE.md) | The 12 agents, the phases, every file |
| [CHARACTER-BIBLE.md](docs/CHARACTER-BIBLE.md) | Keeping a large cast distinct; the tic budget |
| [SERIES.md](docs/SERIES.md) | Multi-book series and canon carry-over |
| [QUALITY-GATES.md](docs/QUALITY-GATES.md) | Scores, gates, mechanical checkers, second opinions |
| [PUBLISHING.md](docs/PUBLISHING.md) | EPUB + print PDFs + IngramSpark, with the rejections we ate |
| [WORKFLOW-AND-HOOKS.md](docs/WORKFLOW-AND-HOOKS.md) | The git workflow, and how to change it |
| [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | What went wrong and what it means |
| [GLOSSARY.md](docs/GLOSSARY.md) | Genesis Score, CVI, Pattern #11, the Amelia Lesson… |

## Layout

```
.claude/         the pipeline: 12 book-* agents, /gemini + /grok commands, hooks, pipeline.conf
tools/           shared tools: install.sh, doctor.sh, new-book.sh, new-series.sh, make_epub.py,
                 make_noicc.sh, collect_completed.py, review scripts, apodictic (dev editor)
docs/            the documentation above
requirements.txt Python dependencies (pip install -r requirements.txt)
books/
  _template/     what a new book is scaffolded from
  _series-template/  what a new series is scaffolded from
  <name>/        one folder per book
  <series>/      a series folder: SERIES-BIBLE.md + one folder per book
completed-books/ generated — every finished book's upload-ready files
```

Each book folder is self-contained (`STATE.yaml`, `foundation.md`, `outline.md`,
`voice-dna.md`, `character-bible.md`, `manuscript/`, `evaluations/`, per-book `tools/`), and
its `STATE.yaml` is the source of truth for that book.

## What makes it different from "ask a model to write a novel"

- **The floor is the score.** Chapters are gated on their weakest dimension, not their
  average, so nothing hides behind one strong quality.
- **Structure is chosen, not defaulted.** The architect picks a macro-structure per premise
  and is explicitly forbidden from converging on ~20 chapters of ~5,000 words in three acts
  — the loudest machine-made tell there is.
- **The evaluator never scores its own prose**, and an anti-inflation protocol assumes it's
  biased anyway: max +0.5 per revision cycle, cited evidence per score.
- **Voice is engineered before it drifts.** A character bible with a hard tic budget stops a
  thirty-chapter cast from collapsing into one voice wearing hats.
- **Mechanical gates back up the judgement.** Python checkers count tics, repeated n-grams,
  simile load and grammar slips across the whole manuscript and fail by exit code.
- **State lives in files.** Any session, days later, resumes from `STATE.yaml`,
  `ENTITY_STATE.yaml` and `feedback/progress.md` — which is what makes a 200,000-word book
  finishable at all.
- **It ends at a real book.** Grayscale no-ICC interiors, CMYK wraps with a real barcode,
  EPUBs with working navigation, and the spec gotchas already discovered the hard way.

## The update rule

The pipeline is edited in **one place — the root `.claude/` + `tools/`** — so every book
inherits every improvement. Improve an agent, a gate, or a shared list there, not inside a
single book's folder. The one exception: each book's `tools/style_check.py` ALLOWLIST is
book-specific by design.

## Git workflow

Default is **`main` only — no branches, no PRs** — enforced by hooks, because manuscripts
don't merge. If that isn't right for you, set `WORKFLOW_LAW="off"` in
`.claude/pipeline.conf`. See [WORKFLOW-AND-HOOKS.md](docs/WORKFLOW-AND-HOOKS.md).

## Credits and licensing

The agent framework is adapted from the open-source
[Best Seller Studio](https://github.com/felipelobomotta-blip/best-seller-studio) project,
substantially extended here: the premise forge, macro-structure selection, the character
bible and tic budget, motif caps, mechanical gates, series support and the print pipeline.
`tools/apodictic/` is a bundled developmental-editing plugin with its own LICENSE.

**The pipeline and the books are different things.** The manuscripts, notes and cover art
under `books/` and `completed-books/` are the author's copyrighted work, not sample content
— no license is granted to them. If you fork this to write your own books, delete the book
folders and keep `.claude/`, `tools/`, `docs/` and the two templates.
