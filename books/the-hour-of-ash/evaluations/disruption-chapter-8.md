# Disruption Report: Chapter 8 — The Thyiades (run 2)

Backup of the pre-pass text: `manuscript/reports/chapter-8-pre-disruption.md`. It is in `reports/`,
not `chapters/`, because the gates glob `chapter-*.md` there.

**Verdict on the input:** a strong chapter. It already had chaos (the Vermont tree lot; Nikaso drinking
Mara's share as the wrong reaction at the cave), an ugly sentence ("The climb went on and on."), a working
farce and an earned laugh. So the pass was light on noise and heavy on tidying stage business. The real
problems were the three flagged items plus a cluster of gestures the regex cannot see: things held up to
the light, Kallia's rags, eyes shut, skirts and fists, "found" and "November".

**Held fixed:**
- **First line and final sentence:** byte-identical, checked by diff.
- **Dialogue:** 26.1% → **26.9%** (band 25–35).
- **Scene breaks:** 0.
- **Median sentence:** **15** (shape_check and metaphor_check both).
- **Em-dashes:** 2, none added.
- **Romance signal:** none (the Valens glimpse is untouched).
- **Foreshadowing:** 0.
- **Spent narrator moves added:** none (no "So I…" opener, no "before I had decided", no command echoed as compliance).
- **Word count:** 7,899 → **7,697** by shape_check (`wc -w` 8,042 → 7,840). Still inside the 7,500–8,800 range.

## Flagged items, resolved

### 1. Steam (4 beats → 2)
- Cut **"The rags steamed in her hands."** That paragraph now opens "Kallia was no help." and ends on
  "…and she did not supply one now." Kallia's withheld husband closes the paragraph, with no object
  clicking it shut.
- Cut "and steam came off her knuckles". The flatbread simile stays, so her rags keep one image.
- Kept the ring of sandals steaming ("The ring of them steamed."). It is a different object, in the
  middle of a paragraph, and it is the one domestic setup.
- So the final sentence is now the chapter's **second** steam, and the first to come off bodies. The
  final sentence itself is unchanged.

### 2. The release
**Verdict before the pass: it was weakened.** The cliff-head exchange broke the rule outright with
husbands (Timo's "My husband says…"; Sostrata's "Tell your husband nothing"), and nobody on the mountain
objected. That made the rule look toothless, and "Say what you like" released almost nothing. The other
early breaches go through a pronoun ("his mother", "his sister", "his mother the dough"). The women talk
*around* men by way of their female kin, which keeps the rule alive as a joke. They stay.

**Fix (also op 8, dialogue mess):** Philista cuts in on the cliff-head exchange:
> "Husbands," said Philista. "On my cliff, and the god not woken."
> "He comes to whoever's awake," Sostrata told Timo, a good deal lower.

- The rule is now enforced on the page, by the woman who later lifts it. Her "He's woken … Say what you
  like" pays off her own "the god not woken". That is a payoff inside the scene, not narratorial
  foreshadowing.
- Sostrata answers Timo's god question only after the rebuke, which makes the exchange messier.
- Her "twenty years" put-down stays. Only the late answer moved.
- The feet scene's "You said a man … Up here." / "A husband isn't a man." now reads as the women
  policing each other, which is what it needed. Timo's "I'll go first," after the release now lands
  as release.

### 3. The rite passages (lyrical climbing, anaphora triads, mystical register)
- **¶ joining the ring.** "because the drum was in the ground and the ground was in my feet and my feet
  were the only part of me that had been warm since the stair" was an anadiplosis chain climbing to an
  ecstatic join. It was the chapter's one lyrical climb, and it also carried an "only" claim. It now
  reads "…and after it I joined the ring, mostly for the sake of my feet." That is bodily realism
  puncturing the moment.
- **¶ the dance.** "Hair came down. Hoods fell back. A woman went by me…" was three parallel short
  sentences, a triad. The first two are merged. The trance image ("with her eyes shut, her mouth open")
  lost its eyes-shut. The second dancer's "torch dripping pitch down her wrist" is now "her torch held
  so far back that the woman behind her had to duck". This is comic and physical, and it also stops
  pre-echoing the pitch on Mara's thumb at the cave.
- **¶ the cry.** Cut "since there was no right". It was the theme spoken aloud.
- **¶ the basket.** Cut "They were waking a god with a farmyard chore, and nobody seemed to find that
  strange but me." It glossed the barley-toss sentence and the "It is bread." / "It's bread as well."
  exchange, which already make the point (see op 7).
- **¶ the cave (no supernatural, deflated).** "The rock chilled my knuckles and the air chilled my palm,
  and there was no telling the one cold from the other; it was the cold of a mountain in January…" had
  two problems. It used the rock / air / cold rendering of the crack, which the bible marks SPENT
  (Ch.3, Ch.6). And "the cold of a [place] in [month]" echoes Ch.3's "the cold of a cellar in August".
  It was then followed by a negation pair ("My skin felt nothing move. Nothing reached me…"). It now
  reads: "My knuckles were on stone and my palm was in the dark, and the two of them were as cold as
  each other, which was January cold and no more." "I left my hand in there until I had been fair to
  it." is intact.

## Operations Applied

| # | Operation | Location | Before → After (brief) |
|---|-----------|----------|----------------------|
| 1 | Simile surgery | ¶ Philista's drum, after the snow | "beating her drum flat and hard, ~~not for dancing,~~ like a cook banging a pot…": the gloss is cut, and the simile does the work. |
| 1 | Simile surgery (domain balance) | ¶ under the stranger's cloak | "as warm as a kitchen with the oven going" → "as warm as a laundromat in February". Kitchen and food were supplying nearly half the chapter's comparisons (pot ×2, saucepan, griddle, biscuit, restaurant tray, licorice store, hot stone, kitchen). This one now comes from late-90s Philadelphia instead, and stops crowding the oven of the song that comes next. |
| 1 | Simile surgery (interpretive appositive) | ¶ Kallia after the cave | Cut "…and studied the flakes, a woman judging how long a job would take" (the whole sentence; see gestures). |
| 4 | Precision deflation | 5× "November" | Three were cut: "In November the crossing…" → "On a mule's back the crossing had taken me most of a morning"; "the mules had found in November" → "the mules had taken"; "built up since November" → "had grown". Kept: "as it had in November" (the ascent) and the shovel scratches "in November" (timeline). |
| 4 | Precision deflation | Kallia's hair; the bank | "every day since October" (the 2nd October) → "every day I had known her". "a bank at Fifteenth and Market" → "a bank downtown". It was the second street intersection in the chapter, and Twenty-second and Pine, the memory, keeps its precision. |
| 6 | Negation break | ¶ the cave | "My skin felt nothing move. Nothing reached me out of the dark." becomes a direct assertion ("January cold and no more"). |
| 7 | Missing paragraph | after "Was it shut?" | DELETED "She had known, then, where I went. All winter she had asked me about water and wool and pots, and of the mountain she had said only what the town said." It explained what "In there." had just shown. "It was not a question." was cut with it, for the same reason. Kallia's knowledge now stays in her two lines. |
| 7 | Missing sentence | ¶ the basket | The "farmyard chore" gloss was cut (above). |
| 8 | Dialogue mess | cliff head | Philista interrupts the husband exchange, and Sostrata answers Timo's question late (see release). |
| 8 | Dialogue mess (subject jump) | the lane | "…you drink what's left." ~~She hitched her skirts higher.~~ "And these squeak, do you hear them?" Nikaso's speech now jumps from wine to sandals without a beat, in one run-on, which is on her card. |

Small fixes ridden along:
- **¶ the stranger's sandals.** Cut "until she stopped trying". It contradicted her own "Each morning I
  tell you about the weather": she never stopped.
- **¶ the heap.** Cut "as I had waited at the spring and in the council hall", a recap clause.

## Gesture / stage-business scan (NO TICS, gestures included)
`tic_report` regex classes are 0 for Ch.8, before and after. The hand count found classes the regex
does not see:
- **Holding a thing up to the light/torch/fire: 7 → 3.**
  - Kept: Nikaso's foot "into my torchlight" (it shows the wet straps), and Sostrata's hand up for
    quiet plus "with her hand still up" (one continuous beat).
  - Cut or recast:
    - Nikaso's skin is now "squeezed … flat between her hands".
    - Kallia's torch held up to the flakes (cut).
    - Kallia "walked on, and the wind took her flame flat".
    - Timo "stuck the foot out at the fire".
    - Nikaso's ruined sandal is now "in her lap".
- **Kallia's rags: 7 → 3.**
  - Kept: turning them like flatbreads; "bent her face over her rags" at the joke (her one unguarded
    moment); "dried rags folded under her cheek".
  - Cut: "sat with her rags in her hands", "spoke over her rags" (now a plain tag), "was turning her
    rags to the fire" (now "Kallia was no help."), "went on with her rags" (now "which suited Kallia").
- **Inspecting / studying: 6 → 4.** Cut Kallia's "took stock of me" and "studied the flakes". Nikaso's
  "studied it" became "waited for it to fail", which is her worldview (everything borrowed will be
  ruined) and sets up "Now I'll have one eye."
- **Eyes shut / opened: 4 → 3.** The dancer's eyes-shut is cut. The stranger keeps all three: eyes shut,
  "without opening her eyes", "Even the big woman had opened her eyes". That is one deliberate arc,
  ending when the verse stops.
- **Skirts and fists: 8 → 6.**
  - Cut Nikaso's "hitched her skirts higher" (her skirts are already in two fists).
  - Sostrata's "torch held clear of the drop in one fist" became "kept clear of the drop".
- **"held out": 2 → 1** in adjacent paragraphs. Kallia's arms are now "stuck out stiff".
- **"found": 6 → 2.**
  - "the wind had got in among them"
  - "Sostrata's cloak had done the same"
  - "Timo leaned to me across the fire"
  - "the mules had taken"
  - Kept: "Nikaso found me", and the bare foot that "found my calf".
- **"settled": 4 → 2.** The ivy "went on my head"; "the night came in over the wall like water over a sill".
- **Duration "a while": 3 → 2.** "I stayed on my knees a while with the hand in my armpit" doubled the
  hand already tucked "under my arm". It now reads "I stayed on my knees; this time I hit nothing…",
  and "against my side" is cut from the tuck.
- **"Nikaso had the skin" ×2 → 1.** The dance-side one stays as the dry reason nobody watched Mara go.
- **"Then" in narration:** paragraph openers 5 → 4 ("Then I withdrew" is gone). Two mid-paragraph
  "Then" sentences are also gone: "Then, because…" and Kallia's "Then she went to help…".
- No gesture was added that already appears in the chapter. "waited for it to fail", "stuck the foot
  out" and "leaned to me" are each new to the chapter.

## Operations NOT Applied (and why)
- **2 Irrelevant thought:** the Writer's two chaos moments are on the page (the Vermont tree lot; the
  wrong reaction at the cave), and the outline says "none of Mara's forced". The women's chaos carries
  the rest.
- **3 Emotional control break:** skipped. Mara's breaks are canon-capped at three (Ch.6, 20, 22); her
  voice failure is retired for Ch.7–9; and the song's laugh ("there was no stopping it, and I did not
  try") already is the chapter's unmanaged moment. A second one would dilute it.
- **5 Ugly sentence:** one already exists ("The climb went on and on.").

## Strongest Disruption
**Philista's "Husbands. On my cliff, and the god not woken."** It does three jobs in eight words: it
makes the no-men rule real on the page, it makes "Say what you like" the release of something, and it
gives Philista a moment of rule-keeping that is pure card (the rite done properly). Close second: the
rags and held-to-the-light thinning. The pen scene now has room for the stranger's cloak, and the last
steam arrives on its own.

## Risk Assessment
- **"Kallia was no help."** It is dry and slightly unkind, and it is narrator judgment rather than a
  beat. I think it's the right temperature, since Mara is on the spot. If the evaluator reads it as
  flip, restore a gesture that is not rags.
- **"laundromat in February".** It is a new modern comparison inside the warmest moment of the chapter.
  It is period-safe (1998), from a different domain, and characterizing. It brushes against the
  tree-lot memory's warmth among strangers without echoing its words.
- **Cutting the Kallia-knew paragraph** loses "All winter she had asked me about water and wool and
  pots", a nice summary of their relationship. The Ch.7 page shows that already.
- The cave sentence now carries less sensory texture (the knuckles/palm contrast is flatter). That is
  deliberate, since the beat is "nothing happens", but it is the one place I traded texture for deflation.

## Bible quotes these edits invalidate (character-bible.md NOT edited)
- **Kallia, Ch.8 block:**
  - "Knows where Mara went (the wet knees…)": still true, but the narration's "She had known, then,
    where I went" is gone.
  - Her one walk-off now reads "and went to help Philista get the women into a line" (no "Then she").
  - "bends her face over her rags at Mara's joke": still on the page.
- **Mara, Ch.8 block / at-risk after Ch.8:**
  - "the only part of me that had been warm" is cut. Ch.8's narration "the one / the only" count is now
    **1** ("the only new thing in the cave").
  - "the hand warmed in her armpit": the page now says "under my arm".
- **Sostrata card:** the syntax example "Your husband says plenty, Timo, for a man who's been married
  since the vintage" still matches. Her Timo exchange gains "He comes to whoever's awake," told late
  and lower. "Tell your husband nothing" is now "Tell him nothing".
- **Philista card:** new page line, "Husbands," / "On my cliff, and the god not woken." (a bark, then
  pride in the rite).
- **Nikaso card:** "If it snows they'll stop squeaking, and then I'm a dead woman." still matches. New
  narration: she puts the mended sandal on and "waited for it to fail".
- **Ch.8 walk-on note, mention-only list:** "a bank at Fifteenth and Market" is now "a bank downtown".
- **Ch.8 spent list:** "waking a god with a farmyard chore" is no longer on the page. The entry can stay
  as spent or be dropped.
- **Theano, the stranger, Timo and Valens quotes:** unchanged.

## Gates after the pass (from /home/user/Books)
`bash books/the-hour-of-ash/tools/check_chapter.sh 8`:

| Gate | Result |
|---|---|
| style | clean (simile 3.1/1k, em-dash 2, foreshadow 0) |
| grammar | 0 errors |
| rhythm | 0 flagged |
| show/tell | no flags |
| voice-wear (strict) | clean |
| tic gate | clean (and-chains 3, 'So' openers 0, 'before I decided' 0; no gesture class in Ch.8) |
| metaphor | no flags (median 15, 6.4% over 40 words) |
| shape | CLEAN (7,697 words, 0 breaks, dlg 27%, median 15, open `dialogue`, end `quiet`) |

`python3 books/the-hour-of-ash/tools/tic_report.py --echoes 8`: **0 echoes.**

These interim failures came from my own edits, and all were fixed before the final run:
- "had gone into" reached 3 book-wide; the bank line is now "turned up in".
- "and kallia let" echoed Ch.7; it is now "which suited Kallia".
- "i was on my" self-repeated against an earlier chapter; it is now "I stayed on my knees".
- The median slipped to 14 after the long-sentence cuts. Two merges at seams I had created restored it to 15.
