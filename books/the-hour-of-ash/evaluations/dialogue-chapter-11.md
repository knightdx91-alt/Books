# Dialogue Polish Report — Chapter 11 "Valens's Yard" (run 2)

Scope: dialogue only, plus the tags and beats attached to it. Three things are byte-identical to the writer's draft (verified by diff against a saved copy):
- the first sentence (the 80-word `long-spiral`);
- the near-kiss block, from "His fist closed on the end of the strap." through "I went out after him.";
- the final practical line ("We take the string to Kirrha for oil the day after tomorrow, at daybreak," … "behind a goat.").

The 3 breaks, the anchor paragraph and the ledger signatures (`long-spiral` → `dialogue`) are unchanged. The header comment now carries the post-polish counts.

## Audit Summary
- **Dialogue ratio (shape_check, the ledger metric):**
  - Before: 35.5% of 6,288 words.
  - **After: 35.7% of 6,308 words.** The band is 35–45%, so the chapter stays above the floor.
  - Words inside quotation marks went from 2,239 to about 2,258.
  - The show/tell gate's own measure (its word count includes the header comments) went from 34.7% to 34.8%.
- **Em-dashes:** 2 → 2 (Felix's cut-off report; "In my country—"). **Simile:** 1.3/1k → 1.3/1k. Median sentence 13 → 14 (gear mid).
- **Conversations analyzed:** 11.
  1. Praxias's price.
  2. The refusal at the trough.
  3. Felix at noon.
  4. The load test.
  5. The figs.
  6. The bells.
  7. The boxing.
  8. The lame black.
  9. Kallia at the pot.
  10. Praxias at the gate and the mind-reading.
  11. The walk up, the sherd and Felix's name, the paper, and the agreement.
- **Lines flagged INDISTINCT:** 2, both resolved.
  - Mara's "He looks at everything. He was pricing it." was a level, unqualified pair of declaratives in Valens's syntax.
  - Mara's "Is it cut on the wall?" / "Did he take you to the god?" was a stacked double question in Felix's shape.
- **Lines flagged WEAK:** 7, all resolved. Details under Changes.
- **FLAT_DIALOGUE / subtext spoken:** 2, both resolved.
  - "At the end of summer I shall not be here" said the outline's subtext out loud.
  - "Felix can't either. It saves arguing." explained the reading reveal instead of playing it.
- **Exposition dumps:** 1, recast. The walk up was a run of convenient questions ("And when they have come?" / "And the crowd?" / "Have you ever…" ×2), and each question is now Mara's own. Valens's fig-drying speech (4 sentences) is accepted: it is his chaos trait surfacing for the first time, not information for the reader.
- **Tag overuse:** none. "said" stays the invisible default. I added no tags and one beat ("the boy ran her up and back once more", which replaces the near command echo "said, 'Again,' and watched her again").
- **"And…" dialogue openers:** 7 → **2**: Mara's "And if somebody takes him?" and Valens's "And you?", which is the line where he asks her name. The cap is ≤4.
- **"Then…" openers in speech:** 2 ("Then sell me back the watch," / "Then I'm right."), within the cap of 2.
- **Banned stage business, checked by hand and by gate:**
  - None in the chapter: nods, shrugs, sighs, swallows, "a long moment", bends, kneels, crouches.
  - Command echo: 0 candidates.
  - The book-wide gesture classes are unchanged from the draft (bend 15, kneel/crouch 12, object handling 9). One of my Felix lines briefly tripped the object-handling regex ("took the eye out of the"), and it is recast ("blinded the Amphissan's bird in one eye").
- **Gates (run from /home/user/Books):**
  - `bash books/the-hour-of-ash/tools/check_chapter.sh 11`: style, grammar, rhythm, show/tell, voice-wear (strict), tic gate, metaphor and shape are all clean.
  - `python3 books/the-hour-of-ash/tools/tic_report.py --echoes 11`: **0 echoes**, with no command-echo candidates.
  - My first pass created 3 echoes ("up to the god", "the god I said", "a second time") and 2 in-chapter recurrences ("the quay at Kirrha" ×3, "three and a half" ×3). I varied all five before finishing.

## Felix's question openers (the catchphrase that was forming)
Counted by script over every Felix speech, using each question's first two words.

| Frame | Before | After |
|---|---|---|
| "Is it…?" | 7 | 1 ("Is it you?" at the barred gate) |
| "Is…" (any) | 10 | 1 |
| "Can I…?" | 4 | 2 |
| "Can you…?" | 3 | 1 |
| "Have you…?" | 4 | 1 ("Have you ever seen a man killed with one blow?") |
| "Did…" (any) | 8 | 3 (Did you / Did he / Did it: one each) |
| "Do you (know)…?" | 3 | 1 |
| "Is that…?" | 3 | 0 |
| "Shall I…?" | 2 | 0 |
| **Highest two-word frame** | **7** | **2** |

**How he keeps his speed without the frame:**
- Questions open on varied words: Are / Which / Was / Where'd / Had / Who's / What's / Would / Will / Has.
- Bare fragments: "Which hand?", "All of it?", "A curse?", "Big?", "The left, I heard."
- Statement-questions: "You're the one he took up to Pan's in the snow.", "That's the bad in her, coming out?"
- Tags: "Yours, is it?", "won't she?", "did you know that?"

**His card's other axis, superlative boasts:** these were missing from the draft. Four are now on the page, each in a different shape so that none becomes a formula:
- the fowler's hawk held bare-armed "and it never put a claw in me";
- "I'd go a round with the Thessalian myself, if they'd let me in the ring" (his arena-madness, seeded);
- "nobody holds an ear better than me";
- "I can see clear to the bend from up here, and past it if I stand."

"He paid more for me than he paid for the black" was already a boast.

**The dramatic irony now lands:** Felix's boxing speech ends on "Have you ever seen a man killed with one blow?", and Valens answers "No." The ex-murmillo's lie sits right against the question.

## Voice Distinctiveness Results
| Character | Speeches (approx.) | Distinct | Weak | Indistinct | Post-Polish |
|---|---|---|---|---|---|
| Valens | 68 | 63 | 4→0 | 1→0 | **PASS** |
| Mara (Greek) | 66 | 61 | 3→0 | 2→0 | **PASS** |
| Felix | 24 | 22 | 2→0 (frame repetition) | 0 | **PASS** |
| Praxias | 9 | 9 | 0 | 0 | **PASS** |
| Kallia | 4 | 4 | 0 | 0 | **PASS** |

**Cover-the-name: Felix vs Valens vs Mara.**
- **Felix** is contracted and fast. He stacks 3–5 short units, asks about fame, fights and birds, boasts, and never waits.
- **Valens** is contracted but level. He speaks in ones and twos, with no comparisons. His questions are practical (who, where), plus one deflection.
- **Mara** is uncontracted, qualifying and dry ("Perhaps his olives are uphill.", "You have been in yourself, surely."). Where a question carries weight she asks one at a time.

The draft's overlaps are gone:
- "Have you ever…" was in both Felix's and Mara's mouths (3 uses). It is now Felix's alone, once.
- "Is it…?" had appeared in Mara's "Is it still going?" and "Is it cut on the wall?".
- "Why not?" had been both Felix's and Mara's. It is now Mara's alone.

**Praxias and Kallia are on their cards, untouched.**
- Praxias names his price first and then bargains down against himself ("little cousin" 2, "for family" 2, both at cap).
- Kallia's labor axis comes as a question back ("Whose water washes it?"). She has 0 chore-replies, never sits, and never touches Mara.

## Changes Made

### Subtext (the romance foundation)
1. **The figs.**
   - **Surface:** drying methods.
   - **Real topic:** whether she stays to see a harvest.
   - **Change:** I cut "Come then." It read as a request that she stay, which is on his evasion list. He now proposes the midwinter contest as if her being there were a given ("You dry them your way, and I'll dry mine…"). I replaced "At the end of summer I shall not be here" with **"Somebody else would have to open mine,"** so the leaving is never said. "Then I'm right." now claims the win by forfeit.
   - **Technique:** displacement (her jar stands for her).
2. **The reading reveal now plays in action.**
   - **Change:** I cut "Felix says you cannot read." / "Felix can't either. It saves arguing." The reveal is now: the edit to her sherd; "It was on the bench."; "I did hear it." (deadpan evasion); his lie to Felix in front of her; and Felix's taunt, which shows what Felix believes ("Go on, then. Say me out loud." … "He can't. Nobody in this yard can but you."). Mara's silence keeps the secret.
   - **Technique:** contradiction (the lie, with the reader as witness).
3. **The bells.**
   - **Change:** "Those want doing." was his spent move of answering closeness with a practical order (spent until Ch.12), so it is cut. He now leaves in silence, with the bells in her lap. Before that, "In the day." became a practical *who* question: **"Who keeps the door, while they sleep?"** It is his exits-and-who-saw worldview. He asks about her world, and then refuses the answer the moment it becomes "In my country—".
   - **Technique:** silence.
4. **The mind-reading.**
   - **Change:** Mara's "He looks at everything. He was pricing it." became **"You had your back to him the whole time he was in the gate."** It is a cost line: she catches him reading a man he never looked at, and he answers past it ("He turned uphill. Not to his own door."). "He was going to his olives." became "Perhaps his olives are uphill." (Mara qualifying).
5. **The walk up.**
   - **Change:** "And the crowd?" became **"Where would you stand, in all that?"** Valens answers a different question, with the crowd and the men "watching the line". That is deflection, and it shows he is already weighing the day. Mara's "Have you ever…" pair became "You have been in yourself, surely." and "Not even a question, sent in by somebody else?". "And if he has nothing for me?" became "Suppose he has nothing for me."
6. **The agreement.**
   - **Change:** "And the priest who writes down the name…?" became **"The priest will write your name down. You told me so yourself."** The risk is now his, named by her and not by him, so he still never names himself as the traceable one. "He let that go by him." then carries it. "Who goes in?" became "At the door. Inside, though?". "Praxias wants four drachmas" became "I cannot meet Praxias's price." His last offer was three and a half, so "four" was a slip.

### Voice adjustments
- **Mara:**
  - "Is it still going?" became "Have you let it stop?", which his "It hasn't stopped." now answers two lines later.
  - "Is it cut on the wall? … Did he take you to the god?" became "Did he take you to the priests," I said, "and have it cut on the wall?" (one qualified question).
  - "And how does a goat get from Kirrha to Delphi?" became "How does a goat get from Kirrha up to Delphi?".
  - Greek uncontracted throughout; no English, aloud or alone.
- **Felix:** every speech re-cut for opener variety (table above). Two logic fixes ride along:
  - The string is away at Kirrha during the boxing ask, so "I'll have the stalls done before noon" / "I'll be here before the string is". The stalls pay off when he forks them in a temper.
  - "Did you know?" became "and I never heard a thing" (his hurt pride that he slept through Valens's night).
- **Valens:**
  - No simile or comparison in speech.
  - No footing order.
  - No come-and-ask line.
  - No self-naming as the traceable one.
  - No practical order in answer to closeness: the one that was there, "Those want doing.", is cut.
  - "How long…?" 0; "What for?" 0.
- **Lame black:** "said, 'Again,' and watched her again" became "said, 'Again,' and the boy ran her up and back once more" (the near command echo is gone).

### Tag/Beat replacements
- 0 tags replaced, 0 tags removed, 1 beat recast (above).
- "He crossed to the stable through the last of the rain." now ends the bells paragraph, because the line before it was cut.

### Natural speech
- Interruptions and cut-offs are unchanged: Felix's report "and the baker said—" and "In my country—".
- Deflections: 3 added (the crowd answer; "Who keeps the door…?" leading straight to the refusal; his reply past "You had your back to him").
- Non-sequiturs: 1 added. "He can't." answers Valens's lie but is spoken to Mara.

## Bible quotes my edits invalidate (character-bible.md NOT edited; for the next bible sync)
**MARA, Ch.11 block (≈l.189–211):**
- "At the end of summer I shall not be here," is gone. It is now "Somebody else would have to open mine,".
- "Felix says you cannot read." is gone.
- New Mara lines to add if the sync wants them:
  - "Have you let it stop?"
  - "You had your back to him the whole time he was in the gate."
  - "Perhaps his olives are uphill."
  - "Where would you stand, in all that?"
  - "You have been in yourself, surely."
  - "The priest will write your name down. You told me so yourself."
  - "I cannot meet Praxias's price."

**VALENS, Ch.11 block (≈l.389–451):**
- "Come then. Dry them your way, and I'll dry mine, and we'll open the two jars at midwinter and see." became "You dry them your way, and I'll dry mine, and we'll open the two jars at midwinter and see."
- "to 'At the end of summer I shall not be here': 'Then I'm right.'" now answers "Somebody else would have to open mine".
- "Felix can't either. It saves arguing." is cut.
- "In the day." is cut. It is replaced by "Who keeps the door, while they sleep?"
- "When she begins 'In my country—' he is on his feet with the bells in her lap: 'Those want doing.'" no longer holds: "Those want doing." is cut, and the refusal is now silence plus leaving.
- "Spent in Ch.11 … 'It saves arguing.'" is no longer on the page.

**FELIX, Ch.11 block (≈l.775–813):** nearly every quoted question burst has changed. Stale:
- "Is it you he took up to Pan's… Which hand was it? Did it bleed much?"
- "Does it want feeding? Why can't I hold it?"
- "Was it your father? Did he have mules? Is it true in Syracuse they eat octopus? Raw?"
- "Can I go? If the string's back by noon can I go?"
- "Why not? What's it cost you? … Have you seen a Thessalian box?"
- "Shall I hold her ear for you? Shall I get the rope on her hind leg?"
- "Is that the bad in her? … Is it all out? Will she go to Kirrha tomorrow?"
- "The one that took out the eye of the Amphissan's bird? Was it the left eye?"
- "Why would he go to the square?" … "Is it true the baker's bird was fed on wine? Can you make a bird brave with wine?"
- "The Amphissan? About his bird? Why's it barred in the day, when we've never barred it in the day?"
- "Can I come down? Is it still nobody you want?"
- "Is that writing? Is it a curse? … Can you write me big?"
- "Go on. What do I say?"
- "Which bit's the start? That one, with the arms on its hips? Is that the F? Will it stay on, if it rains?"
- "Did he hit the Cilician?"
- "Have you seen how he looks at people? Have you?"
- "Do you know what it is in Latin? It's lucky. Do you know he talks to the mules in Latin? Did you know that?"
- "Can I show the dog?"
- "Did you know?" (the poultice morning)
- Mara's "Is it cut on the wall? … Did he take you to the god?"

Two other parts of the block need updating:
- The **Knows** line cites Mara's "Felix says you cannot read." as the source of Felix's belief. The page now shows it through Felix himself: "He can't. Nobody in this yard can but you."
- The **WATCH for Ch.12+** opener counts ("Is it…?" ~9, "Can I…?" 4, "Did…?" 4, "Is that…?" 3, "Is it true…?" 2, "Do you know…?" 2) are stale. Replace them with the after-column above. Also note his four boasts, each a different shape, so no boast formula is in use.

**AT-RISK after Ch.11 (≈l.2560–2607):**
- "Valens reads: the reveal is DONE ('Take out the door,' / 'It was on the bench.' / 'Felix can't either. It saves arguing.')": replace the third quote with "I did hear it." and the lie to Felix.
- "Once each, SPENT: … 'It saves arguing.'" is gone.
- Add as spent:
  - "You had your back to him";
  - "Who keeps the door, while they sleep?";
  - "Somebody else would have to open mine";
  - Felix's hawk, ring and ear boasts.
- The counts line "Dialogue 35.5%; 6,288 words … median sentence 13" is now 35.7%, 6,308 words, median 14.

**Ch.11 walk-on note (≈l.1486):** two mention-only figures are new in Felix's boasts, a fowler with a hawk "down at the harbor" and "a sailor" (octopus gossip). No card is needed.

## Remaining Concerns
- **Dialogue sits only 0.7 points above the floor.** Any later pass (hook-craft, disruptor, editor) that cuts dialogue must re-measure with shape_check. Two lines would be cheap to cut and must not be, because each carries subtext: Mara's "Somebody else would have to open mine," and Felix's taunt "He can't."
- **"Who…?" is Mara's most-used question opener** (Who read it out / Who sewed it last / Who is to say / Who took yours / Who told you). Each is motivated and they are spread across scenes. Still, the next chapter should give her other forms.
- **"Is that the last of it?"** (Valens, the breastband) is the chapter's only "Is that…?" now. I kept it because "That's the heap gone, then." is the scene's second subtext line (no more reason for her to come).

## Cover-the-Name Test: FINAL
| Conversation | Result | Note |
|---|---|---|
| Praxias's price | PASS | price first, then bargains against himself; Mara uncontracted |
| Refusal at the trough | PASS | crowd-reading; the board probe; the watch read and "It hasn't stopped." |
| Felix at noon | PASS | a boast replaces two stacked "Does/Why" questions |
| Load test | PASS | |
| Figs | PASS | the subtext is never spoken |
| Bells | PASS | a practical *who* question, then silence; no order |
| Boxing | PASS | the irony lands on "No." |
| Lame black | PASS | Felix's ear boast; no command echo |
| Kallia at the pot | PASS | |
| Praxias at the gate / mind-reading | PASS | Mara's cost line ("You had your back to him") |
| Walk up | PASS | deflection, not Q&A exposition |
| Sherd and Felix's name | PASS | the reveal plays in action; Felix shows his own belief |
| Paper / near-kiss / agreement | PASS | "And you?" kept as his name-ask; final line untouched |
