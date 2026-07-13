# CLAUDE.md — Black Jewels–like book (working title)

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
- **Read `research/worldbuilding-locked.md` first** — the author-locked world bible.
  The architect BUILDS ON it; never overwrite it.
- **Magic = two axes:** placement = tier (Unlit → left hand/Inner → +right/Outer →
  +forehead/Trinity+Gift → chest/Keystone); celestial grade = depth
  (**Dawn → Dusk → Star → Void**, each lesser/greater). Read as "placement + grade."
- **Cosmology (one fact, three faces):** gems are goddess **Neth's** night-light in
  stone; she bound the titan **Ossuth** at the founding, pouring herself into the
  **Binding**, so her fading = rarer deep-gems = weakening Binding.
- **Conflict = taboo AND hunted, one system:** Church/Crown outlaws the Trinity;
  the **Vigil** (with rotten core the **Ashen Court**) uses that taboo as cover to
  harvest deep-gems — the Court hoards them to stay immortal, hastening the failure.
  On-page villains stay HUMAN; Ossuth is the off-page clock.
- **Hero:** 17-yr-old one-rank orphan (a left-hand Dawn); dedicates alone at a
  backwater shrine (army enlists/dedicates at 17); gifted the chest **Keystone** +
  a deep-grade Trinity by the disguised goddess; hides his 3rd & 4th gems.
- **Prophecy/theme:** the Keystone-King unites LIVING bearers so shared light renews
  the Binding — **hoarded dying light vs. shared living light.**
- **Distinctiveness (hard):** inspired-by Anne Bishop ONLY. No Bishop signature terms
  (Jewels, Blood/landen, Territories, Offering, caste, Warlord Prince). Keep separate
  from `books/sygl-book/` (the sigil system) — different story, do NOT merge.
- **`Domash`** capital war-Domain spelling kept as-is.

## Open author decisions (ask, don't invent)
- **Proposed names pending final sign-off:** the Vigil, the Ashen Court, Neth (the
  Last Light), Ossuth (the First Dark). The architect may build on them; lock before
  drafting to avoid a rename.
- **Working title** ("Black Jewels–like book") — architect to propose a real title.
- Architect to INVENT (keep distinct from Bishop): the gemstones per celestial band,
  the hero's Trinity Gift, the Domain map + names, Neth's surviving cult.

## Status (update as you go)
- Phase 1. Source staged + **worldbuilding LOCKED** (`research/worldbuilding-locked.md`).
  Core spine decisions resolved. **READY for the architect pass** (foundation.md +
  outline.md + voice-dna.md) — not yet run. Resume: `feedback/progress.md`.
