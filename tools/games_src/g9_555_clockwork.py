# -*- coding: utf-8 -*-
"""SEASON 2 · ZONE 9 — 555 CLOCKWORK : โรงนาฬิกา 555
GNR2022 อิเล็กทรอนิกส์พื้นฐาน ภาค 1/2569 · เนื้อหาหลังกลางภาค (ต่อยอดวงจร RC ของโซน 5)
datasheet TI NE555: VCC 4.5–16 V · IO ±200 mA · THRES ≈ 2/3 VCC · TRIG ≈ 1/3 VCC · RESET active low ≈ 0.7 V
Monostable tw ≈ 1.1RC · Astable f ≈ 1.44/((RA+2RB)C), tH ≈ 0.693(RA+RB)C, tL ≈ 0.693 RB C
ไฟล์แยกส่วน: g9_parts/"""
import os
from cpe_common import *
from zone_parts import load
_rd, _P = load(os.path.dirname(os.path.abspath(__file__)), 'g9_parts')

THEME = {
    "PRIMARY_RGB": "234,179,8",   "PRIMARY_HEX": "#eab308",
    "SECOND_RGB":  "20,184,166",  "SECOND_HEX":  "#14b8a6",
    "GOLD_RGB":    "253,230,138", "GOLD_HEX":    "#fde68a",
    "GOLD2_RGB":   "254,243,199", "GOLD2_HEX":   "#fef3c7",
    "RED_RGB":     "251,113,133", "RED_HEX":     "#fb7185",
    "BG_RGB":      "17,13,6",     "BG_HEX":      "#110d06",
    "PANEL_RGB":   "38,30,14",
    "PANEL2_RGB":  "52,41,18",
    "BG2_HEX":     "#18120a",
    "INK_HEX":     "#211a0c",
    "TEXT_HEX":    "#fdf8ec",
    "MUTED_HEX":   "#cdbf9c",
    "MUTED2_HEX":  "#9c8e6c",
    "MUTED3_HEX":  "#86795a",
    "SECOND2_HEX": "#5eead4",
    "PRIM2_HEX":   "#facc15",
    "LIGHT_EMBER": "#a16207", "LIGHT_CORNER": "#0f766e", "LIGHT_GOLD": "#854d0e",
    "LIGHT_GOLD2": "#713f12", "LIGHT_RED": "#be123c",
}

EXTRA_CSS = LAB_CSS + """
.ledlamp{width:40px;height:40px;border-radius:50%;border:2px solid var(--line);background:rgba(var(--ink-panel-rgb),.8);transition:background .05s,box-shadow .05s;flex:none}
.ledlamp.on{background:var(--gold);box-shadow:0 0 22px var(--gold)}
.meas{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:6px;margin:8px 0}
.meas div{padding:8px 10px;border-radius:12px;border:1px solid var(--line);background:rgba(var(--panel-rgb),.55);font-family:var(--mono);font-size:.95rem}
.meas div b{display:block;font-family:var(--font);font-size:.72rem;color:var(--muted);font-weight:500}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin:6px 0}
.chips span{padding:3px 10px;border-radius:999px;border:1px solid var(--line);font-size:.78rem;color:var(--muted)}
.chips span.got{border-color:var(--corner);color:var(--text);background:var(--ember-dim)}
select.sel{font-family:var(--mono);font-size:.85rem;padding:7px 9px;border-radius:10px;border:1px solid var(--line);background:rgba(var(--panel-rgb),.8);color:var(--text)}
.chip555{display:block;width:min(340px,100%);margin:6px auto}
.chip555 .pin{cursor:pointer}
.chip555 .pin rect{fill:rgba(var(--panel-rgb),.9);stroke:var(--line);stroke-width:2;transition:.15s}
.chip555 .pin:hover rect{stroke:var(--ember)}
.chip555 .pin.ok rect{fill:var(--corner);stroke:var(--corner)}
.chip555 .pin.bad rect{fill:var(--red);stroke:var(--red)}
.chip555 text{font-family:var(--mono);fill:var(--text);font-size:13px;pointer-events:none}
.cap{height:10px;border-radius:6px;background:rgba(var(--ink-panel-rgb),.7);border:1px solid var(--line);overflow:hidden;margin:6px 0}
.cap i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--corner),var(--gold))}
"""

HERO = """<svg class="cityart" viewBox="0 0 480 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="หอนาฬิกาที่มีไอซี 555 เป็นหน้าปัดและคลื่นสี่เหลี่ยมรอบ ๆ">
  <defs><filter id="fG9"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
  <rect width="480" height="300" rx="18" fill="#110d06"/>
  <g filter="url(#fG9)" fill="none" stroke-linecap="round">
    <circle cx="240" cy="130" r="78" stroke="#eab308" stroke-width="5"/>
    <rect x="205" y="98" width="70" height="64" rx="8" stroke="#14b8a6" stroke-width="4"/>
    <path d="M190 108 h15 M190 122 h15 M190 136 h15 M190 150 h15 M275 108 h15 M275 122 h15 M275 136 h15 M275 150 h15" stroke="#14b8a6" stroke-width="3"/>
    <path d="M240 130 L240 72 M240 130 L280 150" stroke="#fde68a" stroke-width="3"/>
    <path d="M30 255 h40 v-30 h40 v30 h40 v-30 h40 v30 h40 v-30 h40 v30 h40 v-30 h40 v30 h40 v-30 h40" stroke="#eab308" stroke-width="3"/>
  </g>
  <text x="240" y="138" text-anchor="middle" font-family="monospace" font-size="20" font-weight="700" fill="#fde68a">555</text>
</svg>"""

ZONES = _rd('zones.html')
LAB_JS = _rd('labs.js')
LAB_WIRING = _rd('wiring.js')
INIT_EXTRA = _rd('init.js').strip()
exec(compile(_rd('bank.py'), 'g9_parts/bank.py', 'exec'))
