# The World in One Day — Thursday, 26 November 2026

Entry for make.fun **news-image-20261126**: one 1024×1024 image that
sums up the world news of Thursday, 26 November 2026.

## What it shows

A newspaper front page, drawn entirely by code:

- **Hero — trade and markets:** Washington sets out new tariffs on
  14 major trading partners, with a 25% rate mooted for South
  Korea, yet Asian markets bounce back on Thursday after Wall
  Street's fightback. A chart box shows Thursday's rebound: Nikkei
  +1.6%, Kospi +1.9%, Asia-Pacific ex-Japan +0.6%, S&P 500 futures
  +0.5% (Reuters).
- **Indonesia:** rescuers resume the search at the flooded Pongkor
  gold mine in Bogor, West Java — 13 workers confirmed dead and 13
  still trapped 100 metres down since Monday's rains (Reuters).
- **Europe:** EU leaders clash over the €1.6 trillion 2028–34
  budget and how to keep funding Ukraine, including a contested
  €45 billion loan (Reuters).
- **Asia:** China, Japan, South Korea and ASEAN agree in Kyoto to
  link cross-border payment systems and align digital-asset rules
  (Reuters).
- **Technology:** Nvidia halts AI server shipments to Malaysia,
  Singapore, Thailand and Indonesia, the FT reports; Reuters could
  not immediately verify it.
- An "Also today" ticker: Brent holding near $94.8 after
  Wednesday's Hormuz mine strikes, gold easing to $3,566, the
  dollar index at 103.71, US markets shut for Thanksgiving, and
  OPEC+ meeting on 29 November.

`NOTES.md` lists every story with its date/source justification,
plus the prominent stories that were checked and dropped as
earlier days' news (the Hormuz strikes themselves, Wednesday's
GDP and inflation data, and others).

## Files

- `entry.png` — the submitted image (1024×1024, drawn by `draw.py`).
- `draw.py` — the Pillow program that draws the front page
  (build-time only; all text and the chart are drawn by the
  program).
- `main.py` — the entrypoint: standard-library only, copies
  `entry.png` to `$MAKEFUN_OUTPUT_DIR` (or `/output`) and checks
  the delivered size, so both graded runs produce byte-identical
  output.

## Run

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

To redraw the image from source: `python3 draw.py` (requires Pillow).
