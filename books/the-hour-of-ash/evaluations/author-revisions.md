# Author Revisions — The Hour of Ash

## 2026-10-24 — Watch period beats (author Terry: "fix those 2 things, but make sure they fit")

### 1. Ch.6, superstition (chapter-6.md l.251–253, the first watch scene in the lane)

Inserted between Mara's "He does not need it." and "He was a long while over the back of it…":

> "Was it on him when he died?"
>
> "It was by his bed."

**Why it fits:**
- A practical question in Valens's own register. It asks where and who, like every other question he asks in the chapter. It shows that he worries about a thing that touched a corpse, but he never voices a belief and the narrator never explains. His face still "stayed as it was" a few lines on.
- It follows naturally from his "You took it from him." He reads "He does not need it" as a death, and checks before he keeps the thing. Ch.6's later "You said he didn't need it." still stands.
- Mara answers through the object, never stating the death herself (her evasion on her card). "By his bed" agrees with Ch.1, where the Seiko is on the nightstand "where he had always taken it off at night".
- His questions on the ride down ("What's in it that goes?" / "Who makes them?" / "For hire?" … "I won't drop it.") now read as a man making sure it is men's work.
- **Rejected:** the spit into the tunic fold. The bible marks it CLOSED: Ch.4's goat boy spits into his tunic neck against the uncanny, and Ch.13's Kallia spits into the fold of her dress ("2 book-wide, CLOSED"). Valens also spits on his whetstone in Ch.11, and Ch.6 already carries the spitting-oak exchange.

### 2. Ch.11, seasonal hours (chapter-11.md l.97, the watch read from the pouch)

Before: `"It hasn't stopped." He pulled the pouch shut.`

After:

> "It hasn't stopped. In the snow it had nine of its hours between sunup and sundown, and some over. Now it's eleven." He pulled the pouch shut.

**Why it fits:**
- Short, flat, unsubordinated statements. There is no comparison, no wonder and no rule. "Its hours" is the only marker that the watch keeps different hours from his own. Mara, who knows about temporal hours, registers nothing, so the astronomy goes unexplained.
- The numbers hold at Delphi (~38.5°N). "In the snow" is late November AD 70 (Ch.6), about 9h45m from sunrise to sunset, so "nine … and some over". Ch.11 falls in late February AD 71, ten or more days before the seventh of Bysios, with the almonds coming into flower, about 10h50m–11h15m, so "eleven".
- It agrees with his later "Why does anybody need the hour that close? The day's got a middle." in the same chapter. It sets nothing up for Ch.18, where the hands are near sun time, so there is no foreshadowing.
- **First draft varied:** "and most of the next" echoed Ch.5 and failed voice-wear self-repetition. It became "and some over".

### Gates
- `check_chapter.sh 6` and `check_chapter.sh 11`: ALL MECHANICAL GATES CLEAN, both before and after. Echo scan: 0 before, 0 after, for both chapters.
- `tic_report.py --echoes N` for N = 6..30: the totals and the full listings are byte-identical before and after. Ch.21 is 54 and Ch.22 is 93 (grandfathered); all others are 0.
- `tic_report.py --gate`: clean. Only the word counts changed (Ch.30's count changed because of the concurrent Ch.30 pass, not this one). `voice_wear_check.py`: clean, and the WARN list is back to its pre-edit count.
- Header comment on both chapters: "Author revision 2026-10-24: watch period beats".
- Not touched: Ch.30, character-bible.md, ENTITY_STATE.yaml. Not committed.
