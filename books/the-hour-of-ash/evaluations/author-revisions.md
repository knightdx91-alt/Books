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

## Independent fit check
*book-evaluator, 2026-10-24. Fit check only, not a full chapter evaluation. The chapters were not edited. Replacements were tested on a scratch copy of the book.*

### Verdicts
| Insertion | Verdict |
|---|---|
| Ch.6 l.251–253, "Was it on him when he died?" / "It was by his bed." | **ADJUST.** Keep the question and replace the answer (below). |
| Ch.11 l.97, "In the snow it had nine of its hours … Now it's eleven." | **FITS.** No change required. One optional note follows. |

### 1. Ch.6: ADJUST

**What works.** The question is in Valens's register. It is a where/who question, it does not subordinate, it does not ask why, and it makes no comparison. It reads as one of his questions, not as a stated belief, and the narrator never explains it. The order also works. The death is raised before he turns the watch face up, so the next beat ("The thin seconds hand was going round … his face stayed as it was" / "Something's going in it") lands as a dead man's thing that moves by itself. The reader gets the unease from the sequence alone. The line agrees with Ch.7 l.220 (wondering whether he winds it) and with Ch.12 l.132, where he hands her the pouch before he washes a dead man's blood off his hands. That beat now gains weight without reaching forward. "By his bed" agrees with Ch.1 l.387 (the nightstand). There is no foreshadowing, nothing from the SPENT/CLOSED/CUT lists, and the gates are clean.

**Why it still needs adjusting: the answer confirms the death, and two later lines rest on its never being confirmed.**
1. **Ch.15 l.244–250 (missed by the log):** "The boy says it was your father's." / "It was." / "He'll be wanting it, then." / "He will not," I said. Valens assumes the father is alive, and Mara's "He will not" works as her circling admission. If Ch.6 has already given him the death in a question he asked himself and an answer he accepted, then in Ch.15 he has forgotten it. Nothing on the page supports a forgetful Valens, and his card rules out a wry aside in Greek. This is a continuity break, Logic type. The Hostile and Devoted readers would both catch it.
2. **Ch.6 l.667, same chapter:** "Somebody there wants you back, a father or a husband." Valens builds his reading from evidence in order. Nine paragraphs after accepting the father's death, he names a father as the pursuer. (It is softer than item 1, because he does not believe her about a husband either, but it reads as a slip.)
3. **Mara's card** ("her father's death stated plainly: never; she circles it through his objects"). "It was by his bed" goes through an object, but it accepts the premise "when he died". That makes it a confirmation, which is as close to stating the death as she ever comes. Silence is truer to the card ("When she cannot speak she *inspects* something").

**Replacement (tested). Keep l.251. Replace l.253:**

> "Was it on him when he died?"
>
> The gray had burrs in her mane, worked in close to the skin. I looked at those.

- The question stays unanswered, so the unease is still on the page. Mara's evasion is an inspection, in a clipped two-sentence rhythm ("plain short declaratives when afraid"). He lets it go, and "He was a long while over the back of it" follows on as before.
- The repair runs downstream. Ch.15's "He'll be wanting it, then." now reads as Valens probing again at a question she left open, and "He will not" becomes the answer she finally gives. l.617 ("You said he didn't need it.") and l.667 ("a father or a husband") both stand unchanged.
- **Gates on the scratch copy:** `check_chapter.sh 6` gives ALL MECHANICAL GATES CLEAN (exit 0). Echo scan: 0. Closed ledger: clean. Voice-wear strict: clean. `tic_report.py --echoes N` for N = 7..30 is byte-identical to the live book. `tic_report.py --gate` and `voice_wear_check.py` differ only in the Ch.6 word count. **Tested and rejected:** "There were burrs in the gray's mane…" created a cross-chapter echo in Ch.9 ("the gray's mane"), so it became "in her mane".
- **Alternative if the author wants the spoken answer kept:** keep "It was by his bed." and repair both downstream lines instead. At l.667, "a father or a husband" becomes "a husband or a guardian". That swap was tested and is clean, and the guardian is period-true for a woman whose father is dead. Ch.15 l.248–250 would also need its two lines rewritten (not drafted or tested here). The replacement above touches only the inserted line, so it is recommended.
- **Syncs needed after either fix:** add the beat to the VALENS card's Ch.6 block and the knowledge entry to ENTITY_STATE `knowledge_index`. With the recommended fix: Valens asks, Mara does not answer, and the death is answered only by Ch.15's "He will not". Neither file has been synced yet.

### 2. Ch.11: FITS

- **Voice and rhythm.** Three flat, unsubordinated statements. "Its hours" is the only marker, with no comparison (a contrast of two quantities is not a simile), no wonder and no rule. It answers her "It is fast" as he answers everything: he does not argue, he gives evidence, here that the day itself is what moves. It follows naturally from the existing l.93 ("Since the mountain he had kept it going, every day") and from Felix's daily-winding report (l.119). It also fits his dawn waking ("I am.", l.229). It sits easily beside l.221 ("Why does anybody need the hour that close? The day's got a middle."): he watches the watch closely and still has no use for the precision. Nobody comments on the line, and Mara's silence keeps it from being explained. "And some over" is deliberately imprecise, which works against the precision-flex pattern. Speech habits: the "It hasn't…" openers stay at 2 book-wide (here and Ch.20 l.245), because the opener was already there. He gains one observation in his own units, which does not turn into a counting device. There is no foreshadowing: Ch.18 l.105 sets the hands against a noon shadow and does not pick this up.
- **Continuity.** The watch has been with Valens and running from Ch.6 to Ch.11 (ENTITY `fathers-seiko-watch`: Ch.7 pouch, Ch.9 not mentioned, Ch.11 pouch, Ch.12 pouch). Since it has never stopped or been set, the count is his own. The watch running fast does not affect an interval measured from sunup to sundown.
- **Astronomy, Delphi at 38.5°N, Julian calendar, AD 70–71, computed for a flat horizon with refraction.** Late November to the end of January gives about 10.1h falling to 9.4h at the solstice and back to 9.7h. That is "nine … and some over" whether "in the snow" means the climb day or the snow season. In February, the 10th gives 10.5h, the 20th 10.9h, the 25th 11.1h, and 1 March 11.2h, so "eleven" holds from about 8 Feb to 7 Mar. **Correction to the log's reasoning:** no almonds appear anywhere in the manuscript. The February dating rests on Ch.10 ("In four months" since an October arrival; "The middle of winter's gone by."), on Ch.11's leafless fig putting out green tips, and on Ch.12 being the 4th of Bysios. The mean new moon of 18 Feb AD 71 puts the 7th of Bysios at about 25–26 Feb and Ch.11 at about 13–21 Feb (10.6–10.9h). **This line now pins Ch.11 between mid-February and early March.** Record it in ENTITY_STATE: if Bysios is ever dated to the March lunation (7 Bysios about 27 Mar), "eleven" would be short, since the flat-horizon day would be about 12h, and only Delphi's high horizon would save it.
- **Optional note (investigate only, no change required).** "Nine" sits six lines below "The short one's past the nine" (l.91), the first as a dial position and the second as a count. A reader might connect the two for a moment. Every tested way of avoiding it ("didn't make ten") piles up negations after "It hasn't". Leave it as written.
- **Gates (live file):** `check_chapter.sh 11` gives ALL MECHANICAL GATES CLEAN, with echo scan 0 and closed ledger clean.

### Gates run on the live files for this check
- `bash tools/check_chapter.sh 6`: ALL MECHANICAL GATES CLEAN.
- `bash tools/check_chapter.sh 11`: ALL MECHANICAL GATES CLEAN.

BIAS CHECK: this check was made by the same system that wrote the insertions. The Ch.15 contradiction it found is a mechanical fact on the page. The fit judgements still want the author's ear.

## Correction (entity re-sync, 2026-10-24)

- The fit check's "no almonds anywhere in the manuscript" is wrong: Ch.9 and Ch.13 have them, and they support the February dating of Ch.11.
- A fast-running watch would inflate a sunup-to-sundown count slightly. ENTITY_STATE treats the watch's hours as true hours, and the line still fits mid-February to early March AD 71 at Delphi.
