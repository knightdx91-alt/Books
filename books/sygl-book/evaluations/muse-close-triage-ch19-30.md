# Muse close reading, Ch.19–30: triage against the text (2026-10-21)

Source: `feedback/muse-close-reading-2026-10-21.txt` (Meta Muse's sentence-by-sentence close reading, the full
118-page export). I checked every flag from \[19.011\] to \[30.157\] against `manuscript/chapter-NN.md`, against
`Sygl_Complete.txt` (wherever the line is the author's), against the STATE.yaml rulings, and against the earlier
triage (`evaluations/muse-triage-2026-10-21.md`, fixes B1–B12, still pending). **No chapter or STATE file was
edited.** The B fixes were applied only to a scratch copy, where all four gates pass.

Muse's sentence numbers are its own. I found each flag by its quoted excerpt. Line numbers below refer to the
current files.

Buckets:
- **A**: fine already, or Muse misread it.
- **B**: fix without changing the story.
- **Optional cut**: a B-type telling cut that is left out of the B list because of the word budget and the
  90,000-word floor.
- **C**: author's call.
- **D**: conflicts with an author ruling.
- **Already pending**: an earlier-triage fix already covers it.

## Summary

190 flagged sentences in range (Ch.19 16, Ch.20 16, Ch.21 17, Ch.22 22, Ch.23 9, Ch.24 21, Ch.25 23,
Ch.26 9, Ch.27 21, Ch.28 13, Ch.29 15, Ch.30 8). Each one sits in exactly one bucket. The editor's and agent's
notes are triaged separately at the end and are not in the counts.

| Category | A | B | Optional cut | C | D | Already pending | Total |
|---|---|---|---|---|---|---|---|
| CLARITY | 22 | 30 | 1 | 0 | 0 | 0 | 53 |
| LOGIC | 14 | 10 | 1 | 8 | 3 | 2 | 38 |
| TELLING | 3 | 11 | 13 | 6 | 2 | 0 | 35 |
| REPETITION | 3 | 12 | 3 | 0 | 0 | 0 | 18 |
| IMAGE | 5 | 6 | 0 | 0 | 0 | 0 | 11 |
| RHYTHM | 2 | 4 | 1 | 0 | 0 | 0 | 7 |
| DIALOGUE | 1 | 3 | 0 | 0 | 0 | 0 | 4 |
| CONTINUITY | 6 | 1 | 0 | 1 | 4 | 3 | 15 |
| POV | 0 | 4 | 0 | 0 | 1 | 0 | 5 |
| GRAMMAR | 1 | 3 | 0 | 0 | 0 | 0 | 4 |
| **Total** | **57** | **84** | **19** | **15** | **10** | **5** | **190** |
**Words.** The B list is 81 edits covering 84 flags, and its net is **−95 words**, inside the −120 to +60
window. Three edits each cover two flags: CB53, CB56 and CB62.
- Baseline: 90,082.
- With this B list alone: 89,987.
- With this B list and the earlier B1–B12 (+25): **90,012**. That is above the 90,000 floor, but only by
  12 words.
- So the optional cuts below (−182 in all) **cannot be taken without words added back somewhere else**.

**Priority-list items in range:**

| Item | Bucket | Note |
|---|---|---|
| 2 (20.211) | already pending (B7) | B7 makes Ch.18 match Ch.20, the reverse of Muse's direction. |
| 5 (22.047) | A | The line is correct. |
| 6 (24.410) | B | CB7. |
| 12 (28.195) | A | The book's world has TV. |
| 14 (30.157) | D | The script's own wording. |

## B: apply-ready fixes

Each old string occurs exactly once in its file, and the table gives the final gate-clean wording. ⏎⏎ marks a
paragraph break. CB37, CB60 and CB84 were moved to the optional cuts (O3, O10, O19) to protect the word floor.

| Fix | Ch. | Exact old text | New text | Flag / category | Δw |
|---|---|---|---|---|---|
| CB1 | 19 | `Apparently, when the originators called the teachers in this morning, he told them that` | `Apparently, when the originators called the teachers in this morning, Mr. Porter told them that` | 19.011 CLARITY | +1 |
| CB2 | 19 | `Ban all students from socializing with other students, except in class,` | `Ban students from socializing with other sygls, except in class,` | 19.024 LOGIC | -1 |
| CB3 | 19 | `It had been full of ideas about Toma, and Toma could wait.` | `It had given him a few ideas about Toma, and Toma could wait.` | 19.044 CLARITY | +1 |
| CB4 | 19 | `He hesitated, then gave her the rest of it, since it was true.` | `He hesitated, then gave her the rest of it.` | 19.081 TELLING | -4 |
| CB5 | 19 | `He was in the villages in his head, in Thad's narrow room with the bad news.` | `His mind went to the villages, to Thad's narrow room and the bad news.` | 19.090 CLARITY | -2 |
| CB6 | 19 | `He was extremely pleased with that one.⏎⏎Viridia let out` | `Viridia let out` | 19.112 TELLING | -7 |
| CB7 | 24 | `Lora transferred the poison with her wooden spoon.` | `Bal emptied a mugful of the brandy into the washbasin first. Lora transferred the poison with her wooden spoon.` | 24.410 LOGIC (prio 6) | +11 |
| CB8 | 25 | `turned any liquid into pure water. Any liquid. Whatever` | `turned any liquid into pure water. Whatever` | 25.169 REPETITION | -2 |
| CB9 | 19 | `It stung and then mostly stopped stinging.` | `It stung, then mostly stopped.` | 19.164 REPETITION | -2 |
| CB10 | 19 | `theirs gave way. It retreated into the cuts.` | `theirs gave way. Their blood retreated into the cuts.` | 19.177 CLARITY | +1 |
| CB11 | 19 | `It had to be steady and it had to be gentle, both at once, in two people` | `It had to be steady and it had to be gentle, in two people` | 19.183 REPETITION | -3 |
| CB12 | 19 | `his blood rolled over theirs and took it.` | `his blood rolled over theirs and took hold.` | 19.190 CLARITY | +0 |
| CB13 | 19 | `into the hall at breakfast, and he would bring it to their table, and he would find out it was too late.` | `into the hall at breakfast, bring it to their table, and learn it was too late.` | 19.232 RHYTHM | -6 |
| CB14 | 20 | `Then the heads stayed around.` | `Then the heads stayed turned.` | 20.012 RHYTHM | +0 |
| CB15 | 20 | `interfering with another sygl's member, Mr. Porter?` | `interfering with a member of another sygl, Mr. Porter?` | 20.108 DIALOGUE | +2 |
| CB16 | 20 | `to hear what came next, all of it, the Terra` | `to hear what came next, the Terra` | 20.112 RHYTHM | -3 |
| CB17 | 20 | `That's a lie, and people like Mr. Porter here keep spreading it so` | `The stories saying so are lies, and people like Mr. Porter here keep spreading them so` | 20.116 CLARITY | +3 |
| CB18 | 20 | `wring the milk from her skirt and kept having to stop.` | `wring the milk from her skirt and kept having to stop to laugh.` | 20.160 CLARITY | +2 |
| CB19 | 20 | `before he had to declare war on me.` | `before I could declare war on him.` | 20.174 LOGIC | -1 |
| CB20 | 20 | `He ought to leave your village alone.` | `He'll probably leave your village alone.` | 20.199 CLARITY | -1 |
| CB21 | 21 | `underneath them. It was a sight to see.` | `underneath them.` | 21.030 TELLING | -6 |
| CB22 | 21 | `Bal felt it. He let it happen. He gave` | `Bal felt it. He gave` | 21.114 LOGIC | -4 |
| CB23 | 21 | `and sent him into the tree behind him.` | `and sent him into the nearest tree.` | 21.118 CLARITY | -1 |
| CB24 | 21 | `Bal knew he was telling the truth.` | `Bal believed him.` | 21.155 LOGIC | -4 |
| CB25 | 21 | `he had not even felt go in.` | `he had not even felt land.` | 21.183 CLARITY | -1 |
| CB26 | 21 | `That was the one that was going to hurt most, now it had started hurting.` | `That was the one that would hurt most, now that it had started.` | 21.187 GRAMMAR | -2 |
| CB27 | 21 | `The blade had gone through into the muscle.` | `The blade had gone deep into the muscle.` | 21.188 CLARITY | +0 |
| CB28 | 21 | `It was all over his face." Amelia was enjoying this. "So Aren` | `It was all over his face. So Aren` | 21.253 TELLING | -4 |
| CB29 | 22 | `Nobody in Raizen's lands would ever mistake it.` | `Nobody in Raizen's lands would ever mistake what it meant.` | 22.044 CLARITY | +2 |
| CB30 | 22 | `We managed to kill them both before` | `We managed to wipe out both before` | 22.074 CLARITY | +0 |
| CB31 | 22 | `The three of them meet in a week's time` | `He and the others meet in a week's time` | 22.097 CLARITY | +0 |
| CB32 | 22 | `Xavier came around behind his chair` | `Xavier came around behind Bal's chair` | 22.101 CLARITY | +0 |
| CB33 | 22 | `She went with him or she didn't go, he told them` | `Either she went with him, or she didn't go at all, he told them` | 22.149 LOGIC | +3 |
| CB34 | 22 | `with Hopper ranging ahead of her through the soldiers' legs.` | `with Hopper ranging ahead of her through the press of soldiers.` | 22.157 IMAGE | +1 |
| CB35 | 22 | `People were not going to look closely at whoever was traveling with someone so obviously Tempus. So Viridia was` | `Viridia was` | 22.218 REPETITION | -17 |
| CB36 | 22 | `He reached for help.` | `He looked to Lora for help.` | 22.299 CLARITY | +2 |
| CB38 | 23 | `"Of course," the big guard said again, quick` | `"Certainly, my lady," the big guard said, quick` | 23.154 REPETITION | +0 |
| CB39 | 24 | `had been told to look out for them.` | `had been told to expect them.` | 24.007 CLARITY | -2 |
| CB40 | 24 | `We could always use our blood darts.` | `We could just use our blood darts.` | 24.179 DIALOGUE | +0 |
| CB41 | 24 | `Bal reached her before it finished opening.` | `Bal reached her before the door finished opening.` | 24.223 CLARITY | +1 |
| CB42 | 24 | `Viridia might have guessed, and so might Bal.` | `Viridia might have guessed as much, and so might Bal.` | 24.239 CLARITY | +2 |
| CB43 | 24 | `since she couldn't leave the cauldron until the brew was well under way.` | `since she couldn't leave the cauldron once the brew was under way.` | 24.245 LOGIC | -1 |
| CB44 | 24 | `but less than it had at noon.` | `but less than it had at the gate.` | 24.284 CLARITY | +1 |
| CB45 | 24 | `He had not only asked her about after school to learn her plans.` | `He hadn't asked her about after school only to learn her plans.` | 24.318 CLARITY | -1 |
| CB46 | 25 | `Lora had read them that part of the book too. No one had found a cure for nightstalker poison.` | `Lora had read them that part of the book too.` | 25.121 REPETITION | -9 |
| CB47 | 25 | `Bal waited at the bar and let the shelves go by in front of him without taking in any of it.` | `Bal waited at the bar and looked along the shelves without taking in any of it.` | 25.142 IMAGE | -5 |
| CB48 | 25 | `went bouncing around the empty room.` | `went bouncing around the quiet room.` | 25.180 CLARITY | +0 |
| CB49 | 25 | `when it no longer mattered what he found out.` | `when finding out would do nobody any good.` | 25.188 CLARITY | -1 |
| CB50 | 25 | `Lora, off at her own table, sipped her water.` | `Lora, off at her own table, wet her lips with her water.` | 25.226 LOGIC | +3 |
| CB51 | 25 | `She was shaking so hard it rattled into his own teeth.` | `She was shaking so hard it went through his hands.` | 25.237 IMAGE | -1 |
| CB52 | 25 | `"Viridia." It was too fast, and he could not slow it.` | `"Viridia." The words came too fast, and he could not slow them.` | 25.241 CLARITY | +1 |
| CB53 | 25 | `the first mouthful, whatever she had tasted and thought nothing of. Then it reached her face.` | `the first mouthful, how watery it had tasted. Then he saw it reach her face.` | 25.253 LOGIC + 25.254 IMAGE | -1 |
| CB54 | 26 | `Viridia was down off her horse first. She had nothing to add.` | `Viridia was down off her horse first.` | 26.018 TELLING | -5 |
| CB55 | 26 | `She took a deep breath. It left her slow and uneven.` | `She took a deep breath. It left her slowly and unevenly.` | 26.050 CLARITY | +0 |
| CB56 | 26 | `to the grass again. Some of it was fear. More of it was relief. Bal heard that in it too. She was alive` | `to the grass again. She was alive` | 26.083 + 26.085 TELLING | -16 |
| CB57 | 26 | `He didn't mean much by it, and she knew he didn't.` | `He didn't mean much by it, and she seemed to know he didn't.` | 26.120 POV | +2 |
| CB58 | 26 | `The words hung there in the dark and nothing answered them.` | `The words hung there in the dark.` | 26.131 IMAGE | -4 |
| CB59 | 26 | `Nobody had followed them down the road all night.` | `Nobody seemed to have followed them down the road.` | 26.144 POV | +0 |
| CB61 | 27 | `They walked south through the yellow grass` | `They rode at a walk south through the yellow grass` | 27.014 CLARITY | +3 |
| CB62 | 27 | `Bal smiled at her, at the pleasure all over her. The Three Boars was behind her, then. Her hair was popping again, tiny blue snaps along the ends of it every time the breeze lifted them, and he had missed the sound more than he'd realized.` | `Bal smiled at her. Her hair was popping again, tiny blue snaps along the ends of it every time the breeze lifted them, and he had missed the sound more than he'd realized. The Three Boars was behind her, then.` | 27.055 + 27.056 TELLING | -6 |
| CB63 | 27 | `They did not feel what he felt, plainly.` | `They did not seem to feel what he felt.` | 27.080 POV | +1 |
| CB64 | 27 | `Bal's attention was still back toward Londra` | `Bal's mind was still back toward Londra` | 27.100 REPETITION | +0 |
| CB65 | 27 | `The horse that had been hit was Lora's.` | `The horse that had been hit was Lora's. Neither of the others was anywhere in sight.` | 27.161 CONTINUITY | +8 |
| CB66 | 27 | `He worked the straps loose breathing through his mouth` | `He worked the straps loose, breathing through his mouth` | 27.164 GRAMMAR | +0 |
| CB67 | 27 | `Whenever he stopped, it found him again` | `Whenever he stopped, their absence found him again` | 27.206 CLARITY | +1 |
| CB68 | 27 | `He slid down off Barda and left him to graze.` | `He slid down off Barda, blown and head-down, and left him to graze.` | 27.261 LOGIC | +3 |
| CB69 | 27 | `His body had gone somewhere else and not told him where.` | `His body had gone somewhere else.` | 27.339 IMAGE | -5 |
| CB70 | 27 | `His legs might have belonged to somebody else.` | `His legs would not answer.` | 27.348 REPETITION | -3 |
| CB71 | 28 | `before the slop had finished spreading.` | `before the spill had finished spreading.` | 28.010 REPETITION | +0 |
| CB72 | 28 | `He lay and let that settle on him, and it got no easier with lying there.` | `He lay and let that settle on him. Lying there made it no easier.` | 28.020 CLARITY | -2 |
| CB73 | 28 | `not to speak of them. Nobody should. It touched` | `not to speak of them. It touched` | 28.199 TELLING | -2 |
| CB74 | 28 | `He felt her sigh against him, all of it, held, it seemed, since she had left the room.` | `He felt her sigh against him, held, it seemed, since she had left the room.` | 28.210 CLARITY | -3 |
| CB75 | 28 | `Sometime in the first night one idea nearly worked, and she called` | `Sometime in the first night, one idea nearly worked. She called` | 28.232 RHYTHM | -1 |
| CB76 | 29 | `The cords stood out in her neck with it.` | `The cords stood out in her neck with the shouting.` | 29.022 CLARITY | +1 |
| CB77 | 29 | `free to do whatever she wants.` | `free to do whatever she wanted.` | 29.053 GRAMMAR | +0 |
| CB78 | 29 | `She jumped. She bounded` | `She bounded` | 29.066 REPETITION | -2 |
| CB79 | 29 | `as tall as before and turning as it had turned,` | `as tall as before, still turning,` | 29.181 REPETITION | -4 |
| CB80 | 29 | `If somebody comes asking me to, I can compromise.` | `If somebody comes asking me to convert them, I can compromise.` | 29.260 DIALOGUE | +2 |
| CB81 | 29 | `He was not used to mortals forgetting themselves` | `From his face, he was not used to mortals forgetting themselves` | 29.283 POV | +3 |
| CB82 | 29 | `engaging you again." His beard stirred. "I must return."` | `engaging you again. I must return."` | 29.304 REPETITION | -3 |
| CB83 | 30 | `Not for one minute had they doubted it. Down in the dirt` | `Down in the dirt` | 30.088 TELLING | -8 |
| | | | | **net** | **−95** |

### Why the less obvious B fixes are safe

- **CB1, CB2 (Ch.19, dialogue).** The source has the same wording (src l.783). CB1 names the speaker Amelia
  means. CB2 brings the rule into line with Porter's announced version in Ch.20:47 ("No sygl may socialize
  with another sygl"). In both, the meaning, speaker and placement stay the same.
- **CB3 (19.044).** Ch.18:167 sets up "The history book he had been using for ideas". Muse's "material on Toma"
  would put a living man inside a history book.
- **CB5 (19.090).** Muse's version adds "news he had carried". That is wrong: Thad brings the news to Bal
  (Ch.18:85).
- **CB6 (19.112).** The source line "says with a grin" is carried by the sigh and the laugh. "He grinned" made
  three smiles or grins within 258 words.
- **CB7 (24.410).** Source p.909 has a scraped-out cauldron spooned into a sealed cask. Drawing a mugful off
  first makes the step possible, and it is compatible with B11's "stopper driven back flush".
- **CB10 to CB12 (Ch.19 ritual).** These name the moving blood. Source: "his blood forced theirs back … he
  overwhelmed the blood with his own".
- **CB13 (19.232).** This removes the "he would" chain, which blurred Porter and Bal.
- **CB17 (20.116).** The source has the same slip ("Being a blood mage does not make you more crazy … That's just
  a lie"). As written, "That's a lie" points at Bal's own denial. The fix points it at the stories.
- **CB19 (20.174).** Amelia is the one who declared war (Ch.19:191, Ch.20:101). The new line says so.
- **CB20 (20.199).** Source: "He should leave your village alone", meaning a prediction. The new line keeps that
  sense.
- **CB22 (21.114).** Source: "all he did was step backwards a step". "He let it happen" claimed a choice the
  source does not make.
- **CB24 (21.155).** The fix keeps Bal's judgement and drops the narrator's certainty. Violence is unchanged
  (justified-violence ruling).
- **CB28 (21.253).** This cuts the narration inside Amelia's anecdote. The quotes are merged so her speech runs
  on.
- **CB33 (22.149).** The meaning is unchanged: Viridia goes only if Bal goes.
- **CB35 (22.218).** This is the third statement of hair-as-passport in Ch.22 (after :109 and :117). Lora's
  Ch.24 line is the author's dialogue and stays (24.083 is A).
- **CB38 (23.154).** "Said again" wrongly gave the big guard the truncheon guard's earlier "Of course". The new
  line also varies the third "Of course".
- **CB43 (24.245).** Lora is explaining why she will be tied down once she starts, not saying the cauldron is
  already lit.
- **CB50 (25.226).** This makes Lora's mimed drinking explicit, so "never got any emptier" pays off. Ch.26:79
  "water she couldn't taste" still fits.
- **CB53 (25.253/254).** Source: Viridia "remembers the watery taste of the brandy". It is the source's own
  sensory fact.
- **CB56 (26.083/085).** Muse's strongest Ch.26 note. "She was alive, and it had only now reached her" carries
  the beat.
- **CB59, CB57, CB63, CB81.** These POV fixes keep the knowledge inside Bal's perception (Bal-only close-third
  ruling).
- **CB61 (27.014).** "Walk them" means the horses. Ch.27 later has them riding.
- **CB65 (27.161).** All three horses bolted at the attack. This one line accounts for the two that are not
  found, and adds no new fact.
- **CB68 (27.261).** Source: Bal rode "all night … alternating between a gallop and a slower trot". "Blown and
  head-down" prices that ride in three words.
- **CB80 (29.260).** Source: "If I am approached about it, I can compromise". "It" is the conversion ability
  Aren just asked about, so naming it adds nothing new.

### Rewording forced by the gates

These were the first drafts that tripped a gate; the table above has the gate-clean versions.

- "He had been reading/using it for ideas" (CB3): voice_wear, echoes Ch.18:167.
- "poured … off into the" (CB7): tic, "off into the" 3×.
- "He grinned." (CB6): gesture class.
- "and find out it was too late" (CB13): tic, "and find out" 3×.
- "He and the other two meet" (CB31) and "The other two were nowhere in sight" (CB65): tic, "the other two" 4×.
- "It went out of her" and "let it go" (CB55): tic, 3×.
- "Lying there did not make it any easier" (CB72): tic, "did not make" 3×.
- "let his eyes go over" (CB47): voice_wear and tic.
- "As far as he could tell" (CB59): voice_wear "as far as he", tic "he could tell".
- "a sigh she seemed to have held" (CB74): the sigh count reached 3 in Ch.28.
- "as if she had held it" (CB74): voice_wear self-repeat.

## Optional cuts (not in the B list)

These are all telling or repetition cuts Muse asked for. They are kept out of the B list because the book would
fall below 90,000 words: the B list already leaves only 12 words of headroom. O3, O10 and O19 were gate-tested
inside the B list before being moved out. The rest are exact-string checked but not gate-tested. To take any of
them, add the same number of words elsewhere first. The highest-value ones are O3, O9, O12 and O19.

| Cut | Flag | Ch. | Exact old text | New text | Δw |
|---|---|---|---|---|---|
| O1 | 19.235 | 19 | `He did not mention that he could have had another before he reached the door. The dorm would have made it for him gladly.` | `He did not mention that the dorm would gladly have made him another.` | -11 |
| O2 | 22.109 | 22 | `He went around the problem one way and then the other. He was looking` | `He was looking` | -11 |
| O3 | 22.313 | 22 | `She had stopped pacing. She was afraid, and not only for him.` | `She had stopped pacing.` | -8 |
| O4 | 23.055 | 23 | `He was amazed at his luck, constantly. One beautiful` | `One beautiful` | -7 |
| O5 | 23.160 | 23 | `wherever Viridia passed, a good many of them.` | `wherever Viridia passed.` | -5 |
| O6 | 24.414 | 24 | `Five hard blows drove the stopper home, and they must have carried down to every table below.` | `Five hard blows drove the stopper home.` | -10 |
| O7 | 25.055 | 25 | `He walked Viridia's horse to a stall with enormous care,` | `He walked Viridia's horse to a stall,` | -3 |
| O8 | 25.126 | 25 | `She let her lashes fall once, slowly, the signal a lady gives her servant, and turned` | `She let her lashes fall once, slowly, and turned` | -7 |
| O9 | 26.106 | 26 | `caught her glasses. Her face was harder to read than usual. She had been` | `caught her glasses. She had been` | -8 |
| O10 | 27.009 | 27 | `Bal was satisfied. "Nobody's` | `"Nobody's` | -3 |
| O11 | 27.018 | 27 | `and then she had slept. This morning she was herself again, or near enough that Bal saw no difference from where he rode.` | `and then she had slept.` | -18 |
| O12 | 28.027 | 28 | `He told her the rest, all of it, from the leaf in Viridia's hair to the bolt out of a clear sky, the craters, the empty grass, Jazen and Barda, the mage with the whip made of lightning.` | `He told her the rest, all of it.` | -30 |
| O13 | 28.037 | 28 | `and she would break the rule against interfering to do it. Then the other originators would have every reason they needed. That was what this whole war was about to begin with: Amelia and the rest of them, and the rules, and who got to break them.` | `and she would break the rule against interfering to do it. Then the other originators would have every reason they needed.` | -26 |
| O14 | 29.008 | 29 | `Magnificent was the only word for him. His robes` | `His robes` | -7 |
| O15 | 29.011 | 29 | `Fern's file had said. He wore his years proudly.` | `Fern's file had said.` | -5 |
| O16 | 29.094 | 29 | `He brushed at one sleeve, though not a grain clung to it.` | `He brushed at one sleeve.` | -7 |
| O17 | 29.189 | 29 | `They did not exist. They never had.` | `They did not exist.` | -3 |
| O18 | 29.222 | 29 | `as well. Elemental and priest were life-bonded. Whatever` | `as well. Whatever` | -5 |
| O19 | 30.092 | 30 | `There was no answer to that in him. He stood there` | `He stood there` | -8 |

## C: author's call (options and a recommendation for each)

**19.162, simultaneous double conversion (LOGIC).** Source l.792: "The only thing he did differently was cutting
and converting them at the same time." The source gives no motive. The cost is already shown at Ch.19:159.
- Options: (a) leave; (b) add a motive clause (invented).
- **Recommendation:** (a). Invented motives are ruled out.

**21.265, Amelia's assurance to Aren ("only people you cared about") vs Bal's open invitation in Ch.20
(CONTINUITY).** Both are source lines: src p.126 "if he does it will only be ones he cares about", and Ch.20's
"welcome you with open arms".
- Options: (a) leave; (b) narrow Ch.20's invitation; (c) a Bal reaction beat. Muse's "Amelia lied" reading is D
  (the Amelia-not-manipulative ruling).
- **Recommendation:** (a). The invitation is to people who want to join, which is not a converting campaign.

**21.288, the familiar loophole (LOGIC).** Source line verbatim in substance ("as I am also Bal's familiar, so I
can help on certain things").
- Options: (a) leave; (b) define the loophole's scope (new worldbuilding).
- **Recommendation:** (a).

**22.136 / 22.145, the pitch and Xavier's objection are summarised, not played (TELLING).** The source also
summarises them.
- Options: (a) leave; (b) dramatise 2–3 lines of Bal's pitch and one line from Xavier. That would be new
  dialogue built only from facts already on the page. It adds about +60 words, which the floor would welcome.
- **Recommendation:** (b) only if the author wants a longer Ch.22; otherwise (a).

**23.051, "He was falling in love with the Vampire Goddess" (TELLING).** Source: "he felt he was starting to fall
in love with the Vampire Goddess". This is the author's own declaration.
- Options: (a) leave; (b) dramatise it.
- **Recommendation:** (a). The new paragraph around it (Ch.23:33) already earns it with the gate goodbye.

**24.229, Lora's three hours at the alchemist creates a witness (LOGIC).** This is source content.
- Options: (a) leave; (b) a one-line exposure worry (new beat).
- **Recommendation:** (a).

**24.270 / 24.281, the poison plan is decided in the street, and the cask dilution and bystanders are not priced
(LOGIC).** Source: "Why don't we just poison the whole cask?" / "Yeah that would probably work better", said on
the street. The book already prices potency ("By far the most potent brandy", the 20-hour brew).
- Options: (a) leave; (b) add a lowered-voice beat, or one exchange on dilution (new).
- **Recommendation:** (a).

**25.165 (+ front matter item 5), the purification rune is not planted before it saves Viridia (LOGIC).** The
source introduces the rune at that moment too. The ruling covers how it works (it works when carved), not where
it is planted. CB8 already removes the triple insistence.
- Options: (a) leave; (b) one line in Ch.18's rune-failure montage where Bal copies the purification rune. That
  would be a new beat. The montage already has Mr. Winters' runes class, and Ch.25:145 already claims "copied
  off Mr. Winters' chalkboard that first week".
- **Recommendation:** (b). One sentence, about +15 words, and it gives the floor margin.

**27.199, two days walking with no food accounted for (LOGIC).** Source: "Bal rode all night". The walk itself
is the book's.
- Options: (a) leave; (b) "He had nothing to eat, and did not look for anything." (about +11, a new fact).
- **Recommendation:** (b). It is cheap, and it helps the floor.

**28.229 + 29.060 + front matter / agent notes, the withheld memories and training, and the rules taught "off
page" and then recalled in Ch.29 (TELLING/LOGIC).** Source l.976: the memories are private, and Bal "understood
why she did not want him to speak of these things". The training is summarised in the source too. The rules
lesson recalled at Ch.29:47 is the book's bridge to Bal's source negotiation (src: "Killing Lora and Viridia
after I am dead will be an act of war").
- Options: (a) leave; (b) move the rules lesson into Ch.28's roof summary as one sentence (no new fact, only
  placement); (c) dramatise a memory or a technique (new content).
- **Recommendation:** (b) at most; (a) otherwise.

**30.066 + 30.099 + agent notes, the Ch.30 recap: circle mechanics re-explained, the elemental mystery
re-confessed, "cut the recap by a third" (TELLING).** The ruling is that the girls tell the kidnapping using
established facts only. Cutting a third (about 510 words) would break the 90,000 floor. 30.099 needs a new fact
about the elemental to "advance" it.
- Options: (a) leave; (b) trim inside the recap and add the same number of words elsewhere.
- **Recommendation:** (a).

**Front matter / agent notes: the "agency pattern" (19.162, 20.154, 30.157; Ch.19, Ch.20 and Ch.21 agent notes:
Bal "arranging outcomes", the recruitment speech hiding the costs, the darkening arc).** The rulings settle it:
- No new Bal flaw (FRICTION ruling).
- No guilt over the conversions.
- Violence is justified.
- Amelia manipulates no one.

"Amelia was rubbing off on him" (Ch.20:121) is the source's own line (src l.807).
- **Recommendation:** leave. It is a theme decision, not a line edit.

**Front matter / Ch.29 agent note: plant the blood-touching-a-bond beat before the climax (29.239, 29.327).**
- Options: (a) leave, since the accidental conversion is the source climax and the STATE premise; (b) one
  unexplained beat on Ch.28's roof (a new mechanic).
- **Recommendation:** (a).

## A: fine / Muse wrong (one-line proof each)

| Flag | Proof |
|---|---|
| 19.109 | Author's line (src l.789), and Bal is right: Porter cannot punish them in Ch.20. |
| 19.206 | Source: "Bal pulls them both into a hug kissing them." It is deliberate. |
| 20.001 | "Kenmei's wave and Raizen's lightning" reads distributively; each girl had one. |
| 20.030 | "Arm in one fist" is ordinary idiom, the hand that grips. |
| 20.058 | Porter's rule is the source's wording, and "sygl" as a faction noun is the book's standing usage. |
| 20.188 | "Come over to theirs" is clear: their sygl, the subject of the speech. |
| 21.002 | The next sentence ("slapped the water and called her") makes "tried her" plain. |
| 21.017 | "She" follows "Amelia dropped" in the same sentence, so the nearest referent is Amelia. |
| 21.064 | Ch.20's whip is called while Bal sits watching Sean. Here he is rolling through thorns. The two situations differ. |
| 21.157 | Deliberate restraint, and the next sentence shows the result. More gore cuts against tone. |
| 21.167 | Canon: Bal has a high pain tolerance. Ch.22:133 keeps the thigh sore. |
| 22.002 | Sound arriving after a teleport ("ears caught up") is clear in context. |
| 22.007 | "For it" is the clang, the only event in the sentence. |
| 22.034 | Thad's glowing stone is established in Ch.18 (repeat visits). |
| 22.038 | One flowing scene-change sentence; the meeting lands in the dialogue that follows. |
| 22.047 | Correct: Ch.19 ends at night → Ch.20 next morning ("the day before") → Ch.20:195 "meeting until tonight" → Ch.21 lake → Ch.22 the same day. |
| 22.066 | Bal sees Thad in his room whenever the stone glows (Ch.18:85), so the reference is a visit. |
| 22.142 | The italic *they* is the point: the priests caught that Bal includes himself. |
| 22.203 | Used: Ch.24:83 follows "every second Wednesday" to the brewer, where he buys the gift cask. |
| 22.287 | "The girls on the bed" sets their position in the line itself. |
| 23.078 | "Its palm" is the hand's palm ("a small hand came up"), not the child's. |
| 23.152 | Viridia's cover performance, coached by Lora. It is a lie the scene plays deliberately. |
| 23.164 | Source verbatim ("Exactly how rare is Viridia's gift?"). |
| 23.181 | Logic holds: the guard's route turns at the third street, and passing it shows she isn't going to the Three Boars. |
| 24.076 | Source verbatim ("I honestly didn't realize it either"). |
| 24.083 | Source dialogue ("with them looking at you they won't be looking at us"), protected by the dialogue ruling. |
| 24.090 | Same as 22.203: Bal follows the ale cask to the brewer. That is the pivot. |
| 24.152 | "Them" is Bal's party, inside Bal's own thought. |
| 24.156 | Source: "Bal willingly paying more to keep the man happy". Deliberate. |
| 24.382 | On the brewing day, the day before the meeting, Aleric is "a day early". |
| 24.404 | A small cask Bal can lift in both arms can ride on a boy's shoulder. |
| 25.036 | "Chest" matches "Lora's alchemy chest" in Ch.27:171. Changing it would break that. |
| 25.058 | Generosity in character. No contradiction, and the boy's gaping is the beat. |
| 25.063 | "Too much" is the reason Bal laughs, and "He gaped" shows the face. |
| 25.073 | A barman polishing a glass is a legitimate beat, and it sets up the rag hand he points with. |
| 25.118 | A standard image, clear at the moment. |
| 25.123 | "Set and hard" plus "he understood it" is followed by the stated decision. |
| 25.152 | Source verbatim (the barman's cold rune, src p.921). |
| 25.168 | Source rule ("the purification rune turns any liquid into pure water"), and the purification ruling covers it. |
| 25.206 | Aleric means word reached the priests when they arrived. The syntax supports it. |
| 26.107 | Shock-numbness, which Muse's earlier reading praised ("the water she cannot taste"). |
| 27.028 | "Something … like a cloud" is the image; deleting it orphans "It came and went". |
| 27.137 | Attack near six, waking at a low red sun: about two summer hours, then searching till dark. |
| 27.243 | From the army's side the villagers only cursed, so "no trouble" is accurate. |
| 27.248 | Source: "a quite large head". Affectionate hyperbole. |
| 27.282 | Leaving a horse to graze before going in on foot is ordinary. |
| 27.296 | Bal is athletic (roof jumper), and the source has the same move. |
| 27.301 | Source: "he had pulled back at the last moment so Bal was not able to push the dagger all the way in". |
| 28.134 | The healing is Amelia's *own* blood (Ch.28:115 "her own would heal"), not temple offerings. |
| 28.151 | Source verbatim ("A regular priest does get the healing though"). |
| 28.164 | The beat is new: the postscript, then the letter rolled out of sight. |
| 28.184 | Source: "Bal was not sure what she was talking about, but nodded accepting her instructions." |
| 28.195 | Source simile ("as if he were watching a movie"). The world has TV (Ch.3:127–135; Ch.1:35 "bad television signal"). |
| 29.113 | The italics make it a quotation: *No inheritance gift,* Fern had read. |
| 29.172 | Deliberate: the conversion is the unmeasured moment. A measure would be a new fact. |
| 30.101 | Viridia's laugh at the next line needs "the very temple" detail. |
| 30.140 | The author's line (src: "there's no way to tell to what extent my actions will affect our future"), polished. |

## D: conflicts with an author ruling

| Flag | Ruling |
|---|---|
| 20.034, 20.086, 21.122, 25.162 (right palm and right arm) | 2026-10-20: the whip comes from the RIGHT palm and "blood magic need not come from the sygl hand"; 2026-10-21: the dagger "forms from whichever hand is free (right in Ch.25 …)". The optional explaining line is the earlier triage's M5 (b). |
| 19.218 (Amelia makes them priests without asking) | Source line (src l.795). FRICTION ruling: no invented friction; the girls' choice is shown through the source's beats. Amelia is not a manipulator. |
| 21.267 (give Aren a condition or resistance) | POV ruling: what Bal doesn't witness is reported as the source reports it ("Aren thought for a moment then agreed"). No invented plot. |
| 22.213, 24.012 (Amelia's advance booking and the letter's timing) | 2026-10-21 Winespring ruling (option A, set up in Ch.22 and paid off by "We had your letter"). |
| 30.108 (stage Toma's fate) | 2026-10-21 Toma ruling (option A: Aren took him to the Heir's School to be healed). |
| 30.157 (gaze at "those three beautiful women") | Script wording (src p.186: "Bal stared at those three beautiful women"). The rulings: the ending is unambiguously happy and the book is NA. The final line is LOCKED. |

## Already pending from the earlier triage

| Flag | Covered by |
|---|---|
| 20.211 (war rule, priority item 2) | **B7**, which makes Ch.18:151 add "nor any new priests". The source states both versions (l.777 / l.813), and the plot uses Ch.20's. Muse's opposite direction is not taken. |
| 20.239 ("lake we found last week") | **B8** (Ch.18 "The lake was in the last week of the six"). |
| 24.418 (the dent) | **B11** and **B12**. |
| 20.192 ("a few days of practice") | Earlier **C S4b** (source wording; leave). |
| 23.185 (Viridia finds the Winespring unaided) | Earlier **C S5**, option (b): Xavier's directions in Ch.22. |

## Editor's and agent's notes (not counted above)

| Note | Bucket | Verdict |
|---|---|---|
| Ch.19: consent architecture, girls rushed, Amelia escalates to priesthood | D | FRICTION ruling; the conversions are free choices; source pacing. |
| Ch.19: bedroom joke "withholds an alternative" | A | Source ("not mentioning he could easily create another one"); the author ruled it is a joke. |
| Ch.19: keep the 19.227 war-rule wording in view | pending B7 | See above. |
| Ch.20: Bal's temper and his promise to kill Sean | D | Justified-violence ruling; source line. |
| Ch.20: the recruitment speech hides the costs | C | Part of the agency pattern; leave. |
| Ch.20, Ch.22, Ch.29: summary sentences cataloguing, restatement pairs | B (partly) | CB16, CB78 and CB79 thin them; the rest are left. |
| Ch.21: moral drift (hanging, beheading, "No one threatens my girls") | D | Justified-violence ruling; the memorable line is protected. |
| Ch.21: mobility after wounds | A | High pain tolerance (canon). |
| Ch.22: two briefings play the same; dialogue voices uniform | C | Craft observation; any fix rewrites author dialogue. Leave. |
| Ch.22: hair-as-passport stated three times | B | CB35. |
| Ch.23: the refugee montage repeats its structure | A | It compresses on the third pass already. |
| Ch.24: Lora's errand is a pacing cul-de-sac | C | Source content. Leave. |
| Ch.25: poison clock ("a day from now" vs "six tomorrow night") | A | "A day from now" is Viridia's rough reckoning, and the hour is locked in Ch.26–27. |
| Ch.25: rune convenience | C | 25.165 (b). |
| Ch.26: definition by negation, worth counting | A | voice_wear and tic gates are clean. |
| Ch.27: horses unaccounted; daylight budget | B / A | CB65, CB68; 27.137 is A. |
| Ch.28: fragment pairs; information by announcement | A / C | Gates clean; see the Ch.28 C item. |
| Ch.29: "not understanding" refrain | C | Same as 30.099 and the plant item; source admissions (src: Amelia "Honestly I don't either"). Leave. |
| Ch.30: geography wobble ("home to the school" vs "the temple couch") | A | Muse misread: the big red couch is in the dorm at the school (Ch.30:3), and Aren sent them "home to the school" (Ch.29:243). |
| Ch.30: household framing at the doorframe | D | 30.157. |

## Gate results

Scratch copy: `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/cr3/`. It was reset from
the real manuscript and holds the chapters as both `manuscript/chapter-NN.md` and
`manuscript/chapters/chapter-N.md`, plus `tools/`, `STATE.yaml` and `character-bible.md`. The real files are
untouched.

| Run | style_check | grammar_check | tic_report --gate | voice_wear_check | Words |
|---|---|---|---|---|---|
| CB1–CB84 (81 edits) | clean | clean | clean | clean (strict) | 89,987 |
| CB1–CB84 + earlier B1–B12 | clean | clean | clean | clean (strict) | **90,012** |
