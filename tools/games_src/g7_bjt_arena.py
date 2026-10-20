# -*- coding: utf-8 -*-
"""SEASON 2 · ZONE 7 — BJT ARENA : สังเวียนทรานซิสเตอร์
GNR2022 อิเล็กทรอนิกส์พื้นฐาน ภาค 1/2569 · เนื้อหาหลังกลางภาค (เสริมโซน Z6 และ Z4 ที่ห้องอ่อน)
ตัวเลขอ้างอิง datasheet: 2N3904 (hFE 100–300 @ IC 10 mA, VCE(sat) ≤ 0.2 V @ 10 mA / ≤ 0.3 V @ 50 mA, VCEO 40 V, IC 200 mA)
ESP32 GPIO: ระดับลอจิก 3.3 V
ไฟล์แยกส่วน: g7_parts/zones.html, g7_parts/labs.js, g7_parts/bank.py"""
import os
from cpe_common import *
_P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'g7_parts')
def _rd(n): return open(os.path.join(_P, n), encoding='utf-8').read()

THEME = {
    "PRIMARY_RGB": "0,240,255",   "PRIMARY_HEX": "#00f0ff",
    "SECOND_RGB":  "177,75,255",  "SECOND_HEX":  "#b14bff",
    "GOLD_RGB":    "198,255,61",  "GOLD_HEX":    "#c6ff3d",
    "GOLD2_RGB":   "230,255,158", "GOLD2_HEX":   "#e6ff9e",
    "RED_RGB":     "251,113,133", "RED_HEX":     "#fb7185",
    "BG_RGB":      "5,16,26",     "BG_HEX":      "#05101a",
    "PANEL_RGB":   "12,30,46",
    "PANEL2_RGB":  "18,42,62",
    "BG2_HEX":     "#081826",
    "INK_HEX":     "#0c2234",
    "TEXT_HEX":    "#e8fbff",
    "MUTED_HEX":   "#9cc3cf",
    "MUTED2_HEX":  "#6c93a0",
    "MUTED3_HEX":  "#5a808d",
    "SECOND2_HEX": "#d09bff",
    "PRIM2_HEX":   "#7ff8ff",
    "LIGHT_EMBER": "#0e7490", "LIGHT_CORNER": "#7e22ce", "LIGHT_GOLD": "#4d7c0f",
    "LIGHT_GOLD2": "#3f6212", "LIGHT_RED": "#be123c",
}

EXTRA_CSS = LAB_CSS + """
.ledlamp{width:42px;height:42px;border-radius:50%;border:2px solid var(--line);background:rgba(var(--ink-panel-rgb),.8);transition:.25s;flex:none}
.ledlamp.on{background:var(--gold);box-shadow:0 0 calc(6px + 24px*var(--lv,1)) var(--gold)}
.ledlamp.hot{background:var(--red);box-shadow:0 0 22px var(--red)}
.rgchips{display:flex;gap:6px;flex-wrap:wrap;margin:6px 0}
.rgchips span{padding:3px 10px;border-radius:999px;border:1px solid var(--line);font-size:.78rem;color:var(--muted)}
.rgchips span.got{border-color:var(--corner);color:var(--text);background:var(--ember-dim)}
.meas{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:6px;margin:8px 0}
.meas div{padding:8px 10px;border-radius:12px;border:1px solid var(--line);background:rgba(var(--panel-rgb),.55);font-family:var(--mono);font-size:.95rem}
.meas div b{display:block;font-family:var(--font);font-size:.72rem;color:var(--muted);font-weight:500}
"""

HERO = """<svg class="cityart" viewBox="0 0 480 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="สังเวียนนีออนที่มีทรานซิสเตอร์ยักษ์อยู่กลางเวที">
  <defs><radialGradient id="gSpot" cx="50%" cy="40%" r="60%"><stop offset="0%" stop-color="rgba(0,240,255,.35)"/><stop offset="100%" stop-color="rgba(0,240,255,0)"/></radialGradient>
  <filter id="fGlow7"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
  <rect x="0" y="0" width="480" height="300" rx="18" fill="#05101a"/>
  <ellipse cx="240" cy="120" rx="220" ry="130" fill="url(#gSpot)"/>
  <ellipse cx="240" cy="250" rx="200" ry="30" fill="none" stroke="#b14bff" stroke-width="3" opacity=".7"/>
  <ellipse cx="240" cy="250" rx="160" ry="22" fill="none" stroke="#00f0ff" stroke-width="2" opacity=".5"/>
  <g filter="url(#fGlow7)" fill="none" stroke-linecap="round">
    <circle cx="250" cy="140" r="62" stroke="#00f0ff" stroke-width="5"/>
    <path d="M120 140 H226 M226 104 V176 M226 122 L278 92 V40 M226 158 L278 188 V244" stroke="#00f0ff" stroke-width="5"/>
    <path d="M262 182 L278 188 L258 194" fill="#c6ff3d" stroke="#c6ff3d" stroke-width="3"/>
    <path d="M150 128 l14 12 l-14 12" stroke="#c6ff3d" stroke-width="3"/>
    <path d="M296 56 l-10 -14 M308 68 l-8 -16" stroke="#b14bff" stroke-width="3"/>
  </g>
  <g font-family="monospace" font-size="20" font-weight="700"><text x="96" y="130" fill="#c6ff3d">B</text><text x="290" y="36" fill="#c6ff3d">C</text><text x="290" y="262" fill="#c6ff3d">E</text></g>
</svg>"""

ZONES = _rd('zones.html')
LAB_JS = _rd('labs.js')
LAB_WIRING = r"""
  const rb=e.target.closest('[data-rmrb]'); if(rb){rmRB=+rb.dataset.rmrb;SFX.play('select');rmUpdate(true);return;}
  const rr=e.target.closest('[data-rlrb]'); if(rr){rlRB=+rr.dataset.rlrb;rlDead=false;SFX.play('select');rlUpdate(true);return;}
  if(e.target.closest('#rlDiode')){rlD=!rlD;const b=$('#rlDiode');b.textContent=rlD?'มีไดโอดกันกลับ':'ไม่มีไดโอด';b.className='toggle '+(rlD?'on':'off');SFX.play('select');rlUpdate(true);return;}
  if(e.target.closest('#rlGpio')){if(!rlRB){rlUpdate(false);return;}rlOn=!rlOn;const b=$('#rlGpio');b.textContent=rlOn?'GPIO HIGH':'GPIO LOW';b.className='toggle '+(rlOn?'on':'off');SFX.play('select');rlUpdate(true,rlOn?'on':'off');return;}
  const dp=e.target.closest('[data-db]'); if(dp){dbPick(+dp.dataset.db);return;}
  if(e.target.closest('#dbNext')){dbI=(dbI+1)%DB.length;SFX.play('select');dbRender();return;}
"""
INIT_EXTRA = " $('#rmV').addEventListener('input',()=>rmUpdate(true)); rmUpdate(false); rlUpdate(false); dbRender();"

exec(compile(_rd('bank.py'), 'g7_parts/bank.py', 'exec'))
