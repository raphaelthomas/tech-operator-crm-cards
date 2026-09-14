#!/usr/bin/env python3
"""Render use/*.md as A6 pocket cards.

The markdown is the source of truth: this only decides layout - which
sections go on which side, and which of them are ordered sequences that
earn step numbers. Text is never rewritten. check.py enforces that.
"""
import html as H, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
USE = ROOT.parent / "use"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# sides: the sections printed on each A6 side, in order ("*" = everything)
# numbered: sections that are a sequence to work through, not a set of rules
# split_before: break one paragraph into steps at these opening words
CARDS = {
    "0-always": dict(sides=[["*"]], numbered=[]),
    "1-before-change": dict(
        sides=[["Time-Out - stop, out loud, everyone", "Pre-mortem"],
               ["Go / No-Go", "On the keys", "Solo"]],
        numbered=["Time-Out - stop, out loud, everyone", "Pre-mortem"],
        split_before={"Pre-mortem": ["Mitigate or accept each"]}),
    "2-during-incident": dict(
        sides=[["Reset - 10 for 10", "Scope - Is / Is-Not", "Decide - FOR-DEC"],
               ["Stop rules", "Solo"]],
        numbered=[]),
    "3-handover-brief": dict(
        sides=[["SBAR", "Check-back", "Transfer control"]],
        numbered=["Transfer control"]),
    "4-blameless-postmortem": dict(
        sides=[["", "Setup"], ["Analysis", "Actions"]],
        numbered=[], dense=True),
}

BRAND = "Tech Ops CRM"
REPO = "github.com/raphaelthomas/tech-operator-crm-cards"
SENTENCE = re.compile(r"(?<=[.?!])\s+")


def inline(s):
    s = H.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", s)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", s)


def lay_out(text):
    """One line per sentence, and a line of its own for a lead-in colon.

    Values on a card are read at a glance, not as prose: breaking them the
    way they are spoken beats wrapping them to the column width.
    """
    parts, out = SENTENCE.split(text), []
    for p in parts:                       # never break inside bold markers
        if out and out[-1].count("**") % 2:
            out[-1] += " " + p
        else:
            out.append(p)

    lines = []
    for chunk in out:
        # "Name roles aloud: a · b · c" -> lead-in on its own line, then one
        # line per item. Only lists a colon introduces are broken up this
        # way; a bare mnemonic stays on one line.
        m = re.match(r"^([^:]{1,40}:)\s+(.*·.*)$", chunk)
        if m:
            lines.append(m.group(1))
            items = [part.strip() for part in m.group(2).split("·")]
            # the separator stays on the line it followed: nothing is dropped
            lines += [f"{p} ·" for p in items[:-1]] + items[-1:]
        else:
            lines.append(chunk)
    return "<br>".join(inline(l) for l in lines)


def parse(md):
    """-> (title, [ {heading, items} ]) with items as typed tuples."""
    title, blocks, cur = None, [], {"heading": "", "items": []}
    para = []

    def flush():
        if para:
            cur["items"].append(("prose", "<br>".join(lay_out(l) for l in para)))
            para.clear()

    for line in md.splitlines():
        s = line.rstrip()
        if s.startswith("# "):
            title = re.sub(r"^[^\x00-\x7F\s]+\s*", "", s[2:]).strip()
        elif s.startswith(("## ", "### ")):
            flush(); blocks.append(cur)
            cur = {"heading": s.lstrip("# ").strip(), "items": []}
        elif s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) == 2 and not set(cells[0]) <= set(": -"):
                flush()
                cur["items"].append(("row", inline(cells[0]), lay_out(cells[1])))
        elif s.startswith("> "):
            flush()
            cur["items"].append(("quote", inline(re.sub(r"^[-*]\s+", "", s[2:]))))
        elif s.startswith("- "):
            flush()
            cur["items"].append(("bullet", inline(s[2:])))
        elif s.strip():
            para.append(s.strip())
        else:
            flush()
    flush(); blocks.append(cur)
    return title, [b for b in blocks if b["items"]]


def render_items(block, numbered, split_before):
    items, n = block["items"], 0
    heading = block["heading"]
    # a section of quoted lines numbers the quotes only: the sentences that
    # introduce and close them are not steps
    quotes_only = any(k == "quote" for k, *_ in items)

    def step(kind):
        nonlocal n
        if heading not in numbered or (quotes_only and kind != "quote"):
            return ""
        n += 1
        return f'<span class="n">{n}</span>'


    if all(k == "bullet" for k, *_ in items):          # Solo-style lists
        paras = []
        for _, text in items:
            lead = re.sub(r"^([^:]+:)", r"<strong>\1</strong>", text)
            paras.append(f"\n      <p>{lead}</p>")
        return '\n    <div class="body">' + "".join(paras) + "\n    </div>"

    rows = []
    for kind, *rest in items:
        if kind == "prose":
            chunks = [rest[0]]
            for marker in split_before.get(heading, []):
                nxt = []
                for c in chunks:
                    parts = SENTENCE.split(c)
                    at = next((i for i, p in enumerate(parts)
                               if p.startswith(marker)), None)
                    nxt += ([" ".join(parts[:at]), " ".join(parts[at:])]
                            if at else [c])
                chunks = nxt
            for c in chunks:
                rows.append(f'      <li class="prose">{step("prose")}'
                            f'<span class="resp">{c}</span></li>')
        elif kind == "quote":
            rows.append(f'      <li class="prose">{step("quote")}'
                        f'<span class="resp">{rest[0]}</span></li>')
        else:
            rows.append(f'      <li>{step("row")}<span class="item">{rest[0]}</span>'
                        f'\n        <span class="resp">{rest[1]}</span></li>')
    return "\n    <ol>\n" + "\n".join(rows) + "\n    </ol>"


def title_card():
    """Deck cover: the deck's name, nothing else.

    Both lines are set to the same printed width, so they lock flush at
    either edge. Sizes are in card.css.
    """
    cover = f'''
<article class="card cover">
  <h1 class="deck-title">
    <span class="l1">Tech</span>
    <span class="l2">Ops</span>
    <span class="l3">CRM</span>
  </h1>
</article>
'''
    (ROOT / "title.html").write_text(PAGE.format(title=BRAND, body=cover))
    return ROOT / "title.html", [cover]


def closing_card():
    """Back of the deck: where it came from."""
    closing = f'''
<article class="card cover closing">
  <p class="repo">{REPO}</p>
</article>
'''
    (ROOT / "closing.html").write_text(PAGE.format(title=BRAND, body=closing))
    return ROOT / "closing.html", [closing]


def build(stem):
    cfg = CARDS[stem]
    assert len(cfg["sides"]) <= 2, f"{stem}: a card is one sheet, two sides at most"
    md = (USE / f"{stem}.md").read_text()
    title, blocks = parse(md)
    index = stem.split("-")[0].zfill(2)
    by_heading = {b["heading"]: b for b in blocks}

    sides = []
    for side in cfg["sides"]:
        wanted = blocks if side == ["*"] else [by_heading[h] for h in side]
        parts = []
        for b in wanted:
            body = render_items(b, cfg["numbered"], cfg.get("split_before", {}))
            if not b["heading"]:
                parts.append(f'\n  <section class="box nonum bare">{body}'
                             f'\n  </section>')
                continue
            cls = "box" if b["heading"] in cfg["numbered"] else "box nonum"
            if all(k == "bullet" for k, *_ in b["items"]):
                cls += " solo"
            parts.append(f'\n  <section class="{cls}">\n    '
                         f'<h2>{inline(b["heading"])}</h2>{body}\n  </section>')
        klass = "card dense" if cfg.get("dense") else "card"
        sides.append(f'''
<article class="{klass}">

  <header class="masthead">
    <span class="index">{index}</span>
    <span class="title">{title}</span>
    <span class="strap">{BRAND}</span>
  </header>
{"".join(parts)}

</article>
''')

    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title} - Tech Operator CRM Cards</title>
<link rel="stylesheet" href="card.css">
</head>
<body>
{"".join(sides)}
</body>
</html>
'''
    out = ROOT / f"{stem}.html"
    out.write_text(doc)
    return out, sides


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<link rel="stylesheet" href="card.css">
</head>
<body>
{body}
</body>
</html>
"""

def deck(all_sides):
    """One file, every card, continuous - no blank padding."""
    pages, sheet = [], []
    for stem, sides in all_sides:
        sheet.append((stem, len(sides), 0))
        pages += sides
    (ROOT / "deck.html").write_text(PAGE.format(
        title="Tech Operator CRM Cards", body="".join(pages)))
    return sheet, len(pages)


SCRATCH = ROOT / ".fit"


def fit(page, sides):
    """Percentage of each A6 side actually used. Clipping shows up as ~100%."""
    from PIL import Image
    SCRATCH.mkdir(exist_ok=True)
    doc = page.read_text().replace('href="card.css"',
                                   f'href="{ROOT / "card.css"}"')
    out = []
    for i in range(sides):
        hide = f".card:not(:nth-of-type({i + 1})) {{ display: none }}"
        one = SCRATCH / f"{page.stem}-{i}.html"
        one.write_text(doc.replace("</head>", f"<style>{hide}</style></head>"))
        pdf = one.with_suffix(".pdf")
        subprocess.run([CHROME, "--headless", "--disable-gpu",
                        "--no-pdf-header-footer", f"--print-to-pdf={pdf}",
                        str(one)], capture_output=True)
        png = SCRATCH / f"{pdf.name}.png"
        png.unlink(missing_ok=True)
        subprocess.run(["qlmanage", "-t", "-s", "1000", "-o", str(SCRATCH),
                        str(pdf)], capture_output=True)
        im = Image.open(png).convert("L")
        w, h = im.size
        rows = [y for y in range(h)
                if any(im.getpixel((x, y)) < 245 for x in range(0, w, 3))]
        out.append(100 * (rows[-1] + 1) / h if rows else 0)
    return out


if __name__ == "__main__":
    stems = sys.argv[1:] or list(CARDS)
    collected = []
    if not sys.argv[1:]:
        page, sides = title_card()
        collected.append(("title", sides))
        subprocess.run([CHROME, "--headless", "--disable-gpu",
                        "--no-pdf-header-footer",
                        f"--print-to-pdf={page.with_suffix('.pdf')}",
                        str(page)], capture_output=True)
        print(f'{"title":24} cover')
    for stem in stems:
        page, sides = build(stem)
        collected.append((stem, sides))
        pdf = page.with_suffix(".pdf")
        subprocess.run([CHROME, "--headless", "--disable-gpu",
                        "--no-pdf-header-footer", f"--print-to-pdf={pdf}",
                        str(page)], capture_output=True)
        chk = subprocess.run([sys.executable, str(ROOT / "check.py"),
                              str(USE / f"{stem}.md"), str(page)],
                             capture_output=True, text=True)
        ok = chk.stdout.strip() or chk.stderr.strip()
        fills = fit(page, len(CARDS[stem]["sides"]))
        marks = " ".join(
            f"side {i + 1}: {f:.0f}%" + ("  CLIPPED?" if f > 97 else "")
            for i, f in enumerate(fills))
        print(f'{stem:24} {"OK" if ok.startswith("OK") else ok}   {marks}')

    if not sys.argv[1:]:
        page, sides = closing_card()
        collected.append(("closing", sides))
        subprocess.run([CHROME, "--headless", "--disable-gpu",
                        "--no-pdf-header-footer",
                        f"--print-to-pdf={page.with_suffix('.pdf')}",
                        str(page)], capture_output=True)
        print(f'{"closing":24} repo link')

    sheets, total = deck(collected)
    subprocess.run([CHROME, "--headless", "--disable-gpu",
                    "--no-pdf-header-footer",
                    f"--print-to-pdf={ROOT / 'deck.pdf'}",
                    str(ROOT / "deck.html")], capture_output=True)
    print()
    for stem, n, pad in sheets:
        print(f'  {stem:24} {n} side(s)' + (' + 1 blank' if pad else ''))
    print(f'  deck.pdf: {total} pages')
