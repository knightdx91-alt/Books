#!/usr/bin/env python3
"""tic_report.py — ASSIST (not a gate): surface motif/tic density + verb-form candidates per chapter.

It does NOT decide anything. It flags candidates so the line-edit judgment pass is systematic
instead of eyeballed. Two reports:

  1. MOTIF DENSITY — counts the book's deliberate recurring phrases per chapter. Deliberate motifs
     are load-bearing and STAY; the point is to spot *incidental over-use* (a chapter far above the
     book median) so the redundant instances can be thinned while the load-bearing one is kept.
     (This is the AI-reviewers' "vary internal motifs" note — banking / count / small true things.)

  2. VERB-FORM / RHYTHM CANDIDATES — lines with dense past-perfect ("had -ed") chains or -ing
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
# Pompeii / "The Hour of Ash" deliberate motifs (book-specific — like the style_check ALLOWLIST).
# NOTE: seeded fresh for THIS book. Do NOT carry another book's motif vocabulary in here (that is
# cross-book tic bleed). Extend with this book's own load-bearing recurrences only.
MOTIFS = [
    # NO TICS law: no character device, no refrain. ONLY the allowlisted object-motif phrases from
    # tools/style_check.py ALLOWLIST (foundation.md §12; each capped at 3 uses book-wide). Anything
    # ELSE that recurs 3+ times across the book is a defect — see AUTO-RECURRENCE below.
    r"the one it brought",
    r"where the dead go out",
    r"the seventh of bysios",
]
# World terms / proper names that legitimately recur (place names, titles, institutions). NOT
# motifs and NOT tics — exempt from the recurrence gate. Keep to nouns the story cannot avoid.
WORLD_TERMS = [
    "the oracle", "the pythia", "the library of alexandria", "the temple of apollo",
    "the corycian cave", "the nuceria gate", "the basilica julia", "the appian way",
    "the castalian spring", "the sarno", "the polygonal wall", "the sacred way",
]

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
    """RUN 2 — AUTHOR RULING: TIC BUDGET = 0.
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

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file")
    ap.add_argument("--gate", action="store_true",
                    help="exit 1 if any non-allowlisted phrase recurs 3+ times book-wide (tic budget = 0)")
    a = ap.parse_args()
    files = [a.file] if a.file else sorted(
        glob.glob("manuscript/chapters/chapter-*.md"),
        key=lambda p: int(re.search(r"(\d+)", Path(p).name).group(1)))
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
    allfiles = sorted(glob.glob("manuscript/chapters/chapter-*.md"),
                      key=lambda p: int(re.search(r"(\d+)", Path(p).name).group(1)))
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
    if a.gate:
        print(f"RESULT: {'FAIL — ' + str(bad) + ' recurring phrase(s) to vary/remove' if bad else 'clean (tic gate)'}")
        sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
