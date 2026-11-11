"""Draws assets/banner.svg and assets/bench.svg for the profile.

To update the bench: change BENCH below (project, stage), then run
    python3 tools/cards.py
Stages, in order: SPEC · AI DRAFT · EXPLAIN · PREDICT · RUN · MODIFY · BUG HUNT · MAKE
"""
from pathlib import Path

LADDER = ["Python", "Dev tools", "Maths for ML", "Data", "Classical ML", "Neural nets", "LLMs &amp; agents"]
CURRENT_RUNG = 0  # index into LADDER

BENCH = {
    "number": "01",
    "title": "Match Scorecard",
    "line": "A cricket scorecard, typed ball by ball.",
    "stage": "SPEC",
    "now": "writing the spec",
}
STAGES = ["SPEC", "AI DRAFT", "EXPLAIN", "PREDICT", "RUN", "MODIFY", "BUG HUNT", "MAKE"]

MINT, AMBER, BLUE = "#5eead4", "#f5b544", "#5b8cff"
FONTS = """.mono{font-family:ui-monospace,"SF Mono",Menlo,Consolas,"DejaVu Sans Mono",monospace}
.sans{font-family:"Segoe UI",Inter,"Helvetica Neue",Arial,"DejaVu Sans",sans-serif}"""


def frame(w, h, alt, style, body, extra_defs=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{alt}">
<defs>
<pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#14233b" stroke-width="1"/></pattern>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>
<clipPath id="card"><rect width="{w}" height="{h}" rx="20"/></clipPath>{extra_defs}
</defs>
<style>{FONTS}
{style}</style>
<g clip-path="url(#card)"><rect width="{w}" height="{h}" fill="#0a0f1a"/><rect width="{w}" height="{h}" fill="url(#grid)"/>
{body}
</g><rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="20" fill="none" stroke="#1f3355"/></svg>'''


def chips(items, x, y, cls="chip"):
    out = []
    for t in items:
        w = len(t) * 9.1 + 30
        out.append(f'<rect x="{x}" y="{y}" width="{w:.0f}" height="32" rx="16" fill="#0f1a2c" stroke="#263e66"/>'
                   f'<text x="{x+15}" y="{y+21}" class="mono" font-size="15" fill="#b9c7de">{t}</text>')
        x += w + 10
    return "".join(out)


def banner():
    W, H = 1200, 360
    body = '''<rect width="1200" height="360" fill="url(#glow)"/>
<rect width="1200" height="44" fill="#0d1524"/><line x1="0" y1="44" x2="1200" y2="44" stroke="#1c2d49"/>
<circle cx="26" cy="22" r="6" fill="#ff5f57"/><circle cx="46" cy="22" r="6" fill="#febc2e"/><circle cx="66" cy="22" r="6" fill="#28c840"/>
<text x="92" y="27" class="mono" font-size="14" fill="#6f84a6">shayanlabs@lab: ~/python-projects — python3 learn.py</text>
<circle cx="1052" cy="22" r="5" fill="#5eead4" class="live"/><text x="1064" y="27" class="mono" font-size="14" fill="#5eead4">climbing</text>
<text x="58" y="104" class="mono" font-size="16" fill="#5b8cff">// builder log · python first, then up the ladder</text>
<text x="54" y="182" class="sans" font-size="80" font-weight="900" letter-spacing="1" fill="url(#name)">SHAYAN UMER</text>
<text x="58" y="226" class="mono" font-size="20" fill="#d7e0ee">AI writes the first draft.</text>
<text x="58" y="256" class="mono" font-size="20" fill="#d7e0ee">I read it, break it, and make it mine.<tspan class="cur" fill="#5eead4">▌</tspan></text>
''' + chips(["spec it", "read it", "break it", "make it"], 58, 290)
    # the ladder
    x0, x1, base, gap = 790, 1130, 316, 36
    n = len(LADDER)
    top = base - (n - 1) * gap
    body += (f'<path d="M{x0} {base+24} V{top-26} M{x1} {base+24} V{top-26}" stroke="#1f3355" stroke-width="3"/>'
             f'<path d="M{x0} {base+24} V{top-26} M{x1} {base+24} V{top-26}" stroke="{AMBER}" stroke-width="3" class="climb" pathLength="100"/>')
    for i, name in enumerate(LADDER):
        y = base - i * gap
        if i == CURRENT_RUNG:
            body += (f'<rect x="{x0+8}" y="{y-14}" width="{x1-x0-16}" height="28" rx="8" fill="{AMBER}" opacity=".25" filter="url(#blur)" class="breathe"/>'
                     f'<rect x="{x0+8}" y="{y-14}" width="{x1-x0-16}" height="28" rx="8" fill="#2a210c" stroke="{AMBER}" stroke-width="2"/>'
                     f'<text x="{x0+24}" y="{y+5}" class="mono" font-size="14" fill="{AMBER}">0{i+1}  {name}</text>'
                     f'<text x="{x1-24}" y="{y+5}" text-anchor="end" class="mono" font-size="12" fill="{AMBER}">◀ HERE</text>')
        else:
            op = max(0.28, 1 - i * 0.12)
            body += (f'<g opacity="{op:.2f}"><rect x="{x0+8}" y="{y-14}" width="{x1-x0-16}" height="28" rx="8" fill="#0b1322" stroke="#3a5f9e" stroke-dasharray="2 4"/>'
                     f'<text x="{x0+24}" y="{y+5}" class="mono" font-size="14" fill="#a9bad6">0{i+1}  {name}</text></g>')
    style = '''.cur{animation:blink 1.1s steps(1) infinite}@keyframes blink{0%{opacity:1}50%,100%{opacity:0}}
.live{animation:live 1.6s ease-in-out infinite}@keyframes live{0%,100%{opacity:1}50%{opacity:.25}}
.breathe{animation:breathe 2.4s ease-in-out infinite}@keyframes breathe{0%,100%{opacity:.15}50%{opacity:.45}}
.climb{fill:none;stroke-dasharray:6 100;animation:climb 3.5s linear infinite}
@keyframes climb{0%{stroke-dashoffset:6;opacity:0}10%{opacity:1}80%{opacity:.8}100%{stroke-dashoffset:-100;opacity:0}}'''
    defs = '''
<linearGradient id="name" x1="0" x2="1"><stop offset="0" stop-color="#eef3fb"/><stop offset="1" stop-color="#8fb0ff"/></linearGradient>
<radialGradient id="glow" cx="80%" cy="70%" r="45%"><stop offset="0" stop-color="#3a2a0a" stop-opacity=".55"/><stop offset="1" stop-color="#0a0f1a" stop-opacity="0"/></radialGradient>'''
    return frame(W, H, "Shayan Umer: AI writes the first draft, I read it, break it, and make it mine. Python first, then up the ladder.", style, body, defs)


def bench():
    W, H = 1200, 410
    b = BENCH
    body = (f'<text x="48" y="64" class="mono" font-size="16" fill="{AMBER}">{b["number"]} // ACTIVE BENCH</text>'
            f'<text x="46" y="118" class="sans" font-size="46" font-weight="900" fill="#eef3fb">{b["title"]}</text>'
            f'<text x="48" y="154" class="sans" font-size="20" fill="#b9c7de">{b["line"]}</text>'
            f'<text x="48" y="200" class="mono" font-size="13" fill="#6f84a6">THE PIPELINE · AI drafts, I do the understanding</text>')
    cur = STAGES.index(b["stage"])
    x, y = 48, 216
    for i, st in enumerate(STAGES):
        if i == 4:
            x, y = 48, 270
        w = len(st) * 9.4 + 30
        if i < cur:
            fill, stroke, txt = "#0c1d1f", MINT, MINT
        elif i == cur:
            fill, stroke, txt = "#2a210c", AMBER, AMBER
        else:
            fill, stroke, txt = "#0b1322", "#2c4672", "#7d8fae"
        if i == cur:
            body += f'<rect x="{x}" y="{y}" width="{w:.0f}" height="34" rx="17" fill="{AMBER}" opacity=".3" filter="url(#blur)" class="breathe"/>'
        body += (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="34" rx="17" fill="{fill}" stroke="{stroke}" stroke-width="{2 if i == cur else 1.2}"/>'
                 f'<text x="{x+15}" y="{y+22}" class="mono" font-size="14" fill="{txt}">{"✓ " if i < cur else ""}{st}</text>')
        if i not in (3, 7):
            body += f'<text x="{x+w+6:.0f}" y="{y+22}" class="mono" font-size="14" fill="#3a5f9e">→</text>'
        x += w + 26
    body += (f'<text x="48" y="352" class="mono" font-size="14" fill="#6f84a6">now ▸ <tspan fill="{AMBER}">{b["now"]}</tspan>'
             f'  ·  next ▸ <tspan fill="#a9bad6">{STAGES[min(cur+1, len(STAGES)-1)].lower()}</tspan></text>'
             f'<text x="48" y="380" class="mono" font-size="13" fill="#4f6385">rule ▸ AI never debugs for me · nothing ships that I can\'t explain</text>')
    # scoreboard
    px, py, pw, ph = 690, 48, 470, 300
    body += (f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="14" fill="#0b1322" stroke="#22385c"/>'
             f'<text x="{px+22}" y="{py+34}" class="mono" font-size="13" fill="#6f84a6">🏏 SCORECARD · target 20 · 2 overs</text>')
    overs = [[1, 4, 0, 2, 1, 1], [6, 4, 0, 1, 2, 1]]
    lines = ["9 runs · Total 9 · 🎯 Need 11", "14 runs · Total 23 · ✅ Chased"]
    css = []
    t, step = 4, 6.2  # percent of the 14s loop
    k = 0
    for o, balls in enumerate(overs):
        oy = py + 82 + o * 96
        body += f'<text x="{px+22}" y="{oy+6}" class="mono" font-size="14" fill="#a9bad6">OVER {o+1}</text>'
        for j, r in enumerate(balls):
            cx = px + 128 + j * 52
            col = MINT if r == 6 else AMBER if r == 4 else "#e8eef9"
            ring = MINT if r == 6 else AMBER if r == 4 else "#3a5f9e"
            body += f'<circle cx="{cx}" cy="{oy}" r="19" fill="none" stroke="#1f3355" stroke-dasharray="3 3"/>'
            body += (f'<g class="b{k}"><circle cx="{cx}" cy="{oy}" r="19" fill="#0f1a2c" stroke="{ring}" stroke-width="2"/>'
                     f'<text x="{cx}" y="{oy+6}" text-anchor="middle" class="mono" font-size="17" font-weight="700" fill="{col}">{r}</text></g>')
            css.append(f'.b{k}{{opacity:0;animation:b{k} 14s infinite}}@keyframes b{k}{{0%,{t:.1f}%{{opacity:0}}{t+1.5:.1f}%,92%{{opacity:1}}96%,100%{{opacity:0}}}}')
            t += step
            k += 1
        body += f'<text x="{px+128}" y="{oy+50}" class="mono s{o}" font-size="15" fill="{MINT if o else "#d7e0ee"}">📋 {lines[o]}</text>'
        css.append(f'.s{o}{{opacity:0;animation:s{o} 14s infinite}}@keyframes s{o}{{0%,{t-step+2:.1f}%{{opacity:0}}{t-step+4:.1f}%,92%{{opacity:1}}96%,100%{{opacity:0}}}}')
    body += f'<text x="{px+pw}" y="{py+ph+28}" text-anchor="end" class="mono" font-size="12" fill="#4f6385">▲ the target behaviour · ships when it runs</text>'
    style = '''.breathe{animation:breathe 2.4s ease-in-out infinite}@keyframes breathe{0%,100%{opacity:.15}50%{opacity:.5}}
''' + "\n".join(css)
    return frame(W, H, f'Active bench: project {b["number"]} {b["title"]}, at the {b["stage"]} stage of the pipeline', style, body)


if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "assets"
    (out / "banner.svg").write_text(banner())
    (out / "bench.svg").write_text(bench())
    print("wrote banner.svg and bench.svg")
