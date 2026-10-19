#!/usr/bin/env python3
"""tic_report.py — ASSIST (not a gate): surface motif/tic density + verb-form candidates per chapter.

It does NOT decide anything. It flags candidates so the line-edit judgment pass is systematic
instead of eyeballed. Two reports:

  1. MOTIF DENSITY — counts the book's deliberate recurring phrases per chapter. Deliberate motifs
     are load-bearing and STAY; the point is to spot *incidental over-use* (a chapter far above the
     book median) so the redundant instances can be thinned while the load-bearing one is kept.
     (This is the AI-reviewers' "vary internal motifs" note — banking / count / small true things.)

  2. GESTURE / ACTION-BEAT layer — stage business counted by CLASS regardless of wording
     (object handling, nods, swallows, 'a long moment'…); a repeated gesture is a tic.

  3. VERB-FORM / RHYTHM CANDIDATES — lines with dense past-perfect ("had -ed") chains or -ing
     stacks. These are the class Eilidh (Book One reviewer) touched by preference (looked->look,
     smelling->smelled): grammatically correct, so LanguageTool stays silent — a human/Claude must
     judge whether the tense/ending reads better changed. Pure candidates, high false-positive rate.

Usage:
  python3 tools/tic_report.py                      # all chapters
  python3 tools/tic_report.py --file manuscript/chapters/chapter-4.md
"""
import argparse, glob, re, statistics, sys
from pathlib import Path

# Deliberate recurring motifs (keep — flag only incidental over-use). Extend per book.
# NOTE: seeded fresh for THIS book. Do NOT carry another book's motif vocabulary in here (that is
# cross-book tic bleed). Extend with this book's own load-bearing recurrences only.
MOTIFS = [
    # AUTHOR'S NO-TICS LAW: no character device, no refrain. This list holds ONLY the few allowlisted
    # OBJECT-motif phrases from tools/style_check.py ALLOWLIST (each capped at 3 uses book-wide).
    # Anything ELSE that recurs 3+ times across the book is a defect — see AUTO-RECURRENCE below.
]
# World terms / proper names that legitimately recur (place names, titles, institutions). NOT
# motifs and NOT tics — exempt from the recurrence gate. Keep to nouns the story cannot avoid.
WORLD_TERMS = [
    # e.g. "the citadel", "the high council" — nouns the story cannot avoid; NOT motifs, NOT tics.
]
# The narrator's professional reflex: the phrases by which THIS book's narrator files everything she
# sees under her own expertise (a lab, a seminar, a trade). Book-specific; leave empty if none. The gate
# caps them per chapter (CREDENTIAL_MAX, narration only): it is characterization at a low rate and a
# device at a high one.
CREDENTIAL_PATTERNS = [
]
CREDENTIAL_MAX = 4


def strip_comments(t): return re.sub(r"<!--.*?-->", "", t, flags=re.S)

def analyze(path):
    raw = strip_comments(Path(path).read_text())
    words = len(raw.split())
    counts = {}
    for pat in MOTIFS:
        n = len(re.findall(pat, raw, flags=re.I))
        if n: counts[pat] = n
    total = sum(counts.values())
    # verb-form candidates: lines with >=3 "had <word>ed" or >=3 "-ing" in one sentence-ish span
    vf = []
    for i, line in enumerate(raw.splitlines(), 1):
        had_ed = len(re.findall(r"\bhad \w+ed\b", line))
        ing = len(re.findall(r"\b\w+ing\b", line))
        if had_ed >= 3 or ing >= 6:
            vf.append((i, had_ed, ing, line[:90]))
    return words, total, counts, vf

STOP = set("the a an and or but of to in on at for with as is was were be been her his its their "
           "my your she he it they i you we him them me that this had have has not no so if then".split())
QUOTE = re.compile(r"[\u201c\"]([^\u201d\"]{2,400})[\u201d\"]")

def content_rich(g):
    return sum(1 for w in g if w not in STOP) >= max(2, len(g) - 2)

def recurrence_scan(files, allow):
    """AUTHOR'S NO-TICS LAW (every book): tic budget = 0.
    Any content-rich 3-6-word phrase recurring 3+ times across the BOOK (prose), and any 2-6-word
    phrase (3-6 words) recurring 3+ times inside QUOTED SPEECH (a catchphrase forming), is a tic candidate —
    a defect unless it is one of the few allowlisted object-motifs (cap 3)."""
    prose, speech, where = {}, {}, {}
    for f in files:
        raw = strip_comments(Path(f).read_text())
        toks = [w.lower() for w in re.findall(r"[A-Za-z'\u2019\-]+", raw)]
        seen = set()
        for n in range(3, 7):
            for i in range(len(toks) - n + 1):
                g = tuple(toks[i:i+n])
                if not content_rich(g): continue
                prose[g] = prose.get(g, 0) + 1
                if g not in seen:
                    where.setdefault(g, []).append(Path(f).stem.split("-")[-1]); seen.add(g)
        for q in QUOTE.findall(raw):
            qt = [w.lower() for w in re.findall(r"[A-Za-z'\u2019\-]+", q)]
            for n in range(3, 7):
                for i in range(len(qt) - n + 1):
                    g = tuple(qt[i:i+n])
                    if not content_rich(g): continue
                    speech[g] = speech.get(g, 0) + 1
    def keep(d, floor):
        out = []
        for g, c in d.items():
            if c < floor: continue
            j = " ".join(g)
            if any(a in j or j in a for a in allow): continue
            out.append((c, j))
        out.sort(key=lambda x: (-len(x[1].split()), -x[0]))
        kept = []
        for c, j in out:
            if any(j in k[1] for k in kept): continue
            kept.append((c, j))
        return sorted(kept, key=lambda x: -x[0])
    return keep(prose, 3), keep(speech, 3), where

# ---- GESTURE / ACTION-BEAT LAYER (author ruling 2026-10-18: a repeated GESTURE is a tic) -------------
# The n-gram scans only see repeated WORDS. A character who keeps picking things up and setting them
# down, nodding, swallowing, looking away, or pausing "for a long moment" is repeating a gesture with
# the wording varied — the reader feels it by chapter six. Each class below is matched by meaning
# (regex over inflections), counted book-wide (density per 1,000 words) and per chapter (clustering).
# Flags: a class above GESTURE_BOOK_MAX per 1k words book-wide, or GESTURE_CHAPTER_MAX+ hits in one
# chapter. Extend the classes per book if a new piece of stage business starts to recur.
GESTURE_CLASSES = {
    "object handling (set down / put down / pick up / take out / put back / hold out / turn over)":
        r"\b(?:pick(?:ed|s|ing)?\s+(?:it|them|the\s+\w+|her\s+\w+|his\s+\w+|my\s+\w+|a\s+\w+)?\s*(?:back\s+)?up|set(?:s|ting)?\s+(?:it|them|the\s+\w+|her\s+\w+|his\s+\w+|my\s+\w+|a\s+\w+)\s+(?:back\s+)?(?:down|aside)|put(?:s|ting)?\s+(?:it|them|the\s+\w+|her\s+\w+|his\s+\w+|my\s+\w+)\s+(?:back\s+)?(?:down|aside|back)|laid\s+(?:it|them|the\s+\w+|her\s+\w+|his\s+\w+|my\s+\w+)\s+(?:down|on\s+the|aside)|took\s+(?:it|them|the\s+\w+|her\s+\w+|his\s+\w+|my\s+\w+)\s+(?:out\s+of|off|from)\s+(?:her|his|my|the|a)\b|held\s+(?:it|them|the\s+\w+|a\s+\w+)\s+out|turn(?:ed|s|ing)?\s+(?:it|them|the\s+\w+)\s+over)\b",
    "nod": r"\bnod(?:ded|s|ding)?\b",
    "shrug": r"\bshrug(?:ged|s|ging)?\b",
    "sigh": r"\bsigh(?:ed|s|ing)?\b",
    "swallow": r"\bswallow(?:ed|s|ing)?\b",
    "breath beat (let out a breath / exhaled / breath caught)": r"\b(?:let\s+out\s+(?:a|the|her|his|my)\s+breath|exhal\w+|breathed\s+out|breath\s+(?:caught|hitched)|took\s+a\s+(?:deep\s+)?breath|drew\s+a\s+breath)\b",
    "jaw (set / tight / clench)": r"\bjaw\b",
    "look away / look down": r"\blook(?:ed|s|ing)?\s+(?:away|down)\b",
    "turn away / turn back": r"\bturn(?:ed|s|ing)?\s+(?:away|back)\b",
    "hand through hair": r"\b(?:hand|fingers)\s+through\s+(?:her|his|my|their)\s+hair\b",
    "fingers / grip tighten": r"\b(?:fingers|hands?|grip|knuckles)\s+(?:tighten\w*|whiten\w*)\b",
    "'a (long) moment'": r"\b(?:for\s+)?a\s+(?:long\s+)?moment\b",
    "something in (chest / stomach / throat)": r"\bsomething\s+in\s+(?:her|his|my)\s+(?:chest|stomach|throat)\b",
    "eyes (narrowed / widened / closed)": r"\beyes\s+(?:narrow\w*|widen\w*|clos\w+)\b",
    "lips (pressed / thinned)": r"\b(?:lips|mouth)\s+(?:press\w*|thin\w*|tighten\w*)\b",
    "head shake": r"\bsh(?:ook|akes?|aking)\s+(?:her|his|my|their)\s+head\b",
}
GESTURE_BOOK_MAX = 0.30      # per 1,000 words, book-wide (applies once the manuscript has GESTURE_MIN_WORDS)
GESTURE_CHAPTER_MAX = 4      # per-chapter cap = max(this, chapter words / 1000); a long chapter earns a little more room
GESTURE_MIN_WORDS = 20000    # the density rule needs a sample; a two-chapter book is judged per chapter only
GESTURE_WINDOW = 500         # words; a SCENE cluster — 3+ of one class inside this window is the reader-visible tic
GESTURE_WINDOW_MAX = 3
# Bending to the work (added after Hour of Ash ch.9: a cast that bends over every task is a gesture tic too).
GESTURE_CLASSES["bend / stoop over"] = (r"\b(?:bent|bending|bends|bend|stooped|stooping|stoops|stoop|leaned|leaning)\s+"
                                        r"(?:over|down|to|forward|close|low|closer|in)\b")
# Kneeling / crouching / squatting (added 2026-10-19 at the author's ruling: "should definitely be limited.
# Nothing repetitive that makes it seem like AI"). Counts every kneel, crouch and squat, deliberate or not.
GESTURE_CLASSES["kneel / crouch / squat"] = r"\b(?:knelt|kneeled|kneeling|kneels|kneel|crouched|crouching|crouches|crouch|squatted|squatting|squats|squat)\b"

# ---- PROP FIDGET layer: the same object handled again and again inside one scene ------------------
# The Saeren lesson: a headmistress sets down her paper, takes off her spectacles, picks them up,
# turns them over, puts them back on — all between lines of one conversation. The prop does the
# acting. This finds any noun that is FIDGETED with (turned, twisted, set/put down, picked up, taken
# off/out, put back/on, folded, tapped…) 3+ times within PROP_WINDOW words. Real action (fighting for
# a bag, packing a parcel) uses other verbs and does not fire.
PROP_WINDOW = 400
_FV = (r"(?:turn(?:ed|s|ing)?|twist(?:ed|s|ing)?|roll(?:ed|s|ing)?|fold(?:ed|s|ing)?|unfold(?:ed|s|ing)?|"
       r"tap(?:ped|s|ping)?|fiddl(?:ed|es|ing)|smooth(?:ed|s|ing)?|straighten(?:ed|s|ing)?|adjust(?:ed|s|ing)?|"
       r"set(?:s|ting)?|put(?:s|ting)?|pick(?:ed|s|ing)?|took|tak(?:es|ing)|laid|slid|weigh(?:ed|s|ing)?|"
       r"tilt(?:ed|s|ing)?|rub(?:bed|s|bing)?|spun|spin(?:s|ning)?)")
_PART = r"(?:back\s+)?(?:down|up|over|off|out|on|aside|away|round|around|back)"
_PLACE = r"(?:in|into|between|through)\s+(?:his|her|my|their)\s+(?:fingers|hands?|mouth|lap|teeth)"
_DET = r"(?:the|his|her|my|their|its|a|an)"
# A: verb + det + [adj] + NOUN + (particle | in his fingers/mouth)   e.g. "turned the celery in his fingers"
# B: verb + particle + det + [adj] + NOUN                             e.g. "set down the paper"
# C: verb + it/them + (particle | place)                              e.g. "turned them over" -> last named prop
_PA = re.compile(rf"\b{_FV}\s+{_DET}\s+(?:\w+\s+)?([a-z]+)\s+(?:{_PART}|{_PLACE})\b", re.I)
_PB = re.compile(rf"\b{_FV}\s+{_PART}\s+{_DET}\s+(?:\w+\s+)?([a-z]+)\b", re.I)
_PC = re.compile(rf"\b{_FV}\s+(it|them)\s+(?:\w+\s+)?(?:{_PART}|{_PLACE})\b", re.I)
PROP_STOP = set("hand hands head face eyes eye arm arms shoulder shoulders foot feet leg legs back way time "
                "breath voice look mind word words light lights air door doors heart chin lips mouth fingers "
                "finger knee knees neck hair attention money".split())

def prop_scan(files):
    """Any one PROP fidgeted with 3+ times inside PROP_WINDOW words (pronouns follow the last named prop)."""
    flags = []
    for f in files:
        ch = Path(f).stem.split("-")[-1]
        t = strip_comments(Path(f).read_text())
        def wpos(i): return len(re.findall(r"[A-Za-z'\u2019\-]+", t[:i]))
        events = []
        for rx in (_PA, _PB):
            for m in rx.finditer(t):
                noun = m.group(1).lower()
                if noun in PROP_STOP or len(noun) < 3: continue
                events.append((m.start(), noun))
        for m in _PC.finditer(t):
            events.append((m.start(), None))
        events.sort()
        hits, last, last_pos = {}, None, -10**9
        for start, noun in events:
            p = wpos(start)
            if noun is None:
                if last is None or p - last_pos > 150: continue
                noun = last
            last, last_pos = noun, p
            hits.setdefault(noun, []).append(p)
        for noun, pos in hits.items():
            for i in range(len(pos)):
                j = i
                while j + 1 < len(pos) and pos[j + 1] - pos[i] <= PROP_WINDOW: j += 1
                if j - i + 1 >= 3:
                    flags.append(f"prop fidget: '{noun}' handled {j - i + 1}x within {PROP_WINDOW} words in chapter {ch} "
                                 f"(around word {pos[i]}) — the prop is doing the acting")
                    break
    return flags

# ---- RHYTHM & VOICE REFLEXES (narration only; quoted speech and italic documents excluded) --------
# AND-CHAINS: sentences with 4+ "and"s. One designed held sentence per chapter is a device; a dozen is
# the narrator's default rhythm. Cap: max(AND_CHAIN_MIN_CAP, chapter words / AND_CHAIN_WORDS_PER).
AND_CHAIN_MIN_CAP = 9
AND_CHAIN_WORDS_PER = 900

def _narration(text):
    text = re.sub(r"[\u201c\"][^\u201d\"]*[\u201d\"]", " ", text)         # quoted speech
    text = re.sub(r"(?m)^\*[^*\n].*\*\s*$", " ", text)                       # whole italic paragraphs (documents)
    text = re.sub(r"(?m)^#.*$", " ", text)
    return text

# NEGATION PIVOT: "the mule did not pull; she sat back" — a short negated clause hinged on a semicolon to a
# pronoun that says what happened instead. Define-by-negation in miniature; it reads as a device fast.
# Fails a chapter with more than PIVOT_CHAPTER_MAX, or a book with PIVOT_BOOK_MAX+ (the 3+ recurrence rule).
PIVOT_RX = re.compile(r"\b(?:did not|didn't|was not|wasn't|were not|weren't|would not|wouldn't|could not|couldn't|"
                      r"had not|hadn't|does not|doesn't|is not|isn't)\s+(?:\w+\s+){0,2}?\w+;\s+(?:he|she|it|I|they|we)\s+\w+",
                      re.I)
PIVOT_CHAPTER_MAX = 1
PIVOT_BOOK_MAX = 3

# NARRATOR MOVES the evaluator kept freezing by name (Hour of Ash, Ch.1-7): a paragraph that opens "So I…"
# (the narrator's consequence hinge) and "before I had decided/thought…" (the body outrunning the mind).
# Each is fine once; as a habit it is a voice tic. Cap 1 per chapter. A "So" opener in 4+ consecutive
# chapters is printed as a WATCH (not a failure) so the streak is visible before it hardens.
SO_OPENER_RX = re.compile(r"(?m)^(?:So|And so) (?:I|she|he|we|they|it)\b")
BEFORE_DECIDED_RX = re.compile(r"\bbefore (?:I|she|he|we|they) (?:had )?(?:decided|thought|known|meant|chosen|realized|realised|noticed)\b", re.I)
MOVE_CHAPTER_MAX = 1
# The consequence hinge as a FAMILY: cap "So" alone and the habit moves to "Then… / After that… / Afterward…"
# (it did, in Hour of Ash Ch.8: 0-3 per chapter, then 8). Paragraph openers from the family are capped at
# max(HINGE_MIN_CAP, words / HINGE_WORDS_PER).
HINGE_RX = re.compile(r"(?m)^(?:So|And so|Then|And then|After that|Afterward|Afterwards|Later|Next)\b[ ,]")
HINGE_MIN_CAP = 3
HINGE_WORDS_PER = 2500
SO_STREAK_WATCH = 4

def reflex_scan(files):
    rows, flags = [], []
    pivot_total = 0
    creds = [re.compile(p, re.I) for p in CREDENTIAL_PATTERNS]
    for f in files:
        ch = Path(f).stem.split("-")[-1]
        t = strip_comments(Path(f).read_text())
        words = len(re.findall(r"[A-Za-z'\u2019\-]+", t))
        nar = _narration(t)
        sents = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", nar))
        chains = sum(1 for s in sents if len(re.findall(r"\band\b", s, re.I)) >= 4)
        cap = max(AND_CHAIN_MIN_CAP, round(words / AND_CHAIN_WORDS_PER))
        cred = sum(len(rx.findall(nar)) for rx in creds)
        pivots = len(PIVOT_RX.findall(re.sub(r"\s+", " ", nar)))
        pivot_total += pivots
        so_open = len(SO_OPENER_RX.findall(t))
        before = len(BEFORE_DECIDED_RX.findall(nar))
        hinges = len(HINGE_RX.findall(t))
        hcap = max(HINGE_MIN_CAP, round(words / HINGE_WORDS_PER))
        if hinges > hcap:
            flags.append(f"hinge paragraph openers (So/Then/After that/Afterward…): {hinges} in chapter {ch} (cap {hcap}) — start on the thing itself")
        rows.append((ch, chains, cap, cred, pivots, so_open, before))
        if so_open > MOVE_CHAPTER_MAX:
            flags.append(f"'So I…' paragraph openers: {so_open} in chapter {ch} (cap {MOVE_CHAPTER_MAX}) — open on the action itself")
        if before > MOVE_CHAPTER_MAX:
            flags.append(f"'before I had decided/thought': {before} in chapter {ch} (cap {MOVE_CHAPTER_MAX}) — a narrator move turning into a habit")
        if pivots > PIVOT_CHAPTER_MAX:
            flags.append(f"negation pivots: {pivots} in chapter {ch} (cap {PIVOT_CHAPTER_MAX}) — 'did not X; she Y'; say what happened")
        if chains > cap:
            flags.append(f"and-chains: {chains} sentences with 4+ 'and' in chapter {ch} (cap {cap}) — the narrator's default rhythm; split or recast")
        if creds and cred > CREDENTIAL_MAX:
            flags.append(f"credential asides: {cred} in chapter {ch} (cap {CREDENTIAL_MAX}) — the narrator filing the world under her expertise")
    if pivot_total >= PIVOT_BOOK_MAX:
        flags.append(f"negation pivots: {pivot_total} book-wide (fails at {PIVOT_BOOK_MAX}) — a construction recurring is a tic")
    return rows, flags

def gesture_scan(files):
    """Return (rows, flags). rows: (class, total, per1k, worst_chapter, worst_count)."""
    texts = [(Path(f).stem.split("-")[-1], strip_comments(Path(f).read_text())) for f in files]
    total_words = sum(len(re.findall(r"[A-Za-z'’\-]+", t)) for _, t in texts) or 1
    rows, flags = [], []
    for name, pat in GESTURE_CLASSES.items():
        rx = re.compile(pat, re.I)
        per_ch = [(ch, len(rx.findall(t))) for ch, t in texts]
        chap_words = {ch: len(re.findall(r"[A-Za-z'\u2019\-]+", t)) for ch, t in texts}
        total = sum(c for _, c in per_ch)
        if not total:
            continue
        per1k = total / total_words * 1000
        worst_ch, worst = max(per_ch, key=lambda x: x[1])
        rows.append((name, total, per1k, worst_ch, worst))
        if per1k > GESTURE_BOOK_MAX and total_words >= GESTURE_MIN_WORDS:
            flags.append(f"{name}: {total}x book-wide = {per1k:.2f}/1k (> {GESTURE_BOOK_MAX})")
        for ch, c in per_ch:   # every chapter against its OWN cap (a 4 in a short chapter must not hide behind a long one)
            cap = max(GESTURE_CHAPTER_MAX, round(chap_words.get(ch, 0) / 1000))
            if c >= cap:   # reaching the cap fails (the law: 4+ of one class, or one per 1,000 words)
                flags.append(f"{name}: {c}x in chapter {ch} (cap {cap} for a {chap_words.get(ch, 0):,}-word chapter)")
        # scene-window cluster: positions (in words) of each hit; 3+ inside GESTURE_WINDOW words
        for ch, t in texts:
            pos = [len(re.findall(r"[A-Za-z'\u2019\-]+", t[:m.start()])) for m in rx.finditer(t)]
            for i in range(len(pos)):
                j = i
                while j + 1 < len(pos) and pos[j + 1] - pos[i] <= GESTURE_WINDOW:
                    j += 1
                if j - i + 1 >= GESTURE_WINDOW_MAX:
                    flags.append(f"{name}: {j - i + 1}x within {GESTURE_WINDOW} words in chapter {ch} (around word {pos[i]}) — a scene is running on this gesture")
                    break
    rows.sort(key=lambda r: -r[2])
    return rows, flags

def echo_scan(files, n_target, allow):
    """Phrases in chapter n_target that already occur in an earlier chapter (2nd use)."""
    def grams(text):
        toks=[w.lower() for w in re.findall(r"[A-Za-z'\u2019\-]+", text)]
        out={}
        for n in range(3,7):
            for i in range(len(toks)-n+1):
                g=tuple(toks[i:i+n])
                if not content_rich(g): continue
                # a 3-gram must be DISTINCTIVE to count as an echo: at least one word of 6+ letters
                # ("full of grit" yes; "after a while" no). 4+-grams count as they are.
                if n==3 and not any(len(w)>=6 for w in g): continue
                out.setdefault(g,0); out[g]+=1
        return out
    earlier={}
    target=None
    for f in files:
        ch=int(re.search(r"(\d+)",Path(f).name).group(1))
        g=grams(strip_comments(Path(f).read_text()))
        if ch==n_target: target=g
        elif ch<n_target:
            for k in g: earlier.setdefault(k,set()).add(ch)
    # The book's voice-bank samples are benchmark passages, never text to reuse: a phrase lifted from one
    # is an echo exactly like a phrase from an earlier chapter (it shows as "voice-bank").
    for vb in sorted((BOOK_DIR / "voice-bank").glob("**/sample-*.md")):
        for k in grams(strip_comments(vb.read_text())):
            if len(k) >= 5: earlier.setdefault(k,set()).add("voice-bank")   # 5+ words: the samples share the book's nouns
    if target is None: return []
    hits=[]
    for g in target:
        if g in earlier:
            j=" ".join(g)
            if any(a in j or j in a for a in allow): continue
            hits.append((len(g), j, sorted(earlier[g], key=str)))
    hits.sort(key=lambda x:(-x[0], x[1]))
    kept=[]
    for L,j,chs in hits:
        if any(j in k[1] for k in kept): continue
        kept.append((L,j,chs))
    return kept

# Chapters are found relative to THIS script (books/<name>/tools/), not the current directory, so a
# run from the repo root checks the same files as a run from the book folder instead of finding none.
BOOK_DIR = Path(__file__).resolve().parent.parent

def chapter_files():
    files = sorted(glob.glob(str(BOOK_DIR / "manuscript" / "chapters" / "chapter-*.md")),
                   key=lambda p: int(re.search(r"(\d+)", Path(p).name).group(1)))
    if not files:
        sys.exit(f"tic_report: no chapters found under {BOOK_DIR}/manuscript/chapters — refusing to report a clean result")
    return files

# ---- COMMAND ECHO candidates (hand-judged; printed with --echoes) -------------------------------------
# A short quoted order whose verb returns at the head of the next narration paragraph ("Hold that corner."
# / "I held it…") — the narrator answering an order by repeating it as compliance. Defiance and plain
# narrative also match ("Look at me." / "I looked at the jar"), so this lists candidates; it never fails.
CMD_IRR={"tell":["told"],"take":["took","taken"],"give":["gave","given"],"go":["went","gone"],"hold":["held"],"bring":["brought"],"put":["put"],"sit":["sat"],"stand":["stood"],"keep":["kept"],"leave":["left"],"come":["came"],"get":["got"],"say":["said"],"find":["found"],"eat":["ate","eaten"],"drink":["drank"],"run":["ran"],"lie":["lay"],"make":["made"],"shut":["shut"],"let":["let"],"send":["sent"],"wind":["wound"],"sing":["sang"],"speak":["spoke"],"throw":["threw"],"wear":["wore"],"hang":["hung"],"sweep":["swept"],"fetch":["fetched"],"stamp":["stamped"],"walk":["walked"]}
def _cmd_forms(v):
    f={v,v+"s",v+"ed",v+"d",v+"ing",v[:-1]+"ied" if v.endswith("y") else v}
    if len(v)>2 and v[-1] not in "aeiouwy" and v[-2] in "aeiou" and v[-3] not in "aeiou": f.add(v+v[-1]+"ed")
    f.update(CMD_IRR.get(v,[])); return f
CMD_STOP={"i","you","we","no","yes","oh","what","who","why","how","where","when","the","a","it","that","this","and","but","if","so","not","then","there","here","they","he","she","my","your","good","well","all","one","now","come"}
def command_echo_scan(path):
    t=re.sub(r"<!--.*?-->","",Path(path).read_text(),flags=re.S)
    paras=[p.strip() for p in t.split("\n") if p.strip() and not p.startswith("#")]
    hits=[]
    for a,b in zip(paras,paras[1:]):
        qs=re.findall(r"[“\"]([^”\"]+)[”\"]",a)
        if not qs or re.search(r"[“\"]",b): continue
        for q in qs:
            w=re.findall(r"[A-Za-z']+",q)
            if len(w)<1 or len(w)>8: continue
            v=w[0].lower()
            if v in CMD_STOP or len(v)<3: continue
            head=[x.lower() for x in re.findall(r"[A-Za-z']+",b)[:8]]
            if _cmd_forms(v) & set(head):
                hits.append((q[:50], " ".join(head)))
    return hits

# PRONOUN-SWAPPED echoes: "She stayed where she was" (ch.5) -> "I stayed where I was" (ch.9) is the same move
# with the pronouns changed. 5-6-word phrases are compared with subject/object/possessive pronouns folded
# together, and must carry one content word of 5+ letters (idioms like "could not get" stay out).
_PN_SUBJ = {"i", "she", "he", "we", "they"}
_PN_OBJ = {"me", "him", "us", "them"}
_PN_POSS = {"my", "his", "our", "their"}
_PN_WEAK = {"said", "could", "would", "should", "there", "their", "where", "which", "about", "again", "never", "before", "after",
            "bottom", "front", "behind", "under", "middle", "inside", "outside", "along", "across", "around", "between", "still", "other", "first"}

def _pn_norm(w):
    return "<S>" if w in _PN_SUBJ else ("<O>" if w in _PN_OBJ else ("<P>" if w in _PN_POSS else w))

def _pn_grams(text):
    out = set()
    for para in text.split("\n"):          # a phrase never spans a paragraph break
        toks = [_pn_norm(w.lower()) for w in re.findall(r"[A-Za-z'\u2019\-]+", para)]
        for n in range(5, 7):
            for i in range(len(toks) - n + 1):
                g = tuple(toks[i:i + n])
                if not any(x.startswith("<") for x in g):
                    continue
                if any(len(x) >= 5 and x not in STOP and x not in _PN_WEAK for x in g if not x.startswith("<")):
                    out.add(g)
    return out

def pronoun_echo_scan(files, n_target):
    earlier, target = {}, set()
    for f in files:
        ch = int(re.search(r"(\d+)", Path(f).name).group(1))
        g = _pn_grams(strip_comments(Path(f).read_text()))
        if ch == n_target: target = g
        elif ch < n_target:
            for k in g: earlier.setdefault(k, set()).add(ch)
    hits = sorted((" ".join(g), sorted(earlier[g])) for g in target if g in earlier)
    kept = []
    for j, chs in hits:
        if not any(j in k or k in j for k, _ in kept): kept.append((j, chs))
    return kept

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file")
    ap.add_argument("--echoes", type=int, metavar="N",
                    help="ECHO scan: list every content-rich 3-6-word phrase in chapter N that already occurs in ANY "
                         "earlier chapter (a second use, before the 3+ gate fires). Run it on a fresh draft and vary each hit.")
    ap.add_argument("--gate", action="store_true",
                    help="exit 1 if any non-allowlisted phrase recurs 3+ times book-wide, or a gesture beat clusters (tic budget = 0)")
    a = ap.parse_args()
    if a.echoes:
        allfiles = chapter_files()
        allow = [re.sub(r"\\b|\(\?:|[()\\|?]", "", m).strip() for m in MOTIFS] + [w.lower() for w in WORLD_TERMS]
        hits = echo_scan(allfiles, a.echoes, allow)
        print(f"ECHO SCAN — chapter {a.echoes}: phrases already used in an earlier chapter (2nd use; vary them now)")
        if not hits: print("  none — no cross-chapter echoes.")
        for L,j,chs in hits[:60]:
            print(f"  \"{j}\"  (earlier in ch {','.join(map(str,chs))})")
        pn = pronoun_echo_scan(allfiles, a.echoes)
        for j, chs in pn:
            print(f"  \"{j}\"  (pronoun-swapped; earlier in ch {','.join(map(str, chs))})")
        print(f"RESULT: {len(hits) + len(pn)} echo(es)")
        target_file = [f for f in allfiles if int(re.search(r"(\d+)", Path(f).name).group(1)) == a.echoes]
        cands = command_echo_scan(target_file[0]) if target_file else []
        print("COMMAND ECHO candidates (an order repeated back as compliance? judge each; a book allows ~3 total):")
        for q, head in cands:
            print(f"  \"{q}\"  ->  {head}")
        if not cands: print("  none.")
        sys.exit(0)
    if a.file and not Path(a.file).exists() and (BOOK_DIR / a.file).exists():
        a.file = str(BOOK_DIR / a.file)
    files = [a.file] if a.file else chapter_files()
    rows = []
    for f in files:
        w, total, counts, vf = analyze(f)
        per1k = round(total / max(w, 1) * 1000, 1)
        rows.append((f, w, total, per1k, counts, vf))
    med = statistics.median([r[3] for r in rows]) if rows else 0
    print(f"MOTIF DENSITY (per 1k words) — book median {med}")
    for f, w, total, per1k, counts, vf in rows:
        flag = "  <-- HIGH, review for incidental over-use" if per1k > med * 1.3 and len(rows) > 1 else ""
        print(f"  {Path(f).name:16} {per1k:5}/1k ({total} in {w}w){flag}")
    if a.file:
        f, w, total, per1k, counts, vf = rows[0]
        print(f"\nMotif breakdown for {Path(f).name}:")
        for pat, n in sorted(counts.items(), key=lambda x: -x[1]):
            print(f"  {n:3}x  {pat}")
        print(f"\nVERB-FORM / RHYTHM candidates (judge each; correct-but-maybe-reworkable):")
        for i, he, ing, s in vf:
            print(f"  L{i}: had-ed={he} -ing={ing}  {s}...")
        if not vf: print("  (none)")

    # ---- AUTO-RECURRENCE (tic candidates) — always book-wide ----------------
    allfiles = chapter_files()
    allow = [re.sub(r"\\b|\(\?:|[()\\|?]", "", m).strip() for m in MOTIFS] + [w.lower() for w in WORLD_TERMS]
    prose_hits, speech_hits, where = recurrence_scan(allfiles, allow)
    print("\nAUTO-RECURRENCE — tic candidates (tic budget = 0; allowlisted motifs exempt):")
    bad = 0
    if speech_hits:
        print("  SPOKEN refrains (a catchphrase forming) — 3+ uses in dialogue book-wide:")
        for c, j in speech_hits[:25]:
            print(f"    {c}x  \"{j}\""); bad += 1
    if prose_hits:
        print("  PROSE phrases — 3+ uses book-wide:")
        for c, j in prose_hits[:40]:
            chs = ",".join(where.get(tuple(j.split()), []))
            print(f"    {c}x  \"{j}\"  [ch {chs}]"); bad += 1
    if not bad:
        print("  none — clean.")
    # ---- GESTURE / ACTION-BEAT recurrence (stage business repeated with varied wording) -------------
    grows, gflags = gesture_scan(allfiles)
    gflags += prop_scan(allfiles)
    rrows, rflags = reflex_scan(allfiles)
    print("\nRHYTHM & VOICE REFLEXES (narration only):")
    streak = best = 0
    for ch, chains, cap, cred, pivots, so_open, before in rrows:
        print(f"  ch {ch:>3}: and-chains {chains:>3} (cap {cap})   credential asides {cred:>3}" + (f" (cap {CREDENTIAL_MAX})" if CREDENTIAL_PATTERNS else "")
              + f"   negation pivots {pivots} (cap {PIVOT_CHAPTER_MAX})   'So' openers {so_open}   'before I decided' {before}")
        streak = streak + 1 if so_open else 0
        best = max(best, streak)
    if best >= SO_STREAK_WATCH:
        print(f"  WATCH: a 'So …' paragraph opener in {best} consecutive chapters — give the next chapter none")
    gflags += rflags
    print("\nGESTURE BEATS — stage business by class (book-wide; a repeated gesture is a tic):")
    for name, total, per1k, wch, worst in grows[:16]:
        mark = "  <-- FLAG" if any(f.startswith(name + ":") for f in gflags) else ""
        print(f"  {total:4d}x  {per1k:5.2f}/1k  worst ch {wch}: {worst}x   {name}{mark}")
    if not grows:
        print("  none found.")
    if gflags:
        print("  FLAGS:")
        for f in gflags:
            print(f"    - {f}")
        bad += len(gflags)

    if a.gate:
        print(f"RESULT: {'FAIL — ' + str(bad) + ' recurring phrase(s) to vary/remove' if bad else 'clean (tic gate)'}")
        sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
