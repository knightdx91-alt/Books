# Muse close reading, Ch.10–18: triage against the text (2026-10-21)

Source: `feedback/muse-close-reading-2026-10-21.txt` (Meta Muse's sentence-by-sentence close reading, the full 118-page copy). This file covers every flag keyed 10.xxx to 18.xxx (219 flags), plus priority-list items 3, 4, 9, 10, 11 and 13. Each flag was found by its quoted excerpt in `manuscript/chapter-10.md` to `chapter-18.md` and checked against `Sygl_Complete.txt` (Ch.10 = src L362–392, Ch.11 L394–539, Ch.12 L541–593, Ch.13 L595–691, Ch.14 L691–703, Ch.15 L704–715, Ch.16 L715–745, Ch.17 L748–766, Ch.18 L767–780), against the STATE.yaml rulings, and against the earlier triage (`evaluations/muse-triage-2026-10-21.md`, fixes B1–B12 still pending). **No chapter or STATE file was edited and nothing was committed.**

Buckets: **A** the text already handles it, or Muse misread it · **B** surgical fix, story unchanged · **C** author's call · **D** conflicts with an author ruling.

## Priority-list items in this range

| # | Item | Verdict |
|---|---|---|
| 3 | 18.095, the dropped negative ("had stopped at not liking") | **B.** Muse is right: as written the sentence says the opposite of the source ("began beating and killing"). Fix: `had gone past not liking.` |
| 4 | 17.157, juggling "learned as a boy" with no left hand | **B.** The boyhood juggling is in the source ("as he had learned to do when he was younger"), so it stays. The fix reconciles it with the hand: `He had learned it as a boy, with one hand. Two made it easy.` (+1 word; this also covers 17.158 "His hands had not forgotten how"). |
| 9 | 15.119, originator ranking vs Ch.11 | **Already pending (B6)**, "lowest of the four". Ch.11:59 puts Amelia below all of them; B6 makes Raizen lowest of the established four. No new fix. |
| 10 | 14.129, ring terms vs the jeweler's card (Ch.13:179) | **B.** Ch.14 drops "shape" and "after every use". The fix restores both. The wording avoids the Ch.13 phrase, which tripped voice_wear on the first draft. |
| 11 | The 72-hour flowers (17.037–038 → Ch.18) | **Already pending (B9)**, the Ch.18 line where Ms. Summers helps Lora brew the two potions inside the 72 hours. No new fix. (17.037 is not a separate flag in the chapter list.) |
| 13 | 12.113, "That honestly is all she told me" | **C** (see C3). It is the source's line, but it is untrue on the page (Amelia told Bal that Viridia likes him, Ch.11:223/231), and the next line ("I'm glad she did") only makes sense if Amelia told him. |

## Counts

219 flags. Merged duplicates are counted under the flag they repeat, never twice.

| Bucket | CLARITY | LOGIC | TELLING | REPETITION | IMAGE | RHYTHM | DIALOGUE | CONTINUITY | POV | GRAMMAR | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B (new fixes) | 28 | 11 | 4 | 10 | 10 | 1 | 1 | 6 | 4 | 4 | **79** |
| B (already pending: B4, B5, B6) | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | **3** |
| B (optional cuts) | 0 | 0 | 2 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | **6** |
| C | 2 | 6 | 3 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | **13** (11 items) |
| D | 1 | 0 | 4 | 0 | 1 | 0 | 2 | 1 | 2 | 0 | **11** |
| A | 33 | 16 | 10 | 9 | 8 | 8 | 11 | 3 | 2 | 7 | **107** |
| All | 64 | 34 | 23 | 22 | 19 | 10 | 14 | 12 | 10 | 11 | **219** |

Per chapter (B new / pending / optional / C / D / A): Ch.10 8/0/0/1/1/14 · Ch.11 9/0/2/6/0/15 · Ch.12 4/1/1/1/1/11 · Ch.13 22/0/2/3/8/47 · Ch.14 11/1/0/1/0/4 · Ch.15 7/1/1/1/0/4 · Ch.16 10/0/0/0/0/6 · Ch.17 5/0/0/0/0/3 · Ch.18 3/0/0/0/1/3.

**Word count.** The 78 B edits (covering 79 flags) come to **−78 words** net, inside the −120/+60 budget. On the scratch copy: baseline 90,082 → **90,004** with these fixes, and **90,029** with the earlier B1–B12 applied as well. The optional cuts total −44. Taking all of them would put the book at 89,985, under the 90,000 floor, so take at most ~25 words of them (or fewer if other ranges also cut).

Most of the A verdicts on DIALOGUE, TELLING and REPETITION flags rest on one fact: the flagged line is the author's own dialogue or beat, nearly verbatim from the source, and the ruling keeps it ("Author's dialogue is the BASE … keep what each line says"). Where a polish kept the meaning, I put it in B instead.

## B: apply-ready fixes

Each old string occurs exactly once in its chapter file (verified by script). Words = net change. 14.096 needs two edits, and both must be applied. Five fixes were reworded after the first gate run (see the gate section). The wording below is the final, gate-clean version.

| Flag | Cat. | Ch. | Exact current text | Replacement | Words |
|---|---|---|---|---|---|
| 10.031 | LOGIC | 10 | `When she was done she went back over the ones at the bottom of the pile that she had missed, until the whole pile glittered.` | `When she was done she stirred the pile with a fry and salted the ones she had missed, until the whole pile glittered.` | -2 |
| 10.110 | LOGIC | 10 | `and Amelia would be wherever Bal was.` | `and Amelia was mostly wherever Bal was.` | +0 |
| 10.152 | CLARITY | 10 | `He didn't waste anything after that.` | `He didn't waste a word after that.` | +1 |
| 10.168 | POV | 10 | `she had heard them and come anyway.` | `she must have heard them and come anyway.` | +1 |
| 10.201 | GRAMMAR | 10 | `He was with Kenmei's army, when he was younger.` | `He was with Kenmei's army when he was younger.` | +0 |
| 10.210 | CLARITY | 10 | `Bal was about to ask why on earth anyone wouldn't have practiced with her.` | `Bal was about to ask why on earth nobody had wanted to practice with her.` | +1 |
| 10.232 | CLARITY | 10 | `waited until he had it, then drew back.` | `waited until he had the parry, then drew back.` | +1 |
| 10.244 | CLARITY | 10 | `Bal learned a little. Lora` | `Bal learned a little about her. Lora` | +2 |
| 11.002 | RHYTHM | 11 | `the same mark Bal wore on his, and below the sweater was a short black skirt.` | `the same mark Bal wore on his. Below the sweater was a short black skirt.` | -1 |
| 11.048 | GRAMMAR | 11 | `So many soldiers in one place was a thing Bal had no practice at.` | `Never in his life had Bal seen so many soldiers in one place.` | -1 |
| 11.102 | CLARITY | 11 | `Only this morning he had met this in the library, in neat print.` | `Only this morning he had met armies like this one in the library, in neat print.` | +3 |
| 11.105 | IMAGE | 11 | `He knew that already, the same as he knew his own name.` | `He knew that already.` | -8 |
| 11.125 | CLARITY | 11 | `It seemed to sit up and want attention.` | `The likeness seemed to sit up and want attention.` | +1 |
| 11.147 | REPETITION | 11 | `for twelve years. He had been six, twelve years ago.` | `for twelve years.` | -7 |
| 11.206 | CLARITY | 11 | `and two whole sets belonged to High Priests` | `and two whole sets of rooms belonged to High Priests` | +2 |
| 11.210 | GRAMMAR | 11 | `Looking out at it, Bal believed them all.` | `Looking out at it, he could believe all twelve.` | +1 |
| 11.265 | CLARITY | 11 | `already training his own army to do the same to them.` | `already training his own army to come after them.` | -2 |
| 12.013 | CLARITY | 12 | `It went, and returned full and steaming.` | `The silver went, and returned full and steaming.` | +1 |
| 12.032 | LOGIC | 12 | `Nobody ever sat at it but Bal and one Tempus girl choosing to sit with him, and the whole school could see it from every bench in the hall.` | `Nobody sat at it but Bal and one Tempus girl choosing to sit with him, and the whole hall could see it.` | -7 |
| 12.043 | IMAGE | 12 | `Her mouth curled up at one side and stayed that way.` | `Her mouth curled up at one side.` | -4 |
| 12.069 | LOGIC | 12 | `having dinner with everybody else, it might` | `having dinner, it might` | -3 |
| 13.019 | REPETITION | 13 | `brown trousers and a brown jacket with patches` | `brown trousers and a jacket with patches` | -1 |
| 13.038 | CLARITY | 13 | `Bal put up a hand and stopped, and waved for them to go first.` | `Bal stopped, put up a hand, and waved for them to go first.` | -1 |
| 13.049 | CLARITY | 13 | `He guessed she was not used to being one of a group of anything.` | `He guessed she was not used to being part of a group.` | -2 |
| 13.084 | CLARITY | 13 | `planned to go on that way the whole five.` | `planned to go on that way the whole five miles.` | +1 |
| 13.107 | REPETITION | 13 | `Bal's eyes went to Viridia again.` | `Bal looked over at Viridia.` | -1 |
| 13.158 | REPETITION | 13 | `Lora walked beside Bal with her hands back in her pockets.` | `Lora walked beside Bal.` | -7 |
| 13.185 | REPETITION | 13 | `and kept it hidden there. The tops of her ears had gone red.` | `and kept it hidden there.` | -8 |
| 13.271 | LOGIC | 13 | `Her voice was steadier than it ever was when she talked to people.` | `Her voice was steadier than it ever was in company.` | -3 |
| 13.287 | CLARITY | 13 | `The page-turning had stopped on both sides.` | `Neither girl was turning pages now.` | -1 |
| 13.351 | TELLING | 13 | `with a sunrise stitched on the breast. Bal guessed it was a uniform.` | `with a sunrise stitched on the breast.` | -6 |
| 13.356 | CLARITY | 13 | `Lora stepped forward before Bal could.` | `Lora stepped forward before Bal could speak.` | +1 |
| 13.380 | IMAGE | 13 | `She set her jaw and jerked her head at the counter.` | `She jerked her head at the counter.` | -4 |
| 13.386 | TELLING | 13 | `from one girl to the other and back, and stayed a second longer than it needed to. Then` | `from one girl to the other and back. Then` | -9 |
| 13.392 | IMAGE | 13 | `Lora kept making small exasperated noises through her nose.` | `Lora kept huffing through her nose.` | -3 |
| 13.415 | IMAGE | 13 | `Lora blushed to the roots of her hair.` | `Lora blushed.` | -6 |
| 13.430 | REPETITION | 13 | `She stopped, and the tapping stopped.` | `She stopped mid-tap.` | -3 |
| 13.434 | TELLING | 13 | `Lora's face changed.` | `Lora grinned.` | -1 |
| 13.480 | IMAGE | 13 | `showed white on the back, she glowed.` | `showed white on the back, she beamed.` | +0 |
| 13.505 | TELLING | 13 | `Viridia started, and stopped, and he watched her get there.` | `Viridia started, and stopped.` | -6 |
| 13.528 | REPETITION | 13 | `Viridia's chin came up. Something mischievous got into her face and made itself at home.` | `Something mischievous got into Viridia's face.` | -9 |
| 13.551 | DIALOGUE | 13 | `"You picked a good one. I'm glad we can help her out."` | `"You picked a good one. I'm glad we can help her out," Bal said.` | +2 |
| 14.021 | POV | 14 | `Bal remembered the boys in Lora's town` | `Bal remembered what Lora had said about the boys in her town` | +5 |
| 14.023 | CLARITY | 14 | `they were not getting another turn.` | `they were not getting another turn at her.` | +2 |
| 14.038 | CLARITY | 14 | `with a name inked neatly on the cover` | `with Viridia's name inked neatly on the cover` | +0 |
| 14.040 | IMAGE | 14 | `and her face jumped.` | `and she jumped.` | -1 |
| 14.047 | CONTINUITY | 14 | `with fewer of its authors in the room.` | `with its author out of the room.` | -1 |
| 14.096a | LOGIC | 14 | `Bal sat down beside Amelia.` | `Bal dropped the pack on the rug and sat beside Amelia.` | +6 |
| 14.096b | LOGIC | 14 | `Bal eased the pack off onto the rug and opened it.` | `Bal pulled the pack to him and opened it.` | -2 |
| 14.100 | LOGIC | 14 | `That left one thing in the bottom of the bag` | `That left one gift in the bottom of the bag` | +0 |
| 14.112 | CLARITY | 14 | `Nothing spilled.` | `No tears spilled.` | +1 |
| 14.129 | CONTINUITY | 14 | `had promised it could move the earth, briefly, and warned that it cost a lot to recharge.` | `had promised it could shift and shape the ground for a short while, and warned that it needed a costly recharge after each use.` | +7 |
| 14.145 | LOGIC | 14 | `He had worn the corner smooth on the road, without meaning to,` | `He had rubbed at the corner on the walk home, without meaning to,` | +1 |
| 14.175 | GRAMMAR | 14 | `would have taken him for stabbed.` | `would have thought him stabbed.` | -1 |
| 15.013 | CLARITY | 15 | `left to spend on talking, and Lora, three places down the line, watched him with` | `left to spend on talking. Lora, three places down the line, watched Bal with` | -1 |
| 15.076 | POV | 15 | `It was the question she had been hoping he would skip` | `It was plainly the question she had been hoping he would skip` | +1 |
| 15.081 | CLARITY | 15 | `So the school would make it a rule. Probably.` | `Going by the teachers' faces, the school would make it a rule.` | +3 |
| 15.098 | LOGIC | 15 | `and did not come out again.` | `and did not come out again for hours.` | +2 |
| 15.101 | CLARITY | 15 | `Bal took the old couch with the history of Raizen's wars.` | `Bal took the old couch and the history of Raizen's wars.` | +0 |
| 15.121 | CLARITY | 15 | `This was all they had left,` | `Going after her followers was all they had left,` | +3 |
| 16.057 | CLARITY | 16 | `Bal tried Amelia.` | `Bal faced Amelia.` | +0 |
| 16.077 | CLARITY | 16 | `how long they would keep once they were.` | `how long they would keep once cut.` | -1 |
| 16.105 | CONTINUITY | 16 | `Clear of the castle,` | `Clear of the town,` | +0 |
| 16.112 | CONTINUITY | 16 | `Everyone had their weapon out before they had finished standing.` | `Every weapon was out before they had finished standing.` | -1 |
| 16.135 | CLARITY | 16 | `She was already reaching for whatever it was inside the band that she had to reach for.` | `She was already reaching for whatever lay inside the band.` | -7 |
| 16.166 | REPETITION | 16 | `he roared and swung harder. Bal circled. The axe` | `he roared and swung harder. The axe` | -2 |
| 16.197 | IMAGE | 16 | `dragged his good wrist across his eyes` | `dragged his sword wrist across his eyes` | +0 |
| 16.200 | CONTINUITY | 16 | `and her left hand pressed to her stomach.` | `and her eyes on the fight.` | -2 |
| 16.266 | LOGIC | 16 | `The crossbows, which none of them knew how to use.` | `The crossbows, which none of them knew how to use, so they left them.` | +4 |
| 16.349 | IMAGE | 16 | `planted herself over Bal` | `stood over Bal` | -1 |
| 17.041 | REPETITION | 17 | `Pretty much. The flowers are rare, and what goes in with them isn't cheap either.` | `Pretty much. What goes in with them isn't cheap either.` | -5 |
| 17.047 | CLARITY | 17 | `She was already halfway into that shop in her head.` | `She was already halfway into Ms. Summers' shop in her head.` | +1 |
| 17.079 | CLARITY | 17 | `what she'd make in a month selling the others.` | `what she'd make in a month selling her other potions.` | +1 |
| 17.139 | CLARITY | 17 | `spun her back on all of them` | `spun her back to all of them` | +0 |
| 17.157 | CONTINUITY | 17 | `He had learned it as a boy. His hands had not forgotten how.` | `He had learned it as a boy, with one hand. Two made it easy.` | +1 |
| 18.095 | LOGIC | 18 | `had stopped at not liking.` | `had gone past not liking.` | +0 |
| 18.143 | CLARITY | 18 | `to share news and gossip, and to drink, Bal suspected.` | `to share news and gossip. And to drink, Bal suspected.` | +0 |
| 18.195 | REPETITION | 18 | `Amelia had smiled at him. The smile came slowly.` | `Amelia had smiled at him, slowly.` | -3 |
Merged into the rows above: 13.529 (with 13.528) and 15.082 (with 15.081).

**Already pending from the earlier triage (do not duplicate):** 12.012 breakfast at dinner = **B4** · 14.029 "nearly two hours" = **B5** · 15.119 ranking = **B6** · priority 11, the 72-hour flowers = **B9**. All four were gate-tested together with the new fixes and stay clean.

Notes on the less obvious fixes:
- **18.095.** Source L767–780: "The villagers, who had already been against those bearing the blood sygl began beating and killing…". "Gone past" restores the source's meaning.
- **17.157.** The source has him learn to juggle "when he was younger", and canon has him one-handed until he was eighteen. One-handed juggling follows from those two facts and adds nothing new.
- **14.129.** Restores the Ch.13:179 card terms: move *and shape* the earth, briefly, recharged after *every* use, at a real magykal cost.
- **14.096.** Bal sat through the whole confession still wearing the pack (Ch.14:37 → :85). The fix gets the pack off before he sits.
- **16.105.** The party is at Whitehaven's town limit, not the castle. This was a real slip.
- **16.112.** Amelia carries no weapon ("I am my own weapon"), so "everyone" was wrong.
- **12.032.** "Nobody ever sat at it" contradicted Ch.12:17, where Amelia ate at the table the day before. The fix also drops "from every bench in the hall".
- **12.069.** Amelia would be eating at Bal's table, not "with everybody else". The cut keeps the source's "others seeing her in here".
- **13.271.** "When she talked to people": she is talking to Viridia. The fix gives "in company".
- **13.551.** Adds the speaker tag. The source gives the line to Bal.
- **10.168.** Bal can only infer that Lora had heard the stories (source: "surely circulating").
- **15.076.** Viridia's hope is the source's, but in Bal's POV it reads as his inference ("plainly").
- **13.158.** Lora's hands in her pockets, a third time in 70 sentences, is cut. Under the no-tics law a repeated gesture is a liability.
- **13.185, 13.415.** Two of the chapter's five blush notes are gone. 13.415 returns to the source's plain "Lora blushed."

## B: optional cuts (lowest value; together they would breach the word floor)

All six are gate-clean on top of the full B set. Together they come to −44 words, and taking all of them would put the book at 89,985. **Take at most about 25 words of them.** The best value is 13.025 and 11.341.

| Flag | Cat. | Ch. | Exact current text | Replacement | Words |
|---|---|---|---|---|---|
| 13.025 | REPETITION | 13 | `He was in his boxers. Only his boxers, and the corridor was cold too.` | `He was in his boxers.` | −9 |
| 11.341 | TELLING | 11 | `"Thank you for asking." Her voice had gone small. "Just give me a little time."` | `"Thank you for asking. Just give me a little time."` | −5 |
| 13.256 | REPETITION | 13 | `No matter what." She was quiet again. "Joking around` | `No matter what. Joking around` | −4 |
| 11.329 | RHYTHM | 11 | `Somewhere, in some drawer or under some loose stone in the world, there was a book,` | `Somewhere in the world there was a book,` | −8 |
| 15.142 | REPETITION | 15 | `"I hope I don't have to offer it yet. If it comes to that, I will.` | `"If it comes to that, I will.` | −9 (cuts a repeat inside the source's own dialogue) |
| 12.063 | TELLING | 12 | `It was hard to argue with her when she was right.` | `Bal nodded.` | −9 (the source has "Bal nods") |

Note: 12.063 was in the first B draft. Removing it changes Ch.12's length, and so its simile rate, which already sits near the 4.0/1k ceiling. It tested clean in the optional set, but recheck Ch.12 if other fixes shorten that chapter.

## C: author's call

**C1. 12.113 (priority 13), "That honestly is all she told me."** This is the source's line (src L541–593: "that's honestly all she told me"). On the page it is untrue. Amelia told Bal "I think she really does like you" and "she does say some interesting things about you" (Ch.11:223, 231), and the source's own narration says Bal "realises that Amelia had been telling the truth when she said Viridia liked him". The next line, "I'm glad she did, because otherwise I might never have worked up the courage", only makes sense if Amelia told him.
- (a) Leave it as Bal's white lie.
- (b) Polish it to a true line with the same reassurance: `"Hey," he said. "It's okay. She only said you liked me. That's all, I promise."`
- (c) Cut the denial and keep "I promise".
- **Recommendation: (b).** It keeps the speaker, the placement and the reassurance, and it makes "I'm glad she did" coherent. It stays a sweet beat, with no "cost" or friction added (see D for 12.115).

**C2. 13.470, Soren "plainly" knows Norheart is Bal's surname.** Bal never gives her his name. Amelia did speak "Balthazaar Norheart" publicly at the claiming (Ch.6:175), but Soren is in New Spring. Muse's priority item 7 pairs this flag with 6.195, and item 7 is outside this range.
- (a) Leave it. The claiming was public, so word could have travelled.
- (b) Make it Bal's inference: `Norheart was his own last name, and plainly the story of the claiming had reached New Spring.` (+6, not gate-tested).
- (c) Soften it to `and she seemed to know it.`
- **Recommendation:** decide together with priority item 7. If 6.195 stays as it is, take (b).

**C3. 11.123 + 11.136, one man laid every stone of a canyon-filling temple in twelve years.** This is source content ("Every stone was laid by his hand"; "twelve years"). Any fix would add magic aid or shrink the temple. **Recommendation: leave.** It is Amelia's devotional telling of Peter's story.

**C4. 11.231 + 11.233, the ring's "various other things" / "Bal caught her meaning".** Duplicates the earlier triage's C item M8b (source line, flirtatious beat). **Recommendation: leave**, as before.

**C5. 11.076, what "ranked" means.** Source dialogue ("ranked in a way is the best way I can put it"). Defining a basis for the ranking would be a new worldbuilding fact. **Recommendation: leave.** B6 already fixes the ranking's continuity.

**C6. 11.165, the scope of Amelia's "look impartial".** This is the source's rule (src L394–539). Bounding it would add a new rule. (The related flags 11.167 and 11.212 are A: the rule covers her *lesser* followers, and promoting priests is exactly how she avoids dealing with them directly.) **Recommendation: leave.**

**C7. 10.187, the four-and-a-half-foot rapier.** Source detail; duplicates the earlier triage's C item 10.5. **Recommendation: leave.**

**C8. 13.211, no prices shown.** Source: "Bal checked the price". Giving a figure is a new fact. **Recommendation: leave.**

**C9. 13.545, the alchemist "doesn't feel well".** This is the source's wording. A named ailment would be new backstory, and Ch.16:65–67 already shows her frail ("not up to it this year"). **Recommendation: leave.**

**C10. 14.197, "his beautiful Vampire Goddess".** This is the author's own closing epithet (src: "crawls in beside his Beautiful Vampire Goddess"). Muse calls it possessive and fandom-flavoured.
- (a) Keep it.
- (b) `He climbed in beside her` (−3).
- **Recommendation: (a), keep.** It is the author's chapter close.

**C11. 15.117, the war analysis given as summary, not scene.** In the source it is Bal's direct speech, and Viridia stays silent. Muse wants a dialogue argument with Viridia, which would invent friction.
- (a) Leave the summary.
- (b) Recast Ch.15:109's summary as Bal's direct speech, as in the source, with no Viridia argument.
- **Recommendation: (a).** Her silence after it is the source's beat, and (b) is more than a surgical fix.

## D: conflicts with a ruling

| Flag | Muse wants | Ruling |
|---|---|---|
| 10.115 | Make Bal's "Viridia wouldn't mind" uncertain; "price" Amelia's manipulation | 2026-10-20 tone ruling: Amelia is not a manipulator. Same as the earlier triage's D item 10.1. |
| 12.115 | Bal should admit he learned of Viridia's feelings "the wrong way" | 2026-10-20 FRICTION ruling (no invented friction or Bal flaw); "I like you too" scene as the source has it. |
| 13.248, 13.254, 13.259, 13.269, 13.296, 13.297 | Add particulars to the girls' backstories (a named arranged marriage, the deciding body, a training image, a sample taunt, a petty act) | "Do NOT invent plot, friction, motives, quirks or backstory." These are the source's bookstore monologues. |
| 13.270, 13.272 | Replace "an extension of who I am" and cut the dolls line | Dialogue ruling: keep what each line says. Both are Lora's source lines nearly verbatim. |
| 18.055 | Give Bal an arrow shirt too | 2026-10-20 arrow-shirt ruling: "the girls wear them on later jobs". |

## A: already fine / Muse misread (one-line proof)

| Flag | Proof |
|---|---|
| 10.037 | "Turn the edge" of a blade is the standard idiom for deflecting it. Source: "repel a longsword". |
| 10.059 | Callback to Ch.9:123: "All the purple had drained out … He was the color of the chalk." |
| 10.086 | "One" refers to "my hands" in the sentence just before. |
| 10.090 | Bal's "Hopper" is already its own paragraph. The run-on is a PDF artifact. |
| 10.106 | The preceding lines spell out the exchange (meat plus time near Amelia). |
| 10.131 | Source dialogue verbatim; it reads clearly when spoken. |
| 10.167 | "Nobody else" means beyond the two of them. Viridia came with him. |
| 10.193 | The gripping/holding contrast (tense vs relaxed) is the point. |
| 10.197 | "There" refers back to "where hers had been", one clause earlier. |
| 10.205 | The pluperfect "had pulled a spear off the next rack over" already places her. |
| 10.213 | The areas are set up at Ch.10:97: "six training areas marked out … in packed sand". |
| 10.239 | Muse's proposed fix is the current text. |
| 10.257 | Remembering which peg is plausible. |
| 10.269 | Idiomatic voice. |
| 11.016 | "A little at a time" is idiomatic. Source: "faded slowly". |
| 11.082 | The two lines before give the reason (fights are ranked; his only targets are her or Naisura). |
| 11.095 | Source dialogue. Each clause adds a step (theft, possession, insult). |
| 11.134 | The exception is on the page: Peter gave his whole lifeblood "so he could live with me forever". |
| 11.142 | Amelia's own speech, from the source ("hurt him deeply"). |
| 11.167, 11.212 | The rule covers "lesser followers". Making priests is the channel the rule requires. |
| 11.176 | Source, and clear ("before she killed anybody"). |
| 11.238 | Bal's free indirect view of how he must look to them. |
| 11.247 | Grammatical. Source description. |
| 11.249 | The antecedent is "He had clear blue eyes", the sentence before. |
| 11.252 | Grammatical reported speech. |
| 11.257 | Flagged as selective just before ("more than he would tell the commander, though not everything"). |
| 11.278 | The glow lasts until he comes and answers in person, which is coherent (source mechanics). |
| 11.328 | Comic irony, from the source ("he would have no choice now"). |
| 12.001 | Bal reads it from her reaction (her head comes up, she smiles). Not a POV break. |
| 12.010 | Clear. |
| 12.031 | Deliberate pivot. |
| 12.074 | The groping hand is answered by the napkin Bal passes her. |
| 12.079 | Bal's reading of her face. Source: "nervous look", which the next sentence needs. |
| 12.084 | Source dialogue ("some priest stuff"). |
| 12.091 | Source dialogue, a joke. |
| 12.117 | Source dialogue. In context it plainly means Bal's teasing. |
| 12.120 | Clear, and it is a good closing beat. |
| 12.125 | Lora sat alone on a stretch of bench (Ch.12:5), so "her bench" is exact. |
| 12.126 | The afterglow blur is deliberate. |
| 13.003 | Idiomatic. |
| 13.032 | Comic sprawl; deliberate. |
| 13.033 | Source ("still had pink in their cheeks"). |
| 13.064 | Deliberate contrast ("more slowly than he had gotten into it"). |
| 13.072 | Sets up "He wanted her to hear it from him anyway". Source. |
| 13.091 | Source ("so many requests"). It is consistent with 13.370 (see below). |
| 13.093 | The context is her speech. |
| 13.140 | A sound beat on purpose. The image follows at Ch.13:119. |
| 13.175 | Author's dialogue verbatim. |
| 13.180 | Author's dialogue verbatim. |
| 13.183 | Author's dialogue verbatim; Viridia's "He did call you beautiful" depends on it. |
| 13.184 | Comic staging of the source's "hiding her blushing face". Not an error. |
| 13.189 | Author's dialogue verbatim ("I just tell the truth"). |
| 13.195 | Source summary of the seller's pitch. |
| 13.202 | Bal is a rune student (Rune Working from Ch.9). Checking a rune is within his skill. |
| 13.214 | Price checked, nothing wrapped, ring pocketed while the girls were busy at the next window. Plausible. |
| 13.226 | Plain inventory, from the source. |
| 13.275 | Source verbatim ("begged me to enter"). |
| 13.295 | Bal is behind the shelf and can only hear. A "noise" is right. |
| 13.340 | Source ("echoing in the bookstore"). |
| 13.346 | Source wording ("not like anyone else"). A softer polish ("not like") tripped tic_report: "i'm not like" ×3 book-wide. |
| 13.348 | Source ("large ornate sign"). |
| 13.362 | Source verbatim. |
| 13.370 | Lora knows the team route (she explains it at Ch.13:87). Her surprise is only that non-members needn't join first. Consistent. |
| 13.377 | Source dialogue. |
| 13.378 | Source ("Lora's head dropped at the mention of a team"). |
| 13.381 | It is italicised in the manuscript (*Go.*), marking Bal's reading of the gesture. |
| 13.395 | One beat. Source: "shakes her head in amusement". |
| 13.399 | Author's dialogue verbatim ("You want this Lora, it's okay"). |
| 13.411 | Clear: Viridia asks him, and he keeps his attention on Lora. |
| 13.412 | Author's dialogue verbatim. |
| 13.433 | Author's dialogue verbatim. |
| 13.440 | Author's dialogue verbatim, colloquial. |
| 13.449 | Source ("talking quietly to each other"). |
| 13.463 | Muse misreads. A surname gives "Amelia" cover, not more exposure. Source reasoning. |
| 13.467 | Source ("Praying Amelia wouldn't mind"). |
| 13.469 | Source ("Soren raises an eyebrow"). |
| 13.478 | The cards borrowing the maker's hand reads as magic. Nothing contradicts it. |
| 13.481 | Source verbatim. |
| 13.508 | Comic beat (source: "she says laughing again"). Harmless. |
| 13.521 | Source dialogue. |
| 13.538 | Callback to his dropped jaw (source "Bal's mouth dropped open"). |
| 13.557 | Source verbatim. |
| 13.561 | Muse is wrong. Viridia did meet Lora through Bal: Lora joined *Bal's* rack in Warfare (Ch.10:117). |
| 13.562 | Source verbatim ("shyly smiled back"). |
| 13.564 | Source verbatim. |
| 13.567 | Source dialogue. |
| 14.060 | Acceptable free indirect speech. |
| 14.079 | Reads as intended (friends who aren't there only for gain). Source wording. |
| 14.104 | Source verbatim, a playful lilt ("They give gifts?"). |
| 14.177 | Source: "They sat talking for awhile". The summary is a deliberate choice. Expanding it would add words and dialogue. |
| 15.042 | Whimsical but clear. |
| 15.080 | "*expel*" is italicised, marking the word. |
| 15.092 | The backfill IS the beat ("Bal had put it there that morning…"). Source: "When Bal had gotten up that morning he had added…". Rooms appear by picturing (Ch.7:23). |
| 15.131 | "Pulled" is set up at Ch.13:41 ("all the teachers got pulled by the originators"). Source dialogue. |
| 16.041 | True. Bal was not in the forest. Hopper is only reported (Ch.10) until Ch.16. |
| 16.067 | "The alchemist" is the antecedent in the same sentence. |
| 16.131 | Bal has not yet seen Viridia's power ("Until that day Bal hadn't seen Viridia use her own power", Ch.18:73). |
| 16.146 | Bal is charging the leader. Viridia's account at Ch.16:279 supplies the rest ("Hopper had … gone for the crossbows first"). |
| 16.178 | Source has the gash across the back, and canon gives Bal high pain tolerance. Lora's salve follows. |
| 16.279 | Author ruling (2026-10-20): the ring stays on Heath's hand so its pair feels his heart stop. Paid off at Ch.21:119. |
| 17.003 | Two different actions (shedding over time; edges sheared clean). Source. |
| 17.086 | They followed the river in and follow it back out. Source. |
| 17.094 | The masking is planted: river noise ("The water went on talking", :77), the birds gone silent, and Amelia's "I honestly never heard it… I was listening to Lora" (:135, source). |
| 18.010 | The joke works: a whole dorm for a "kind" of one. |
| 18.082 | The sentence itself places her ("had not moved from the bank"). |
| 18.094 | "For being afraid" (= because of it) is idiomatic. |

## Gate results (scratch copy)

Scratch copy: `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/cr2/`. It holds the whole manuscript as `manuscript/chapter-NN.md` and as `manuscript/chapters/chapter-N.md`, plus `tools/`, `STATE.yaml` and `character-bible.md`. Gates were run from that folder.

| Gate | B fixes only (90,004w) | B + earlier B1–B12 (90,029w) | + all optional cuts (89,985w) |
|---|---|---|---|
| `style_check.py --dir manuscript` | clean | clean | clean |
| `grammar_check.py --dir manuscript` | clean | clean | clean |
| `tic_report.py --gate` | clean | clean | clean |
| `voice_wear_check.py` | clean (strict) | clean (strict) | clean (strict) |

The first gate run failed, and these rewordings fixed it:
- **tic_report** found 17 new trigrams at 3× book-wide. Reworded: 11.048 ("Bal had never" → "Never in his life had Bal"), 11.210 ("every one of them" → "all twelve"), 12.013 ("The plate went" → "The silver went"), 13.107 ("Bal turned to Viridia" → "Bal looked over at Viridia"), 13.271 ("than Bal had ever" → "in company"), 13.551 (tag moved to the end), 14.021, 14.096a, 14.145 ("the whole way" → "on the walk home"), 15.081 ("a school rule" → "make it a rule"), 16.057 ("Bal turned to Amelia" → "Bal faced Amelia"). 13.346 ("i'm not like" ×3) was withdrawn to A.
- **voice_wear** failed on "move and shape the earth briefly" (14.129 echoing Ch.13). Reworded to "shift and shape the ground for a short while".
- **style_check** found Ch.12 over the simile ceiling (4.4/1k) because a first draft of 12.069 used "like everybody else". Now it is a cut, and 12.063 moved to optional.
