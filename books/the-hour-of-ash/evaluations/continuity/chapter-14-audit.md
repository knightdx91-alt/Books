# Continuity Audit: Chapter 14 (run 2, per-chapter drift audit)

**Date:** 2026-10-20
**Mode:** MANUSCRIPT AUDIT. Ch.14 "What Pompeii Means" (post-disruptor) checked against Ch.1–13 as they stand on disk; ENTITY_STATE.yaml (as of Ch.13, read only, because the tracker runs in parallel); outline.md; foundation.md; voice-dna.md; character-bible.md; voice-bank samples 01–13; STATE.yaml guardrails and resolved_author_decisions.
**Chapter reviewed:** `manuscript/chapters/chapter-14.md`
- **Length:** **3,043** prose words by shape_check (3,377 by `wc -w` with the header). The floor is 3,000, so there are **43 words of headroom**. The recommended fixes below come to about **+13 words net**.
- **Shape:** dialogue 4.8% (band 0–10). 9 breaks. Median sentence 12 (gear low). `I-punch` → `long-fade`, which matches the ledger.
- **Citations:** `l.NN` is the file line in chapter-14.md. Lines in other chapters are cited as `ChN l.NN`.

**Mechanical baseline** (`bash tools/check_chapter.sh 14`, run read only): **ALL CLEAN.**
- Style: simile 0.7/1k, em-dash 0, foreshadow 0.
- Grammar 0; rhythm 0; voice-wear strict clean.
- Tic gate clean, including gesture classes. Echo scan 0. Command echo 0.
- And-chains 1; credential asides 0 by gate (2 by hand, under the cap of 4).
- Shape audit: SHAPE CLEAN.

**My own sweeps:**
- 4-grams against every voice-bank sample, the bible, voice-dna, foundation and outline.
- A by-hand pass on the spent and at-risk registries.
- Paragraph-final negations, counted by script and checked by hand.
- Every "I meant to…", "yet", "would" and conditional line.
- Moon and calendar arithmetic.
- The 1998-era facts: exhibition history, Pliny, the Pompeii plan, Saint Paul, garum.
- An information-flow table for every person under Kallia's roof.

**Total findings: 46. CRITICAL: 1 | WARN: 13 | INFO: 32**

**Summary**
- **The one CRITICAL is the moon.** Ch.13 dates this day as the 7th of Bysios, and the Delphic month is lunar. That night the moon is a half moon in the evening sky and sets around midnight. The page instead has Valens say "There's no moon till the new one" and puts an old waning crescent rising before dawn. That sky belongs to days 24–28 of the month. The fix is three phrase-level swaps and costs about +2 words.
- **No foreshadowing.** Every forward-facing line is an intention, a plan or a conditional. Mara never narrates her own outcome. The one ambiguity that reads as the god naming the WHEN is "He had picked the year." (W-04).
- **Information flow is clean on who hears what.** Mara tells no one, and each cover is true against Ch.13. Two narration lines misstate Ch.13's mechanics:
  - Valens "carried [the word] out of the temple" (W-02). In fact he lost the non-Greek word.
  - The god "heard my question out, from a gladiator, word for word" (W-03). In fact the priest read the question off the wax.
- **1998-era knowledge:**
  - Pliny (with one misattribution, W-07), the town plan, Saint Paul's ship, Neapolis, Halloran's offer and her father's Campanian permit all check out.
  - **The 1988 casts do not.** I found no US showing of Pompeii casts in 1988. The documented tours ran in 1978–79 and 1990–91 (W-01). The brief's premise that the "A.D. 79" show toured in the 1980s does not hold: that tour was 1978–79.
- **Characters:** Kallia's blanket and chores, Valens across the doorway (outline beat 4) and Felix (off the page, his Italy question honored) all hold. Three world slips:
  - a house latrine Ch.7 says Kallia's house does not have (W-05);
  - fig leaves in late winter (W-13);
  - the cliff path's "long turns" against Ch.6's "short zigzags" (W-06).
- **CH13-7:** the cave errand is set for the morning (Valens has gone down for the mules; Mara is to wait "at the bottom of the climb"). Ch.15 must account for the visit.
- **The Ch.10 edit** ("I knew it the way I knew the Armada, as a date on a page with a fire in it.") reads correctly and conflicts with nothing. The bible still quotes an older wording (I-24).
- **Voice:** no tics; gates clean. Drift found by hand:
  - the laugh re-runs Ch.2's Halloran laugh (W-09);
  - paragraph-final negations at about 2.0/1k, against the ≤1.5 watch (W-10);
  - a lying-awake shard coda with a button (W-11);
  - a 4-gram from the reserved Ch.42 sample, with the "painted door" cap now reached (W-12);
  - a narrator call-out pointer (W-08).

---

## Scorecard by category

| Category | Result |
|---|---|
| No-foreshadowing (§0, families A–E) | ✓ 0 breaches. W-04 is ambiguous, not a breach. I-05, I-06 and I-30 were checked and pass. |
| AD 79 as present thought (voice-dna §0.3 "Ch.14: the night she knows") | ✓ "Seventy-nine, late in the summer, in August." gives the month, not the day (the day is reserved for Ch.36). |
| Oracle canon (WHERE given, WHEN withheld) | ✓ l.50 "The god had not said when." W-04 wobbles. |
| 1998-era knowledge | Pliny ✓ except W-07. Plan ✓. Paul ✓. Neapolis ✓. Halloran/permit ✓. **Casts ✗ (W-01).** |
| Information flow (she tells no one; covers true) | ✓ Covers true. W-02 and W-03 are narration slips. |
| Timeline (same night; moon; eight years) | Same night ✓. Eight years ✓. **Moon ✗ (C-01).** |
| Characters (Kallia, Valens, Felix, Thessalians, Theano) | ✓ except W-05, W-08 and W-13. |
| World / geography | W-05, W-06, W-13. |
| Objects (knife, blanket, silver, bowl, jars) | ✓ |
| Plot threads (CH13-7, bowl, Felix/Italy, non-Greek word, CH12-2) | ✓ carried. Cascades in I-16 to I-19. |
| Voice drift (no tics, spent moves, voice-bank, fragmented reflexes) | Gates clean. W-08 to W-12 found by hand. |

---

## PRIORITY: ENTITY_STATE conflicts (processed first)

ENTITY_STATE holds 34 UNRESOLVED flags. The ones Ch.14 touches:

- **CH13-7 (the cave "Tomorrow", info).** Ch.14 keeps the commitment and stages it:
  - l.138 "'Tomorrow,' I had said, about the cave."
  - l.144 "I meant to go up as soon as it was light and find out which."
  - l.152 "He's gone down for the mules… You're to wait for him at the bottom of the climb."

  **Status: carried, not resolved.** The visit itself now falls to Ch.15, as an opening backfill or a clause. Patch below.
- **CH12-2 (the form of the manumission record, low).**
  - l.126 "His own freedom was a line in a book in a record office there." agrees with Ch.12 l.180/200 (the magistrate's book) and Ch.13 l.382 "Mine's written. At Corinth."
  - It does not settle the bound book against outline Ch.17's bronze-and-wax diptych. **Still open.**
- **CH12-4 (sailing season, info).**
  - l.130 "The sailing season closed with the autumn and opened with the spring." agrees with Kallia (Ch.13 l.340) and is compatible with Ch.12's gulf boats. **Still open as recorded.**
- **CH13-3, CH13-6, CH13-8, CH13-13:** not touched by Ch.14.
- **plot_threads.the-non-greek-word:** not resolved by Ch.14. W-02 shows how one line half-touches it.
- No new physical-attribute contradictions. Valens's bruise (left forearm) and the stranger's knife both agree with Ch.12 and Ch.13.

---

## CRITICAL ISSUES (must fix before proceeding)

### [C-01] The moon contradicts the date: the 7th of a lunar month has a half moon up in the evening, not "no moon" and an old crescent at dawn

- **Audit:** Timeline / world rules (calendar).
- **Chapters:** 14 (l.84, l.130, l.148) against 13 (title "The Seventh of Bysios"; l.340).
- **Evidence:**
  - l.84: "There's no moon till the new one," he said. "She'll dig it crooked."
  - l.148: "Before the gray, the old moon rose above the mountain's eastern shoulder, a paring of it, too thin to give any light."
  - l.130: "The boats going west at this new moon were for people who had both."
  - Ch.13 title: the day is the **7th** of Bysios. Ch.13 l.340, Kallia: "The boats go west at the new moon."
  - Ch.13 audit I-12, already on file: "The 7th of a lunar month puts the moon down before dawn."
- **Why it is wrong:**
  - The Delphic year was lunar. A month began at the new moon (the first crescent), and Apollo's day was the 7th.
  - On the 7th the moon is about six or seven days old, near first quarter, roughly half lit.
  - It stands in the southwest at sunset, lights the evening (the laugh is before midnight), and sets around midnight to 1 a.m.
  - An old moon, a thin waning crescent rising before dawn, appears only around days 24–28.
  - The next new moon is about three weeks off. Kallia's Ch.13 line fits that. Valens's "no moon till the new one" does not, and neither does Mara's "this new moon".
  - Valens is a muleteer who moves strings before light, so he is the last man to get the moon wrong. Mara, who has just been registered on a dated consultation day, would also notice.
- **Why CRITICAL:** two time references in the book contradict each other (the day of the month against the phase). The title fixes the day, so the sky has to give way. The fix is cheap and the error is checkable.
- **Suggested fix** (net about +2 words):
  1. **l.84:** "There's no moon till the new one," → **"The moon's down by midnight,"**
     - Keep "she said / She'll dig it crooked." She digs after moonset, in the dark, so the joke survives.
  2. **l.148:** replace the first two sentences with:
     > **"Long before the gray, the half moon had gone down behind the ridge to the west, and the court was black to the walls. I watched the sky over Parnassus's eastern shoulder until it began to pale, and somewhere after that I slept."**
     - This is 43 words, the same as the original.
     - "Parnassus's" also removes the brief ambiguity of "the mountain" (I-03). Elsewhere in this chapter "the mountain" means Vesuvius.
  3. **l.130:** "at this new moon" → **"at the next new moon"** (+1).
- **Cascade risk:**
  - Bible "At-risk after Ch.14": the row "The old moon before dawn … and Valens's 'There's no moon till the new one' … the new moon is now near (Kallia's boats)" must be rewritten. The new moon is about three weeks off.
  - From here the book's moon must count from the 7th: about full around the 14th–15th, new around the turn of the next month (Theoxenios).
  - The latrine shard's "stars … thicker" (l.98) is correct only after moonset. "Some hours on" covers that.
  - Re-run the rhythm gate and the echo scan on the new l.148. "the ridge to the west" and "black to the walls" are untested strings.

---

## WARN ISSUES (should fix)

### [W-01] The February 1988 cast exhibition has no record; the documented US showings were 1978–79 and 1990–91
- **Audit:** World / 1998-era knowledge (outline beat 1; voice-dna §0.2).
- **Evidence:**
  - l.38: "In February of 1988 some of the casts had crossed the Atlantic. I took the train up to see them on a Saturday. I was twenty-three and still a student…"
  - l.40: "…carried the other half in its paper as far as Trenton."
- **The record** (checked this session):
  - **"Pompeii A.D. 79"** toured the US as follows (tour poster and catalogue imprint):
    - Museum of Fine Arts, Boston: Apr–Jul 1978;
    - Art Institute of Chicago: Aug–Nov 1978;
    - Dallas Museum of Fine Arts: Jan–Mar 1979;
    - American Museum of Natural History, New York: Apr–Jul 1979.
  - **"Rediscovering Pompeii"** (IBM-Italia) showed at the IBM Gallery of Science and Art, New York, 12 Jul–15 Sep 1990, then the Museum of Fine Arts, Houston, 11 Nov 1990–27 Jan 1991.
  - I found no showing of the casts in the US in 1988, or in any February.
  - The brief's working premise ("casts toured the US in the 1980s, e.g. 'A.D. 79: Pompeii'") is off by a decade: that tour was 1978–79.
  - The train "up" from Philadelphia, past Trenton, points to New York. New York had the casts in spring–summer 1979 and summer 1990 only.
- **Mitigation, and why it is still WARN:** the page names no venue, so most readers will not notice. But this is a conservator's own memory in a book whose authenticity dial is 8+, and the error is upstream: outline Ch.14 beat 1, voice-dna §0.2/§0.3 and the bible all say "1988".
- **Suggested fix** (the age arithmetic holds either way: Ch.1 l.375 "twenty-six" in Dec 1991 plus Ch.6 l.332 "thirty-three" puts her birth in Dec 1964–Feb 1965):
  - **A (preferred; the documented dates):**
    > "In April of 1979 some of the casts had crossed the Atlantic. I took the train up to see them on a Saturday. I was fourteen and had told my mother I was at a friend's, with a head cold and a book report due on the Monday."

    - +3 words.
    - Her mother is still in the house in 1979 (she leaves in 1981, Ch.1 l.7). Her father is home in April.
    - A fur hat on a cold April Saturday in New York is plausible. The rest of the shard stands.
    - Before committing, **verify against the 1978 catalogue** (*Pompeii A.D. 79*, MFA Boston, 2 vols.) that it lists a human cast and the carbonized loaf. I believe it lists both but could not confirm the entries this session.
  - **B:** summer 1990, the IBM Gallery. She is 25, a graduate student, which fits Ch.3's 1989 department party.
    - The fur hat and head cold need summer replacements.
    - I could not confirm that body casts were in that show. Use B only if the catalogue does.
- **Cascade risk:**
  - outline Ch.14 beat 1 ("a 1988 exhibition … as a graduate student");
  - voice-dna §0.2 and §0.3 ("the 1988 exhibition of the plaster casts");
  - the bible's Mara Ch.14 block and the "1988 casts: SPENT" row;
  - the ENTITY memory fact for Mara.

  Option A drops the Augustan-coinage paper (a credential aside) and nothing else.

### [W-02] "He had carried it out of the temple himself": the antecedent is "the word", which Valens lost
- **Audit:** Information flow.
- **Evidence:**
  - l.78: "It had been there all evening, the word, behind my teeth, with everything that came after it. He had carried it out of the temple himself, and risen under Kallia's gallery and said it all to me without a syllable out of place…"
  - Ch.13 l.174–182: "There was a word in it I didn't know, not Greek, and she gave it twice…" / "I didn't keep it. It wasn't in what he gave me." / "It's gone,"
- **Problem:**
  - Grammatically, "it" is the word "Pompeii". Valens did not carry a city name out of the temple: he carried the priest's verse, and he lost the non-Greek word.
  - Read literally, the line either contradicts Ch.13, or has Mara silently conclude that the non-Greek word was "Pompeii". That would resolve plot_threads.the-non-greek-word off the page.
  - The second half of the sentence ("said it all … without a syllable out of place") is about the verse, so "it" shifts mid-sentence.
- **Suggested fix (+3):** "He had carried **the god's half of it** out of the temple himself…"
- **Cascade risk:** none. The thread stays open.

### [W-03] "heard my question out, from a gladiator, word for word": the priest read the question off the wax
- **Audit:** Information flow / continuity with Ch.13 mechanics.
- **Evidence:**
  - l.62: "And the god of Greece had heard my question out, from a gladiator, word for word, and found me a place in Campania after all."
  - Ch.13 l.162: "He reads the question off the wax, at the screen, in an ordinary voice."
  - The word-for-word carrying was the **answer**, coming out (Ch.13 l.290–292; foundation anchor 13).
- **Suggested fix (+3):** "had heard my question out, **with a gladiator standing for me at the screen**, and found me a place in Campania after all."

### [W-04] "He had picked the year." reads as the god naming the WHEN
- **Audit:** Canon (the Oracle withholds the WHEN) / internal consistency.
- **Evidence:**
  - l.62: "He had outranked Halloran. He had picked the year."
  - l.6: "I knew the year." This defines "the year" as 79.
  - l.50: "The god had not said when. Theano would not say whether he had."
  - STATE canon: the Oracle withholds the WHEN, and Mara hopes for an early door until Ch.36.
- **Problem:**
  - The intended joke is that the god outranked the permit-holder and chose the era.
  - With "the year" pinned to 79 by the opening line, the sentence also reads as Mara conceding that the door is in 79. That undoes l.50 a page later and pre-empts Fenn (Ch.25) and the arithmetic (Ch.36).
- **Suggested fix (0 words):** "He had picked the **decade**." This is the town's last decade, grim and exact, with no WHEN. "the century" also works.

### [W-05] "I needed the latrine": Kallia's house has no latrine (Ch.7)
- **Audit:** Character / world consistency.
- **Evidence:**
  - l.94: "Some hours on, I needed the latrine."
  - Ch.7 l.76: "that night she showed me, without comment, a lidded pot kept beside the jars, and in the morning the dung heap at the lane's end where it went. Delphi's women … had no bodily needs at all outside their own walls…" The only latrine on the page is the men's public one by the market.
- **Suggested fix (+4):** "Some hours on, I needed **the pot by the water jars**."
  - This places it in the court, where l.150 has "the two water jars … beside the wood". The crossing over Valens and the court scene then follow unchanged.

### [W-06] The cliff path: "long turns" here, "short zigzags" in Ch.6
- **Audit:** Geography.
- **Evidence:**
  - l.154: "the path to the plateau scratched up the rock in its long turns"
  - Ch.6 l.324: "onto a path that went at the cliff in short zigzags, cut steps and worn rock and loose stone."
  - Ch.3 l.91's "long zigzags" is the upper slope, a different stretch.
- **Suggested fix (0):** "in its **short** turns" (or "tight turns").
- **Cascade risk:** none. The ending signature stays `long-fade`.

### [W-07] Pliny's letters credited with the town: they never mention Pompeii
- **Audit:** 1998-era knowledge (Pliny).
- **Evidence:** l.46: "The day was in two letters… The mountain opened at midday. Stones fell on the town all that afternoon and all night. Roofs went in under them."
- **Problem:**
  - In context, "the town" is Pompeii and the letters are the source. Neither *Ep.* 6.16 nor 6.20 names or describes Pompeii.
  - The stone-fall in the letters is at Stabiae: the courtyard filling with ash and pumice, the house rocking, pillows tied on against the stones.
  - Roof collapse at Pompeii is excavation knowledge.
  - Mara has translated both letters (l.46), so she would not credit them with the town.
- **Suggested fix (0):** "Stones fell **across the bay** all that afternoon and all night. Roofs went in under them."
  - This is true to the letters and still dreadful.
  - Leave "midday" (Pliny: "about the seventh hour"; foundation: about 1 p.m.). It is a fair round figure in memory.

### [W-08] "Kallia asked me nothing" against "every other piece of it from me, in its order": a seam, plus a narrator call-out pointer
- **Audit:** Character consistency / voice (call-out pointers: bible cap ≤1, "treat it as 0"; Ch.13 W-15).
- **Evidence:**
  - l.20: "Kallia asked me nothing."
  - l.110: "Kallia had had every other piece of it from me, in its order."
  - Ch.13 l.10–12: "I told it in the order it had been given to me."
- **Problem:**
  - The reader is not told when Kallia got "every other piece", given that she asked nothing at supper.
  - "in its order" points back at Ch.13's spring scene. That is the call-out reflex.
- **Suggested fix (+2):** "Kallia had had every other piece of **the day** from me, **over the supper pot**."
  - This removes the pointer and fixes the time: she asked nothing, and Mara told her anyway.

### [W-09] The laugh re-runs Ch.2's: same trigger (Halloran and the permit), same opener, same long-run shape
- **Audit:** Voice drift (situations recur; words must not; bible "the laugh … new shape").
- **Evidence:**
  - l.64: "I laughed."
  - l.66: "…It ran on well after the funny part had gone out of it, and then it stopped."
  - Ch.2 l.69: "I laughed. It came out of me as a bark first and then a long run that bent me over the sink…" This was triggered by Halloran's permit call, the bureaucracy of the dead.
- **Problem:**
  - The outline requires the laugh, and the body work here is new: the wrist, the squeak, dry eyes, the ribs.
  - But the trigger chain ends at Halloran again, the paragraph opens on the identical two-word "I laughed.", and it closes on the same "long run" arc.
  - An evaluator reading Ch.2 and Ch.14 back to back will see a rebuilt beat.
- **Suggested fix (−2):** cut the one-line paragraph l.64. Open l.66 with "**The laugh** was loud, the loudest I had made in that house…" (in place of "The sound was loud"). Optionally change "It ran on well after" to "It went on well after" (0).
- **Cascade risk:** the disruptor kept "I laughed." on purpose. This is the editor's call. If it is kept, vary the run-on sentence at least.

### [W-10] Paragraph-final negations about 2.0/1k, against the ≤1.5 watch
- **Audit:** Voice drift (bible: "Paragraph-final negations: WATCH (Ch.12 ≈2.5/1k; Ch.13 ≤1.5/1k)").
- **Evidence:** six true instances in 3,043 words:
  - l.18 "and I had nothing in my hands."
  - l.32 "and got only the benches."
  - l.50 "with nothing going past it but a dog."
  - l.70 "I had not heard him move."
  - l.140 "That door went home with no sea in the way, and no town."
  - l.154 "…and nobody on it yet."

  l.78's "no more idea … than the cat" is a seventh by a strict count.
- **Suggested fix** (recast two; net +1):
  - l.18 "and I had nothing in my hands." → "**and my hands were empty.**" (−2)
  - l.70 "I had not heard him move." → "**He had come up off the blanket in silence.**" (+3)
  - Keep the dog, the sea and the ending.

### [W-11] The S4 closer is a lying-awake coda with a button, in a chapter with five shard-end kickers
- **Audit:** Voice drift / fragmented-chapter reflexes (Ch.8 eval P5 "lying-awake coda", tracked in every eval since; disruptor: "One kicker per shard is still about the most a fragmented chapter can carry before it reads as a device").
- **Evidence:**
  - l.52: "I lay with my face to the roof beams and kept hold of that."
  - Shard-end kickers: S2 l.32 (benches), S4 l.52, S6 l.90 (fish sauce), S8 l.134 ("and it held"), S9 l.144 ("find out which").
- **Problem:**
  - The disruptor deliberately kept S6, S8 and S9. S4's line adds nothing they don't already do.
  - "kept hold of that" clicks the shard shut. It is the one most like a device.
- **Suggested fix (−4):** move "I lay with my face to the roof beams." to open the l.50 paragraph ("I lay with my face to the roof beams. The god had not said when…"). Drop "and kept hold of that". The shard then ends on the dog on the tomb road.

### [W-12] A reserved voice-bank 4-gram, and the "painted door" at-risk cap now reached
- **Audit:** Voice drift (voice-dna §6: "No sentence, image or line from any sample may be reused"; bible at-risk: "the painted door", max 2).
- **Evidence:**
  - l.32: "I tried for most of an hour to call up **a painted door on** any of them"
  - sample-07 l.12 (the reserved Ch.42 door sample): "**a painted door on** a dead man's tomb."
  - Uses of "painted door": Ch.13 l.342 (1) and Ch.14 l.32 (2).
- **Suggested fix (+1):** "to call up **a painted tomb door** on any of them". This breaks the 4-gram and the verbatim at-risk string.
- **Cascade risk:** record "the painted door" as **2/2 used**. Ch.19, 30, 36 and 41–42 must use "the false door", "the dead man's door" or fresh words.

### [W-13] Fig leaves in late winter
- **Audit:** Period/season (authenticity dial ≥8).
- **Evidence:**
  - l.20: "with their share of the sacrifice wrapped in fig leaves."
  - Ch.13 l.6: the same dawn "under a frost so hard that Kallia's jars rang".
  - Ch.13 l.28: almonds in first full flower.
- **Problem:**
  - The fig is deciduous and leafs out in April–May.
  - On the 7th of Bysios (about February–March) at Delphi's altitude the trees are bare.
  - Valens's figs are this book's running subject (Ch.11; Ch.15 "the figs that aren't ripe"), so a fig slip will be noticed.
- **Suggested fix (0):** "wrapped in **cabbage** leaves" (a winter crop), or "wrapped in a cloth".

---

## INFO (polish / tracking / cascades)

**Sequence and image**
- **I-01** l.150 / l.154: "Kallia stood at the gate with the bar in her hands." then "She took the bar down". If the bar is already in her hands, it is already down. Fix: "with **her hands on the bar**" (+1).
- **I-02** l.154: "gray at their feet first and then, very slowly, a paler gray along the rim". In twilight the sky behind a rim brightens first, and Ch.13 l.38 brings the light down from the top. This is defensible (the faces lit by skylight, the rim last against a paling sky), but worth a second look. Leave it if the editor prefers the line, because it carries the long fade.
- **I-03** "the mountain" means Vesuvius at l.6, l.62 and l.130 ("years ahead of the mountain"), and Parnassus at l.148. C-01's fix names Parnassus.

**Phrasing and voice**
- **I-04** "the word" stands in for Pompeii three times in narration (l.6, l.78, l.90). The chapter never names the town, which is right. To keep the stand-in from settling into a device, l.6 "closed on the word" → "closed on **the name**" (0).
- **I-05** l.128: "Eight years was plenty of time, I told myself." This is self-knowledge within the moment and passes the §0 test. It is not a forward reach. Keep.
- **I-06** l.140: "The last time I had been up there". It contains the banned-family string "the last time I", but it faces backward (Ch.8's January visit; Ch.8 l.164 has the hand in "to the wrist", which l.140 renders "my own arm"). It passes. "When I was last up there" (−1) would dodge an evaluator's reflex.
- **I-07** l.90: "To everybody under that roof it was a town in Italy where they made fish sauce."
  - Nobody under the roof has heard the word, so "**would have been**" (+2) is the stricter logic.
  - The fact is good: Pliny, *NH* 31.94, praises Pompeii's garum.

**1998-era knowledge verified**
- **I-08** Pliny:
  - *Ep.* 6.16 and 6.20 to Tacitus, written about 106–107: "nearly thirty years" ✓.
  - "in his eighteenth year" = seventeen ✓.
  - Livy and the extracts ✓.
  - "a boy of nine now": born late 61 or 62, so 8 or 9 in spring 71; acceptable.
  - "north of Italy": Comum; "somewhere" covers it.
  - "had no good word for" (the surge) ✓. Bible: these details are now SPENT until Ch.39–42.
- **I-09** Town plan:
  - Fiorelli's regions, insulae and doors (1858) ✓.
  - The Faun (the statuette in the impluvium) ✓. The Tragic Poet (the actors' mosaic) ✓.
  - Forum at the west end, long and narrow ✓. Via dell'Abbondanza east to the Sarno Gate ✓.
  - Herculaneum Gate schola benches ✓. Nuceria road tombs (excavated in the 1950s; known by 1998) ✓.
  - **Cascade:** she now remembers the Nuceria road. Ch.19 trying the famous Herculaneum road first is still natural, but don't let her "discover" that the Nuceria road has tombs.
- **I-10** Halloran and Emilio:
  - Ch.1 l.359: the "Campanian survey season" *permesso*, deadline 20 April.
  - Ch.2 l.53–97: the last Saturday in March; the empty flat; "a room in the dig house … with a window … So that you could see it."; "I might be in Greece."; signed on Wednesday, 1 April 1998.
  - l.56–60 agree on every point: "in March", "the bare floor of a flat he was leaving", "a room with a window in it", "I had said Greece, perhaps.", "signed it over to Halloran in April".
  - The September homecomings agree with Ch.1 l.23, Ch.3 l.51 and Ch.13 l.342. "next year" agrees with canon (he never took her abroad).
  - Neapolis was still a Greek-speaking city in AD 71 ✓.
  - The Campania blind spot left by Ch.13 (Ch.13 audit I-29) is owned implicitly by "found me a place in Campania after all" ✓.
- **I-11** Saint Paul: Acts 27–28, an Alexandrian ship that had wintered at Malta, to Puteoli, about AD 59–61. "ten or eleven years" and "in chains" ✓.

**Information flow, characters and objects**
- **I-12** Information flow, everyone under the roof:

  | Who | Knows | How |
  |---|---|---|
  | Valens | the verse, the Etna gloss, that Theano sent for Mara, "Theano's jar was empty", the Amphissa well (retold) | Ch.13 plus l.16 and l.80 |
  | Valens | NOT "Pompeii" ✓ | |
  | Kallia | the verse (from the lean-to), the day's "other pieces", "her stool" | Ch.13 l.100 plus l.112 |
  | Kallia | NOT the name ✓ | |
  | Felix | the verse, "Italy" as his own guess | Ch.13 l.332 |
  | Felix | not present tonight ✓ | |
  | The Thessalian father | nothing | |

  The covers are true: the jar (l.10); the well (Ch.13 l.206–264, "this morning" ✓); the stool (Ch.13 l.440, l.482). The word is said "with no sound in it" (l.90) ✓.
- **I-13** Kallia:
  - The blanket (l.116, l.150) ✓.
  - Her chores are Mara's chores from Ch.6 l.308 (ashes, hearth, water) ✓.
  - She never sits ✓. She touches objects, not people (the blanket dropped over his feet) ✓.
  - Her lines are task- and carrier-oriented ("One of those priests could carry it down for her," "It isn't their knees.") ✓.
  - "folded in four" (l.150) repeats the situation of Ch.6 l.308 ("I folded the blanket in four"). That is a 3-gram, and the gate is clean. Optional: "folded small".
- **I-14** Valens:
  - Across the doorway: outline beat 4 ✓, set up by Ch.13 l.386–394 ✓.
  - The knife is the stranger's (Ch.12 l.74, l.156) ✓. The bruise is on the left forearm (Ch.13 l.48) ✓.
  - No simile in his speech ✓. Deliberation pause 0 ✓. No exit by gait ✓.
  - The father "sat on his heels" (l.98) is a squat the kneel/crouch regex does not catch (Ch.8 l.8 "down on her heels" is a second). The book-wide rate stays under 0.3/1k even counting both.
  - **Pipeline note (root):** add "(sat|down) on (his|her|my|their) heels" to the class in `tic_report.py`.
- **I-15** Felix: "if it was Italy" ✓ (Ch.13 l.332). Asleep with the string (Ch.13 l.390) ✓. "He's gone down for the mules" fits the yard down the Kirrha road (Ch.11 l.144) ✓.
- **I-16** CH13-7: staged for the morning ✓. Ch.15 must give the visit a clause or a backfill. The bible spends the cave descriptors.

**Threads and records**
- **I-17** Euthydikos's bowl (l.124) agrees with Ch.13 l.226–236. The plan (winter in Delphi, then the bowl, then sail) differs from outline Ch.15–16 (Corinth in autumn). Ch.15 or 16 must register the change of plan or pay off the bowl.
- **I-18** plot_threads.the-non-greek-word: untouched. Keep it untouched (W-02).
- **I-19** l.126 "a line in a book in a record office" agrees with Ch.12's "magistrate's book" (CH12-2 still open against the outline's diptych).

**Small polish**
- **I-20** "in a book" appears twice in the chapter (l.28 "a plan in a book", l.126). Optional: vary one.
- **I-21** l.102, the Thessalian: "Every mile, it told us." A Greek on a non-Roman road would count stades. "**Every step of it**, it told us." (+1).
- **I-22** l.98: "the stars were thicker than Philadelphia had ever let me see them". This is the book's second Philadelphia superlative (Ch.3 l.11 "green in a way nothing in Philadelphia was ever green in May") and a stock observation. It is also correct only after moonset (C-01). Optional recast.
- **I-23** "woodpile" (l.20) against Ch.13's "woodstack" (l.100, l.290, l.296) for the same object. Align to "woodstack".
- **I-24** Theano's jars: l.10 "her jar stood empty" and then "her big jar". Two jars, briefly unclear. "her **water** jar stood empty" (+1).

**Syncs**
- **I-25** The Ch.10 edit, l.68: "I knew it the way I knew the Armada, as a date on a page with a fire in it."
  - It reads correctly. It still means Jerusalem (the antecedent "it"), and the Armada's fire is the fireships.
  - It no longer collides with Ch.14's opening "I knew the year." (voice-wear clean).
  - It conflicts with nothing in Ch.5 (the herald, Josephus) or Ch.14.
  - **The bible is stale here:** its Tool/text note says Ch.10 "now reads 'the way I knew the date of the Armada'". The page dropped "the date of", which avoids "date … a date". Sync the bible to the page.
- **I-26** **Bible lag (Ch.14 block and "At-risk after Ch.14"):** it quotes the Writer's draft, not this page:
  - "Her water carried." → page "Theano's jar was empty." / "She kept you."
  - "He had not troubled with a permit." → "He had outranked Halloran."
  - "Every year there was next year. Next year there was never room." → "Every year it was going to be next year, and then next year there was never a spare bed."
  - "What a single person in that town…" → "What anybody in that town…"
  - "one man set down in two letters to Tacitus" → "as much of it as one man set down for Tacitus"
  - "deliberation pause 1 (He weighed me a while longer.)" → cut, now 0.
  - Add the plaster-hand return (l.42).
  - Plus the C-01 and W-01 cascades.

**Pass notes**
- **I-27** Eight years: spring AD 71 (l.48 "the spring was only started") to late August 79 is eight years and about five months. "a little over" ✓. "A year to get there. Seven, after that" sums to eight ✓. Spring 72 sailing agrees with outline Ch.15, 18 and 19 ✓.
- **I-28** l.40: "On the train home I bought a pretzel from the man with the cart". Northeast Corridor trains had café cars, not cart vendors. Optional: "at the station". W-01's option A keeps the train.
- **I-29** voice-dna §0 E: Kallia's plaster leads to the memory of the casts. This is Part One and unpointed (no line links her trade to what the ash will do). It passes.
- **I-30** Forward-facing lines checked:
  - l.144 "I meant to go up…" (intention).
  - l.154 "nobody on it yet" (this half hour).
  - l.88 "One word, and he would be awake again. He would ask…" (conditional).
  - l.124–132 the plan in conditionals and modals.
  - l.142 "After that the one door left … would be the door the plan ended at".
  - l.134 "and it held" (present judgment; the irony is the reader's).

  None narrates her outcome.
- **I-31** The laugh is not one of foundation's three "breaks" (Ch.6, 20, 22). It is the outline's designed surprise and stays private. ✓ The bible notes that Ch.22's fit needs a fifth laugh shape.
- **I-32** Ch.13 l.20, Kallia: "the Thessalians will be up at the sanctuary till dark". Ch.14 l.20 has them home roasting as the sun leaves the temple roof. This is trivial: a family with a sick boy comes home early.

---

## Word ledger (recommended fixes only)

| Fix | Δ words |
|---|---|
| C-01 (l.84 +1, l.148 0, l.130 +1) | +2 |
| W-01 option A | +3 |
| W-02 | +3 |
| W-03 | +3 |
| W-04 | 0 |
| W-05 | +4 |
| W-06 | 0 |
| W-07 | 0 |
| W-08 | +2 |
| W-09 | −2 |
| W-10 (l.18 −2, l.70 +3) | +1 |
| W-11 | −4 |
| W-12 | +1 |
| W-13 | 0 |
| **Net** | **+13 → about 3,056** (floor 3,000) |

INFO extras, if taken: I-01 +1, I-07 +2, I-21 +1, I-24 +1. Dialogue share stays about 4.8% (dialogue-side edits: C-01 +1).

---

## SUGGESTED YAML PATCHES (for the entity-tracker UPDATE after the editor's fixes)

```yaml
suggested_patches:
  - entity: "meta.contradictions.CH13-7"
    action: "update"
    value: "Ch.14 keeps the errand: l.138 \"'Tomorrow,' I had said, about the cave.\"; l.144 'I meant to go up as soon as it was light and find out which.'; l.152 Kallia: 'He's gone down for the mules … You're to wait for him at the bottom of the climb.' The visit itself falls to Ch.15 (backfill or clause)."
    reason: "carried, not resolved"

  - entity: "timeline / locations.delphi (moon)"
    action: "add"
    value: "7th of Bysios AD 71: moon ~6-7 days old (near first quarter), up in the evening, sets ~midnight; next new moon ~3 weeks off (Kallia's westward boats)"
    reason: "C-01; record AFTER the editor replaces l.84/l.148/l.130 (do not record the post-disruptor 'old moon' or 'no moon till the new one')"

  - entity: "mara-reyes.memories (the casts)"
    action: "update"
    value: "pending W-01: venue unnamed; date to be set by the editor (recommended April 1979, AMNH New York, age 14); NOT 'February 1988'"
    reason: "no 1988 US showing found; documented tours 1978-79 and 1990-91"

  - entity: "mara-reyes.knowledge"
    action: "add"
    value:
      - { fact: "Pompeii = AD 79, late summer, August (month only; the day is reserved for Ch.36)", learned: "ch-14 l.6", method: "own 1998 knowledge" }
      - { fact: "the god's verse decoded: Vesuvius, the bay, the tombs outside the gates; the door's WHEN unknown ('could open on any day in eight years')", learned: "ch-14 l.6; l.50" }
    reason: "Ch.14 knowledge acquisition"

  - entity: "knowledge_index.pompeii-name"
    action: "add"
    value: "knowers: Mara (Theano told her), Theano. NOT Valens, Kallia, Felix. Valens is told in Ch.15 (outline)."
    reason: "the information-flow table, I-12"

  - entity: "plot_threads.euthydikos-bowl"
    action: "update"
    value: "Ch.14 plan: wait the winter in Delphi, do the bowl, sail in spring (l.124). It diverges from outline Ch.15-16 (Corinth in autumn): Ch.15/16 must register the change or pay it off."
    reason: "I-17"

  - entity: "plot_threads.the-non-greek-word"
    action: "keep_open"
    reason: "Ch.14 does not resolve it; after W-02 the l.78 line no longer implies it"

  - entity: "kallia.traits / objects.kallias-blanket"
    action: "add"
    value: "brown, burned at one corner by a coal (l.116); dropped over Valens's feet; folded on the threshold at dawn (l.150)"
    reason: "new object detail"

  - entity: "walk-ons"
    action: "create"
    value:
      - "thessalian-father (Larisa; big, black-bearded; the ram family's father) l.98-106"
      - "thessalian-youngest-son (sick on the god's fat) l.98-106"
      - "fountain-woman-with-jug ('the whole street was thirsty, not only Syracuse') l.10"
      - "fur-hat-woman and husband (memory, the casts) l.38"
    reason: "new walk-ons in Ch.14"

  - entity: "locations.theanos-house"
    action: "add"
    value: "the lion's-head fountain with moss under its lip, where the street turns below her house (l.10); a big storage jar inside by the hearth (l.10)"
    reason: "new location fact"

  - entity: "at-risk registry (bible, not YAML)"
    action: "note"
    value: "'painted door' 2/2 used (Ch.13 l.342, Ch.14 l.32); later uses must vary"
    reason: "W-12"
```
