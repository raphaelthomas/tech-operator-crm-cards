# Print

A6 pocket cards (105 x 148 mm) generated from `use/*.md`.

## Render

```sh
python3 build.py              # every card, plus the deck
python3 build.py 2-during-incident   # one card
```

Produces one PDF per card, plus `deck.pdf` with all of them.

## Requires

- **B612 and B612 Mono installed** as system fonts. `card.css` asks for them
  by family name, so a machine without them renders in the fallback face
  *without any error* - and the cover sizes, which are solved for B612's
  metrics, stop meaning anything. Check the output if you are not on a
  machine that has them.
- **Google Chrome**, used headless as the PDF renderer. The path is hardcoded
  at the top of `build.py`.
- **Pillow**, and **macOS** (`qlmanage`) for the fit report only.

Only `deck.pdf` is committed; every other HTML and PDF here is build output.
It carries B612 subsets embedded, so it prints correctly anywhere, including
where the build itself would not run.

Output per run:

```
1-before-change          OK   side 1: 75% side 2: 73%
```

`OK` is the source check; the percentages are how much of each A6 side the
content fills. Anything over 97% is flagged `CLIPPED?` - the card overflows
and needs a section moved to another side.

## The markdown is the source

`build.py` never rewrites text. It decides layout only: which sections go on
which side, which sections are ordered sequences that earn step numbers, and
whether a card takes the denser setting. All of it lives in `CARDS` at the
top of the file.

A card is one sheet: two sides at most, asserted at build time. If a card no
longer fits, move the fold rather than adding a third side - and if it still
does not fit, mark it `dense=True`, as card 04 is.

`check.py` enforces this after every build, in both directions: every string
in the markdown appears on the card, and everything on the card comes from
the markdown. The only permitted exceptions are listed in `CHROME` there -
card index, brand line, step numbers, and the title emoji, which does not
print.

## Printing

- **Duplex, short-edge binding**, at 100% scale. Do not use "fit to page".
- The deck is continuous: no blank padding, so one sheet can carry the back
  of one card and the front of the next. Cut accordingly.
- `deck.pdf` opens with the title card and is 9 pages.

## Type

B612 and B612 Mono, designed for Airbus cockpit displays and named after the
asteroid in *The Little Prince*. Chrome subsets both into the PDF, so it
prints correctly on a machine without the font installed.
