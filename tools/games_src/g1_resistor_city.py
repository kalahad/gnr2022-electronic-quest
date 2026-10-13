# -*- coding: utf-8 -*-
"""SEASON 1 · ZONE 1 — RESISTOR CITY : เมืองตัวต้านทาน
เขียนใหม่บนเอนจินมาตรฐาน โดยใช้เนื้อหาจากเกมฉบับเดิม (gnr2022_game1_resistor_color_code.html)
อ้างอิงรหัสสี: IEC 60062 · ค่ามาตรฐาน: IEC 60063 (E6/E12/E24)"""
from cpe_common import *
from legacy_port import zone_theme

THEME = zone_theme('#f97316', '#a855f7', '#facc15', '#ef4444', '#c2410c', '#7e22ce', '#8a6a00', '#b91c1c', bg='#0f0a14')

EXTRA_CSS = LAB_CSS + """
.ctab td.sw{width:22px;padding:0}
.ctab i{display:inline-block;width:18px;height:18px;border-radius:5px;border:1px solid rgba(255,255,255,.35);vertical-align:middle}
.rbody{display:block;width:100%;max-width:420px;margin:6px auto}
.bandbtns{display:flex;gap:6px;flex-wrap:wrap;justify-content:center;margin:8px 0}
.bandbtns .btn{min-width:74px}
.cpal{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:8px 0}
.cpal button{width:34px;height:34px;border-radius:9px;border:2px solid rgba(255,255,255,.25);cursor:pointer}
.cpal button.sel{outline:3px solid var(--gold);outline-offset:2px}
.ledbulb{width:54px;height:54px;border-radius:50% 50% 12px 12px;border:2px solid var(--line);flex:none;transition:.25s;background:rgba(var(--ink-panel-rgb),.8)}
.ledbulb.burn{background:#3a3a3a !important;box-shadow:none !important;border-color:var(--red)}
.epick{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.epick button{padding:7px 10px;border-radius:10px;border:1px solid var(--line);background:rgba(var(--panel-rgb),.6);color:var(--text);font-family:var(--mono);cursor:pointer}
.epick button.sel{border-color:var(--gold);box-shadow:0 0 0 2px var(--ember-dim)}
"""

HERO = """<svg class="cityart" viewBox="0 0 480 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="เมืองยามค่ำที่ตึกเป็นตัวต้านทานแถบสี">
  <defs><filter id="fGlow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <linearGradient id="gSky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a1030"/><stop offset="1" stop-color="#0f0a14"/></linearGradient></defs>
  <rect x="0" y="0" width="480" height="300" rx="18" fill="url(#gSky)"/>
  <g fill="#eef0ff" opacity=".6"><circle cx="40" cy="30" r="1.4"/><circle cx="120" cy="60" r="1.2"/><circle cx="260" cy="24" r="1.5"/><circle cx="400" cy="50" r="1.3"/></g>
  <g filter="url(#fGlow)">
    <rect x="40" y="110" width="70" height="150" rx="16" fill="#d6b48a"/><rect x="40" y="132" width="70" height="12" fill="#facc15"/><rect x="40" y="154" width="70" height="12" fill="#a855f7"/><rect x="40" y="176" width="70" height="12" fill="#f97316"/><rect x="40" y="226" width="70" height="10" fill="#c9a227"/>
    <rect x="140" y="70" width="80" height="190" rx="18" fill="#c7a77d"/><rect x="140" y="96" width="80" height="13" fill="#7c4a1e"/><rect x="140" y="120" width="80" height="13" fill="#111"/><rect x="140" y="144" width="80" height="13" fill="#f97316"/><rect x="140" y="222" width="80" height="11" fill="#c9a227"/>
    <rect x="250" y="130" width="64" height="130" rx="15" fill="#d6b48a"/><rect x="250" y="150" width="64" height="11" fill="#ef4444"/><rect x="250" y="170" width="64" height="11" fill="#ef4444"/><rect x="250" y="190" width="64" height="11" fill="#7c4a1e"/><rect x="250" y="232" width="64" height="9" fill="#c9a227"/>
    <rect x="344" y="96" width="76" height="164" rx="17" fill="#c7a77d"/><rect x="344" y="118" width="76" height="12" fill="#3b82f6"/><rect x="344" y="140" width="76" height="12" fill="#9ca3af"/><rect x="344" y="162" width="76" height="12" fill="#ef4444"/><rect x="344" y="228" width="76" height="10" fill="#c9a227"/>
  </g>
  <path d="M0 262 H480" stroke="#f97316" stroke-width="3"/>
  <text x="240" y="288" text-anchor="middle" font-size="10" letter-spacing="3" fill="#c9b8d8">READ · DECODE · CHOOSE</text>
</svg>"""

COLORS_TABLE = """<div class="tbl-wrap"><table class="ctab">
      <tr><th></th><th>สี</th><th>ตัวเลข</th><th>ตัวคูณ</th><th>ค่าคลาดเคลื่อน</th></tr>
      <tr><td class="sw"><i style="background:#111"></i></td><td>ดำ</td><td>0</td><td>× 1</td><td>—</td></tr>
      <tr><td class="sw"><i style="background:#7c4a1e"></i></td><td>น้ำตาล</td><td>1</td><td>× 10</td><td>± 1%</td></tr>
      <tr><td class="sw"><i style="background:#ef4444"></i></td><td>แดง</td><td>2</td><td>× 100</td><td>± 2%</td></tr>
      <tr><td class="sw"><i style="background:#f97316"></i></td><td>ส้ม</td><td>3</td><td>× 1 k</td><td>—</td></tr>
      <tr><td class="sw"><i style="background:#facc15"></i></td><td>เหลือง</td><td>4</td><td>× 10 k</td><td>—</td></tr>
      <tr><td class="sw"><i style="background:#22c55e"></i></td><td>เขียว</td><td>5</td><td>× 100 k</td><td>± 0.5%</td></tr>
      <tr><td class="sw"><i style="background:#3b82f6"></i></td><td>น้ำเงิน</td><td>6</td><td>× 1 M</td><td>± 0.25%</td></tr>
      <tr><td class="sw"><i style="background:#8b5cf6"></i></td><td>ม่วง</td><td>7</td><td>× 10 M</td><td>± 0.1%</td></tr>
      <tr><td class="sw"><i style="background:#9ca3af"></i></td><td>เทา</td><td>8</td><td>—</td><td>—</td></tr>
      <tr><td class="sw"><i style="background:#f8fafc"></i></td><td>ขาว</td><td>9</td><td>—</td><td>—</td></tr>
      <tr><td class="sw"><i style="background:#c9a227"></i></td><td>ทอง</td><td>—</td><td>× 0.1</td><td>± 5%</td></tr>
      <tr><td class="sw"><i style="background:#cbd5e1"></i></td><td>เงิน</td><td>—</td><td>× 0.01</td><td>± 10%</td></tr>
    </table></div>"""

ZONES = """
<!-- ===== PREVIEW 1 ===== -->
<section id="scr-preview1" class="screen">
  <div class="panel">
    <span class="tag">City Block 01</span>
    <h2>กำลังจะเข้าสู่: ลานโอห์ม (Ohm Plaza)</h2>
    <div class="dcard">
      <div class="ico"><svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
        <path d="M40 10 L70 66 H10 Z" fill="none" stroke="#f97316" stroke-width="4" stroke-linejoin="round"/><path d="M22 46 H58 M40 46 V66" stroke="#facc15" stroke-width="3"/>
        <text x="40" y="38" text-anchor="middle" font-size="13" fill="#facc15" font-family="monospace">V</text><text x="29" y="61" text-anchor="middle" font-size="12" fill="#a855f7" font-family="monospace">I</text><text x="51" y="61" text-anchor="middle" font-size="12" fill="#a855f7" font-family="monospace">R</text></svg></div>
      <div><div class="skillcard" style="margin:0">
        <div class="sk-name">ทักษะที่จะได้: ใช้กฎของโอห์มและกำลังไฟฟ้า คำนวณตัวต้านทานจำกัดกระแสให้ LED</div>
        <p class="muted" style="margin:6px 0 0">ทุกครั้งที่เลือกตัวต้านทาน คำถามแรกคือ "กระแสจะเป็นเท่าไร" และ "ตัวต้านทานจะร้อนเกินไหม"</p>
      </div></div>
    </div>
    <div class="btn-row"><button class="btn primary" data-goto="scr-lesson1">เข้าลานโอห์ม</button></div>
  </div>
</section>

<!-- ===== BLOCK 1 ===== -->
<section id="scr-lesson1" class="screen">
  <div class="panel">
    <span class="tag">Block 01 · Ohm Plaza</span>
    <h2>ลานโอห์ม: แรงดัน กระแส ความต้านทาน และ LED</h2>
    <p>แรงดัน (V) คือแรงผลักให้ประจุเคลื่อนที่ กระแส (I) คือปริมาณประจุที่ไหลผ่านต่อวินาที ความต้านทาน (R) คือสิ่งที่ขัดขวางการไหล
      ทั้งสามปริมาณผูกกันด้วย <b>กฎของโอห์ม V = I × R</b> รู้สองค่าก็หาค่าที่สามได้เสมอ และกระแสที่ไหลผ่านตัวต้านทานจะกลายเป็น <b>ความร้อน</b> ตามกำลังไฟฟ้า P</p>
    <div class="tbl-wrap"><table>
      <tr><th>ปริมาณ</th><th>หน่วย</th><th>สูตร</th><th>เทียบกับระบบน้ำ</th></tr>
      <tr><td>แรงดัน V</td><td>โวลต์ (V)</td><td>V = I × R</td><td>ความสูงของถังน้ำ</td></tr>
      <tr><td>กระแส I</td><td>แอมแปร์ (A)</td><td>I = V / R</td><td>ปริมาณน้ำที่ไหลต่อวินาที</td></tr>
      <tr><td>ความต้านทาน R</td><td>โอห์ม (Ω)</td><td>R = V / I</td><td>ความคอดของท่อ</td></tr>
      <tr><td>กำลัง P</td><td>วัตต์ (W)</td><td>P = V × I = I² × R = V² / R</td><td>พลังที่ทำให้กังหันหมุน</td></tr>
    </table></div>
    <div class="codebox">ตัวคูณหน่วย: k = 10³   M = 10⁶   m = 10⁻³   µ = 10⁻⁶
ตัวอย่าง: 20 mA = 0.020 A   4.7 kΩ = 4,700 Ω   2.2 MΩ = 2,200,000 Ω</div>
    <p><b>ทำไม LED ต้องมีตัวต้านทานอนุกรมเสมอ</b> LED เป็นไดโอด เมื่อแรงดันถึงแรงดันตกคร่อมไปหน้า (Vf) กระแสจะเพิ่มขึ้นเร็วมาก
      ตัวต้านทานจึงรับแรงดันส่วนที่เหลือไว้ และกำหนดกระแสให้อยู่ในย่านใช้งาน (LED 5 มม. ทั่วไปใช้ราว 10–20 mA)</p>
    <div class="codebox">R = (Vs − Vf) / I
ตัวอย่าง: Vs = 9 V, LED แดง Vf ≈ 2.0 V, ต้องการ I = 20 mA
  R = (9 − 2.0) / 0.020 = 350 Ω  → เลือกค่ามาตรฐานที่สูงกว่า 390 Ω
  I จริง = 7.0 / 390 ≈ 17.9 mA   P บน R = 7.0 × 0.0179 ≈ 0.13 W → ใช้ตัว ¼ W ได้</div>
    <div class="tbl-wrap"><table>
      <tr><th>สี LED</th><th>Vf โดยประมาณ</th><th>ข้อสังเกต</th></tr>
      <tr><td>แดง</td><td>1.8 – 2.2 V</td><td>ต่ำสุดในกลุ่ม ใช้ไฟ 3.3 V ได้สบาย</td></tr>
      <tr><td>เขียว (มาตรฐาน) / เหลือง</td><td>2.0 – 2.2 V</td><td>ใกล้เคียงสีแดง</td></tr>
      <tr><td>น้ำเงิน / ขาว</td><td>2.8 – 3.4 V</td><td>สูงกว่า ต้องใช้ R ค่าน้อยลงที่แรงดันเดียวกัน</td></tr>
    </table></div>
    <div class="keyfact">จำให้ขึ้นใจ: <b>R = (Vs − Vf) / I</b> · ค่าที่คำนวณได้ให้ปัด <b>ขึ้น</b> เป็นค่ามาตรฐาน · ตรวจ <b>P = I² × R</b> ไม่ให้เกินพิกัดวัตต์</div>

    <h3 style="margin-top:18px">ห้องทดลอง: แท่นทดสอบ LED</h3>
    <p class="muted">เลือกแหล่งจ่าย สี LED และค่า R แล้วกดจ่ายไฟ ดูกระแส ความสว่าง และความร้อนบนตัวต้านทาน ลองให้เจอทั้ง 3 สถานะ: หรี่ ปกติ และเกินพิกัด</p>
    <div class="labrow">
      <button class="btn sm" data-vs="5">5 V</button><button class="btn sm" data-vs="9">9 V</button><button class="btn sm" data-vs="12">12 V</button>
      <span class="sp" style="width:10px"></span>
      <button class="btn sm" data-led="red">แดง</button><button class="btn sm" data-led="green">เขียว</button><button class="btn sm" data-led="blue">น้ำเงิน</button>
    </div>
    <label class="muted" for="ledR" style="display:block;font-size:.85rem">ค่า R (ค่ามาตรฐาน E12): <b id="ledRt">390 Ω</b></label>
    <input type="range" class="rng" id="ledR" min="0" max="24" value="11" aria-label="ค่าตัวต้านทาน">
    <div class="labrow">
      <div class="ledbulb" id="ledBulb"></div>
      <span class="readout" id="ledI">—</span><span class="readout" id="ledP">—</span>
      <button class="toggle on" id="ledPow">จ่ายไฟ</button>
    </div>
    <div class="meter"><i id="ledBar"></i></div>
    <div class="status-line" id="ledStatus">เลือกค่าแล้วกดจ่ายไฟ</div>
    <div class="btn-row"><button class="btn primary" data-quiz="check1">ไปทำแบบฝึกหัดด่านนี้</button></div>
  </div>
</section>

<!-- ===== PREVIEW 2 ===== -->
<section id="scr-preview2" class="screen">
  <div class="panel">
    <span class="tag">City Block 02</span>
    <h2>กำลังจะเข้าสู่: ถนนสายสี (Color Street)</h2>
    <div class="dcard">
      <div class="ico"><svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
        <path d="M4 40 H16 M64 40 H76" stroke="#c7a77d" stroke-width="4"/><rect x="16" y="26" width="48" height="28" rx="11" fill="#d6b48a"/>
        <rect x="24" y="26" width="6" height="28" fill="#facc15"/><rect x="34" y="26" width="6" height="28" fill="#8b5cf6"/><rect x="44" y="26" width="6" height="28" fill="#f97316"/><rect x="55" y="26" width="5" height="28" fill="#c9a227"/></svg></div>
      <div><div class="skillcard" style="margin:0">
        <div class="sk-name">ทักษะที่จะได้: ถอดรหัสแถบสี 4 และ 5 แถบ และเลือกสีจากค่าที่ต้องการ</div>
        <p class="muted" style="margin:6px 0 0">ตัวต้านทานเล็กเกินกว่าจะพิมพ์ตัวเลข จึงใช้แถบสีตามมาตรฐาน IEC 60062</p>
      </div></div>
    </div>
    <div class="btn-row"><button class="btn primary" data-goto="scr-lesson2">เข้าถนนสายสี</button></div>
  </div>
</section>

<!-- ===== BLOCK 2 ===== -->
<section id="scr-lesson2" class="screen">
  <div class="panel">
    <span class="tag">Block 02 · Color Street</span>
    <h2>ถนนสายสี: อ่านรหัสแถบสี</h2>
    <p>หันแถบค่าคลาดเคลื่อน (ทองหรือเงิน ซึ่งมักแยกห่างจากแถบอื่น) ไว้ทางขวาก่อนเสมอ แล้วอ่านจากซ้าย
      <b>แบบ 4 แถบ</b> = เลข 2 หลัก + ตัวคูณ + ค่าคลาดเคลื่อน · <b>แบบ 5 แถบ</b> = เลข 3 หลัก + ตัวคูณ + ค่าคลาดเคลื่อน (มักเป็นตัวต้านทานฟิล์มโลหะ ±1%)</p>
    """ + COLORS_TABLE + """
    <div class="codebox">ตัวอย่าง 4 แถบ: เหลือง ม่วง ส้ม ทอง     = 47 × 1 k   = 47 kΩ ± 5%
ตัวอย่าง 4 แถบ: น้ำตาล ดำ ทอง ทอง      = 10 × 0.1  = 1.0 Ω ± 5%
ตัวอย่าง 5 แถบ: น้ำตาล ดำ ดำ แดง น้ำตาล = 100 × 100 = 10 kΩ ± 1%
ย้อนกลับ: 2.2 kΩ ± 5% = 22 × 100 → แดง แดง แดง ทอง</div>
    <div class="keyfact">จำให้ขึ้นใจ: เลข 2–7 ไล่ตามสีรุ้ง <b>แดง ส้ม เหลือง เขียว น้ำเงิน ม่วง</b> · หัวมืด ดำ 0 น้ำตาล 1 · ท้ายสว่าง เทา 8 ขาว 9 · <b>ทอง ±5% เงิน ±10%</b></div>

    <h3 style="margin-top:18px">ห้องทดลอง: เครื่องถอดรหัสแถบสี</h3>
    <p class="muted">เลือกแถบที่จะเปลี่ยน แล้วแตะสีด้านล่าง ค่าจะคำนวณทันที กด "โจทย์ใหม่" เพื่อรับค่าเป้าหมาย แล้วตั้งสีให้ตรง ทำให้ถูก 3 โจทย์</p>
    <svg class="rbody" id="rbSvg" viewBox="0 0 420 110" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="ตัวต้านทาน 4 แถบสี"></svg>
    <div class="bandbtns" id="rbSlots"></div>
    <div class="cpal" id="rbPal"></div>
    <div class="labrow"><span class="readout" id="rbVal">—</span><span class="readout" id="rbTgt"><small>ยังไม่มีโจทย์</small></span></div>
    <div class="labrow"><button class="btn sm" id="rbNew">โจทย์ใหม่</button><button class="btn sm primary" id="rbCheck">ตรวจคำตอบ</button></div>
    <div class="status-line" id="rbStatus">แตะแถบ แล้วเลือกสี</div>
    <div class="btn-row"><button class="btn primary" data-quiz="check2">ไปทำแบบฝึกหัดด่านนี้</button></div>
  </div>
</section>

<!-- ===== PREVIEW 3 ===== -->
<section id="scr-preview3" class="screen">
  <div class="panel">
    <span class="tag">City Block 03</span>
    <h2>กำลังจะเข้าสู่: หอค่ามาตรฐาน (Standard Tower)</h2>
    <div class="dcard">
      <div class="ico"><svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
        <rect x="26" y="8" width="28" height="64" rx="4" fill="none" stroke="#a855f7" stroke-width="4"/><path d="M32 20 H48 M32 32 H48 M32 44 H48 M32 56 H48" stroke="#facc15" stroke-width="3"/></svg></div>
      <div><div class="skillcard" style="margin:0">
        <div class="sk-name">ทักษะที่จะได้: ใช้ค่าคลาดเคลื่อน ค่ามาตรฐาน E-series และพิกัดกำลัง เลือกตัวต้านทานที่หาซื้อได้จริง</div>
        <p class="muted" style="margin:6px 0 0">ค่าที่คำนวณได้มักไม่มีขาย เช่น 350 Ω เราต้องรู้ว่าจะเลือกตัวไหนแทน</p>
      </div></div>
    </div>
    <div class="btn-row"><button class="btn primary" data-goto="scr-lesson3">ขึ้นหอค่ามาตรฐาน</button></div>
  </div>
</section>

<!-- ===== BLOCK 3 ===== -->
<section id="scr-lesson3" class="screen">
  <div class="panel">
    <span class="tag">Block 03 · Standard Tower</span>
    <h2>หอค่ามาตรฐาน: ค่าคลาดเคลื่อน E-series และพิกัดวัตต์</h2>
    <p>ค่าคลาดเคลื่อนบอกช่วงค่าจริงที่ผู้ผลิตรับประกัน เช่น 1 kΩ ±5% มีค่าจริงได้ตั้งแต่ <b>950 Ω ถึง 1,050 Ω</b>
      ผู้ผลิตจึงผลิตเฉพาะ <b>ค่ามาตรฐาน (E-series ตาม IEC 60063)</b> ที่ช่วงคลาดเคลื่อนของค่าที่อยู่ติดกันต่อกันพอดี และค่าชุดเดียวกันซ้ำทุกทศนิยม (10, 100, 1 k, 10 k ...)</p>
    <div class="tbl-wrap"><table>
      <tr><th>อนุกรม</th><th>ค่าคลาดเคลื่อน</th><th>ค่าในหนึ่งทศนิยม</th></tr>
      <tr><td>E6</td><td>± 20%</td><td>10 15 22 33 47 68</td></tr>
      <tr><td>E12</td><td>± 10%</td><td>10 12 15 18 22 27 33 39 47 56 68 82</td></tr>
      <tr><td>E24</td><td>± 5%</td><td>E12 + 11 13 16 20 24 30 36 43 51 62 75 91</td></tr>
    </table></div>
    <div class="codebox">ขั้นตอนเลือกตัวต้านทานสำหรับ LED
1) คำนวณ R = (Vs − Vf) / I
2) เลือกค่ามาตรฐานที่ "สูงกว่าและใกล้ที่สุด" เพื่อให้กระแสไม่เกินที่ออกแบบ
3) คำนวณ P = I² × R แล้วเลือกพิกัดวัตต์อย่างน้อย 2 เท่าของ P (เผื่อความร้อน)
ตัวอย่าง: 12 V, LED น้ำเงิน Vf 3.2 V, 20 mA → R = 440 Ω → E12 = 470 Ω
          I = 8.8 / 470 ≈ 18.7 mA   P ≈ 0.165 W → เลือก ½ W (¼ W มีระยะเผื่อไม่ถึง 2 เท่า)</div>
    <div class="keyfact">จำให้ขึ้นใจ: <b>ค่าที่คำนวณได้ ปัดขึ้นเป็นค่ามาตรฐาน</b> · <b>พิกัดวัตต์ ≥ 2 × P</b> · 1 kΩ ±5% = 950 ถึง 1,050 Ω</div>

    <h3 style="margin-top:18px">ห้องทดลอง: เลือกตัวต้านทานที่หาซื้อได้จริง</h3>
    <p class="muted">กด "งานใหม่" ระบบจะให้แหล่งจ่าย สี LED และกระแสเป้าหมาย เลือกค่า E12 และพิกัดวัตต์ แล้วกดส่งงาน ทำให้ผ่าน 3 งาน</p>
    <div class="status-line" id="pkJob">กด "งานใหม่" เพื่อรับงาน</div>
    <div class="epick" id="pkR"></div>
    <div class="epick" id="pkW"></div>
    <div class="labrow"><button class="btn sm" id="pkNew">งานใหม่</button><button class="btn sm primary" id="pkGo">ส่งงาน</button></div>
    <div class="status-line" id="pkStatus">ยังไม่ได้ส่งงาน</div>
    <div class="btn-row"><button class="btn primary" data-quiz="check3">ไปทำแบบฝึกหัดด่านนี้</button></div>
  </div>
</section>
"""

LAB_JS = r"""
/* ---- ข้อมูลร่วม ---- */
const E12=[10,12,15,18,22,27,33,39,47,56,68,82];
const E12R=(function(){const o=[];[1,10,100,1000].forEach(m=>E12.forEach(v=>o.push(v*m)));return o.filter(v=>v>=47&&v<=4700);})();
function fmtOhm(r){ if(r>=1e6) return +(r/1e6).toPrecision(3)+' MΩ'; if(r>=1000) return +(r/1000).toPrecision(3)+' kΩ'; return +r.toPrecision(3)+' Ω'; }
const LEDS={red:{n:'แดง',vf:2.0,c:'#ef4444'},green:{n:'เขียว',vf:2.1,c:'#22c55e'},blue:{n:'น้ำเงิน',vf:3.2,c:'#3b82f6'}};

/* ---- LAB 1: LED bench ---- */
let ledVs=9, ledC='red', ledOn=true;
function ledUpdate(user){
  const R=E12R[+$('#ledR').value], L=LEDS[ledC], b=$('#ledBulb'), st=$('#ledStatus');
  $('#ledRt').textContent=fmtOhm(R);
  document.querySelectorAll('[data-vs]').forEach(x=>x.classList.toggle('primary',+x.dataset.vs===ledVs));
  document.querySelectorAll('[data-led]').forEach(x=>x.classList.toggle('primary',x.dataset.led===ledC));
  if(!ledOn){ b.className='ledbulb'; b.style.background=''; b.style.boxShadow=''; $('#ledI').innerHTML='0<small>mA</small>'; $('#ledP').innerHTML='0<small>W</small>'; $('#ledBar').style.width='0%'; st.className='status-line'; st.textContent='ปิดไฟอยู่ กดจ่ายไฟ'; return; }
  const I=Math.max(0,(ledVs-L.vf)/R), P=I*I*R, mA=I*1000;
  $('#ledI').innerHTML=mA.toFixed(1)+'<small>mA</small>'; $('#ledP').innerHTML=P.toFixed(3)+'<small>W บน R</small>';
  $('#ledBar').style.width=Math.min(100,mA/40*100)+'%';
  let k;
  b.className='ledbulb';
  if(mA>30){ k='burn'; b.classList.add('burn'); st.className='status-line'; st.innerHTML='<b>LED ไหม้</b> — '+mA.toFixed(1)+' mA เกินพิกัดสูงสุดราว 30 mA ต้องเพิ่มค่า R'; }
  else{
    const lv=Math.min(1,mA/20); b.style.background=L.c; b.style.opacity=(0.25+0.75*lv).toFixed(2); b.style.boxShadow='0 0 '+(6+30*lv)+'px '+L.c;
    if(mA>20){ k='hot'; st.className='status-line'; st.innerHTML='<b>เกินกระแสใช้งาน</b> — '+mA.toFixed(1)+' mA สว่างมากแต่ร้อนและอายุสั้น ควรอยู่ในช่วง 10–20 mA'; }
    else if(mA>=10){ k='ok'; st.className='status-line ok'; st.innerHTML='<b>ปกติ</b> — I = ('+ledVs+' − '+L.vf+') / '+fmtOhm(R)+' = '+mA.toFixed(1)+' mA อยู่ในย่านใช้งาน'; }
    else { k='dim'; st.className='status-line'; st.innerHTML='<b>หรี่</b> — '+mA.toFixed(1)+' mA น้อยเกินไป ลองลดค่า R'; }
  }
  if(P>0.25) st.innerHTML+=' · ตัวต้านทาน ¼ W ร้อนเกินพิกัด ('+P.toFixed(2)+' W)';
  if(user) markLab('lab1',k,3);
}

/* ---- LAB 2: color decoder ---- */
const CC=[['ดำ','#111'],['น้ำตาล','#7c4a1e'],['แดง','#ef4444'],['ส้ม','#f97316'],['เหลือง','#facc15'],['เขียว','#22c55e'],['น้ำเงิน','#3b82f6'],['ม่วง','#8b5cf6'],['เทา','#9ca3af'],['ขาว','#f8fafc'],['ทอง','#c9a227'],['เงิน','#cbd5e1']];
const MULT={0:1,1:10,2:100,3:1e3,4:1e4,5:1e5,6:1e6,7:1e7,10:0.1,11:0.01};
const TOL={1:1,2:2,5:0.5,6:0.25,7:0.1,10:5,11:10};
let rb=[4,7,3,10], rbSel=0, rbTarget=null, rbOk=0;
function rbValue(){ return (rb[0]*10+rb[1])*MULT[rb[2]]; }
function rbDraw(){
  const x=[118,158,198,268], body='<path d="M0 55 H70 M350 55 H420" stroke="#9ca3af" stroke-width="6"/><rect x="70" y="18" width="280" height="74" rx="30" fill="#d6b48a"/>';
  $('#rbSvg').innerHTML=body+rb.map((c,i)=>'<rect x="'+x[i]+'" y="18" width="22" height="74" fill="'+CC[c][1]+'"'+(i===rbSel?' stroke="#fff" stroke-width="3"':'')+'/>').join('');
  $('#rbSlots').innerHTML=['เลขตัวที่ 1','เลขตัวที่ 2','ตัวคูณ','คลาดเคลื่อน'].map((t,i)=>'<button class="btn sm'+(i===rbSel?' primary':'')+'" data-rbslot="'+i+'">'+t+'<br><small>'+CC[rb[i]][0]+'</small></button>').join('');
  const ok=rbSel<2?[0,1,2,3,4,5,6,7,8,9]:rbSel===2?[0,1,2,3,4,5,6,7,10,11]:[1,2,5,6,7,10,11];
  $('#rbPal').innerHTML=ok.map(c=>'<button data-rbc="'+c+'" title="'+CC[c][0]+'" aria-label="'+CC[c][0]+'" style="background:'+CC[c][1]+'" class="'+(rb[rbSel]===c?'sel':'')+'"></button>').join('');
  $('#rbVal').innerHTML=fmtOhm(rbValue())+'<small>± '+TOL[rb[3]]+'%</small>';
}
function rbSet(c){ rb[rbSel]=c; SFX.play('select'); if(rbSel<3) rbSel++; rbDraw(); markLab('lab2','c'+rbValue(),1); }
function rbNew(){
  const d1=1+Math.floor(Math.random()*9), d2=Math.floor(Math.random()*10), m=[0,1,2,3,4,5,10][Math.floor(Math.random()*7)], t=[10,11,1,2][Math.floor(Math.random()*4)];
  rbTarget={v:(d1*10+d2)*MULT[m],t:TOL[t]};
  $('#rbTgt').innerHTML='เป้าหมาย '+fmtOhm(rbTarget.v)+'<small>± '+rbTarget.t+'%</small>';
  const st=$('#rbStatus'); st.className='status-line'; st.textContent='ตั้งแถบสีให้ได้ค่าเป้าหมาย แล้วกดตรวจคำตอบ'; SFX.play('click');
}
function rbCheck(){
  const st=$('#rbStatus');
  if(!rbTarget){ st.textContent='กด "โจทย์ใหม่" ก่อน'; return; }
  const ok=Math.abs(rbValue()-rbTarget.v)<1e-9 && TOL[rb[3]]===rbTarget.t;
  if(ok){ rbOk++; st.className='status-line ok'; st.innerHTML='<b>ถูกต้อง</b> — '+rb.map(c=>CC[c][0]).join(' ')+' = '+fmtOhm(rbTarget.v)+' ± '+rbTarget.t+'% (ถูกแล้ว '+rbOk+' โจทย์)'; SFX.play('fanfare'); markLab('lab2','t'+rbOk,4); rbTarget=null; $('#rbTgt').innerHTML='<small>กดโจทย์ใหม่</small>'; }
  else { st.className='status-line'; st.innerHTML='ยังไม่ตรง — ตอนนี้คือ '+fmtOhm(rbValue())+' ± '+TOL[rb[3]]+'% ตรวจตัวคูณและแถบสุดท้ายอีกครั้ง'; SFX.play('wrong'); }
}

/* ---- LAB 3: real-world picker ---- */
let pkJob=null, pkRsel=null, pkWsel=null, pkDone=0;
const PKW=[0.125,0.25,0.5,1];
function pkNew(){
  const vs=[5,9,12][Math.floor(Math.random()*3)], lk=['red','green','blue'][Math.floor(Math.random()*3)], i=[0.010,0.015,0.020][Math.floor(Math.random()*3)];
  const need=(vs-LEDS[lk].vf)/i, best=E12R.find(v=>v>=need-1e-9);
  pkJob={vs:vs,lk:lk,i:i,need:need,best:best}; pkRsel=null; pkWsel=null;
  $('#pkJob').className='status-line'; $('#pkJob').innerHTML='งาน: แหล่งจ่าย <b>'+vs+' V</b> · LED <b>'+LEDS[lk].n+'</b> (Vf '+LEDS[lk].vf+' V) · กระแสไม่เกิน <b>'+(i*1000)+' mA</b>';
  pkDraw(); SFX.play('click');
}
function pkDraw(){
  $('#pkR').innerHTML=E12R.filter(v=>v>=100&&v<=1000).map(v=>'<button data-pkr="'+v+'" class="'+(pkRsel===v?'sel':'')+'">'+fmtOhm(v)+'</button>').join('');
  $('#pkW').innerHTML=PKW.map(w=>'<button data-pkw="'+w+'" class="'+(pkWsel===w?'sel':'')+'">'+(w===0.125?'⅛':w===0.25?'¼':w===0.5?'½':'1')+' W</button>').join('');
}
function pkGo(){
  const st=$('#pkStatus');
  if(!pkJob){ st.textContent='กด "งานใหม่" ก่อน'; return; }
  if(pkRsel==null||pkWsel==null){ st.textContent='เลือกทั้งค่า R และพิกัดวัตต์'; return; }
  const I=(pkJob.vs-LEDS[pkJob.lk].vf)/pkRsel, P=I*I*pkRsel, wNeed=PKW.find(w=>w>=2*P);
  const okR=pkRsel===pkJob.best, okW=pkWsel===wNeed;
  const sol='R คำนวณ = ('+pkJob.vs+' − '+LEDS[pkJob.lk].vf+') / '+(pkJob.i*1000)+' mA = '+fmtOhm(+pkJob.need.toFixed(1))+' → E12 ที่สูงกว่าและใกล้สุด = '+fmtOhm(pkJob.best);
  if(okR&&okW){ pkDone++; st.className='status-line ok'; st.innerHTML='<b>ผ่าน</b> — '+sol+' · I = '+(I*1000).toFixed(1)+' mA · P = '+P.toFixed(3)+' W → พิกัด ≥ '+(2*P).toFixed(3)+' W (สำเร็จ '+pkDone+' งาน)'; SFX.play('fanfare'); markLab('lab3','j'+pkDone,5); pkJob=null; }
  else { st.className='status-line'; st.innerHTML='<b>ยังไม่ผ่าน</b> — '+(okR?'ค่า R ถูกแล้ว':'ค่า R: '+sol)+' · '+(okW?'พิกัดวัตต์ถูกแล้ว':'พิกัดวัตต์ต้องไม่น้อยกว่า 2 × P'); SFX.play('wrong'); }
}
"""

LAB_WIRING = r"""
  const vsb=e.target.closest('[data-vs]'); if(vsb){ledVs=+vsb.dataset.vs;SFX.play('select');ledUpdate(true);return;}
  const lb=e.target.closest('[data-led]'); if(lb){ledC=lb.dataset.led;SFX.play('select');ledUpdate(true);return;}
  if(e.target.closest('#ledPow')){ledOn=!ledOn;const b=$('#ledPow');b.textContent=ledOn?'จ่ายไฟ':'ปิดไฟ';b.className='toggle '+(ledOn?'on':'off');SFX.play('select');ledUpdate(true);return;}
  const sl=e.target.closest('[data-rbslot]'); if(sl){rbSel=+sl.dataset.rbslot;SFX.play('click');rbDraw();return;}
  const rc=e.target.closest('[data-rbc]'); if(rc){rbSet(+rc.dataset.rbc);return;}
  if(e.target.closest('#rbNew')){rbNew();return;}
  if(e.target.closest('#rbCheck')){rbCheck();return;}
  const pr=e.target.closest('[data-pkr]'); if(pr){pkRsel=+pr.dataset.pkr;SFX.play('select');pkDraw();return;}
  const pw=e.target.closest('[data-pkw]'); if(pw){pkWsel=+pw.dataset.pkw;SFX.play('select');pkDraw();return;}
  if(e.target.closest('#pkNew')){pkNew();return;}
  if(e.target.closest('#pkGo')){pkGo();return;}
"""
INIT_EXTRA = " $('#ledR').addEventListener('input',()=>ledUpdate(true)); ledUpdate(false); rbDraw(); pkDraw();"

B = {}
B['district1'] = [
 ('ตัวต้านทาน 1 kΩ ต่อกับแหล่งจ่าย 5 V กระแสที่ไหลผ่านมีค่าเท่าใด',
  ['5 mA', '5 A', '0.2 mA', '200 mA'],
  'I = V / R = 5 / 1,000 = 0.005 A = 5 mA'),
 ('มีกระแส 20 mA ไหลผ่านตัวต้านทาน 470 Ω แรงดันตกคร่อมตัวต้านทานเท่าใด',
  ['9.4 V', '23.5 V', '0.94 V', '4.7 V'],
  'V = I × R = 0.020 × 470 = 9.4 V'),
 ('ข้อใดคือสูตรกำลังไฟฟ้าที่ "ไม่ถูกต้อง"',
  ['P = V / I', 'P = V × I', 'P = I² × R', 'P = V² / R'],
  'กำลังไฟฟ้า P = V × I และแทน V = IR จะได้ I²R หรือแทน I = V/R จะได้ V²/R ส่วน V / I คือความต้านทาน ไม่ใช่กำลัง'),
 ('ตัวต้านทาน 100 Ω มีกระแส 50 mA ไหลผ่าน กำลังที่กลายเป็นความร้อนเท่าใด',
  ['0.25 W', '5 W', '0.5 W', '2.5 W'],
  'P = I² × R = (0.05)² × 100 = 0.0025 × 100 = 0.25 W ตัวต้านทาน ¼ W จะทำงานเต็มพิกัดพอดี จึงควรเลือก ½ W'),
 ('4.7 kΩ มีค่าเท่ากับกี่โอห์ม',
  ['4,700 Ω', '470 Ω', '47,000 Ω', '0.0047 Ω'],
  'k = 10³ ดังนั้น 4.7 kΩ = 4.7 × 1,000 = 4,700 Ω'),
 ('ทำไมต้องต่อตัวต้านทานอนุกรมกับ LED ทุกครั้ง',
  ['เพื่อจำกัดกระแส เพราะเมื่อแรงดันถึง Vf กระแสของ LED จะเพิ่มขึ้นเร็วมาก', 'เพื่อเพิ่มแรงดันให้ LED สว่างขึ้น', 'เพื่อเปลี่ยนสีของแสง LED', 'เพื่อให้ LED ต่อกลับขั้วได้'],
  'LED เป็นไดโอด เมื่อแรงดันถึงแรงดันไปหน้า Vf กระแสจะพุ่งขึ้นอย่างรวดเร็ว ตัวต้านทานรับแรงดันส่วนเกินและกำหนดกระแสให้อยู่ในย่านใช้งาน'),
 ('แหล่งจ่าย 5 V ขับ LED แดง Vf = 2 V ที่กระแส 20 mA ต้องใช้ตัวต้านทานกี่โอห์ม',
  ['150 Ω', '250 Ω', '100 Ω', '350 Ω'],
  'R = (Vs − Vf) / I = (5 − 2) / 0.020 = 150 Ω'),
 ('แหล่งจ่าย 9 V ขับ LED แดง Vf = 2 V ที่ 20 mA คำนวณ R ได้ 350 Ω ควรเลือกค่ามาตรฐาน E12 ค่าใด',
  ['390 Ω', '330 Ω', '300 Ω', '360 Ω'],
  'ปัดขึ้นเป็นค่ามาตรฐานที่ใกล้สุดเพื่อให้กระแสไม่เกินที่ออกแบบ ในอนุกรม E12 ค่าถัดจาก 330 คือ 390 Ω (300 และ 360 อยู่ใน E24 ไม่ใช่ E12)'),
 ('ใช้ตัวต้านทาน 390 Ω กับแหล่งจ่าย 9 V และ LED แดง Vf = 2 V กระแสจริงประมาณเท่าใด',
  ['17.9 mA', '23.1 mA', '20.0 mA', '5.1 mA'],
  'I = (9 − 2) / 390 = 7 / 390 ≈ 0.0179 A = 17.9 mA ต่ำกว่า 20 mA เล็กน้อย ปลอดภัยต่อ LED'),
 ('LED สีน้ำเงินมี Vf สูงกว่า LED สีแดง ถ้าใช้แหล่งจ่ายและกระแสเท่ากัน ค่า R สำหรับ LED น้ำเงินจะเป็นอย่างไร',
  ['น้อยกว่า เพราะแรงดันที่เหลือตกคร่อม R น้อยลง', 'มากกว่า เพราะ Vf สูงกว่า', 'เท่ากัน เพราะกระแสเท่ากัน', 'ต้องเป็นศูนย์'],
  'R = (Vs − Vf) / I เมื่อ Vf สูงขึ้น ตัวตั้ง (Vs − Vf) ลดลง R ที่ต้องใช้จึงน้อยลง'),
 ('ถ้าเพิ่มค่าตัวต้านทานที่ต่ออนุกรมกับ LED จาก 220 Ω เป็น 1 kΩ โดยแหล่งจ่ายเท่าเดิม จะเกิดอะไรขึ้น',
  ['กระแสลดลง LED หรี่ลง', 'กระแสเพิ่มขึ้น LED สว่างขึ้น', 'แรงดัน Vf ของ LED เพิ่มเป็นสองเท่า', 'ไม่มีผลใด ๆ'],
  'แรงดันที่ตกคร่อม R ใกล้เคียงเดิม เมื่อ R เพิ่มขึ้น กระแส I = (Vs − Vf) / R จึงลดลง และ LED หรี่ลง'),
 ('20 mA มีค่าเท่ากับกี่แอมแปร์',
  ['0.020 A', '0.20 A', '2.0 A', '0.0020 A'],
  'm = 10⁻³ ดังนั้น 20 mA = 20 × 0.001 = 0.020 A'),
 ('ตัวต้านทาน 1 kΩ ต่อตรงกับแหล่งจ่าย 12 V ใช้ตัวพิกัด ¼ W ได้หรือไม่',
  ['ไม่ได้ เพราะ P = 12² / 1,000 = 0.144 W เกินครึ่งของพิกัด ควรใช้ ½ W', 'ได้ เพราะ P = 0.012 W', 'ได้ เพราะ P = 12 W', 'ไม่ได้ เพราะ P = 12 W'],
  'P = V² / R = 144 / 1,000 = 0.144 W ไม่เกิน ¼ W แต่ระยะเผื่อน้อยกว่า 2 เท่า ตามแนวปฏิบัติจึงควรเลือก ½ W'),
]
B['district2'] = [
 ('ตัวต้านทาน 4 แถบ สี น้ำตาล ดำ แดง ทอง มีค่าเท่าใด',
  ['1 kΩ ± 5%', '102 Ω ± 5%', '10 kΩ ± 5%', '1 kΩ ± 10%'],
  'น้ำตาล = 1, ดำ = 0 ได้ 10 แดงเป็นตัวคูณ × 100 = 1,000 Ω ทองคือ ± 5%'),
 ('ตัวต้านทาน 4 แถบ สี เหลือง ม่วง ส้ม ทอง มีค่าเท่าใด',
  ['47 kΩ ± 5%', '473 Ω ± 5%', '4.7 kΩ ± 5%', '470 kΩ ± 5%'],
  'เหลือง 4 ม่วง 7 ได้ 47 ส้มคือ × 1 k จึงได้ 47 kΩ'),
 ('ตัวต้านทาน 4 แถบ สี แดง แดง น้ำตาล ทอง มีค่าเท่าใด',
  ['220 Ω ± 5%', '22 Ω ± 5%', '2.2 kΩ ± 5%', '221 Ω ± 5%'],
  'แดง 2 แดง 2 ได้ 22 น้ำตาลคือ × 10 จึงได้ 220 Ω'),
 ('ต้องการตัวต้านทาน 10 kΩ ± 5% แบบ 4 แถบ ต้องเป็นสีใด',
  ['น้ำตาล ดำ ส้ม ทอง', 'น้ำตาล ดำ แดง ทอง', 'น้ำตาล ดำ เหลือง ทอง', 'ดำ น้ำตาล ส้ม ทอง'],
  '10 kΩ = 10 × 1,000 ตัวเลข 1 0 คือ น้ำตาล ดำ ตัวคูณ × 1 k คือส้ม และ ± 5% คือทอง'),
 ('แถบที่สามของตัวต้านทาน 4 แถบเป็นสีทอง หมายความว่าอย่างไร',
  ['คูณด้วย 0.1', 'ค่าคลาดเคลื่อน ± 5%', 'คูณด้วย 1,000', 'เลขนัยสำคัญตัวที่ 3'],
  'ในตำแหน่งตัวคูณ ทองคือ × 0.1 และเงินคือ × 0.01 ใช้กับตัวต้านทานที่มีค่าต่ำกว่า 10 Ω'),
 ('ตัวต้านทาน 4 แถบ สี น้ำตาล ดำ ทอง ทอง มีค่าเท่าใด',
  ['1.0 Ω ± 5%', '10 Ω ± 5%', '0.1 Ω ± 5%', '100 Ω ± 5%'],
  'ตัวเลข 1 0 = 10 คูณ 0.1 (ทอง) = 1.0 Ω'),
 ('แถบค่าคลาดเคลื่อนสีเงินหมายถึงเท่าใด',
  ['± 10%', '± 5%', '± 1%', '± 20%'],
  'ทอง ± 5% และเงิน ± 10% ถ้าไม่มีแถบค่าคลาดเคลื่อนเลยคือ ± 20%'),
 ('ตัวต้านทาน 5 แถบ สี น้ำตาล ดำ ดำ แดง น้ำตาล มีค่าเท่าใด',
  ['10 kΩ ± 1%', '1 kΩ ± 1%', '100 Ω ± 1%', '10 kΩ ± 2%'],
  'แบบ 5 แถบใช้เลข 3 หลัก: 1 0 0 = 100 คูณ × 100 (แดง) = 10,000 Ω แถบสุดท้ายน้ำตาลคือ ± 1%'),
 ('ก่อนเริ่มอ่านรหัสสี ควรวางตัวต้านทานอย่างไร',
  ['ให้แถบค่าคลาดเคลื่อน (ทองหรือเงิน ที่มักแยกห่าง) อยู่ทางขวา', 'ให้แถบสีดำอยู่ทางขวา', 'ให้ขาที่ยาวกว่าอยู่ทางซ้าย', 'วางด้านใดก็ได้ผลเท่ากัน'],
  'แถบค่าคลาดเคลื่อนมักเป็นทองหรือเงินและเว้นระยะห่างจากแถบอื่น เมื่อวางไว้ทางขวาจะอ่านจากซ้ายได้ถูกลำดับ'),
 ('สีใดแทนตัวเลข 7',
  ['ม่วง', 'น้ำเงิน', 'เทา', 'เขียว'],
  'ไล่ตามสีรุ้งตั้งแต่ 2: แดง 2 ส้ม 3 เหลือง 4 เขียว 5 น้ำเงิน 6 ม่วง 7 จากนั้นเทา 8 ขาว 9'),
 ('ตัวต้านทาน 1 kΩ แบบ 4 แถบ ± 5% ข้อใดคือสีที่ถูกต้อง',
  ['น้ำตาล ดำ แดง ทอง', 'น้ำตาล ดำ ส้ม ทอง', 'ดำ น้ำตาล แดง ทอง', 'น้ำตาล แดง ดำ ทอง'],
  '1 kΩ = 10 × 100 จึงเป็น น้ำตาล (1) ดำ (0) แดง (× 100) ทอง (± 5%)'),
 ('ตัวต้านทาน 4 แถบ สี ส้ม ส้ม ดำ ทอง มีค่าเท่าใด',
  ['33 Ω ± 5%', '330 Ω ± 5%', '3.3 Ω ± 5%', '330 kΩ ± 5%'],
  'ส้ม 3 ส้ม 3 ได้ 33 ดำคือ × 1 จึงได้ 33 Ω'),
 ('ตัวต้านทาน 4 แถบ สี น้ำเงิน เทา แดง ทอง มีค่าเท่าใด',
  ['6.8 kΩ ± 5%', '68 kΩ ± 5%', '682 Ω ± 5%', '680 Ω ± 5%'],
  'น้ำเงิน 6 เทา 8 ได้ 68 แดงคือ × 100 จึงได้ 6,800 Ω = 6.8 kΩ'),
]
B['district3'] = [
 ('ตัวต้านทาน 1 kΩ ± 5% มีค่าจริงอยู่ในช่วงใด',
  ['950 Ω ถึง 1,050 Ω', '995 Ω ถึง 1,005 Ω', '900 Ω ถึง 1,100 Ω', '500 Ω ถึง 1,500 Ω'],
  '5% ของ 1,000 Ω คือ 50 Ω ค่าจริงจึงอยู่ระหว่าง 1,000 − 50 ถึง 1,000 + 50'),
 ('ตัวต้านทาน 470 Ω ± 10% มีค่าสูงสุดที่ยอมรับได้เท่าใด',
  ['517 Ω', '480 Ω', '470 Ω', '564 Ω'],
  '10% ของ 470 คือ 47 ค่าสูงสุดคือ 470 + 47 = 517 Ω'),
 ('ข้อใดคือค่าในอนุกรม E12 ทั้งหมด',
  ['10 12 15 18 22 27 33 39 47 56 68 82', '10 20 30 40 50 60 70 80 90 100 110 120', '10 15 22 33 47 68', '10 11 12 13 15 16 18 20 22 24 27 30'],
  'E12 มี 12 ค่าต่อหนึ่งทศนิยม ใช้กับค่าคลาดเคลื่อน ± 10% ส่วน 10 15 22 33 47 68 คือ E6'),
 ('ทำไมค่ามาตรฐาน E-series จึงไม่เป็นเลขกลม ๆ เช่น 10 20 30',
  ['เพราะเลือกค่าให้ช่วงคลาดเคลื่อนของค่าที่อยู่ติดกันต่อกันพอดีในสเกลลอการิทึม', 'เพราะผลิตเลขกลมไม่ได้', 'เพราะเลขกลมแพงกว่า', 'เพราะเป็นค่าที่สุ่มเลือกมา'],
  'ค่าใน E-series เพิ่มขึ้นด้วยอัตราส่วนคงที่ (ราก 12 ของ 10 สำหรับ E12) ช่วง ± 10% ของแต่ละค่าจึงครอบคลุมทุกค่าความต้านทานโดยไม่มีช่องว่าง'),
 ('คำนวณตัวต้านทาน LED ได้ 350 Ω ทำไมควรเลือก 390 Ω แทน 330 Ω',
  ['เลือกค่าที่สูงกว่า ทำให้กระแสไม่เกินที่ออกแบบ', 'เพราะ 390 Ω ราคาถูกกว่า', 'เพราะ 330 Ω ไม่มีในอนุกรม E12', 'เพราะค่าที่ต่ำกว่าทำให้ LED หรี่ลง'],
  'R ที่ต่ำกว่าค่าคำนวณทำให้กระแสสูงกว่าที่ออกแบบ เช่น 7 / 330 ≈ 21.2 mA เกิน 20 mA จึงเลือกค่ามาตรฐานที่สูงกว่า'),
 ('ตัวต้านทานพิกัด ¼ W มีกำลังสูญเสียจริง 0.2 W ควรทำอย่างไร',
  ['เปลี่ยนเป็นพิกัด ½ W ขึ้นไป เพื่อให้มีระยะเผื่ออย่างน้อย 2 เท่า', 'ใช้ต่อได้ เพราะยังไม่เกิน 0.25 W', 'เปลี่ยนเป็น ⅛ W', 'เพิ่มแรงดันจ่าย'],
  '0.2 W ใกล้พิกัด 0.25 W มาก ตัวต้านทานจะร้อนจัดและอายุสั้น แนวปฏิบัติคือเลือกพิกัดไม่น้อยกว่า 2 เท่าของกำลังจริง คือ ≥ 0.4 W จึงใช้ ½ W'),
 ('12 V ขับ LED น้ำเงิน Vf = 3.2 V ที่ 20 mA ควรเลือกค่ามาตรฐาน E12 ค่าใด',
  ['470 Ω', '390 Ω', '440 Ω', '560 Ω'],
  'R = (12 − 3.2) / 0.020 = 440 Ω ไม่มีในอนุกรม ค่า E12 ที่สูงกว่าและใกล้สุดคือ 470 Ω'),
 ('ใช้ 470 Ω กับ 12 V และ LED น้ำเงิน Vf 3.2 V กำลังที่ตกบนตัวต้านทานประมาณเท่าใด',
  ['0.165 W', '0.306 W', '0.0187 W', '1.65 W'],
  'I = 8.8 / 470 ≈ 18.7 mA และ P = I² × R ≈ 0.0187² × 470 ≈ 0.165 W ระยะเผื่อ 2 เท่าต้องการ 0.33 W จึงควรใช้ ½ W'),
 ('ตัวต้านทานแบบ 5 แถบที่แถบสุดท้ายเป็นสีน้ำตาล มักเป็นชนิดใด',
  ['ฟิล์มโลหะ ค่าคลาดเคลื่อน ± 1%', 'ฟิล์มคาร์บอน ± 5%', 'ลวดพัน ± 20%', 'ตัวต้านทานปรับค่าได้'],
  'ตัวต้านทานความแม่นยำสูงต้องการเลข 3 หลัก จึงใช้ 5 แถบ และแถบน้ำตาลคือ ± 1% ซึ่งพบมากในฟิล์มโลหะ'),
 ('ค่าใดต่อไปนี้ "ไม่มี" ในอนุกรม E12 แต่มีใน E24',
  ['51', '47', '68', '82'],
  '51 อยู่ในอนุกรม E24 (± 5%) ส่วน 47 68 82 อยู่ใน E12'),
 ('ถ้าต่อตัวต้านทาน 220 Ω สองตัวอนุกรมกัน ความต้านทานรวมเท่าใด',
  ['440 Ω', '110 Ω', '220 Ω', '48.4 kΩ'],
  'อนุกรมนำค่ามาบวกกัน 220 + 220 = 440 Ω ใช้เทคนิคนี้เมื่อต้องการค่าที่ไม่มีในอนุกรมมาตรฐาน'),
 ('ถ้าต่อตัวต้านทาน 1 kΩ สองตัวขนานกัน ความต้านทานรวมเท่าใด',
  ['500 Ω', '2 kΩ', '1 kΩ', '250 Ω'],
  'ตัวต้านทานค่าเท่ากัน n ตัวต่อขนาน ได้ R / n = 1,000 / 2 = 500 Ω'),
 ('การปัดค่าตัวต้านทานจำกัดกระแส LED ขึ้นเป็นค่ามาตรฐาน มีผลต่อกระแสอย่างไร',
  ['กระแสลดลงเล็กน้อยจากค่าที่ออกแบบ', 'กระแสเพิ่มขึ้นเล็กน้อย', 'กระแสเท่าเดิมทุกกรณี', 'LED จะไม่ติด'],
  'R จริงสูงกว่าค่าคำนวณ กระแส I = (Vs − Vf) / R จึงต่ำกว่าที่ออกแบบเล็กน้อย ซึ่งเป็นด้านที่ปลอดภัย'),
]

STAR = star_table([
 ('CITY ARCHITECT', 'อ่านรหัสสีและเลือกตัวต้านทานได้ถูกต้องทุกขั้น พร้อมออกแบบวงจรจริงแล้ว'),
 ('BAND READER', 'เกือบเต็ม ทบทวนข้อที่พลาดแล้วลองห้องทดลองหอค่ามาตรฐานอีกรอบ'),
 ('OHM WALKER', 'ผ่านเกณฑ์แล้ว ฝึกอ่านแถบสีให้เร็วขึ้นในห้องทดลองถนนสายสี'),
 ('COLOR ROOKIE', 'เริ่มจับหลักได้ ทบทวนตารางสีและสูตร R = (Vs − Vf) / I'),
 ('NEW RESIDENT', 'มีพื้นฐานบ้างแล้ว เล่นให้ครบทั้ง 3 ย่านแล้วกลับมาทดสอบอีกครั้ง'),
 ('CITY VISITOR', 'ยังไม่คุ้นเนื้อหา เริ่มจากลานโอห์ม อ่านการ์ดทีละใบ แล้วเล่นแท่นทดสอบ LED'),
])

BADGES = r"""[
  {id:'perfect',  name:'CITY ARCHITECT', desc:'Posttest ถูกครบ 6 ข้อ',               test:s => s.post === 6},
  {id:'zero2hero',name:'BAND BOOSTER',   desc:'คะแนนเพิ่มขึ้น 3 ข้อขึ้นไปจาก Pretest',  test:s => (s.post - s.pre) >= 3},
  {id:'fast',     name:'QUICK DECODER',  desc:'ตอบถูกภายใน 8 วินาที',                test:s => s.fastCorrect},
  {id:'labrat',   name:'BENCH BUILDER',  desc:'เล่นห้องทดลองครบทั้งสามย่าน',          test:s => s.labs.lab1.length >= 3 && s.labs.lab2.length >= 3 && s.labs.lab3.length >= 1},
  {id:'combo',    name:'COLOR COMBO',    desc:'ตอบถูกติดกัน 5 ข้อขึ้นไป',            test:s => s.maxCombo >= 5},
  {id:'sweep',    name:'FULL BLOCK',     desc:'ได้ 2/2 ครบทั้งสามย่าน',              test:s => s.postByD.district1 === 2 && s.postByD.district2 === 2 && s.postByD.district3 === 2}
]"""

ADVICE = r"""
  const tips=[];
  if(labCount('lab1')<3) tips.push('ในแท่นทดสอบ LED หาให้เจอทั้งสถานะหรี่ ปกติ และเกินพิกัด แล้วสังเกตว่า R เปลี่ยนกระแสอย่างไร');
  if(labCount('lab2')<3) tips.push('ในถนนสายสี กด "โจทย์ใหม่" แล้วตั้งสีให้ถูกอย่างน้อย 3 โจทย์ เพื่อฝึกอ่านย้อนกลับจากค่าเป็นสี');
  if(labCount('lab3')<1) tips.push('ในหอค่ามาตรฐาน ทำงานเลือก R และพิกัดวัตต์ให้ผ่านอย่างน้อย 1 งาน');
  if(postInfo.stars===6) tips.push('ได้ครบ 6 ดาวแล้ว ไปต่อโซน 2 LUMEN STATION เพื่อใช้ตัวต้านทานในวงจรแบ่งแรงดัน');
  return tips;
"""

CFG = {
    'filename': 'game1_resistor_city.html',
    'title': 'RESISTOR CITY : เมืองตัวต้านทาน',
    'brand': 'RESISTOR CITY',
    'edition': 'CITY EDITION',
    'desc': 'เกมบทเรียน GNR2022 โซน 1: กฎของโอห์ม ตัวต้านทานจำกัดกระแส LED รหัสแถบสี 4 และ 5 แถบ ค่ามาตรฐาน E-series และพิกัดวัตต์',
    'ogdesc': 'เดินผ่าน 3 ย่านของเมืองตัวต้านทาน จากกฎของโอห์ม สู่การอ่านแถบสี จนเลือกตัวต้านทานที่หาซื้อได้จริง',
    'favicon': "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='18' fill='%230f0a14'/><rect x='14' y='34' width='72' height='32' rx='14' fill='%23d6b48a'/><rect x='28' y='34' width='8' height='32' fill='%23facc15'/><rect x='42' y='34' width='8' height='32' fill='%238b5cf6'/><rect x='56' y='34' width='8' height='32' fill='%23f97316'/><rect x='72' y='34' width='6' height='32' fill='%23c9a227'/></svg>",
    'theme': THEME,
    'extra_css': EXTRA_CSS,
    'arcade_label': 'ด่านไต่ตึกเมืองตัวต้านทาน',
    'hero_svg': HERO,
    'subtitle': 'สวมบทบาท <b>นักวางผังเมืองวงจร</b> เดินผ่าน 3 ย่าน ตั้งแต่ลานโอห์มที่คำนวณกระแสให้ LED ถนนสายสีที่ถอดรหัสตัวต้านทาน จนถึงหอค่ามาตรฐานที่เลือกตัวต้านทานที่หาซื้อได้จริง',
    'login_tag': 'City Planner Registration',
    'features': '<span>S1 · โซน 1</span><span>OHM · COLOR CODE · E12</span><span>PRETEST / POSTTEST</span><span>ระบบดาว 6 ดวง</span>',
    'climb_text': 'ตัวละครไต่ตึกขึ้น 1 ชั้น ทันที',
    'zones_html': ZONES,
    'checks': [('Block 01', 'ลานโอห์ม'), ('Block 02', 'ถนนสายสี'), ('Block 03', 'หอค่ามาตรฐาน')],
    'post_desc': '6 ข้อใหม่ (ย่านละ 2 ข้อ) เพื่อวัดความเข้าใจหลังเดินครบทั้ง 3 ย่าน',
    'report_tag': 'City Report',
    'course': COURSE,
    'footer_line': 'Season 1 · โซน 1 กฎของโอห์ม รหัสแถบสี และการเลือกตัวต้านทาน — ภาคเรียนที่ 1/2569',
    'bank': bank_js(B),
    'skill_labels': "{district1:'กฎของโอห์มและ LED', district2:'รหัสแถบสี', district3:'ค่ามาตรฐานและพิกัดวัตต์'}",
    'skey': 'gnr2022_resistorcity_v1_state',
    'star_table': STAR,
    'navstops': navstops('B1 OHM', 'B2 COLOR', 'B3 E12'),
    'lock_msg': 'ย่านนี้ยังไม่เปิด เดินตามลำดับก่อนนะครับ',
    'act': {'floor': 'ชั้น', 'top': 'ดาดฟ้าตึก', 'ground': 'ถนนหน้าเมือง', 'theme': 'city'},
    'pre_sub': 'นี่คือเส้นฐานของคุณ เดินครบ 3 ย่านแล้วเรามาวัดกันใหม่',
    'go_first': 'เข้าย่านแรก',
    'lab_js': LAB_JS,
    'lab_wiring': LAB_WIRING,
    'init_extra': INIT_EXTRA,
    'badges': BADGES,
    'advice_js': ADVICE,
    'role': 'นักวางผังเมืองวงจร',
    'filekey': 'GNR2022_Z1_resistorcity',
    'avatars': avatars('#140c1c', ['#f97316', '#a855f7', '#facc15', '#ef4444', '#fdba74', '#d8b4fe']),
}
