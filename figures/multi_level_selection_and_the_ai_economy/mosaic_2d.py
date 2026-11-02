"""Generate mosaic_2d.svg: a 2-dimension version of the mosaic figure.

With two axes a radar chart degenerates to a line, so each capability
profile is drawn as a rectangle from the origin to (verbal, math).
The mosaic envelope is the rectangle spanned by the best human score on
each axis; the average is the rectangle spanned by the mean human scores.
GrokBot is drawn on the same scale for comparison.

Shares colors/fonts with mosaic_triangle.py.
Run:  python3 figures/multi_level_selection_and_the_ai_economy/mosaic_2d.py
"""
from pathlib import Path

from mosaic_triangle import BG, INK, MUTED, GRID, RED, RED_FILL, LAV, LAV_FILL, SERIF, SANS

# ---- data -------------------------------------------------------------
X_AXIS, Y_AXIS = "Verbal", "Math"
PEOPLE = [
    ("Person 1", "Verbal+ / Math−", (0.90, 0.30)),
    ("Person 2", "Math+ / Verbal−", (0.30, 0.90)),
]
MOSAIC = tuple(max(p[2][i] for p in PEOPLE) for i in range(2))
AVERAGE = tuple(sum(p[2][i] for p in PEOPLE) / len(PEOPLE) for i in range(2))

BOT_MULT = 3
BOT = ("GrokBot", f"{BOT_MULT}× best human on both", tuple(BOT_MULT * v for v in MOSAIC))

VMAX = 3.0  # axis range shared by every panel

BOT_C = "#5a8f8c"
BOT_FILL = "#a9cdca"

W, H = 900, 1160


class Plot:
    """Square plot area: data in [0, VMAX] on both axes, origin bottom-left."""

    def __init__(self, left, top, size, vmax=VMAX):
        self.left, self.top, self.size, self.vmax = left, top, size, vmax
        self.bottom = top + size
        self.k = size / vmax

    def xy(self, v, m):
        return self.left + v * self.k, self.bottom - m * self.k

    def rect(self, v, m, attrs):
        x, y = self.xy(0, m)
        return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{v * self.k:.1f}" '
                f'height="{m * self.k:.1f}" {attrs}/>')

    def dot(self, v, m, color, r):
        x, y = self.xy(v, m)
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"/>'

    def frame(self, label_size, label_pad, ticks=False):
        L, T, S, B = self.left, self.top, self.size, self.bottom
        out = [f'<rect x="{L}" y="{T}" width="{S}" height="{S}" fill="none" '
               f'stroke="{GRID}" stroke-width="1.2"/>']
        for t in range(1, int(self.vmax)):
            d = t * self.k
            out.append(f'<line x1="{L + d:.1f}" y1="{T}" x2="{L + d:.1f}" y2="{B}" '
                       f'stroke="{GRID}" stroke-width="0.8" stroke-dasharray="2 3"/>')
            out.append(f'<line x1="{L}" y1="{B - d:.1f}" x2="{L + S}" y2="{B - d:.1f}" '
                       f'stroke="{GRID}" stroke-width="0.8" stroke-dasharray="2 3"/>')
        if ticks:
            for t in range(0, int(self.vmax) + 1):
                d = t * self.k
                out.append(f'<text x="{L + d:.1f}" y="{B + 16}" font-family="{SANS}" font-size="11" '
                           f'fill="{MUTED}" text-anchor="middle">{t}</text>')
                if t:
                    out.append(f'<text x="{L - 8}" y="{B - d + 4:.1f}" font-family="{SANS}" '
                               f'font-size="11" fill="{MUTED}" text-anchor="end">{t}</text>')
        # axes
        out.append(f'<line x1="{L}" y1="{B}" x2="{L + S}" y2="{B}" stroke="{MUTED}" stroke-width="1"/>')
        out.append(f'<line x1="{L}" y1="{B}" x2="{L}" y2="{T}" stroke="{MUTED}" stroke-width="1"/>')
        out.append(f'<text x="{L + S / 2}" y="{B + label_pad + label_size * 0.7:.1f}" '
                   f'font-family="{SERIF}" font-size="{label_size}" fill="{INK}" '
                   f'text-anchor="middle">{X_AXIS} →</text>')
        lx, ly = L - label_pad, T + S / 2
        out.append(f'<text x="{lx}" y="{ly}" font-family="{SERIF}" font-size="{label_size}" '
                   f'fill="{INK}" text-anchor="middle" transform="rotate(-90 {lx} {ly})">'
                   f'{Y_AXIS} →</text>')
        return out


def build():
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
         f'<rect width="{W}" height="{H}" fill="{BG}"/>']

    # (a) small multiples
    s.append(f'<text x="{W/2}" y="60" font-family="{SERIF}" font-size="24" fill="{INK}" '
             f'text-anchor="middle">(a) Jagged capabilities across domains</text>')
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

    # (b) organizational envelope
    s.append(f'<text x="{W/2}" y="445" font-family="{SERIF}" font-size="24" fill="{INK}" '
             f'text-anchor="middle">(b) Mosaic intelligence: organizational envelope</text>')
    size = 440
    p = Plot((W - size) / 2, 490, size)
    s += p.frame(19, 34, ticks=True)
    bv, bm = BOT[2]
    s.append(p.rect(bv, bm, f'fill="{BOT_FILL}" fill-opacity="0.35" stroke="none"'))
    s.append(p.rect(*MOSAIC, f'fill="{RED_FILL}" fill-opacity="0.35" stroke="none"'))
    s.append(p.rect(*AVERAGE, f'fill="{LAV_FILL}" fill-opacity="0.8" stroke="none"'))
    for _, _, (v, m) in PEOPLE:
        s.append(p.rect(v, m, f'fill="none" stroke="{MUTED}" stroke-opacity="0.7" stroke-width="1.1"'))
    s.append(p.rect(*AVERAGE, f'fill="none" stroke="{LAV}" stroke-width="2.2" stroke-dasharray="5 4"'))
    s.append(p.rect(*MOSAIC, f'fill="none" stroke="{RED}" stroke-width="2.6"'))
    s.append(p.rect(bv, bm, f'fill="none" stroke="{BOT_C}" stroke-width="3"'))
    for _, _, (v, m) in PEOPLE:
        s.append(p.dot(v, m, MUTED, 3.5))
    s.append(p.dot(*AVERAGE, "#a8a7d4", 4.5))
    s.append(p.dot(*MOSAIC, RED, 5.5))
    s.append(p.dot(bv, bm, BOT_C, 6.5))
    bx, by = p.xy(bv, bm)
    s.append(f'<text x="{bx - 10:.1f}" y="{by + 24:.1f}" font-family="{SERIF}" font-size="17" '
             f'fill="{BOT_C}" text-anchor="end">GrokBot</text>')

    # legend
    lx, ly = 500, 1040
    legend = [
        (f'stroke="{MUTED}" stroke-width="1.5"', f"Individual workers (i = 1, …, {len(PEOPLE)})"),
        (f'stroke="{LAV}" stroke-width="3" stroke-dasharray="6 4"', "Average intelligence (random pairing)"),
        (f'stroke="{RED}" stroke-width="3"', "Mosaic intelligence (comparative advantage)"),
        (f'stroke="{BOT_C}" stroke-width="3"', f"GrokBot ({BOT_MULT}× best human on each axis)"),
    ]
    for j, (style, label) in enumerate(legend):
        y = ly + j * 26
        s.append(f'<line x1="{lx}" y1="{y}" x2="{lx + 36}" y2="{y}" {style}/>')
        s.append(f'<text x="{lx + 52}" y="{y + 5}" font-family="{SERIF}" font-size="15" '
                 f'fill="{INK}">{label}</text>')

    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    out = Path(__file__).with_suffix(".svg")
    out.write_text(build())
    print(f"wrote {out}")
