"""Shared helpers for Sygl's production build (assemble, interior, placeholder cover).

- load_config(): delivery/ebook.yaml, the single source for title, author, ISBNs,
  trim and revision.
- smarten(): typesetting-only typography. The chapter files use straight ASCII
  quotes and "..."; print and ebook get curly quotes, apostrophes and a true
  ellipsis. The chapter files themselves are never touched.
"""
import os, re

BOOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = os.path.join(BOOK, "delivery", "ebook.yaml")


def load_config():
    import yaml
    with open(CONFIG, encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh)
    for k in ("title", "author", "year", "revision", "isbn_hyphen", "print"):
        if not cfg.get(k):
            raise SystemExit(f"error: {CONFIG} is missing '{k}'")
    return cfg


def manuscript_path(cfg):
    return os.path.join(BOOK, "manuscript", f"full-manuscript-{cfg['revision']}.md")


_LEAD = set(" \t\n([{\u2014\u2013")          # a quote after these opens
_OPEN_CTX = _LEAD | set("*_\"'\u201c\u2018")   # ...and, weaker, after these
_CLOSE_NEXT = set(".,;:!?)]}\u2014\u2013*_\"'")


def _quote(ch, prev, nxt):
    o, c = ("\u201c", "\u201d") if ch == '"' else ("\u2018", "\u2019")
    if ch == "'" and prev and prev.isalnum() and nxt and nxt.isalnum():
        return c                                   # don't, Bal's
    if nxt is None or nxt.isspace():
        return c                                   # ...said." / the girls' room
    if prev is None or prev in _LEAD:
        return o                                   # opens a line / follows a space
    if nxt in _CLOSE_NEXT:
        return c                                   # Why?"* / Heirs,'"
    if prev in _OPEN_CTX:
        return o                                   # *"Why / "'The
    return c


def smarten(text):
    """Straight quotes -> curly, '...' -> ellipsis. Decides by context, char by char."""
    text = text.replace("...", "\u2026")
    out = []
    for i, ch in enumerate(text):
        if ch in "\"'":
            prev = text[i - 1] if i else None
            nxt = text[i + 1] if i + 1 < len(text) else None
            out.append(_quote(ch, prev, nxt))
        else:
            out.append(ch)
    return "".join(out)
