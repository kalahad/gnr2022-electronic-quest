# -*- coding: utf-8 -*-
"""รูปวงจรขนาดเล็กสำหรับใส่ในตัวโจทย์ (SVG ฝังในข้อความ ใช้สีตามธีมผ่าน currentColor และตัวแปร CSS)
ใช้: from qfig import series, zener, bands, seg7, parallel, E12_NOTE"""

W = 360

def _svg(body, h):
    return ('<svg class="qfig" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="รูปวงจรประกอบโจทย์">'
            '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</g></svg>') % (W, h, body)

def _t(x, y, s, anchor='middle', size=12, color='currentColor'):
    return '<text x="%g" y="%g" text-anchor="%s" font-size="%d" fill="%s" stroke="none" font-family="inherit">%s</text>' % (x, y, anchor, size, color, s)

def _part(kind, cx, y, label, rev=False):
    """วาดชิ้นส่วนแนวนอนกว้าง 44 px ศูนย์กลาง cx บนเส้น y"""
    a = 'var(--ember,#c2410c)'
    if kind == 'R':
        g = '<rect x="%g" y="%g" width="44" height="14" rx="2" stroke="%s"/>' % (cx - 22, y - 7, a)
    elif kind in ('D', 'LED', 'Z'):
        d = -1 if rev else 1
        x0, x1 = cx - 12 * d, cx + 12 * d
        g = '<path d="M%g %g L%g %g L%g %g Z" stroke="%s" fill="%s" fill-opacity=".25"/>' % (x0, y - 11, x1, y, x0, y + 11, a, a)
        if kind == 'Z':
            g += '<path d="M%g %g L%g %g L%g %g L%g %g" stroke="%s"/>' % (x1 - 4 * d, y - 13, x1, y - 11, x1, y + 11, x1 + 4 * d, y + 13, a)
        else:
            g += '<path d="M%g %g V%g" stroke="%s"/>' % (x1, y - 12, y + 12, a)
        g += '<path d="M%g %g H%g M%g %g H%g" />' % (cx - 22, y, x0 if d == 1 else x1, x1 if d == 1 else x0, y, cx + 22)
        if kind == 'LED':
            g += '<path d="M%g %g l7 -8 M%g %g l7 -8" stroke="var(--gold,#b8860b)"/>' % (cx + 2, y - 14, cx + 9, y - 12)
    else:
        g = ''
    return g + _t(cx, y + 30, label, size=11)

def series(vs, parts, current=None):
    """แหล่งจ่าย vs (ข้อความ) ต่ออนุกรมกับ parts = [(ชนิด 'R'|'D'|'LED'|'Z', ป้าย, rev?), ...]"""
    h, top, bot = 112, 26, 92
    n = len(parts); xs = [115 + i * (160 / (n - 1)) for i in range(n)] if n > 1 else [200]
    body = '<path d="M30 %d V52 M30 60 V%d H330 V%d" />' % (top, bot, top)
    body += '<path d="M18 52 H42 M24 60 H36" stroke-width="2.6"/>'
    body += _t(12, 48, '+', size=12) + _t(40, 80, vs, anchor='start', size=12)
    # สายด้านบนแบ่งเป็นช่วงระหว่างชิ้นส่วน
    edges = [30] + [v for x in xs for v in (x - 22, x + 22)] + [330]
    for i in range(0, len(edges), 2):
        body += '<path d="M%g %d H%g"/>' % (edges[i], top, edges[i + 1])
    for (k, lab, *r), x in zip(parts, xs):
        body += _part(k, x, top, lab, rev=bool(r and r[0]))
    if current:
        body += _t(330, 106, current, anchor='end', size=11, color='var(--gold,#b8860b)')
    return _svg(body, h)

def zener(vin, rs, vz, rl):
    """วงจรควบคุมแรงดันซีเนอร์: Vin – Rs – โหนด – (ซีเนอร์ลงกราวด์) ∥ (RL ลงกราวด์ หรือ None)"""
    h, top, bot = 130, 24, 112
    a = 'var(--ember,#c2410c)'
    body = '<path d="M30 %d V54 M30 62 V%d H330 M30 %d H96 M140 %d H330 M210 92 V%d" />' % (top, bot, top, top, bot)
    body += '<path d="M18 54 H42 M24 62 H36" stroke-width="2.6"/>' + _t(12, 50, '+', size=12) + _t(40, 86, vin, anchor='start')
    body += '<rect x="96" y="%d" width="44" height="14" rx="2" stroke="%s"/>' % (top - 7, a) + _t(118, top + 28, rs if rs.startswith('Rs') else 'Rs = ' + rs, size=11)
    # ซีเนอร์แนวตั้ง แคโทดอยู่บน (ไบแอสย้อนกลับ)
    body += '<path d="M198 92 L222 92 L210 66 Z" stroke="%s" fill="%s" fill-opacity=".25"/><path d="M194 70 L198 66 H222 L226 62" stroke="%s"/><path d="M210 %d V66"/>' % (a, a, a, top)
    body += _t(232, 84, vz if vz.startswith('Vz') else 'Vz ' + vz, anchor='start', size=11)
    if rl:
        body += '<path d="M330 %d V50 M330 82 V%d"/><rect x="323" y="50" width="14" height="32" rx="2" stroke="%s"/>' % (top, bot, a) + _t(318, 70, rl if rl.startswith(('RL', 'I')) else 'RL = ' + rl, anchor='end', size=11)
    else:
        body += _t(320, 70, 'ไม่มีโหลด', anchor='end', size=11)
    return _svg(body, h)

COL = {'ดำ': '#111', 'น้ำตาล': '#7c4a1e', 'แดง': '#ef4444', 'ส้ม': '#f97316', 'เหลือง': '#facc15', 'เขียว': '#22c55e',
       'น้ำเงิน': '#3b82f6', 'ม่วง': '#8b5cf6', 'เทา': '#9ca3af', 'ขาว': '#f8fafc', 'ทอง': '#c9a227', 'เงิน': '#cbd5e1'}

def bands(names):
    """ภาพตัวต้านทานพร้อมแถบสีตามลำดับ (แถบสุดท้ายแยกห่างเป็นค่าคลาดเคลื่อน)"""
    names = names.split() if isinstance(names, str) else names
    n = len(names); body = '<path d="M20 45 H90 M270 45 H340" stroke-width="4"/>'
    body += '<rect x="90" y="20" width="180" height="50" rx="20" fill="#d6b48a" stroke="#a0825c"/>'
    xs = [114 + i * 26 for i in range(n - 1)] + [246]
    for nm, x in zip(names, xs):
        body += '<rect x="%d" y="20" width="12" height="50" fill="%s" stroke="none"/>' % (x, COL[nm])
        body += _t(x + 6, 86, nm, size=10)
    return _svg(body, 94)

def seg7():
    """ตัวแสดงผล 7 ส่วนพร้อมชื่อส่วน a–g (ไม่ติดไฟ)"""
    s = ('<g stroke="none" fill="currentColor" fill-opacity=".18">'
         '<rect x="150" y="8" width="60" height="9" rx="4"/><rect x="211" y="18" width="9" height="40" rx="4"/>'
         '<rect x="211" y="70" width="9" height="40" rx="4"/><rect x="150" y="111" width="60" height="9" rx="4"/>'
         '<rect x="140" y="70" width="9" height="40" rx="4"/><rect x="140" y="18" width="9" height="40" rx="4"/>'
         '<rect x="150" y="59" width="60" height="9" rx="4"/></g>')
    for lab, x, y in (('a', 180, 6), ('b', 232, 42), ('c', 232, 94), ('d', 180, 136), ('e', 128, 94), ('f', 128, 42), ('g', 180, 54)):
        s += _t(x, y, lab, size=13, color='var(--ember,#c2410c)')
    return _svg(s, 140)

def parallel(r1, r2, vlabel=None):
    a = 'var(--ember,#c2410c)'
    body = '<path d="M40 50 H110 M110 22 V78 M250 22 V78 M250 50 H320 M110 22 H158 M202 22 H250 M110 78 H158 M202 78 H250"/>'
    body += '<rect x="158" y="15" width="44" height="14" rx="2" stroke="%s"/><rect x="158" y="71" width="44" height="14" rx="2" stroke="%s"/>' % (a, a)
    body += _t(180, 10, r1, size=11) + _t(180, 100, r2, size=11) + _t(40, 44, 'A', size=12) + _t(320, 44, 'B', size=12)
    return _svg(body, 106)

E12_NOTE = ('<div class="qnote">ค่ามาตรฐาน E12 (±10%) คือชุดค่าที่ผู้ผลิตทำขาย ซ้ำทุกหลักสิบ: '
            '<b>10 12 15 18 22 27 33 39 47 56 68 82</b> × 1, × 10, × 100 ...</div>')
E24_NOTE = ('<div class="qnote">E24 (±5%) ละเอียดกว่า มีค่า E12 ทั้งหมด และเพิ่ม <b>11 13 16 20 24 30 36 43 51 62 75 91</b></div>')

def chain(parts):
    """ตัวต้านทานต่ออนุกรมระหว่างจุด A กับ B (ไม่มีแหล่งจ่าย)"""
    n = len(parts); xs = [130 + i * 100 for i in range(n)]
    edges = [40] + [v for x in xs for v in (x - 22, x + 22)] + [320]
    body = ''.join('<path d="M%g 40 H%g"/>' % (edges[i], edges[i + 1]) for i in range(0, len(edges), 2))
    for (k, lab), x in zip(parts, xs): body += _part(k, x, 40, lab)
    body += _t(40, 30, 'A', size=12) + _t(320, 30, 'B', size=12)
    return _svg(body, 84)

# ======================= รูปเพิ่มเติม (โซน 2, 3, 5, 6) =======================
A = 'var(--ember,#c2410c)'; G = 'var(--gold,#b8860b)'

def _vres(x, y1, y2, label, ldr=False, side='left'):
    """ตัวต้านทานแนวตั้งระหว่าง y1–y2 (สายต่อเข้าปลายบนล่าง)"""
    m = (y1 + y2) / 2
    g = '<path d="M%g %g V%g M%g %g V%g"/>' % (x, y1, m - 16, x, m + 16, y2)
    g += '<rect x="%g" y="%g" width="14" height="32" rx="2" stroke="%s"/>' % (x - 7, m - 16, A)
    if ldr:
        g += '<path d="M%g %g l9 7 M%g %g l9 7" stroke="%s"/>' % (x - 24, m - 16, x - 24, m - 6, G)
    lx = x - 14 if side == 'left' else x + 14
    g += _t(lx - (12 if ldr and side == 'left' else 0), m + 4, label, anchor='end' if side == 'left' else 'start', size=11)
    return g

def _gnd(x, y):
    return '<path d="M%g %g H%g M%g %g H%g M%g %g H%g"/>' % (x - 10, y, x + 10, x - 6, y + 4, x + 6, x - 2, y + 8, x + 2)

def _bat(x, y, label):
    return ('<path d="M%g %g H%g M%g %g H%g" stroke-width="2.6"/>' % (x - 12, y, x + 12, x - 6, y + 8, x + 6)
            + _t(x - 16, y - 2, '+', size=12) + _t(x + 16, y + 8, label, anchor='start', size=12))

def divider(vin, rtop, rbot, out='Vout', ldr_top=False, ldr_bot=False, load=None):
    """วงจรแบ่งแรงดันแนวตั้ง: +Vin – R บน – จุดวัด – R ล่าง – GND (มีโหลดคร่อม R ล่างได้)"""
    x = 180; body = '<path d="M60 20 H%g V30 M60 20 V66 M60 74 V150 H%g"/>' % (x, x + (110 if load else 70))
    body += _bat(60, 66, vin)
    body += _vres(x, 30, 76, rtop, ldr=ldr_top) + _vres(x, 94, 150, rbot, ldr=ldr_bot)
    body += '<path d="M%g 76 V94 M%g 85 H%g"/><circle cx="%g" cy="85" r="3" fill="currentColor"/>' % (x, x, x + (110 if load else 70), x)
    if load:
        body += _vres(x + 110, 85, 150, '', side='right') + _t(x + 126, 122, load, anchor='start', size=11)
        body += _t(x + 60, 78, out, size=12, color=G)
    else:
        body += '<circle cx="%g" cy="85" r="3"/>' % (x + 70) + _t(x + 78, 89, out, anchor='start', size=12, color=G)
    return _svg(body, 160)

def pot_two_legs(vin):
    """VR ที่ใช้เพียงขากลางกับขาปลาย 1 ข้าง (ขา 1 ลอย)"""
    x = 180
    body = '<path d="M60 20 H%g V30 M60 20 V66 M60 74 V150 H%g V130"/>' % (x, x) + _bat(60, 66, vin)
    body += '<rect x="%g" y="30" width="14" height="100" rx="2" stroke="%s"/>' % (x - 7, A)
    body += '<path d="M%g 80 H%g M%g 80 l8 -5 M%g 80 l8 5" stroke="%s"/>' % (x + 7, x + 40, x + 7, x + 7, A)
    body += '<path d="M%g 80 H%g"/><circle cx="%g" cy="80" r="3"/>' % (x + 40, x + 80, x + 80) + _t(x + 88, 84, 'จุดวัด', anchor='start', size=11)
    body += '<path d="M%g 30 V12" stroke-dasharray="3 4"/>' % x
    body += _t(x - 12, 36, 'ขา 1 (ไม่ได้ต่อ)', anchor='end', size=10) + _t(x + 12, 72, 'ขา 2', anchor='start', size=10) + _t(x - 12, 128, 'ขา 3', anchor='end', size=10)
    body += _t(x - 12, 84, 'VR 10 kΩ', anchor='end', size=11)
    return _svg(body, 160)

def _ac(x, y, label, below=False):
    return ('<circle cx="%g" cy="%g" r="16"/><path d="M%g %g c4 -9 8 -9 12 0 s8 9 12 0" />' % (x, y, x - 12, y)
            + (_t(x + 20, y - 20, label, anchor='start', size=11) if below else _t(x - 22, y + 4, label, anchor='end', size=11)))

def _dio(x1, y1, x2, y2):
    """ไดโอดบนเส้นตรงจาก (x1,y1) แอโนด ไป (x2,y2) แคโทด"""
    import math
    L = math.hypot(x2 - x1, y2 - y1); ang = math.degrees(math.atan2(y2 - y1, x2 - x1)); m = L / 2
    g = '<g transform="translate(%g %g) rotate(%g)">' % (x1, y1, ang)
    g += '<path d="M0 0 H%g M%g 0 H%g"/>' % (m - 10, m + 10, L)
    g += '<path d="M%g -9 L%g 0 L%g 9 Z" stroke="%s" fill="%s" fill-opacity=".25"/><path d="M%g -10 V10" stroke="%s"/>' % (m - 10, m + 8, m - 10, A, A, m + 8, A)
    return g + '</g>'

def halfwave(vin, rl='RL', cap=None, d='D1'):
    """เรียงกระแสครึ่งคลื่น: แหล่ง AC – ไดโอด – RL (มีตัวเก็บประจุคร่อมได้)"""
    body = '<path d="M90 24 V54 M90 86 V116 H290 V100 M90 24 H130 M170 24 H290 V60"/>' + _ac(90, 70, vin)
    body += _dio(130, 24, 170, 24) + _t(150, 14, d, size=11)
    body += '<rect x="283" y="60" width="14" height="40" rx="2" stroke="%s"/>' % A + _t(304, 84, rl, anchor='start', size=11)
    if cap:
        body += '<path d="M230 24 V64 M230 76 V116 M216 64 H244 M216 76 H244" />' + _t(222, 72, cap, anchor='end', size=10)
    return _svg(body, 130)

def bridge(vin, rl='RL', cap=None):
    """เรียงกระแสเต็มคลื่นแบบบริดจ์ D1–D4"""
    cx, cy, r = 160, 70, 44
    L, T, R, Bm = (cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)
    body = _ac(50, 62, vin, below=True)
    body += '<path d="M50 46 V8 H220 V70 H%g M50 78 V92 H96 V70 H%g"/>' % (R[0], L[0])
    body += _dio(L[0], L[1], T[0], T[1]) + _dio(R[0], R[1], T[0], T[1]) + _dio(Bm[0], Bm[1], L[0], L[1]) + _dio(Bm[0], Bm[1], R[0], R[1])
    for lab, (x, y) in (('D1', (cx - 30, cy - 30)), ('D2', (cx + 30, cy - 30)), ('D3', (cx - 30, cy + 34)), ('D4', (cx + 30, cy + 34))):
        body += _t(x, y, lab, size=10)
    body += '<path d="M%g %g H310 V52 M%g %g H310 V92"/>' % (T[0], T[1], Bm[0], Bm[1])
    body += '<rect x="303" y="52" width="14" height="40" rx="2" stroke="%s"/>' % A + _t(298, 76, rl, anchor='end', size=11)
    body += _t(318, 22, '+', size=12, color=G) + _t(318, 124, '−', size=12, color=G)
    if cap:
        body += '<path d="M260 26 V64 M260 76 V114 M246 64 H274 M246 76 H274"/>' + _t(246, 96, cap, anchor='end', size=10)
    return _svg(body, 130)

def bjt(ib='IB', ic='IC', ie='IE', beta=None):
    """ทรานซิสเตอร์ NPN พร้อมทิศกระแสที่ขา B C E"""
    body = '<circle cx="200" cy="70" r="30"/><path d="M120 70 H186 M186 50 V90 M186 60 L214 40 V14 M186 80 L214 100 V128"/>'
    body += '<path d="M206 94 L214 100 L204 102" fill="currentColor"/>'
    body += '<path d="M140 62 l10 8 l-10 8" stroke="%s"/><path d="M222 24 l-8 10 l-8 -10" stroke="%s"/><path d="M222 112 l-8 10 l-8 -10" stroke="%s"/>' % (G, G, G)
    body += _t(150, 56, 'B · ' + ib, size=11, color=G) + _t(228, 30, 'C · ' + ic, anchor='start', size=11, color=G) + _t(228, 120, 'E · ' + ie, anchor='start', size=11, color=G)
    if beta: body += _t(260, 74, beta, anchor='start', size=12)
    return _svg(body, 140)

def proj6():
    """โครงงานที่ 6 วงจรหรี่ไฟอัตโนมัติ: R2 + VR2 จาก +9 V เข้าเบส, LDR จากเบสลงกราวด์, R3 + LED2 ที่คอลเล็กเตอร์"""
    body = '<path d="M30 14 H300"/>' + _t(30, 10, '+9 V', anchor='start', size=11)
    body += _vres(110, 14, 52, 'R2 24 kΩ') + _vres(110, 52, 92, 'VR2 10 kΩ')
    body += '<path d="M110 92 V100"/><circle cx="110" cy="100" r="3" fill="currentColor"/>'
    body += _vres(110, 100, 150, 'LDR', ldr=True) + _gnd(110, 150)
    body += '<path d="M110 100 H186 M186 86 V114 M186 94 L214 80 V70 M186 106 L214 120 V150"/><path d="M206 116 L214 120 L204 122" fill="currentColor"/>' + _gnd(214, 150)
    body += _t(196, 134, 'Q1', anchor='start', size=11)
    body += _vres(214, 14, 40, 'R3 330 Ω', side='right')
    body += '<path d="M214 40 V46 M214 66 V70"/><path d="M203 46 L225 46 L214 64 Z" stroke="%s" fill="%s" fill-opacity=".25"/><path d="M203 66 H225" stroke="%s"/>' % (A, A, A)
    body += '<path d="M228 52 l8 -6 M228 60 l8 -6" stroke="%s"/>' % G + _t(240, 62, 'LED2', anchor='start', size=11)
    body += _t(150, 94, 'VB', size=10, color=G)
    return _svg(body, 162)

def led_collector():
    """ทรานซิสเตอร์อิ่มตัวขับ LED ผ่าน R 330 Ω จาก 9 V"""
    body = '<path d="M30 14 H260"/>' + _t(30, 10, '+9 V', anchor='start', size=11)
    body += _vres(200, 14, 52, 'R 330 Ω', side='right')
    body += '<path d="M200 52 V58 M200 78 V86"/><path d="M189 58 L211 58 L200 76 Z" stroke="%s" fill="%s" fill-opacity=".25"/><path d="M189 78 H211" stroke="%s"/>' % (A, A, A)
    body += _t(214, 72, 'LED VF 2 V', anchor='start', size=11)
    body += '<path d="M130 110 H172 M172 96 V124 M172 104 L200 90 V86 M172 116 L200 130 V146"/><path d="M192 126 L200 130 L190 132" fill="currentColor"/>' + _gnd(200, 146)
    body += _t(126, 114, 'เบส (อิ่มตัว)', anchor='end', size=11) + _t(214, 118, 'VCE(sat) ≈ 0.2 V', anchor='start', size=11)
    return _svg(body, 160)

def base_drive(v='5 V', rb='RB = ?'):
    body = _t(30, 74, v, anchor='start', size=12) + '<circle cx="62" cy="70" r="3"/><path d="M65 70 H96 M140 70 H186 M186 56 V84 M186 64 L214 50 V20 M186 76 L214 90 V120"/>'
    body += '<rect x="96" y="63" width="44" height="14" rx="2" stroke="%s"/>' % A + _t(118, 98, rb, size=11)
    body += '<path d="M206 86 L214 90 L204 92" fill="currentColor"/>' + _gnd(214, 120) + _t(222, 16, 'C', anchor='start', size=11)
    body += _t(160, 60, 'IB = 0.1 mA →', size=10, color=G) + _t(222, 70, 'VBE = 0.7 V', anchor='start', size=11)
    return _svg(body, 132)

def pin1_node(sw='S1 รีดสวิตช์'):
    """ขา 1 ของไอซีเสียงเพลง: R1 10 kΩ ดึงขึ้นไป +5 V และสวิตช์ (รีดสวิตช์หรือทรานซิสเตอร์) ดึงลงกราวด์"""
    body = '<path d="M60 14 H200"/>' + _t(60, 10, '+5 V (จาก 7805)', anchor='start', size=11)
    body += _vres(120, 14, 62, 'R1 10 kΩ') + '<path d="M120 62 V72 M120 72 H250"/><circle cx="120" cy="72" r="3" fill="currentColor"/>'
    body += '<rect x="250" y="56" width="74" height="40" rx="6" stroke="%s"/>' % A + _t(287, 74, 'UM66', size=11) + _t(287, 88, 'ขา 1', size=10, color=G)
    if sw.startswith('?'):
        body += '<path d="M120 72 V92 M120 128 V140"/><rect x="104" y="92" width="32" height="36" rx="4" stroke-dasharray="4 4" stroke="%s"/>' % A + _t(120, 115, '?', size=14, color=G)
    elif 'ทรานซิสเตอร์' in sw:
        body += '<path d="M120 72 V92 M86 110 H106 M106 98 V122 M106 104 L120 96 M106 116 L120 126 V140"/><path d="M114 123 L120 126 L112 128" fill="currentColor"/>'
        body += _t(80, 114, 'จาก LDR', anchor='end', size=10)
    else:
        body += '<path d="M120 72 V96 M120 118 V140 M120 96 L134 116"/><circle cx="120" cy="96" r="2.5"/><circle cx="120" cy="118" r="2.5"/>'
    body += _gnd(120, 140) + _t(144, 112, sw, anchor='start', size=11)
    return _svg(body, 152)

def pn(forward=True):
    """ก้อนรอยต่อ PN ต่อแหล่งจ่าย (ไบแอสตรง: + เข้า P)"""
    body = '<rect x="100" y="20" width="80" height="50" fill="#ef4444" fill-opacity=".14" stroke="%s"/><rect x="180" y="20" width="80" height="50" fill="#3b82f6" fill-opacity=".14" stroke="%s"/>' % (A, A)
    body += _t(140, 50, 'P', size=16) + _t(220, 50, 'N', size=16)
    body += '<path d="M100 45 H70 V110 H160 M200 110 H290 V45 H260"/>'
    l, s = (160, 172) if forward else (172, 160)
    body += '<path d="M%g 98 V122 M%g 104 V116" stroke-width="2.6"/>' % (l, s)
    body += _t(l, 92, '+', size=12, color=G) + _t(s, 92, '−', size=12)
    body += '<path d="M160 110 H172" stroke-width="0"/><path d="M172 110 H200"/>'
    return _svg(body, 130)
