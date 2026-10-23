# Dialogue Polish Report — Chapter 26 ("Letters in English")

## Audit Summary
- **Dialogue ratio:** 11.2% before → **10.9% after** (shape_check; band 10–20%). The letters are italic, not quoted, so they do not count.
- **Words (shape):** 5,645 → 5,621
- **Conversations analyzed:** 9. Grata through the wall; Grata on the eighth day; Valens and the 1964 letter; dawn "Goodnight." / Grata; Grata collecting the reply; the carter; Valens at night; Felix with the tables; the bone and the frame. Six Fenn letters audited separately.
- **Lines flagged INDISTINCT:** 0
- **Lines flagged WEAK:** 2 (Mara's stiff baseball explanation; the carter reads a little Grata-ish) → 1 resolved; the carter was left as is (functional walk-on, one line)
- **FLAT_DIALOGUE flags:** 0. Valens's jealousy comes through as mind-reading ("She sleeps for that.") and is never named.
- **Exposition dumps:** 0
- **Tag overuse:** 0. Tags are sparse and mostly beats. No new gesture beats were added.
- **Guard violations found:** 6 → 6 resolved (see below)

## Voice Distinctiveness Results
| Character | Lines | Distinct | Weak | Indistinct | Post-Polish |
|-----------|-------|----------|------|------------|-------------|
| Valens | 22 | 22 | 0 | 0 | DISTINCT |
| Mara | 20 | 19 | 1 | 0 | DISTINCT |
| Grata | 5 speeches | 5 | 0 | 0 | DISTINCT |
| Felix | 3 | 3 | 0 | 0 | DISTINCT |
| Carter (walk-on) | 1 | 0 | 1 | 0 | WEAK (acceptable) |
| Fenn (6 letters) | — | all | 0 | 0 | DISTINCT. The 1968 idiom and the "and"-chains sit far from Mara's 1998 narration |

## Changes Made (15 edits; narration untouched apart from one dialogue beat)
### Guard / constraint fixes
- **Who-pays / "Whose …?" frame (CLOSED):**
  - Felix's "is it money, does he send you money? What's he want back for it?" is now "Is it gold? It's gold, I'd know that weight anywhere." The stacked-question burst is kept and his boast comes back.
  - Grata's "knows whose wall that is" is now "knows that wall's my boy's".
- **Spoken line from an earlier chapter:** the rage letter's "Don't you dare explain it to me" repeated Ch.25's "Don't you dare,". It is now "Don't explain it to me, I mean it."
- **"nobody … but" frame (WATCH at 2, no third):** Fenn's "nobody here knows it but you now" is now "as of this letter that's one person around here who knows it".
- **Recurring epithet:** "the big fellow" (birth letter) plus "Mrs. Big Fellow" (first letter) made a nickname for Valens. The birth letter now says "Tell your mister I said so." "fellow" in the chapter is down from 5 to 3 ("a carful of fellows" is now "a carful of grown men").
- **Refrain risk:** "The tables are coming" appeared in two letters. The rage letter now closes with "*Tables soon. A. F.*", a tired four-word fragment after the outburst.
- **Grata's "My man" ×2 in one speech (WATCH):** the second is now "He'd call the moon…".
- **Teeth (the Ch.26 guard on Ch.24's birth machinery):** the beat "with the thread's knot in her teeth" is now "knotting the thread". The action is the same; no new gesture.
- **Word-wear:** "all square" is cut from the first letter, because "square" was ×3 in the chapter. Grata's "since market day" is now "in a week" ("market" ×3 in her mouth).

### Stiff rewordings / continuity
- **Mara's baseball explanation:** "Men who play at a game with a stick and a ball … They lost, and she made him walk home." is now "Men who hit a ball with a stick, in his city, when he was young. He went to watch them with his sister. She made him walk home after, the length of the city." This drops the repeat of "His side lost a game".
- **Valens's "All that way up a street with her":** he does not understand the English letter, so he could not know there was a street. Mara now gives him "the length of the city", and his line is "All that way with her, and no name."
  - The second sentence of his old line echoed Mara's "He doesn't put her name" back at her and pointed at the subtext. It is cut.
  - Mara's "It's uphill, that street." still lands.
- **1964 letter:** "she saw plenty of that on the TV Monday" was unclear. It is now "she's had six days of that already", tied to "dropped six straight" (27 Sept 1964 was the seventh loss).
- **Grata on the eighth day:**
  - "writing her letters of her own" is now "writing to this one".
  - "me with my eyes going over my own accounts" was ambiguous. It is now "me squinting at my own accounts".

### Gate-driven variations (made in this pass)
- "I can't read" (Grata) would have been the 3rd book-wide use, so it is now "squinting".
- "Can I see" (Felix) would have been the 3rd book-wide use, so it is cut.
- "before he came over" echoed Ch.21, so it is now "when he was young".

### Checked and left alone
- **"Goodnight."** It is spoken once on the page (to Grata). The night scene and the dun get it only in narration, and it is never called back. Grata answers it as a greeting, and nobody corrects or explains.
- **The rage letter** is one real outburst: jokes ("I got used to Claudius"), then "Voice. Mail.", then "Nobody said they'd go on making new ones without me". It never mentions her father, and nothing in the chapter repeats it.
- **Valens's lines:** no comparisons, and the only "why" is practical. "Then use the ones he knows." is the chapter's only spoken "Then…" opener (1 of ≤2).
- **Fenn's idiom** stays within the bible caps: holy cow 1, the whole shebang 1, knock it off 1, monkey's uncle 1, so sue me 1, tickled pink 1, okay 2. There is no numbering or listing.
- **Protected text:** the first sentence of the opening letter and the closing photograph sentence are byte-identical to the draft.
- **Names:** there are no instances of "Vesuvius" or "Margaret". The mountain is not named.

## Remaining Concerns (Writer/Editor)
- **Narration I did not touch (the dialogue-only rule) that may explain what the scene shows:**
  - "The dun had never thrown her head at anybody in her life, and he knew I knew it." (§7)
  - "Before him, the only English ever spoken aloud in that street had been mine. He had handed his to Grata … and she had accepted it." (§4)
  - "I could not argue with that, and he knew it, and it did not please him." (§3)
  - The evaluator should judge these.
- **character-bible.md is now stale** where it quotes changed strings. Downstream sync should replace:
  - FELIX: "is it money … What's he want back for it?"
  - GRATA: "My man would call the moon…" and "whose wall"
  - FENN: "nobody here knows it but you now", "Don't you dare explain it to me", "The tables are coming." in letter 5, and "the big fellow"
  - VALENS: "All that way up a street with her."
  - The At-risk after Ch.26 WATCH entry for Grata's "My man" (2) is now 1.
- **Dialogue share is 10.9%,** close to the floor. Later passes should not cut quoted lines without replacing them.

## Cover-the-Name Test: FINAL
- Grata through the wall: PASS
- Grata, eighth day: PASS
- Valens / 1964 letter: PASS
- Dawn "Goodnight." / Grata: PASS
- Grata collecting the reply: PASS
- Carter: PASS (weak but functional)
- Valens at night: PASS
- Felix / tables: PASS
- Bone and frame: PASS
- Fenn letters vs Mara narration: PASS. The gap between 1968 and 1998 is audible and never explained.

**Mechanical:** `bash tools/check_chapter.sh 26` prints ALL MECHANICAL GATES CLEAN (echo scan 0, tic gate clean, voice-wear strict clean).
