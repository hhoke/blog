"""Generate mosaic_triangle.svg: a 3-axis simplification of the
"jagged capabilities / mosaic intelligence" radar figure.

Run:  python3 figures/multi_level_selection_and_the_ai_economy/mosaic_triangle.py
"""
import math
from pathlib import Path

# ---- data -------------------------------------------------------------
AXES = ["Verbal", "Math", "Culture"]
PEOPLE = [
    ("Person 1", "Verbal+ / Math−",   [0.95, 0.25, 0.60]),
    ("Person 2", "Math+ / Culture−",  [0.45, 0.95, 0.20]),
    ("Person 3", "Culture+ / Verbal−", [0.20, 0.50, 0.95]),
]

# Mosaic: each task goes to whoever is best at it.
MOSAIC = [max(p[2][i] for p in PEOPLE) for i in range(len(AXES))]
# Average: tasks assigned without regard to skill -> mean capability per axis.
AVERAGE = [sum(p[2][i] for p in PEOPLE) / len(PEOPLE) for i in range(len(AXES))]

# ---- style ------------------------------------------------------------
BG = "#f8f8f7"
INK = "#2b2b2b"
MUTED = "#9a9a9a"
GRID = "#dcdcdc"
RED = "#d98a8a"
RED_FILL = "#e8b4b4"
LAV = "#b3b2df"
LAV_FILL = "#d4d3ee"
SERIF = "Georgia, 'Times New Roman', serif"
SANS = "'Helvetica Neue', Helvetica, Arial, sans-serif"

W, H = 900, 1080


def pt(cx, cy, r, i, v=1.0):
    """Point on axis i (axis 0 points straight up, clockwise)."""
    a = -math.pi / 2 + 2 * math.pi * i / len(AXES)
    return cx + r * v * math.cos(a), cy + r * v * math.sin(a)


def poly(cx, cy, r, vals):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in
                    (pt(cx, cy, r, i, v) for i, v in enumerate(vals)))


def smooth(cx, cy, r, vals, t=0.9):
    """Closed Catmull-Rom curve through the value points, as an SVG path."""
    P = [pt(cx, cy, r, i, v) for i, v in enumerate(vals)]
    n = len(P)
    d = [f"M{P[0][0]:.1f},{P[0][1]:.1f}"]
    for i in range(n):
        p0, p1, p2, p3 = P[i - 1], P[i], P[(i + 1) % n], P[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 6, p1[1] + (p2[1] - p0[1]) * t / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 6, p2[1] - (p3[1] - p1[1]) * t / 6)
        d.append(f"C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}")
    return " ".join(d) + "Z"


def grid(cx, cy, r, label_size, label_pad):
    out = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{GRID}" stroke-width="1.2"/>',
           f'<circle cx="{cx}" cy="{cy}" r="{r + 4}" fill="none" stroke="{GRID}" stroke-width="0.6"/>']
    for f in (0.33, 0.66):
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r * f:.1f}" fill="none" '
                   f'stroke="{GRID}" stroke-width="0.8" stroke-dasharray="2 3"/>')
    for i, name in enumerate(AXES):
        x, y = pt(cx, cy, r, i)
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" '
                   f'stroke="{GRID}" stroke-width="0.8"/>')
        lx, ly = pt(cx, cy, r + label_pad, i)
        if i == 0:
            ly -= 4
        else:
            ly += label_size * 0.9
        out.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-family="{SERIF}" '
                   f'font-size="{label_size}" fill="{INK}" text-anchor="middle">{name}</text>')
    return out


def dots(cx, cy, r, vals, color, rad):
    return [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rad}" fill="{color}"/>'
            for x, y in (pt(cx, cy, r, i, v) for i, v in enumerate(vals))]


def build():
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
         f'<rect width="{W}" height="{H}" fill="{BG}"/>']

    # (a) small multiples
    s.append(f'<text x="{W/2}" y="60" font-family="{SERIF}" font-size="24" fill="{INK}" '
             f'text-anchor="middle">(a) Jagged human capabilities across domains</text>')
    r_small, cy_small = 85, 285
    for k, (name, sub, vals) in enumerate(PEOPLE):
        cx = W / 2 + (k - 1) * 285
        s.append(f'<text x="{cx}" y="112" font-family="{SERIF}" font-size="18" fill="{INK}" '
                 f'text-anchor="middle">{name}</text>')
        s.append(f'<text x="{cx}" y="136" font-family="{SANS}" font-size="13" fill="{MUTED}" '
                 f'text-anchor="middle">{sub}</text>')
        s += grid(cx, cy_small, r_small, 14, 16)
        s.append(f'<polygon points="{poly(cx, cy_small, r_small, vals)}" fill="{RED_FILL}" '
                 f'fill-opacity="0.55" stroke="{RED}" stroke-width="2" stroke-linejoin="round"/>')
        s += dots(cx, cy_small, r_small, vals, RED, 3.5)

    # (b) organizational envelope
    s.append(f'<text x="{W/2}" y="445" font-family="{SERIF}" font-size="24" fill="{INK}" '
             f'text-anchor="middle">(b) Mosaic intelligence: organizational envelope</text>')
    cx, cy, r = W / 2, 735, 205
    s += grid(cx, cy, r, 19, 24)
    s.append(f'<polygon points="{poly(cx, cy, r, MOSAIC)}" fill="{RED_FILL}" fill-opacity="0.18" stroke="none"/>')
    s.append(f'<path d="{smooth(cx, cy, r, AVERAGE)}" fill="{LAV_FILL}" fill-opacity="0.7" stroke="none"/>')
    for _, _, vals in PEOPLE:
        s.append(f'<polygon points="{poly(cx, cy, r, vals)}" fill="none" stroke="{MUTED}" '
                 f'stroke-opacity="0.6" stroke-width="1.1" stroke-linejoin="round"/>')
    s.append(f'<path d="{smooth(cx, cy, r, AVERAGE)}" fill="none" stroke="{LAV}" '
             f'stroke-width="2.4" stroke-dasharray="7 5"/>')
    s += dots(cx, cy, r, AVERAGE, "#a8a7d4", 4.5)
    s.append(f'<polygon points="{poly(cx, cy, r, MOSAIC)}" fill="none" stroke="{RED}" '
             f'stroke-width="3" stroke-linejoin="round"/>')
    s += dots(cx, cy, r, MOSAIC, RED, 6)

    # legend
    lx, ly = 515, 990
    legend = [
        (f'stroke="{MUTED}" stroke-width="1.5"', f"Individual workers (i = 1, …, {len(PEOPLE)})"),
        (f'stroke="{LAV}" stroke-width="3" stroke-dasharray="6 4"', "Average intelligence (random pairing)"),
        (f'stroke="{RED}" stroke-width="3"', "Mosaic intelligence (comparative advantage)"),
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
