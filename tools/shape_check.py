#!/usr/bin/env python3
"""
shape_check.py — manuscript-wide PREDICTABILITY audit (the anti-uniformity gate).

The loudest machine-made tell is not a bad sentence; it is every chapter having the same
SHAPE: the same length, the same opening move, the same closing punch-line, the same number
of scene breaks, the same dialogue share, the same sentence rhythm. A reader cannot name it
but feels it by chapter six. This script measures shape across the whole manuscript and
flags uniformity. It is deterministic and book-agnostic; run it from the repo root:

    python3 tools/shape_check.py books/<slug>            # report + flags
    python3 tools/shape_check.py books/<slug> --strict   # exit 1 on any flag (gate)
    python3 tools/shape_check.py books/<slug> --json     # machine-readable

Run it every ~5 chapters inside the chapter loop (the orchestrator does) and at the end.
It needs at least 4 chapters to say anything; most checks wake up at 6.

Per chapter it records: words, scene breaks, dialogue share, median sentence length, the
OPENING signature (dialogue / "I" / scene-setting / short-punch / long) and the ENDING
signature (dialogue / punch / question / quiet / one-line paragraph). Then it looks for the
patterns a human author never produces by accident:

  LEN-CLUSTER     chapter lengths cluster (coefficient of variation too low, or max/min < 2)
  OPEN-RUN        the same opening signature 3+ chapters in a row
  OPEN-SHARE      one opening signature on > 40% of chapters
  END-RUN         the same ending signature 3+ chapters in a row
  END-SHARE       one ending signature on > 50% of chapters
  PUNCH-REFLEX    > 60% of chapters end on a <= 7-word line (the "every chapter ends on a
                  hook" reflex — itself a tell; some chapters should just stop)
  DIALOGUE-FLAT   dialogue share nearly identical across chapters (CV < 0.2)
  BREAKS-SAME     identical scene-break count 4+ chapters running
  RHYTHM-FLAT     median sentence length within 2 words across every chapter
  ONE-LINER-REFLEX > 50% of chapters open or close on a one-sentence paragraph

Exit code 0 = no flags (or not strict). It never edits anything.
"""
import argparse
import json
import re
import statistics
import sys
from pathlib import Path

CHAPTER_RE = re.compile(r"chapter-(\d+)\.md$")
BREAK_RE = re.compile(r"^\s*(\*\s*\*\s*\*|\* \* \*|---+|⁂|#{1,3}\s)\s*$|^\s*#{1,3}\s+\S")
HEADING_RE = re.compile(r"^\s*#{1,6}\s")
QUOTE_RE = re.compile(r"[“\"]([^”\"]{1,600})[”\"]")
PARA_QUOTE_RE = re.compile(r"[“\"]([^”\"\n]*)(?:[”\"]|$)")
SENT_SPLIT = re.compile(r"(?<=[.!?…])\s+(?=[\"“'(A-Z0-9])")
WORD_RE = re.compile(r"[A-Za-z’'\-]+")
TIME_OPENERS = re.compile(
    r"^(It was|That (morning|night|evening|afternoon|winter|summer|spring|autumn|year|day)|"
    r"The (morning|night|evening|afternoon|winter|summer|spring|autumn|day|first|last|next)|"
    r"In the (morning|evening|spring|summer|winter|autumn|year|days|weeks|months)|"
    r"By (the|then|morning|noon|evening|dawn|dusk)|On the (first|second|third|fourth|fifth|morning|day|night)|"
    r"(Two|Three|Four|Five|Six|Seven|Ten|Twenty) (days|weeks|months|years|hours))\b", re.I)


def chapters(book: Path):
    d = book / "manuscript" / "chapters"
    files = []
    for p in d.glob("chapter-*.md"):
        m = CHAPTER_RE.search(p.name)
        if m:
            files.append((int(m.group(1)), p))
    return [p for _, p in sorted(files)]


def prose_lines(text: str):
    out = []
    for line in text.splitlines():
        if HEADING_RE.match(line):
            continue
        out.append(line)
    return out


def paragraphs(lines):
    paras, cur = [], []
    for line in lines:
        if line.strip() == "" or BREAK_RE.match(line):
            if cur:
                paras.append(" ".join(cur).strip())
                cur = []
        else:
            cur.append(line.strip())
    if cur:
        paras.append(" ".join(cur).strip())
    return [p for p in paras if p]


def sentences(text: str):
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    return [s for s in SENT_SPLIT.split(text) if s.strip()]


def wc(text: str) -> int:
    return len(WORD_RE.findall(text))


def opening_signature(first_para: str):
    s = sentences(first_para)
    first = s[0] if s else first_para
    n = wc(first)
    if first.lstrip().startswith(("“", "\"", "‘")):
        return "dialogue"
    if TIME_OPENERS.match(first.strip()):
        return "scene-set"
    if re.match(r"^I\b", first.strip()):
        return "I-statement" if n > 8 else "I-punch"
    if n <= 8:
        return "short-punch"
    if n >= 28:
        return "long-spiral"
    return "narrative"


def ending_signature(last_para: str):
    s = sentences(last_para)
    last = s[-1] if s else last_para
    n = wc(last)
    stripped = last.strip()
    if stripped.endswith(("”", "\"")) or stripped.startswith(("“", "\"")):
        return "dialogue"
    if stripped.endswith("?"):
        return "question"
    if n <= 7:
        return "punch"
    if n >= 25:
        return "long-fade"
    return "quiet"


COMMENT_RE = re.compile(r"<!--.*?-->", re.S)


def analyse(path: Path):
    text = COMMENT_RE.sub("", path.read_text(encoding="utf-8", errors="replace"))
    lines = prose_lines(text)
    paras = paragraphs(lines)
    body = "\n".join(lines)
    words = wc(body)
    breaks = sum(1 for ln in text.splitlines() if BREAK_RE.match(ln) and not HEADING_RE.match(ln))
    # count ### scene headings as breaks too, but not the chapter title
    sub_heads = sum(1 for ln in text.splitlines() if re.match(r"^\s*#{2,3}\s", ln))
    breaks += sub_heads
    # Per paragraph, never across one: a speech left open at a paragraph's end (multi-paragraph speech)
    # counts to the end of that paragraph, and must not pair with the next paragraph's opening quote.
    quoted = sum(wc(m) for para in body.split("\n") for m in PARA_QUOTE_RE.findall(para))
    dlg = (quoted / words) if words else 0.0
    sents = sentences(body)
    slens = [wc(s) for s in sents] or [0]
    med = statistics.median(slens)
    short = sum(1 for n in slens if n <= 6) / len(slens)
    longp = sum(1 for n in slens if n >= 35) / len(slens)
    first_para = paras[0] if paras else ""
    last_para = paras[-1] if paras else ""
    return {
        "file": path.name,
        "words": words,
        "paragraphs": len(paras),
        "breaks": breaks,
        "dialogue": round(dlg, 3),
        "median_sent": med,
        "short_pct": round(short, 3),
        "long_pct": round(longp, 3),
        "open": opening_signature(first_para),
        "open_one_liner": len(sentences(first_para)) == 1,
        "end": ending_signature(last_para),
        "end_one_liner": len(sentences(last_para)) == 1,
        "first_line": sentences(first_para)[0][:90] if sentences(first_para) else "",
        "last_line": sentences(last_para)[-1][:90] if sentences(last_para) else "",
    }


def cv(xs):
    xs = [x for x in xs if x is not None]
    if len(xs) < 2:
        return 0.0
    m = statistics.mean(xs)
    if m == 0:
        return 0.0
    return statistics.pstdev(xs) / m


def longest_run(seq):
    best, cur, val, best_val = 0, 0, None, None
    for x in seq:
        if x == val:
            cur += 1
        else:
            val, cur = x, 1
        if cur > best:
            best, best_val = cur, val
    return best, best_val


def flags_for(rows):
    n = len(rows)
    flags = []
    if n < 4:
        return flags, ["need >= 4 chapters for a shape audit (have %d)" % n]
    notes = []
    words = [r["words"] for r in rows]
    if n >= 6:
        c = cv(words)
        ratio = (max(words) / min(words)) if min(words) else 0
        if c < 0.25 or ratio < 2.0:
            flags.append(("LEN-CLUSTER",
                          f"chapter lengths cluster: CV {c:.2f} (<0.25) / max÷min {ratio:.1f} (<2.0). "
                          "Real books are lumpy — vary length by beat, add a short punch or a long immersive chapter."))
    run, val = longest_run([r["open"] for r in rows])
    if run >= 3:
        flags.append(("OPEN-RUN", f"opening signature '{val}' {run} chapters running — rotate the opening move."))
    for sig in set(r["open"] for r in rows):
        share = sum(1 for r in rows if r["open"] == sig) / n
        if n >= 5 and share > 0.40:
            flags.append(("OPEN-SHARE", f"opening signature '{sig}' on {share:.0%} of chapters (>40%)."))
    run, val = longest_run([r["end"] for r in rows])
    if run >= 3:
        flags.append(("END-RUN", f"ending signature '{val}' {run} chapters running — rotate the closing move."))
    for sig in set(r["end"] for r in rows):
        share = sum(1 for r in rows if r["end"] == sig) / n
        if n >= 5 and share > 0.50:
            flags.append(("END-SHARE", f"ending signature '{sig}' on {share:.0%} of chapters (>50%)."))
    punch = sum(1 for r in rows if r["end"] == "punch") / n
    if n >= 5 and punch > 0.60:
        flags.append(("PUNCH-REFLEX", f"{punch:.0%} of chapters end on a <=7-word line. 'Every chapter ends on a hook' "
                                      "is itself a tell — let some chapters simply stop."))
    if n >= 6:
        d = cv([r["dialogue"] for r in rows])
        if d < 0.20:
            flags.append(("DIALOGUE-FLAT", f"dialogue share nearly identical across chapters (CV {d:.2f}) — a two-hander and an "
                                           "interior chapter should not weigh the same."))
    run, val = longest_run([r["breaks"] for r in rows])
    if run >= 4:
        flags.append(("BREAKS-SAME", f"exactly {val} scene breaks in {run} consecutive chapters — the same number of scenes every time."))
    if n >= 6:
        meds = [r["median_sent"] for r in rows]
        if max(meds) - min(meds) <= 2:
            flags.append(("RHYTHM-FLAT", f"median sentence length sits within 2 words across every chapter ({min(meds)}–{max(meds)}) — "
                                         "no chapter changes gear."))
    o1 = sum(1 for r in rows if r["open_one_liner"]) / n
    e1 = sum(1 for r in rows if r["end_one_liner"]) / n
    if n >= 5 and (o1 > 0.50 or e1 > 0.50):
        flags.append(("ONE-LINER-REFLEX", f"one-sentence paragraph opens {o1:.0%} / closes {e1:.0%} of chapters (>50%) — a formatting tic."))
    return flags, notes


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("book", help="book folder (contains manuscript/chapters/)")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any flag fires")
    ap.add_argument("--json", action="store_true", help="JSON output")
    args = ap.parse_args()
    book = Path(args.book)
    files = chapters(book)
    if not files:
        print(f"no chapters under {book}/manuscript/chapters/")
        return 2
    rows = [analyse(p) for p in files]
    flags, notes = flags_for(rows)
    if args.json:
        print(json.dumps({"chapters": rows, "flags": flags, "notes": notes}, indent=1))
        return 1 if (args.strict and flags) else 0
    print(f"SHAPE AUDIT — {book}  ({len(rows)} chapters, {sum(r['words'] for r in rows):,} words)\n")
    print(f"{'ch':>4} {'words':>6} {'brk':>3} {'dlg%':>5} {'med':>4} {'open':<12} {'end':<9}  first → last line")
    for r in rows:
        n = CHAPTER_RE.search(r["file"]).group(1)
        print(f"{n:>4} {r['words']:>6} {r['breaks']:>3} {r['dialogue']*100:>5.0f} {r['median_sent']:>4.0f} "
              f"{r['open']:<12} {r['end']:<9}  {r['first_line'][:38]!r} → {r['last_line'][:38]!r}")
    words = [r["words"] for r in rows]
    print(f"\nlength: min {min(words):,} / median {int(statistics.median(words)):,} / max {max(words):,} "
          f"/ CV {cv(words):.2f} / max÷min {(max(words)/min(words)) if min(words) else 0:.1f}")
    print(f"dialogue share: {min(r['dialogue'] for r in rows)*100:.0f}–{max(r['dialogue'] for r in rows)*100:.0f}% "
          f"(CV {cv([r['dialogue'] for r in rows]):.2f});  opening sigs: "
          + ", ".join(f"{s}×{sum(1 for r in rows if r['open']==s)}" for s in sorted(set(r['open'] for r in rows)))
          + ";  ending sigs: "
          + ", ".join(f"{s}×{sum(1 for r in rows if r['end']==s)}" for s in sorted(set(r['end'] for r in rows))))
    for note in notes:
        print(f"\nnote: {note}")
    if flags:
        print(f"\nFLAGS ({len(flags)}) — predictability detected:")
        for code, msg in flags:
            print(f"  [{code}] {msg}")
        print("\nRESULT: SHAPE FLAGS (uniformity) — vary the next chapters away from the flagged signature;"
              " if the run is on finalized chapters, revise the most recent offender.")
        return 1 if args.strict else 0
    print("\nRESULT: SHAPE CLEAN — no uniformity pattern across chapters.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
