# Muse close reading, Ch.1–9: triage against the text (2026-10-21)

Source: `feedback/muse-close-reading-2026-10-21.txt` (Meta Muse, sentence-by-sentence close reading). This triage covers
**every flag for Chapters 1–9** (IDs 1.xxx–9.xxx) and the **priority-list items 1, 7 and 8** (Bal's age in Ch.1;
"Norheart" at 6.195; the 5.157–5.158 pronoun). Muse numbers its own sentences, so I found each flag by its quoted excerpt
in `manuscript/chapter-NN.md`. I checked every author line against `Sygl_Complete.txt` (src l.1–362 covers Ch.1–9) and
every flag against the STATE.yaml rulings and the earlier triage (`evaluations/muse-triage-2026-10-21.md`, B1–B12).

**No chapter or STATE file was edited, and nothing was committed.** The B fixes were applied only to a scratch copy,
where all four gates pass (see the end of this file).

Buckets: **A** the text already handles it, or Muse misreads · **B** fix without changing the story (with an optional-cuts
sub-list) · **C** author's call · **D** conflicts with a ruling. "Pending" means the flag repeats a fix already waiting
in the earlier triage, so it is not repeated here.

## Counts

255 flags (Ch.1 28 · Ch.2 31 · Ch.3 30 · Ch.4 29 · Ch.5 21 · Ch.6 22 · Ch.7 33 · Ch.8 28 · Ch.9 33).

| Bucket | Flags | Edits |
|---|---|---|
| **B** (apply-ready) | **62** | 60 edits (4.042+4.046 and 5.157+5.158 each share one edit) |
| B, optional cuts | 19 | 19 edits |
| Already pending (earlier triage B1, B2, B3) | 5 | none new |
| **C** author's call | **5** | 1 new, plus 4 that repeat earlier C items |
| **D** conflicts with a ruling | **2** | none |
| **A** fine / Muse wrong | **162** | none |

By category:

| Category | B | B-opt | pending | C | D | A | Total |
|---|---|---|---|---|---|---|---|
| CLARITY | 25 | 0 | 3 | 2 | 0 | 32 | 62 |
| TELLING | 4 | 5 | 0 | 1 | 0 | 27 | 37 |
| REPETITION | 4 | 9 | 0 | 0 | 0 | 20 | 33 |
| RHYTHM | 5 | 2 | 0 | 0 | 0 | 23 | 30 |
| IMAGE | 8 | 2 | 0 | 0 | 0 | 19 | 29 |
| LOGIC | 5 | 0 | 0 | 2 | 0 | 17 | 24 |
| DIALOGUE | 1 | 0 | 0 | 0 | 2 | 14 | 17 |
| POV | 4 | 1 | 0 | 0 | 0 | 7 | 12 |
| CONTINUITY | 1 | 0 | 2 | 0 | 0 | 3 | 6 |
| GRAMMAR | 5 | 0 | 0 | 0 | 0 | 0 | 5 |
| **Total** | **62** | **19** | **5** | **5** | **2** | **162** | **255** |

Why A is so large: most flagged TELLING, RHYTHM and DIALOGUE sentences are the author's own script lines, carried
across nearly word for word ("At her words, Balthazaar heard the truth", "Hoping to forestall a lot of questions…",
"It was information Bal would never have gotten…", "hate and stuff", "But who knows", "a leg up", "This would be all over
the castle by dinner"). The ruling makes the author's lines the base, so I left them alone unless a line had a real
grammar or logic slip (5.157, 4.105, 5.130). Several flags also misread the text (see A).

### Priority-list items 1, 7, 8

| Item | Verdict |
|---|---|
| **1. Bal's age in Ch.1** (also flags 2.007, 3.013) | **Already pending (B1).** Ch.1:19 becomes "Balthazaar Norheart, or Bal to his friends, was eighteen and could not remember ever having a left hand." |
| **7. Norheart at 6.195 / 13.470** | **6.195: already pending (B1).** B1 puts his surname in Ch.1, so when Amelia says it at the claiming, he hears his own name, not a reveal. A reaction beat would be invented. **13.470** (outside my range): Soren's "plainly she knew it" already works, because the name was spoken at a public claiming and Porter uses it in class (Ch.9:93). |
| **8. 5.157–5.158 pronoun** | **B, CB36.** The author's request is kept and its grammar fixed: "I need it to reach my full strength. Without it, I'm worried I won't be able to stop the others if they try something tomorrow." |

## Word count

- **B list: net −82 words** (inside the −120 to +60 band). Scratch copy with B applied: **90,000** words (baseline 90,082).
  With the earlier pending fixes (+25), the book is about **90,025**, above the 90,000 floor.
- Optional cuts: a further **−174** if all are taken (scratch total 89,815, below the floor). Take them only if
  other triage ranges add words. Each one is independent.
- I moved four lower-value cuts from B to the optional list (O16–O19) to keep the floor safe. The B list started at −115.

## B: apply-ready fixes

Each "exact current text" occurs exactly once in its chapter file (checked by script). The fixes are in chapter order.
Δw is the word change.

| Fix | Flag | Ch | Exact current text | Replacement | Δw |
|---|---|---|---|---|---|
| CB1 | 1.013 | 01 | `for a building that age, three stories of weathered brick` | `for a building that age. It was three stories of weathered brick` | +2 |
| CB2 | 1.063 | 01 | `though he'd watched it until his eyes watered, but he knew what he'd seen.` | `though he'd watched it until his eyes watered. But he knew what he'd seen.` | +0 |
| CB3 | 1.076 | 01 | `the part about how hard it was to stop.` | `the part about how hard it was to steer.` | +0 |
| CB4 | 1.099 | 01 | `No school would take you without one, no matter how much magic you could push through a stump.` | `No school would take him without one, no matter how much magic he could push through a stump.` | +0 |
| CB5 | 1.119 | 01 | `staring at the ceiling, his heart thudding in his ears.` | `staring at the ceiling, the end of his stump still tingling.` | +1 |
| CB6 | 1.139 | 01 | `down into the wool, and as he finished saying the words, the gold and sky blue carpet` | `down into the wool, and the gold and sky blue carpet` | -6 |
| CB7 | 1.157 | 01 | `and the daylight changed color around him,` | `and the daylight turned amber around him,` | +0 |
| CB8 | 1.167 | 01 | `only a dry smell of something spiced.` | `only a dry smell of cloves and old resin.` | +2 |
| CB9 | 2.064 | 02 | ` A thin film of dust lay on them.` | *(delete)* | -8 |
| CB11 | 2.092 | 02 | `a little crease between those perfect eyebrows.` | `a little crease between her brows.` | -1 |
| CB12 | 2.102 | 02 | `His voice came out embarrassingly high.` | `His voice came out high.` | -1 |
| CB13 | 2.232 | 02 | `that the knuckles showed.` | `that the knuckles were white.` | +1 |
| CB14 | 2.244 | 02 | `worn flat, like directions to the bathroom.` | `worn flat, like a grace said before supper.` | +1 |
| CB15 | 2.268 | 02 | `and the spell of the moment broke.` | `and the moment broke.` | -3 |
| CB16 | 2.271 | 02 | `beneath the hem of her dress like a girl let out of lessons early.` | `beneath the hem of her dress.` | -8 |
| CB17 | 3.021 | 03 | `When Bal next checked, the cut had closed over,` | `The cut had already closed over,` | -3 |
| CB18 | 3.030 | 03 | `and then all at once began to drain away,` | `and then drained away all at once,` | -2 |
| CB19 | 3.043 | 03 | `as he'd watched the others do with their own hands a thousand times without ever thinking about it.` | `the way the others did with their own hands a thousand times a day, never thinking about it.` | +0 |
| CB20 | 3.109 | 03 | `They sat like that for a few minutes,` | `They stayed like that for a few minutes,` | +0 |
| CB21 | 3.142 | 03 | `and the carving was finer than it had looked from across the wall:` | `and the carving was very fine:` | -7 |
| CB22 | 3.156 | 03 | `For once, she looked no older than Bal.` | `For once, she seemed no older than Bal.` | +0 |
| CB23 | 3.226 | 03 | `missing every time, and nobody minded, and the whole field` | `missing every time, and the whole field` | -3 |
| CB24 | 4.003 | 04 | `white tiles that always seemed to echo as you walked on them.` | `white tiles that always seemed to echo underfoot.` | -4 |
| CB25 | 4.046 (+4.042) | 04 | ` Otherwise the office was as spartan and bare as a waiting room.` | *(delete)* | -12 |
| CB26 | 4.054 | 04 | `Everyone's did, and all his life they had always found the same thing there.` | `Everyone's did. All his life they had found the same thing there.` | -2 |
| CB27 | 4.095 | 04 | `Once they call roll for any blood sygls, you'll stand.` | `Once they call for the blood sygls, you'll stand.` | -1 |
| CB28 | 4.105 | 04 | `haven't outlawed blood sygls from attending` | `haven't barred blood sygls from attending` | +0 |
| CB29 | 4.170 | 04 | `which in that office meant you were finished.` | `which in that office meant the talk was over.` | +1 |
| CB30 | 4.183 | 04 | `As the majority of his belongings were not things of sentimental value, it did not take Bal long to pack.` | `Most of his belongings meant nothing much to him, so it did not take Bal long to pack.` | -2 |
| CB31 | 4.205 | 04 | `had been a friend, and he didn't want to leave them behind.` | `was a friend, and he didn't want to leave them behind.` | -1 |
| CB32 | 5.014 | 05 | `as though it might have gone back to normal overnight,` | `as though it might have vanished overnight,` | -3 |
| CB34 | 5.039 | 05 | `was showing plainly under her bangs.` | `glowed plainly through her bangs.` | -1 |
| CB35 | 5.130 | 05 | `your sygl will appear on your clothes, so don't worry about it not being there before.` | `your sygl will appear on your clothes. Don't worry that it isn't there yet.` | -2 |
| CB36 | 5.157 + 5.158 (priority 8) | 05 | `and I need it to be at my full strength. I'm worried I won't be able to stop the others if they try something tomorrow without it.` | `and I need it to reach my full strength. Without it, I'm worried I won't be able to stop the others if they try something tomorrow.` | -1 |
| CB37 | 5.172 | 05 | `He hugged her back anyway, a beat late, and then she had already let him go and was sitting back on her own bedroll pulling at the string on her parcel and saying nothing about it.` | `He hugged her back anyway, a beat late. By then she had let him go and was sitting back on her own bedroll, pulling at the string on her parcel and saying nothing about the hug.` | +0 |
| CB38 | 6.013 | 06 | `Bal twisted to check his own back, which was still blank, exactly` | `Bal twisted to check his own back. What little showed of it was still blank, exactly` | +4 |
| CB39 | 6.019 | 06 | `It wasn't long until he caught` | `It wasn't long before he caught` | +0 |
| CB40 | 6.046 | 06 | `Verin gave him that grandfather's smile again.` | `Verin gave him that easy smile again.` | +0 |
| CB41 | 6.140 | 06 | `He and Amelia were the only two people left` | `Bal and Amelia were the only two people left` | +0 |
| CB42 | 6.179 | 06 | ` The same shock was on every one of their faces.` | *(delete)* | -10 |
| CB44 | 6.188 | 06 | `That made sense, Bal thought. A lot of sense.` | `That made sense, Bal thought.` | -4 |
| CB45 | 6.212 | 06 | `Every student in the school's first year was standing` | `Every first-year in the school was standing` | -2 |
| CB47 | 7.092 | 07 | `every bit as large as the bed called for.` | `as wide as the bed.` | -4 |
| CB48 | 7.119 | 07 | `It was smaller than the common room,` | `It was smaller than the room with the couch,` | +2 |
| CB49 | 7.134 | 07 | `Why walk your dinner across a hallway?` | `Why walk your dinner from one door to the next?` | +3 |
| CB50 | 7.173 | 07 | `So it had been her doing the crackling, after all,` | `So the crackling had been her hair, after all,` | -1 |
| CB51 | 7.249 | 07 | `It was instructions for ordering a meal.` | `It gave instructions for ordering a meal.` | +0 |
| CB52 | 7.358 | 07 | `as he passed and then turned to study his face, and kept on looking.` | `as he passed, then turned and kept studying his face.` | -4 |
| CB53 | 7.359 | 07 | `the whole length of the corridor, flat and unfriendly.` | `the whole length of the corridor with a flat, unfriendly stare.` | +2 |
| CB54 | 8.081 | 08 | `the heel of his palm, light as a feather, without breaking the skin.` | `the heel of his palm without breaking the skin.` | -4 |
| CB55 | 8.140 | 08 | `Even fewer than there are now.` | `Even fewer then than there are now.` | +1 |
| CB56 | 8.227 | 08 | `somewhere back on his own side of the world.` | `somewhere back on his home plane.` | -3 |
| CB57 | 9.008 | 09 | `He had it in his back pocket.` | `He'd picked it up on his way out.` | +1 |
| CB58 | 9.053 | 09 | `A few went around by the windows so` | `A few gave his corner a wide berth so` | +1 |
| CB59 | 9.096 | 09 | `a faint, slow pulse, like the warmth that stays in a stone after the sun has gone off it.` | `a faint, slow pulse, warm as a stone after the sun has gone off it.` | -4 |
| CB60 | 9.117 | 09 | `He paid no attention at all to what the teacher's face was doing.` | `He didn't check what the teacher's face was doing.` | -4 |
| CB61 | 9.184 | 09 | `stayed open, empty.` | `stayed open, wordless.` | +0 |
| CB62 | 9.213 (+9.270) | 09 | `the room was quiet enough to hear the clock.` | `the room went very quiet.` | -4 |
| CB63 | 9.231 | 09 | `for what they had done to her, and somewhere between that and the bell` | `for what they had done to her. Somewhere between that and the bell` | -1 |
| CB64 | 9.241 | 09 | `and with each other's.` | `and with each other's followers.` | +1 |


### Why each B fix is safe (one line each)

- **Ch.1.** CB1 splits the inventory sentence. CB2 fixes the "though…, but" double hinge. CB3: a lighter body is not hard
  to *stop* but is hard to *steer*, so the rejected option now has a real reason. CB4 puts the rule in Bal's frame instead
  of a generic "you". CB5 swaps a stock heart-in-ears for the stump he just worked through. CB6: he had already said the
  incantation two paragraphs earlier (src has it in one breath; the book split it). CB7 and CB8 name the light and the
  smell (sensory texture only, no plot).
- **Ch.2.** CB9: created benches can't carry dust, and the dust clashes with "didn't have a speck of dirt" four lines
  later. CB11: "perfect eyebrows" echoes "perfectly trimmed eyebrow" (Ch.2:21). CB12 cuts the adverb. CB13 completes the
  image. CB14 swaps a jarring simile for one of repetition. CB15 removes a figurative "spell" right after real magic.
  CB16 cuts the schoolgirl simile at the bond offer (the NA age-register point Muse raises; the feet swinging stays).
- **Ch.3.** CB17 makes the healing immediate. CB18 fixes "all at once began to". CB19 makes the other children clearly the
  ones not thinking about it. CB20: Amelia kneels and Bal sits, so they "stayed", not "sat". CB21: the kids worked those
  doors with crowbars, so "from across the wall" was the wrong vantage, and the comparison is dropped. CB22: "seemed" makes
  this her guard dropping, not her face changing. CB23: the cheering already shows nobody minded.
- **Ch.4.** CB24 removes the generic "you" from the narration. CB25 (also covers 4.042) cuts the third statement that the
  office is bare and keeps the author's "little in the way of personality". CB26 fixes "they had always found" (the eyes
  as finders, plus a doubled "all his life… always"). CB27 and CB28 are grammar polish on Mrs. Brown's lines with the
  meaning unchanged ("outlaw… from attending" becomes "barred… from attending"). CB29 removes the generic "you". CB30 turns
  committee prose into plain prose. CB31: "had been a friend" implied the friendship was over; the ruling says Fredrick
  *is* a friend.
- **Ch.5.** CB32 removes the "normal" value judgment. CB34: the brand can't be "showing plainly under her bangs"; it glows
  *through* them (Ch.3:65 "beneath her dark hair"; Ch.7:223 she lifts the bangs). CB35 untangles the negative in Verin's
  line. CB36 fixes the pronoun and the dangling "without it" (priority item 8). CB37 splits the five-action chain and gives
  "about it" a referent.
- **Ch.6.** CB38: no one can see their own back by twisting, so he now sees only part of it. CB39 changes "until" to
  "before". CB40 avoids reusing "grandfather" (Ch.5:35 already has "an easy smile"). CB41: the previous sentence's subject
  is Raizen. CB42 cuts the caption after four shown reactions. CB44 removes the doubled "A lot of sense". CB45 fixes a
  misplaced modifier.
- **Ch.7.** CB47 states the chest's size plainly. CB48: the book calls it the main room, not the common room. CB49: no
  hallway exists; the rooms are side by side off the main room. CB50 names the hair, which is the source of the
  crackling. CB51 fixes number agreement. CB52 removes a gaze repeated three times. CB53 makes "unfriendly" modify the
  stare.
- **Ch.8.** CB54 drops a feather simile that doesn't fit a fingernail line. CB55 adds "then" to the comparison (author's
  meaning: "More rare than they are today"). CB56 uses the term Amelia used a line earlier ("On your home plane").
- **Ch.9.** CB57: the schedule was left on the coffee table (Ch.8:93), so he now picks it up. CB58: Bal sits under the
  window, so avoiding him "by the windows" made no sense. CB59 makes the pulse warm instead of mixing pulse and warmth.
  CB60 softens "paid no attention", since the next lines track Porter's color. CB61 makes the mouth wordless rather than
  "empty". CB62 removes the classroom clock, which was never set up; the library clock (src) stays, so 9.270 is resolved.
  CB63 splits the long motive sentence. CB64 adds the noun the clause was missing.

Fixes considered and rejected: "between her eyebrows", "far side of the room", "to see what", "the coffee table" (each
made a 3+ phrase recur 3 times book-wide); "than he had ever noticed" and "as far as he could see" (each recurred across
two of Bal's chapters). They were reworded to the forms above.

## B, optional cuts (verdict sentences and repeats)

Each is a clean deletion or trim and gate-clean on its own. The scene already shows what the cut sentence tells. Take
any of them only if the book-wide word budget allows (all of them together: −174).

| Cut | Flag | Ch | Exact current text | Replacement | Δw |
|---|---|---|---|---|---|
| O1 | 1.103 | 01 | ` It was the kindest thing anyone had done for Bal in years.` | *(delete)* | -12 |
| O16 | 2.085 | 02 | `The braziers burned low and steady and gave off no smoke at all, and he couldn't see any wood in them.` | `He couldn't see any wood in the braziers.` | -13 |
| O7 | 2.016 | 02 | ` Her skin was pale as candle wax against all that black.` | *(delete)* | -11 |
| O8 | 2.125 | 02 | `Bal wasn't sure that was the comfort she seemed to think it was.⏎⏎` | *(delete)* | -13 |
| O10 | 3.064 | 03 | ` It was very distracting.` | *(delete)* | -4 |
| O2 | 3.214 | 03 | ` No cars, no phones, no television.` | *(delete)* | -6 |
| O3 | 3.025 | 03 | `It hurt. There was no point pretending otherwise; it hurt badly, a deep, pulling ache in the bones.` | `It hurt, a deep, pulling ache in the bones.` | -9 |
| O4 | 3.052 | 03 | `brightening a little under his gaze and dimming when he looked away.` | `brightening a little under his gaze.` | -6 |
| O9 | 3.004 | 03 | ` Bal was fairly sure of it.` | *(delete)* | -6 |
| O11 | 4.038 | 04 | ` Bal was worried enough for both of them.` | *(delete)* | -8 |
| O17 | 5.037 | 05 | `kind blue eyes set in a nest of wrinkles.` | `kind blue eyes.` | -6 |
| O18 | 6.183 | 06 | ` Nothing about her had changed at all.` | *(delete)* | -7 |
| O19 | 6.267 | 06 | `her eyes traveled on along the corridor, past the paintings to wherever it was they were going.` | `her eyes traveled on along the corridor, past the paintings.` | -7 |
| O12 | 7.117 | 07 | ` The kitchen had a stove in it and food in it, which was what kitchens were supposed to have, and he stood there pleased with it anyway.` | *(delete)* | -27 |
| O13 | 8.208 | 08 | ` The rest of the dorm was empty and silent.` | *(delete)* | -9 |
| O5 | 8.066 | 08 | ` He couldn't seem to get it closed.` | *(delete)* | -7 |
| O6 | 8.118 | 08 | ` He read it again and it said the same thing.` | *(delete)* | -10 |
| O14 | 9.148 | 09 | ` He was the color of the chalk.` | *(delete)* | -7 |
| O15 | 9.240 | 09 | ` Thankfully she was the helpful sort.` | *(delete)* | -6 |

Lowest-cost, highest-value optional cuts: O12 (−27; the joke repeats what the stocked kitchen already shows), O1 (the
garden string already proves the kindness), O18 and O19 (6.183 and 6.267, in Muse's headline examples), O6 and O5 (filler).

## C: author's call

| Flag | Item | Options | Recommendation |
|---|---|---|---|
| 3.026 (TELLING) | Bal's high pain tolerance is first stated at the regrowth, just when the scene needs it. | (a) Leave. It is canon (CLAUDE.md canon facts; src l.281 "Having an unusually high pain tolerance") and is phrased as a lifelong trait. (b) Plant it earlier in Ch.1, e.g. a clause on the long-healed stump or a roof scrape. That would be a new incident, which counts as invention. | **Leave.** Ch.5's bite ("Bal barely felt it") confirms it straight after. |
| 3.213 | School-plane exposition mid-walk | Already C in the earlier triage (3.2). | Leave (as before). |
| 5.062 | Amelia's cover story ("I'll just say I'm enrolling") is asserted, not built | Already C in the earlier triage (5.1). Source line verbatim. | Leave (as before). |
| 7.057 | Curfew exemption as Lead Mage | Already C in the earlier triage (7.1). Source line. | Leave (as before). |
| 8.088 | Conversion mechanism vague ("gets used to your blood") | Already C in the earlier triage (8.5). Source line verbatim. | Leave (as before). |

## D: conflicts with a ruling

| Flag | Muse's ask | Ruling |
|---|---|---|
| 7.323 | Replace "You'd be surprised" with something wittier | 2026-10-20: "'You'd be surprised' stays at the pizza scene" (source order ruling). |
| 8.050 | Bal should hear "too good to pass up" as predatory, or challenge it | 2026-10-20: Amelia is not a manipulator; do not invent friction or a new Bal flaw; conversions are free choices. The book already has Bal reason "So it would be up to Viridia. Hers to choose." (Ch.8:67). |

## A: fine as is / Muse misread (one-line proof)

"Src" means the flagged sentence is the author's own script line (or very close to it), kept under the dialogue/script ruling.

**Ch.1.** 1.024 src ("For some reason the stump had always itched"). 1.030: the late "left palm" is the payoff Muse itself
names a standout (1.034). 1.039 src; the antecedent is his magic, two sentences earlier. 1.048 src ("Which is why Bal was on
the roof…"). 1.061: "until it went brown" *is* the statement that he sat for minutes. 1.072: Bal's voice, and Muse praises
the joke. 1.086: clear; Fredrick's send-off gets its own scene two paragraphs later. 1.111: Bal stretching the textbook's
limit is the point ("He'd decided that counted"). 1.129: blockage mechanics clear; src "magical blockage". 1.148: speed is
intended (Muse concedes). 1.151: the look-down joke needs the chain. 1.154: "without thinking" marks instinct; no rule
needed. 1.155: src ("What Bal didn't expect was that…"). 1.173: src spell words ("Locos cantis"). 1.180: src ("high stone
pillars"). 1.184: motes do turn in light. 1.190: the interruption *is* the transition into "Because it's magic" (src).
1.197: inference from a mischievous whisper is within Bal's POV.

**Ch.2.** 2.008: misread. The *cat* is Bal (she studies *him* like a stray on her doorstep), not Amelia. 2.011: fine.
2.017: src ("just the right amount of curves"); the age issue is closed by B1 and the NA ruling. 2.022: src ("which was
a first for Bal"). 2.037: fine. 2.083: framed as the sitting-still second look ("Now that he was sitting still…").
2.086: the new fact is "though nobody… could get through those doors", which sets up "who did the sweeping". 2.099: one
sentence of Bal's recognition. 2.111: src ("scrambled to his feet backing away slowly"). 2.151: src verbatim, followed
by the bodily "click". 2.169: Ch.4 explains it: a strong sygl shows at birth ("His sygl showed the day he was born"; src).
2.215: src joke ("As in she literally exploded"). 2.224, 2.227: fine. 2.240: src. 2.247: the narrowing into firelight is
the mechanism given (src "the firelight reflecting off her blood red eyes"). 2.260: src ("never taking her eyes from
his"). 2.264: misread. *anything* deliberately echoes her "Would you do *anything* to go?" 2.296: dreamlike list intended.
2.301: sygls sit on the palm, so needing a hand for the mark is exactly right; the blood connection is a separate thing.

**Ch.3.** 3.001: src's opening line ("regrowing a hand is accomplished by…"), a memorable line. 3.017: a fierce entry
that settles to warmth, which is the trajectory Muse asks for. 3.037: src narration, attributed ("She was right about
that"). 3.063, 3.091: src beats (stretch; embarrassment at the vow), NA register. 3.078: src ("Bals heart began beating
faster"). 3.116: src ("she says giggling"). 3.135: "to see how he would take it" sets up the echo "Bal didn't know how to
take it". 3.139: there is a wall (Ch.2:31 "over the wall"; Ch.3:95 mossy wall). 3.148: release panorama, intended. 3.170:
fine. 3.183: "anyway" answers "And it smells". 3.185: src verbatim. 3.222, 3.236: fine.

**Ch.4.** 4.012: habitual "had worn" (src "always wore"). 4.014, 4.018, 4.020: src. 4.033: deliberate. Src's "in two weeks"
contradicts its own next-day claiming. 4.040: src ("little in the way of personality"); its repeats are handled by CB25.
4.043: "frame" is needed for "the man in the frame" later. 4.057: src verbatim. 4.058: the summary is already blurted
("And… And…"); a mid-stream interruption would be invented business. 4.072: established at Ch.3:3 ("vampire goddess")
and src. 4.073: src goldfish. 4.078: one-line dry shout, fine. 4.146: deliberate one-clause callback marking her return to
herself. 4.193: deadpan voice. 4.215: src ("just a regular girl"). 4.253: src verbatim. 4.258: paid off at Ch.8:35 ("someone
with his rarest inheritance gift"). 4.281: misread. "I doubt it" is *Amelia's* reply to Bal's "You'll be sorry."

**Ch.5.** 5.004: needed. Author ruling introduces Pierre, and the earlier triage (A 4.5) relies on this line. 5.061: src.
5.073: the antecedent is "both hands" in the previous sentence. 5.099, 5.104, 5.108: src. 5.102: one beat of duration,
harmless. 5.176: src. 5.182: src, and the next line's joke ("Well, maybe not the vampire part") needs it. 5.191: src
briefing, already interrupted by Amelia's shaking shoulders. 5.209: src verbatim. 5.226: misread. It is one image
(smudges *like spilled flour*), not two. 5.296: the comma pause is deliberate.

**Ch.6.** 6.001: src. 6.017: author ruling. The guess is wrong on purpose and corrected at Ch.7:117. 6.021: src; mortals
don't know, and the originators are rarely seen ("the only time you ever see them"). 6.079: src ("sandalwood sandals").
6.096, 6.102: src speech. 6.150: what Bal sees "properly" up close (src: Kenmei's eyes). 6.166: src ("smiles sadly").
6.195: already pending (B1). 6.199: src memorable threat. 6.206: shaking heads answers "Will you [return]?" with no;
src. 6.253, 6.258: src verbatim.

**Ch.7.** 7.025: src setup for the rooms appearing. 7.063: src. 7.090: the doubled "anybody" is the joke. 7.145: a
deliberate three-beat stillness. 7.152: fine. 7.159: Ch.5:119 rule ("your sygl will appear on your clothes"). 7.170: src
("pale blue hair and matching color eyes"). 7.176: misread. Shaking wool in dry winter air *does* crackle with static.
7.181, 7.184, 7.206, 7.215, 7.222: src lines verbatim. 7.230: src pun, made right after the hair crackles. 7.237: fine.
7.251: src rule; Ch.9:5 confirms it. 7.255: voice. 7.265: fine. 7.306: src verbatim. 7.337: one beat. 7.343: src
verbatim. 7.356: src ("hostile stares"). 7.366: src phrase ("the whole High Priest thing").

**Ch.8.** 8.019: deliberate parallel. 8.026, 8.029: src ("Something in Amelia's voice"; "waits for Bal to make the
connection"). 8.047: fine. 8.062: fine. 8.091: Bal's irreverence, a callback to lunch. 8.104: src verbatim. 8.120: the
joke escalates. 8.145: compares delivery and is clear. 8.165, 8.167, 8.168, 8.171: src (mortal/Immortal threshold,
"leg up", "automatically teleported"). 8.185: "her roof", where he has looked all book long; reads clearly. 8.194: src;
adding battle detail would be invention. 8.204, 8.209, 8.221, 8.223, 8.226: src lines.

**Ch.9.** 9.006: already plain. 9.018: banter. 9.022: deliberate. 9.032, 9.039, 9.063, 9.101: src. 9.089: fine.
9.107: src glasses-catch-light, used twice. 9.134: fine. 9.157: the slow-turn echo is deliberate. 9.180: fine. 9.193:
src ("Like a switch had been flipped"); the world has modern tech. 9.197, 9.201: src. 9.206: earlier triage A 9.2.
9.227: Bal's guess, harmless. 9.228: src route. 9.249: a deliberate pause before the recognition. 9.255, 9.259: src
verbatim (and Ch.8: "they decided to leave me alone"). 9.270: the library clock is src; the classroom clock is removed by
CB62. 9.276: the next sentence states the reason.

## Gate results (scratch copy)

Scratch copy: `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/cr1/`. It holds the whole
manuscript as both `manuscript/chapter-NN.md` and `manuscript/chapters/chapter-N.md`, plus `tools/`, `STATE.yaml` and
`character-bible.md`, with the 60 B fixes applied. The real files are untouched.

| Gate (run from cr1/) | Baseline | With B fixes |
|---|---|---|
| `style_check.py --dir manuscript` | clean | clean (repeated-phrase list identical to baseline) |
| `grammar_check.py --dir manuscript` | clean | clean |
| `tic_report.py --gate` | clean | clean |
| `voice_wear_check.py` | clean (strict) | clean (strict) |
| Words (`manuscript/chapters`) | 90,082 | 90,000 (−82) |

First run: my first wording of seven fixes failed the strict gates. Five made a 3+ word phrase recur three times book-wide
("between her eyebrows", "the far side", "to see what", "the coffee table", "the main room"). Two made a phrase recur
across two of Bal's chapters ("than he had ever", "as far as he"). All seven were reworded (CB11, CB21, CB38, CB48, CB57,
CB58, CB60), and every gate came back clean. The optional cuts, applied on top in a second copy (`scratchpad/cr1o/`), are
also clean on all four gates (89,815 words), after O19 was reworded to avoid a third "her eyes went".
