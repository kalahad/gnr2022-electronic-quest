# -*- coding: utf-8 -*-
"""SEASON 1 · ZONE 4 — DIODE FORGE : โรงตีไดโอด
ไดโอดและการไบแอส · LED กับตัวแสดงผล 7 ส่วน · ซีเนอร์ไดโอดและวงจรควบคุมแรงดัน
อ้างอิงค่า: 1N4001–1N4007 (IF(AV) 1 A, VRRM 50–1000 V) · 74LS47 (เอาต์พุต active-low สำหรับ common anode)
CD4511 (เอาต์พุต active-high สำหรับ common cathode) · ซีเนอร์ 5.1 V 0.5 W (Izm = P/Vz)"""
from cpe_common import *
from legacy_port import zone_theme

THEME = zone_theme('#ff6a1f', '#ff2e88', '#ffd60a', '#ff4d4d', '#c84300', '#c2155f', '#8a6a00', '#b91c1c', bg='#120806')

EXTRA_CSS = LAB_CSS + """
.seg7{display:block;width:min(150px,32vw);height:auto;margin:4px auto}
.seg7 .s{fill:rgba(255,255,255,.07);stroke:rgba(255,255,255,.12);stroke-width:1;transition:.2s}
.seg7 .s.on{fill:var(--gold);filter:drop-shadow(0 0 6px var(--gold))}
.pinrow{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:8px 0}
.pinrow button{min-width:52px;padding:7px 8px;border-radius:10px;border:1px solid var(--line);background:rgba(var(--panel-rgb),.6);color:var(--text);font-family:var(--mono);cursor:pointer;line-height:1.15}
.pinrow button b{display:block;font-size:1rem}
.pinrow button.hi{border-color:var(--gold);background:var(--ember-dim)}
.dio{display:block;width:100%;max-width:440px;margin:4px auto}
"""

HERO = """<svg class="cityart" viewBox="0 0 480 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="โรงตีเหล็กที่ทั่งเป็นสัญลักษณ์ไดโอด มีประกายไฟและตัวเลข 7 ส่วน">
  <defs><filter id="fGlow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <radialGradient id="gHeat" cx="50%" cy="70%" r="60%"><stop offset="0" stop-color="rgba(255,106,31,.55)"/><stop offset="1" stop-color="rgba(255,106,31,0)"/></radialGradient></defs>
  <rect x="0" y="0" width="480" height="300" rx="18" fill="#120806"/>
  <rect x="0" y="0" width="480" height="300" rx="18" fill="url(#gHeat)"/>
  <g filter="url(#fGlow)">
    <path d="M60 176 H160" stroke="#ffd60a" stroke-width="5"/><path d="M160 136 L230 176 L160 216 Z" fill="#ff6a1f"/><path d="M232 132 V220" stroke="#ff6a1f" stroke-width="8"/><path d="M232 176 H300" stroke="#ffd60a" stroke-width="5"/>
    <g fill="#ffd60a"><circle cx="250" cy="110" r="3"/><circle cx="270" cy="92" r="2.4"/><circle cx="236" cy="84" r="2"/><circle cx="292" cy="118" r="2.2"/><circle cx="214" cy="104" r="1.8"/></g>
  </g>
  <g transform="translate(340 96)" filter="url(#fGlow)">
    <rect x="-8" y="-8" width="96" height="152" rx="12" fill="#1c0c08" stroke="#ff2e88" stroke-width="2"/>
    <g fill="#ffd60a"><rect x="14" y="4" width="52" height="10" rx="5"/><rect x="66" y="14" width="10" height="52" rx="5"/><rect x="66" y="74" width="10" height="52" rx="5"/><rect x="14" y="126" width="52" height="10" rx="5"/><rect x="14" y="65" width="52" height="10" rx="5"/><rect x="4" y="74" width="10" height="52" rx="5"/></g>
    <g fill="rgba(255,255,255,.08)"><rect x="4" y="14" width="10" height="52" rx="5"/></g>
  </g>
  <path d="M40 250 H440" stroke="#ff6a1f" stroke-width="3"/>
  <text x="240" y="284" text-anchor="middle" font-size="10" letter-spacing="3" fill="#e8c9b8">BIAS · LIGHT · CLAMP</text>
</svg>"""

ZONES = """
<!-- ===== PREVIEW 1 ===== -->
<section id="scr-preview1" class="screen">
  <div class="panel">
    <span class="tag">Forge Hall 01</span>
    <h2>กำลังจะเข้าสู่: เตาไบแอส (Bias Furnace)</h2>
    <div class="dcard">
      <div class="ico"><svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
        <path d="M6 40 H26 M54 40 H74" stroke="#ffd60a" stroke-width="4"/><path d="M26 22 L54 40 L26 58 Z" fill="#ff6a1f"/><path d="M56 20 V60" stroke="#ff6a1f" stroke-width="5"/></svg></div>
      <div><div class="skillcard" style="margin:0">
        <div class="sk-name">ทักษะที่จะได้: ระบุขาไดโอด ไบแอสตรงและย้อนกลับ และคำนวณกระแสด้วยแบบจำลองแรงดันตกคงที่</div>
        <p class="muted" style="margin:6px 0 0">ต่อยอดจากรอยต่อ PN ในโซน 3 สู่ไดโอดจริงที่ใช้บนแผงวงจร</p>
      </div></div>
    </div>
    <div class="btn-row"><button class="btn primary" data-goto="scr-lesson1">เข้าเตาไบแอส</button></div>
  </div>
</section>

<!-- ===== HALL 1 ===== -->
<section id="scr-lesson1" class="screen">
  <div class="panel">
    <span class="tag">Hall 01 · Bias Furnace</span>
    <h2>เตาไบแอส: ไดโอดเป็นประตูทางเดียว</h2>
    <p>ไดโอดคือรอยต่อ PN ที่มีขา <b>แอโนด (A, ฝั่ง P)</b> และ <b>แคโทด (K, ฝั่ง N)</b> บนตัวถังจะมี <b>แถบสีที่ด้านแคโทด</b>
      เมื่อป้อนขั้วบวกเข้าแอโนด (ไบแอสตรง) และแรงดันเกินแรงดันเข่า ไดโอดจะนำกระแส เมื่อกลับขั้ว (ไบแอสย้อนกลับ) จะมีเพียงกระแสรั่วเล็กมาก
      และแรงดันเกือบทั้งหมดของแหล่งจ่ายจะตกคร่อมไดโอด</p>
    <div class="tbl-wrap"><table>
      <tr><th>แบบจำลอง</th><th>VF ที่ใช้คำนวณ</th><th>ใช้เมื่อ</th></tr>
      <tr><td>อุดมคติ</td><td>0 V</td><td>แรงดันวงจรสูงมากเทียบกับ VF</td></tr>
      <tr><td>ซิลิคอน (ใช้บ่อยที่สุด)</td><td>≈ 0.7 V</td><td>วิเคราะห์วงจรทั่วไป เช่น 1N4007</td></tr>
      <tr><td>เจอร์เมเนียม</td><td>≈ 0.3 V</td><td>ไดโอดสัญญาณรุ่นเก่า</td></tr>
    </table></div>
    <div class="codebox">ไบแอสตรง (Vs > VF):  I = (Vs − VF) / R     VD ≈ VF
ไบแอสย้อนกลับ:      I ≈ 0               VD ≈ −Vs (ต้องไม่เกิน PIV)
ตัวอย่าง: 5 V, ไดโอดซิลิคอน, R = 1 kΩ → I = (5 − 0.7) / 1,000 = 4.3 mA</div>
    <div class="tbl-wrap"><table>
      <tr><th>รุ่น</th><th>กระแสเฉลี่ยไปหน้า</th><th>แรงดันย้อนกลับสูงสุด</th></tr>
      <tr><td>1N4001</td><td>1 A</td><td>50 V</td></tr>
      <tr><td>1N4004</td><td>1 A</td><td>400 V</td></tr>
      <tr><td>1N4007</td><td>1 A</td><td>1,000 V</td></tr>
    </table></div>
    <div class="keyfact">จำให้ขึ้นใจ: <b>แถบ = แคโทด</b> · ไบแอสตรง <b>บวกเข้าแอโนด</b> · ซิลิคอน <b>VF ≈ 0.7 V</b> · ไบแอสย้อนกลับแรงดันตกคร่อมไดโอดเกือบทั้งหมด</div>

    <h3 style="margin-top:18px">ห้องทดลอง: แท่นทดสอบไบแอส</h3>
    <p class="muted">เลื่อนแรงดันแหล่งจ่ายจากลบถึงบวก เปลี่ยนแบบจำลองไดโอด แล้วดูกระแสและแรงดันตกคร่อม หาให้ครบ: ไบแอสตรง ต่ำกว่าแรงดันเข่า และไบแอสย้อนกลับ</p>
    <svg class="dio" id="dbSvg" viewBox="0 0 440 130" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="วงจรแหล่งจ่าย ไดโอด และตัวต้านทาน 1 kΩ"></svg>
    <label class="muted" for="dbV" style="display:block;font-size:.85rem">แรงดันแหล่งจ่าย Vs: <b id="dbVt">5.0 V</b> · R = 1 kΩ</label>
    <input type="range" class="rng" id="dbV" min="-100" max="100" value="50" aria-label="แรงดันแหล่งจ่าย">
    <div class="labrow"><button class="btn sm" data-dbm="0">อุดมคติ 0 V</button><button class="btn sm" data-dbm="0.7">ซิลิคอน 0.7 V</button><button class="btn sm" data-dbm="0.3">เจอร์เมเนียม 0.3 V</button></div>
    <div class="labrow"><span class="readout" id="dbI">—</span><span class="readout" id="dbVD">—</span></div>
    <div class="status-line" id="dbStatus">เลื่อนแถบเพื่อเปลี่ยนแรงดัน</div>
    <div class="btn-row"><button class="btn primary" data-quiz="check1">ไปทำแบบฝึกหัดด่านนี้</button></div>
  </div>
</section>

<!-- ===== PREVIEW 2 ===== -->
<section id="scr-preview2" class="screen">
  <div class="panel">
    <span class="tag">Forge Hall 02</span>
    <h2>กำลังจะเข้าสู่: ทั่งตัวเลข (Digit Anvil)</h2>
    <div class="dcard">
      <div class="ico"><svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
        <g fill="#ffd60a"><rect x="26" y="8" width="28" height="6" rx="3"/><rect x="54" y="14" width="6" height="24" rx="3"/><rect x="54" y="42" width="6" height="24" rx="3"/><rect x="26" y="66" width="28" height="6" rx="3"/><rect x="26" y="37" width="28" height="6" rx="3"/></g>
        <g fill="rgba(255,255,255,.15)"><rect x="20" y="14" width="6" height="24" rx="3"/><rect x="20" y="42" width="6" height="24" rx="3"/></g></svg></div>
      <div><div class="skillcard" style="margin:0">
        <div class="sk-name">ทักษะที่จะได้: ต่อ LED ให้ปลอดภัย และควบคุมตัวแสดงผล 7 ส่วนแบบแอโนดร่วมและแคโทดร่วม</div>
        <p class="muted" style="margin:6px 0 0">7-segment คือ LED 7 ดวงในตัวถังเดียว ทุกกฎของ LED จึงใช้กับทุกส่วน</p>
      </div></div>
    </div>
    <div class="btn-row"><button class="btn primary" data-goto="scr-lesson2">เข้าทั่งตัวเลข</button></div>
  </div>
</section>

<!-- ===== HALL 2 ===== -->
<section id="scr-lesson2" class="screen">
  <div class="panel">
    <span class="tag">Hall 02 · Digit Anvil</span>
    <h2>ทั่งตัวเลข: LED และตัวแสดงผล 7 ส่วน</h2>
    <p><b>LED</b> คือไดโอดเปล่งแสง ทำงานเมื่อไบแอสตรงเท่านั้น <b>ขายาวคือแอโนด</b> และด้านที่ขอบตัวถังตัดเรียบคือแคโทด
      ต้องมีตัวต้านทานจำกัดกระแส R = (Vs − VF) / I เสมอ <b>ตัวแสดงผล 7 ส่วน</b> มี LED ชื่อ a ถึง g (และจุด dp)
      แบบ <b>แคโทดร่วม (CC)</b> ต่อขาร่วมลงกราวด์ ส่วนจะติดเมื่อขานั้นเป็น <b>HIGH</b> แบบ <b>แอโนดร่วม (CA)</b> ต่อขาร่วมเข้าไฟบวก ส่วนจะติดเมื่อขานั้นเป็น <b>LOW</b></p>
    <div class="divfig">     a
   ─────
  f│     │b
   │  g  │
   ─────
  e│     │c
   │  d  │
   ─────  · dp</div>
    <div class="tbl-wrap"><table>
      <tr><th>ตัวเลข</th><th>ส่วนที่ติด</th><th>ตัวเลข</th><th>ส่วนที่ติด</th></tr>
      <tr><td>0</td><td>a b c d e f</td><td>5</td><td>a c d f g</td></tr>
      <tr><td>1</td><td>b c</td><td>6</td><td>a c d e f g</td></tr>
      <tr><td>2</td><td>a b d e g</td><td>7</td><td>a b c</td></tr>
      <tr><td>3</td><td>a b c d g</td><td>8</td><td>a b c d e f g</td></tr>
      <tr><td>4</td><td>b c f g</td><td>9</td><td>a b c d f g</td></tr>
    </table></div>
    <div class="tbl-wrap"><table>
      <tr><th>ชนิด</th><th>ขาร่วมต่อที่</th><th>ส่วนติดเมื่อ</th><th>ไอซีถอดรหัสที่ใช้คู่กัน</th></tr>
      <tr><td>แคโทดร่วม (CC)</td><td>กราวด์</td><td>ขา = HIGH (1)</td><td>CD4511 (เอาต์พุต active-high)</td></tr>
      <tr><td>แอโนดร่วม (CA)</td><td>+V</td><td>ขา = LOW (0)</td><td>74LS47 (เอาต์พุต active-low)</td></tr>
    </table></div>
    <div class="codebox">ตัวต้านทานต่อส่วน: 5 V, VF ≈ 2 V, 10 mA → R = 3 / 0.010 = 300 Ω → ใช้ 330 Ω ทุกส่วน
ใช้ตัวต้านทานแยกทุกส่วน ไม่ใช้ตัวเดียวที่ขาร่วม เพราะจำนวนส่วนที่ติดเปลี่ยน ความสว่างจะเปลี่ยนตาม</div>
    <div class="keyfact">จำให้ขึ้นใจ: <b>CC ติดเมื่อ 1 · CA ติดเมื่อ 0</b> · เลข 1 = b c · เลข 8 = ทุกส่วน · ตัวต้านทาน <b>หนึ่งตัวต่อหนึ่งส่วน</b></div>

    <h3 style="margin-top:18px">ห้องทดลอง: ทั่งตัวเลข 7 ส่วน</h3>
    <p class="muted">เลือกชนิด CC หรือ CA แล้วแตะขา a–g เพื่อสลับระดับลอจิก 0/1 ดูว่าส่วนไหนติด กด "โจทย์ใหม่" แล้วตั้งขาให้แสดงตัวเลขเป้าหมาย ทำให้ถูกทั้งแบบ CC และ CA</p>
    <div class="labrow" style="justify-content:center"><button class="toggle on" id="sgType">แคโทดร่วม (CC)</button><span class="readout" id="sgTgt"><small>ยังไม่มีโจทย์</small></span></div>
    <svg class="seg7" id="sgSvg" viewBox="0 0 100 170" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="ตัวแสดงผล 7 ส่วน"></svg>
    <div class="pinrow" id="sgPins"></div>
    <div class="labrow" style="justify-content:center"><button class="btn sm" id="sgNew">โจทย์ใหม่</button><button class="btn sm primary" id="sgCheck">ตรวจคำตอบ</button></div>
    <div class="status-line" id="sgStatus">แตะขาเพื่อเปลี่ยนระดับลอจิก</div>
    <div class="btn-row"><button class="btn primary" data-quiz="check2">ไปทำแบบฝึกหัดด่านนี้</button></div>
  </div>
</section>

<!-- ===== PREVIEW 3 ===== -->
<section id="scr-preview3" class="screen">
  <div class="panel">
    <span class="tag">Forge Hall 03</span>
    <h2>กำลังจะเข้าสู่: บ่อชุบซีเนอร์ (Zener Quench)</h2>
    <div class="dcard">
      <div class="ico"><svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
        <path d="M6 40 H26 M54 40 H74" stroke="#ffd60a" stroke-width="4"/><path d="M26 22 L54 40 L26 58 Z" fill="#ff2e88"/><path d="M48 16 L54 20 V60 L60 64" stroke="#ff2e88" stroke-width="5" fill="none"/></svg></div>
      <div><div class="skillcard" style="margin:0">
        <div class="sk-name">ทักษะที่จะได้: ออกแบบวงจรควบคุมแรงดันด้วยซีเนอร์ คำนวณ Rs, Iz และกำลังสูญเสีย</div>
        <p class="muted" style="margin:6px 0 0">ซีเนอร์คือไดโอดที่ "ตั้งใจ" ให้ทำงานในย่านพังทลายย้อนกลับ</p>
      </div></div>
    </div>
    <div class="btn-row"><button class="btn primary" data-goto="scr-lesson3">เข้าบ่อชุบซีเนอร์</button></div>
  </div>
</section>

<!-- ===== HALL 3 ===== -->
<section id="scr-lesson3" class="screen">
  <div class="panel">
    <span class="tag">Hall 03 · Zener Quench</span>
    <h2>บ่อชุบซีเนอร์: ตรึงแรงดันให้คงที่</h2>
    <p>ซีเนอร์ไดโอดต่อแบบ <b>ไบแอสย้อนกลับ</b> เมื่อแรงดันถึง <b>Vz</b> จะพังทลายแบบไม่เสียหาย แรงดันคร่อมคงที่ใกล้ Vz แม้กระแสเปลี่ยน
      ต้องมี <b>ตัวต้านทานอนุกรม Rs</b> รับแรงดันส่วนต่าง และคุมให้กระแสซีเนอร์ <b>Iz</b> อยู่ระหว่าง <b>Izk</b> (ต่ำสุดที่ยังตรึงได้) กับ <b>Izm</b> (สูงสุดตามพิกัดกำลัง)
      ถ้าต่อไบแอสตรง ซีเนอร์จะทำตัวเหมือนไดโอดธรรมดา VF ≈ 0.7 V</p>
    <div class="codebox">Is = (Vin − Vz) / Rs          IL = Vz / RL          Iz = Is − IL
ออกแบบ: Rs = (Vin − Vz) / (Iz + IL)       Pz = Vz × Iz       Izm = Pz(max) / Vz
ตัวอย่าง: Vin 12 V, Vz 5.1 V, IL 20 mA, Iz 10 mA → Rs = 6.9 / 0.030 = 230 Ω
ซีเนอร์ 5.1 V พิกัด 0.5 W → Izm = 0.5 / 5.1 ≈ 98 mA</div>
    <div class="tbl-wrap"><table>
      <tr><th>เหตุการณ์ (Vin และ Rs คงที่)</th><th>ผลต่อ Iz</th><th>ข้อควรระวัง</th></tr>
      <tr><td>โหลดดึงกระแสมากขึ้น (RL ลดลง)</td><td>Iz ลดลง</td><td>ถ้า Iz &lt; Izk แรงดันออกจะตกต่ำกว่า Vz</td></tr>
      <tr><td>ถอดโหลดออก (IL = 0)</td><td>Iz = Is ทั้งหมด</td><td>กรณีเลวร้ายที่สุดของกำลังในซีเนอร์</td></tr>
      <tr><td>Vin เพิ่มขึ้น</td><td>Iz เพิ่มขึ้น</td><td>Vout ยังคงใกล้ Vz แต่ Pz สูงขึ้น</td></tr>
    </table></div>
    <div class="keyfact">จำให้ขึ้นใจ: <b>ซีเนอร์ต่อไบแอสย้อนกลับ</b> · <b>Iz = Is − IL</b> · ตรวจกรณี <b>ไม่มีโหลด</b> ว่า Pz ไม่เกินพิกัด</div>

    <h3 style="margin-top:18px">ห้องทดลอง: วงจรควบคุมแรงดันซีเนอร์ 5.1 V</h3>
    <p class="muted">ซีเนอร์ 5.1 V พิกัด 0.5 W (Izk ≈ 1 mA) ปรับ Vin เลือก Rs และโหลด แล้วหาให้ครบ 3 สถานะ: ควบคุมได้ ซีเนอร์ไม่ทำงาน และกำลังเกินพิกัด</p>
    <label class="muted" for="znV" style="display:block;font-size:.85rem">Vin: <b id="znVt">12.0 V</b></label>
    <input type="range" class="rng" id="znV" min="40" max="200" value="120" aria-label="แรงดันอินพุต">
    <div class="labrow"><span class="muted" style="font-size:.8rem">Rs</span><button class="btn sm" data-zrs="47">47 Ω</button><button class="btn sm" data-zrs="100">100 Ω</button><button class="btn sm" data-zrs="220">220 Ω</button><button class="btn sm" data-zrs="470">470 Ω</button></div>
    <div class="labrow"><span class="muted" style="font-size:.8rem">RL</span><button class="btn sm" data-zrl="0">ไม่มีโหลด</button><button class="btn sm" data-zrl="1000">1 kΩ</button><button class="btn sm" data-zrl="470">470 Ω</button><button class="btn sm" data-zrl="100">100 Ω</button></div>
    <div class="labrow"><span class="readout" id="znOut">—</span><span class="readout" id="znIz">—</span><span class="readout" id="znPz">—</span></div>
    <div class="meter"><i id="znBar"></i></div>
    <div class="status-line" id="znStatus">ปรับค่าเพื่อเริ่มทดลอง</div>
    <div class="btn-row"><button class="btn primary" data-quiz="check3">ไปทำแบบฝึกหัดด่านนี้</button></div>
  </div>
</section>
"""

LAB_JS = r"""
/* ---- LAB 1: diode bias bench ---- */
let dbVf=0.7;
function dbUpdate(user){
  const Vs=(+$('#dbV').value)/10, R=1000, fwd=Vs>0, on=Vs>dbVf;
  const I=on?(Vs-dbVf)/R:0, VD=on?dbVf:Vs, VR=I*R;
  $('#dbVt').textContent=Vs.toFixed(1)+' V';
  document.querySelectorAll('[data-dbm]').forEach(b=>b.classList.toggle('primary',+b.dataset.dbm===dbVf));
  $('#dbI').innerHTML=(I*1000).toFixed(2)+'<small>mA</small>'; $('#dbVD').innerHTML='VD '+VD.toFixed(2)+'<small>V</small>';
  const col=on?'var(--gold)':'rgba(160,160,190,.5)';
  $('#dbSvg').innerHTML='<path d="M30 30 H160 M240 30 H300 M380 30 H410 V100 H30 V30" fill="none" stroke="'+col+'" stroke-width="3"/>'
    +'<circle cx="30" cy="65" r="18" fill="none" stroke="var(--ember)" stroke-width="2.5"/><text x="30" y="70" text-anchor="middle" font-size="13" fill="var(--text)" font-family="monospace">'+(Vs>=0?'+':'−')+'</text>'
    +'<path d="M170 12 L222 30 L170 48 Z" fill="'+(on?'var(--ember)':'rgba(255,106,31,.25)')+'"/><path d="M226 10 V50" stroke="var(--ember)" stroke-width="5"/>'
    +'<text x="196" y="72" text-anchor="middle" font-size="12" fill="var(--muted)" font-family="monospace">A → K</text>'
    +'<rect x="300" y="18" width="80" height="24" rx="6" fill="none" stroke="var(--corner)" stroke-width="2"/><text x="340" y="35" text-anchor="middle" font-size="12" fill="var(--text)" font-family="monospace">1 kΩ</text>'
    +'<text x="340" y="70" text-anchor="middle" font-size="12" fill="var(--muted)" font-family="monospace">VR '+VR.toFixed(2)+' V</text>';
  const st=$('#dbStatus'); let k;
  if(on){ k='f'+dbVf; st.className='status-line ok'; st.innerHTML='<b>ไบแอสตรง นำกระแส</b> — I = ('+Vs.toFixed(1)+' − '+dbVf+') / 1 kΩ = '+(I*1000).toFixed(2)+' mA'; }
  else if(fwd){ k='knee'; st.className='status-line'; st.innerHTML='<b>ยังไม่ถึงแรงดันเข่า</b> — Vs = '+Vs.toFixed(1)+' V ไม่เกิน VF '+dbVf+' V ไดโอดยังแทบไม่นำ'; }
  else if(Vs<0){ k='rev'; st.className='status-line'; st.innerHTML='<b>ไบแอสย้อนกลับ</b> — กระแส ≈ 0 แรงดัน '+Math.abs(Vs).toFixed(1)+' V ตกคร่อมไดโอดเกือบทั้งหมด (1N4007 ทนได้ถึง 1,000 V)'; }
  else { k='zero'; st.className='status-line'; st.textContent='Vs = 0 V ไม่มีกระแส'; }
  if(user) markLab('lab1',k,2);
}

/* ---- LAB 2: 7-segment anvil ---- */
const SG='abcdefg'.split('');
const DIG={0:'abcdef',1:'bc',2:'abdeg',3:'abcdg',4:'bcfg',5:'acdfg',6:'acdefg',7:'abc',8:'abcdefg',9:'abcdfg'};
let sgCA=false, sgPin={a:0,b:0,c:0,d:0,e:0,f:0,g:0}, sgTarget=null, sgDone={cc:0,ca:0};
const SGP={a:'M22 8 H78 L70 16 H30 Z',b:'M80 10 V78 L72 72 V18 Z',c:'M80 92 V160 L72 152 V98 Z',d:'M22 162 H78 L70 154 H30 Z',e:'M20 92 V160 L28 152 V98 Z',f:'M20 10 V78 L28 72 V18 Z',g:'M24 85 L32 79 H68 L76 85 L68 91 H32 Z'};
function sgLit(s){ return sgCA ? sgPin[s]===0 : sgPin[s]===1; }
function sgDraw(){
  $('#sgSvg').innerHTML='<rect x="4" y="2" width="92" height="166" rx="10" fill="#140a08"/>'+SG.map(s=>'<path class="s'+(sgLit(s)?' on':'')+'" d="'+SGP[s]+'"/>').join('');
  $('#sgPins').innerHTML=SG.map(s=>'<button data-sgp="'+s+'" class="'+(sgPin[s]?'hi':'')+'">'+s+'<b>'+sgPin[s]+'</b></button>').join('');
  const b=$('#sgType'); b.textContent=sgCA?'แอโนดร่วม (CA)':'แคโทดร่วม (CC)'; b.className='toggle '+(sgCA?'off':'on');
}
function sgNew(){ sgTarget=Math.floor(Math.random()*10); $('#sgTgt').innerHTML='แสดงเลข <b>'+sgTarget+'</b><small>'+(sgCA?'CA':'CC')+'</small>'; const st=$('#sgStatus'); st.className='status-line'; st.textContent='ตั้งระดับลอจิกของขา a–g ให้แสดงเลข '+sgTarget; SFX.play('click'); }
function sgCheck(){
  const st=$('#sgStatus'); if(sgTarget==null){ st.textContent='กด "โจทย์ใหม่" ก่อน'; return; }
  const want=DIG[sgTarget], ok=SG.every(s=>sgLit(s)===(want.indexOf(s)>=0));
  if(ok){ const t=sgCA?'ca':'cc'; sgDone[t]++; st.className='status-line ok';
    st.innerHTML='<b>ถูกต้อง</b> — เลข '+sgTarget+' ใช้ส่วน '+want.split('').join(' ')+' · แบบ '+(sgCA?'CA ส่วนที่ติดต้องเป็น 0':'CC ส่วนที่ติดต้องเป็น 1')+' (CC '+sgDone.cc+' · CA '+sgDone.ca+')';
    SFX.play('fanfare'); markLab('lab2',t+sgDone[t],3); sgTarget=null; $('#sgTgt').innerHTML='<small>กดโจทย์ใหม่</small>'; }
  else { st.className='status-line'; st.innerHTML='ยังไม่ใช่ — เลข '+sgTarget+' ต้องติด '+want.split('').join(' ')+' และแบบ '+(sgCA?'CA ติดเมื่อขาเป็น 0':'CC ติดเมื่อขาเป็น 1'); SFX.play('wrong'); }
}

/* ---- LAB 3: zener regulator ---- */
let znRs=220, znRL=1000; const VZ=5.1, PZM=0.5, IZK=0.001;
function znUpdate(user){
  const Vin=(+$('#znV').value)/10; $('#znVt').textContent=Vin.toFixed(1)+' V';
  document.querySelectorAll('[data-zrs]').forEach(b=>b.classList.toggle('primary',+b.dataset.zrs===znRs));
  document.querySelectorAll('[data-zrl]').forEach(b=>b.classList.toggle('primary',+b.dataset.zrl===znRL));
  const open=znRL?Vin*znRL/(znRs+znRL):Vin;
  let Vout, Iz=0, k; const st=$('#znStatus');
  if(open<=VZ){ Vout=open; k='off'; st.className='status-line'; st.innerHTML='<b>ซีเนอร์ไม่ทำงาน</b> — แรงดันที่แบ่งได้ '+open.toFixed(2)+' V ยังไม่ถึง Vz 5.1 V ไม่มีการตรึงแรงดัน'; }
  else {
    Vout=VZ; const Is=(Vin-VZ)/znRs, IL=znRL?VZ/znRL:0; Iz=Is-IL; const Pz=VZ*Iz;
    if(Pz>PZM){ k='burn'; st.className='status-line'; st.innerHTML='<b>กำลังเกินพิกัด</b> — Pz = 5.1 × '+(Iz*1000).toFixed(1)+' mA = '+Pz.toFixed(2)+' W เกิน 0.5 W ซีเนอร์จะร้อนจนเสียหาย ต้องเพิ่ม Rs'; }
    else if(Iz<IZK){ k='izk'; st.className='status-line'; st.innerHTML='<b>ใกล้หลุดการควบคุม</b> — Iz = '+(Iz*1000).toFixed(2)+' mA ต่ำกว่า Izk ≈ 1 mA'; }
    else { k='reg'; st.className='status-line ok'; st.innerHTML='<b>ควบคุมได้</b> — Is = '+(Is*1000).toFixed(1)+' mA, IL = '+(IL*1000).toFixed(1)+' mA, Iz = Is − IL = '+(Iz*1000).toFixed(1)+' mA, Pz = '+Pz.toFixed(3)+' W'; }
  }
  $('#znOut').innerHTML='Vout '+Vout.toFixed(2)+'<small>V</small>'; $('#znIz').innerHTML='Iz '+(Iz*1000).toFixed(1)+'<small>mA</small>'; $('#znPz').innerHTML='Pz '+(VZ*Iz).toFixed(3)+'<small>W</small>';
  $('#znBar').style.width=Math.min(100,VZ*Iz/PZM*100)+'%';
  if(user) markLab('lab3',k,3);
}
"""

LAB_WIRING = r"""
  const dm=e.target.closest('[data-dbm]'); if(dm){dbVf=+dm.dataset.dbm;SFX.play('select');dbUpdate(true);return;}
  if(e.target.closest('#sgType')){sgCA=!sgCA;SFX.play('select');sgDraw();markLab('lab2',sgCA?'tca':'tcc',1);if(sgTarget!=null) $('#sgTgt').innerHTML='แสดงเลข <b>'+sgTarget+'</b><small>'+(sgCA?'CA':'CC')+'</small>';return;}
  const sp=e.target.closest('[data-sgp]'); if(sp){sgPin[sp.dataset.sgp]^=1;SFX.play('tick');sgDraw();return;}
  if(e.target.closest('#sgNew')){sgNew();return;}
  if(e.target.closest('#sgCheck')){sgCheck();return;}
  const zr=e.target.closest('[data-zrs]'); if(zr){znRs=+zr.dataset.zrs;SFX.play('select');znUpdate(true);return;}
  const zl=e.target.closest('[data-zrl]'); if(zl){znRL=+zl.dataset.zrl;SFX.play('select');znUpdate(true);return;}
"""
INIT_EXTRA = " $('#dbV').addEventListener('input',()=>dbUpdate(true)); dbUpdate(false); sgDraw(); $('#znV').addEventListener('input',()=>znUpdate(true)); znUpdate(false);"

B = {}
B['district1'] = [
 ('แถบสีบนตัวถังไดโอดอยู่ด้านขาใด',
  ['แคโทด', 'แอโนด', 'เกต', 'ไม่บ่งบอกขาใด'],
  'แถบบนตัวถังแสดงด้านแคโทด ตรงกับเส้นขวางในสัญลักษณ์ไดโอด กระแสไหลจากแอโนดเข้าหาแถบ'),
 ('ไดโอดอยู่ในสภาวะไบแอสตรงเมื่อใด',
  ['ขั้วบวกของแหล่งจ่ายต่อเข้าแอโนด ขั้วลบต่อเข้าแคโทด', 'ขั้วบวกต่อเข้าแคโทด ขั้วลบต่อเข้าแอโนด', 'ต่อขาทั้งสองเข้าขั้วบวก', 'ไม่ต่อแหล่งจ่าย'],
  'ไบแอสตรงคือบวกเข้าฝั่ง P (แอโนด) ลบเข้าฝั่ง N (แคโทด) บริเวณปลอดพาหะแคบลงและไดโอดนำกระแสเมื่อแรงดันเกินแรงดันเข่า'),
 ('ไดโอดซิลิคอนเริ่มนำกระแสอย่างชัดเจนที่แรงดันไปหน้าประมาณเท่าใด',
  ['0.7 V', '0.3 V', '1.5 V', '5.1 V'],
  'ในการวิเคราะห์วงจรทั่วไปใช้แบบจำลองแรงดันตกคงที่ VF ≈ 0.7 V สำหรับไดโอดซิลิคอน'),
 ('ไดโอดเจอร์เมเนียมมีแรงดันไปหน้าโดยประมาณเท่าใด',
  ['0.3 V', '0.7 V', '0 V', '1.2 V'],
  'เจอร์เมเนียมมีช่องว่างพลังงานแคบกว่าซิลิคอน แรงดันไปหน้าจึงต่ำกว่า ประมาณ 0.3 V'),
 ('แหล่งจ่าย 5 V ต่ออนุกรมกับไดโอดซิลิคอน (ไบแอสตรง) และตัวต้านทาน 1 kΩ กระแสเท่าใด',
  ['4.3 mA', '5.0 mA', '5.7 mA', '0.7 mA'],
  'I = (Vs − VF) / R = (5 − 0.7) / 1,000 = 4.3 mA'),
 ('ใช้แบบจำลองไดโอดอุดมคติ แหล่งจ่าย 5 V อนุกรมกับไดโอด (ไบแอสตรง) และ 1 kΩ กระแสเท่าใด',
  ['5.0 mA', '4.3 mA', '0 mA', '50 mA'],
  'แบบจำลองอุดมคติถือว่า VF = 0 V กระแสจึงเท่ากับ 5 / 1,000 = 5.0 mA'),
 ('กลับขั้วไดโอดในวงจร 5 V และ 1 kΩ ให้เป็นไบแอสย้อนกลับ ข้อใดถูกต้อง',
  ['กระแสแทบเป็นศูนย์ และแรงดันเกือบ 5 V ตกคร่อมไดโอด', 'กระแส 4.3 mA ไหลย้อนทิศ', 'แรงดัน 5 V ตกคร่อมตัวต้านทาน', 'ไดโอดเสียทันที'],
  'ไบแอสย้อนกลับมีเพียงกระแสรั่วเล็กมาก แรงดันตกคร่อมตัวต้านทานเกือบศูนย์ แรงดันแหล่งจ่ายเกือบทั้งหมดจึงตกคร่อมไดโอด'),
 ('ไดโอดเบอร์ 1N4007 มีพิกัดกระแสเฉลี่ยไปหน้าและแรงดันย้อนกลับสูงสุดเท่าใด',
  ['1 A และ 1,000 V', '1 A และ 50 V', '3 A และ 1,000 V', '200 mA และ 100 V'],
  'ตระกูล 1N4001–1N4007 มีพิกัดกระแส 1 A เท่ากัน ต่างกันที่แรงดันย้อนกลับ ตั้งแต่ 50 V (1N4001) ถึง 1,000 V (1N4007)'),
 ('ไดโอดซิลิคอนต่อไบแอสตรงกับแหล่งจ่าย 0.5 V และตัวต้านทาน จะเกิดอะไรขึ้น',
  ['แทบไม่มีกระแส เพราะแรงดันยังไม่ถึงแรงดันเข่า', 'มีกระแสสูงมาก', 'ไดโอดพังทลาย', 'กระแสเท่ากับ 0.5 V / R พอดี'],
  'ต่ำกว่าแรงดันเข่าประมาณ 0.7 V กระแสไปหน้ายังน้อยมาก ไดโอดจึงแทบไม่นำ'),
 ('กระแสอิ่มตัวย้อนกลับ (IS) ของไดโอดซิลิคอนมีขนาดประมาณใด',
  ['เล็กมาก ระดับนาโนแอมแปร์หรือต่ำกว่า', 'ระดับแอมแปร์', 'เท่ากับกระแสไปหน้า', 'เป็นศูนย์พอดีเสมอ'],
  'กระแสย้อนกลับเกิดจากพาหะส่วนน้อย มีขนาดเล็กมากในไดโอดซิลิคอน และเพิ่มขึ้นเมื่ออุณหภูมิสูงขึ้น'),
 ('ไดโอดซิลิคอน 2 ตัวต่ออนุกรมไบแอสตรงกับ 9 V และ 1 kΩ กระแสเท่าใด',
  ['7.6 mA', '8.3 mA', '9.0 mA', '6.2 mA'],
  'ไดโอด 2 ตัวมีแรงดันตกรวม 1.4 V จึงได้ I = (9 − 1.4) / 1,000 = 7.6 mA'),
 ('ลักษณะกราฟกระแส-แรงดันของไดโอดในย่านไบแอสตรงเป็นอย่างไร',
  ['กระแสน้อยมากจนถึงแรงดันเข่า จากนั้นเพิ่มขึ้นอย่างรวดเร็ว', 'เป็นเส้นตรงผ่านจุดกำเนิดแบบตัวต้านทาน', 'กระแสคงที่ทุกแรงดัน', 'กระแสลดลงเมื่อแรงดันเพิ่ม'],
  'ไดโอดเป็นอุปกรณ์ไม่เชิงเส้น กระแสเพิ่มแบบเอกซ์โพเนนเชียล จึงเห็นเป็นเข่าที่ราว 0.6–0.7 V สำหรับซิลิคอน'),
 ('PIV (Peak Inverse Voltage) ของไดโอดหมายถึงอะไร',
  ['แรงดันย้อนกลับสูงสุดที่ไดโอดทนได้ก่อนพังทลาย', 'แรงดันไปหน้าที่ไดโอดเริ่มนำ', 'กระแสสูงสุดที่ไหลไปหน้า', 'กำลังสูงสุดของไดโอด'],
  'ในวงจรเรียงกระแส ต้องเลือกไดโอดที่ทนแรงดันย้อนกลับสูงกว่าแรงดันย้อนกลับสูงสุดที่เกิดขึ้นจริง'),
]
B['district2'] = [
 ('LED ย่อมาจากอะไร และเปล่งแสงเมื่อใด',
  ['Light Emitting Diode เปล่งแสงเมื่อไบแอสตรง', 'Light Emitting Diode เปล่งแสงเมื่อไบแอสย้อนกลับ', 'Low Energy Device เปล่งแสงทั้งสองทิศ', 'Light Energy Detector ใช้วัดแสง'],
  'LED เป็นไดโอดที่เปล่งแสงเมื่ออิเล็กตรอนและโฮลรวมตัวกันที่รอยต่อขณะไบแอสตรง'),
 ('ขาใดของ LED แบบ 5 มม. ทั่วไปคือแอโนด',
  ['ขาที่ยาวกว่า', 'ขาที่สั้นกว่า', 'ขาด้านที่ขอบตัวถังตัดเรียบ', 'ขาทั้งสองเป็นแอโนด'],
  'ขายาวคือแอโนด ส่วนขาสั้นและด้านที่ขอบตัวถังตัดเรียบคือแคโทด'),
 ('แหล่งจ่าย 5 V ขับ LED แดง VF = 2 V ที่ 15 mA ต้องใช้ตัวต้านทานกี่โอห์ม',
  ['200 Ω', '333 Ω', '133 Ω', '300 Ω'],
  'R = (5 − 2) / 0.015 = 200 Ω'),
 ('ตัวแสดงผล 7 ส่วน มีส่วนแสดงตัวเลขกี่ส่วน (ไม่นับจุด)',
  ['7 ส่วน ชื่อ a ถึง g', '8 ส่วน ชื่อ a ถึง h', '10 ส่วน ตามตัวเลข 0–9', '4 ส่วน แบบ BCD'],
  'มี 7 ส่วนชื่อ a b c d e f g และมักมีจุดทศนิยม dp อีก 1 ดวง'),
 ('การแสดงเลข 1 ต้องให้ส่วนใดติด',
  ['b และ c', 'e และ f', 'a และ d', 'f และ g'],
  'เลข 1 ใช้สองส่วนทางขวา คือ b (บนขวา) และ c (ล่างขวา)'),
 ('การแสดงเลข 7 ต้องให้ส่วนใดติด',
  ['a b c', 'a f g', 'b c g', 'a b g'],
  'เลข 7 คือแถบบน a กับสองส่วนทางขวา b และ c'),
 ('การแสดงเลข 0 ต้องให้ส่วนใด "ดับ"',
  ['g', 'a', 'd', 'ไม่มี ทุกส่วนติด'],
  'เลข 0 ใช้ a b c d e f ส่วนกลาง g ต้องดับ ถ้า g ติดด้วยจะกลายเป็นเลข 8'),
 ('ตัวแสดงผลแบบแคโทดร่วม (CC) ส่วนหนึ่งจะติดเมื่อใด',
  ['ขาของส่วนนั้นเป็น HIGH (ลอจิก 1)', 'ขาของส่วนนั้นเป็น LOW (ลอจิก 0)', 'ขาร่วมต่อไฟบวก', 'ทุกส่วนติดตลอดเวลา'],
  'แคโทดร่วมต่อขาร่วมลงกราวด์ ส่วนใดได้แรงดันบวก (HIGH) ที่แอโนดของมันก็จะไบแอสตรงและติด'),
 ('ตัวแสดงผลแบบแอโนดร่วม (CA) ขาร่วมต่อที่ใด และส่วนติดเมื่อใด',
  ['ขาร่วมต่อ +V ส่วนติดเมื่อขาเป็น LOW', 'ขาร่วมต่อกราวด์ ส่วนติดเมื่อขาเป็น HIGH', 'ขาร่วมต่อ +V ส่วนติดเมื่อขาเป็น HIGH', 'ขาร่วมลอยไว้'],
  'แอโนดร่วมต่อขาร่วมเข้าไฟบวก ต้องดึงแคโทดของส่วนนั้นลง LOW จึงจะเกิดไบแอสตรงและติด'),
 ('ไอซี 74LS47 เหมาะจะใช้ขับตัวแสดงผลชนิดใด',
  ['แอโนดร่วม เพราะเอาต์พุตเป็นแบบ active-low', 'แคโทดร่วม เพราะเอาต์พุตเป็นแบบ active-high', 'ใช้ได้กับ LCD เท่านั้น', 'ใช้ขับมอเตอร์'],
  '74LS47 เป็นตัวถอดรหัส BCD เป็น 7 ส่วนที่มีเอาต์พุต open-collector แบบ active-low จึงจับคู่กับแอโนดร่วม'),
 ('ไอซี CD4511 เหมาะจะใช้ขับตัวแสดงผลชนิดใด',
  ['แคโทดร่วม เพราะเอาต์พุตเป็นแบบ active-high', 'แอโนดร่วม เพราะเอาต์พุตเป็นแบบ active-low', 'ใช้ได้ทั้งสองแบบโดยไม่ต้องคำนึง', 'ใช้กับหลอดไส้เท่านั้น'],
  'CD4511 ถอดรหัส BCD และขับเอาต์พุต HIGH ให้ส่วนที่ต้องติด จึงจับคู่กับแคโทดร่วม'),
 ('ทำไมจึงควรใช้ตัวต้านทานแยกหนึ่งตัวต่อหนึ่งส่วน แทนตัวเดียวที่ขาร่วม',
  ['ความสว่างจะคงที่ไม่ว่าจะติดกี่ส่วน', 'ประหยัดตัวต้านทาน', 'ทำให้แสดงตัวเลขได้เร็วขึ้น', 'ทำให้ไม่ต้องใช้ไอซีถอดรหัส'],
  'ถ้าใช้ตัวต้านทานตัวเดียวที่ขาร่วม กระแสรวมถูกแบ่งตามจำนวนส่วนที่ติด เลข 1 จะสว่างกว่าเลข 8 อย่างเห็นได้ชัด'),
 ('การแสดงเลข 4 ต้องให้ส่วนใดติด',
  ['b c f g', 'a b c g', 'b c e g', 'a d f g'],
  'เลข 4 ใช้ส่วนบนซ้าย f ส่วนกลาง g และสองส่วนขวา b c'),
]
B['district3'] = [
 ('ซีเนอร์ไดโอดที่ใช้ควบคุมแรงดันต้องต่อแบบใด',
  ['ไบแอสย้อนกลับ ให้ทำงานที่แรงดันพังทลาย Vz', 'ไบแอสตรง ให้ได้ 0.7 V', 'ต่ออนุกรมกับโหลดแบบไบแอสตรง', 'ต่อขนานแบบไบแอสตรง'],
  'ซีเนอร์ออกแบบให้พังทลายย้อนกลับแบบไม่เสียหายที่ Vz และตรึงแรงดันคร่อมไว้ใกล้ค่า Vz'),
 ('วงจรซีเนอร์ Vin = 12 V, Vz = 5.1 V, Rs = 230 Ω กระแสผ่าน Rs เท่าใด',
  ['30 mA', '52 mA', '22 mA', '3.0 mA'],
  'Is = (Vin − Vz) / Rs = 6.9 / 230 = 0.030 A = 30 mA'),
 ('ต้องการ Vout = 5.1 V จาก Vin = 12 V โหลดดึง 20 mA และให้ซีเนอร์มีกระแส 10 mA ต้องใช้ Rs เท่าใด',
  ['230 Ω', '345 Ω', '690 Ω', '170 Ω'],
  'Rs = (Vin − Vz) / (Iz + IL) = 6.9 / 0.030 = 230 Ω'),
 ('ซีเนอร์ 5.1 V มีกระแส 20 mA กำลังสูญเสียในซีเนอร์เท่าใด',
  ['0.102 W', '0.255 W', '1.02 W', '0.0102 W'],
  'Pz = Vz × Iz = 5.1 × 0.020 = 0.102 W'),
 ('ซีเนอร์ 5.1 V พิกัด 0.5 W รับกระแสสูงสุดได้ประมาณเท่าใด',
  ['98 mA', '255 mA', '10 mA', '2.55 A'],
  'Izm = Pz(max) / Vz = 0.5 / 5.1 ≈ 0.098 A = 98 mA'),
 ('ในวงจรซีเนอร์ที่ Vin และ Rs คงที่ ถ้าโหลดดึงกระแสมากขึ้น กระแสซีเนอร์จะเป็นอย่างไร',
  ['ลดลง เพราะ Is คงที่และ Iz = Is − IL', 'เพิ่มขึ้นตามโหลด', 'คงที่เสมอ', 'กลับทิศ'],
  'เมื่อซีเนอร์ยังตรึงที่ Vz กระแส Is = (Vin − Vz)/Rs คงที่ โหลดดึงไปมากขึ้น ส่วนที่เหลือให้ซีเนอร์จึงลดลง'),
 ('ถ้ากระแสซีเนอร์ลดต่ำกว่า Izk จะเกิดอะไรขึ้น',
  ['ซีเนอร์หลุดการควบคุม แรงดันออกตกต่ำกว่า Vz', 'แรงดันออกเพิ่มเป็นสองเท่า', 'ซีเนอร์ร้อนจนไหม้', 'ไม่มีผลใด ๆ'],
  'Izk คือกระแสต่ำสุดที่ซีเนอร์ยังอยู่ในย่านพังทลาย ต่ำกว่านั้นจะออกจากย่านควบคุม แรงดันออกจะขึ้นกับตัวแบ่งแรงดัน Rs กับ RL แทน'),
 ('กรณีใดทำให้ซีเนอร์มีกำลังสูญเสียมากที่สุด เมื่อ Vin และ Rs คงที่',
  ['เมื่อถอดโหลดออก (IL = 0)', 'เมื่อโหลดดึงกระแสสูงสุด', 'เมื่อ Vin ต่ำที่สุด', 'เมื่อ Rs มีค่าสูงที่สุด'],
  'ไม่มีโหลด กระแส Is ทั้งหมดไหลผ่านซีเนอร์ Iz จึงสูงสุด ต้องตรวจว่า Pz กรณีนี้ไม่เกินพิกัด'),
 ('ถ้าต่อซีเนอร์ไดโอดแบบไบแอสตรง จะทำตัวอย่างไร',
  ['เหมือนไดโอดธรรมดา แรงดันตกประมาณ 0.7 V', 'ตรึงแรงดันที่ Vz เหมือนเดิม', 'ไม่นำกระแสเลย', 'เปล่งแสงเหมือน LED'],
  'ในทิศไบแอสตรง ซีเนอร์เป็นรอยต่อ PN ซิลิคอนธรรมดา จึงนำกระแสที่ราว 0.7 V'),
 ('วงจรซีเนอร์ 5.1 V ที่ควบคุมได้ปกติ ถ้า Vin เพิ่มจาก 9 V เป็น 12 V แรงดันออกจะเป็นอย่างไร',
  ['ยังคงประมาณ 5.1 V แต่กระแสซีเนอร์เพิ่มขึ้น', 'เพิ่มเป็น 12 V', 'ลดลงเป็น 0 V', 'เพิ่มขึ้นตามสัดส่วน 12/9'],
  'ซีเนอร์ตรึงแรงดันไว้ใกล้ Vz แรงดันส่วนเพิ่มไปตกคร่อม Rs ทำให้ Is และ Iz เพิ่มขึ้น'),
 ('Vin = 12 V, Rs = 220 Ω, Vz = 5.1 V, RL = 1 kΩ กระแสซีเนอร์ประมาณเท่าใด',
  ['26.3 mA', '31.4 mA', '5.1 mA', '36.5 mA'],
  'Is = 6.9 / 220 ≈ 31.4 mA, IL = 5.1 / 1,000 = 5.1 mA ดังนั้น Iz = 31.4 − 5.1 ≈ 26.3 mA'),
 ('Vin = 12 V, Rs = 220 Ω, Vz = 5.1 V และ RL = 100 Ω แรงดันออกเท่าใด',
  ['ประมาณ 3.75 V เพราะซีเนอร์ไม่ทำงาน', '5.1 V', '12 V', '6.9 V'],
  'ตรวจก่อนว่าถ้าไม่มีซีเนอร์ แรงดันที่แบ่งได้คือ 12 × 100 / 320 = 3.75 V ต่ำกว่า Vz ซีเนอร์จึงไม่พังทลาย Vout = 3.75 V'),
 ('สัญลักษณ์ของซีเนอร์ไดโอดต่างจากไดโอดธรรมดาอย่างไร',
  ['เส้นด้านแคโทดหักงอปลายคล้ายตัว Z', 'ไม่มีเส้นด้านแคโทด', 'มีลูกศรชี้ออกแบบ LED', 'มีวงกลมล้อมรอบเสมอ'],
  'ซีเนอร์ใช้สามเหลี่ยมและเส้นแคโทดเหมือนไดโอด แต่ปลายเส้นแคโทดหักงอคล้ายตัว Z'),
]


# ---------- รูปวงจรประกอบโจทย์ ----------
from qfig import series, zener, seg7
AUG = {
 'district1': {4: series('5 V', [('D', 'ไดโอด Si'), ('R', '1 kΩ')]),
               5: series('5 V', [('D', 'ไดโอดอุดมคติ'), ('R', '1 kΩ')]),
               6: series('5 V', [('D', 'กลับขั้ว', True), ('R', '1 kΩ')]),
               8: series('0.5 V', [('D', 'ไดโอด Si'), ('R', 'R')]),
               10: series('9 V', [('D', 'Si'), ('D', 'Si'), ('R', '1 kΩ')])},
 'district2': {2: series('5 V', [('R', 'R = ?'), ('LED', 'แดง Vf 2 V')], current='I = 15 mA'),
               4: seg7(), 5: seg7(), 6: seg7(), 12: seg7()},
 'district3': {1: zener('12 V', '230 Ω', '5.1 V', 'RL'),
               2: zener('12 V', 'Rs = ?', '5.1 V', 'IL 20 mA'),
               9: zener('9 → 12 V', 'Rs', '5.1 V', 'RL'),
               10: zener('12 V', '220 Ω', '5.1 V', '1 kΩ'),
               11: zener('12 V', '220 Ω', '5.1 V', '100 Ω')},
}
for _d, _m in AUG.items():
    for _i, _fig in _m.items():
        _q, _c, _e = B[_d][_i]; B[_d][_i] = (_q + _fig, _c, _e)

# ปรับสมดุลความยาวตัวเลือก (Rescue รอบ 1) ดู bank_rew.py
from bank_rew import apply as _rew
_rew(B, 'g4')

STAR = star_table([
 ('FORGE MASTER', 'คุมไดโอด LED 7 ส่วน และซีเนอร์ได้ครบ พร้อมต่อวงจรแสดงผลและวงจรจ่ายไฟจริง'),
 ('ANVIL SMITH', 'เกือบเต็ม ทบทวนข้อที่พลาดแล้วลองห้องทดลองบ่อชุบซีเนอร์อีกรอบ'),
 ('SPARK WORKER', 'ผ่านเกณฑ์แล้ว ฝึกตั้งตัวเลขทั้งแบบ CC และ CA ให้คล่อง'),
 ('HEAT APPRENTICE', 'เริ่มจับหลักได้ ทบทวน VF 0.7 V และสูตร Rs = (Vin − Vz) / (Iz + IL)'),
 ('FORGE VISITOR', 'มีพื้นฐานบ้างแล้ว เล่นให้ครบทั้ง 3 ห้องแล้วกลับมาทดสอบอีกครั้ง'),
 ('COLD IRON', 'ยังไม่คุ้นเนื้อหา เริ่มจากเตาไบแอส อ่านการ์ดทีละใบ แล้วเล่นแท่นทดสอบ'),
])

BADGES = r"""[
  {id:'perfect',  name:'FORGE MASTER',   desc:'Posttest ถูกครบ 6 ข้อ',                test:s => s.post === 6},
  {id:'zero2hero',name:'HOT START',      desc:'คะแนนเพิ่มขึ้น 3 ข้อขึ้นไปจาก Pretest',   test:s => (s.post - s.pre) >= 3},
  {id:'fast',     name:'QUICK SPARK',    desc:'ตอบถูกภายใน 8 วินาที',                 test:s => s.fastCorrect},
  {id:'labrat',   name:'BENCH SMITH',    desc:'เล่นห้องทดลองครบทั้งสามห้อง',           test:s => s.labs.lab1.length >= 3 && s.labs.lab2.length >= 3 && s.labs.lab3.length >= 3},
  {id:'combo',    name:'CHAIN STRIKE',   desc:'ตอบถูกติดกัน 5 ข้อขึ้นไป',             test:s => s.maxCombo >= 5},
  {id:'sweep',    name:'FULL FORGE',     desc:'ได้ 2/2 ครบทั้งสามห้อง',               test:s => s.postByD.district1 === 2 && s.postByD.district2 === 2 && s.postByD.district3 === 2}
]"""

ADVICE = r"""
  const tips=[];
  if(labCount('lab1')<3) tips.push('ในแท่นทดสอบไบแอส หาให้ครบทั้งไบแอสตรง ต่ำกว่าแรงดันเข่า และไบแอสย้อนกลับ');
  if(labCount('lab2')<3) tips.push('ในทั่งตัวเลข ตั้งเลขเป้าหมายให้ถูกทั้งแบบแคโทดร่วมและแอโนดร่วม');
  if(labCount('lab3')<3) tips.push('ในบ่อชุบซีเนอร์ หาให้ครบทั้งสถานะควบคุมได้ ซีเนอร์ไม่ทำงาน และกำลังเกินพิกัด');
  if(postInfo.stars===6) tips.push('ได้ครบ 6 ดาวแล้ว ไปต่อโซน 5 STORM HARBOR เพื่อใช้ไดโอดในวงจรเรียงกระแส');
  return tips;
"""

CFG = {
    'filename': 'game4_diode_forge.html',
    'title': 'DIODE FORGE : โรงตีไดโอด',
    'brand': 'DIODE FORGE',
    'edition': 'FORGE EDITION',
    'desc': 'เกมบทเรียน GNR2022 โซน 4: ไดโอดและการไบแอส LED และตัวแสดงผล 7 ส่วนแบบแอโนดร่วมและแคโทดร่วม ซีเนอร์ไดโอดและวงจรควบคุมแรงดัน',
    'ogdesc': 'เข้าโรงตีไดโอด 3 ห้อง จากเตาไบแอส สู่ทั่งตัวเลข 7 ส่วน จนถึงบ่อชุบซีเนอร์ที่ตรึงแรงดันให้คงที่',
    'favicon': "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='18' fill='%23120806'/><path d='M12 50 H34 M70 50 H88' stroke='%23ffd60a' stroke-width='7'/><path d='M34 28 L68 50 L34 72 Z' fill='%23ff6a1f'/><path d='M70 26 V74' stroke='%23ff6a1f' stroke-width='8'/></svg>",
    'theme': THEME,
    'extra_css': EXTRA_CSS,
    'arcade_label': 'ด่านไต่ปล่องโรงตี',
    'hero_svg': HERO,
    'subtitle': 'สวมบทบาท <b>ช่างตีไดโอด</b> ผ่าน 3 ห้องของโรงตี ตั้งแต่เตาไบแอสที่ทดสอบทิศของกระแส ทั่งตัวเลขที่สั่งตัวแสดงผล 7 ส่วน จนถึงบ่อชุบซีเนอร์ที่ตรึงแรงดันให้นิ่ง',
    'login_tag': 'Forge Smith Registration',
    'features': '<span>S1 · โซน 4</span><span>DIODE · LED · 7-SEG · ZENER</span><span>PRETEST / POSTTEST</span><span>ระบบดาว 6 ดวง</span>',
    'climb_text': 'ตัวละครไต่ปล่องโรงตีขึ้น 1 ชั้น ทันที',
    'zones_html': ZONES,
    'checks': [('Hall 01', 'เตาไบแอส'), ('Hall 02', 'ทั่งตัวเลข'), ('Hall 03', 'บ่อชุบซีเนอร์')],
    'post_desc': '6 ข้อใหม่ (ห้องละ 2 ข้อ) เพื่อวัดความเข้าใจหลังผ่านครบทั้ง 3 ห้อง',
    'report_tag': 'Forge Report',
    'course': COURSE,
    'footer_line': 'Season 1 · โซน 4 ไดโอด LED ตัวแสดงผล 7 ส่วน และซีเนอร์ — ภาคเรียนที่ 1/2569',
    'bank': bank_js(B),
    'skill_labels': "{district1:'ไดโอดและการไบแอส', district2:'LED และ 7 ส่วน', district3:'ซีเนอร์ไดโอด'}",
    'skey': 'gnr2022_diodeforge_v1_state',
    'star_table': STAR,
    'navstops': navstops('H1 BIAS', 'H2 7-SEG', 'H3 ZENER'),
    'lock_msg': 'ห้องนี้ยังไม่เปิด เดินตามลำดับก่อนนะครับ',
    'act': {'floor': 'ชั้น', 'top': 'ปากปล่องโรงตี', 'ground': 'ลานเตา', 'theme': 'forge'},
    'pre_sub': 'นี่คือเส้นฐานของคุณ ผ่านครบ 3 ห้องแล้วเรามาวัดกันใหม่',
    'go_first': 'เข้าห้องแรก',
    'lab_js': LAB_JS,
    'lab_wiring': LAB_WIRING,
    'init_extra': INIT_EXTRA,
    'badges': BADGES,
    'advice_js': ADVICE,
    'role': 'ช่างตีไดโอด',
    'filekey': 'GNR2022_Z4_diodeforge',
    'avatars': avatars('#1a0c08', ['#ff6a1f', '#ff2e88', '#ffd60a', '#ff4d4d', '#fdba74', '#f9a8d4']),
}
