#!/usr/bin/env python3
"""Build a self-contained static gallery (docs/index.html) from the dediren package.

Reads the *model's own* sources — project.json (titles/questions/kind), the rendered
generated/svg/*.svg, and generated/render-metadata/*.json (node/edge counts) — and
emits one standalone HTML file with every diagram inlined. No external assets, so it
works on GitHub Pages, a static host, or opened straight from disk.

Usage:  python3 docs/build-gallery.py
"""
import json, os, re, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
PKG  = os.path.join(HERE, "architecture", "uljas.dediren")
SVG  = os.path.join(PKG, "generated", "svg")
RMETA= os.path.join(PKG, "generated", "render-metadata")
OUT  = os.path.join(HERE, "index.html")

# --- group definition: notation-coded plate sections ---
def group_of(view_id):
    if view_id.startswith("seq-"):  return ("seq",  "Sekvenssit",           "UML 2.5",      "S")
    if view_id.startswith("data-"): return ("data", "Tietomallit",          "UML 2.5",      "T")
    return                                 ("ctx",  "Konteksti & prosessit","ArchiMate 3.2","K")

# A view is flagged "dense" when it carries many relationships — edge routing, not
# node count, is what makes a diagram hard to read. This isolates the sprawling
# Tilityserittely model (92 edges) and recomputes correctly if the model changes.
DENSE_EDGES = 50

def count(path):
    d = json.load(open(path, encoding="utf-8"))
    return len(d.get("nodes", {})), len(d.get("edges", {}))

def main():
    proj = json.load(open(os.path.join(PKG, "project.json"), encoding="utf-8"))
    counters, data = {}, []
    for v in proj["views"]:
        vid = v["id"]
        key, gtitle, gnote, prefix = group_of(vid)
        counters[key] = counters.get(key, 0) + 1
        n, e = count(os.path.join(RMETA, vid + ".json"))
        data.append({
            "id": vid,
            "code": f"{prefix}{counters[key]}",
            "group": {"key": key, "title": gtitle, "note": gnote},
            "title": v.get("title", vid),
            "q": v.get("question", ""),
            "kind": v.get("diagramKind", ""),
            "nodes": n, "edges": e,
            "status": "warning" if e >= DENSE_EDGES else "ok",
        })

    plates = []
    for d in data:
        svg = open(os.path.join(SVG, d["id"] + ".svg"), encoding="utf-8").read().strip()
        plates.append(f'<template class="plate" data-id="{d["id"]}">{svg}</template>')
    plates_html = "\n".join(plates)

    favicon = "data:image/svg+xml," + quote(
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>"
        "<text y='.9em' font-size='88'>\U0001F4D0</text></svg>")

    html = (TEMPLATE
            .replace("__FAVICON__", favicon)
            .replace("__DATA__", json.dumps(data, ensure_ascii=False))
            .replace("__PLATES__", plates_html))
    open(OUT, "w", encoding="utf-8").write(html)
    kb = os.path.getsize(OUT) / 1024
    print(f"wrote {OUT}  ({kb:.0f} KB, {len(data)} plates)")

# ---------------------------------------------------------------- template ----
TEMPLATE = r"""<!doctype html>
<html lang="fi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Uljas · rajapinnan arkkitehtuurikuvasto</title>
<link rel="icon" href="__FAVICON__">
<style>
:root{
  --paper:#f1f0ea; --panel:#ffffff; --rail:#f7f6f1; --ink:#1b1a16; --muted:#6b675e; --faint:#9b978b;
  --line:#ddd9cf; --line-2:#c9c4b6; --accent:#4b45c4; --accent-ink:#3a34a6; --wash:#ecebfb;
  --sheet:#ffffff; --sheet-line:#e7e3d8; --ok:#2f6b45; --ok-wash:#e6f1ea; --warn:#8a5a12; --warn-wash:#f6ead0;
  --sans:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,"SF Mono",SFMono-Regular,"JetBrains Mono",Menlo,Consolas,monospace;
  --shadow:0 1px 0 rgba(27,26,22,.03),0 18px 40px -26px rgba(27,26,22,.42);
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --paper:#131419; --panel:#1b1d25; --rail:#171922; --ink:#e9e7df; --muted:#9c988e; --faint:#6f6c63;
  --line:#282b34; --line-2:#3a3e49; --accent:#9b96f6; --accent-ink:#b9b5fb; --wash:#22233a;
  --sheet:#ffffff; --sheet-line:#d8d4cb; --ok:#7ad3a0; --ok-wash:#123123; --warn:#e7c17c; --warn-wash:#332913;
  --shadow:0 1px 0 rgba(0,0,0,.4),0 20px 46px -26px rgba(0,0,0,.7);
}}
:root[data-theme="dark"]{
  --paper:#131419; --panel:#1b1d25; --rail:#171922; --ink:#e9e7df; --muted:#9c988e; --faint:#6f6c63;
  --line:#282b34; --line-2:#3a3e49; --accent:#9b96f6; --accent-ink:#b9b5fb; --wash:#22233a;
  --sheet:#ffffff; --sheet-line:#d8d4cb; --ok:#7ad3a0; --ok-wash:#123123; --warn:#e7c17c; --warn-wash:#332913;
  --shadow:0 1px 0 rgba(0,0,0,.4),0 20px 46px -26px rgba(0,0,0,.7);
}
*{box-sizing:border-box}
html,body{margin:0;height:100%}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);line-height:1.5;-webkit-font-smoothing:antialiased}
.mono{font-family:var(--mono)}
#app{display:grid;grid-template-columns:304px minmax(0,1fr);height:100vh;overflow:hidden}

/* ---------- register rail ---------- */
#rail{background:var(--rail);border-right:1px solid var(--line);display:flex;flex-direction:column;min-height:0}
.mast{padding:22px 20px 16px;border-bottom:1px solid var(--line)}
.mast-eyebrow{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent-ink)}
.mast-title{margin:11px 0 0;font-size:20px;line-height:1.18;font-weight:640;letter-spacing:-.02em;text-wrap:balance}
.mast-sub{margin:9px 0 0;font-family:var(--mono);font-size:11px;line-height:1.55;color:var(--muted);letter-spacing:.01em}
#register{flex:1;min-height:0;overflow-y:auto;padding:6px 10px 20px}
.reg-group{margin-top:15px}
.reg-head{display:flex;align-items:baseline;justify-content:space-between;padding:2px 8px 7px;border-bottom:1px solid var(--line);margin-bottom:5px}
.reg-title{font-family:var(--mono);font-size:10.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);font-weight:600}
.reg-note{font-family:var(--mono);font-size:10px;letter-spacing:.06em;color:var(--faint)}
.reg-item{display:grid;grid-template-columns:34px 1fr auto;align-items:center;gap:9px;width:100%;text-align:left;
  border:0;border-left:2px solid transparent;background:transparent;color:var(--ink);
  padding:7px 8px 7px 10px;border-radius:0 7px 7px 0;cursor:pointer;font-family:inherit}
.reg-item:hover{background:color-mix(in srgb,var(--accent) 7%,transparent)}
.reg-item[aria-selected="true"]{background:var(--panel);border-left-color:var(--accent);box-shadow:var(--shadow)}
.reg-code{font-family:var(--mono);font-size:12px;font-weight:600;color:var(--faint);font-variant-numeric:tabular-nums;letter-spacing:.02em}
.reg-item[aria-selected="true"] .reg-code{color:var(--accent-ink)}
.reg-label{font-size:12.5px;letter-spacing:-.005em;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.reg-item[aria-selected="true"] .reg-label{font-weight:600}
.reg-meta{font-family:var(--mono);font-size:9.5px;color:var(--faint);font-variant-numeric:tabular-nums}
.rail-foot{padding:9px 20px;border-top:1px solid var(--line);font-family:var(--mono);font-size:10px;color:var(--faint);
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}

/* ---------- stage ---------- */
#stage{display:flex;flex-direction:column;min-width:0;min-height:0}
#head{display:flex;gap:20px;align-items:flex-start;justify-content:space-between;padding:16px 24px 15px;
  border-bottom:1px solid var(--line);background:var(--panel)}
.head-plate{display:flex;gap:14px;min-width:0}
#p-code{font-family:var(--mono);font-size:27px;font-weight:600;line-height:1;letter-spacing:.01em;color:var(--accent-ink);
  padding-top:3px;font-variant-numeric:tabular-nums}
.head-main{min-width:0}
.eyebrow{display:flex;gap:7px;align-items:center;flex-wrap:wrap;margin-bottom:6px}
#p-title{margin:0;font-size:19px;font-weight:640;letter-spacing:-.02em;line-height:1.2;text-wrap:balance}
#p-q{margin:5px 0 0;font-size:13px;color:var(--muted);max-width:74ch}
.chip{display:inline-flex;align-items:center;font-family:var(--mono);font-size:10.5px;font-weight:600;letter-spacing:.03em;
  padding:3px 8px;border-radius:5px;white-space:nowrap}
.chip-kind{background:var(--wash);color:var(--accent-ink)}
.chip-ok{background:var(--ok-wash);color:var(--ok)}
.chip-warn{background:var(--warn-wash);color:var(--warn)}
.chip-count{background:transparent;border:1px solid var(--line-2);color:var(--muted);font-variant-numeric:tabular-nums}
.tools{display:flex;gap:9px;align-items:center;flex-shrink:0}
.zoom{display:inline-flex;border:1px solid var(--line-2);border-radius:8px;overflow:hidden;background:var(--panel)}
.zoom button{border:0;background:transparent;color:var(--ink);font-family:var(--mono);font-size:12px;font-weight:600;
  padding:7px 11px;cursor:pointer}
.zoom button+button{border-left:1px solid var(--line)}
.zoom button:hover{background:color-mix(in srgb,var(--accent) 10%,transparent)}
.iconbtn{border:1px solid var(--line-2);background:var(--panel);color:var(--ink);width:35px;height:34px;border-radius:8px;
  cursor:pointer;font-size:15px;line-height:1}
.iconbtn:hover{background:color-mix(in srgb,var(--accent) 10%,transparent)}

#viewer{flex:1;min-height:0;overflow:auto;padding:26px;display:flex;align-items:flex-start}
#sheet{background:var(--sheet);border:1px solid var(--sheet-line);border-radius:10px;box-shadow:var(--shadow);
  padding:20px;width:max-content;margin-inline:auto}
#sheet.swap{animation:swap .18s ease}
@keyframes swap{from{opacity:0;transform:translateY(5px)}to{opacity:1;transform:none}}
#plate-host{display:block}
#plate-host svg{display:block;height:auto;max-width:none}
#plate-host svg [data-arch-a11y="visible-title"]{display:none}  /* title lives in the chrome */
#foot{display:flex;gap:16px;align-items:center;padding:8px 24px;border-top:1px solid var(--line);
  background:var(--panel);font-family:var(--mono);font-size:11px;color:var(--faint)}
#p-note{color:var(--warn)}

:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:3px}

@media (max-width:900px){
  #app{grid-template-columns:1fr;grid-template-rows:auto minmax(0,1fr)}
  #rail{border-right:0;border-bottom:1px solid var(--line);max-height:40vh}
  #p-code{font-size:22px}
}
@media (prefers-reduced-motion:reduce){#sheet.swap{animation:none}}
</style>
</head>
<body>
<div id="app">
  <aside id="rail">
    <div class="mast">
      <div class="mast-eyebrow">Ulosottolaitos · Uljas</div>
      <h1 class="mast-title">Rajapinnan arkkitehtuurikuvasto</h1>
      <p class="mast-sub">Tietojärjestelmähakijan sanomarajapinta<br>24 levyä · ArchiMate 3.2 + UML 2.5</p>
    </div>
    <nav id="register" aria-label="Näkymät" role="tablist"></nav>
    <div class="rail-foot">docs/architecture/uljas.dediren</div>
  </aside>
  <main id="stage">
    <header id="head">
      <div class="head-plate">
        <div id="p-code" aria-hidden="true"></div>
        <div class="head-main">
          <div class="eyebrow">
            <span id="p-kind" class="chip chip-kind"></span>
            <span id="p-status" class="chip"></span>
            <span id="p-count" class="chip chip-count"></span>
          </div>
          <h2 id="p-title"></h2>
          <p id="p-q"></p>
        </div>
      </div>
      <div class="tools">
        <div class="zoom" role="group" aria-label="Zoomaus">
          <button id="zout" title="Loitonna" aria-label="Loitonna">–</button>
          <button id="zfit" title="Sovita leveyteen">Sovita</button>
          <button id="zin" title="Lähennä" aria-label="Lähennä">+</button>
        </div>
        <button id="theme" class="iconbtn" title="Vaihda vaalea/tumma" aria-label="Vaihda teema">◐</button>
      </div>
    </header>
    <div id="viewer"><div id="sheet"><div id="plate-host"></div></div></div>
    <footer id="foot"><span id="p-path"></span><span id="p-note"></span></footer>
  </main>
</div>

<div hidden>__PLATES__</div>

<script>
"use strict";
const DATA = __DATA__;
const byId = Object.fromEntries(DATA.map(d => [d.id, d]));
const q = s => document.querySelector(s);
const esc = s => s.replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
let current = null, zoom = 100;

// build the register from the data
(function buildRegister(){
  const groups = [];
  for (const d of DATA){
    let g = groups.find(x => x.key === d.group.key);
    if (!g){ g = {key:d.group.key, title:d.group.title, note:d.group.note, items:[]}; groups.push(g); }
    g.items.push(d);
  }
  q('#register').innerHTML = groups.map(g => `
    <section class="reg-group">
      <header class="reg-head"><span class="reg-title">${esc(g.title)}</span><span class="reg-note">${esc(g.note)} · ${g.items.length}</span></header>
      ${g.items.map(d => `
        <button class="reg-item" role="tab" data-id="${d.id}" aria-selected="false" title="${esc(d.title)}">
          <span class="reg-code">${d.code}</span>
          <span class="reg-label">${esc(d.title)}</span>
          <span class="reg-meta">${d.nodes}·${d.edges}</span>
        </button>`).join('')}
    </section>`).join('');
})();

const viewer = q('#viewer'), sheet = q('#sheet');
// Available content width inside the sheet at 100% ("fit to width"). Zoom scales
// off this so the diagram is sized in real pixels — the sheet then shrink-wraps it
// (width:max-content) and grows past the viewport, keeping the rounded card intact.
function availWidth(){
  const vs = getComputedStyle(viewer), ss = getComputedStyle(sheet);
  const inner  = viewer.clientWidth - parseFloat(vs.paddingLeft) - parseFloat(vs.paddingRight);
  const chrome = parseFloat(ss.paddingLeft) + parseFloat(ss.paddingRight)
               + parseFloat(ss.borderLeftWidth) + parseFloat(ss.borderRightWidth);
  return Math.max(0, inner - chrome);
}
function applyZoom(){ const s = q('#plate-host svg'); if (s) s.style.width = Math.round(availWidth() * zoom / 100) + 'px'; }
function setZoom(z){ zoom = Math.max(25, Math.min(400, z)); applyZoom(); }

function select(id){
  const d = byId[id]; if (!d) return;
  current = id;
  document.querySelectorAll('.reg-item').forEach(b => b.setAttribute('aria-selected', String(b.dataset.id === id)));
  const tpl = document.querySelector(`template.plate[data-id="${id}"]`);
  q('#plate-host').replaceChildren(tpl ? tpl.content.cloneNode(true) : document.createTextNode(''));
  q('#p-code').textContent  = d.code;
  q('#p-kind').textContent  = d.kind;
  q('#p-title').textContent = d.title;
  q('#p-q').textContent     = d.q;
  const st = q('#p-status');
  st.textContent = d.status === 'warning' ? 'tiheä asettelu' : 'asettelu ok';
  st.className = 'chip ' + (d.status === 'warning' ? 'chip-warn' : 'chip-ok');
  q('#p-count').textContent = `${d.nodes} solmua · ${d.edges} yhteyttä`;
  q('#p-path').textContent  = `generated/svg/${d.id}.svg`;
  q('#p-note').textContent  = d.status === 'warning' ? 'tiheä kaavio — zoomaa yksityiskohtiin' : '';
  zoom = 100; applyZoom();
  if (location.hash.slice(1) !== id) history.replaceState(null, '', '#' + id);
  const sheet = q('#sheet'); sheet.classList.remove('swap'); void sheet.offsetWidth; sheet.classList.add('swap');
  document.querySelector(`.reg-item[data-id="${id}"]`)?.scrollIntoView({block:'nearest'});
}

document.querySelectorAll('.reg-item').forEach(b => b.addEventListener('click', () => select(b.dataset.id)));
q('#zin').onclick  = () => setZoom(zoom + 25);
q('#zout').onclick = () => setZoom(zoom - 25);
q('#zfit').onclick = () => setZoom(100);
addEventListener('resize', applyZoom);  // keep "fit" honest when the window changes

q('#register').addEventListener('keydown', e => {
  if (e.key !== 'ArrowDown' && e.key !== 'ArrowUp') return;
  e.preventDefault();
  const ids = DATA.map(d => d.id), i = ids.indexOf(current);
  const next = e.key === 'ArrowDown' ? Math.min(ids.length - 1, i + 1) : Math.max(0, i - 1);
  select(ids[next]);
  document.querySelector(`.reg-item[data-id="${ids[next]}"]`)?.focus();
});

const root = document.documentElement;
q('#theme').onclick = () => {
  const cur = root.getAttribute('data-theme') || (matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light');
  root.setAttribute('data-theme', cur === 'dark' ? 'light' : 'dark');
};

addEventListener('hashchange', () => {
  const id = location.hash.slice(1);
  if (byId[id] && id !== current) select(id);
});

const start = byId[location.hash.slice(1)] ? location.hash.slice(1) : DATA[0].id;
select(start);
</script>
</body>
</html>
"""

if __name__ == "__main__":
    sys.exit(main())
