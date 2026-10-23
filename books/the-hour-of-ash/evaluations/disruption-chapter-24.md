# Disruption Report: Chapter 24, "Lucius"

**Verdict on intake:** a strong chapter. It is already subverted (the teeth; the tenderness is in the hoof-trimming), and it already has its chaos: the peas, Mrs. Dunphy, the legs shaking twice, the ugly sentence, Statia's lentils, and "Which cock?". So it got a light touch: three operations, plus the lime ruling, plus two small birth beats made stranger. Backup: `manuscript/reports/chapter-24-pre-disruption.md`.

## Operations Applied

| # | Operation | Location | Before → After |
|---|-----------|----------|----------------|
| R | Editor ruling: residue on Valens's body (CLOSED after Ch.21) | *Ninth hour*, *Cockcrow* | **Cut:** "white with lime to the knees"; "He had stopped at the well to wash his arms, and they were wet to the elbow."; "Statia eyed the lime on his legs"; "The lime on him smelled of the kilns."; "and there was horn dust still in the creases of the fingers"; "against the lime on the tunic". **Recast** (the one beat that needed lime): "It'll not show under the lime." → "That arm's carried lime since dawn." The line now refers to his day's work and shows nothing on his body. It still answers the nail marks the same way: his arm can take it. No residue beat is left on Valens. Felix's "horn in his hair" stays, since he is not Valens and Grata's "there's a stable on it" depends on it. |
| 7 | Missing paragraph (the predictable birth hush) | *Cockcrow* | Cut "For a breath, nothing." and the stand-alone "He cried." → "…into her hands, and he was crying before she had him turned." The held silence before the first cry is the beat every birth scene sets up. This one gives no hush: he is loud from the start, which is truer. |
| 7b | Predictable beat (the women's chorus) | *Cockcrow* | "Grata laughed and cried at once, and held me" → "Grata held me". Her first response is now the bill to the goddess. Her tears stay where they are truer, later and blamed on the dittany. |
| + | Household absurdity at the sacred moment | *Cockcrow*, the cloth on the floor | Added: "My man wears that to the Floralia," said Grata. / "It's a cloth now. Fetch the father." The cloth the father must lift his son from turns out to be the husband's good tunic. It is said once and never explained. It merges Statia's existing "Fetch the father" into her verdict line, so it costs no extra tag. |
| 1 | Simile surgery | *Ninth hour*, Statia unpacking | "She set it out the way I laid out a bench; her hands knew the knife's place ahead of her." → the extension is cut and the simile left raw. |
| 7c | Explanation cut | *Cockcrow* | "Valens was right there. He had been standing just outside it." → the second sentence is cut, because "right there" already says it. |
| 7d | Explanation cut / near-aphorism | *First light*, the fontanelle | "Nobody had to mend it. It was meant to be left open." → it now ends on "Nobody had to mend it." The second sentence stated the theme and edged toward a closing aphorism. |
| 7e | Explanation cut | *First light* | "The child was in his arm now. He had taken him from me once the feeding was done, and had not given him up since." → the second sentence is cut. The *Cockcrow* shard already showed that he won't give him back. |

## Operations NOT Applied (and why)
- **Irrelevant thought:** skipped. The peas and Mrs. Dunphy are already here, and the Ch.22/23 inserts rule out a third.
- **Emotional control break:** skipped. The legs shaking twice is already a failed management that the narration does not process.
- **Ugly sentence:** skipped. The Writer's one exists ("I was tired and it was hot and I wanted water…").
- **Precision deflation:** skipped. The only real counts are "four times" (plot: Felix's complaint) and Grata's cakes (the bargain), and both serve the story.
- **Negation break:** skipped. There are 0 narration pivots, and the "not Greek, not Syrian" is the husband's speech, part of the Ch.25 plant.
- **Dialogue mess:** skipped. Felix's stacked questions, the untagged shard and "Were you afraid?" answered with the mule are already off-centre. Messing up the Chaldean exchange would blur the plant.
- **Father's awe / first look:** left alone. The anchor (the jar on locked arms, "by inches", "He's cold." / "He's wet.") is already the subversion.

## Strongest Disruption
The cry and the tunic, together. The reader braces for the hush and then the first cry, then the women's tears, then the solemn floor. Instead they get a baby yelling at once, Grata pricing the goddess, and the father lifting his son off the husband's festival tunic. It is a Pompeian household being itself at the one moment a birth chapter expects reverence. The anchor that follows lands harder against it.

## Risk Assessment
- "That arm's carried lime since dawn." reads as dry and literal, Valens's register. It is the only lime left in the chapter and is in speech, so it shows no residue.
- The tunic exchange adds 15 words of dialogue at cockcrow. It holds the anchor up for a moment but does not dissolve it. Bible re-sync: add Grata's line and Statia's "It's a cloth now." to the Ch.24 walk-on and STATIA card quotes. Mark the lime and horn strings above as CUT, never to be restored.
- The header comment's word counts are stale (they were already stale after the dialogue pass).

## Laws checked
No foreshadowing added. No new gesture beats: one "eyed" was removed, and the gesture gate is clean. Teeth are still at 3. No laugh or mouth beat for Mara. No present-tense generalisation. No tomb or door. The child is never called a citizen. No wall-turn close and no singing walk-on. "I hated the midwife.", the untagged *Past midnight* shard and the closing watch paragraph are untouched.

## Gates
- `bash tools/check_chapter.sh 24` → **ALL MECHANICAL GATES CLEAN**. One intermediate echo ("that's my husband's", Ch.20) was varied to "My man wears that to the Floralia".
- `python3 tools/tic_report.py --echoes 24` → 0 echoes, 0 command echoes, 0 spoken-line echoes.
- **Dialogue: 27.9%** (show_tell, 6,030 words), up from 27.3%; the band is 25–35.
