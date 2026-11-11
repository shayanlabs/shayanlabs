"""Draws assets/road.svg, the profile's ladder (the syllabus chapters).

To update it: change a station's status below, then run
    python3 tools/road.py
Statuses: shipped · building · next · planned
"""
from pathlib import Path

STATIONS = [
    # (number, title, one line, status, icon)
    ("01", "PYTHON", "lists, functions, files, OOP", "building", "python"),
    ("02", "DEV TOOLS", "git, terminal, AI coding tools", "next", "git"),
    ("03", "MATHS FOR ML", "algebra, calculus, statistics", "planned", "maths"),
    ("04", "DATA", "NumPy, pandas, charts, SQL", "planned", "data"),
]
THEN = "then → classical ML · neural nets · deep learning · LLMs &amp; agents"

W, H, Y = 1200, 340, 158
MINT, AMBER, BLUE = "#5eead4", "#f5b544", "#5b8cff"
LOOK = {  # status -> (colour, pill text, pill fill)
    "shipped": (MINT, "SHIPPED", "#0d2a26"),
    "building": (AMBER, "ON THE BENCH", "#2a210c"),
    "next": (BLUE, "NEXT", "#0f1a2c"),
    "planned": (BLUE, "PLANNED", "#0f1a2c"),
}


def icon(kind, x, y, c):
    if kind == "python":
        return (f'<path d="M{x-24} {y-12} L{x-10} {y} L{x-24} {y+12}" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<path d="M{x-2} {y+13} H{x+22}" stroke="{c}" stroke-width="3" stroke-linecap="round" class="blink"/>')
    if kind == "git":
        return (f'<path d="M{x-12} {y-20} V{y+20} M{x-12} {y-2} C{x-12} {y-14} {x+14} {y-10} {x+14} {y-20}" fill="none" stroke="{c}" stroke-width="2.4"/>'
                + "".join(f'<circle cx="{a}" cy="{b}" r="5.5" fill="#0a0f1a" stroke="{c}" stroke-width="2.4"/>' for a, b in [(x-12, y-20), (x-12, y+20), (x+14, y-20)]))
    if kind == "maths":
        return (f'<text x="{x}" y="{y+13}" text-anchor="middle" class="sans" font-size="38" font-weight="700" fill="{c}">∑</text>')
    return "".join(f'<rect x="{x-22+i*12}" y="{y+18-h}" width="8" height="{h}" rx="2" fill="{c}" opacity="{0.5+i*0.15:.2f}"/>' for i, h in enumerate([14, 26, 20, 34]))


def build():
    n = len(STATIONS)
    xs = [int(W / (n + 1) * (i + 1)) for i in range(n)]
    body = '<text x="48" y="40" class="mono" font-size="16" fill="#5b8cff">02 // THE LADDER</text>'
    for i in range(n - 1):  # the track between stations
        a, b = STATIONS[i][3], STATIONS[i + 1][3]
        d = f'M{xs[i]+52} {Y} H{xs[i+1]-52}'
        if a == "shipped" and b == "shipped":
            body += f'<path d="{d}" stroke="{MINT}" stroke-width="2.4"/>'
        elif b == "building" or a == "building":
            body += f'<path d="{d}" stroke="{AMBER}" stroke-width="2.4" class="flow"/>'
        else:
            body += f'<path d="{d}" stroke="#2a4470" stroke-width="2" stroke-dasharray="3 7"/>'
    for x, (num, title, line, status, kind) in zip(xs, STATIONS):
        c, pill, pill_bg = LOOK[status]
        if status == "building":
            body += (f'<circle cx="{x}" cy="{Y}" r="46" fill="{AMBER}" opacity=".18" filter="url(#blur)"/>'
                     f'<circle cx="{x}" cy="{Y}" r="46" fill="none" stroke="{AMBER}" stroke-opacity=".5" stroke-width="2" class="ring"/>'
                     f'<circle cx="{x}" cy="{Y}" r="46" fill="#0f1828" stroke="{AMBER}" stroke-width="2.6" stroke-dasharray="10 6" class="spin"/>')
        elif status == "shipped":
            body += (f'<circle cx="{x}" cy="{Y}" r="46" fill="{MINT}" opacity=".14" filter="url(#blur)"/>'
                     f'<circle cx="{x}" cy="{Y}" r="46" fill="#0c1d1f" stroke="{MINT}" stroke-width="2.6"/>')
        else:
            body += f'<circle cx="{x}" cy="{Y}" r="46" fill="#0b1322" stroke="#3a5f9e" stroke-width="1.6" stroke-dasharray="2 5"/>'
        body += icon(kind, x, Y, c)
        bright = status in ("shipped", "building")
        body += f'<text x="{x}" y="{Y+82}" text-anchor="middle" class="mono" font-size="13" fill="#6f84a6">{num}</text>'
        body += f'<text x="{x}" y="{Y+108}" text-anchor="middle" class="sans" font-size="21" font-weight="800" fill="{"#eef3fb" if bright else "#a9bad6"}">{title}</text>'
        body += f'<text x="{x}" y="{Y+134}" text-anchor="middle" class="sans" font-size="15" fill="#8193b0">{line}</text>'
        w = len(pill) * 8.6 + 24
        body += (f'<rect x="{x-w/2:.0f}" y="{Y-88}" width="{w:.0f}" height="24" rx="12" fill="{pill_bg}" stroke="{c}" stroke-opacity="{1 if bright else .5}"/>'
                 f'<text x="{x}" y="{Y-71}" text-anchor="middle" class="mono" font-size="12.5" fill="{c}">{pill}</text>')
    body += f'''<g class="mono" font-size="13" fill="#6f84a6"><circle cx="880" cy="314" r="6" fill="{MINT}"/><text x="892" y="319">shipped</text>
<circle cx="976" cy="314" r="6" fill="none" stroke="{AMBER}" stroke-width="2" stroke-dasharray="3 2"/><text x="988" y="319">building</text>
<circle cx="1074" cy="314" r="6" fill="none" stroke="#3a5f9e" stroke-width="1.5" stroke-dasharray="1.5 2.5"/><text x="1086" y="319">planned</text></g>'''
    body += f'<text x="48" y="319" class="mono" font-size="13" fill="#6f84a6">{THEN}</text>'
    alt = "The ladder: " + ", ".join(f"{s[0]} {s[1].title()} {s[3]}" for s in STATIONS)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{alt}">
<defs>
<pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#14233b" stroke-width="1"/></pattern>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>
<clipPath id="card"><rect width="{W}" height="{H}" rx="20"/></clipPath>
</defs>
<style>
.mono{{font-family:ui-monospace,"SF Mono",Menlo,Consolas,"DejaVu Sans Mono",monospace}}
.sans{{font-family:"Segoe UI",Inter,"Helvetica Neue",Arial,"DejaVu Sans",sans-serif}}
.flow{{stroke-dasharray:8 8;animation:flow 1s linear infinite}}
@keyframes flow{{to{{stroke-dashoffset:-16}}}}
.ring{{transform-box:fill-box;transform-origin:center;animation:ring 2.4s ease-out infinite}}
@keyframes ring{{0%{{transform:scale(1);opacity:.8}}100%{{transform:scale(1.35);opacity:0}}}}
.spin{{transform-box:fill-box;transform-origin:center;animation:spin 12s linear infinite}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
.blink{{animation:blink 1.1s steps(1) infinite}}
@keyframes blink{{0%{{opacity:1}}50%,100%{{opacity:0}}}}
</style>
<g clip-path="url(#card)"><rect width="{W}" height="{H}" fill="#0a0f1a"/><rect width="{W}" height="{H}" fill="url(#grid)"/>
{body}
</g><rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="20" fill="none" stroke="#1f3355"/></svg>'''


if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "assets" / "road.svg"
    out.write_text(build())
    print(f"wrote {out}")
