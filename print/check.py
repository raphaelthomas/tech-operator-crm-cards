#!/usr/bin/env python3
"""Verify a print card against its markdown source, both directions.

  forward  - every string in the .md appears on the card
  reverse  - every string on the card appears in the .md

Only CHROME (below) may appear on a card without being in the source.
"""
import html, re, sys

# Deliberate deviations, and the only ones allowed:
#   - the card index and brand line, which are card furniture
#   - step numbers inside an ordered section
#   - the emoji in a card title, dropped because it does not print
CHROME = {"01", "02", "03", "04", "0", "tech ops crm"}
EMOJI = re.compile(r"[\U0001F300-\U0001FAFF\u2190-\u21FF\u2600-\u27BF\uFE0F]")

INLINE = re.compile(r"</?(?:strong|em|code|b|i)>")


def norm(s):
    """Text as a reader sees it: inline tags vanish, block tags become space."""
    s = INLINE.sub("", s)                       # **I**llness -> Illness
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\*+", "", html.unescape(s))    # *not* -> not
    return re.sub(r"\s+", " ", EMOJI.sub("", s)).strip()

def source_strings(md):
    out = []
    for line in md.splitlines():
        line = line.strip()
        if line.startswith("> "):
            line = re.sub(r"^[-*]\s+", "", line[2:]).strip()
        if line.startswith("|") and "**" in line:
            out += [c for c in (x.strip() for x in line.strip("|").split("|")) if c]
        elif line.startswith("- "):
            out.append(line[2:])
        elif line.startswith("#"):
            out.append(line.lstrip("# ").strip())
        elif line and not line.startswith("|"):
            out.append(line)
    return out

def card_strings(doc):
    body = doc[doc.index("<body>"):]
    return [norm(m) for m in re.findall(r"<(?:h2|span|li)\b[^>]*>(.*?)</(?:h2|span|li)>", body, re.S)]

def main(md_path, html_path):
    md, doc = open(md_path).read(), open(html_path).read()
    blob = norm(md.replace("|", " "))
    # step numbers interrupt source sentences split across list items; drop them
    # before checking that the source text survives on the card
    card = norm(re.sub(r'<span class="n">.*?</span>', " ", doc, flags=re.S))

    missing = [s for s in source_strings(md) if norm(s) and norm(s) not in card]
    invented = [s for s in card_strings(doc)
                if s and s.lower() not in CHROME and not s.isdigit() and s not in blob]

    for label, items in (("not on the card", missing), ("not in the source", invented)):
        if items:
            print(f"FAIL - {len(items)} string(s) {label}:")
            for s in items:
                print(f"    {s!r}")
    if not missing and not invented:
        print(f"OK - {html_path} matches {md_path} in both directions")
        return 0
    return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
