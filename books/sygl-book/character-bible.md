# Character Bible — Sygl

> **Purpose.** The canonical home for the cast's VOICE and DISTINCTNESS — one entry per NAMED
> character. This is a **living document**: the Writer ADDS an entry the moment a new named character
> first appears on the page (book-writer rule), so a cast that grows across many chapters never drifts
> into sounding alike. The Architect seeds it; every downstream agent writes FROM it. Each entry ends
> with a **DISTINCTNESS GUARANTEE**.
>
> Seeded 2026-10-20 from `Sygl_Complete.txt` (the canon), `project/foundation.md` §0/§3/§7,
> `project/outline.md`, STATE.yaml `decisions`, the CLAUDE.md canon guardrails, and the finished
> chapters `manuscript/chapter-01.md` … `chapter-10.md`. **Source facts only (author law for this
> book):** nothing here invents backstory, habits or quirks. Where foundation.md and the source differ,
> the source and the STATE.yaml decisions win. Where the source gives nothing for an axis, the card says
> "source silent — keep to function". Sample lines are quoted from the finished chapters (Ch.N) or the
> source (p.N / the chapter the outline assigns them to); the dialogue rule lets the Writer polish
> wording but never meaning, speaker or placement.
>
> POV reminder: close third on **Bal only**, past tense. Every other character's voice reaches the page
> only through what they say aloud and what Bal sees. Their inner lives are never narrated.

## How distinctness works here (read before adding a character)

Distinctness is **NOT** "give everyone a verbal tic." A cast where every character has a catchphrase
reads as machine-made — it is the most common way a large cast collapses into one voice wearing hats.
Distinguish characters on **four axes** first:

1. **Attention / worldview** — what they NOTICE and reduce the world to (the deepest differentiator).
2. **Syntax / register** — sentence shape and formality (clips vs spirals; subordinates vs fragments).
3. **Evasion** — what they will NOT say (subject, register, or feeling they refuse).
4. **Physicality / silence** — the body-tell or pause that stands in for a spoken tic.

## NO TICS (author's standing law, 2026-10-18 — hard, every book)

- **Tic-bearer roster: NONE.** No character — narrator included — leads with a verbal tic,
  catchphrase, refrain or pet phrase. Every card's tic line reads `none — distinguished by <axis>`.
- **No devices.** Counting, listing, pricing, rating, cataloguing are one device in different coats,
  and it is retired for everyone — not rationed to one character. (Thad reading casualty figures off a
  report in Ch.22 is a source beat, once; it is not his "thing".)
- **Motifs are objects and situations, never lines.** The style-gate ALLOWLIST holds ≤5 phrases, each
  capped at 3 uses book-wide. This book's motifs: blood given freely; the wooden Dawn cards and the name
  Norheart; hands and palms; runes (foundation §5).
- **THE AMELIA LESSON:** in an earlier book a quantifying/counting device and the phrase "never once"
  calcified into a tic AND bled across characters until the cast sounded alike, needing a
  manuscript-wide de-tic. The earned tics spread too — hence zero. Watch that the POV narrator's
  habits do NOT bleed onto secondary characters. (Note: this book's goddess shares the name Amelia
  with that lesson. Coincidence of name only; the lesson applies here doubly.)
- **Enforced every chapter:** `voice_wear_check.py` (self-repetition FAILS), `tic_report.py --gate`
  (any non-allowlisted phrase 3+ times book-wide, or any spoken 3+-word phrase recurring, FAILS). This
  book uses the flat `manuscript/chapter-NN.md` layout: run both on a scratch copy laid out as
  `manuscript/chapters/` (see the book's CLAUDE.md).

### The book's two author-ruled exceptions (2026-10-20) — exactly two, no others

1. **"Master."** Amelia may call Bal "Master." It is a familiar's title for her bonded mage, a form of
   address and **not a tic**. Use it **sparingly**: where the source uses it ("You called, Master?" and
   "Okay, master!" in Ch.9; "Of course, Master" at the chalice in Ch.28) or where the familiar
   relationship makes it natural. Never build a joke on repeating it. **Status (author ruling 2026-10-20):** source uses only — Ch.9's three, Viridia's Ch.10 line about it, and the
   Ch.28 "Of course, Master." The invented uses in Ch.3, 4, 7 and 8 were removed. Nobody else uses it as address
   (classmates quoting it with scorn, as in Ch.10, is reported speech, not usage).
2. **The stuck-out tongue happens once each, as the source has them, never again:** Amelia (Ch.5, the
   bench: "Who else is going to teach you blood magic?") and Viridia (Ch.7, answering the hair joke).
   Both are now **spent**. Two single source beats by two characters, not a shared device; neither
   recurs for anyone.

### Retired / at-risk list (fail on sight; extend as the gates flag more)

- `never once` (template seed; the AMELIA LESSON phrase).
- **Book-wide gestures near the density cap (≤0.3 per 1,000 words book-wide; 4+ of one class in a
  chapter fails):** nods / nodded; looking away / looking down / glancing away. Treat both classes as
  closed except where the source places a specific one. Also rationed (STYLE_CONSTRAINTS §2): shrugs,
  head-shakes, grins as a tag, hair tucked behind an ear, anything picked up and set down. **Laugh class:
  ≤4 per chapter, source laughs first** (Ch.2 and Ch.3 were capped on it).
- **"firelight in her eyes" / firelight reflecting off her eyes** — spent in Ch.2. Firelight is texture
  only from here on.
- **Single-use images (STYLE_CONSTRAINTS §3 and the outline ledger):** the softball game (Ch.3); the
  flexed new hand (Ch.3; already echoed once in Ch.5 — now closed); the tongue-out (once per character,
  Ch.5 and Ch.7 — spent); the juggled stones (Ch.17 only); the map under a finger (Fern's map under
  Bal's drumming fingers, Ch.18 only — not Xavier's route in Ch.22 as an anchor); the cloud of bats (Ch.2).
- **Spent comic/staging beats:** Viridia choking on food (Ch.7 pizza) — her Ch.12 cough on her drink
  must be staged differently; "Amelia laughed, delighted, and" (cross-chapter repeat, removed); Lora's
  stammered "L-Lora" (Ch.10, once).
- **Shared gestures resolved (author ruling 2026-10-20: no two characters share a gesture):** *pulling Bal
  along by the hand or sleeve* belongs to **Viridia** (Ch.7, source); Amelia's Ch.3–4 versions were varied.
  *Hair tucked behind an ear* belongs to **Lora** (her source beat, Ch.13); Amelia's Ch.4 use was removed.
  *finger-snap* (Amelia, often in the source; Aren once, p.126 and
  p.182–183) — vary the rendering every time (pop, a blink, the cushion puffing back up) so no snap
  becomes a signature.
- **"my girls" / "his girls"** — at risk. Bal's spoken "my girls" belongs to its source lines only (the
  duel warning to Sean, Ch.20; "No one threatens my girls", Ch.21; "I just want to live my life with my
  girls", Ch.29). In narration, name them or vary; never let "his girls" become the narrator's refrain.
- **Source lines used once, where the source has them, never as signatures:** "I'm not like most people"
  (Viridia, Ch.7 — spent); "I need to study more" (Lora, Ch.13); "That girl loves having the last word"
  (Bal, Ch.24); "That's my Warrior Goddess" (Bal, Ch.22); "You'd be surprised" (Amelia, Ch.7 — spent).
- **Cross-book:** no signature, image or phrase here may repeat across the author's other books; keep
  this book separate from the-fourfold-crown.

## Voice-card format (one per named character)

```
#### [CHARACTER]  — [role]
- Attention / worldview: [what they notice / reduce the world to]
- Vocabulary band: [education/era/region/profession leaking into word choice]
- Syntax fingerprint: [sentence length & clause habits]
- Evasion — never says: [what they refuse]
- Physicality / silence: [the body-tell or pause]
- Verbal tic: none — distinguished by <axis>   (ALWAYS none; the no-tics law)
- DISTINCTNESS GUARANTEE: [one sentence — sharpest marker + what it contrasts against]
- Sample line: [one line only this character could say]
```

---

## PRINCIPALS

#### BALTHAZAAR "BAL" NORHEART — POV (close third, past tense); Amelia's High Priest; Blood Lead Mage; leader of Sygls Best
- **Source facts:** sixteen; mother died giving birth; raised at Saint Andre's; born with a blood sygl,
  hand removed in infancy; could always do some magic, weaker without a sygl; taught himself from
  Fredrick's books (`Sygldry Year 2`); bought a rune engraving kit with kitchen wages; skilled and
  precise with runes from the start; **high pain tolerance** (stated plainly, never as a refrain);
  regrown left hand with the blood sygl **on the palm**; curious, likes secrets and reading ("I like to
  read"); prefers handling his own problems; warm and frank with the girls; protective ("I'd much
  rather I got hurt than any of you"); refuses to answer Raizen's persecution in kind; Bal's violence
  against those who threaten his girls is justified and carries no guilt or self-fear (the surge of
  anger at Sean is noted once, Ch.20, and not developed). Juggles stones once (Ch.17).
- **Attention / worldview:** mechanisms and practicalities — how a thing works and who has to do the
  work (the dorm that grows rooms on a thought; who washes the plates that vanish, Ch.7; whether the
  school has someone to do the potatoes, Ch.5); secrets as things to be found; people in terms of "what
  can I do to help?" He reads the gods' histories and comes away seeing followers as pieces on a board
  (Ch.9). His irrelevant thoughts are domestic and concrete (the brown apple, the sock on the ceiling,
  the porridge); they are HIS and must not bleed onto other characters.
- **Vocabulary band:** a bright, plain-spoken American sixteen-year-old raised in an institution;
  book-learned terms for magic and runes, kitchen-and-dormitory words for everything else. No ornament.
- **Syntax fingerprint:** short, plain, friendly statements and direct practical questions ("What can I
  do to help?", "How exactly am I supposed to do that?"). Jokes under pressure, usually at his own
  expense. When someone threatens his girls the register drops to quiet, complete, exact sentences
  ("What part of she is no longer your concern did you not understand?", asked quietly). Under grief
  (Ch.27) the prose goes short and flat. Registers, not tics.
- **Evasion — never says:** anything that dwells on his own hurt — wounds are made light of ("Would you
  believe I fell on my rapier?", Ch.21); his own lack of a claim or a home is never complained about.
  He never asks Amelia to solve his problems for him (won't summon her for his own trouble, Ch.9; refuses
  her offer to fetch the girls, Ch.28). He never calls her "Lady Amelia" to her face (he drops the title on
  purpose in front of Porter, Ch.9) — the one person who addresses her as plain "Amelia". (He does say
  "Lady Amelia" when speaking ABOUT her to the hall in the Ch.20 speech, as the source has it.)
- **Physicality / silence:** the regrown left hand (stump-itch and flexing are spent — Ch.1/Ch.3);
  stillness and a lowered voice when his girls are threatened (Sean, Iro); in grief, small mechanical
  actions (breaking twigs while Viridia sobs, Ch.26 — source).
- **Verbal tic:** none — distinguished by worldview (mechanisms, how-to-help) + plain syntax.
- **DISTINCTNESS GUARANTEE:** the only voice in the book that answers marvels with a practical question
  or a joke at his own expense, against Amelia's grandeur, Viridia's needling and Lora's hedging.
- **Sample line:** "Nah. Just makes you more interesting." (Ch.5, on being fed from)

#### AMELIA — the Vampire Goddess; originator of the Blood sygl; Bal's familiar ("Amelia Norheart" on her Dawn card)
- **Source facts:** looks a few years older than Bal; pale, black hair to mid-back, red eyes, long black
  dress, ruby teardrop earrings; familiar brand on her forehead, shown or hidden at will; turned at
  sixteen, left on a road, killed the farmer who found her while blood-mad; became the newest originator
  by consuming magical energy; once wiped out half a battlefield; feared because she won't play the
  others' games; trusted them, betrayed, imprisoned almost 3,000 years by eight high priests' deaths;
  carries Peter's memories through his offerings; explodes into bats when furious (once, Ch.2 — spent);
  weeps blood; reads Viridia's diary and may keep her own; needs "a little time" before eating with the
  others; "I feel useless" when she can't protect them; loving, open with affection, lethal to enemies.
  **Manipulates no one** (author ruling): the Hopper bond is a kindness Bal admires as clever (Ch.10);
  nothing she does to her own is a trap.
- **Attention / worldview:** people's secrets ("I like to know people's secrets") and loyalties; the
  gods' wars as games she refuses to play and whose toys she means to break. Her own are hers to protect
  ("anyone else who desires to come after me or mine").
- **Vocabulary band:** ancient being with a modern ear (bats and ravens keep her current; "I know the
  cook here burns the porridge every Tuesday"); casual and girlish in play, formal and archaic at
  ritual ("Caro maestro … May our blood sing together for a thousand years and more").
- **Syntax fingerprint:** quick, teasing, playful questions and dares in private; flips without warning
  to calm, complete-sentence menace toward enemies, no contractions, no raised voice ("Are you implying
  that I need permission from you to go anywhere I wish?"; "Think your next words through, very
  carefully"). The flip itself (switch on, switch off, Ch.9) is her signature MOVE, not a phrase.
- **Evasion — never says:** a direct request to be included or wanted ("Just give me a little time");
  withholds information playfully rather than refusing it ("You'll find out at the ceremony"; "Maybe.
  You'll never find it though"; "if you want to find out, you'd have to win").
- **Physicality / silence:** sudden arrivals and departures (render each differently; no signature
  snap); sitting cross-legged in odd places (Bal's desk, Ch.9; his sickbed, Ch.28); blood tears, the
  single wiped tear (Ch.5) and the sobbing that stains his shirt (Ch.14); kneeling for ritual (the
  binding, Ch.3; the chalice, Ch.28 — the source pairs these on purpose). Bats: spent.
- **Form of address:** may call Bal "Master" — see the exception above; sparingly.
- **Verbal tic:** none — distinguished by worldview (secrets, the gods' game) + the play-to-menace syntax
  flip ("Master" is a title, not a tic).
- **DISTINCTNESS GUARANTEE:** the only character who can turn from a girl's teasing to a god's cold,
  unhurried complete sentences mid-scene, against Viridia, whose teasing never threatens, and Bal,
  whose anger goes quiet but stays a boy's.
- **Sample line:** "A *myth*? They have made me a *myth*?" (Ch.2)

#### VIRIDIA VIZER — Heir of Raizen (Tempus) converted to Blood; storm inheritance; priest of Amelia; Hopper's bonded mage
- **Source facts:** pale blue hair and matching eyes, the hair crackling with static (Raizen's rarest
  inheritance gift, more control over storms); a little taller than Bal; tan (p.133, "long tan arms");
  from a village where sygls are rare and her life was planned at birth, including marriage to the
  headman's son Bran; a sygl was her way out; thinks the originators are "people just like us"; doesn't
  care about petty politics; the elite of her class by inheritance; bonded the bloodwolf Hopper with
  Amelia's help (reported, Ch.10); uses a spear; wears the earth ring Bal gives her (left hand, middle
  finger); glances at jewellery in shop windows (New Spring, Londra — source); brave to the point of
  drinking what she believes is poison (Ch.25); breaks down afterward (Ch.26); rarely uses her power (the
  water snake, Ch.18).
- **Attention / worldview:** status games — who is snubbing whom, who wants something — noticed in
  order to refuse them. Reads Bal's social position for him ("No one rolling out the red carpet for you
  yet?"; why classmates ask about him but won't approach, Ch.12).
- **Vocabulary band:** village-raised, casual, plain American teen ("Nah", "jerk", "lame"); can put on a
  borrowed noble register on command (coached by Lora, Ch.23–25: haughty, "filthy blood mages").
- **Syntax fingerprint:** blunt, dry statements; provocations framed as questions ("What if I wanted to
  kiss Amelia instead?"); deflating one-liners about authority. Talks with her hands when telling a story
  (Ch.10). Does not hedge.
- **Evasion — never says:** sincere feeling, until it is too big to deflect (the diary, Ch.12; "I was so
  scared", Ch.26). Does not talk about her own gift (Lora: "It's not something she really talks about").
- **Physicality / silence:** the hair: crackles when she is nervous, lies still when she is frightened
  or drained (Ch.26), back to popping when she recovers (Ch.27) — only where the source places it, and
  rendered differently each time. Twists the ring on her finger while deciding (Ch.19, source, once).
  Elbows Lora lightly when teasing her (source, twice: bookstore and conversion) — vary or let one go.
  Tongue-out and towing Bal by the sleeve: spent (Ch.7). Choking on food: spent (Ch.7).
- **Verbal tic:** none — distinguished by syntax (needling questions, no hedges) + physicality (the hair).
- **DISTINCTNESS GUARANTEE:** the one who needles authority and never hedges, against Lora, who hedges
  and never needles, and against Amelia, whose teasing can turn dangerous where Viridia's only deflates.
- **Sample line:** "Nah. They're people just like us. They've got faults just like us. They just live
  longer than the rest of us." (Ch.7)

#### LORA AEGIS — Heir of Kenmei (Waves) converted to Blood; rapier prodigy; alchemist; priest of Amelia; Dawn faction enthusiast
- **Source facts:** shy; brown hair (long), glasses that slide down her nose, freckles; Kenmei/Waves sygl
  (loses waves magic on conversion and doesn't mind); trained by her father (once in Kenmei's army) and
  her town's weapons master; beat every boy in her town's tournament at thirteen and was mocked for it;
  two years of training by day and reading by night; her father had her rapier enchanted never to need
  sharpening; wants to join the Dawn faction; alchemist (the alchemy book, Ms. Summers, the nightstalker
  poison); loses herself in whatever she is doing (the three hours with the young alchemist, Ch.24);
  dispatched three bandits alone (Ch.16); coaches Viridia on noble manners; has a raven familiar (sick,
  left at the castle, Ch.16); holds Viridia through her breakdown; "We'll figure it out, together."
- **Attention / worldview:** craft and preparation — technique, ingredients, timings, terrain,
  history. Watches Bal's sword work and catalogues his mistakes to teach him, not to rank him (Ch.16).
- **Vocabulary band:** bookish and exact: alchemy (asphodel, ginger root, seventy-two hours, dormant
  twenty-four hours), weapons, military history learned from her father, noble etiquette.
- **Syntax fingerprint:** two registers. With people: hedged, apologetic, self-correcting, sentences
  that restart ("I like books better than people. Mostly. Not you. I mean, I don't know you. I mean…",
  Ch.10). On her subjects: fluent, complete, brisk, even bossy ("Do either of you know anything about
  alchemy? No you don't. You'll just be in my way here."). The switch between the two is her marker.
- **Evasion — never says:** that she wants something, for fear she isn't ready ("I'm not sure if I'm
  ready … I need to study more", once, Ch.13); won't let friends join anything only for her sake.
- **Physicality / silence:** the rapier as an extension of her (sets her feet and starts an exercise
  without a word, Ch.10); glasses sliding as she works; going white when frightened for someone (Ch.25,
  source); a hand on someone's cheek or hand to steady them (Viridia, Ch.26; Bal, Ch.26 — source).
  Stammer "L-Lora": spent (Ch.10). Hair behind the ear: hers (her source beat, Ch.13); no one else uses it.
- **Verbal tic:** none — distinguished by worldview (craft) + the hedged-to-fluent register switch.
- **DISTINCTNESS GUARANTEE:** the only voice that hedges with people and turns exact and bossy the
  moment the subject is a blade, a potion or a plan, against Viridia, who is blunt everywhere and never
  explains a technique.
- **Sample line:** "I like books better than people … Books don't mind if you don't say anything." (Ch.10)

#### RAIZEN — originator of the Tempus sygl; principal antagonist
- **Source facts:** looks middle-aged; plain orange monk's clothing; sits with his hands together on
  his knees (Ch.6); reads his names in a drier voice than the others; pays no attention to his followers
  (Viridia, Ch.10); ranked lowest of the four, so the burden of dealing with the freed Amelia falls to
  him; had a follower kidnap and torture one of Amelia's high priests long ago (Ch.4); suggested the
  original idea of locking her away (his public statement, Ch.18); blames her madness in public; turns
  villages on blood sygls; cheats by telling his assassins where Bal is and teleporting them near (Ch.21);
  his High Priest is Toma; rages at the conversion ("This is why we locked Amelia away in the first
  place. Her followers are too dangerous!"); confined by Amelia's demand for three thousand years in the
  very temple she was locked in (Ch.29). Never shares a private scene with Bal.
- **Attention / worldview:** possession and rank — what is his stays his ("They do not share"); his
  rarest gift wandering to the Blood is an insult, not a loss of a person.
- **Vocabulary band:** a god's; formal on the stage, plain and petulant when crossed.
- **Syntax fingerprint:** accusation addressed past the accused to a higher authority ("Do you see?" to
  Aren); indignant rhetorical questions ("That's it? She just gets away with taking my High Priest?").
- **Evasion — never says:** a denial or a defence. When Aren asks whether he cheated, he says nothing
  (p.126). He never addresses Bal directly in the source.
- **Physicality / silence:** stillness that breaks (his hands come apart at Amelia's clap, Ch.6); in
  defeat, literally shaking with rage, then fear replacing it at her demand (Ch.29). Acts through others
  (priests, statements, assassins) and is mostly absent from the page — his absence is part of the voice.
- **Verbal tic:** none — distinguished by evasion (silence instead of denial) + possessive worldview.
- **DISTINCTNESS GUARANTEE:** the only character who speaks about people as property and appeals over
  their heads to Aren, against Amelia, who speaks to her followers directly and calls them hers to
  protect, not to keep.
- **Sample line:** "Do you see? This is why we locked Amelia away in the first place. Her followers are
  too dangerous!" (p.180; Ch.29) *(spoken lines not yet on page — seeded from source)*

---

## SECONDARY & SUPPORTING

*On the page in Ch.1–10 first, in order of appearance; then characters still to come, in source order.
Cards marked "(not yet on page — seeded from source; Writer confirms on first appearance)" must be
re-read and confirmed (or corrected against the page) the moment the character enters.*

### On the page (Ch.1–10)

#### FREDRICK — Bal's friend at Saint Andre's (Ch.1, remembered goodbye; author-approved addition)
- Attention / worldview: Bal's ability, plainly ("You're better at this than half the kids who'll be in
  my year"); generosity without ceremony. He left for one of the lesser Sygldry schools.
- Vocabulary band: a year older, an orphan like Bal; plain, brotherly.
- Syntax fingerprint: short declaratives, a refusal that is also a gift ("I could. I'm not going to.").
- Evasion — never says: the obvious thing both boys know (that Bal can't go to a school); leaves it
  unspoken.
- Physicality / silence: terra sygl on his left palm; tall and all elbows; the stack of books tied with
  garden string; ruffles Bal's hair; waves through a rear car window. (No humming or other habits: an
  invented quirk was cut at Ch.1 evaluation.)
- Verbal tic: none — distinguished by evasion (leaves the hard truth unsaid).
- DISTINCTNESS GUARANTEE: the friend who gives by refusing to take, against Bal, who asks questions
  about everything.
- Sample line: "I could. I'm not going to." (Ch.1)

#### MRS. SARAH BROWN — runs Saint Andre's with others; the adult Bal goes to (Ch.4–5)
- Attention / worldview: procedure and consequences — how the claiming works, who will be unhappy, what
  needs packing; catches people, and expects them to own being caught. Quietly, injustice to blood
  sygls: her husband's late-surfacing affinity was **Blood**; the factory fired him so as not to be "seen
  as a blood mage supporter"; he was shot coming home from work; she has suspicions.
- Vocabulary band: an administrator's plain, unsentimental English.
- Syntax fingerprint: verdicts and instructions; short dismissals ("Well then."; "For now, it's best you
  run along and pack. I'll send Pierre for you in the morning."). Dry humour in one line ("You just don't
  do anything by half measures, do you?").
- Evasion — never says: more than the bare facts of her grief; the husband's story takes under a minute
  and she returns to business.
- Physicality / silence: forties, light grey skirt, white blouse, bun; one photograph on a bare desk,
  which her eyes go to once; the goldfish mouth of shock; a quick, hard hug on parting (Ch.5). No
  invented habits (the pen-tap in Ch.4 is one scene's texture, not a habit; dusting was cut as invented).
- Verbal tic: none — distinguished by syntax (verdicts, dismissals) + evasion (grief told short).
- DISTINCTNESS GUARANTEE: the only adult who speaks in rulings and ends conversations by looking back at
  her paperwork, against Verin, who explains at length and kindly.
- Sample line: "You just don't do anything by half measures, do you?" (Ch.4)

#### PIERRE — another orphan who sometimes helps Mrs. Brown (Ch.5; author decision 2026-10-20)
- Attention / worldview: getting the message delivered right and getting back to bed.
- Vocabulary band: a sleepy orphan's.
- Syntax fingerprint: relays instructions in order ("Kitchen, then office").
- Evasion — never says: anything about the hand, though he stares at it.
- Physicality / silence: pajama bottoms and sweater, hair flattened on one side, yawns mid-sentence.
- Verbal tic: none — distinguished by function (the messenger).
- DISTINCTNESS GUARANTEE: a walk-on who only ever passes on someone else's words.
- Sample line: "Kitchen, then office. Don't make me come back up." (Ch.5)

#### VERIN — escort mage; Bal and Amelia's driver to the school (Ch.5–6)
- Attention / worldview: logistics and the newcomer's comfort — portals, enchantments, the ceremony's
  order, stew in the pot, the horse.
- Vocabulary band: an old professional mage's easy, explanatory English; calls Mrs. Brown "Sarah."
- Syntax fingerprint: patient, complete explanations with a small self-correction ("Portaling doesn't
  work in or near the school. Well. Not properly, anyway."); briefs while eating.
- Evasion — never says: a question too many ("Verin knows not to ask too many questions. He's been at
  this for years."). Never learns who slept on his floor.
- Physicality / silence: older; faded but clean and pressed red robes; kind blue eyes; grandfatherly
  smile; snores softly; horse Thistle.
- Verbal tic: none — distinguished by evasion (asks nothing) + explanatory syntax.
- DISTINCTNESS GUARANTEE: the adult who explains everything and asks nothing, against Mr. Porter, who
  demands and interrogates.
- Sample line: "That's about it. Anything else, you'll have to figure out on your own." (Ch.5)

#### THISTLE — Verin's horse (Ch.5–6)
- Attention / worldview: water, grass, Verin. Vocabulary/Syntax: none (an animal).
- Evasion: source silent — keep to function.
- Physicality / silence: drinks at the trough, blows affectionately at Verin, lifts his head at Bal's laugh.
- Verbal tic: none — distinguished by function.
- DISTINCTNESS GUARANTEE: the unhurried horse of the journey, against Barda, the warhorse of the race.
- Sample line: none (non-speaking).

#### AREN (by night NERA) — originator of the Duality sygl; the eldest; the gods' arbiter (Ch.6; Ch.21 reported; Ch.29)
- Attention / worldview: order and the rules — who may attend, what the war rules allow, what is fair
  under them; does not take sides until the rules force a ruling (declares Amelia the winner; lifts the
  school rule as her concession). Explained to Amelia what she had become (Ch.8). Will not step into the
  war (Ch.18).
- Vocabulary band: ceremonial, faintly old-fashioned ("Young man", "alas", "Is that understood?").
- Syntax fingerprint: measured, complete sentences addressed to a crowd; rulings in plain clauses ("I
  declare Amelia the winner."); a dry parting line ("Try not to start another war.").
- Evasion — never says: an apology for the imprisonment; he frames it as the conflict's "source."
- Physicality / silence: by day an elderly man, long white beard, brown wizard's robes, sandalwood
  sandals; by night Nera, a young blond woman in a shimmering white dress (not yet seen); stumbles at
  Amelia's clap; snaps his fingers to send people away (render differently from Amelia's arrivals).
- Verbal tic: none — distinguished by worldview (the rules as the only side he takes).
- DISTINCTNESS GUARANTEE: the only god who speaks as a judge, against Raizen's accusations and
  Amelia's threats.
- Sample line: "I'm sorry, young ones. If yours is the blood sygl, then I'm afraid you've come so far
  for nothing." (Ch.6)

#### KENMEI — originator of the Waves sygl; Lora's original originator (Ch.6)
- Attention / worldview: source silent beyond indifference: she "did not care one way or the other"
  about the rule (Ch.19); Amelia guesses the rule "sounds like something Kenmei would suggest" (Ch.15).
- Vocabulary band / Syntax: reads her list "in a low, clear voice" (Ch.6); otherwise source silent —
  keep to function.
- Evasion — never says: source silent — keep to function.
- Physicality / silence: tall, stately, flowing blue robes, brown hair, very pale sea-green eyes; grips
  her throne's arms at the clap.
- Verbal tic: none — distinguished by function (the indifferent one).
- DISTINCTNESS GUARANTEE: the god defined by not caring, against Raizen, who cares only about what is his.
- Sample line: none on page; keep her silent unless the source gives a line.

#### NAISURA — originator of the Terra sygl (Ch.6; Ch.21 reported)
- Attention / worldview: source gives conduct, not speech: went after Nera last year and was badly
  beaten; won the old war with Kenmei by sealing her command tent in stone; his high priest built
  Amelia's prison temple; opens his mouth to argue at the concession (p.126).
- Vocabulary band / Syntax: reads his list without standing (Ch.6); source silent — keep to function.
- Evasion — never says: source silent — keep to function.
- Physicality / silence: looks thirty-something, bare-chested, white drawstring pants; sits bolt
  upright at the clap. Zoran resembles him.
- Verbal tic: none — distinguished by function and physicality.
- DISTINCTNESS GUARANTEE: the god who can't be bothered to stand, against Aren, who rises to speak.
- Sample line: none on page; source silent.

#### MR. PORTER — familiars teacher; hostile to blood mages (Ch.9; Ch.19–21 reported/on stage)
- Attention / worldview: rules and rank — who disobeyed orders, who belongs at which table; reports
  Lora and Viridia to the gods and suggests the no-mingling rule and taking Hopper (Ch.19).
- Vocabulary band: a pedant's formal teacher-English; "Mr. Norheart", "ms. Vizer".
- Syntax fingerprint: lecturing complete sentences; sarcasm by question ("Is it a rodent, perhaps? Or a
  toad?"); before power, he collapses into stammered fragments and repeated instructions.
- Evasion — never says: the end of the sentence about what a blood mage is ("But you're … And he's a…",
  Ch.9); he never says the insult to Amelia's face.
- Physicality / silence: fifties, thinning grey hair, brown tweed buttoned over his stomach, glasses
  that flash and hide his eyes; colour rising red to purple, draining to chalk (one scene — spent);
  hand to the knot of his tie. Huginn is his. Later a "nasty smile" announcing the rule (Ch.20, source).
- Verbal tic: none — distinguished by evasion (the unfinished slur) + formal sarcasm.
- DISTINCTNESS GUARANTEE: the only adult who addresses Bal as "Mr. Norheart" with contempt and then
  can't finish a sentence in front of Amelia, against Verin's courtesy and Zoran's economy.
- Sample line: "But since you feel you have such a grasp on things that you do not need my instruction,
  why don't you show us your familiar? Is it a rodent, perhaps? Or a toad?" (Ch.9)

#### HUGINN — Mr. Porter's raven familiar (Ch.9)
- Attention / worldview: cheese; his master. Close to fifteen years with Porter; saved his life twice.
- Vocabulary band / Syntax: none (a bird); a small dry noise in his throat.
- Evasion: source silent — keep to function.
- Physicality / silence: big, sleek; takes cheese neatly and tips his beak to swallow; freezes at
  Amelia; flies out after the class to watch them.
- Verbal tic: none — distinguished by function.
- DISTINCTNESS GUARANTEE: the familiar as a teacher's tool, against Hopper, the familiar as Amelia's kin.
- Sample line: none (non-speaking).

#### TYLER — a boy in the front row of the familiar class (Ch.9)
- Attention / worldview: the literal meaning of a rule.
- Vocabulary band: ordinary student.
- Syntax fingerprint: one alarmed literal question.
- Evasion — never says: source silent — keep to function.
- Physicality / silence: hand straight up; later crouched behind his chair when Amelia appears.
- Verbal tic: none — distinguished by function.
- DISTINCTNESS GUARANTEE: the classmate who takes Porter literally, against the class's anonymous stares.
- Sample line: "We can't leave the class? Like, ever?" (Ch.9)

#### THE LIBRARIAN — school library, second floor (Ch.9)
- Attention / worldview: finding the right books for a reader; sets books aside for Bal.
- Vocabulary band / Syntax: goes into the stacks "without a word"; source silent — keep to function.
- Evasion: source silent — keep to function.
- Physicality / silence: a woman with a pencil behind each ear (Ch.9 texture; don't make it a bit).
- Verbal tic: none — distinguished by function. (Unnamed in the source; if the Writer names her, keep
  this card and add the name.)
- DISTINCTNESS GUARANTEE: help without conversation, against Lora's talk of books.
- Sample line: none on page.

#### MR. WINTERS — rune working teacher (Ch.9; Ch.19 mentioned)
- Attention / worldview: precision and use — what a rune is for and when you'll need it.
- Vocabulary band: practical craftsman-teacher.
- Syntax fingerprint: brief praise attached to a practical application.
- Evasion — never says: source silent — keep to function.
- Physicality / silence: short, skinny; walks the rows and bends over the work; taps the rune.
- Verbal tic: none — distinguished by worldview (use-value).
- DISTINCTNESS GUARANTEE: the teacher who praises by naming a use, against Porter, who lectures by
  naming a rule. (His avoidance-rune praise is a re-read plant toward the purification rune, Ch.25.)
- Sample line: "That's precise. Very good. That's an essential one to know if you're ever travelling at
  night in unfriendly territory." (Ch.9)

#### ZORAN — Warfare teacher (Ch.10; Ch.18 praises Bal's rapier)
- Attention / worldview: fitness to fight; pairs students by one look at their grip.
- Vocabulary band: drill-ground plain.
- Syntax fingerprint: imperatives, no wasted words ("Then you attack him. Slowly.").
- Evasion — never says: anything about Bal's sygl or the rumours; source silent on more.
- Physicality / silence: young, broad-shouldered, Naisura's build and stance (could be his son); working
  sword forms alone before class; keeps his shirt on.
- Verbal tic: none — distinguished by syntax (bare imperatives).
- DISTINCTNESS GUARANTEE: the only teacher who speaks in orders and nothing else, against Winters' mild
  praise and Porter's sarcasm.
- Sample line: "Take your time choosing a weapon. Pick each one up. Imagine using it. Take the one that
  speaks to you." (Ch.10)

#### HOPPER — the bloodwolf; Viridia's familiar (named on page by report, Ch.10; first seen Ch.13/16)
- Attention / worldview: bloody meat and being near Amelia (her terms for the bond); danger ahead.
  Bloodwolves are partly Amelia's creation (plains wolves given her blood) and look on her as a mother.
- Vocabulary band / Syntax: none; growls, a chuff in answer (Ch.16, source).
- Evasion: won't swim (Ch.21, source).
- Physicality / silence: female (the source slips once to "his" teeth at p.92 — keep her female);
  young, paws already bigger than Viridia's hands; silver fur with blood red across back and shoulders;
  pelt turns a crossbow bolt; the size-adjustment collar shrinks her to dog size (Ch.13); ranges ahead;
  bristles like a porcupine when she growls.
- Verbal tic: none — distinguished by physicality and function.
- DISTINCTNESS GUARANTEE: the familiar who chose her bond for Amelia's sake, against Huginn, a teacher's
  bird.
- Sample line: none (non-speaking).

### Still to come (source order)

#### PETER — Amelia's follower who built the hidden temple; dead about a thousand years (Ch.11, told by Amelia) *(on page Ch.11 — reported only, confirmed)*
- **Ch.11 as written:** exists only in Amelia's telling on the hill (Terra stoneworking family, sixteen, shunned, the mountains, twelve years, the altar, all his memories still with her) and in the temple itself, which Bal sees from the High Priest's window and judges by it. No flashback, no lines, nothing added.
- Attention / worldview: known only through Amelia's telling and his memories: the lone blood sygl in a
  Terra stone-working family, shunned at sixteen; twelve years laying every stone; glad to make
  something that would endure.
- Vocabulary band / Syntax: never speaks on the page (reported only).
- Evasion — never says: source silent — keep to function.
- Physicality / silence: his hands laid every stone; final dedication on her altar so he could live
  with her forever.
- Verbal tic: none — distinguished by function (the told tale).
- DISTINCTNESS GUARANTEE: the outsider whose whole voice is a building, against Bal, the outsider who
  talks.
- Sample line: none (reported only). Never dramatize him as a flashback.

#### THAD MOREN — one of Amelia's two first priests; the cost-counter of the war (Ch.11, 18, 22, 27–28) *(on page Ch.11 — confirmed)*
- **Ch.11 as written:** introduces himself first; carries the practical speech (the paired rune stone: "If we have to reach you, we'll signal you with that…"); tosses Bal the stone. When Bal tells them Amelia did not abandon them, his hands go flat on the table (once; not a recurring gesture). Speaks plainly, no flourish. Physical description as the source.
- Attention / worldview: the cost — casualties, exhaustion, what the army can't hold (reads the reports).
- Vocabulary band: soldier-priest's plain speech.
- Syntax fingerprint: blunt summaries ("We've got a war is what we've got."); reads figures off a paper
  once (Ch.22 — a source beat, not a device).
- Evasion — never says: that they will lose; "Our boys won't embarrass themselves."
- Physicality / silence: twenties; slight; long black hair in a ponytail, pale, sharp nose; scarlet robe,
  white sash; dark circles; scratches the stubble on his chin (once, source). Gives Bal the paired rune
  stone (light + pair).
- Verbal tic: none — distinguished by worldview (the cost). Differentiate from Xavier by what he
  notices, never by habits (foundation §3).
- DISTINCTNESS GUARANTEE: the priest who reports the damage, against Xavier, who proposes the route.
- Sample line: "We've got a war is what we've got." (p.128; Ch.22)

#### XAVIER GILES — Amelia's other first priest; the planner (Ch.11, 20, 22, 28) *(on page Ch.11 — confirmed)*
- **Ch.11 as written:** the quieter of the two here; agrees with Thad that Lady Amelia's choice is good enough. His clear blue eyes go over Bal once and "did not miss much" (the source's "intelligence"). At the story of Amelia's imprisonment he says nothing and his eyes fix on a bare patch of wall (once; not a recurring gesture). Physical description as the source (big in the shoulders, tan, blade scars on the backs of his hands).
- Attention / worldview: the route and the target — strike the priests, then the High Priest; Londra's
  layout, deliveries, patrols, bribable innkeepers.
- Vocabulary band: intelligence-briefing English.
- Syntax fingerprint: decisive recommendations ("That is our only chance."); orderly briefings.
- Evasion — never says: source silent — keep to function.
- Physicality / silence: broad-shouldered, weapon scars on his hands, tan, clear blue eyes; traces a
  path on the map (Ch.22 — not an anchor; the map-under-a-finger image is Fern's, Ch.18); pokes his head
  round the door with bad news (Ch.28).
- Verbal tic: none — distinguished by worldview (the plan).
- DISTINCTNESS GUARANTEE: the priest who answers "what now?", against Thad, who answers "what did it cost?"
- Sample line: "We must try to send in a force to eliminate the priests, then take out the High Priest.
  That is our only chance." (p.129; Ch.22)

#### COMMANDER FERN — commander of the Blood army (Ch.18, 22; mentioned 27) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Attention / worldview: what force and intelligence can do (spies with no sygls posing as labourers;
  Toma's file); ready to answer in kind until Bal forbids it.
- Vocabulary band: a commander's blunt plain speech.
- Syntax fingerprint: short blunt assessments ("There's not much we can do"); a hard proposal as a
  question ("Could we do the same to them?").
- Evasion — never says: source silent — keep to function.
- Physicality / silence: short, stocky, long grey beard, intelligent grey eyes, carries great authority;
  thumbs through a stack of papers at his desk.
- Verbal tic: none — distinguished by worldview (force and intelligence).
- DISTINCTNESS GUARANTEE: the only voice that proposes retaliation, against Bal's "We will not respond
  in kind."
- Sample line: "Could we do the same to them? See how they respond to it." (p.107; Ch.18)

#### ERIC — younger officer given the battalion at Raizen's border (Ch.22) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- All four axes: source silent — keep to function (named once; leads the distraction so blood-sygl
  civilians can be evacuated).
- Verbal tic: none — distinguished by function.
- DISTINCTNESS GUARANTEE: a name on Fern's order, not a speaking role unless the source gives one.
- Sample line: none.

#### MARCUS — the Blood army's weapons master (Ch.22, reported) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Attention / worldview: makes Lora work for her win (reported by Lora). Other axes: source silent —
  keep to function. Reported only; Bal does not witness the spar.
- Verbal tic: none — distinguished by function.
- DISTINCTNESS GUARANTEE: the one fighter who nearly beats Lora, known only through her excitement.
- Sample line: none (reported only).

#### SOREN — Dawn Hall clerk, New Spring (Ch.13, 17) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Attention / worldview: guild procedure — membership, team rules, dues, ledgers, the right job.
- Vocabulary band: courteous professional.
- Syntax fingerprint: polite procedural explanations; a reasonable counter-question ("why would you not
  join first if that's what you wanted?").
- Evasion — never says: her guess about "Amelia Norheart"; she raises an eyebrow and says nothing.
- Physicality / silence: guild uniform; writes names in white flowing script that engraves into the
  wood; staffs the always-open hall.
- Verbal tic: none — distinguished by evasion (the eyebrow and silence).
- DISTINCTNESS GUARANTEE: the stranger who notices the borrowed surname and keeps it to herself,
  against Mrs. Locklan, who tells everyone everything.
- Sample line: "Welcome to the Dawn Hall. My name is Soren and this is Kim. What can we do for you
  today?" (p.75; Ch.13)

#### KIM — Soren's colleague at the Dawn Hall (Ch.13) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- All four axes: source silent — keep to function (introduced by Soren; never speaks).
- Verbal tic: none — distinguished by function.
- DISTINCTNESS GUARANTEE: present, named, silent.
- Sample line: none.

#### MS. SUMMERS — New Spring's alchemist; Lora's mentor (Ch.13, 16–17; mentioned 24) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Attention / worldview: the craft and its economy — only enough ingredients for three, "no point in
  being greedy"; lonely; eyes light up at Lora's questions; trades two potions as part payment.
- Vocabulary band / Syntax: speaks mainly through Lora's reports; her praise is rare ("glowing praise
  from her," Ch.24). Source silent beyond — keep to function.
- Evasion — never says: source silent — keep to function.
- Physicality / silence: older; too unwell to fetch the flowers herself; normally hires an escort.
- Verbal tic: none — distinguished by worldview (thrift and craft).
- DISTINCTNESS GUARANTEE: the expert whose approval is scarce, against Lora, who gives hers freely to a
  book. (Source spells her Ms./Mrs. interchangeably; use **Ms. Summers**, as foundation does.)
- Sample line: none direct (reported through Lora).

#### HEATH — bandit leader on the Whitehaven road; wears a heart ring (Ch.16; named by Iro, Ch.21) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Attention / worldview: robbery as business, then cruelty aimed at what Bal protects; "past his prime"
  per Iro. Sent by Raizen's side to kill Bal.
- Vocabulary band: rough, mock-polite.
- Syntax fingerprint: mock courtesy ("Your weapons if you please"), then taunts.
- Evasion — never says: his name or who sent him (Bal learns both from Iro).
- Physicality / silence: older, grey-haired, large; pitted steel chain shirt with dried blood; missing,
  dirty teeth; the **heart ring** on his right hand (paired; it is how Raizen's side knew he died,
  Ch.21). Unnamed on the page until Ch.21.
- Verbal tic: none — distinguished by syntax (mock courtesy).
- DISTINCTNESS GUARANTEE: the bandit who says "please" before he threatens the girls, against Iro, who
  chats while he fights.
- Sample line: "Want to kill me yourself, huh? Don't blame you. Not with those pretty girls watching."
  (p.93; Ch.16)

#### IRO — assassin at the lake (Ch.21) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Attention / worldview: the kill as sport; scores Bal's swordwork; brags about orders from "my High
  Priest of course."
- Vocabulary band: young, cocky, conversational.
- Syntax fingerprint: chatty running commentary in a fight ("Almost had you there"; "Oh, that's got to
  hurt"); once caught, frightened truthful blurting, his name said twice in one breath (one moment,
  source; not a refrain).
- Evasion — never says: fear, until the whip is round his neck.
- Physicality / silence: barely older than Bal; woodsman clothes; short brown hair; sharp blue eyes;
  twirls his sword in his right hand. His death is justified and unremarked by guilt.
- Verbal tic: none — distinguished by syntax (fight commentary).
- DISTINCTNESS GUARANTEE: the only enemy who banters, against Toma, who is grave, and Aleric, who is
  courtly.
- Sample line: "I don't know how you managed to kill Heath with that shoddy sword work." (p.122; Ch.21)

#### SEAN KIIN — Tempus Lead Mage (a fourth year) (Ch.13 described; Ch.20 on stage) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Attention / worldview: rank and ownership of "his" Tempus students; enforces rules (no loud talk, no
  kissing, study time; five demerits = any chore he wants).
- Vocabulary band: a prefect's.
- Syntax fingerprint: indignant echo-questions of Bal's words ("Not my concern? Who are you to tell me
  she's not my concern…"); "you filthy blood mage."
- Evasion — never says: anything back once Bal threatens the duel; he swallows and turns away (source;
  mind the look-away density cap — render once).
- Physicality / silence: grabs and yanks Viridia; dragged across a table by the blood whip, slides down
  his own. (No invented craving for Raizen's notice — cut by author decision.)
- Verbal tic: none — distinguished by syntax (echo-questions) + worldview (ownership).
- DISTINCTNESS GUARANTEE: the bully who repeats Bal's words back as outrage, against Porter, who
  interrogates with sarcasm.
- Sample line: "She's a Tempus and she'll not be wearing anything to do with your sygl." (p.115; Ch.20)

#### JAMES — the brewer, Londra (Ch.24) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Attention / worldview: the trade — vintages, dates burned into lids, what the priests drink, what a
  customer can pay.
- Vocabulary band: merchant's frank, proud of stock.
- Syntax fingerprint: sales talk with a wink ("It depends on how much coin you have"); a loud belly laugh.
- Evasion — never says: source silent — keep to function.
- Physicality / silence: forties, muscular, sleeves rolled to the elbow, thinning brown hair, sharp eyes;
  a neat, tidy office; warehouse on the water.
- Verbal tic: none — distinguished by worldview (the trade).
- DISTINCTNESS GUARANTEE: the only Londra voice that talks money with relish, against Mrs. Locklan's
  hospitality.
- Sample line: "It depends on how much coin you have, and how much your lady would like to impress
  them." (p.143; Ch.24)

#### MRS. LOCKLAN — innkeeper, the Winespring Inn (Ch.24–25) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Attention / worldview: guests, payment, and the thrill of a high-born lady with Raizen's favour under
  her roof.
- Vocabulary band: cheerful, chatty innkeeper.
- Syntax fingerprint: warm run-on welcomes; tells more than she's asked ("I still can't wait to tell my
  husband…").
- Evasion — never says: source silent — keep to function.
- Physicality / silence: plump, welcoming smile, apron, wipes her hands as she hurries out; the letter
  from her apron pocket. (Source spells Mrs./Ms.; she has a husband: **Mrs. Locklan**.)
- Verbal tic: none — distinguished by syntax (over-telling).
- DISTINCTNESS GUARANTEE: the stranger who tells everything, against the Three Boars' quiet barman.
- Sample line: "Why, by the sparking hair of course." (p.140; Ch.24)

#### ALERIC — Raizen's priest; the clever, ambitious one (Ch.24–25) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Attention / worldview: suspicion and advantage — who refuses a drink, who his High Priest will want to
  meet; most unpredictable of the three; comes early.
- Vocabulary band: courtly priest-speak ("Let us celebrate Raizen's glory").
- Syntax fingerprint: smooth courtesy that hardens into two-word commands ("I insist."; "Get her a cup.").
- Evasion — never says: a threat aloud; his menace stays inside politeness.
- Physicality / silence: scar through the right eye (narrows his good eye); azure robes; drains his cup
  before commanding. No invented origin for the scar (Bal only wonders).
- Verbal tic: none — distinguished by syntax (courtesy to command).
- DISTINCTNESS GUARANTEE: the enemy who poisons with good manners, against Titus's impatience and
  Leon's curiosity.
- Sample line: "I insist." (p.155; Ch.25)

#### TITUS — Raizen's priest (Ch.25) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Attention / worldview: follows orders; impatient.
- Syntax fingerprint: short impatient summons ("Come now. We've been waiting for you.").
- Vocabulary band / Evasion: source silent — keep to function.
- Physicality / silence: azure robes. Source silent beyond.
- Verbal tic: none — distinguished by syntax (impatience).
- DISTINCTNESS GUARANTEE: the priest who hurries, against Aleric's "We have all day."
- Sample line: "Come now. We've been waiting for you." (p.155; Ch.25)

#### LEON — Raizen's priest, the youngest (Ch.25) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Attention / worldview: curiosity about the Ventish brandy; does the pouring as the youngest.
- Syntax fingerprint: eager, appreciative remarks ("Now that smells divine.").
- Vocabulary band / Evasion: source silent — keep to function.
- Physicality / silence: azure robes; sticks his nose in the bung-hole to smell it. (Source slip p.157:
  "Aleric … motioning for Aleric to refill" — it is Leon who pours.)
- Verbal tic: none — distinguished by worldview (curiosity).
- DISTINCTNESS GUARANTEE: the priest who wants to taste it, against Titus, who wants it over with.
- Sample line: "Now that smells divine." (p.157; Ch.25)

#### BRAN — the headman's son Viridia was promised to (Ch.27, reported only) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Attention / worldview: entitlement — "he would have me eventually."
- Vocabulary band / Syntax: never speaks on the page; quoted only by Viridia.
- Evasion: source silent — keep to function.
- Physicality / silence: the smirk; two years older; tried to get his father to keep her.
- Verbal tic: none — distinguished by function (the life she escaped).
- DISTINCTNESS GUARANTEE: the boy who claimed her without asking, against Bal, who asks every time.
- Sample line: none (reported only).

#### JAZEN GREY — centurion of the Blood army (Ch.27) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Attention / worldview: duty and the mission at hand; gives his own horse without a second thought.
- Vocabulary band: soldier's plain, respectful ("High Priest").
- Syntax fingerprint: quiet, practical, a message to carry; affectionate about his horse.
- Evasion — never says: source silent — keep to function.
- Physicality / silence: hurries up quietly; pats Barda's neck.
- Verbal tic: none — distinguished by function.
- DISTINCTNESS GUARANTEE: the soldier who gives instead of reporting, against Thad and Xavier's
  briefings.
- Sample line: "Ol' Barda hasn't let me down yet. He'll get you there safely and quickly." (p.167; Ch.27)

#### BARDA — Jazen Grey's warhorse (Ch.27) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Physicality: large white warhorse, powerful legs, big head; gallop and trot through the night.
  Other axes: none (non-speaking).
- Verbal tic: none — distinguished by function.
- DISTINCTNESS GUARANTEE: the race horse of the book, against Thistle's plod.
- Sample line: none.

#### HIGH PRIEST TOMA — Raizen's High Priest (Ch.18 file; Ch.28 letter; Ch.29 duel) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Attention / worldview: the rules of the duel and the grief of a man whose priests were killed; real
  care for his fellow priests (give it its line); cruelty promised in return; takes the girls as leverage
  and keeps them unharmed.
- Vocabulary band: formal, ceremonious priest's English; calls Amelia Bal's "pet originator" in writing.
- Syntax fingerprint: assured statements, rules recited ("As mage duels go, among high priests, there can
  be no interference"); a single incantation ("Czak"); contemptuous short questions ("Is that it?").
- Evasion — never says: that his elemental is an inheritance gift until it is too late (Fern's file:
  "no inheritance gift").
- Physicality / silence: fifty-six, no family, several concubines; blue robes with lightning bolts sewn
  on; after the conversion, rocking on the ground, blood tears, the blood sygl on his palm. Sent to the
  school with the girls (Ch.29); source silent after.
- Verbal tic: none — distinguished by worldview (rules and grief).
- DISTINCTNESS GUARANTEE: the only enemy who mourns, against Raizen, who only resents.
- Sample line: "Yes, I can see that you care for them. As I cared for my fellow priests, but at least
  yours are still alive." (p.175–176; Ch.29)

#### AKORA — Toma's life-bonded storm elemental; becomes the blood elemental (Ch.29) *(not yet on page — seeded from source; Writer confirms on first appearance)*
- Physicality: a crackling being of pure electrical energy; whips of electricity; swirls to pull Bal into
  its maelstrom; a core. Converted, it becomes swirling blood and follows Bal; Amelia sends it to her
  domain to study. Other axes: none (non-speaking). Life-bonded inheritance gift, so not a familiar.
- Verbal tic: none — distinguished by function.
- DISTINCTNESS GUARANTEE: the book's one impossible creature, a blood elemental.
- Sample line: none.

### Named or present but not carded (keep it that way unless the source gives them more)

- **Dracula** — mentioned only (Ch.2; long dead).
- **Mrs. Brown's husband** — unnamed; the photograph (narrow face, collar buttoned to the top, Ch.4).
- **Lora's father** and her town's **weapons master** — unnamed; reported only.
- **Lora's raven** — unnamed; sick, left at the castle (Ch.16).
- **Unnamed speaking walk-ons** (function only; no invented traits): the Terra boy built like a door
  (Ch.10, reported); the girl who elbows Sean (Ch.20); the refugee father who spits and names Kysmer
  (Ch.23, once); the two Londra gate guards (truncheon; the awed young one); the Winespring stable boy
  ("We were told to expect you"); the young Londra alchemist (reported by Lora); the Three Boars' quiet
  barman ("It's a cold rune"); the eager Three Boars stable boy; the young blond storm mage ("I think
  I'll get a promotion after killing you," Ch.27); the bookstore's stout woman. **If the Writer gives any
  of them a name, add a card the same day.**

---

## CAST-WIDE DISTINCTNESS MATRIX (cover-the-name, pre-solved)

| Character | Sharpest distinguisher | Contrast vs nearest character |
| --- | --- | --- |
| Bal | answers marvels with a practical question or a joke at his own expense; addresses her as plain "Amelia", never "Lady" | Amelia speaks in grandeur and menace; Lora explains, Bal asks |
| Amelia | flips mid-scene from teasing girl to cold, complete-sentence god | Viridia teases as an equal and her teasing never threatens |
| Viridia | needles authority with questions; never hedges | Lora hedges and never needles |
| Lora | hedged with people, exact and bossy on blades, potions and plans | Viridia is blunt everywhere and never explains a technique |
| Raizen | talks about people as property; appeals past them to Aren; silence instead of denial | Amelia speaks to her own directly, as hers to protect |
| Aren | rules as the only side he takes; a judge's plain rulings | Raizen accuses; Amelia threatens |
| Mrs. Brown | verdicts and dismissals; grief told in under a minute | Verin explains at length and asks nothing |
| Verin | explains everything, asks nothing | Porter demands and interrogates |
| Mr. Porter | formal sarcasm; can't finish the sentence in front of Amelia | Sean echoes Bal's words as outrage |
| Mr. Winters | praise attached to a use | Zoran gives orders, Porter gives rules |
| Zoran | bare imperatives, nothing else | Winters' mild practical praise |
| Hopper | Amelia's kin, bonded for meat and nearness to her | Huginn, a teacher's bird |
| Thad | reports what it cost | Xavier proposes the route |
| Xavier | proposes the route and the target | Thad reports the damage |
| Fern | the one voice that proposes retaliation | Bal: "We will not respond in kind." |
| Soren | notices the borrowed surname and keeps it to herself | Mrs. Locklan tells everyone everything |
| Sean Kiin | echo-questions of Bal's words; ownership of "his" students | Porter's sarcasm by question |
| Heath | mock courtesy ("if you please") before threats | Iro chats while he fights |
| Iro | running fight commentary | Toma's gravity, Aleric's courtliness |
| Aleric | courtesy hardening into two-word commands | Titus hurries; Leon is curious |
| Toma | the only enemy who mourns | Raizen only resents |

**Cover-the-name pairs to watch most** (the cast's real collision risks): Amelia/Viridia (both tease —
hold Amelia's flip and Viridia's equal-footing needles apart); Viridia/Lora (needle vs hedge); Thad/Xavier
(cost vs route — never distinguish them by habits); Porter/Sean (sarcasm vs echo-outrage); and the
narrator-bleed risk: Bal's domestic irrelevant thoughts and plain jokes stay with Bal.

## Source discrepancies noted while seeding (resolved by canon; Writer follows the resolution)

- Blood whip "from the palm of his right hand" (p.115): **author ruling 2026-10-20 — keep the RIGHT palm.**
  Blood magic need not come from the sygl hand (the sygl is on the regrown left palm); Ch.27 has dagger left,
  whip right.
- Hopper is "his" once (p.92); she is female everywhere else.
- Thad: black hair (p.~62) but "brown stubble" (p.129). Keep black; render the stubble without colour.
- "Aleric … motioning for Aleric to refill" (p.157): Leon pours.
- Leon calls the brandy "Ventish wine" (p.155): it is Ventish brandy.
- Ms./Mrs. Summers and Ms./Mrs. Locklan alternate in the source: **Ms. Summers**, **Mrs. Locklan**.
- Ch.6 has Bal guess the buggy trio are siblings: his mistaken guess, consistent with the 2026-10-20
  decision that they are not.
