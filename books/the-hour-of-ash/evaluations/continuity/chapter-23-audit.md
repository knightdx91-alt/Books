# Continuity Audit: Chapter 23 "An Inn on the Appian Way" (run 2, per-chapter drift audit)

**Date:** 2026-10-23
**Mode:** MANUSCRIPT AUDIT. Ch.23 is audited as it stands on disk, after the writer, dialogue-polish, hook-craft and disruptor passes. The file has 320 lines and md5 `be315dc2…`. Every quote below is taken from that page.

**Checked against:**
- Ch.1–22 by targeted greps. These passages were read in full:
  - Ch.12, the onion and the telling at the stream;
  - Ch.15, HEAT 1 l.526–568;
  - Ch.16, the ridges and the marks;
  - Ch.19, the inn loft l.159–185;
  - Ch.22, the court l.150–300, the steps l.404–440 and the arrival l.8–34.
- ENTITY_STATE.yaml as of Ch.22, read only. The parallel Ch.23 UPDATE was not touched. Its new CH23-1…CH23-4 were read and are cross-referenced below.
- outline.md: Ch.23 and its ledger row; Ch.24 for forward collisions.
- foundation.md: §6e, §9 and §10.
- STATE.yaml guardrails and every AUTHOR-* decision (CP2-2, CP2-3, CP3-3, CP4-1, CP4-2, END-1).
- voice-dna.md §5.
- character-bible.md:
  - the Valens card (Ch.22 block);
  - the Acca card;
  - the Ch.23 walk-on block;
  - At-risk after Ch.5, Ch.15 (Heat 1), Ch.19, Ch.21, Ch.22 (including the Ch.23 guards) and Ch.23.
- The Ch.23 dialogue, hook and disruption reports.

**Citations:** `l.NN` means a line in `manuscript/chapters/chapter-23.md`. Other chapters are cited as `ChN l.NN`.

**Total findings: 42. CRITICAL: 5 | WARN: 19 | INFO: 18**

**Speech is protected.** Dialogue sits at 15.4% against a 15% floor, so no fix below cuts a spoken word. Every fix is a cut or a swap in narration. If all CRITICAL and WARN fixes are applied, narration drops by about 290 words and the dialogue share rises to about 16.5%. The style count falls from 3,821 to about 3,530; there is no per-chapter floor, and nothing needs padding back. Each replacement string was grepped against Ch.1–22 and appears in no earlier chapter. None restores a string that the dialogue-polish or disruptor cut, including "I'm the size of a wine jar", "A small one", "These days I was always hungry", the five-years paragraph and the rain-as-mood lines.

---

## Summary

**The chapter delivers the outline:**
- the blanket open (8 words);
- the bad supper, the landlady and the rain;
- the five words (l.180) and the onion memory, unexplained and in fresh words against Ch.12 and Ch.22;
- HEAT 2, in which she leads and he is the one held;
- the door-side turn;
- the long fade into rain and fleas.

**The book laws hold:**
- no foreshadowing;
- no tomb, and no reserved door;
- the child is "it", never a citizen;
- no who-pays or "Whose …?" question;
- no Mara laugh and no mouth channel;
- no hand on the belly and no heel;
- no backlit doorway and no lying-awake close;
- no "So…" opener and no teeth.

**Timeline, geography and history check out.** Forum Appii sits at the 43rd mile, and the canal and towpath ran about 19 miles beside the road to near Tarracina, so a flooded towpath and a barge there in late-April rain are plausible. Tarracina to Sinuessa is about 44 miles, which is two days by mule carriage, or three in rain. The Horace details match Satire 1.5.

**What fails is rebuilding.** The chapter reconstructs three earlier set pieces:
- HEAT 1's road comparison and its undressing sequence;
- the Ch.19 inn-loft sleep close;
- Ch.22's sound-reading at night and the bent-over-the-child phrasing of its laugh scene.

It also uses the closed "the color of [thing]" shape and contradicts itself on the colour of the scars. Below CRITICAL there is a cluster of narrated-state counts over the ≤3 rule: Valens downcast, his hands on the blanket, his door-vigilance, Acca and the hen, and Mara's hunger.

---

## CRITICAL ISSUES (must fix before the evaluator)

### [C-01] "the color of lentil soup": the CLOSED "the [color] of [thing]" shape, a third use
- **Audit:** NO TICS / closed sentence shapes.
- **Evidence:** l.24: "Beside it ran the canal, the color of lentil soup, with mules on the towpath hauling barges at a walk."
- **Registry:** the bible's At-risk after Ch.7 says "**'The [color] of [thing]' as a sentence shape**: CLOSED at 2 (Ch.1 …). SPENT. … **A third use anywhere is a CRITICAL.**" At-risk after Ch.15 repeats "still CLOSED at 2", and Ch.21's "the color of the sand" was cut for the same reason. The bible's own At-risk after Ch.23 lists this phrase as spent texture, so no earlier pass caught it.
- **Fix (word-neutral):** `the color of lentil soup,` → `brown as lentil soup,` This follows the "white as whey" precedent kept in Ch.15. "brown as" appears in no chapter.
- **Cascade:** none. The bible's At-risk after Ch.23 should log the new wording, and log the old one as CUT.

### [C-02] HEAT 2 rebuilds HEAT 1's road comparison and goes over the one-comparison cap
- **Audit:** HEAT rules / NO TICS.
- **Evidence:**
  - l.240: "He gave me the attention he gave a strange road, all of it, and nothing in his face that I could read."
  - l.256: "as he would steady a load on a bad slope."
  - Ch.15 (HEAT 1, SPENT): "as a man learned a road he meant to take again at night, feeling where it led and where it gave".
- **Registry:**
  - At-risk after Ch.15, "Heat 1, SPENT staging": "Ch.23 and Ch.34 find other orders, other bodies, other senses: … **no road comparison**."
  - voice-dna §5 anti-patterns: "one characterizing comparison at most per scene."
  - l.240 compares his look at her body to a road, which is exactly Heat 1's comparison. With l.256 the scene has two comparisons, three if l.228's "combed" back is counted.
- **Fix (−11 words):** `He gave me the attention he gave a strange road, all of it, and nothing in his face that I could read.` → `His face, while he looked, gave me nothing to read.`
  - Do not use "He looked at all of it": it would echo her "All of it's yours" as compliance, and the command echo is SPENT.
  - "while he looked", "gave me nothing" and "nothing to read" appear in no chapter.
- **Cascade:** l.256's load on the slope becomes the scene's one comparison, which is allowed (see I-17).

### [C-03] The undressing rebuilds HEAT 1's sequence: graceful, then belt first, then the garment catching on the way off
- **Audit:** HEAT rules / NO TICS.
- **Evidence:**
  - l.234: "At six months there was no graceful way to do it, and I did not try for one. The belt first. The tunic next, in two goes, because it caught on the belly the first time, and the shift under it likewise."
  - Ch.15 l.530: "I had meant to be graceful about the rest of it, and I got my belt off well enough. Then I took the chiton by its skirt and dragged it upward past my face, and at the top the cloth caught on itself and trapped my arms inside it."
- **Registry:** At-risk after Ch.15 lists as SPENT staging "The chiton caught over her arms", "The belt: 'laid it away in the corner…'" and "no belt-as-work". The three moves come in the same order: the grace disclaimer, the belt, the garment catching.
- **Fix (−42 words):** delete `At six months there was no graceful way to do it, and I did not try for one. The belt first. The tunic next, in two goes, because it caught on the belly the first time, and the shift under it likewise.` The paragraph then reads: "I lifted my cheek, got off the bed and took my own clothes off. I stood barefoot in the leak's spray and let him see."
- **Cascade:**
  - This also removes the month count that conflicts with Ch.22 (see W-01).
  - l.290's "Getting off him was no more graceful than getting on." still works, because its comparison is the mounting at l.252 ("needed two tries"). "graceful" becomes 1 in Ch.23.
  - The pregnancy stays fully on the page in l.236–238.

### [C-04] The sleep close rebuilds Ch.19's inn-loft close and contradicts Valens's on-page laughs
- **Audit:** NO TICS (frame rebuilt) / character consistency.
- **Evidence:**
  - l.318: "He let a breath go through his nose, which in Valens was the most of a laugh you got, and settled his shoulder lower. By and by his breath came long and even, with a little catch at the top of it, and he slept with his face to the wall."
  - l.320: "and the mule below kicked its stall again and stopped,"
  - Ch.19 l.183 (the inn loft over the stalls, with two carters): "Valens laughed once under his breath, and settled. Soon his breathing changed, and so did the carters', and below us a mule knocked a hoof against her stall and was still."
- **Why it fails:**
  - The beat order matches Ch.19 exactly: a half-laugh, "settled", the breathing changes, the mule below strikes its stall and goes quiet.
  - Ch.22 l.178 also ended a section with Valens turning "on his side toward the wall" and sleeping, so this is the second running chapter with that close.
  - "a little catch" in his breath repeats Ch.15's SPENT "the catch that came into his breath".
  - "the most of a laugh you got" contradicts Valens's earlier laughs: he laughs in the cave (Ch.6), helplessly in the hut (Ch.15 l.546–548, "He laughed. It started low in him and went on, helpless"), Mara tells Plautia "He laughed then." (Ch.16 l.374), and he laughs under his breath at Ch.19 l.183. ENTITY CH23-4 records the same clash.
- **Fix (−46 words):**
  - l.318: `He let a breath go through his nose, which in Valens was the most of a laugh you got, and settled his shoulder lower. By and by his breath came long and even, with a little catch at the top of it, and he slept with his face to the wall.` → `He let a breath go through his nose, and by and by he slept.` This keeps the disruptor's protected "It's right." and the breath through the nose. l.300 already turns him to face the wall.
  - l.320: delete `and the mule below kicked its stall again and stopped,` The fade then runs "…with a hush between them, and down at the foot of the bed, under the blanket…". It is still about 84 words, so the long-fade ledger is kept.
- **Cascade:**
  - l.184's single mule kick stays, mid-chapter, so the Ch.19 echo drops to one detail and is no longer a close.
  - Bible: At-risk after Ch.23 should log the breath-through-the-nose without the laugh label, and log "the most of a laugh you got" as CUT.
  - ENTITY: CH23-4 resolves.

### [C-05] The scars are "pale" in one sentence, and the skin "over the ridges" is "road-brown" in the next
- **Audit:** Character consistency: distinguishing marks.
- **Evidence:** l.228: "more than a dozen, raised and pale and shining a little, harder than the skin round them. … Over the ridges the skin was road-brown. Between them it was paler, so that his back looked combed."
- **Why it fails:** the ridges are the scars, which the paragraph has just called pale, and scar tissue does not tan. The two sentences put the colours on the wrong surfaces. "road-brown" is also a third road word in the heat (see C-02, and "road posts" at l.264).
- **Fix (−6 words):** `Over the ridges the skin was road-brown. Between them it was paler, so that his back looked combed.` → `Between them the skin was brown, so that his back looked combed.` "Between them the skin" appears in no chapter.
- **Cascade:** none. The first full sight of the back now agrees with Ch.12 ("They flogged me"), with Ch.16's "the ridges of it" felt by touch, and with ENTITY's new back entry. Left and right agree throughout: left shoulder to right hip, two low on the right.

---

## WARN ISSUES (fix before the evaluator; the evaluator counts these)

### [W-01] The month count: "At six months" is about six weeks after Ch.22's "Five. Nearly six."
- **Audit:** Timeline.
- **Evidence:**
  - l.234: "At six months".
  - Ch.22 l.28: "Five. Nearly six." This is said on the arrival day. In the final Ch.22 text the arrival is in March, with "a month" in the house before the court sat.
  - The sentence was given on 20 April. With 2–3 days on the road, the inn falls about 23–24 April.
- **Arithmetic:** "nearly six" in mid-March gives about 6½–7 months now. Ch.20 and Ch.21 put the pregnancy in its early weeks in Oct/Nov AD 73 ("nothing yet to find there" about 21 Nov), which points the same way. The birth still falls in summer AD 74 either way. ENTITY CH23-3 notes it as compatible only as a round count.
- **Fix:** C-03 removes the sentence, and with it the number. If C-03 is not taken: `At six months` → `That far along` (word-neutral). This keeps outline and foundation's "about six months" from being contradicted by the page.
- **Cascade:** Grata's "until the eighth month" (l.246) then reads as near the limit, which is truthful. Do not add any line that notices it.

### [W-02] Valens's room-read on entering rebuilds the bodyguard exits-scan that Ch.22 cut twice, and his door-vigilance runs to 5 narrated notes
- **Audit:** NO TICS / narrated-trait rule (≤3 notes of one state).
- **Evidence:**
  - l.54: "He took in the room as he took in every room: the carters, the second door, to the yard, the ladder to the ceiling hatch, the window and its shutter."
  - "with the door in his eye" (l.54); the latch and the stool search (l.174); "He rose on his elbow to see the door past me." (l.292); "He watched it a little." (l.300).
- **Registry:**
  - At-risk after Ch.13: "Inside the temple as a bodyguard's report (floor, the one door, men …): SPENT."
  - Ch.22 audit W-08 cut both of Ch.22's narrated exit-watches ("with the whole aisle in front of him and the way out at both ends of it"; "stood with the street in view").
  - The list is also an item sequence, and its comma ("the second door, to the yard,") makes "to the yard" read as a separate item.
- **Fix (−29 words):** delete `He took in the room as he took in every room: the carters, the second door, to the yard, the ladder to the ceiling hatch, the window and its shutter.` l.54 then reads "Valens arrived streaming and stopped a pace in. He came and sat opposite, on the wall bench, with the door in his eye."
  - Optional, to reach 3: delete `He watched it a little.` (l.300).
- **Cascade:** the door-side turn keeps its setup: "with the door in his eye", the latch at l.174, the elbow at l.292 and "The latch is wood." That is enough for the payoff at l.300.

### [W-03] "to look him over": the pronoun points at the driver, but the carter's question is for Valens
- **Audit:** Dialogue attribution.
- **Evidence:** l.56–60: the driver comes in complaining; then "The older carter turned on his bench to look him over. 'That your carriage out there? The Capuan's?' / 'Hired.'" The nearest "him" is the driver, who is the Capuan. "Hired." only makes sense from Valens, and it is unattributed.
- **Fix (word-neutral):** `to look him over` → `to look Valens over`.
- **Cascade:** "He'll have you over at Fundi" now points at the Capuan driver standing there, which is the joke.

### [W-04] "I had been on the steps for it" contradicts Ch.22's gallery, and the paragraph recalls the SPENT sneeze
- **Audit:** Information flow / NO TICS.
- **Evidence:**
  - l.136: "I had heard the beginning, as far as what he slept on outside her door, and then a man sneezed and I was gone. … he had stood up for an hour in front of half of Rome, and I had been on the steps for it."
  - Ch.22 l.296–318: Mara watched the cross-examination from the gallery ("Celer's advocate had closed on Valens"). She heard "I watched the street", "Who was on the roofs", "Ask the cook", and the killing question.
  - At-risk after Ch.22 lists "the sneeze and the court's 'Salve' chorus" as SPENT (no second use anywhere).
- **What is correct:** "as far as what he slept on outside her door" matches Ch.22 l.232–236 ("on the tiles" and then the sneeze). "the young man's uncle" matches Ch.22 l.136.
- **Fix (−3 words net):**
  - `and then a man sneezed and I was gone` → `and then I was gone`
  - `and I had been on the steps for it` → `and I had been outside for most of it`
  - Before the gallery she was on the steps and walking the Forum, so "most" is true.
- **Cascade:** "I missed it," … "All you told them." (l.128) still holds, because she missed the direct examination after the tiles. Keep "I had laughed it away": it refers back to the laugh and is not a new one.

### [W-05] Valens downcast is narrated in 6 notes (cap 3)
- **Audit:** Narrated-trait rule (the Ch.22 cycle-1 hand count).
- **Evidence:**
  - "Valens broke a piece of bread and held it." (l.68)
  - "He watched the road." (l.126)
  - "He considered the bread in his hand." (l.134)
  - "his eyes were on the floor between his boots" (l.178)
  - "and he sat on in it" (l.194)
  - "The floor had him again." (l.224)
  - The bread is held twice and the floor is looked at twice.
- **Fix (−13 words):**
  - delete `The floor had him again.` (l.224);
  - delete `He considered the bread in his hand.` (l.134), so the speech joins into one line: `"It was the same. Near enough the same."`
- **Cascade:** that leaves four notes, the l.126 summary and three images, which is the strongest legal shape. If the evaluator still counts four, cut `and he sat on in it` next.

### [W-06] His hands on the blanket are narrated in 4 notes (cap 3)
- **Audit:** Narrated-trait rule.
- **Evidence:**
  - l.258: "palms up, one each side of his head"
  - l.262: "The fingers stirred once on the felt and went loose."
  - l.274: "His hands were on the blanket still, open,"
  - l.278: "the hand still lying open"
- **Fix (−7 words):** l.274 `His hands were on the blanket still, open, and he let me look at his face with nothing in front of it.` → `He let me look at his face with nothing in front of it.`
- **Cascade:** l.276's "the nearer hand from beside his head" still places the hand. The disruptor's #3 trims stand.

### [W-07] Acca holds the hen in 4 notes; the bible says 3
- **Audit:** Narrated-trait rule / the bible's ACCA card.
- **Evidence:**
  - l.22: "a hen in the crook of her other arm … kept it on her arm since we arrived"
  - l.86: "She gathered up the hen"
  - l.86: "She kept to the hearth with the hen against her chest."
  - l.98: "without letting the hen go, pouring one-handed"
  - The ACCA card records 3: the arrival, "gathered up the hen" and "without letting the hen go".
- **Fix (−6 words):** `She kept to the hearth with the hen against her chest.` → `She kept to the hearth.`
- **Cascade:** none. Her hen and roof address stays at 3.

### [W-08] Mara's hunger is narrated in 4 notes
- **Audit:** Narrated-trait rule.
- **Evidence:**
  - l.40: "hungry since Forum Appii", "and hungry again a mile after it", and Grata's "the child eating … So far it had asked for everything."
  - l.122: "I was hungry the way I was always hungry now, which was all the time" (the Writer's protected ugly sentence).
- **Fix (−6 words):** `I had been hungry since Forum Appii, where I had eaten last, and hungry again a mile after it.` → `I had been hungry since Forum Appii, where I had eaten last.`
- **Cascade:** none. The disruptor's cut of "These days I was always hungry." stays cut.

### [W-09] Hearing the gray's lameness through the floor rebuilds Ch.22's night sound-reading and its "through" marvel
- **Audit:** NO TICS (frame from the previous chapter).
- **Evidence:**
  - l.218: "I listened and heard three mules. He had heard which one was favoring a leg, through a floor, in the rain."
  - Ch.22 l.150–166, SPENT (At-risk after Ch.22): the night carts, "That one's losing a wheel" / "From up here?" / "It knocks every turn"; then the heel, "You can tell that through me?"
- **Why it fails:** the same shape: at night, in bed, he diagnoses a fault by sound, and Mara marvels at the medium he heard it through.
- **Fix (−22 words):** delete both sentences, so the paragraph opens "Down there the man was laughing now, a tired laugh, …".
- **Cascade:** Valens's "The gray's lame," … "Off hind. He's walked it through the water." (l.216) is kept: it is his line, and l.196 already gives "three by the sound of their feet".

### [W-10] HEAT 1 echoes inside HEAT 2: the climax marked by a limb, and his weight given up
- **Audit:** HEAT rules / NO TICS.
- **Evidence:**
  - l.276: "I came, my fingers spread wide on his chest, a long, slow, shaking time". Ch.15 SPENT: "I came with my heel hooked behind his knee". The disruptor varied "I came with my", but the shape survives: "I came" plus where one limb was.
  - l.306: "he lay back against me with his weight given up into the bed and the belly and my arm." Ch.15 SPENT: "all his weight came down onto me and stayed"; Ch.15 l.568: "until his weight was on me properly".
- **Fix (−19 words):**
  - l.276: `I came, my fingers spread wide on his chest, a long, slow, shaking time,` → `I came, a long, slow, shaking time,`
  - l.306: `and he lay back against me with his weight given up into the bed and the belly and my arm.` → `and he lay back against me.`
- **Cascade:**
  - l.276's earlier "with my other palm on his chest to keep my balance" keeps the hand.
  - l.306 still carries the outline's "he is the one comforted" through the long muscles letting go "down to the hip".

### [W-11] The phrasing of Ch.22's laugh scene comes back in the heat, and "the belly" appears ×7
- **Audit:** NO TICS.
- **Evidence:**
  - l.280: "I bent to it as far as the belly let me". Ch.22 l.246 (the SPENT fifth laugh shape): "I bent forward over the child, as far as it allowed, and gripped the bench's edge in my two fists".
  - l.226: "took the hem of his tunic in two fists"
  - l.272: "slowly, because slow was all the belly allowed"
  - "the belly" appears at l.156, 234, 256, 272, 280 and twice at l.302. The construction "the belly allowed / let me" appears twice in 8 lines.
- **Fix (−17 words):**
  - l.280: `and I bent to it as far as the belly let me, and got my arms round it` → `and I bent to it and got my arms round it`
  - l.226: `in two fists ` → delete, leaving `took the hem of his tunic and pulled it up`
  - l.272: `I began to move, slowly, because slow was all the belly allowed.` → `I began to move, slowly.`
- **Cascade:**
  - "the belly" falls to 5, or 4 if C-03 is taken.
  - Narrated "slow" falls from 4 to 3 ("by slow degrees", "slowly", "long, slow, shaking"). Ch.15's SPENT doubling "It was slow, and stayed slow" is no longer echoed.

### [W-12] "told the roof": a HEAT 1 string reused
- **Audit:** NO TICS.
- **Evidence:**
  - l.150: "and the landlady told the roof a word that I did know."
  - Ch.15 (Heat 1 SPENT): "He told the roof something in Latin".
  - "told the roof" appears only in Ch.15 and Ch.23.
- **Fix (word-neutral):** `told the roof` → `gave the roof`
- **Cascade:** the l.32 payoff ("a dialect I could not follow" → "a word that I did know") stands. Her address count is unchanged at 3.

### [W-13] "and I asked nothing": a labelled silence (the Felix rule) and a fourth use book-wide
- **Audit:** NO TICS.
- **Evidence:**
  - l.194: "Who we were, he left out, and I asked nothing."
  - l.190 has just said "I kept quiet."
  - "asked nothing" also appears at Ch.3, Ch.12 l.318 and Ch.13 l.124. The last two are Felix's silence as a reported beat, which At-risk after Ch.21 says to "show …, never label".
- **Fix (−4 words):** `Who we were, he left out, and I asked nothing.` → `Who we were, he left out.`
- **Cascade:** none. The onion stays unexplained, and l.190 carries her silence.

### [W-14] "The nipples had gone wide and dark": kin of the CLOSED "had gone (quiet|still)"
- **Audit:** NO TICS.
- **Evidence:**
  - l.238.
  - At-risk after Ch.15: "'had gone (quiet|still)': CLOSED".
  - Ch.21's "his face had gone young" was cut as its kin (I-09, logged in the FELIX card).
- **Fix (word-neutral):** `The nipples had gone wide and dark.` → `The nipples were wider and darker.`
- **Cascade:** none.

### [W-15] The body paragraph sweeps the body as a head-to-foot list of parts
- **Audit:** Heat register.
- **Evidence:** l.238 runs belly → navel → line → breasts → veins → nipples → "My ankles were puffed over the strap marks. I had a flea bite on my shin and another above my knee. The one on the shin I had scratched until it bled."
- **Rules:**
  - voice-dna §5: "It is never a parts inventory (that would also be the retired catalogue device)."
  - Ch.12's head-to-foot inventory look was a CRIT.
  - The ankles are also a second note of l.40's swollen ankles.
- **Fix (−33 words):** delete the last three sentences (ankles, the two bites, the scratched shin). The paragraph keeps everything that does work: the belly, the March line, and the sore breasts that pay off at l.242 and l.280.
  - Lighter alternative: delete only `My ankles were puffed over the strap marks.` (−8). That leaves a sweep, so WARN would remain at INFO level.
- **Cascade:** the flea thread survives at l.20, 138–146, 272 and 320. Bible: At-risk after Ch.23's "the bites on shin and knee" moves to CUT.

### [W-16] Ch.24 set-up: the lamp lit below by night over a lame mule pre-stages Ch.24's anchor
- **Audit:** Forward collision.
- **Evidence:**
  - l.300: "A lamp had been lit underneath us. It showed in lines between the boards, and somebody down there was talking low to the gray."
  - outline Ch.24 beat 4: "Valens outside the door … trimming a mule's hooves by lamplight at midnight." That is the chapter's designated tenderness, a man and an equine's foot by lamp at night.
- **Fix (−12 words):** `A lamp had been lit underneath us. It showed in lines between the boards, and somebody down there was talking low to the gray.` → `Somebody down there was talking low to the gray.`
- **Cascade:**
  - The disruptor's #4b keeps its function: the barge man sees to the gray and Valens turns his back to the door after hearing it. The rain-easing it replaced is not restored.
  - l.218's "nobody down there said anything more" now meets a voice later (see I-04).

### [W-17] "a carrel beside a radiator that knocked": a Ch.6 string with its tense changed, and the fifth radiator in Mara's memories
- **Audit:** NO TICS.
- **Evidence:**
  - l.124.
  - Ch.6 l.332: "an apartment with a radiator that knocks all night in February".
  - Radiators also appear at Ch.1 l.333, Ch.2, Ch.5 l.223 (a student room, "a radiator nobody could turn off") and Ch.9 l.188.
- **Fix (−4 words):** `in a carrel beside a radiator that knocked,` → `in a carrel,` "carrel" appears in no other chapter.
- **Cascade:** the memory rule (CP2-2) still passes. The memory is triggered by the road, takes one clause, and goes back into the scene ("I sat with it, and it did not last").

### [W-18] The "five years" count, which foundation §10 assigns to Ch.23, is no longer printed
- **Audit:** Plan vs page (ENTITY CH23-1).
- **Evidence:**
  - foundation §10, "Counts the Writer will print": "the frame (69) to the trial (spring 74) is **five years** (Ch.23)".
  - outline: "The truth cost five years … and changes nothing about his back."
  - The disruptor's op #1 cut the only sentence that carried the count.
- **Fix (+2 words; restores the count, not the cut paragraph):** l.230 `Every mark was where it had always been.` → `Every mark was where it had been for five years.`
- **Alternative (orchestrator):** amend foundation §10 and leave the page alone. Ch.22's Plautia already has "in five years".

### [W-19] Two carters at an inn for the second time; the Ch.19 inn texture surfaces again
- **Audit:** NO TICS (walk-on staging).
- **Evidence:**
  - l.42: "Two carters sat at the table's far end".
  - Ch.19 l.163: "Two carters from Nola … had taken the end under the gable". At-risk after Ch.19 SPENT: "the inn loft and the slipped tile".
  - Ch.23 also has a landlady meeting them on arrival (l.26; Ch.19 l.159), a room over the stalls, and a cracked tile that leaks (l.158). The room over the stable and the tiles are outline-mandated, so only the walk-ons are flagged.
- **Fix (word-neutral):** `Two carters` → `Two tilers`. They are hauling roof tiles. The later mentions then need `carter(s)` → `tiler(s)` at l.56 ("to the carters"), l.58, l.70, l.112, the first carter of l.148 ("The nearer carter"), and l.54 if W-02 is not taken. Leave l.148's "the cheating carter" alone, because he is the third man who sold the mule. These are narration-only swaps; "the Capuan's" carriage is unaffected.
- **Alternative:** leave the walk-ons and log the pair as SPENT. This is the lowest-priority WARN.

---

## INFO

- **I-01 Bible re-sync (for the downstream chain; nothing to edit in the chapter).** At-risk after Ch.23 still quotes draft strings that are off the page:
  - `"I'm the size of a wine jar," / "A small one."` and `"These days I was always hungry."` → log as CUT, never restore.
  - Add `"Your left knee," … "The cords are lower on this side."`, the cramp (`"Leg," … "Leg, leg."`), the barge man's `"Let me get them dry first. You can shout after."` and the carter's `"It won't,"`.
  - ACCA card: the address count should be 3 (roof twice, hen once), and "Shout if the roof comes in" is said "to our backs".
  - ACCA's "Never names what is in the pot" conflicts with her own "I've eels!" (l.208). Amend the card.
  - Log whatever C-01…W-19 change.
- **I-02** "The nearer carter" (l.148) is a third label for two men, after "the older" and "the younger". It is harmless; swap to `The younger carter` if W-19 is not taken.
- **I-03** l.194: "The crack over the door spat a fine wet dust onto the floor". "dust" falls on Valens just after the work-residue beat was CLOSED (Ch.21), and "fine" repeats l.158's "fine spray". Optional, word-neutral: `spat a fine wet dust onto` → `spat rain onto`.
- **I-04** l.218 "nobody down there said anything more" and l.300's voice "talking low to the gray" sit loosely together. The disruptor wants l.218 loose. If the evaluator reads it as a contradiction: `said anything more` → `answered her`.
- **I-05 Grata's "until the eighth month" (l.246).** She named the pregnancy in the olive month of AD 73 (Ch.20), and Mara left for Puteoli before the Kalends of March, so any winter conversation fits. "Grata had told me in the winter" (l.40) dates the other advice the same way. Valens's "Grata says what she thinks will rile me" fits Ch.21's Grata. It does not count against Grata's "on men" cap, because she does not speak on the page. The advice is folk practice, not a period error worth raising.
- **I-06 The onion, third surfacing: consistent and fresh.** Ch.12: "They hung them under the eaves. In strings, to dry." Ch.22: the village and the autumn. Ch.23: the rain, his mother, "round her neck", which agrees with the strings. It avoids all four banned elements (no village, no autumn, no smell before seeing, no "They grew those"). It is Mara's first knowledge of his mother. Mara knows "Thrace" and "taken as a boy" from Ch.22 l.210–214, which she heard before the sneeze, so "Who we were, he left out" is right. Ch.41 needs fresh words again (no mother running, no rain, no shift).
- **I-07 Wrists and the watch.** No watch and no bracelet on the page. That is no conflict (right wrist the Seiko, left the bracelet, Ch.18). Ch.24's watch winding is unspent.
- **I-08 Geography and history verified.**
  - The marsh road straight between reeds; Forum Appii to Tarracina in a day; the Decennovium canal and towpath with mule-hauled barges (Horace's own barge had a mule).
  - The flood "Past the halfway post"; the cliff with a temple of Jupiter (Anxur) "supposed to be up there"; the road leaving the marsh at the cliff foot (Trajan's cutting is later, so it still went over the hill).
  - Fundi, 13 miles on; Sinuessa about 44 miles, so "two days" and "Three" in rain are both right.
  - The carriage taken outside the Capena Gate (Ch.22 l.10: no wheels inside by day); the chair's price carried by the freedman (Ch.22 l.410–414).
  - Pennyroyal against fleas (Pliny's *pulegium*); the eight-scored loaf.
  - Horace, Sat. 1.5: the bad water and his war on his stomach, the frogs, the drunk boatman singing to his absent girl, the inns. "a hundred years" against 37 BC → AD 74 is a fair round number.
- **I-09 Laws: pass.**
  - Foreshadowing 0 ("the whole wet night ahead of them" belongs to the fleas).
  - No tomb. "door" is literal throughout, and the door-side staging is outline-planned.
  - The child is "it" and never a citizen (CP4-1). No "Whose …?" or who-pays question.
  - No Mara laugh and no mouth channel. "I had laughed it away" refers back to Ch.22; it is not a new laugh.
  - No hand on the belly and no heel. The child reaches Valens only through his back (l.304), as the bible designed.
  - No backlit doorway. Acca "waiting in the doorway" (l.26) is not backlit.
  - No lying-awake close (he sleeps), no "So…" opener, no teeth (reserved for Ch.24's midwife).
  - Spoken "Then…" openers 2 (at cap). Narrated "somewhere" 2 (at cap).
- **I-10** "I'll be up in the night. Twice, at least." (l.294) points at the bladder, a body-rebel channel SPENT since Ch.17 and kept out of Ch.22 (C-02). Here it is a practical reason, not a rebel, and nothing is named. Acceptable, but leave it at one.
- **I-11 The cramp (l.284–288).** It falls after the climax, so "her asides go quiet" during the act still holds. The disruptor's own fallback, "until my left calf knotted under me." with his hand dropped, is available if the evaluator objects. "Leg," … "Leg, leg." is a cramp cry, not an anaphora triad.
- **I-12 "a while" ×3** (l.232 narration, l.266 narration, l.282 spoken). Ch.22 W-07 flagged four. Optional: l.232 `For a while that was all.` → `That was all.`
- **I-13 The permission frame "let" ×5** (l.178, 260 spoken, 274, 280 "allowed", 284). It is thematic, but the evaluator may count it. Optional: l.284 `He kept hold of me, and I let him, until` → `He kept hold of me until`. This one fix also fixes I-12's count if paired.
- **I-14 Singing walk-ons.** The driver sings to the frogs (l.24) and Horace's boatman sings (l.124). This follows the Ch.17 baker, the Ch.19 mason and the Ch.22 drover. Watch for Ch.24 and after. No fix here, because "If he stops singing at it." is speech.
- **I-15 "the bridge".** "since the bridge" (l.186) and "Bridge was under." (l.200) may read as the same bridge, which the carriage crossed. This is harmless; leave it.
- **I-16 "You heard it at Kirrha. At the stream."** (ENTITY CH23-2): a loose naming of the Ch.12 pool on the Kirrha road, in his mouth. Fine.
- **I-17 One comparison.** After C-02, the heat has one comparison, "as he would steady a load on a bad slope", which is allowed. l.228's "looked combed" precedes the act, inside the back look. If the evaluator counts it in the scene, the total is still 2, which is within the voice-dna metric of ≤2 similes per heat scene.
- **I-18 The rest of Ch.24's setup is clean.**
  - Home is named ("Down. Home." / "Pompeii.").
  - The child is awake and kicking, with nothing pointing to labour.
  - No midwife, no Grata's back room, no teeth, no watch, no Mrs. Dunphy.
  - Ch.24's hook must not be CONTRAST and its pull must not be EMOTIONAL GUT PUNCH (hook report).
  - After C-04, Ch.24 should not close a section on Valens turning to a wall to sleep (Ch.22, Ch.23).

---

## Fix ledger (in page order; narration only; 0 spoken words cut)

| ID | Line | Change | Words |
|---|---|---|---|
| C-01 | 24 | `the color of lentil soup` → `brown as lentil soup` | 0 |
| W-08 | 40 | cut `, and hungry again a mile after it` | −6 |
| W-19 | 42, 56, 58, 70, 112, 148 (first) | `carter(s)` → `tiler(s)` (optional; not "the cheating carter") | 0 |
| W-02 | 54 | cut the room-read sentence | −29 |
| W-03 | 58 | `look him over` → `look Valens over` | 0 |
| W-07 | 86 | cut `with the hen against her chest` | −6 |
| W-17 | 124 | cut `beside a radiator that knocked` | −4 |
| W-05 | 134 | cut `He considered the bread in his hand.` (join the speech) | −7 |
| W-04 | 136 | `a man sneezed and I was gone` → `I was gone`; `on the steps for it` → `outside for most of it` | −3 |
| W-12 | 150 | `told the roof` → `gave the roof` | 0 |
| W-13 | 194 | cut `, and I asked nothing` | −4 |
| W-09 | 218 | cut the two "I listened … in the rain." sentences | −22 |
| W-05 | 224 | cut `The floor had him again.` | −5 |
| W-11 | 226 | cut `in two fists` | −3 |
| C-05 | 228 | two sentences → `Between them the skin was brown, so that his back looked combed.` | −6 |
| W-18 | 230 | `where it had always been` → `where it had been for five years` | +2 |
| C-03 | 234 | cut the three undressing sentences | −42 |
| W-14 | 238 | `had gone wide and dark` → `were wider and darker` | 0 |
| W-15 | 238 | cut the ankle and flea-bite sentences | −33 |
| C-02 | 240 | → `His face, while he looked, gave me nothing to read.` | −11 |
| W-11 | 272 | → `I began to move, slowly.` | −7 |
| W-06 | 274 | → `He let me look at his face with nothing in front of it.` | −7 |
| W-10 | 276 | cut `my fingers spread wide on his chest,` | −6 |
| W-11 | 280 | cut `as far as the belly let me,` | −7 |
| W-16 | 300 | → `Somebody down there was talking low to the gray.` | −12 |
| W-02 (opt.) | 300 | cut `He watched it a little.` | −5 |
| W-10 | 306 | cut `with his weight given up into the bed and the belly and my arm` | −13 |
| C-04 | 318 | → `He let a breath go through his nose, and by and by he slept.` | −37 |
| C-04 | 320 | cut `and the mule below kicked its stall again and stopped,` | −9 |

After the edits, re-run `bash tools/check_chapter.sh 23` and `python3 tools/tic_report.py --echoes 23`. Re-measure show/tell dialogue; it should rise to about 16.5%.

---

## SUGGESTED YAML PATCHES (for the entity-tracker's next UPDATE; not applied)

```yaml
suggested_patches:
  - entity: "conflicts.CH23-3 (pregnancy count)"
    action: "update"
    reason: "if C-03 is taken the page carries no month count; if W-01's alternative is taken, prose = 'That far along'. Either way CH23-3 resolves (no number on the page against Ch.22's 'Five. Nearly six.')"
  - entity: "conflicts.CH23-4 / valens.traits (his laugh)"
    action: "remove_conflict"
    reason: "C-04 cuts 'which in Valens was the most of a laugh you got'; the breath through the nose stays as an act, unlabelled"
  - entity: "conflicts.CH23-1 (five years)"
    action: "update"
    reason: "W-18 prints the count at the back ('where it had been for five years'), or the orchestrator amends foundation §10"
  - entity: "valens.physical (flogged back, ch23_page)"
    action: "update"
    value: "'raised and pale'; 'Between them the skin was brown, so that his back looked combed.' (no 'road-brown' over the ridges)"
    reason: "C-05"
  - entity: "acca.physicality"
    action: "update"
    value: "holds the hen 3 times on the page (arrival; 'gathered up the hen'; 'without letting the hen go'); address to hen/roof 3; 'gave the roof a word that I did know'"
    reason: "W-07, W-12"
  - entity: "walk-ons ch-23 (the carters)"
    action: "update"
    reason: "if W-19 is taken they are 'Two tilers' hauling roof tiles to Tarracina"
```
