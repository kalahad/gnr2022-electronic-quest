# -*- coding: utf-8 -*-
"""SEASON 2 · ZONE 8 — OP-AMP TOWER : หอคอยออปแอมป์
GNR2022 อิเล็กทรอนิกส์พื้นฐาน ภาค 1/2569 · เนื้อหาหลังกลางภาค (ต่อยอดโซน 2 และ 5)
อ้างอิง: เอกสารการสอน "วงจรออปแอมป์และการประยุกต์ใช้งานเซนเซอร์" (docx ในโฟลเดอร์ เครื่องมือ-Lab)
datasheet: uA741 (VIO ≤ 6 mV, SR ≈ 0.5 V/µs, Zi ≈ 2 MΩ, Zo ≈ 75 Ω) · LF351 (SR 13 V/µs typ, IIB 50 pA typ)
LM324 (ไฟเดี่ยว 3–32 V, GBW 1.2 MHz, SR 0.5 V/µs) · หัวข้อ integrator/differentiator/slew rate อยู่ใน Hard Mode
ไฟล์แยกส่วน: g8_parts/"""
import os
from cpe_common import *
from zone_parts import load
_rd, _P = load(os.path.dirname(os.path.abspath(__file__)), 'g8_parts')

THEME = {
    "PRIMARY_RGB": "139,123,255", "PRIMARY_HEX": "#8b7bff",
    "SECOND_RGB":  "255,138,31",  "SECOND_HEX":  "#ff8a1f",
    "GOLD_RGB":    "255,225,77",  "GOLD_HEX":    "#ffe14d",
    "GOLD2_RGB":   "255,240,170", "GOLD2_HEX":   "#fff0aa",
    "RED_RGB":     "251,113,133", "RED_HEX":     "#fb7185",
    "BG_RGB":      "10,8,28",     "BG_HEX":      "#0a081c",
    "PANEL_RGB":   "24,20,58",
    "PANEL2_RGB":  "34,28,78",
    "BG2_HEX":     "#0f0c28",
    "INK_HEX":     "#16123a",
    "TEXT_HEX":    "#efecff",
    "MUTED_HEX":   "#aca6d8",
    "MUTED2_HEX":  "#7d76aa",
    "MUTED3_HEX":  "#68629a",
    "SECOND2_HEX": "#ffb366",
    "PRIM2_HEX":   "#b8adff",
    "LIGHT_EMBER": "#5b45e0", "LIGHT_CORNER": "#c2410c", "LIGHT_GOLD": "#8a6a00",
    "LIGHT_GOLD2": "#6b5200", "LIGHT_RED": "#be123c",
}

EXTRA_CSS = LAB_CSS + """
.ledlamp{width:34px;height:34px;border-radius:50%;border:2px solid var(--line);background:rgba(var(--ink-panel-rgb),.8);transition:.2s;flex:none}
.ledlamp.on{background:var(--gold);box-shadow:0 0 18px var(--gold)}
.ledlamp.hot{background:var(--red);box-shadow:0 0 18px var(--red)}
.bar4{display:flex;gap:10px;align-items:flex-end;margin:8px 0}
.bar4 div{text-align:center;font-family:var(--mono);font-size:.72rem;color:var(--muted)}
.meas{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:6px;margin:8px 0}
.meas div{padding:8px 10px;border-radius:12px;border:1px solid var(--line);background:rgba(var(--panel-rgb),.55);font-family:var(--mono);font-size:.95rem}
.meas div b{display:block;font-family:var(--font);font-size:.72rem;color:var(--muted);font-weight:500}
.scope{width:100%;height:130px;border-radius:12px;border:1px solid var(--line);background:rgba(var(--ink-panel-rgb),.85);display:block}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin:6px 0}
.chips span{padding:3px 10px;border-radius:999px;border:1px solid var(--line);font-size:.78rem;color:var(--muted)}
.chips span.got{border-color:var(--corner);color:var(--text);background:var(--ember-dim)}
select.sel{font-family:var(--mono);font-size:.85rem;padding:7px 9px;border-radius:10px;border:1px solid var(--line);background:rgba(var(--panel-rgb),.8);color:var(--text)}
"""

HERO = """<svg class="cityart" viewBox="0 0 480 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="หอคอยรูปสามเหลี่ยมออปแอมป์เรืองแสงกลางท้องฟ้ายามค่ำ">
  <defs><linearGradient id="gT8" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8b7bff"/><stop offset="1" stop-color="#ff8a1f"/></linearGradient>
  <filter id="fG8"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
  <rect width="480" height="300" rx="18" fill="#0a081c"/>
  <g fill="#efecff" opacity=".6"><circle cx="50" cy="40" r="1.5"/><circle cx="140" cy="70" r="1.2"/><circle cx="420" cy="50" r="1.6"/><circle cx="380" cy="120" r="1.2"/></g>
  <path d="M0 262 H480" stroke="#2a2460" stroke-width="2"/>
  <g filter="url(#fG8)" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M180 60 L180 250 L340 155 Z" stroke="url(#gT8)" stroke-width="6"/>
    <path d="M110 105 H180 M110 205 H180 M340 155 H420" stroke="#8b7bff" stroke-width="4"/>
    <path d="M150 105 h0" stroke="#ffe14d"/>
    <path d="M200 105 h22 M200 205 h22 M211 194 v22" stroke="#ffe14d" stroke-width="4"/>
    <path d="M380 155 V90 H140 V105" stroke="#ff8a1f" stroke-width="3" stroke-dasharray="6 6"/>
  </g>
  <path d="M60 230 q20 -40 40 0 t40 0" stroke="#ffe14d" stroke-width="2.5" fill="none" opacity=".8"/>
  <path d="M400 230 q20 -80 40 0 t40 0" stroke="#ff8a1f" stroke-width="2.5" fill="none" opacity=".8" transform="translate(-30 0)"/>
</svg>"""

ZONES = _rd('zones.html')
LAB_JS = _rd('labs.js')
LAB_WIRING = _rd('wiring.js')
INIT_EXTRA = _rd('init.js').strip()
exec(compile(_rd('bank.py'), 'g8_parts/bank.py', 'exec'))
