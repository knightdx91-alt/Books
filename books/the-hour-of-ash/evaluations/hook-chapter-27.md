# Hook-Craft Report: Chapter 27 "Cumae"

**Verdict: both ends work. No edits. The chapter file is unchanged.**

## Opening (Hook)
- **Type:** QUESTION. Not VOICE ✓ (Ch.26 was VOICE).
- **Score:** 8/10 (Information gap 3/3, Emotional pull 2/3, Voice 2/2, Connection 1/2)
- **Rewritten:** no.
- **First sentence:** *"I had expected the Sibyl's cave to be a door, a live one, cool under the hand and quiet in the way the Corycian had been quiet on the morning I crawled into it, and I had expected it on no better evidence than Fenn's refusal to tell me what was in there."* 51 words, starts with "I", and the claim is about what she expected the cave to be, so it meets the ledger. shape_check reads it as `I-statement` ✓.
- **Why it grabs:** "had expected" tells the reader the cave will turn out to be something else, and that is the question the whole chapter answers (it is a door, but a dead one, and it is Fenn's). The second clause adds a second gap: Fenn will not say what is in there. Sentence two grounds the scene straight away (Puteoli wharf, evening, the baby held up at arm's length), and Fenn's first line arrives before the reader has time to drift. One strong hook, and it is a question rather than a voice hook. It is the same type as Ch.24, but that was three chapters back, so it is legal.
- **Connection (1/2):** Ch.26 closed on the photograph of Lucius and Aelia. This opens on Aelia in Fenn's hands and on doors, so it carries on the thread of her children rather than the scene itself. That is adequate. The chapter does not open with a recap.
- **Alternatives considered (not used):** IN MEDIAS RES on Fenn holding Aelia up (7). That throws away the ledger's I-statement and the chapter's central question. TICKING CLOCK on how far it is to walk there and back before dark (6). The deadline would be fake and the tone wrong. TICKING CLOCK stays unused.

## Ending (Pull)
- **Type:** QUESTION PLANT. Not EMOTIONAL GUT PUNCH ✓ (Ch.26 was GUT PUNCH).
- **Score:** 8/10 (Forward pull 2/3, Emotional charge 3/3, Unpredictability 1/2, Promise 2/2)
- **Rewritten:** no.
- **Is it a real long fade, or a spoken button?** A real fade. The question is planted in the exchange ("Write me... Just that it's cold." / "And if it isn't?" / "It will be,"), but the chapter does not end on that line. A full narrative paragraph follows: the last rise, the lamps, then a 52-word final sentence that runs down with the light. shape_check reads it as `long-fade` ✓. Fenn's "It will be" sits mid-exchange and does not act as a button. The prose then takes the energy down without letting it go slack. The question is left open: why does Fenn need to keep hearing that Eros's door is dead?
- **Foreshadowing check:** clean. The purple runs "from the far shore inward, the water first and then the long hills across it". That is the earth's shadow at dusk, plural "hills", with no single peak picked out and no smoke or steam. The steam and sulphur stay back at the hot ground in S2 and do not come back at the close. The mountain is never named in the chapter (grep for mountain/Vesuv is clean). The narrator shows no dread and the chapter has no "for eleven more days" line. "watching the color go out of everything except the lamps" is a concrete thing she sees, not an aphorism. No tic or device closes the scene. Fenn never says or implies "don't end up like me". He asks for news that the door is cold and gives no reason, which is exactly the gap.
- **Ch.28 pre-emption:** none. Felix is never mentioned at the close, so nothing at home is hinted at, and the news on their return stays untouched.
- **Midnight test:** passes, but quietly. The chapter is a slow walk home, so the page-turn comes from the open question about the door and from where the lamps lead (home, and whatever is there). It does not come from a jolt. That suits this genre (threshold 7) and this register.
- **Alternatives considered (not used):** end on "It will be," said Fenn (DECISION/button, 6). That breaks the ledger and is exactly the spoken button the brief rules out. Add an ominous line at the lamps (OMINOUS PROMISE, 5). That would be narrator dread and would point straight at Ch.28.

## Break transitions (3)
1. **S1 to S2 (line 74):** she won't ask whether it is a door because "people... could not leave them be". The next section starts in the yard with Valens and the jenny. **Strong.** The question she won't ask carries over the white space.
2. **S2 to S3 (line 236):** "what I had wanted was gone. I wrapped the camera in its cloth again." The next section opens on the ridge path and Cumae coming into view. **Adequate.** The close is soft, but the new section moves fast and puts the destination in front of the reader within three sentences. No edit, because this is the middle and outside my remit.
3. **S3 to S4 (line 394):** the carbon of the coat sits unread in the satchel while Fenn stands at his mark, "quite comfortable". The next section opens on Lucius drawing in the dust. **Strong.** The dramatic irony carries on underneath the play scene.

## Chain Check
- **Previous chapter pull:** EMOTIONAL GUT PUNCH (Ch.26). **This hook:** QUESTION. **Transition momentum:** adequate to strong.
- **This pull feeds Ch.28 ("Felix in the Arena"):** yes, by placement only. The lamps and the homecoming hand over straight to the news on return. Nothing is given away.

## Type Diversity
- Ch.21 IN MEDIAS RES / QUESTION PLANT → Ch.22 SENSORY / DECISION POINT → Ch.23 CONTRAST / EMOTIONAL GUT PUNCH → Ch.24
  QUESTION / QUESTION PLANT → Ch.25 SENSORY / DECISION POINT → Ch.26 VOICE / EMOTIONAL GUT PUNCH → **Ch.27 QUESTION /
  QUESTION PLANT**. No consecutive repeats. TICKING CLOCK is still unused. It fits neither end of this chapter.

## Verification
- `bash tools/check_chapter.sh 27` (run unedited) prints **ALL MECHANICAL GATES CLEAN**.
- `python3 tools/shape_check.py books/the-hour-of-ash` gives Ch.27 `I-statement` / `long-fade`, which matches the ledger row.
- Dialogue is still 35.3%. Nothing was edited, so no spoken line was added and NO TICS still holds. The mountain is not named.
