#!/usr/bin/env python3
"""Draw 'The World in One Day' front page for Thursday 26 November 2026.

Build-time only: renders entry.png (1024x1024) with Pillow. All stories
were date-checked against wire coverage of Thursday 26 Nov 2026; see
NOTES.md for the source and dateline of every item.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
MARGIN = 44
PAPER = (248, 244, 233)
INK = (24, 22, 19)
FAINT = (96, 90, 80)
ACCENT = (150, 30, 24)
GREEN = (22, 108, 50)
BOX = (238, 231, 214)
BAND = (28, 26, 24)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def f(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, font, width):
    """Greedy word wrap against a pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def block(draw, x, y, text, font, width, leading, fill=INK):
    for line in wrap(draw, text, font, width):
        draw.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def kicker(draw, x, y, text):
    draw.text((x, y), text, font=f(SANS_B, 18), fill=ACCENT)
    return y + 27


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
CW = W - 2 * MARGIN  # column width

# ---------------- masthead ----------------
d.line([(MARGIN, 34), (W - MARGIN, 34)], fill=INK, width=5)
mast = f(SERIF_B, 63)
title = "THE WORLD IN ONE DAY"
tw = d.textlength(title, font=mast)
d.text(((W - tw) / 2, 48), title, font=mast, fill=INK)
d.line([(MARGIN, 128), (W - MARGIN, 128)], fill=INK, width=2)
d.line([(MARGIN, 134), (W - MARGIN, 134)], fill=INK, width=5)

date_f = f(SANS_B, 21)
d.text((MARGIN, 148), "THURSDAY, 26 NOVEMBER 2026", font=date_f, fill=INK)
tag = "The day's world news, on one page"
tag_f = f(SERIF_I, 20)
d.text((W - MARGIN - d.textlength(tag, font=tag_f), 148), tag, font=tag_f, fill=FAINT)
d.line([(MARGIN, 182), (W - MARGIN, 182)], fill=INK, width=2)

# ---------------- hero ----------------
y = 196
y = kicker(d, MARGIN, y, "TRADE  ·  MARKETS")
head_f = f(SERIF_B, 47)
for line in ("US unveils tariffs on 14 partners,",
             "and Asia's markets bounce back"):
    d.text((MARGIN, y), line, font=head_f, fill=INK)
    y += 57
y += 10

stand = ("Washington set out new duties on 14 major trading partners under "
         "its unfair-trade probe \u2014 a 25% rate mooted for South Korea, "
         "which vowed talks to protect its interests. Yet after Wall Street "
         "fought back from deep lows, Asian shares rallied on Thursday, led "
         "by Tokyo and Seoul, even as AI-financing worries lingered. "
         "(Reuters, Thursday)")
y_end = block(d, MARGIN, y, stand, f(SERIF, 19.5), 560, 26)

# chart box: Thursday's rebound
bx, by, bw, bh = 648, y, W - MARGIN - 648, 182
d.rectangle([bx, by, bx + bw, by + bh], fill=BOX, outline=INK, width=2)
d.text((bx + 16, by + 11), "THURSDAY'S REBOUND", font=f(SANS_B, 17), fill=INK)
rows = [("Nikkei 225 (Tokyo)", "+1.6%"),
        ("Kospi (Seoul)", "+1.9%"),
        ("Asia-Pacific ex-Japan", "+0.6%"),
        ("S&P 500 futures", "+0.5%")]
ry = by + 44
for name, val in rows:
    d.text((bx + 16, ry), name, font=f(SANS, 15.5), fill=INK)
    vw = d.textlength(val, font=f(SANS_B, 16))
    d.text((bx + bw - 16 - vw, ry - 1), val, font=f(SANS_B, 16), fill=GREEN)
    pct = float(val.strip('+%')) / 2.0
    d.rectangle([bx + 16, ry + 21, bx + 16 + int(190 * pct), ry + 27], fill=GREEN)
    ry += 35
y = max(y_end, by + bh) + 14

d.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=2)
panel_top = y + 14

# ---------------- panels (2 x 2) ----------------
panels = [
    ("INDONESIA",
     "13 dead, 13 still trapped as search resumes at Pongkor",
     "Rescuers resumed the search on Thursday for 13 workers still "
     "trapped 100 metres down at an unauthorised gold mine in Bogor, "
     "West Java, with 13 more confirmed dead. The 26 men were cut off "
     "on Monday when heavy rain flooded the shaft. (Reuters)"),
    ("EUROPE",
     "EU leaders clash over \u20ac1.6tn budget and Ukraine cash",
     "Leaders met on Thursday to wrestle over the 2028\u201334 budget "
     "and how to keep funding Ukraine: up to \u20ac100 billion is in "
     "the plan, but four countries object to a \u20ac45 billion loan "
     "for Kyiv. (Reuters)"),
    ("ASIA",
     "China, Japan, Korea and ASEAN to link payments",
     "ASEAN+3 finance deputies agreed in Kyoto on Thursday to connect "
     "cross-border payment systems and align digital-asset rules, "
     "and flagged a new emergency lending tool under the $240 "
     "billion safety net. (Reuters)"),
    ("TECHNOLOGY",
     "Nvidia halts chip shipments to Southeast Asia",
     "Nvidia has told its partners to stop shipping AI servers to "
     "Malaysia, Singapore, Thailand and Indonesia, the Financial "
     "Times reported on Thursday; Reuters could not immediately "
     "verify it. (FT via Reuters)"),
]
col_w = (CW - 28) // 2
ROW_H = 176
for i, (kick, head, body) in enumerate(panels):
    px = MARGIN + (i % 2) * (col_w + 28)
    py = panel_top + (i // 2) * ROW_H
    d.line([(px, py), (px + col_w, py)], fill=INK, width=2)
    ky = kicker(d, px, py + 9, kick)
    hy = block(d, px, ky, head, f(SANS_B, 23), col_w, 28)
    block(d, px, hy + 5, body, f(SERIF, 16), col_w, 20.5)

# ---------------- ticker ----------------
band_y = 912
d.rectangle([0, band_y, W, H], fill=BAND)
d.text((MARGIN, band_y + 13), "ALSO TODAY", font=f(SANS_B, 18), fill=(240, 200, 90))
ticker = ("Brent crude holds near $94.8 after Wednesday's mine strikes on two tankers "
          "in the Strait of Hormuz  \u00b7  Gold eases 0.4% to $3,566  \u00b7  Dollar index "
          "103.71; yen steady at 159.14  \u00b7  US markets shut for Thanksgiving \u2014 no "
          "WTI settlement on Thursday  \u00b7  OPEC+ meets on 29 November to set 2027 "
          "output policy")
block(d, MARGIN, band_y + 42, ticker, f(SANS, 16), CW, 21.5, fill=(238, 234, 224))

img.save("entry.png", optimize=True)
print("saved entry.png")
