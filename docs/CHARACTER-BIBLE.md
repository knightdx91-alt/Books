# The character bible

`books/<slug>/character-bible.md` — the canonical home for the cast's **voice and
distinctness**. One entry per named character, each ending in a DISTINCTNESS GUARANTEE.

This is the file that stops a thirty-chapter book with twenty named characters from
collapsing into one voice wearing different hats. It is also the file most likely to be
skipped, because a book seems fine without it right up until chapter nineteen, when three
characters have started sounding like the narrator and the fix is a manuscript-wide pass.

## The three canon files, and which one you want

| File | Holds | Question it answers |
|---|---|---|
| `ENTITY_STATE.yaml` | Facts: names, ages, places, objects, timeline, who-knows-what-when | "Was her coat green in chapter 4?" |
| `voice-dna.md` | The **narration's** voice + the cast-wide differentiation matrix and anti-pattern budget | "How does this book sound?" |
| `character-bible.md` | Each **character's** voice: worldview, syntax, evasion, physicality (never a tic) | "Would Marek say this line?" |

They overlap on purpose but they are not substitutes. A continuity error is an
ENTITY_STATE problem; a character who sounds like everyone else is a character-bible
problem, and no amount of fact-checking catches it.

## Who writes it, and when

**The architect seeds it** during the voice dispatch (Phase 2.5), alongside `voice-dna.md`.
It is a **required deliverable**, not an optional extra — a missing bible means re-dispatch
the architect. It should cover, at minimum, the protagonist, the antagonist, and every
character who speaks in two or more scenes.

**The writer maintains it.** The moment a new named character appears on the page — even a
functional one — the writer adds their entry *before finalizing the chapter*. That timing
matters: written at introduction, the voice gets designed. Written retroactively at chapter
30, it gets described, and by then the drift has already happened.

**The evaluator audits against it.** A newcomer with no entry, or any character who has
acquired a tic or a device on the page, is a finding — and a tic anywhere in the cast caps
the Characters dimension at 7.5 no matter how good the chapter otherwise is.

**The dialogue-polish pass writes from it**, running the cover-the-name test against the
cards.

**No bible, no chapters — enforced.** Every book folder must have a `character-bible.md`
before a chapter is written or revised, whatever the run mode (genesis, revise/expand, or a
book started before this rule). A PreToolUse hook, `.claude/hooks/require-character-bible.sh`,
blocks any Write/Edit to `books/**/manuscript/chapter-*.md` or `manuscript/chapters/*.md` when
the book folder (the one holding `STATE.yaml`) has no bible, and says how to fix it. The
SessionStart hook lists every book that lacks one, and `tools/doctor.sh` warns.

To create one: `bash tools/ensure-character-bible.sh <book-dir>` copies the template stub
(`--list` shows every book still missing one). Then populate it: from the blueprint for a
new book, or by following *Retrofitting* below for a book with chapters already written.
The book-orchestrator and book-writer agents do both steps themselves when they find it
missing. Switch: `REQUIRE_CHARACTER_BIBLE` in `.claude/pipeline.conf` (default `on`).

## How distinctness actually works: the four axes

Distinctness is **not** "give everyone a verbal tic." A cast where everybody has a
catchphrase is the single most common way a large cast reads as machine-made. Characters
are separated on four axes, in roughly this order of power:

1. **Attention / worldview** — what they *notice*, and what they reduce the world to. The
   deepest differentiator by a distance. A carpenter, a priest and a thief walk into the
   same room and three different rooms come out.
2. **Syntax / register** — sentence shape and formality. Clips vs spirals; subordinate
   clauses vs fragments; questions vs statements.
3. **Evasion** — what they will *not* say. The subject, register or feeling they refuse.
   Silence characterizes harder than speech.
4. **Physicality / silence** — the body-tell or pause that stands in for a spoken tic.

There is no fifth thing. **Nobody gets a verbal tic.**

## NO TICS — the author's standing law (hard, every book, permanently)

Ruled by the author on 2026-10-18 and not negotiable per book: **the tic budget is zero.**
No character in any book — the narrator included — leads with a verbal tic, catchphrase,
refrain, pet phrase, or signature device (no counting habit, no pricing-in-feelings, no
misquoted-proverb habit, no cataloguing-under-stress, no "as I always say"). A character
is distinct on the four axes above or they are not distinct yet; a tic is never the fix.

What this means in practice:

- **The bible records `Tic-bearer roster: NONE`** and every card's tic line reads
  `none — distinguished by <axis>`. The architect never designs a tic; the writer never
  hands a newcomer one; dialogue-polish removes any that forms.
- **No devices either.** Counting, listing, pricing, rating, quantifying and cataloguing are
  the same device in different coats, and the device is retired for everyone — not rationed
  to one character.
- **Motifs are objects and situations, not phrases.** A recurring *image* (the lamp, the
  knot, the stamped loaf) is fine; a recurring *line* is a tic. The style-gate ALLOWLIST
  stays short (≤5 phrases) and each entry is capped at 3 uses book-wide.
- **Gestures are tics too.** Stage business repeated with the wording varied — characters
  forever picking things up and setting them down, nodding, swallowing, sighing, looking
  away, pausing "for a long moment" — is a tic the n-gram scans cannot see, and readers feel
  it by chapter six. `tic_report.py` counts gesture *classes* by meaning and fails a cluster
  (4+ of one class in a chapter, or more than 0.3 per 1,000 words book-wide). A motif object
  may recur; the *handling* of it must not become the book's reflex.
- **Mechanically enforced every chapter** (see [QUALITY-GATES.md](QUALITY-GATES.md)):
  `voice_wear_check.py` fails on any phrase a POV repeats across chapters;
  `tic_report.py --gate` fails on any non-allowlisted phrase recurring 3+ times book-wide
  and on any spoken phrase of 3+ words recurring in dialogue (a catchphrase forming); the
  retired-phrase list fails on sight; the evaluator's tic-proliferation scan caps
  Characters at 7.5 if ANY character leads with a tic.
- **Watch for bleed from the narrator.** A POV character's habit leaking onto secondary
  characters is the failure that makes everyone sound alike, and it is nearly invisible
  from inside a single chapter — which is why the gate is book-wide, every chapter.

### The Amelia Lesson

Named after the book where it happened, and kept in the template so it doesn't happen
again: a quantifying/counting device and the phrase **"never once"** calcified into a tic,
then *bled across multiple characters* until the cast sounded alike — and fixing it needed
a manuscript-wide de-tic pass.

The lesson isn't "watch for that phrase." It's that voice tics **spread**, because each
chapter's writer imitates the voice they can see in the previous chapters, and a habit
repeated three times reads as intentional. That is why the budget is now zero rather than
"a few, earned": the earned ones spread too. The bible carries a **retired / at-risk
phrase list** (seeded with "never once"), and `voice_wear_check.py` + `tic_report.py`
catch calcification every chapter. Prevention by construction, because detection at
chapter 30 is already too late.

## The SPENT / CLOSED ledger (pipeline standard since The Hour of Ash)

A long book's real risk is not a catchphrase but a **re-used move**: the same laugh, the same entrance,
the same comparison frame, rebuilt in fresh words twenty chapters later. So at every chapter's bible
sync the writer (bookkeeping mode) adds an `At-risk after Ch.N` block that logs what the final page
spent:

- **USED (n of cap)** — a phrase or image with budget left;
- **SPENT** — used up; no further uses;
- **CLOSED** — never again, in any wording (a body-channel, a frame, a set piece);
- **CUT** — strings a pass removed; they must never be restored;
- **guards for the next chapter** — what its hook/pull may not be, what it must not pre-empt.

The writer, dialogue-polish, the disruptor, the editor and the evaluator all read the ledger before
touching a chapter, and a replacement string that rebuilds a closed move is a finding, not a fix.
Narrated states (a character's closed eyes, waiting, stillness, a trembling hand) are counted like
gestures: more than 3 in a chapter fails.

## The card format

```
#### MAREK VOSS — harbourmaster, Rieke's estranged brother
- Attention / worldview: reads people the way he reads weather — for what they are about
  to do, never for what they mean.
- Vocabulary band: dockside trade, tide tables, ship names; no abstractions he can't touch.
- Syntax fingerprint: clips. Two clauses maximum, then he stops. Never subordinates.
- Evasion — never says: anyone's name who has died. Substitutes "him", "her", "that one".
- Physicality / silence: turns his cup a quarter-turn before answering anything hard.
- Verbal tic: none — distinguished by evasion + clipped syntax.
- DISTINCTNESS GUARANTEE: the only character who refuses names, against Rieke, who uses
  them like handholds.
- Sample line: "Tide's wrong. Ask me tomorrow."
```

Then the cast-wide matrix, which is the cover-the-name test pre-solved:

| Character | Sharpest distinguisher | Contrast vs nearest character |
|---|---|---|
| Marek | refuses to say names | Rieke over-names everyone |

If any two characters share their sharpest marker, differentiate further **before** you
finish the bible. Solving it here costs a sentence; solving it in chapter 22 costs a pass
over every scene they share.

## The cover-the-name test

Take a page of dialogue, delete every speaker tag and name, hand it to someone. If they
can't tell who is speaking, the voices aren't distinct — regardless of how good the cards
look. `dialogue-polish` runs this on all speaking characters in a chapter; the evaluator
runs it as part of Dimension 3.

## Retrofitting a bible onto an existing manuscript

Common case: a draft exists (yours, or an earlier pipeline run) and there's no bible.

1. **Extract the facts first.** Run `entity-tracker` in BUILD mode over the manuscript to
   get `ENTITY_STATE.yaml` — you need the full cast list before you can audit voices.
2. **Sample each character's dialogue.** For every named speaker, pull their lines across
   the whole draft (`grep` on names is a blunt but effective start). You are looking for
   what they already do, not what you wish they did.
3. **Write the card from the evidence**, on the four axes. Where a character has no
   distinguishing voice yet, say so in the card — that's a revision target, not a failure.
4. **Audit for the collapse.** Count how many characters lead with a tic; look for two
   characters sharing a device; look for the narrator's device on secondary characters. In
   an unguided draft you will usually find at least one.
5. **Fix by subtraction first.** De-tic the bleed (remove the habit from everyone who
   borrowed it) before adding new distinguishing habits. Subtraction is safer: it can't
   introduce continuity problems, and an over-tic'd cast is nearly always the actual
   disease.
6. **Then let the evaluator re-score Dimension 3** and treat the delta as your check.

## Series

A returning character keeps their card. Copy it forward into the new book's bible and
evolve it deliberately — a book of grief should change a voice — but never re-invent it
from scratch, and never hand a returning character a tic (nobody has one). Re-run the
recurrence gate against the *new* book, since a phrase that was fresh in book one is a
fingerprint by book three. See [SERIES.md](SERIES.md).

## Common failure modes

| Symptom | What's actually wrong |
|---|---|
| Everyone sounds thoughtful and observant | The narrator's worldview has been given to the whole cast |
| Any character has a catchphrase | The no-tics law ignored; distinctness outsourced to decoration |
| Two characters feel like one | Device collision — check the one-device map |
| Voices fine early, mushy after ch.20 | The bible stopped being updated at introduction time |
| A phrase that was striking now grates | Motif calcification — check the retired/at-risk list and the motif cap |
