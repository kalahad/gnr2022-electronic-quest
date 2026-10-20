# -*- coding: utf-8 -*-
"""SEASON 1 · ZONE 6 — NIGHT MELODY (ด่านบอส Season 1) : วงจรเพลงยามค่ำ
GNR2022 อิเล็กทรอนิกส์พื้นฐาน ภาค 1/2569 · ทบทวนข้อสอบกลางภาคข้อ 72 (ห้องได้เฉลี่ย 18%)
อ้างอิงเอกสาร LAB "โครงงานเซนเซอร์และทรานสดิวเซอร์": โครงงานที่ 3 (รีดสวิตช์ + UM66) รูปที่ 3 และโครงงานที่ 6 (LDR) รูปที่ 6"""
from cpe_common import *

THEME = {
    "PRIMARY_RGB": "167,139,250", "PRIMARY_HEX": "#a78bfa",
    "SECOND_RGB":  "45,212,191",  "SECOND_HEX":  "#2dd4bf",
    "GOLD_RGB":    "250,204,21",  "GOLD_HEX":    "#facc15",
    "GOLD2_RGB":   "254,240,138", "GOLD2_HEX":   "#fef08a",
    "RED_RGB":     "251,113,133", "RED_HEX":     "#fb7185",
    "BG_RGB":      "7,10,30",     "BG_HEX":      "#070a1e",
    "PANEL_RGB":   "17,22,56",
    "PANEL2_RGB":  "24,31,74",
    "BG2_HEX":     "#0b1030",
    "INK_HEX":     "#0e1438",
    "TEXT_HEX":    "#eef0ff",
    "MUTED_HEX":   "#a8afd8",
    "MUTED2_HEX":  "#6f77a8",
    "MUTED3_HEX":  "#5d6596",
    "SECOND2_HEX": "#5eead4",
    "PRIM2_HEX":   "#c4b5fd",
    "LIGHT_EMBER": "#6d28d9", "LIGHT_CORNER": "#0f766e", "LIGHT_GOLD": "#a16207",
    "LIGHT_GOLD2": "#854d0e", "LIGHT_RED": "#be123c",
}

EXTRA_CSS = LAB_CSS + """
.ledlamp{width:46px;height:46px;border-radius:50%;border:2px solid var(--line);background:rgba(var(--ink-panel-rgb),.8);transition:.25s;flex:none}
.ledlamp.on{background:var(--gold);box-shadow:0 0 calc(6px + 26px*var(--lv,1)) var(--gold)}
.chain{display:flex;flex-wrap:wrap;gap:6px;align-items:stretch;margin:10px 0}
.chain .lk{flex:1 1 110px;padding:9px 10px;border-radius:12px;border:1px solid var(--line);background:rgba(var(--panel-rgb),.55);font-size:.82rem;line-height:1.35}
.chain .lk b{display:block;font-family:var(--mono);font-size:.7rem;color:var(--muted);margin-bottom:3px}
.chain .lk.hi{border-color:var(--corner);box-shadow:0 0 0 2px rgba(var(--second-rgb),.25)}
.chain .lk.lo{border-color:var(--red)}
.notes{font-size:1.6rem;min-height:34px;color:var(--gold);letter-spacing:4px}
.notes.play i{display:inline-block;animation:nb .6s ease-in-out infinite alternate;font-style:normal}
.notes.play i:nth-child(2){animation-delay:.15s}.notes.play i:nth-child(3){animation-delay:.3s}
@keyframes nb{from{transform:translateY(0)}to{transform:translateY(-8px)}}
.order{display:flex;flex-wrap:wrap;gap:6px;min-height:40px;padding:8px;border-radius:12px;border:1px dashed var(--line)}
.order span{padding:4px 10px;border-radius:9px;background:var(--ember-dim);font-size:.82rem}
"""

HERO = """<svg class="cityart" viewBox="0 0 480 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="ภาพเมืองยามค่ำที่มี LDR ทรานซิสเตอร์ และโน้ตเพลงลอยขึ้น">
  <defs>
    <radialGradient id="gMoon" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="rgba(250,204,21,.55)"/><stop offset="100%" stop-color="rgba(250,204,21,0)"/></radialGradient>
    <filter id="fGlow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect x="0" y="0" width="480" height="300" rx="18" fill="#070a1e"/>
  <circle cx="380" cy="70" r="70" fill="url(#gMoon)"/><circle cx="380" cy="70" r="26" fill="#fef08a"/><circle cx="392" cy="62" r="24" fill="#070a1e"/>
  <g fill="#eef0ff" opacity=".7"><circle cx="60" cy="40" r="1.6"/><circle cx="130" cy="70" r="1.2"/><circle cx="210" cy="30" r="1.5"/><circle cx="300" cy="110" r="1.2"/><circle cx="440" cy="150" r="1.4"/></g>
  <path d="M0 230 h60 v-40 h40 v40 h30 v-70 h50 v70 h40 v-30 h50 v30 h60 v-55 h45 v55 h105 v70 H0z" fill="#111638"/>
  <g stroke="#2dd4bf" stroke-width="2.4" fill="none">
    <path d="M70 262 H150 M190 262 H280 M320 262 H420"/>
  </g>
  <g filter="url(#fGlow)">
    <circle cx="170" cy="262" r="18" fill="none" stroke="#fb7185" stroke-width="3"/><path d="M160 252 l20 20" stroke="#fb7185" stroke-width="3"/>
    <path d="M152 236 l8 8 M162 230 l6 9" stroke="#facc15" stroke-width="2"/>
    <circle cx="300" cy="262" r="18" fill="none" stroke="#a78bfa" stroke-width="3"/><path d="M292 252 v20 M292 262 h-10 M292 256 l12 -8 M292 268 l12 8" stroke="#a78bfa" stroke-width="3" fill="none"/>
    <path d="M440 250 l14 -8 v40 l-14 -8 z" fill="#2dd4bf"/>
  </g>
  <g fill="#facc15" filter="url(#fGlow)" font-size="26" font-family="serif">
    <text x="452" y="226">&#9834;</text><text x="420" y="196">&#9835;</text><text x="455" y="170">&#9834;</text>
  </g>
  <text x="240" y="292" text-anchor="middle" font-size="10" letter-spacing="3" fill="#a8afd8">SENSE · SWITCH · SING</text>
</svg>"""

ZONES = """
<!-- ===== PREVIEW 1 ===== -->
<section id="scr-preview1" class="screen">
  <div class="panel">
    <span class="tag">Night Gate 01</span>
    <h2>กำลังจะเข้าสู่: ประตู 1 ดวงตาแห่งแสง (LDR และวงจรแบ่งแรงดัน)</h2>
    <div class="dcard">
      <div class="ico"><svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
        <circle cx="40" cy="42" r="20" fill="none" stroke="#fb7185" stroke-width="4"/><path d="M28 30 l24 24" stroke="#fb7185" stroke-width="4"/>
        <path d="M14 12 l10 10 M26 6 l6 12" stroke="#facc15" stroke-width="3"/></svg></div>
      <div><div class="skillcard" style="margin:0">
        <div class="sk-name">ทักษะที่จะได้: อ่านพฤติกรรม LDR และคำนวณแรงดันขาออกของวงจรแบ่งแรงดัน</div>
        <p class="muted" style="margin:6px 0 0">มืดแล้วความต้านทานเพิ่ม แรงดันที่จุดกึ่งกลางจะขึ้นหรือลง ขึ้นกับว่า LDR อยู่ด้านบนหรือด้านล่าง</p>
      </div></div>
    </div>
    <div class="btn-row"><button class="btn primary" data-goto="scr-lesson1">เปิดประตู</button></div>
  </div>
</section>

<!-- ===== GATE 1 ===== -->
<section id="scr-lesson1" class="screen">
  <div class="panel">
    <span class="tag">Gate 01 · Light Eye</span>
    <h2>ประตู 1: LDR และวงจรแบ่งแรงดัน</h2>
    <p><b>LDR (Light Dependent Resistor)</b> ทำจากสารแคดเมียมซัลไฟด์ (CdS) ความต้านทานจะ <b>ลดลงเมื่อแสงมากขึ้น</b>
      ในที่สว่างอาจเหลือราวหลัก kΩ และในที่มืดสูงขึ้นถึงหลักร้อย kΩ จนถึงราว 1 MΩ (ขึ้นกับรุ่น)
      LDR ไม่ได้สร้างแรงดันเอง วงจรจึงต้องต่อ LDR เป็น <b>วงจรแบ่งแรงดัน</b> กับตัวต้านทานอีกตัว เพื่อแปลงความต้านทานที่เปลี่ยนไปเป็นแรงดันที่วัดได้</p>
    <div class="divfig">  +Vs ──[ R บน ]──┬── Vout
                   │
                [ R ล่าง ]
                   │
                  GND

  Vout = Vs × R ล่าง / (R บน + R ล่าง)</div>
    <div class="tbl-wrap"><table>
      <tr><th>ตำแหน่ง LDR</th><th>เมื่อมืดลง (LDR สูงขึ้น)</th><th>ใช้กับงาน</th></tr>
      <tr><td>ด้านล่าง (ระหว่าง Vout กับ GND)</td><td>Vout สูงขึ้น</td><td>เปิดไฟหรือส่งเสียงเมื่อมืด (โครงงานที่ 6)</td></tr>
      <tr><td>ด้านบน (ระหว่าง +Vs กับ Vout)</td><td>Vout ต่ำลง</td><td>ทำงานเมื่อสว่าง เช่น เตือนประตูตู้เย็นเปิด</td></tr>
      <tr><td>ใช้ VR แทน R คงที่</td><td>เลื่อนจุดที่วงจรเริ่มทำงาน</td><td>ปรับความไวให้เหมาะกับห้องจริง</td></tr>
    </table></div>
    <div class="codebox">ตัวอย่าง: Vs = 9 V, R บน = 10 kΩ, LDR ด้านล่าง
  สว่าง LDR = 1 kΩ    → Vout = 9 × 1 / (10 + 1)   ≈ 0.82 V
  มืด   LDR = 100 kΩ  → Vout = 9 × 100 / (10 + 100) ≈ 8.18 V</div>
    <div class="keyfact">จำให้ขึ้นใจ: <b>มืด = LDR สูง</b> · LDR อยู่ด้านล่าง มืดแล้ว Vout สูง · LDR อยู่ด้านบน มืดแล้ว Vout ต่ำ</div>

    <h3 style="margin-top:18px">ห้องทดลอง: เครื่องวัดแสงด้วย LDR</h3>
    <p class="muted">เลื่อนระดับแสง สลับตำแหน่ง LDR และเปลี่ยน R คงที่ แล้วดูว่า Vout ขึ้นหรือลง (แหล่งจ่าย 9 V) ลองให้ครบทั้งมืดและสว่างในทั้งสองตำแหน่ง</p>
    <input type="range" class="rng" id="ldrL" min="0" max="100" value="70" aria-label="ระดับแสง">
    <div class="labrow">
      <button class="toggle on" id="ldrPos">LDR ด้านล่าง</button>
      <button class="btn sm" data-ldrr="10000">R = 10 kΩ</button><button class="btn sm" data-ldrr="47000">R = 47 kΩ</button>
    </div>
    <div class="labrow"><span class="readout" id="ldrR">—</span><span class="readout" id="ldrV">—</span></div>
    <div class="meter"><i id="ldrBar"></i></div>
    <div class="status-line" id="ldrStatus">เลื่อนแถบเพื่อเปลี่ยนระดับแสง</div>
    <div class="btn-row"><button class="btn primary" data-quiz="check1">ไปทำแบบฝึกหัดด่านนี้</button></div>
  </div>
</section>

<!-- ===== PREVIEW 2 ===== -->
<section id="scr-preview2" class="screen">
  <div class="panel">
    <span class="tag">Night Gate 02</span>
    <h2>กำลังจะเข้าสู่: ประตู 2 สวิตช์ไร้หน้าสัมผัส (ทรานซิสเตอร์)</h2>
    <div class="dcard">
      <div class="ico"><svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
        <circle cx="42" cy="40" r="24" fill="none" stroke="#a78bfa" stroke-width="4"/><path d="M34 26 v28 M18 40 h16 M34 34 l18 -12 M34 46 l18 12" stroke="#a78bfa" stroke-width="4" fill="none"/>
        <path d="M46 54 l6 4 l-7 2" fill="#2dd4bf"/></svg></div>
      <div><div class="skillcard" style="margin:0">
        <div class="sk-name">ทักษะที่จะได้: ใช้ทรานซิสเตอร์ NPN เป็นสวิตช์ และคำนวณ IB, IC, IE</div>
        <p class="muted" style="margin:6px 0 0">วิเคราะห์วงจรหรี่ไฟอัตโนมัติ (โครงงานที่ 6 รูปที่ 6) ที่ใช้ LDR ขับทรานซิสเตอร์</p>
      </div></div>
    </div>
    <div class="btn-row"><button class="btn primary" data-goto="scr-lesson2">เปิดประตู</button></div>
  </div>
</section>

<!-- ===== GATE 2 ===== -->
<section id="scr-lesson2" class="screen">
  <div class="panel">
    <span class="tag">Gate 02 · Silent Switch</span>
    <h2>ประตู 2: ทรานซิสเตอร์เป็นสวิตช์</h2>
    <p>ทรานซิสเตอร์ BJT ชนิด <b>NPN</b> มี 3 ขา คือ <b>เบส (B) คอลเล็กเตอร์ (C) อิมิตเตอร์ (E)</b>
      กระแสเบสเล็ก ๆ ควบคุมกระแสคอลเล็กเตอร์ที่ใหญ่กว่าได้ ทรานซิสเตอร์ซิลิคอนเริ่มนำเมื่อ <b>VBE ≈ 0.7 V</b>
      ในงานสวิตช์ เราใช้เพียง 2 สถานะ คือ <b>คัตออฟ (OFF)</b> และ <b>อิ่มตัว (ON เต็มที่)</b></p>
    <div class="codebox">IC = β × IB          IE = IB + IC
ตัวอย่าง: β = 100, IB = 40 µA → IC = 4 mA, IE = 4.04 mA
ตัวต้านทานเบส: RB = (Vขับ − 0.7) / IB
LED ที่ขา C เมื่ออิ่มตัว: IC ≈ (9 − VF − VCE(sat)) / R = (9 − 2 − 0.2) / 330 ≈ 20.6 mA</div>
    <div class="tbl-wrap"><table>
      <tr><th>ย่านทำงาน</th><th>เงื่อนไข</th><th>หน้าที่</th></tr>
      <tr><td>คัตออฟ (Cut-off)</td><td>VBE &lt; 0.7 V แทบไม่มี IB</td><td>สวิตช์ OFF โหลดไม่ทำงาน</td></tr>
      <tr><td>แอกทีฟ (Active)</td><td>IC = β × IB ยังไม่ถึงค่าสูงสุดของวงจร</td><td>ขยายสัญญาณ (LED หรี่ ๆ)</td></tr>
      <tr><td>อิ่มตัว (Saturation)</td><td>IB มากพอจน IC ถูกจำกัดด้วยโหลด VCE ≈ 0.2 V</td><td>สวิตช์ ON โหลดทำงานเต็มที่</td></tr>
    </table></div>
    <div class="divfig">  โครงงานที่ 6 (รูปที่ 6 วงจรหรี่ไฟอัตโนมัติ)
  +9V ─[R2 24k]─[VR2 10k]─┬── B (Q1)      +9V ─[R3 330]─[LED2]─ C (Q1)
                          │                                     E ── GND
                        [LDR]
                          │
                         GND
  มืด → LDR สูง → VB ขึ้นถึง 0.7 V → Q1 นำ → LED2 สว่าง</div>
    <div class="keyfact">จำให้ขึ้นใจ: <b>VBE ≥ 0.7 V = ทรานซิสเตอร์นำ</b> · เพิ่ม VR2 = ต้องมืดกว่าเดิมจึงทำงาน · ลด VR2 = ทำงานเร็วขึ้น</div>

    <h3 style="margin-top:18px">ห้องทดลอง: วงจรหรี่ไฟอัตโนมัติ (โครงงานที่ 6)</h3>
    <p class="muted">แถบบนคือระดับแสง แถบล่างคือ VR2 ดูแรงดันเบสกับกระแส LED แล้วหาให้ครบทั้ง 3 ย่าน: OFF, หรี่, สว่างเต็มที่</p>
    <label class="muted" for="q6L" style="display:block;font-size:.85rem">ระดับแสง: <b id="q6Lt">80%</b></label>
    <input type="range" class="rng" id="q6L" min="0" max="100" value="80" aria-label="ระดับแสง">
    <label class="muted" for="q6V" style="display:block;font-size:.85rem">VR2: <b id="q6Vt">5 kΩ</b> (R ด้านบนรวม = 24 kΩ + VR2)</label>
    <input type="range" class="rng" id="q6V" min="0" max="10000" step="500" value="5000" aria-label="ค่า VR2">
    <div class="labrow"><span class="ledlamp" id="q6Led"></span><span class="readout" id="q6VB">—</span><span class="readout" id="q6IC">—</span></div>
    <div class="status-line" id="q6Status">เลื่อนแถบเพื่อเริ่มทดลอง</div>
    <div class="btn-row"><button class="btn primary" data-quiz="check2">ไปทำแบบฝึกหัดด่านนี้</button></div>
  </div>
</section>

<!-- ===== PREVIEW 3 ===== -->
<section id="scr-preview3" class="screen">
  <div class="panel">
    <span class="tag">Night Gate 03</span>
    <h2>กำลังจะเข้าสู่: ประตู 3 เพลงยามค่ำ (ประกอบระบบ ข้อ 72)</h2>
    <div class="dcard">
      <div class="ico"><svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
        <rect x="8" y="30" width="16" height="20" rx="3" fill="#fb7185"/><rect x="32" y="30" width="16" height="20" rx="3" fill="#a78bfa"/>
        <path d="M58 32 l12 -8 v32 l-12 -8z" fill="#2dd4bf"/><path d="M24 40 h8 M48 40 h10" stroke="#facc15" stroke-width="3"/></svg></div>
      <div><div class="skillcard" style="margin:0">
        <div class="sk-name">ทักษะที่จะได้: ต่อ 2 วงจรใน LAB ให้เป็นระบบ "ส่งเสียงเพลงเมื่อมืด" และตอบข้อเขียนให้ได้คะแนน</div>
        <p class="muted" style="margin:6px 0 0">นำทรานซิสเตอร์ของโครงงานที่ 6 มาทำหน้าที่แทนรีดสวิตช์ในโครงงานที่ 3</p>
      </div></div>
    </div>
    <div class="btn-row"><button class="btn primary" data-goto="scr-lesson3">เปิดประตู</button></div>
  </div>
</section>

<!-- ===== GATE 3 ===== -->
<section id="scr-lesson3" class="screen">
  <div class="panel">
    <span class="tag">Gate 03 · Night Melody</span>
    <h2>ประตู 3: ประกอบระบบเพลงยามค่ำ</h2>
    <p>ในโครงงานที่ 3 (รูปที่ 3) R1 10 kΩ ดึงขา 1 ของไอซีเสียงเพลงขึ้นไปทางไฟบวก ไอซีจึงเงียบ
      เมื่อรีดสวิตช์ S1 ต่อวงจร ขา 1 ถูกดึง <b>ลงกราวด์</b> ไอซีจึงสร้างเพลงออกทางขา 3 ผ่าน R2 ไปให้ Q1 (C9013) ขยายขับลำโพง
      ถ้าต้องการให้เพลงดัง <b>เมื่อมืด</b> ก็นำ <b>ทรานซิสเตอร์ของโครงงานที่ 6</b> มาทำหน้าที่แทน S1 โดยต่อขา C เข้าจุดเดียวกับขา 1 และขา E ลงกราวด์</p>
    <div class="tbl-wrap"><table>
      <tr><th>บล็อก</th><th>อุปกรณ์ (จาก LAB)</th><th>หน้าที่</th></tr>
      <tr><td>1 ตัวรับรู้</td><td>LDR + R2 24 kΩ + VR2 10 kΩ</td><td>แปลงความมืดเป็นแรงดันที่เบส</td></tr>
      <tr><td>2 สวิตช์</td><td>ทรานซิสเตอร์ NPN (แทนรีดสวิตช์ S1)</td><td>มืดแล้วนำ ดึงขา 1 ลงกราวด์</td></tr>
      <tr><td>3 กำเนิดเพลง</td><td>ไอซีเสียงเพลง UM66 + R1 10 kΩ</td><td>สร้างเพลงเมื่อขา 1 ถูกดึงลงกราวด์</td></tr>
      <tr><td>4 ขยายและเอาต์พุต</td><td>R2 2 kΩ + Q1 C9013 + R3 330 Ω + ลำโพง</td><td>ขยายสัญญาณให้แรงพอขับลำโพง</td></tr>
      <tr><td>5 แหล่งจ่าย</td><td>แบตเตอรี่ 9 V + C1 100 µF + IC1 7805</td><td>จ่ายไฟให้ไอซีอย่างคงที่</td></tr>
    </table></div>
    <div class="codebox">สูตรตอบข้อเขียนออกแบบวงจร 4 ขั้น
  1) วาดบล็อกไดอะแกรม: ตัวรับรู้ → สวิตช์ → เอาต์พุต
  2) วาดวงจรพร้อมค่าอุปกรณ์ทุกตัว
  3) อธิบายทีละสถานะ: สว่าง ... / มืด ...
  4) ตรวจหน่วยและขั้วอุปกรณ์ (LED, ตัวเก็บประจุ, ขา B C E)</div>
    <div class="keyfact">จำให้ขึ้นใจ: <b>ข้อ 72 = โครงงานที่ 6 + โครงงานที่ 3</b> · มืด → ทรานซิสเตอร์นำ → ขา 1 ลงกราวด์ → เพลงดัง</div>

    <h3 style="margin-top:18px">ห้องทดลอง: ประกอบระบบเพลงยามค่ำ</h3>
    <p class="muted">เลือกสวิตช์ที่จะใช้ แล้วสลับสว่าง/มืด (หรือนำแม่เหล็กเข้าใกล้รีดสวิตช์) ดูสถานะทุกบล็อกตั้งแต่ตัวรับรู้จนถึงลำโพง</p>
    <div class="labrow">
      <button class="btn sm" data-sw="reed">ใช้รีดสวิตช์ (โครงงาน 3)</button><button class="btn sm" data-sw="bjt">ใช้ LDR + ทรานซิสเตอร์ (ข้อ 72)</button>
      <button class="toggle on" id="sysDark">สว่าง</button><button class="toggle on" id="sysMag">แม่เหล็กอยู่ไกล</button>
    </div>
    <div class="chain" id="sysChain"></div>
    <div class="notes" id="sysNotes" aria-live="polite"></div>
    <div class="status-line" id="sysStatus">สลับสว่าง/มืด เพื่อดูการทำงานของแต่ละบล็อก</div>
    <h3 style="margin-top:14px">ห้องทดลอง: เรียงบล็อกให้ถูกลำดับ</h3>
    <p class="muted">แตะบล็อกตามลำดับการไหลของสัญญาณจากซ้ายไปขวา</p>
    <div class="labrow">
      <button class="btn sm" data-blk="3">ไอซีเสียงเพลง</button><button class="btn sm" data-blk="5">ลำโพง</button>
      <button class="btn sm" data-blk="1">LDR แบ่งแรงดัน</button><button class="btn sm" data-blk="4">C9013 ขยาย</button>
      <button class="btn sm" data-blk="2">ทรานซิสเตอร์สวิตช์</button><button class="btn sm" id="blkReset">เริ่มเรียงใหม่</button>
    </div>
    <div class="order" id="blkOrder"></div>
    <div class="status-line" id="blkStatus">ยังไม่ได้เรียง</div>
    <div class="btn-row"><button class="btn primary" data-quiz="check3">ไปทำแบบฝึกหัดด่านนี้</button></div>
  </div>
</section>
"""

LAB_JS = r"""
/* ---- LAB 1: LDR light meter ---- */
let ldrBottom=true, ldrRf=10000;
function ldrRes(L){ return Math.pow(10, 6 - 3*L/100); }      /* 0% = 1 MΩ (มืด) · 100% = 1 kΩ (สว่าง) */
function fmtOhm(r){ return r>=1e6?(r/1e6).toFixed(2)+' MΩ':r>=1000?(r/1000).toFixed(r>=1e5?0:1)+' kΩ':Math.round(r)+' Ω'; }
function ldrUpdate(user){
  const L=+$('#ldrL').value, R=ldrRes(L), top=ldrBottom?ldrRf:R, bot=ldrBottom?R:ldrRf, v=9*bot/(top+bot);
  $('#ldrR').innerHTML='LDR '+fmtOhm(R)+'<small>แสง '+L+'%</small>';
  $('#ldrV').innerHTML=v.toFixed(2)+'<small>V</small>'; $('#ldrBar').style.width=(v/9*100)+'%';
  const dark=L<30, bright=L>70, st=$('#ldrStatus');
  st.className='status-line'+(v>4.5?' ok':'');
  st.innerHTML=(dark?'<b>มืด</b>':bright?'<b>สว่าง</b>':'<b>สลัว</b>')+' · LDR '+(ldrBottom?'ด้านล่าง':'ด้านบน')+' · Vout = 9 × '+fmtOhm(bot)+' / ('+fmtOhm(top)+' + '+fmtOhm(bot)+') = <b>'+v.toFixed(2)+' V</b>'
    +(v>=0.7?' — ถ้าต่อจุดนี้เข้าเบส ทรานซิสเตอร์จะนำ':' — ต่ำกว่า 0.7 V ทรานซิสเตอร์จะไม่นำ');
  if(user&&(dark||bright)) markLab('lab1',(ldrBottom?'b':'t')+(dark?'D':'B')+ldrRf,3);
}
/* ---- LAB 2: Project 6 auto light ---- */
function q6Update(user){
  const L=+$('#q6L').value, RL=ldrRes(L), Rt=24000+(+$('#q6V').value), beta=150;
  const Vth=9*RL/(Rt+RL), Rth=Rt*RL/(Rt+RL), IB=Math.max(0,(Vth-0.7)/Rth), ICsat=(9-2-0.2)/330, IC=Math.min(beta*IB,ICsat);
  $('#q6Lt').textContent=L+'%'; $('#q6Vt').textContent=(+$('#q6V').value/1000)+' kΩ';
  const VB=IB>0?0.7:Vth, lv=IC/ICsat, lamp=$('#q6Led');
  lamp.classList.toggle('on',lv>0.02); lamp.style.setProperty('--lv',lv.toFixed(2)); lamp.style.opacity=(0.35+0.65*Math.min(1,lv*1.3)).toFixed(2);
  $('#q6VB').innerHTML='VB '+VB.toFixed(2)+'<small>V</small>'; $('#q6IC').innerHTML='I LED '+(IC*1000).toFixed(1)+'<small>mA</small>';
  let k, st=$('#q6Status');
  if(IB<=0){k='off';st.className='status-line';st.innerHTML='<b>คัตออฟ (OFF)</b> — แรงดันเบสยังไม่ถึง 0.7 V (Vth = '+Vth.toFixed(2)+' V) LED2 ดับ ลองทำให้มืดลง หรือลด VR2';}
  else if(beta*IB<ICsat){k='act';st.className='status-line ok';st.innerHTML='<b>แอกทีฟ (หรี่)</b> — IB = '+(IB*1e6).toFixed(1)+' µA → IC = β × IB = '+(IC*1000).toFixed(1)+' mA ยังไม่ถึง '+(ICsat*1000).toFixed(1)+' mA LED2 สว่างไม่เต็มที่';}
  else {k='sat';st.className='status-line ok';st.innerHTML='<b>อิ่มตัว (ON เต็มที่)</b> — IC ถูกจำกัดด้วย R3: (9 − 2 − 0.2) / 330 ≈ 20.6 mA LED2 สว่างเต็มที่';}
  if(user) markLab('lab2',k+'_'+$('#q6V').value,3);
}
/* ---- LAB 3: system chain + block order ---- */
let sysSw='bjt', sysIsDark=false, sysMagNear=false, blkSeq=[];
const BLK={1:'LDR แบ่งแรงดัน',2:'ทรานซิสเตอร์สวิตช์',3:'ไอซีเสียงเพลง',4:'C9013 ขยาย',5:'ลำโพง'};
function sysUpdate(user){
  const ch=$('#sysChain'), st=$('#sysStatus'), nt=$('#sysNotes');
  if(!sysSw){ch.innerHTML='';nt.innerHTML='';return;}
  let closed, sensor;
  if(sysSw==='reed'){ closed=sysMagNear; sensor='<div class="lk '+(closed?'hi':'lo')+'"><b>S1 รีดสวิตช์</b>'+(sysMagNear?'แม่เหล็กใกล้ → หน้าสัมผัสต่อ':'แม่เหล็กไกล → หน้าสัมผัสเปิด')+'</div>'; }
  else { closed=sysIsDark; sensor='<div class="lk '+(sysIsDark?'hi':'lo')+'"><b>LDR + R2/VR2</b>'+(sysIsDark?'มืด → LDR สูง → VB ≥ 0.7 V':'สว่าง → LDR ต่ำ → VB &lt; 0.7 V')+'</div>'
          +'<div class="lk '+(closed?'hi':'lo')+'"><b>ทรานซิสเตอร์ (แทน S1)</b>'+(closed?'นำ: C–E ต่อกัน':'ไม่นำ: C–E เปิด')+'</div>'; }
  ch.innerHTML=sensor
    +'<div class="lk '+(closed?'hi':'lo')+'"><b>ขา 1 ไอซีเพลง</b>'+(closed?'ถูกดึงลงกราวด์ (≈ 0 V)':'R1 ดึงขึ้นไฟบวก')+'</div>'
    +'<div class="lk '+(closed?'hi':'lo')+'"><b>UM66 → C9013</b>'+(closed?'สร้างเพลง และขยาย':'ไม่มีสัญญาณ')+'</div>'
    +'<div class="lk '+(closed?'hi':'lo')+'"><b>ลำโพง</b>'+(closed?'ดัง':'เงียบ')+'</div>';
  nt.className='notes'+(closed?' play':''); nt.innerHTML=closed?'<i>&#9834;</i><i>&#9835;</i><i>&#9834;</i>':'';
  st.className='status-line'+(closed?' ok':'');
  st.innerHTML=sysSw==='bjt'?(sysIsDark?'<b>มืด: เพลงดัง</b> — นี่คือคำตอบข้อ 72':'<b>สว่าง: เงียบ</b> — ทรานซิสเตอร์ไม่นำ ขา 1 ถูกดึงขึ้น')
                            :(sysMagNear?'<b>แม่เหล็กใกล้: เพลงดัง</b> — โครงงานที่ 3 ตามเอกสาร LAB':'<b>แม่เหล็กไกล: เงียบ</b> — S1 เปิด ขา 1 ถูกดึงขึ้น');
  if(user){ SFX.play(closed?'fanfare':'select'); markLab('lab3',sysSw+(sysSw==='bjt'?(sysIsDark?'D':'L'):(sysMagNear?'N':'F')),3); }
}
function blkTap(n){
  if(blkSeq.indexOf(n)>=0) return;
  blkSeq.push(n); $('#blkOrder').innerHTML=blkSeq.map(k=>'<span>'+BLK[k]+'</span>').join('');
  const st=$('#blkStatus'), ok=blkSeq.every((k,i)=>k===i+1);
  if(!ok){ st.className='status-line'; st.innerHTML='ลำดับยังไม่ถูก — สัญญาณเริ่มจากตัวรับรู้ แล้วผ่านสวิตช์ก่อนถึงไอซีเพลง กด "เริ่มเรียงใหม่"'; SFX.play('wrong'); return; }
  if(blkSeq.length===5){ st.className='status-line ok'; st.innerHTML='<b>ถูกต้องทั้งหมด</b> — ตัวรับรู้ → สวิตช์ → กำเนิดเพลง → ขยาย → ลำโพง ใช้เป็นบล็อกไดอะแกรมในข้อเขียนได้ทันที'; SFX.play('fanfare'); markLab('lab3','order',5); }
  else { st.className='status-line ok'; st.innerHTML='ถูกแล้ว '+blkSeq.length+' / 5 บล็อก'; SFX.play('correct'); }
}
"""

LAB_WIRING = r"""
  const lr=e.target.closest('[data-ldrr]'); if(lr){ldrRf=+lr.dataset.ldrr;SFX.play('select');ldrUpdate(true);return;}
  if(e.target.closest('#ldrPos')){ldrBottom=!ldrBottom;const b=$('#ldrPos');b.textContent=ldrBottom?'LDR ด้านล่าง':'LDR ด้านบน';b.className='toggle '+(ldrBottom?'on':'off');SFX.play('select');ldrUpdate(true);return;}
  const sw=e.target.closest('[data-sw]'); if(sw){sysSw=sw.dataset.sw;document.querySelectorAll('[data-sw]').forEach(x=>x.classList.toggle('primary',x===sw));sysUpdate(true);return;}
  if(e.target.closest('#sysDark')){sysIsDark=!sysIsDark;const b=$('#sysDark');b.textContent=sysIsDark?'มืด':'สว่าง';b.className='toggle '+(sysIsDark?'off':'on');if(!sysSw){sysSw='bjt';}sysUpdate(true);return;}
  if(e.target.closest('#sysMag')){sysMagNear=!sysMagNear;const b=$('#sysMag');b.textContent=sysMagNear?'แม่เหล็กใกล้':'แม่เหล็กอยู่ไกล';b.className='toggle '+(sysMagNear?'off':'on');if(!sysSw){sysSw='reed';}sysUpdate(true);return;}
  const bk=e.target.closest('[data-blk]'); if(bk){blkTap(+bk.dataset.blk);return;}
  if(e.target.closest('#blkReset')){blkSeq=[];$('#blkOrder').innerHTML='';const s=$('#blkStatus');s.className='status-line';s.textContent='ยังไม่ได้เรียง';SFX.play('select');return;}
"""
INIT_EXTRA = " $('#ldrL').addEventListener('input',()=>ldrUpdate(true)); ldrUpdate(false); $('#q6L').addEventListener('input',()=>q6Update(true)); $('#q6V').addEventListener('input',()=>q6Update(true)); q6Update(false); sysUpdate(false); const _sb=document.querySelector('[data-sw=\"bjt\"]'); if(_sb) _sb.classList.add('primary');"

B = {}
B['district1'] = [
 ('เมื่อแสงที่ตกกระทบ LDR มากขึ้น ความต้านทานของ LDR จะเป็นอย่างไร',
  ['ลดลง', 'เพิ่มขึ้น', 'คงที่', 'เป็นศูนย์ทันที'],
  'LDR เป็นตัวต้านทานไวแสง แสงมากขึ้นทำให้มีพาหะอิสระมากขึ้น ความต้านทานจึงลดลง ในที่มืดความต้านทานจะสูงมาก'),
 ('LDR ทั่วไปที่ใช้ใน LAB ทำจากสารใด',
  ['แคดเมียมซัลไฟด์ (CdS)', 'ซิลิคอนชนิด N', 'ทองแดงบริสุทธิ์', 'เจอร์เมเนียมชนิด P'],
  'LDR ส่วนใหญ่เป็นตัวต้านทานแบบโฟโตคอนดักทีฟจากแคดเมียมซัลไฟด์ ซึ่งเป็นสารกึ่งตัวนำที่ไวต่อแสงช่วงที่ตามองเห็น'),
 ('วงจรแบ่งแรงดัน 9 V มี R = 10 kΩ ด้านบน และ LDR = 10 kΩ ด้านล่าง Vout เท่าใด',
  ['4.5 V', '9 V', '0 V', '0.9 V'],
  'Vout = 9 × 10 / (10 + 10) = 4.5 V เมื่อตัวต้านทานสองตัวเท่ากัน แรงดันแบ่งครึ่ง'),
 ('วงจรแบ่งแรงดัน 9 V มี R = 10 kΩ ด้านบน และ LDR ด้านล่าง ในที่มืด LDR = 100 kΩ Vout ประมาณเท่าใด',
  ['8.18 V', '0.82 V', '4.5 V', '9.9 V'],
  'Vout = 9 × 100 / (10 + 100) ≈ 8.18 V มืดแล้ว LDR สูง แรงดันที่จุดกึ่งกลางจึงสูง'),
 ('วงจรแบ่งแรงดัน 9 V มี R = 10 kΩ ด้านบน และ LDR ด้านล่าง ในที่สว่าง LDR = 1 kΩ Vout ประมาณเท่าใด',
  ['0.82 V', '8.18 V', '4.5 V', '0.09 V'],
  'Vout = 9 × 1 / (10 + 1) ≈ 0.82 V ถ้าค่าที่ได้ผิด ให้ตรวจว่าใส่ตัวต้านทานด้านล่างไว้ที่ตัวเศษหรือไม่'),
 ('ต่อ LDR ไว้ด้านล่างของวงจรแบ่งแรงดัน เมื่อห้องมืดลง Vout จะเป็นอย่างไร',
  ['สูงขึ้น', 'ต่ำลง', 'คงที่', 'กลับขั้วเป็นลบ'],
  'LDR ด้านล่างมีค่าสูงขึ้นเมื่อมืด สัดส่วน R ล่าง / (R บน + R ล่าง) จึงเพิ่มขึ้น Vout สูงขึ้น เป็นหลักการของวงจรเปิดไฟเมื่อมืด'),
 ('ต้องการให้ Vout สูงขึ้นเมื่อ "สว่าง" ควรต่อ LDR ไว้ตำแหน่งใด',
  ['ด้านบน ระหว่าง +Vs กับจุด Vout', 'ด้านล่าง ระหว่างจุด Vout กับ GND', 'ขนานกับแหล่งจ่ายโดยตรง', 'อนุกรมกับแหล่งจ่ายโดยไม่มีตัวต้านทานอื่น'],
  'สว่างแล้ว LDR ด้านบนมีค่าต่ำ แรงดันตกคร่อมด้านบนน้อย Vout จึงสูง เป็นหลักการของวงจรเตือนเมื่อมีแสง เช่น เตือนประตูตู้เย็นเปิด'),
 ('ทำไมต้องต่อ LDR เป็นวงจรแบ่งแรงดันก่อนนำไปควบคุมทรานซิสเตอร์',
  ['LDR เปลี่ยนเพียงความต้านทาน ไม่ได้สร้างแรงดัน จึงต้องใช้วงจรแบ่งแรงดันแปลงเป็นแรงดัน', 'LDR สร้างแรงดันได้เองเหมือนเซลล์แสงอาทิตย์ จึงไม่ต้องต่อเพิ่ม', 'เพื่อเปลี่ยนไฟ AC เป็น DC', 'เพื่อเพิ่มความถี่ของสัญญาณ'],
  'ทรานซิสเตอร์ต้องการแรงดันที่เบส (≈ 0.7 V) การต่อ LDR กับตัวต้านทานอีกตัวทำให้ความต้านทานที่เปลี่ยนตามแสงกลายเป็นแรงดันที่เปลี่ยนตามแสง'),
 ('สัญลักษณ์ของ LDR ในวงจรคือข้อใด',
  ['ตัวต้านทานที่มีลูกศรแสงชี้เข้าหา', 'ไดโอดที่มีลูกศรแสงชี้ออก', 'ตัวต้านทานที่มีลูกศรทแยงผ่านตัว', 'วงกลมมีขั้วบวกและลบ'],
  'ลูกศรชี้เข้าหมายถึงรับแสง ไดโอดที่มีลูกศรชี้ออกคือ LED ส่วนลูกศรทแยงผ่านตัวต้านทานคือตัวต้านทานปรับค่าได้'),
 ('การใช้ตัวต้านทานปรับค่าได้ (VR) คู่กับ LDR ในวงจรแบ่งแรงดันมีประโยชน์อย่างไร',
  ['ปรับระดับความมืดที่ทำให้วงจรเริ่มทำงาน (ปรับความไว)', 'เพิ่มอัตราขยายกระแสของทรานซิสเตอร์', 'กรองแรงดันให้เรียบ', 'เปลี่ยนไฟ AC เป็น DC'],
  'แต่ละห้องสว่างไม่เท่ากัน VR ช่วยเลื่อนจุดที่แรงดันถึงเกณฑ์ เช่น 0.7 V ที่เบส ให้วงจรทำงานตรงกับความต้องการ'),
 ('วงจรแบ่งแรงดัน 5 V มี R = 10 kΩ ด้านบน ต้องการให้ Vout = 2.5 V พอดี LDR ด้านล่างต้องมีค่าเท่าใด',
  ['10 kΩ', '5 kΩ', '20 kΩ', '2.5 kΩ'],
  'Vout เป็นครึ่งหนึ่งของ Vs เมื่อ R บน = R ล่าง จึงต้องการ LDR = 10 kΩ'),
 ('LDR ตอบสนองต่อการเปลี่ยนแสงช้าระดับหลายสิบมิลลิวินาที ข้อสรุปใดถูกต้อง',
  ['เหมาะกับงานตรวจระดับแสงทั่วไป แต่ไม่เหมาะกับการรับสัญญาณความเร็วสูง', 'เหมาะกับการรับรีโมททีวีที่ความถี่ 38 kHz', 'ตอบสนองเร็วกว่าโฟโตไดโอด', 'ใช้แทนตัวรับแสงในใยแก้วนำแสงได้ดีที่สุด'],
  'งานเปิดไฟหรือส่งเสียงเมื่อมืดไม่ต้องการความเร็ว LDR จึงเหมาะ ส่วนงานสื่อสารความเร็วสูงใช้โฟโตไดโอดหรือโฟโตทรานซิสเตอร์'),
 ('วงจรแบ่งแรงดัน 5 V มี R = 10 kΩ ด้านบน และ LDR = 40 kΩ ด้านล่าง Vout เท่าใด',
  ['4.0 V', '1.0 V', '2.5 V', '5.0 V'],
  'Vout = 5 × 40 / (10 + 40) = 4.0 V ถ้าได้ 1.0 V แสดงว่าสลับตัวต้านทานบนกับล่าง'),
]
B['district2'] = [
 ('ขาทั้งสามของทรานซิสเตอร์ BJT คือข้อใด',
  ['เบส คอลเล็กเตอร์ อิมิตเตอร์', 'เกต เดรน ซอร์ส', 'แอโนด แคโทด เกต', 'อินพุต เอาต์พุต กราวด์'],
  'BJT มีขา B C E ส่วนเกต เดรน ซอร์ส เป็นขาของ MOSFET และแอโนด แคโทด เกต เป็นขาของ SCR'),
 ('ข้อใดคือความสัมพันธ์ของกระแสใน BJT ที่ถูกต้อง',
  ['IE = IB + IC', 'IE = IB × IC', 'IE = IC − IB', 'IE = IB / IC'],
  'กระแสที่ไหลเข้าเบสและคอลเล็กเตอร์รวมกันไหลออกทางอิมิตเตอร์ตามกฎกระแสของเคอร์ชอฟฟ์'),
 ('ทรานซิสเตอร์มี β = 100 เมื่อ IB = 40 µA กระแส IC เท่าใด',
  ['4 mA', '0.4 mA', '40 mA', '4.04 mA'],
  'IC = β × IB = 100 × 40 µA = 4000 µA = 4 mA ส่วน 4.04 mA คือ IE'),
 ('กระแสเบส 75 µA กระแสคอลเล็กเตอร์ 15 mA ค่า β เท่าใด',
  ['200', '20', '2000', '0.005'],
  'β = IC / IB = 15 mA / 75 µA = 15000 µA / 75 µA = 200 ต้องแปลงหน่วยให้เท่ากันก่อนหาร'),
 ('IB = 40 µA และ IC = 4 mA กระแส IE เท่าใด',
  ['4.04 mA', '4 mA', '3.96 mA', '44 mA'],
  'IE = IB + IC = 0.04 mA + 4 mA = 4.04 mA'),
 ('ทรานซิสเตอร์ซิลิคอนชนิด NPN เริ่มนำกระแสเมื่อ VBE ประมาณเท่าใด',
  ['0.7 V', '0.3 V', '1.4 V', '5 V'],
  'รอยต่อเบส–อิมิตเตอร์เป็นรอยต่อ PN ของซิลิคอน จึงต้องการประมาณ 0.7 V เหมือนไดโอดซิลิคอน'),
 ('เมื่อใช้ทรานซิสเตอร์เป็นสวิตช์ จะทำงานในย่านใด',
  ['คัตออฟ (OFF) และอิ่มตัว (ON)', 'แอกทีฟเท่านั้น', 'แอกทีฟและย่านพังทลาย', 'ทุกย่านให้ผลเหมือนกัน'],
  'สวิตช์ต้องดับสนิทหรือติดเต็มที่ จึงใช้ย่านคัตออฟกับอิ่มตัว ส่วนย่านแอกทีฟใช้ขยายสัญญาณ'),
 ('ย่านแอกทีฟของทรานซิสเตอร์เหมาะกับงานใด',
  ['ขยายสัญญาณ', 'สวิตช์ที่ต้องติดเต็มที่', 'ตัดวงจรให้ขาด', 'เรียงกระแส AC เป็น DC'],
  'ในย่านแอกทีฟ IC = β × IB จึงขยายสัญญาณได้ เช่น Q1 C9013 ที่ขยายสัญญาณจากไอซีเพลงไปขับลำโพง'),
 ('โครงงานที่ 6: R2 + VR2 ต่อจาก +9 V เข้าเบส และ LDR ต่อจากเบสลงกราวด์ เมื่อมืดจะเกิดอะไรขึ้น',
  ['VB สูงขึ้นจนทรานซิสเตอร์นำ LED2 สว่าง', 'VB ต่ำลง ทรานซิสเตอร์หยุดนำ', 'LED2 ดับเพราะ LDR มีความต้านทานต่ำ', 'ไม่มีผลเพราะ LDR ไม่ได้ต่อกับ LED'],
  'มืดแล้ว LDR สูง แรงดันที่เบสจึงสูงขึ้นจนถึงราว 0.7 V ทรานซิสเตอร์นำและ LED2 ที่ขาคอลเล็กเตอร์สว่าง'),
 ('ในโครงงานที่ 6 ถ้าปรับ VR2 ให้ความต้านทานเพิ่มขึ้น ผลคืออะไร',
  ['ต้องมืดมากขึ้นกว่าเดิม วงจรจึงทำงาน', 'วงจรทำงานเร็วขึ้นตั้งแต่ยังสว่าง', 'LED2 สว่างตลอดเวลา', 'ไม่มีผลต่อการทำงาน'],
  'R ด้านบนมากขึ้น แรงดันที่เบสต่ำลงที่ความมืดเท่าเดิม ต้องให้ LDR สูงขึ้นอีก (มืดกว่าเดิม) VB จึงถึง 0.7 V'),
 ('R3 = 330 Ω ที่ต่ออนุกรมกับ LED2 ในขาคอลเล็กเตอร์ทำหน้าที่อะไร',
  ['จำกัดกระแสผ่าน LED2', 'ไบอัสขาเบส', 'กรองแรงดันให้เรียบ', 'เพิ่มค่า β ของทรานซิสเตอร์'],
  'เมื่อทรานซิสเตอร์อิ่มตัว กระแสถูกจำกัดด้วย R3 ถ้าไม่มี R3 กระแสจะสูงจน LED หรือทรานซิสเตอร์เสียหาย'),
 ('ทรานซิสเตอร์อิ่มตัว ขับ LED (VF = 2 V) ผ่าน R = 330 Ω จาก 9 V โดย VCE(sat) ≈ 0.2 V กระแส LED ประมาณเท่าใด',
  ['20.6 mA', '27.3 mA', '6.1 mA', '2.06 mA'],
  'IC ≈ (9 − 2 − 0.2) / 330 ≈ 20.6 mA ถ้าได้ 27.3 mA แสดงว่าลืมหัก VF และ VCE(sat)'),
 ('ขับเบสด้วยแรงดัน 5 V ผ่าน RB ต้องการ IB = 0.1 mA RB ควรเป็นเท่าใด (VBE = 0.7 V)',
  ['43 kΩ', '50 kΩ', '7 kΩ', '4.3 kΩ'],
  'RB = (5 − 0.7) / 0.1 mA = 4.3 V / 0.1 mA = 43 kΩ ถ้าได้ 50 kΩ แสดงว่าลืมหัก VBE'),
]
B['district3'] = [
 ('ในโครงงานที่ 3 รีดสวิตช์ S1 ทำหน้าที่อะไร',
  ['สวิตช์ที่ต่อวงจรเมื่อแม่เหล็กเข้าใกล้ ดึงขา 1 ของไอซีเสียงเพลงลงกราวด์', 'ขยายสัญญาณเสียง', 'รักษาระดับแรงดัน', 'กำเนิดความถี่เสียงเพลง'],
  'เอกสาร LAB อธิบายว่าเมื่อแม่เหล็กเข้าใกล้ หน้าสัมผัสของ S1 ต่อถึงกัน ขา 1 ของไอซีเสียงเพลงจึงต่อลงกราวด์และไอซีสร้างเพลง'),
 ('ขณะรีดสวิตช์ S1 เปิดวงจร ขา 1 ของไอซีเสียงเพลงอยู่ในสภาวะใด',
  ['ถูก R1 10 kΩ ดึงขึ้นไปทางไฟบวก ไอซีจึงไม่สร้างเพลง', 'ลอย ไอซีสร้างเพลงตลอด', 'ต่อลงกราวด์ ไอซีสร้างเพลง', 'ขาดไฟเลี้ยงทั้งวงจร'],
  'R1 เป็นตัวต้านทานพูลอัป ทำให้ขา 1 มีแรงดันสูงเมื่อสวิตช์เปิด ไอซีจึงเงียบ'),
 ('ไอซี 7805 (IC1) ในวงจรทำหน้าที่อะไร',
  ['รักษาระดับแรงดันขาออกให้คงที่ 5 V', 'ขยายสัญญาณเสียง', 'สร้างเพลง', 'เรียงกระแส AC เป็น DC'],
  '7805 เป็นไอซีเรกูเลเตอร์ 3 ขา รับแรงดันขาเข้าที่สูงกว่าแล้วจ่ายออก 5 V คงที่'),
 ('Q1 (C9013) และ R2 2 kΩ หลังขา 3 ของไอซีเสียงเพลงทำหน้าที่อะไร',
  ['ขยายสัญญาณจากไอซีให้แรงพอขับลำโพง', 'สร้างเพลง', 'ลดแรงดันแหล่งจ่าย', 'ตรวจจับแสง'],
  'สัญญาณจากไอซีเพลงมีกำลังน้อย จึงผ่าน R2 เข้าเบสของ Q1 ให้ทรานซิสเตอร์ขยายกระแสขับลำโพงผ่าน R3'),
 ('ต้องการให้เพลงดังเมื่อมืด ควรใช้อะไรทำหน้าที่แทนรีดสวิตช์ S1',
  ['ทรานซิสเตอร์จากวงจร LDR โดยขา C ต่อจุดขา 1 และขา E ลงกราวด์', 'LED', 'ตัวเก็บประจุ 100 µF', 'ไดโอดเรียงกระแส'],
  'ทรานซิสเตอร์ที่นำเมื่อมืดทำหน้าที่เหมือนสวิตช์ที่ปิดวงจร ดึงขา 1 ลงกราวด์แทนรีดสวิตช์ นี่คือคำตอบหลักของข้อ 72'),
 ('ในวงจรรวมของข้อ 72 เมื่อสว่างจะเกิดอะไรขึ้น',
  ['ทรานซิสเตอร์ไม่นำ ขา 1 ถูก R1 ดึงขึ้น ลำโพงเงียบ', 'ทรานซิสเตอร์นำ เพลงดัง', 'ลำโพงดังตลอดเวลา', '7805 หยุดทำงาน'],
  'สว่างแล้ว LDR ต่ำ แรงดันเบสไม่ถึง 0.7 V ทรานซิสเตอร์ไม่นำ เหมือนสวิตช์เปิด ขา 1 จึงถูกดึงขึ้นและไอซีเงียบ'),
 ('ข้อใดเรียงบล็อกของวงจร "ส่งเสียงเพลงเมื่อมืด" ตามการไหลของสัญญาณได้ถูกต้อง',
  ['LDR แบ่งแรงดัน → ทรานซิสเตอร์สวิตช์ → ไอซีเสียงเพลง → C9013 ขยาย → ลำโพง', 'ลำโพง → C9013 → ไอซีเสียงเพลง → LDR → ทรานซิสเตอร์', 'ไอซีเสียงเพลง → LDR → ลำโพง → ทรานซิสเตอร์ → C9013', 'ทรานซิสเตอร์ → แบตเตอรี่ → LDR → ลำโพง → ไอซีเสียงเพลง'],
  'สัญญาณเริ่มจากตัวรับรู้ ผ่านสวิตช์ ไปสั่งไอซีสร้างเพลง แล้วขยายก่อนออกลำโพง ใช้เป็นบล็อกไดอะแกรมตอบข้อเขียนได้ทันที'),
 ('ขั้นแรกของ "สูตรตอบข้อเขียนออกแบบวงจร 4 ขั้น" คืออะไร',
  ['วาดบล็อกไดอะแกรม ตัวรับรู้ → สวิตช์ → เอาต์พุต', 'คำนวณค่าตัวต้านทานทุกตัวก่อน', 'เขียนคำอธิบายยาว ๆ ให้ครบ', 'เลือกยี่ห้ออุปกรณ์'],
  'บล็อกไดอะแกรมทำให้เห็นโครงของระบบและได้คะแนนบางส่วนทันที ในกลางภาคมี 17 คนได้ 0 คะแนนในข้อ 72 เพราะไม่ได้เขียนส่วนนี้'),
 ('วงจรรวมไม่ดังเมื่อมืด แต่เมื่อลัดขา C กับ E ของทรานซิสเตอร์ด้วยสายไฟ เพลงดังทันที ปัญหาน่าจะอยู่ที่ใด',
  ['ส่วนตัวรับรู้หรือไบอัสเบส เช่น ต้องปรับ VR2 หรือตรวจ LDR', 'ลำโพงเสีย', 'ไอซี 7805 เสีย', 'ไอซีเสียงเพลงเสีย'],
  'การลัดขา C–E จำลองว่าสวิตช์ปิดแล้วเพลงดัง แปลว่าส่วนเพลง ขยาย และลำโพงทำงานปกติ ปัญหาจึงอยู่ก่อนหน้า คือแรงดันเบสยังไม่ถึง 0.7 V'),
 ('R3 = 330 Ω ที่ต่ออนุกรมกับลำโพงในขา C ของ Q1 มีหน้าที่หลักอะไร',
  ['จำกัดกระแสผ่านลำโพงและทรานซิสเตอร์', 'เพิ่มความดังของลำโพง', 'ไบอัสขาเบสของ Q1', 'กรองไฟ AC'],
  'ลำโพง 8 Ω มีความต้านทานต่ำมาก ถ้าไม่มี R3 กระแสจะสูงเกินจนทรานซิสเตอร์และแบตเตอรี่ทำงานหนัก'),
 ('C1 = 100 µF ที่ต่อคร่อมแหล่งจ่ายมีหน้าที่อะไร',
  ['ช่วยให้แรงดันแหล่งจ่ายนิ่ง ลดสัญญาณรบกวน', 'เก็บเสียงเพลงไว้เล่นซ้ำ', 'ขยายสัญญาณ', 'ตั้งเวลาให้เพลงหยุด'],
  'ตัวเก็บประจุคร่อมแหล่งจ่ายดูดซับการเปลี่ยนแปลงกระแสชั่วขณะ แรงดันที่จ่ายให้ไอซีจึงนิ่งขึ้น'),
 ('ถ้าต้องการให้วงจรทรานซิสเตอร์ + LDR ทำงานเมื่อ "สว่าง" แทน (เช่น เตือนประตูตู้เย็นเปิด) ต้องแก้อย่างไร',
  ['สลับตำแหน่ง LDR กับ R2 + VR2', 'กลับขั้วแบตเตอรี่', 'ถอด 7805 ออก', 'เปลี่ยน LED เป็นสีอื่น'],
  'เมื่อ LDR อยู่ด้านบน สว่างแล้ว LDR ต่ำ แรงดันเบสจะสูงขึ้นจนทรานซิสเตอร์นำ เป็นหลักการเดียวกับโครงงานที่ 24'),
 ('ข้อดีของการออกแบบวงจรเป็นบล็อกคืออะไร',
  ['ทดสอบทีละส่วนและหาจุดเสียได้เร็ว', 'ใช้อุปกรณ์น้อยลงเสมอ', 'ไม่ต้องคำนวณค่าใดเลย', 'ทำให้กระแสไหลเร็วขึ้น'],
  'เมื่อแบ่งเป็นบล็อก เราทดสอบได้ทีละจุด เช่น ลัดขา C–E เพื่อตรวจส่วนเพลง หรือวัด VB เพื่อตรวจส่วนตัวรับรู้'),
]


# ---------- รูปวงจรประกอบโจทย์ (ต่อท้ายโจทย์เดิม ไม่ลบข้อความ) ----------
from qfig import divider, bjt, proj6, led_collector, base_drive, pin1_node
AUG = {
 'district1': {2: divider('9 V', 'R 10 kΩ', 'LDR 10 kΩ', ldr_bot=True), 3: divider('9 V', 'R 10 kΩ', 'LDR 100 kΩ', ldr_bot=True),
               4: divider('9 V', 'R 10 kΩ', 'LDR 1 kΩ', ldr_bot=True), 5: divider('Vs', 'R', 'LDR', ldr_bot=True),
               10: divider('5 V', 'R 10 kΩ', 'LDR = ?', out='2.5 V', ldr_bot=True), 12: divider('5 V', 'R 10 kΩ', 'LDR 40 kΩ', ldr_bot=True)},
 'district2': {2: bjt('40 µA', 'IC = ?', 'IE', 'β = 100'), 3: bjt('75 µA', '15 mA', 'IE', 'β = ?'), 4: bjt('40 µA', '4 mA', 'IE = ?'),
               8: proj6(), 9: proj6(), 10: proj6(), 11: led_collector(), 12: base_drive()},
 'district3': {0: pin1_node(), 1: pin1_node(), 4: pin1_node('? (แทน S1)'), 5: pin1_node('ทรานซิสเตอร์ (แทน S1)'),
               8: pin1_node('ทรานซิสเตอร์ (แทน S1)')},
}
for _d, _m in AUG.items():
    for _i, _fig in _m.items():
        _q, _c, _e = B[_d][_i]; B[_d][_i] = (_q + _fig, _c, _e)

# ปรับสมดุลความยาวตัวเลือก (Rescue รอบ 1) ดู bank_rew.py
from bank_rew import apply as _rew
_rew(B, 'g6')

STAR = star_table([
 ('NIGHT MAESTRO', 'ประกอบระบบได้ครบทุกบล็อก พร้อมตอบข้อเขียนออกแบบวงจรใน Final แล้ว ลองช่วยอธิบายให้คู่ของคุณ'),
 ('MELODY MAKER', 'เกือบสมบูรณ์ ทบทวนข้อที่พลาดอีกครั้ง แล้วลองต่อวงจรจริงบนโปรโตบอร์ด'),
 ('SWITCH RIDER', 'ผ่านเกณฑ์แล้ว เล่นห้องทดลองประตู 2 ให้ครบทั้ง 3 ย่านการทำงาน'),
 ('LIGHT SEEKER', 'เริ่มจับหลักได้ ทบทวนสูตรวงจรแบ่งแรงดันและเงื่อนไข VBE ≥ 0.7 V'),
 ('EVENING STARTER', 'มีพื้นฐานบ้างแล้ว เล่นประตูทั้ง 3 ให้ครบ แล้วกลับมาทำแบบทดสอบอีกครั้ง'),
 ('NEW SPARK', 'ยังไม่คุ้นเนื้อหา ไม่เป็นไร เริ่มจากประตู 1 อ่านการ์ดทีละใบ แล้วเล่นห้องทดลอง'),
])

BADGES = r"""[
  {id:'perfect',  name:'NIGHT MAESTRO',  desc:'Posttest ถูกครบ 6 ข้อ',                 test:s => s.post === 6},
  {id:'zero2hero',name:'DAWN RISER',     desc:'คะแนนเพิ่มขึ้น 3 ข้อขึ้นไปจาก Pretest',    test:s => (s.post - s.pre) >= 3},
  {id:'fast',     name:'QUICK SWITCH',   desc:'ตอบถูกภายใน 8 วินาที',                  test:s => s.fastCorrect},
  {id:'labrat',   name:'BREADBOARD HERO',desc:'เล่นห้องทดลองครบทั้งสามประตู',           test:s => s.labs.lab1.length >= 3 && s.labs.lab2.length >= 3 && s.labs.lab3.length >= 3},
  {id:'combo',    name:'SATURATED',      desc:'ตอบถูกติดกัน 5 ข้อขึ้นไป',              test:s => s.maxCombo >= 5},
  {id:'sweep',    name:'FULL CHAIN',     desc:'ได้ 2/2 ครบทั้งสามประตู',                test:s => s.postByD.district1 === 2 && s.postByD.district2 === 2 && s.postByD.district3 === 2}
]"""

ADVICE = r"""
  const tips=[];
  if(labCount('lab1')<3) tips.push('เล่นเครื่องวัดแสงในประตู 1 ให้ครบทั้งมืดและสว่าง ทั้งตอน LDR อยู่ด้านบนและด้านล่าง');
  if(labCount('lab2')<3) tips.push('ในประตู 2 หาให้เจอทั้ง 3 ย่าน: คัตออฟ แอกทีฟ และอิ่มตัว แล้วสังเกตว่า VR2 เลื่อนจุดทำงานอย่างไร');
  if(labCount('lab3')<3) tips.push('ประกอบระบบในประตู 3 ทั้งแบบรีดสวิตช์และแบบ LDR + ทรานซิสเตอร์ แล้วเรียงบล็อกให้ครบ 5 ชิ้น');
  if(postInfo.stars===6) tips.push('ได้ครบ 6 ดาวแล้ว ลองต่อวงจรข้อ 72 บนโปรโตบอร์ดจริงใน Build Battle เพื่อรับ Combo Stamp');
  return tips;
"""

CFG = {
    'filename': 'game6_night_melody.html',
    'title': 'NIGHT MELODY : วงจรเพลงยามค่ำ',
    'brand': 'NIGHT MELODY',
    'edition': 'NIGHT EDITION',
    'desc': 'เกมทบทวน GNR2022 ข้อ 72: LDR และวงจรแบ่งแรงดัน ทรานซิสเตอร์เป็นสวิตช์ และการประกอบระบบส่งเสียงเพลงเมื่อมืด จากโครงงานที่ 3 และ 6',
    'ogdesc': 'เปิด 3 ประตูยามค่ำ จากตัวรับรู้แสง สู่สวิตช์ทรานซิสเตอร์ จนได้เพลงที่ดังเมื่อมืด วัดผลก่อน-หลังเรียน',
    'favicon': "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='18' fill='%23070a1e'/><circle cx='50' cy='50' r='26' fill='%23fef08a'/><circle cx='60' cy='42' r='24' fill='%23070a1e'/></svg>",
    'theme': THEME,
    'extra_css': EXTRA_CSS,
    'arcade_label': 'ด่านไต่หอยามค่ำ',
    'hero_svg': HERO,
    'subtitle': 'สวมบทบาท <b>วิศวกรยามค่ำ</b> เปิด 3 ประตู ตั้งแต่ LDR ที่รับรู้ความมืด ทรานซิสเตอร์ที่เป็นสวิตช์ จนถึงไอซีที่ร้องเพลงเมื่อไฟดับ ทั้งหมดมาจากวงจรที่คุณเคยต่อใน LAB',
    'login_tag': 'Night Engineer Registration',
    'features': '<span>GNR2022 · ทบทวนข้อ 72</span><span>LDR · BJT · UM66</span><span>PRETEST / POSTTEST</span><span>ระบบดาว 6 ดวง</span>',
    'climb_text': 'ตัวละครไต่หอยามค่ำขึ้น 1 ชั้น ทันที',
    'zones_html': ZONES,
    'checks': [('Gate 01', 'ดวงตาแห่งแสง'), ('Gate 02', 'สวิตช์ไร้หน้าสัมผัส'), ('Gate 03', 'เพลงยามค่ำ')],
    'post_desc': '6 ข้อใหม่ (ประตูละ 2 ข้อ) เพื่อวัดความเข้าใจหลังเปิดครบทั้ง 3 ประตู',
    'report_tag': 'Night Report',
    'course': COURSE,
    'footer_line': 'เกมทบทวนข้อสอบกลางภาคข้อ 72 จากโครงงานที่ 3 และ 6 ในเอกสาร LAB — ภาคเรียนที่ 1/2569',
    'bank': bank_js(B),
    'skill_labels': "{district1:'LDR & วงจรแบ่งแรงดัน', district2:'ทรานซิสเตอร์สวิตช์', district3:'ประกอบระบบเพลงยามค่ำ'}",
    'skey': 'gnr2022_nightmelody_v1_state',
    'star_table': STAR,
    'navstops': navstops('G1 LDR', 'G2 BJT', 'G3 MELODY'),
    'lock_msg': 'ประตูนี้ยังไม่เปิด เดินตามลำดับก่อนนะครับ',
    'act': {'floor': 'ชั้น', 'top': 'ยอดหอยามค่ำ', 'ground': 'ลานหน้าหอ', 'theme': 'circuit'},
    'pre_sub': 'นี่คือเส้นฐานของคุณ เปิดครบ 3 ประตูแล้วเรามาวัดกันใหม่',
    'go_first': 'เปิดประตูแรก',
    'lab_js': LAB_JS,
    'lab_wiring': LAB_WIRING,
    'init_extra': INIT_EXTRA,
    'badges': BADGES,
    'advice_js': ADVICE,
    'role': 'วิศวกรยามค่ำ',
    'filekey': 'GNR2022_Z6_nightmelody',
    'avatars': avatars('#0e1438', ['#a78bfa', '#2dd4bf', '#facc15', '#fb7185', '#c4b5fd', '#5eead4']),
}
