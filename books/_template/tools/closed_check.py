#!/usr/bin/env python3
"""
closed_check.py — the machine-readable half of the character bible's SPENT/CLOSED ledger.

The bible's "At-risk after Ch.N" blocks name constructions that are SPENT or CLOSED for the rest of
the book ("and stayed" closed after Ch.15, "looked at X, and at Y" cut in Ch.25 …). Nobody greps
prose for them by hand reliably; an evaluator once spent a whole cycle finding ten that had been on the
page since the draft. Every ledger entry that CAN be a regex goes into tools/closed_ledger.tsv, and
this gate fails a chapter that uses one after the chapter that closed it.

Ledger format (tab-separated, '#' comments allowed):
    <regex>\t<closed after chapter N>\t<label>
The regex is Python, matched case-insensitively against the chapter body (HTML comments stripped).
Only chapters numbered > N are checked, so the uses that earned the closure stay legal.

Usage: python3 tools/closed_check.py <chapter-number>
Exit 1 and "RESULT: FAIL" on any hit; "RESULT: clean" otherwise.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "tools", "closed_ledger.tsv")


def load_ledger():
    rows = []
    if not os.path.exists(LEDGER):
        return rows
    for i, raw in enumerate(open(LEDGER, encoding="utf-8"), 1):
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            print(f"closed_ledger.tsv:{i}: need <regex>TAB<chapter>TAB<label>; skipped")
            continue
        try:
            rows.append((re.compile(parts[0], re.I), int(parts[1]), parts[2]))
        except (re.error, ValueError) as e:
            print(f"closed_ledger.tsv:{i}: {e}; skipped")
    return rows


def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        sys.exit("usage: closed_check.py <chapter-number>")
    n = int(sys.argv[1])
    path = os.path.join(ROOT, "manuscript", "chapters", f"chapter-{n}.md")
    text = re.sub(r"<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"),
                  open(path, encoding="utf-8").read(), flags=re.S)
    lines = text.splitlines()
    rows = [r for r in load_ledger() if n > r[1]]
    hits = 0
    for rx, since, label in rows:
        for ln, s in enumerate(lines, 1):
            for m in rx.finditer(s):
                hits += 1
                print(f"  l.{ln}: \"{m.group(0)}\" — {label} (closed after Ch.{since})")
    if hits:
        print(f"RESULT: FAIL — {hits} SPENT/CLOSED construction(s) reused; cut or recast (never restore a closed device)")
        sys.exit(1)
    print(f"RESULT: clean ({len(rows)} closed constructions checked)")


if __name__ == "__main__":
    main()
