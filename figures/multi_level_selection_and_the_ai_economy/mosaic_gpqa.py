"""Generate mosaic_gpqa.svg: a "real data" version of the 2D mosaic figure.

The firm: a two-person materials startup employing a chemist and a physicist.

Human data -- GPQA paper (Rein et al. 2023, arXiv:2311.12022), Figure 2:
accuracy of expert validators answering questions in their own domain
(diagonal) and in other domains (off-diagonal), GPQA extended set,
with unrestricted web access (no LLMs), ~30+ min per question for non-experts.

                       answered by chemists    answered by physicists
  chemistry questions        72.6 (n=219)            31.6 (n=563)
  physics questions          34.5 (n=339)            57.9 (n=233)

Bot data:
  GPT-4 (2023), few-shot chain-of-thought, GPQA extended set, same paper
  (Sec. 4): chemistry 31.8, physics 37.0.
  Claude Sonnet 4.6 (Feb 2026), GPQA Diamond per-domain scores from
  interfaze.ai/leaderboards/gpqa-diamond (third-party): chemistry 89.0,
  physics 93.0, biology 80.0. Weighted by Diamond's domain counts
  (93 chem / 86 phys / 19 bio) these reproduce the 89.9% overall Anthropic
  reported, which is the cross-check for using them.

Caveat: humans and GPT-4 are scored on the extended set (546 questions),
Sonnet 4.6 on the Diamond subset (198). The GPQA authors report no consistent
model accuracy difference between the sets; Diamond was filtered to be hard
for non-experts, so if anything this understates the bot.

Rectangles are anchored at chance (25%, four-option multiple choice), not 0.

Shares colors/fonts with mosaic_triangle.py.
Run:  python3 figures/multi_level_selection_and_the_ai_economy/mosaic_gpqa.py
"""
import sys
from pathlib import Path

sys.dont_write_bytecode = True
from mosaic_triangle import BG, INK, MUTED, GRID, RED, RED_FILL, LAV, LAV_FILL, SERIF, SANS  # noqa: E402

# ---- data -------------------------------------------------------------
X_AXIS, Y_AXIS = "Chemistry", "Physics"
CHANCE = 25.0
PEOPLE = [
    ("Chemist", "Chemistry+ / Physics−", (72.6, 34.5)),
    ("Physicist", "Physics+ / Chemistry−", (31.6, 57.9)),
]
MOSAIC = tuple(max(p[2][i] for p in PEOPLE) for i in range(2))
AVERAGE = tuple(sum(p[2][i] for p in PEOPLE) / len(PEOPLE) for i in range(2))

BOT = ("Claude Sonnet 4.6", "2026 frontier model", (89.0, 93.0))
OLD_BOT = ("GPT-4", "2023", (31.8, 37.0))

BOT_C = "#5a8f8c"
BOT_FILL = "#a9cdca"

VMIN, VMAX = CHANCE, 100.0
W, H = 900, 1290


class Plot:
    """Square plot area for accuracies in [VMIN, VMAX]; rectangles start at chance."""

    def __init__(self, left, top, size):
        self.left, self.top, self.size = left, top, size
        self.bottom = top + size
        self.k = size / (VMAX - VMIN)

    def xy(self, v, m):
        return self.left + (v - VMIN) * self.k, self.bottom - (m - VMIN) * self.k

    def rect(self, v, m, attrs):
        x0, y0 = self.xy(VMIN, m)
        x1, y1 = self.xy(v, VMIN)
        return (f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{x1 - x0:.1f}" '
                f'height="{y1 - y0:.1f}" {attrs}/>')

    def dot(self, v, m, color, r):
        x, y = self.xy(v, m)
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"/>'

    def label(self, v, m, text, dx, dy, color, size=14, anchor="start", family=SERIF):
        x, y = self.xy(v, m)
        return (f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" font-family="{family}" '
                f'font-size="{size}" fill="{color}" text-anchor="{anchor}">{text}</text>')

    def frame(self, label_size, label_pad, ticks=False):
        L, T, S, B = self.left, self.top, self.size, self.bottom
        out = [f'<rect x="{L}" y="{T}" width="{S}" height="{S}" fill="none" '
               f'stroke="{GRID}" stroke-width="1.2"/>']
        for t in (50, 75):
            d = (t - VMIN) * self.k
            out.append(f'<line x1="{L + d:.1f}" y1="{T}" x2="{L + d:.1f}" y2="{B}" '
                       f'stroke="{GRID}" stroke-width="0.8" stroke-dasharray="2 3"/>')
            out.append(f'<line x1="{L}" y1="{B - d:.1f}" x2="{L + S}" y2="{B - d:.1f}" '
                       f'stroke="{GRID}" stroke-width="0.8" stroke-dasharray="2 3"/>')
        unit = "%" if ticks else ""
        if ticks:
            for t in (25, 50, 75, 100):
                d = (t - VMIN) * self.k
                out.append(f'<text x="{L + d:.1f}" y="{B + 16}" font-family="{SANS}" font-size="11" '
                           f'fill="{MUTED}" text-anchor="middle">{t}%</text>')
                if t > VMIN:
                    out.append(f'<text x="{L - 8}" y="{B - d + 4:.1f}" font-family="{SANS}" '
                               f'font-size="11" fill="{MUTED}" text-anchor="end">{t}%</text>')
            out.append(f'<text x="{L}" y="{B + 29}" font-family="{SANS}" font-size="10" '
                       f'fill="{MUTED}" text-anchor="middle">(chance)</text>')
        out.append(f'<line x1="{L}" y1="{B}" x2="{L + S}" y2="{B}" stroke="{MUTED}" stroke-width="1"/>')
        out.append(f'<line x1="{L}" y1="{B}" x2="{L}" y2="{T}" stroke="{MUTED}" stroke-width="1"/>')
        xl = f"{X_AXIS} accuracy →" if ticks else f"{X_AXIS} →"
        yl = f"{Y_AXIS} accuracy →" if ticks else f"{Y_AXIS} →"
        out.append(f'<text x="{L + S / 2}" y="{B + label_pad + label_size * 0.7:.1f}" '
                   f'font-family="{SERIF}" font-size="{label_size}" fill="{INK}" '
                   f'text-anchor="middle">{xl}</text>')
        lx, ly = L - label_pad, T + S / 2
        out.append(f'<text x="{lx}" y="{ly}" font-family="{SERIF}" font-size="{label_size}" '
                   f'fill="{INK}" text-anchor="middle" transform="rotate(-90 {lx} {ly})">{yl}</text>')
        return out


def build():
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
         f'<rect width="{W}" height="{H}" fill="{BG}"/>']

    # (a) small multiples
    s.append(f'<text x="{W/2}" y="60" font-family="{SERIF}" font-size="24" fill="{INK}" '
             f'text-anchor="middle">(a) Jagged capabilities: graduate-level science questions</text>')
    size = 180
    panels = [(n, sub, vals, RED, RED_FILL) for n, sub, vals in PEOPLE]
    panels.append((*BOT, BOT_C, BOT_FILL))
    for k, (name, sub, (v, m), stroke, fill) in enumerate(panels):
        cx = W / 2 + (k - (len(panels) - 1) / 2) * 280
        s.append(f'<text x="{cx}" y="112" font-family="{SERIF}" font-size="18" fill="{INK}" '
                 f'text-anchor="middle">{name}</text>')
        s.append(f'<text x="{cx}" y="136" font-family="{SANS}" font-size="13" fill="{MUTED}" '
                 f'text-anchor="middle">{sub}</text>')
        p = Plot(cx - size / 2, 160, size)
        s += p.frame(14, 18)
        s.append(p.rect(v, m, f'fill="{fill}" fill-opacity="0.55" stroke="{stroke}" stroke-width="2"'))
        s.append(p.dot(v, m, stroke, 4))
        s.append(p.label(v, m, f"{v:g}% / {m:g}%", 0, -10 if m < 85 else 22,
                         MUTED, size=11, anchor="end" if v > 60 else "start", family=SANS))

    # (b) organizational envelope
    s.append(f'<text x="{W/2}" y="445" font-family="{SERIF}" font-size="24" fill="{INK}" '
             f'text-anchor="middle">(b) Mosaic intelligence: organizational envelope</text>')
    size = 440
    p = Plot((W - size) / 2, 490, size)
    s += p.frame(18, 40, ticks=True)
    bv, bm = BOT[2]
    ov, om = OLD_BOT[2]
    s.append(p.rect(bv, bm, f'fill="{BOT_FILL}" fill-opacity="0.35" stroke="none"'))
    s.append(p.rect(*MOSAIC, f'fill="{RED_FILL}" fill-opacity="0.35" stroke="none"'))
    s.append(p.rect(*AVERAGE, f'fill="{LAV_FILL}" fill-opacity="0.8" stroke="none"'))
    for _, _, (v, m) in PEOPLE:
        s.append(p.rect(v, m, f'fill="none" stroke="{MUTED}" stroke-opacity="0.7" stroke-width="1.1"'))
    s.append(p.rect(*AVERAGE, f'fill="none" stroke="{LAV}" stroke-width="2.2" stroke-dasharray="5 4"'))
    s.append(p.rect(*MOSAIC, f'fill="none" stroke="{RED}" stroke-width="2.6"'))
    s.append(p.rect(ov, om, f'fill="none" stroke="{BOT_C}" stroke-width="1.8" stroke-dasharray="3 3"'))
    s.append(p.rect(bv, bm, f'fill="none" stroke="{BOT_C}" stroke-width="3"'))
    for name, _, (v, m) in PEOPLE:
        s.append(p.dot(v, m, MUTED, 3.5))
        s.append(p.label(v, m, name, 8, -8, MUTED, size=13))
    s.append(p.dot(*AVERAGE, "#a8a7d4", 4.5))
    s.append(p.dot(*MOSAIC, RED, 5.5))
    s.append(p.label(*MOSAIC, "Team", 8, -8, RED, size=14))
    s.append(p.dot(ov, om, BOT_C, 4))
    s.append(p.label(ov, om, f"{OLD_BOT[0]} ({OLD_BOT[1]})", 8, -6, BOT_C, size=13))
    s.append(p.dot(bv, bm, BOT_C, 6.5))
    s.append(p.label(bv, bm, f"{BOT[0]} (2026)", -10, 24, BOT_C, size=16, anchor="end"))

    # legend
    lx, ly = 470, 1030
    legend = [
        (f'stroke="{MUTED}" stroke-width="1.5"', "Individual experts (GPQA validators)"),
        (f'stroke="{LAV}" stroke-width="3" stroke-dasharray="6 4"', "Average intelligence (random assignment)"),
        (f'stroke="{RED}" stroke-width="3"', "Mosaic intelligence (comparative advantage)"),
        (f'stroke="{BOT_C}" stroke-width="3"', f"{BOT[0]} (2026)"),
        (f'stroke="{BOT_C}" stroke-width="1.8" stroke-dasharray="3 3"', f"{OLD_BOT[0]} ({OLD_BOT[1]})"),
    ]
    for j, (style, label) in enumerate(legend):
        y = ly + j * 26
        s.append(f'<line x1="{lx}" y1="{y}" x2="{lx + 36}" y2="{y}" {style}/>')
        s.append(f'<text x="{lx + 52}" y="{y + 5}" font-family="{SERIF}" font-size="15" '
                 f'fill="{INK}">{label}</text>')

    # sources
    notes = [
        "Humans and GPT-4: Rein et al. 2023, GPQA (arXiv:2311.12022), Fig. 2 and Sec. 4; extended set, experts with web access.",
        "Sonnet 4.6: GPQA Diamond per-domain scores (interfaze.ai, third-party), consistent with the 89.9% overall Anthropic reported.",
        "Accuracy on four-option multiple choice; rectangles start at chance (25%).",
    ]
    for j, line in enumerate(notes):
        s.append(f'<text x="{W/2}" y="{1200 + j * 18}" font-family="{SANS}" font-size="11.5" '
                 f'fill="{MUTED}" text-anchor="middle">{line}</text>')

    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    out = Path(__file__).with_suffix(".svg")
    out.write_text(build())
    print(f"wrote {out}")
