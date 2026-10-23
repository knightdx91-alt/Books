# Continuity Check: Chapter 26, "Letters in English" (manuscript audit vs Ch.1–25)

**Date:** 2026-10-24
**Scope:** `manuscript/chapters/chapter-26.md` as it stands after dialogue-polish, hook-craft (no edits) and the disruptor. Checked against Ch.1–25 (targeted greps: Ch.1 the answering machine and tape, Ch.2 Fenn's 1967–68 documents, Ch.3 the knucklebone, Ch.11/16/21/24 Felix, Ch.19 the rooms, Ch.20 Grata and the fig frame, Ch.21 the stair, Ch.24 the birth machinery, Ch.25 Fenn in full). Also checked against ENTITY_STATE.yaml (tracked to Ch.25; the parallel Ch.26 UPDATE was read only, not edited), outline Ch.25/26/27/28/31/35, foundation §3/§4f/§10, STATE.yaml guardrails and AUTHOR-* decisions, voice-dna §0/§1, and character-bible (Voices from lives; FENN, VALENS, FELIX, GRATA, LUCIUS, AELIA, EMILIO, MARGARET, SECUNDUS; At-risk after Ch.24/25/26).
**Line refs** are file lines in chapter-26.md (header comments l.5–6; prose l.8–250).
**Dialogue share now:** 619 / 5,618 = 11.0%. With every fix below applied it is about 10.8%, still at or above the 10% floor.
**Total:** 6 CRITICAL · 19 WARNING · 18 INFO

**Clean on:**
- No "Vesuvius" and no "mountain" anywhere (CP5-1).
- No "Margaret". Mara keeps the name in the satchel (l.82).
- No tomb. The door appears once, as a thing not written about (l.40).
- "citizen" ×0 (CP4-1). "by degrees" ×0.
- No laugh from Mara and no mouth beat.
- Nothing from Ch.24's birth machinery: no teeth, stool, glue, watch winding, jar-lift, "whole?", Floralia cloth or night-hour stamps.
- No lent adult moods on Aelia (objected / grievance / suspicion / studied / regarded ×0).
- "Nobody had [verb]" ×1 (l.16). "kept … to myself" ×0. "Nobody knows" ×0.
- No Fenn narrated states appear in the narration. "slowly" ×0. "figure" (verb) ×1 (l.132). "Get out" ×0. "nobody … but me" ×0 (the dialogue pass fixed it). "kid" ×1 (noun).
- Fenn's promise and "one door with many mouths" are not quoted. No Zippo.
- "In the finder" ×0. The camera left/right layout is not used.
- The who-pays / "Whose …?" question frame is closed and does not appear as a question (see I-12).
- Spoken "Then…" ×1 (l.170).
- The echo scan and tic gate are clean, per the pass reports.

**Period facts verified:**
- **1964.** On Sunday 27 Sept 1964 (counted from 1 Jan 1964, a Wednesday, the date is a Sunday) the Braves beat the Phillies 14–8 at Connie Mack Stadium, 21st & Lehigh. Johnny Callison hit three home runs. It was the seventh straight loss. Chico Ruiz stole home on Monday 21 Sept, so "the Sunday after Chico Ruiz" is the 27th. "they've dropped six straight" and "six days of that" are both exact. Callison played right field, so "sit up in right" fits. The 23 ran on Germantown Avenue to Chestnut Hill. A three-hour game plus a walk of six to seven miles puts dusk around Mount Airy, which is plausible. All correct.
- **1997.** On Sunday 26 Oct 1997 the Marlins beat Cleveland 3–2 in Game 7, in 11 innings, so a voicemail on "the Monday morning" fits. The franchise first played in 1993 ("isn't as old as your car"). The cap was teal and black with the gold sticker. All correct.
- **Fenn's departure.** Ch.2 has "*Athens on the second of April, TWA.*" and, in July, "*Back before Labor Day*". The note's "Home by Labor Day" (l.62) agrees.
- **Phone canon.** In Ch.1 the answering machine is Emilio's: the two-tape Panasonic in his kitchen, and the microcassette is his greeting. Mara's work is a basement lab with a fax (Ch.2). Office voicemail with a red message light in 1997 fits that, and it does not touch the Ch.1 machine. Emilio died in January 1998, so he was alive in October 1997. The message matches his card: a cheerful run that ends on an invitation and names no date.
- **Ages.** Aelia was born in winter 75–76, so she is about 3 yr 7–8 mo in late summer 79. Fenn's "near four" is his round figure, and the foundation's 3½ holds. Lucius was born in July 74 (Ch.24, "the dead heat"), so he is about 18–20 months across the chapter, matching outline Ch.26 "about eighteen months". Felix was about twelve in 71 (Ch.11) and gave "Fifteen, then. Sixteen." in 73–74 (Ch.21). "seventeen that winter" fits, and so does Ch.28's "eighteen" in AD 76.
- **The eighth day and the crescent.** The dies lustricus for a girl was the eighth day (Lucius had the boy's ninth in Ch.24), and a girl wore a lunula. Correct.
- **Ink.** Carbon ink of lampblack and gum lifts with a wet sponge while it is fresh. Correct.

---

## CRITICAL ISSUES (fix before the evaluator)

### [CRIT-001] The family's rooms are now upstairs over the street; Ch.19 put them on the ground floor behind the shop
- **Audit:** World rules / geography (Ch.19 rooms; ENTITY CH26-1 logged the same thing independently)
- **Lines:** 88, 116, 120, 122, 126, 210, 216, 232
- **Description:** Ch.19 l.245 says "Behind the shop lay two rooms with a door between them. The back one had a bed frame …, a window set high up onto a light-well, and a stair of wooden treads climbing the outside of the house at the back to the roof." Ch.20–25 keep that layout ("at the table in the back room", Ch.20 l.119; the roof stair, Ch.21 l.74–88). No page moves the family. Ch.26 gives the bedroom an upper floor with a street shutter and an inside stair.
- **Evidence:**
  - l.88 "pacing the shop below among the customers' pots … until I came down"
  - l.116 "I stood at the upper shutter with her as Valens passed below with the string … a clear voice that reached me at the window"
  - l.120 (Grata) "that loud one up there at the window"
  - l.122 "Felix came past below at the tail and asked up the wall"
  - l.126 "The street rose to the shutter … I held Aelia up to the gap in the shutter"
  - l.210 "went upstairs with it … Downstairs again,"
  - l.216 "Lucius had the bone upstairs."
  - l.232 "A slab of sun lay in from the upper shutter over the blanket"
- **Fix (move dawn to the shop opening; keep the bed in the back room):**
  - l.88: "pacing the shop below" → "pacing the shop"; "until I came down" → "until I came through"
  - l.116: "at the upper shutter with her as Valens passed below" → "in the shop opening with her as Valens passed"; "that reached me at the window" → "that reached me"
  - l.120: "that loud one up there at the window" → "that loud one in there"
  - l.122: "came past below at the tail and asked up the wall" → "came past at the tail and asked"
  - l.126: "The street rose to the shutter" → "The street came past the boards"; "to the gap in the shutter" → "to the gap in the boards"
  - l.210: "went upstairs with it" → "went through to the back with it"; "Downstairs again," → "Back in the shop,"
  - l.216: "Lucius had the bone upstairs." → "Lucius had the bone by the bed."
  - l.232: "from the upper shutter" → "from the light-well"
  - All of these were grepped and none appears in Ch.1–25. Ch.19's "the high window" and Ch.20's "in the back room" were avoided on purpose.
- **Cascade:** After this fix, the stair Lucius climbs in l.184 is the outside roof stair. That is consistent with Ch.19 and Ch.21. Grata's room stays through the plaster, which works because the two back rooms share a wall. The dialogue share drops by 3 words.

### [CRIT-002] Grata reads Fenn's Greek aloud, but she cannot read
- **Audit:** Character consistency (GRATA card, "**Cannot read:**")
- **Lines:** 14, 44
- **Description:** In Ch.20 Grata "had a carter read it back to her before she would pay me", and she "had the panel read to her by her son as he set off to bathe" (Ch.20 l.433). The bible records this as **Cannot read**. In Ch.26 she reads a Greek horoscope aloud to her customers. The tracker's CH26-3 reads the two pages as compatible, but the card is explicit. "squinting at my own accounts" (l.44, added by the dialogue pass) also implies that she reads.
- **Evidence:**
  - l.14 "Grata had read it aloud in her counter voice to every customer that day, Jupiter and all."
  - l.44 "and me squinting at my own accounts."
- **Fix:**
  - l.14: "Grata had read it aloud in her counter voice to every customer" → "Grata had it read out to every customer". This also removes a narrated habit, "counter voice".
  - l.44: "me squinting at my own accounts" → "me at my own accounts".
  - Neither string appears in any earlier chapter, and the dialogue pass's "can't read" is not restored.
- **Cascade:** None. Ch.31 must keep her unable to read the rival notices she whitewashes.

### [CRIT-003] The item-by-item look (CLOSED book-wide) appears three times in the frame scene
- **Audit:** No tics / closed devices (At-risk after Ch.5 and Ch.20: the item-by-item look and its two-item form are CLOSED, and "the item-by-item gaze over a body stays CLOSED"; Ch.25 CRIT-004 precedent)
- **Lines:** 244, 246
- **Evidence:**
  - l.244 "He watched me, then his father, then me." The look goes X, Y, X, which is the closed two-item form.
  - l.244 "The rest of him did not stir at all, not his arms, not his toes." This is a body inventory in negative.
  - l.246 "I turned the focusing ring until the dust in his eyebrows came clear, and the sun through the rim of his ear, and the water the lip had brought up in his eyes." This is a three-item gaze over a face. "His eyes ran over." follows two sentences later and carries the tears on its own.
- **Fix:**
  - l.244: "He watched me, then his father, then me." → "He watched me."
  - l.244: cut ", not his arms, not his toes"
  - l.246: cut ", and the sun through the rim of his ear, and the water the lip had brought up in his eyes"
- **Cascade:** None. The frame keeps the lip, the held breath, the gust and the eyes running over.

### [CRIT-004] The Ch.25 pronunciation frame is rebuilt one chapter later
- **Audit:** No tics: frames repeated from earlier chapters
- **Line:** 112
- **Description:** The accent-anatomy frame is: a letter sound, then a lengthened vowel, then Philadelphia as the yardstick. Ch.25 l.192 has "He said it the Philadelphia way, with a d in the middle of it and the vowel pulled out long." Ch.26 rebuilds every part of it for Valens's "goodnight". The family also appears in Ch.4 l.41, Ch.7 l.326, Ch.19 l.151 and Ch.25 l.58.
- **Evidence:** l.112 "At the second the pieces ran together, with the d gone soft and the vowel stretched past anything a Philadelphian would do with it."
- **Fix:** cut ", with the d gone soft and the vowel stretched past anything a Philadelphian would do with it". The sentence now ends "At the second the pieces ran together."
- **Cascade:** None.

### [CRIT-005] Command echo (SPENT book-wide at 3 since Ch.9; Ch.25 CRIT-005 precedent)
- **Audit:** No tics / retired devices
- **Lines:** 242, 246, 250
- **Evidence:**
  - l.242 "Hold her," I told Lucius in Latin. "Don't move."
  - l.246 "…in one gust that lifted her hair, and moved nothing else." This repeats the verb of the order as compliance.
  - l.250 "…holding her very carefully…". This is the order's verb again, at the close.
- **Fix:**
  - l.242 → "Don't move," I told Lucius in Latin.
  - l.246: cut ", and moved nothing else"
  - The order and the release ("You can move now.") stay as a pair, and nothing in between repeats them. The closing "holding her" is no longer an echo (see WARN-09 for "very carefully").
- **Cascade:** The dialogue share drops by 2 words.

### [CRIT-006] Fenn's anaphoric negation triad, and a second list (Fenn: "No enumerating, numbering or listing habit, ever"; retired define-by-negation; Ch.25 CRIT-006 precedent)
- **Audit:** Voice drift against the FENN card / retired reflexes
- **Lines:** 132, 152
- **Evidence:**
  - l.132 "Not who's in the White House, not what they get for a pack of Luckies, just who won it the last fall you were there." This is a sentence-initial "Not X, not Y, just Z".
  - l.152 "I've got the Greek for every star there is over this roof and the Latin for half the fish in the bay, I can tell a Syrian sailor from an Egyptian one by how he swears". This is a three-item list of his skills.
- **Fix:**
  - l.132: cut the whole sentence. "Just that." already closes the question, and "ninety-seven" already dates it.
  - l.152: cut " and the Latin for half the fish in the bay". Two items read as a rant, not a list.
- **Cascade:** None. The vow-breaking stays in "Sure, I said it, with my own mouth in my own room, so sue me." (see I-07).

---

## WARNING ISSUES

### [WARN-01] A forward reach in the narration about the letter's future
- **Audit:** NO FORESHADOWING (voice-dna §0, family A; it is also next to family E, because it is about preservation)
- **Line:** 12
- **Evidence:** "A drop of milk had already landed on the Walt Whitman Bridge and dried there in a small glazed blister, which the next damp day would sink into the fibers for good."
- **Fix:** cut ", which the next damp day would sink into the fibers for good".

### [WARN-02] Aelia's life projected forward
- **Audit:** NO FORESHADOWING (outline Ch.26: the anchor "must not be rendered as an outcome")
- **Line:** 126
- **Evidence:** "in the language she would hear all day from everybody but me at night"
- **Fix:** "she would hear" → "she heard".

### [WARN-03] The narrator singles out Fenn's "the summer"
- **Audit:** Law: "Fenn's own 'the summer we go' is allowed; the narrator never comments on it"
- **Line:** 18
- **Evidence:** "She had it from me three times over, the rope walk and the bridge and the peanuts and the summer, in the voice I would have used to read out a recipe."
- **Description:** "the summer" is the last and stressed item, and the flat recipe voice around it reads as a comment.
- **Fix:** cut " and the summer".

### [WARN-04] Three exits before Mara can answer (a nameable rule in one chapter)
- **Audit:** No tics / nameable-rule test
- **Lines:** 122, 142, 202
- **Evidence:**
  - l.122 Felix "had rounded the corner by the fullery before I had answered any of it."
  - l.142 "She was out in the rain again with me still deciding whether I ate standing up."
  - l.202 "He was out and away with no answer from me, whistling, with his hand already flat on the doorpost to swing himself round it."
- **Description:** The third instance also puts a hand flat on a post, which echoes Felix's palm on the gatepost at Ch.21's close and the book-wide "hand flat" class (Ch.3, 4, 6×2, 11, 12, 18).
- **Fix:** l.202 → "Till autumn." He was out and away, whistling. Mara now answers (the sailing season), the device breaks, and the dialogue share gains 2 words. Grepped: neither phrase appears in Ch.1–25.

### [WARN-05] Felix's "Is it…" form returns three times; "Is it gold?" repeats his Ch.16 "Is that gold?"
- **Audit:** Voice / closed refrain (Ch.16 CRIT, "Felix's 'Is it' x10"; FELIX Ch.21 WATCH "Is it" openers 2)
- **Lines:** 192, 200
- **Evidence:**
  - l.192 "Is it from the Chaldean? It's heavy for letters. Is it gold? It's gold, I'd know that weight anywhere."
  - l.200 "…Is it open for good?"
- **Fix:** l.192 → "From the Chaldean? It's heavy for letters. It's gold, I'd know that weight anywhere." This keeps his boast and one "Is it" (l.200).

### [WARN-06] Voices from lives: narrated habits and a remark on Valens's reticence
- **Audit:** AUTHOR-CP5-0b (no one remarks on a habit; nameable-rule test) / narrated-trait census
- **Lines:** 12, 22, 112
- **Evidence:**
  - l.112 "But he had asked me for something, which he did seldom enough that I noticed it each time, and I gave him goodnight." This remarks on Valens's plainness and makes the rule nameable ("he seldom asks").
  - l.12 "Fenn, who wasted nothing he had bought, had flipped it". This names the sunk-cost rule that Ch.25 SPENT ("You finish what you pay for").
  - l.22 "He had slept that way since he could choose." This is a narrated habit on top of a shown posture.
- **Fix:**
  - l.112: cut ", which he did seldom enough that I noticed it each time,"
  - l.12: cut "who wasted nothing he had bought," → "Fenn had flipped it and written to me on the clean side of the blot."
  - l.22: cut the sentence.
- **Census after the fixes and CRIT-002:** ≤2 narrated traits per character (Valens: the sleep and the English; Lucius: the mule-gazing; Aelia: everything in her mouth, which is her age-stage card; the dun: "where she liked it").

### [WARN-07] Talking to objects and animals: three instances (cap ≤1)
- **Audit:** At-risk WATCH ("[X] told [object]" ≤1 per two chapters; the "said to the [thing]" family flagged since Ch.4/5)
- **Lines:** 36, 122, 126
- **Evidence:**
  - l.36 Fenn "talked American at the ceiling" (in his own letter)
  - l.122 Valens "gave it to the dun as well" (the planned wrong use)
  - l.126 "a woman told a dog what she thought of it"
- **Fix:** l.126: cut ", and a woman told a dog what she thought of it". In the same paragraph, "the loaves and the boys and the dog" → "the loaves and the boys and the bucket".
- **Description:** The dun keeps the word, and Fenn's ceiling stays as his own prose. "a dog barked" was rejected because Ch.15 and Ch.20 already use it.

### [WARN-08] Margaret is given lines
- **Audit:** MARGARET card: "never quoted directly … she is never given a line"
- **Lines:** 60, 62
- **Evidence:**
  - l.60 "my sister says we're going, and I say going where, they've dropped six straight, and she says that's where, someone's got to be there"
  - l.62 "She says she's not getting on a 23 with a carful of grown men bawling, she's had six days of that already"
- **Description:** These are reported in Fenn's present tense, but they have the rhythm of direct speech, and two of them are hers.
- **Fix:**
  - l.60: "my sister says we're going, and I say going where, they've dropped six straight, and she says that's where, someone's got to be there, and her good coat's on already" → "they've dropped six straight and my sister's good coat's on already"
  - l.62: "She says she's not getting on a 23 with a carful of grown men bawling, she's had six days of that already, and she starts walking." → "She starts walking."
  - If the editor rules that reported speech is allowed, amend the card instead. Do not do both.
- **Cascade:** The period-reference count for the 23 goes back to 1 of 2.

### [WARN-09] "very carefully" is the 4th use book-wide
- **Audit:** No tics (any non-allowlisted phrase recurring 3+ times book-wide)
- **Line:** 250
- **Evidence:** Ch.17 l.308 and l.350, Ch.21 l.360, and Ch.26 l.250 "holding her very carefully". The hook report raised the same watch.
- **Fix:** cut "very carefully," so the line reads "…with his lip in her fist, holding her, until his father lifted her away." The outline phrase was a design note ("the Writer finds the image"). This is protected text, so it is the editor's call.

### [WARN-10] The film timeline misdates the fig frame
- **Audit:** Objects / timeline (film-roll; foundation §4f)
- **Line:** 230
- **Description:** The fig frame is Ch.20 S2, summer AD 72, which is three and a half years earlier, not about a year.
- **Evidence:** "I had spent no frames that winter, nor in the whole year before, since the frame of Valens sleeping in the fig's shade."
- **Fix:** → "I had spent none since Valens asleep in the fig's shade."
- **Cascade:** If no frames were shot off the page between AD 72 and 76, the shot count after Ch.26 is 12, and frames 13–36 remain for 76–79 (Ch.27, Ch.38's frame 36, and off-page frames). This is for the tracker. It contradicts nothing.

### [WARN-11] The knucklebone has been in "the satchel since the Corycian"
- **Audit:** Object custody (ENTITY: maras-satchel first named in Ch.25, needs_review; the 1998 bag was the duffel; tracker CH26-4)
- **Line:** 48
- **Evidence:** "It had ridden in the bottom of the satchel since the Corycian"
- **Fix:** "the satchel" → "my bags". Grepped: the phrase is not in Ch.1–25.

### [WARN-12] Grata's Secundus grudge explains Ch.31's whitewash in advance
- **Audit:** Plot threads / Ch.31 setup (outline Ch.31 subversion: "it sets up nothing"; GRATA card: "Her whitewash is not shown or explained")
- **Line:** 140
- **Evidence:** "…when every soul in Pompeii knows that wall's my boy's, and I know who, and so will he, and soon."
- **Description:** The threat makes the planned irrational behavior a rational revenge. The notice also stands more than a year before the election of March AD 77 (tracker CH26-7). That is possible but early.
- **Fix:** cut ", and I know who, and so will he, and soon" (−9 dialogue words). Keep the grievance.
- **Cascade:** Ch.31 can treat the campaign as already under way. It must not pay off a Ch.26 "baker's son".

### [WARN-13] Fenn's invitation to Cumae is not in any letter (outline divergence)
- **Audit:** Plot threads (outline Ch.26 "Opens toward Ch.27: Fenn invites her to Cumae"; Ch.27 "Builds on Ch.26: his invitation"; the bible's Ch.27 guard records the omission; tracker CH26-6)
- **Fix:** No Ch.26 edit. The orchestrator either has Ch.27 carry the invitation itself (preferred, because Ch.26's letters are closed) or patches the outline's Ch.26/27 progressive lines.

### [WARN-14] CASCADE: Ch.35's hall-table beat is now partly spent
- **Audit:** Plot threads (outline Ch.35: "1968, in his words: Philadelphia, the morning he left, the note on the hall table")
- **Line:** 62
- **Evidence:** "That's where I left her the note, the morning I went. … Home by Labor Day, I put. A line about the milk."
- **Fix:** No Ch.26 edit. Add a cascade note to outline Ch.35: the note's wording and "the morning I went" are SPENT, so Ch.35's 1968 needs new material (and Margaret's name is still unsaid until then).

### [WARN-15] The camera release is rebuilt for a third time (shutter, mirror, advance)
- **Audit:** No tics / weight carriers "rendered in fresh words every time" (voice-dna §0)
- **Line:** 246
- **Evidence:**
  - Ch.3 "The shutter went; the mirror slapped up and dropped" plus winding on with the thumb
  - Ch.16 "The shutter clacked … the mirror clapping up and back behind the glass"
  - Ch.26 "I let the shutter go. The mirror jumped behind the lens against my brow, and I thumbed the lever round for the next frame."
- **Description:** "thumbed" is also one of the prop-gate verbs.
- **Fix:** cut "The mirror jumped behind the lens against my brow, and I thumbed the lever round for the next frame." End on "I let the shutter go." This also removes the device-adjacent beat two lines before the close.

### [WARN-16] Word wear
- **Audit:** No tics (narrator word habits)
- **Lines:** 38, 190, 216, 244
- **Evidence:**
  - "singly", 9th use, in its 8th chapter (Ch.6, 8, 9, 17, 20, 23, 24, 26). Ch.24's "pulled them singly" is the same use (removing things one at a time). l.38 "unbend the fingers singly".
  - "unasked", 5th use (Ch.13, 15, 19, 24, 26). l.244 "He stopped breathing as well, unasked,".
  - "since the Kalends" twice in consecutive sections (l.190, l.216).
- **Fix:**
  - l.38: cut " singly"
  - l.244: cut " unasked,"
  - l.190: "that was new since the Kalends" → "that was new"

### [WARN-17] "whole" ×6, three of them on the children's bodies
- **Audit:** At-risk after Ch.24, Ch.26 guards ("no 'whole' as the designed word"; Ch.24's evaluator flagged "whole" density)
- **Lines:** 16, 62, 88, 156, 230, 244
- **Fix:**
  - l.156: "her whole fist" → "her fist"
  - l.244: "Lucius set about it with his whole body." → "Lucius set about it."
  - l.230 goes with WARN-10.
  - This leaves 3 (l.16, l.62 Fenn's "whole shebang", l.88).

### [WARN-18] The cedar box may read as opened
- **Audit:** Outline beat 4 NON-NEGOTIABLE ("unopened")
- **Line:** 210
- **Evidence:** "The lid slid in its groove, and he had found the groove with his thumbnail before I had finished reading."
- **Fix:** → "He had found the lid's groove with his thumbnail before I had finished reading."

### [WARN-19] A Ch.27 setup note on the knucklebone (pre-spend risk)
- **Audit:** Ch.27 setup (outline Ch.27 beat 4: "Lucius rolls the knucklebone down the gallery")
- **Lines:** 48, 216
- **Description:** Ch.26 has already shown the rolling ("it rolled, and was fetched, and rolled again"; "setting it on its flat side and pushing it off his palm. He sent it skittering away").
- **Fix:** No Ch.26 edit. Ch.27's roll must use none of rolled / fetched / skittering / flat side / palm. Record this in At-risk after Ch.26 (it is partly recorded already).

---

## INFO

- **I-01. 1964 geography.** Germantown Avenue is about ten blocks east of 21st & Lehigh. "every block of it" is Fenn's hyperbole, and it fits his voice. No action.
- **I-02. The summer letter "read once … at the vintage" (l.58) and "The autumn letter had come at the vintage" (l.130).** Grata's "he'll leave it on a bench at Herculaneum like he did in the autumn" (l.140) is consistent with both arriving late together. The carter's route (Puteoli, coast road, Herculaneum, Pompeii, and on) is consistent with Ch.25 ("Any carter on the road knows Grata"). No action.
- **I-03. The P.S. "Your old man. I'm sorry." (l.208).** Fenn's knowledge has a path: Ch.25 l.114 "where my father lived" (past tense) and her letter's voicemail line. Either reading of the P.S. works (her father's death, or his own rant). No action.
- **I-04. Five mules at dawn (l.116) against the four that crossed in Ch.18/19.** A purchase off the page in four years is plausible (tracker CH26-2). No action.
- **I-05. "feet, which were new to him" (l.216) at about 19–20 months.** This is late but within the normal range. "planted himself at the bedside" (l.48) weeks earlier suggests he was standing by then. No action.
- **I-06. Fenn's "the summer we go" (l.10) assumes Aelia goes through the door.** This is his confident future tense (his card), not an answer to Ch.25's "No idea". It is allowed. The narrator makes no comment on it once WARN-03 is applied.
- **I-07. The vow.** "Sure, I said it, with my own mouth in my own room, so sue me." (l.132) reads as him breaking Ch.25's "not another word", defensive and sheepish, and the cue is clear. This resolves ENTITY CH25-6(b).
- **I-08. Valens's English word.** It is quoted once ("Goodnight.", l.118). It also appears in narration within the same beat (l.112, l.122). No later callback is allowed in any form (forward constraint).
- **I-09. The cedar box.** No reason is narrated anywhere. Lucius under the bed (l.216, "The feet went still while he worked at it in there") never names the box. Pass.
- **I-10. Voicemail and answering machine.** See "Period facts". Pass.
- **I-11. Secundus is named on the page for the first time (l.140).** He was unnamed in Ch.19 and Ch.20. The tracker logged CH19-3 and CH26-7.
- **I-12. Who-pays.** "Don't let your landlady pay me." (l.36) is a statement, and "Who carries it?" (l.152) is about how the post works. Neither is the closed cost/ownership question frame. Leave them, or cut "Who carries it?" if the evaluator reads it as the frame.
- **I-13. Fenn's caps.**
  - Period references: Chico Ruiz is now 2 of 2 (SPENT). The 23 / Germantown Avenue is 2 of 2 (SPENT; 1 if WARN-08 is applied). Callison 1. The El on Market Street and the Walt Whitman Bridge are new.
  - Idiom: holy cow 1, the whole shebang 1, knock it off 1, monkey's uncle 1, so sue me 1, tickled pink 1, pipe down 1, okay 2 (4 book-wide; not in the pool).
- **I-14. "the 34" in Mara's narration (l.136).** This is her own route (Ch.25 l.114), not Fenn's idiom. Pass.
- **I-15. Ch.27 and Ch.29 setup.**
  - The automat is mentioned with no pie (l.36), so Ch.27's lemon meringue needs a trigger other than the letters or the copper.
  - The scorecard's "every little diamond" (l.60) means Ch.27's dust diamond should not reuse "diamond" alongside "little".
  - Mara has given Valens a one-line gloss of baseball (l.74), so Fenn's Ch.29 explanation must not repeat it.
  - Felix's eyebrow cut and his lie (l.190–198) are consistent with the Ch.28 backfill. Nothing is spent, and the palm scratch is held for Ch.28.
- **I-16. Bakers as a time marker ×4 (l.18, 28, 38, 126).** This is at the edge. Optional: l.38 "until the bakers were at their oven" → "until near light".
- **I-17. The knucklebone is "since somebody's goat died" (l.48); Ch.3 has "a sheep, maybe a small goat".** Compatible. No action.
- **I-18. Fenn self-reports "talked all night" (l.36).** The narrated state "talking on" is SPENT as narration only, and in his own letter this is his voice. Pass.

---

## TRACKING NOTES (append to the databases)

- **Timeline.**
  - Spring 75: the first letter, within a month of Puteoli.
  - Summer 75: the 1964 letter, reaching her at the vintage.
  - Vintage 75: the autumn letter (1997 and the birthday melon).
  - Winter 75–76: Aelia is born off the page. The birth letter arrives by her 3rd week. Night reading: week 3. The walking night: week 4. The crescent: day 8. Rope and word: week 5, with "Goodnight." at the next dawn. Reply: week 6. Rage letter: 9 days later. The tables: the tail of winter. The frame: near winter's end, in sun.
- **Knowledge.**
  - Valens knows: the letters come from Puteoli; the "side" lost a game; Fenn has a sister, unnamed; Fenn is angry over a word; one English word. He has no date, rules or place.
  - Fenn knows: Aelia's name and hour; 1997 Florida; the word "voicemail" (unexplained); that her father left the message.
  - Grata: the stars, read to her (after CRIT-002).
  - Felix: the box is from the Chaldean, and it is heavy.
- **Objects.**
  - The tables' copy is in a cedar box under the bedstead, unopened.
  - The letters are in the satchel on the notebook.
  - The knucklebone is with Lucius.
  - The Pentax is on a shelf in a cloth. The Ch.26 named frame is shot.
  - The bronze crescent on a red thread is on Aelia.
  - The strainer is patched (three rivets).

## SUGGESTED YAML PATCHES (for the entity-tracker's next UPDATE; not applied)

```yaml
suggested_patches:
  - entity: "conflicts.CH25-6"
    action: "remove_conflict"
    reason: "part (b) resolved by ch-26 l.132 'Sure, I said it … so sue me' (the vow broken on the page); part (a) resolved by the new 1964 material"
  - entity: "conflicts.CH26-1"
    action: "keep_original"
    reason: "Ch.19 layout (back room, light-well window, outside roof stair) is canon; Ch.26 lines to be repaired per CRIT-001"
  - entity: "conflicts.CH26-3 / pomponia-grata.traits (reading)"
    action: "keep_original"
    reason: "cannot read (Ch.20; bible); Ch.26 l.14 repaired per CRIT-002"
  - entity: "conflicts.CH26-4 / objects.maras-satchel"
    action: "update"
    reason: "after WARN-11 the page says 'my bags since the Corycian'; satchel stays needs_review, not merged with the duffel"
  - entity: "objects.film-roll.frames_shot_ch26"
    action: "add"
    value: { value: 1, subject: "Lucius holding newborn Aelia, his lip in her fist", note: "page states no frames since the Ch.20 fig frame (summer AD 72) once WARN-10 is applied; plan count 12 shot" }
  - entity: "secundus.first_named"
    action: "add"
    value: { chapter: 26, source: "ch-26 l.140", note: "a notice for him by the baths, winter AD 75-76; election March AD 77 (Ch.31)" }
  - entity: "plot_threads.fenn-invites-cumae"
    action: "update"
    reason: "not in Ch.26; Ch.27 must carry it (WARN-13)"
  - entity: "august-fenn.period_references"
    action: "update"
    value: { chico_ruiz: "2 (SPENT)", route_23_germantown: "2 (SPENT) or 1 if WARN-08 applied", callison: 1 }
```

---

## Fix summary for the editor (all subtractive or same-length swaps; all replacement strings grepped against Ch.1–25)

| ID | Line(s) | Change |
|---|---|---|
| CRIT-001 | 88, 116, 120, 122, 126, 210, 216, 232 | upstairs/upper shutter → shop opening / back room (swap strings above) |
| CRIT-002 | 14, 44 | "Grata had it read out to every customer"; "me at my own accounts" |
| CRIT-003 | 244, 246 | "He watched me."; cut "not his arms, not his toes"; cut ear/eyes from the focus line |
| CRIT-004 | 112 | cut the d/vowel/Philadelphian clause |
| CRIT-005 | 242, 246 | "Don't move," I told Lucius in Latin.; cut ", and moved nothing else" |
| CRIT-006 | 132, 152 | cut the "Not … not … just" sentence; cut "and the Latin for half the fish in the bay" |
| WARN-01/02/03 | 12, 126, 18 | cut "which the next damp day…"; "she heard"; cut "and the summer" |
| WARN-04/05 | 202, 192 | "Till autumn." He was out and away, whistling.; drop two "Is it" |
| WARN-06 | 112, 12, 22 | cut the "seldom" clause, "who wasted nothing he had bought," and the sleep-habit sentence |
| WARN-07 | 126 | cut the woman and the dog; "the boys and the bucket" |
| WARN-08 | 60, 62 | Margaret's reported lines out (or amend her card) |
| WARN-09 | 250 | cut "very carefully," (editor's call: protected line) |
| WARN-10/11 | 230, 48 | "I had spent none since Valens asleep in the fig's shade."; "my bags" |
| WARN-12 | 140 | cut ", and I know who, and so will he, and soon" |
| WARN-15/16/17/18 | 246, 38, 244, 190, 156, 210 | cut the mirror/lever sentence; cut "singly", "unasked,", "since the Kalends", "whole" ×2; "He had found the lid's groove…" |

---

## Repair log (book-editor, 2026-10-24)

Pre-repair backup: scratchpad only (not in repo). `bash tools/check_chapter.sh 26` → **ALL MECHANICAL GATES CLEAN** (echo scan 0, tic gate clean, voice-wear strict clean, shape clean). After: shape 5,315 words (was 5,617); dialogue ≈11% (≈600 quoted words), above the 10% floor.

| ID | Status | How |
|---|---|---|
| CRIT-001 | done | Audit swaps at l.88 ("pacing the shop", "until I came through"), l.120 ("that loud one in there"), l.122 ("came past at the tail and asked"), l.126 ("gap in the boards"), l.210, l.216 ("by the bed"), l.232 ("from the light-well"). Varied from the audit where the echo scan or the page objected: l.116 "stood in the shop opening with" (echo of Ch.20/21) → "At daybreak I had her in the shop as Valens passed with the string"; "in a clear voice that reached me" → "in a clear voice:" (she is a few feet away now); l.126 "The street came past the boards" (three "boards" in one paragraph) → "The street went by"; l.210 "went through to the back with it" (echo of Ch.13) → "carried it through", "Back in the shop," kept. No upper floor anywhere; the stair in l.184 is the outside roof stair. |
| CRIT-002 | done | "Grata had it read out to every customer"; "me at my own accounts". |
| CRIT-003 | done | "He watched me."; cut "not his arms, not his toes"; cut the ear and the eye-water from the focus line. |
| CRIT-004 | done | Cut the d/vowel/Philadelphian clause. |
| CRIT-005 | done | `"Don't move," I told Lucius in Latin.`; cut ", and moved nothing else". |
| CRIT-006 | done | Cut the "Not … not … just" sentence; cut "and the Latin for half the fish in the bay". |
| WARN-01 | done | Cut the damp-day clause. |
| WARN-02 | done | "she heard". |
| WARN-03 | done | Cut "and the summer" from the l.18 recap. Fenn's in-letter "the summer we go" untouched. |
| WARN-04 | done | l.202 → `"Till autumn."` / "He was out and away, whistling." Also cut l.142 ("She was out in the rain again…"), so the pattern stands at one (Felix at dawn, l.122). Grata's section now ends on her own line. |
| WARN-05 | done | "From the Chaldean? It's heavy for letters. It's gold, …" One "Is it" left (l.200). |
| WARN-06 | done | All three cuts (Valens "seldom" clause, "who wasted nothing he had bought," and the sleep-habit sentence). |
| WARN-07 | done | Cut the woman and the dog; "the boys and the bucket". To reach ≤1, also cut "at the ceiling" from Fenn's first letter ("talked American till the gulls started up"); the dun keeps the word. |
| WARN-08 | done | Editor's ruling: trim, card unchanged. "The Sunday after Chico Ruiz they've dropped six straight and my sister's good coat's on already …"; "She won't take the trolley home, after. She starts walking." The 23 is now 1 of 2. |
| WARN-09 | skipped | Editor's ruling: "very carefully" stays (outline image, protected closing line). |
| WARN-10 | done | "I had spent no frames since the one of Valens asleep in the fig's shade." ("none" alone lost its noun after "the roll had not run out".) |
| WARN-11 | done | "my bags since the Corycian". |
| WARN-12 | done | Cut ", and I know who, and so will he, and soon". The grievance stays. |
| WARN-13 | skipped | Outline cascade, orchestrator's call; no Ch.26 edit. |
| WARN-14 | skipped | Outline cascade (Ch.35), orchestrator's call. |
| WARN-15 | done | Cut the mirror/lever sentence; the frame ends "I let the shutter go." |
| WARN-16 | done | Cut "singly", "unasked,", and "since the Kalends" at l.190. |
| WARN-17 | done | "her fist"; "Lucius set about it." |
| WARN-18 | done | "He had found the lid's groove with his thumbnail before I had finished reading." The lid stays shut, and no reason is given. |
| WARN-19 | skipped | Ch.27 constraint only; no Ch.26 edit. |
| I-16 | done | l.38 "until the bakers were at their oven" → "until near light" (bakers as a time marker down to 3). |
| I-12 | skipped | "Who carries it?" stays. It is Fenn asking how the post works, not the closed frame. |
| Other INFO | no action | As the audit says. |

Protected text checked after the repair: the first sentence of the opening letter and the closing photograph sentence are unchanged; "Goodnight." is spoken once; the box stays unopened with no reason; Fenn's one voicemail outburst is intact; nothing the dialogue or disruption passes cut has come back; the mountain is not named.
