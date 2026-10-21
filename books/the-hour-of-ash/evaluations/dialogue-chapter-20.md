# Dialogue Polish Report: Chapter 20, "The Mender's Shop" (run 2)

This pass covered dialogue only, on the Writer's draft of `manuscript/chapters/chapter-20.md` (2026-10-21). The chapter is a Collage with 6 breaks, gear mid and a ledger band of 30–40%. The brief set a target of 33–36%, reached by turning narrated speech into spoken lines and never by padding.

**Kept exactly.** These were checked by script against a copy of the chapter taken before the pass.
- The opening italic notice (*A bronze pot has walked off…*), byte-identical.
- Grata's closing speech, ending "It's not my fish. It's a child you've got." The last paragraph is byte-identical.
- The 6 breaks (6 before, 6 after).
- The tremor note paragraph, byte-identical.
- Zosimus's request: "And then how do I know it from the other thirty-nine?" … "Leave me the crack. Leave it where the boys can see it's spoken for. It's dark on that stair, and I'll want to find it with my thumb." This is byte-identical, and the theme stays unspoken. "Nobody at home had ever paid me…" is unchanged.
- The fountain and the pebble, from the child crawling round the trough through "That's a good stone," byte-identical. That covers the father, "It ended when it ended.", Grata's wordless cup and Valens on the roof. Nothing explains it. The only edits in section 6 are to the gossip lines *before* the child (see below).

**Narration.** It is untouched except for these changes:
- tags and beats within one sentence of a changed line;
- the narrated speech that became speech;
- one comprehension sentence;
- three one-verb fixes for compliance echoes.

A dialogue-polish line was added to the header comment. The character bible was **not** edited; the sync list is under Remaining Concerns.

## Audit Summary
- **Dialogue ratio:**
  - show_tell: 30.6% → **33.3%**.
  - shape_check: 31 → **34**.
  - Raw count: dialogue words 2,464 → **2,812** (+348); narration 5,581 → 5,610 (+29).
  - The growth is speech. The few narration words added are tags and beats for new lines.
- **Words:**
  - shape_check: 8,027 → **8,404**.
  - style: 8,430.
  - show_tell: 8,433.
  - `wc -w`: 8,946 including header comments.
  - Range 7,700–8,700.
- **Median sentence:** 16 → **16** (gear mid, held). Mean 17.5; >40w 4.2%. Similes 14 by metaphor_check (1.7/1k style). Em-dash 0. "as if" 0.
- **Conversations analyzed:** 27.
- **INDISTINCT:** 0.
- **WEAK:** 4, all resolved.
- **FLAT_DIALOGUE:** 0. The outline's subtext layer is that the customer's wish teaches Mara without anyone saying it. That is carried by the unchanged request and by Valens's "Left like that." Nothing was added to it.
- **Exposition dumps:** 0. Valens's fig speech ("A young tree carries them all summer…") answers Felix's direct question and stays.
- **Tag overuse:** none. "said" stays the default; "told" is always to the listener. No adverbs, and said/told-to-a-non-listener stays at 0. The new tags are "said", "told her", "told us" and "finished" (the carter reading the board back).

### House-rhythm problems found and fixed
These are not n-gram gates, so they were counted by hand.

**"Then…" speech openers: 10 → 1.** The draft had ten, spread across seven speakers. The at-risk list allows at most 2 per chapter outside a listed sequence. Only Valens's "Then I'll keep to the other." remains. The rest were recast:
- "He should have chained it to the wall." This now mirrors the wife's "He should have chained you."
- "That wants shouting."
- "I'd only break it in the same spot, looking for it."
- "What do we eat out of tonight?"
- "That's yesterday's bread."
- "What's she for?"
- "It's the wind does it, and I'll charge the wind."
- "Polybius is standing on it,"
- "That's wrong."

**"And…" rejoinders: 7 → 3** (the cap is 4). My own first-pass "And then his bread," was replaced. Grata's "And you'll do me a board" became "You'll do me a board too". The painter's "And you, lantern" became "You, lantern". "And the dowry in figs." became "With the dowry in figs." Three remain: Mara's "And a tree.", Valens's "And it's the same." and Zosimus's protected "And then how do I know it…".

**Commands echoed as compliance: 3 → 0.**
- The painter's "Hold it, then." was followed by "Felix held the ladder." It is now "Felix had both fists round the ladder's legs and his weight on his heels."
- "hold that light still" was followed by "The lantern boy held the light up". It is now "The lantern boy's light sagged by degrees until he was told about it, and then it rose."
- "Leave me the crack." was followed by "I left it a thread's thickness proud". It is now "I trimmed it to a thread's thickness proud of the clay." The request itself is unchanged.
- I also took "Felix led me on" out of reach of Grata's "Go on with the boy". It is now "From there Felix took me to the fountain".

**"Whose" question:** 0. A draft line of mine ("Whose is it?") would have been the book's third "whose" question, which is a refrain on the at-risk table. It was cut before the final page: Mara asks "What name goes on the tag?"

## Voice Distinctiveness Results
| Character | Lines | Distinct | Weak | Indistinct | Post-Polish |
|-----------|-------|----------|------|------------|-------------|
| Valens | 32 | 31 | 1 | 0 | DISTINCT: short level statements about animals, ground and the fig. Bare "No." 0. Narrated non-answers 0. Comparisons 0. Orders to Felix 0 ("Tell her it hasn't" goes to Mara). "Then" openers 1. |
| Felix | 22 | 22 | 0 | 0 | DISTINCT: stacked questions, then boasts or facts. 15 speeches end on a boast or a fact (brief: ≥2), for example "Nobody on this road mends like her!", "That's a drop of two of me.", "A blind man could tell that.", "For bread.", "It's people wrote all this.", "There's a name scratched on every wall in this town but mine." No "Is it" or "Is that" opener; no palm scratched. |
| Grata | 11 | 10 | 1 | 0 | DISTINCT: comma-spliced floods that tell, ending on a command ("Shout at the fullers."). Questions 0 anywhere on the page, the reveal included. Teeth 0. Touches: upper arm, forearm, fingertips at the wrist, all unchanged. |
| Mara | 30 | 30 | 0 | 0 | DISTINCT: plain, uncontracted Latin with a dry turn. New lines: "There is no fish, and you are not in it," / "Where does one buy paint, in this quarter?" / "Which are the dogs?" / "I can make it hold coins," … "Whether it fills is your affair." / "His bread comes last," … "It says it is good." / "What name goes on the tag?" |
| Zosimus | 6 | 6 | 0 | 0 | DISTINCT: flat statements stacked into a complaint. The one new line is about place, never feeling: "Zosimus. Of the crossing baths. Down at the furnace, not up with the bathers." Hermes is still named twice in his mouth (no third), and no line of his recurs. No catchphrase. |
| Walk-ons (17 speakers: the leek couple, the cook, the coppersmith, the stewpot woman, the tile carter, the girl and her mother, the quarryman, the turner, the fuller's wife, the board carter, the rain customer, the night crew, the fountain line, the dyer, the fish carter) | 1–5 each | all | 2 | 0 | DISTINCT. Each speaks to its own trouble (see below). |

**WEAK lines resolved (4)**
1. **Grata, "Then it's the wind that puts them in…".** Her retort opened on the house "Then". It is now "It's the wind does it, and I'll charge the wind." This is the Oscan-flavored relative drop, and it tells rather than concludes.
2. **Valens, "Then it's yesterday's bread."** It shared the house opener and read as an inference. It is now "That's yesterday's bread.", a flat statement, which is his syntax.
3. **The stewpot woman, "Then I'd only break it in the same spot looking."** The opener was the house's. "Looking" was ambiguous. It is now "I'd only break it in the same spot, looking for it."
4. **The leek husband, "Then he should have chained it…".** It is now "He should have chained it to the wall.", so the wife's "He should have chained you." lands as a turned line.

## Changes Made

### Narrated speech turned into spoken lines (14)
1. **Mara asks Grata for paint:** "Where does one buy paint, in this quarter?" (was "I asked Grata where…").
2. **Felix's market-day cry:** "Cracked your pot? Dropped your lamp? Bring it to the dead cobbler's, next door to Grata's, and she'll have it whole for you by next market! Nobody on this road mends like her!" The cry ends on a boast.
3. **Grata stopping him:** this was "said he was driving off her custom". It is now a flood that tells and then commands: "…there goes the third man with my cup in his fist and not a copper paid for it. Shout at the fullers."
4. **Mara reading the board to Felix:** "There is no fish, and you are not in it," which answers two of his four questions.
5. **The cook's overcharge:** this was "charged the cook somewhat over his first price". Now the cook stops at her plank: "A handle you could lift a mule by, and he's charged me more than he first asked, like I was the one took the pot. Never again. Next time it walks, it can stay walked." This closes the pot thread in his own grievance.
6. **The quarryman's dare:** "Show us," (the hand-over had been mute).
7. **The board read back to Grata:** "Four, and it's Falernian," … "Which of these is that, then?" Grata answers "The one you'll pay four for. The price tells you which." She sells, and she does not ask.
8. **The fuller's wife at the fountain:** "Twice he's had it from the shelf to look at, and back it goes. Yesterday he brought me home a comb, and couldn't say what for." The narration "Grata was in the line." stands alone after it.
9. **Felix's dare over the hare bowl:** "Break that, anybody, and see what you get." This was "dared anybody in the house to break it".
10. **The rain customer:** "I'll wait till it eases," … "and at dusk he was still in the opening." This was "stood about … to be out of the rain".
11. **Mara reading the panel to Felix:** "His bread comes last," … "It says it is good." This was "reading it out … piece by piece". Felix replies, ending on the fact: "All that red, and a ladder, and three of them out of their beds, and me holding it for them half the night. For bread."
12. **Felix at the pier:** "No candidates on this pier. It's people wrote all this." This was "was not, he said, for candidates".
13. **The red-jar woman:** "Fill and get on," … "and leave the talk to them that's got dowries." This was "told her to fill and get on…".
14. **Grata's chatter during the fish week:** this was "talked … about the fuller's blue scent bottle, which she had known of from the hour it broke". It is now spoken: "Blue glass, his mother's, and he's looking at that shelf yet and can't think why, and she reckons I had it from her at the fountain. I had it the hour it broke. The street heard it go, every door of it."
    - This is displacement: she is telling the counter that she knows things before she is told, while she watches Mara avoid the jar.
    - It is not a question, and it does not point at the reveal.

### Short in-scene replies added (9)
- **The stewpot woman's "dogs" exchange.** This is the comprehension beat; see Mara below.
- **The turner, first visit.** Mara answers him: "I can make it hold coins," … "Whether it fills is your affair." His "Twice," he repeated now repeats against something she said.
- **The turner's second visit:** "Full again in under a month," … "Don't tell my wife it was full."
- **The girl with the rattle:** "He's better,".
- **The fuller's wife at pickup:** "There's his mother's bottle," … "that nobody ever threw at anybody." She sees no break.
- **Zosimus's name.** Mara asks "What name goes on the tag?" Taking the job is her only answer to the request; she says nothing to it.
- **Grata's answer to the carter** and **Felix's bread line** (both listed above).

### Voice adjustments
- **Mara and the comprehension rule.** The rule is unchanged: plain, uncontracted Latin, at most 2 comprehension reports, never an understood-every-word claim. Ch.19's mechanism, losing fast speech, is spent. Ch.20 uses a **different mechanism: a trade word she lacks**, asked for and then shown by hand:
  - The woman says "She had a tinker put his dogs in it the winter I was born."
  - Mara asks "Which are the dogs?" The narration adds "The word belonged to tinkers."
  - The woman "set a fingernail on each clamp in turn. 'These. Lead. They've not shifted since.'"
  - Speed is not mentioned. The word stays in English register ("dogs" is the old joiner's word for a cramp), so the gap reads without a gloss, a Latin word or a book-against-street contrast. That contrast was considered and cut because it is SPENT (Ch.4, Ch.7).
  - Comprehension reports on the page: **1**.
- **Valens:** one line recast ("That's yesterday's bread."). Everything else is as drafted. Every rule in the brief holds:
  - bare "No." 0;
  - narrated non-answers 0;
  - comparisons 0;
  - orders to Felix 0.
- **Felix:** cry, dare, pier and bread lines added. Every one of them ends on a boast or a fact, so his question endings (the Ch.19 WATCH) are now a minority.
- **Grata:** the custom complaint, the price answer and the bottle chatter added. She asks nothing, and every flood ends on a telling or a command. The reveal speech is untouched, with no questions and no teeth.
- **Zosimus:** one line, and his chaos stays Hermes. No line of his recurs and none states the theme.
- **Walk-ons:** each new line speaks to the walk-on's own trouble:
  - the cook's grudge;
  - the carter's suspicion of "Falernian";
  - the turner hiding money from his wife;
  - the fuller's wife's comb;
  - the rain customer staying put;
  - the quarryman's "Show us,".

### Tag/Beat Replacements
- **3 compliance beats recast** (listed above).
- **2 tags removed:** Felix's pier line (the speaker is the paragraph's subject), and Felix's hare-bowl line, which now has the beat "He kept it pressed to his ribs."
- **2 redundant narration tails trimmed** where the speech now carries them: "and give them advice"; "with the news".
- **New beats:**
  - "She set a fingernail on each clamp in turn."
  - "stood in the opening holding it to the daylight, looking for the break and not finding it"
  - "He kept it pressed to his ribs."
- Gesture classes are clean at the gate.

### Natural Speech Additions
- 0 interruptions (em-dash budget kept at 0).
- 1 question asked for a word (the dogs).
- 2 displacements: Grata on the bottle; the fuller's wife's comb.
- 1 non-answer by action: the tag question in place of a reply to "Leave me the crack".

## Mechanical
- **`tic_report.py --echoes 20`:** **0** echoes, **0** command echoes, **0** spoken-line echoes. No whole short line is borrowed from an earlier chapter.
  - The first pass of new lines threw 12 cross-chapter echoes, 11 book-wide 3x phrases and 6 Mara self-repeats. All were varied before the final run.
  - Among them: "down the hill", "a man who had", "said a man", "the fuller's wife" (×3 in the chapter), "baths at the crossing" (×3), "over his shoulder", "the whole street", "up against the", "lifted it off", "under his arm", "was new to me", "what name shall I".
  - New short lines were checked by hand against Ch.1–19: "Show us", "He's better", "That wants shouting", "That's wrong", "What's she for", "Which are the dogs?", "Shout at the fullers", "Fill and get on". None occurs earlier.
- **`bash tools/check_chapter.sh 20`: all clean.**
  - style: clean (simile 1.7/1k, em-dash 0);
  - grammar: 0 errors;
  - rhythm: 0 flagged;
  - show/tell: no flags;
  - voice-wear (strict): clean;
  - tic gate: clean, including gestures;
  - echo scan: 0;
  - metaphor: no flags (fig 2.3/1k, >40w 4.2%);
  - shape: SHAPE CLEAN.
- **Reflexes (unchanged or lower):** and-chains 2 (cap 9); credential asides 1; negation pivots 0; hinge / So openers 0; "Then" speech openers 1; "And" rejoinders 3.

## Remaining Concerns
- **Dialogue is 33.3% by show_tell and 34% by shape_check.** That is inside the 33–36 target but near its floor. Downstream cuts (hook-craft, the disruptor) should not take spoken lines without replacing them. The narrated speech still left is better as summary:
  - the leek woman reading the notice aloud (it would duplicate the italics);
  - "I read it to him" (now opened by a line);
  - Grata's son reading her the panel (his voice is Ch.31's);
  - the letter's carter (the narrated fact carries Ch.21's knowledge path).
- **Character-bible sync (for finalize; not done in this pass).** The Ch.20 blocks quote strings that are no longer on the page:
  - **At-risk after Ch.20, "Spoken shapes spent":** "Then they'll want it shouted." is now "That wants shouting.".
  - **Ch.20 walk-on block:** "Then he should have chained it to the wall." is now "He should have chained it to the wall."; "Then I'd only break it in the same spot looking." is now "I'd only break it in the same spot, looking for it."; the painter's "And you, lantern" is now "You, lantern"; the fountain line's "And the dowry in figs." is now "With the dowry in figs.". Grata's "I'll charge the wind." survives.
  - **ZOSIMUS card:** the narrated name-giving is now the spoken "Zosimus. Of the crossing baths. Down at the furnace, not up with the bathers.", after Mara's "What name goes on the tag?".
  - **At-risk "The lamp" entry:** "the welt left 'a thread's thickness proud of the clay'" now reads "I trimmed it to a thread's thickness proud of the clay". The quoted phrase survives.
  - **New spent shapes to log:**
    - **Mara:** "There is no fish, and you are not in it,"; "Where does one buy paint, in this quarter?"; "Which are the dogs?"; "I can make it hold coins," / "Whether it fills is your affair."; "His bread comes last," / "It says it is good."; "What name goes on the tag?".
    - **Felix:** the market cry ("Nobody on this road mends like her!"); "Break that, anybody, and see what you get."; "For bread."; "No candidates on this pier. It's people wrote all this.".
    - **Grata:** "Shout at the fullers."; "The price tells you which."; "The street heard it go, every door of it.".
    - **Walk-ons:** "Next time it walks, it can stay walked."; "Show us,"; "He's better,"; "that nobody ever threw at anybody."; the comb; "Don't tell my wife it was full."; "I'll wait till it eases,".
  - **New mechanism to log:** the comprehension mechanism (a trade word asked for and shown by hand) is now SPENT. The next chapter that needs a comprehension beat finds a third way.
  - **WATCH, new:** "Then…" as the house speech opener. The draft had 10 across seven speakers, and the gate does not see it. Proposed: a `tic_report.py` count of `^"Then\b` per chapter, capped at 2 (pipeline item for the root).
- **"I gave him no answer."** (Mara to the tile carter) is the chapter's one narrated non-answer. It is Mara's, not Valens's, and it carries the all-or-nothing beat, so it stays (cap ≤1 per chapter).

## Cover-the-Name Test: FINAL
- **The notice and the leek couple; Grata's paint flood; the board; Felix and Valens at the board:** **PASS.** The couple's turned line now mirrors. Mara's "There is no fish" cannot be Felix (no questions stacked) or Grata (no telling).
- **The market cry and Grata's complaint:** **PASS.** Felix asks and then boasts; Grata tells and then commands.
- **The stewpot woman and the dogs:** **PASS.** Mara asks one plain question; the woman answers with her nail and three clipped words.
- **The cook, the coppersmith, the cook's grievance:** **PASS.**
- **The bowl:**
  - **Felix at the stair, the night mend:** **PASS.** Valens's foreman story is short, level and in order.
  - **The tile carter, the rattle girl, Felix's news, "We'll manage with the cookpot,":** **PASS.**
- **The forum:** **PASS** ("That's yesterday's bread." / "Grata would."; "Show us,"; Felix's "rotten in the middle").
- **The roof frame, the figs, Grata at the parapet, the letter, the gate:** **PASS** (unchanged apart from the two openers).
- **The turner and the toothpick; the vow; the wine board and its carter:** **PASS.**
- **The fuller's wife (drop-off, pickup, fountain); the hare bowl; the turner's second box; the rain:** **PASS.**
- **The night painters; Infantio; "It's red"; Grata on Polybius; the pier:** **PASS.**
- **The fountain line and the pebble; Grata's cup; "That's a good stone,":** **PASS** (the pebble beat unchanged).
- **The jug graffito; Zosimus (drop-off, name, pickup); Valens at the lamp; the late figs:** **PASS.**
- **The fish week and the reveal:** **PASS.** Grata's two speeches tell and never ask. The closing speech is unchanged.
