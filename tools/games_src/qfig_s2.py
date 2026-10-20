# -*- coding: utf-8 -*-
"""รูปวงจรประกอบโจทย์ Season 2 (ต่อยอดจาก qfig) — ใช้ต่อท้ายข้อความโจทย์ ห้ามแทนที่ข้อความ"""
from qfig import _svg, _t, _gnd, _vres, A, G

def _tr(x, y, pnp=False, lab=''):
    """ทรานซิสเตอร์ในวงกลม: ขาเบสเข้าจากซ้ายที่ (x-34,y) ขา C ขึ้นบน ขา E ลงล่าง"""
    b = '<circle cx="%g" cy="%g" r="28"/>' % (x + 6, y)
    b += '<path d="M%g %g H%g M%g %g V%g M%g %g L%g %g V%g M%g %g L%g %g V%g"/>' % (
        x - 34, y, x - 6, x - 6, y - 16, y + 16, x - 6, y - 8, x + 18, y - 22, y - 40, x - 6, y + 8, x + 18, y + 22, y + 40)
    if pnp:
        b += '<path d="M%g %g L%g %g L%g %g" fill="currentColor"/>' % (x - 4, y + 9, x + 6, y + 11, x + 3, y + 19)
    else:
        b += '<path d="M%g %g L%g %g L%g %g" fill="currentColor"/>' % (x + 10, y + 16, x + 18, y + 22, x + 8, y + 24)
    if lab: b += _t(x + 40, y + 4, lab, anchor='start', size=11)
    return b

def sym(pnp=False):
    """สัญลักษณ์ทรานซิสเตอร์ไม่มีป้ายชนิด ให้ผู้เรียนดูทิศลูกศร"""
    body = _tr(180, 70, pnp)
    body += _t(140, 64, 'B', size=12) + _t(206, 26, 'C', anchor='start', size=12) + _t(206, 124, 'E', anchor='start', size=12)
    body += _t(250, 74, 'ชนิด = ?', anchor='start', size=12, color=G)
    return _svg(body, 140)

def relay(rb='RB', vin='GPIO 3.3 V', diode=True, coil='5 V · 70 Ω'):
    """ทรานซิสเตอร์ NPN ขับขดลวดรีเลย์จากขา GPIO พร้อมไดโอดกันกลับ"""
    body = '<path d="M150 14 H300"/>' + _t(300, 10, '+5 V', anchor='end', size=11)
    body += '<path d="M214 14 V30 M214 74 V88"/><rect x="200" y="30" width="28" height="44" rx="3" stroke="%s"/>' % A
    body += '<path d="M204 40 h20 M204 48 h20 M204 56 h20 M204 64 h20" stroke="%s" stroke-width="1.4"/>' % A
    body += _t(234, 56, 'รีเลย์ ' + coil, anchor='start', size=10)
    if diode:
        body += '<path d="M214 22 H170 V36 M170 70 V82 H214"/><path d="M160 66 L180 66 L170 50 Z" stroke="%s" fill="%s" fill-opacity=".25"/><path d="M160 48 H180" stroke="%s"/>' % (A, A, A)
        body += _t(156, 62, 'D', anchor='end', size=11)
    body += _t(20, 112, vin, anchor='start', size=11) + '<path d="M86 108 H100 M144 108 H180"/>'
    body += '<rect x="100" y="101" width="44" height="14" rx="2" stroke="%s"/>' % A + _t(122, 134, rb, size=11)
    body += _tr(214, 108)[0:0]
    body += '<path d="M180 108 H208 M208 92 V124 M208 98 L214 92 V88 M208 118 L214 124 V146"/><path d="M206 116 L214 124 L204 124" fill="currentColor"/>' + _gnd(214, 146)
    return _svg(body, 160)

def darlington():
    body = _t(30, 98, 'IB', anchor='start', size=11) + '<path d="M50 94 H96 M96 80 V108 M96 86 L120 72 V20 M96 102 L120 114 V122 H180 V112"/>'
    body += '<path d="M112 110 L120 114 L110 116" fill="currentColor"/>'
    body += '<path d="M180 112 V100 M180 128 V150 M180 100 L204 86 V20 M180 124 L204 138 V150"/>'
    body += '<path d="M168 112 H180 M180 100 V128"/><path d="M196 134 L204 138 L194 140" fill="currentColor"/>'
    body += '<path d="M120 20 H204"/>' + _t(160, 14, 'C ร่วม', size=11) + _gnd(204, 150)
    body += _t(84, 140, 'Q1 β1', size=11) + _t(236, 116, 'Q2 β2', anchor='start', size=11)
    return _svg(body, 162)

def _tri(x, y, h=56):
    """สามเหลี่ยมออปแอมป์ ขา − บน ขา + ล่าง (x,y = มุมซ้ายบน) คืน (body, (xm,ym-), (xm,ym+), (xo,yo))"""
    b = '<path d="M%g %g V%g L%g %g Z" stroke="%s"/>' % (x, y, y + h, x + 64, y + h / 2, A)
    b += _t(x + 9, y + 18, '−', size=13) + _t(x + 9, y + h - 8, '+', size=13)
    return b, (x, y + 14), (x, y + h - 14), (x + 64, y + h / 2)

def opamp(kind='inv', ri='Ri', rf='Rf', vin='Vin', vout='Vo'):
    """kind: inv | non | buf | cmp (เปรียบเทียบ ไม่มีป้อนกลับ)"""
    tb, m, p, o = _tri(170, 50)
    b = tb + '<path d="M%g %g H%g"/>' % (o[0], o[1], o[0] + 46) + _t(o[0] + 50, o[1] + 4, vout, anchor='start', size=11)
    if kind == 'inv':
        b += '<path d="M40 %g H70 M114 %g H%g"/><rect x="70" y="%g" width="44" height="14" rx="2" stroke="%s"/>' % (m[1], m[1], m[0], m[1] - 7, A)
        b += _t(92, m[1] - 12, ri, size=11) + _t(36, m[1] + 4, vin, anchor='end', size=11)
        b += '<path d="M150 %g V20 H184 M228 20 H260 V%g"/><rect x="184" y="13" width="44" height="14" rx="2" stroke="%s"/>' % (m[1], o[1], A) + _t(206, 10, rf, size=11)
        b += '<path d="M150 %g H170"/>' % m[1]
        b += '<path d="M%g %g H140 V128"/>' % (p[0], p[1]) + _gnd(140, 128)
    elif kind == 'non':
        b += '<path d="M40 %g H%g"/>' % (p[1], p[0]) + _t(36, p[1] + 4, vin, anchor='end', size=11)
        b += '<path d="M150 %g V20 H184 M228 20 H260 V%g M150 %g H170"/><rect x="184" y="13" width="44" height="14" rx="2" stroke="%s"/>' % (m[1], o[1], m[1], A) + _t(206, 10, rf, size=11)
        b += '<path d="M150 %g V90"/><rect x="143" y="90" width="14" height="30" rx="2" stroke="%s"/><path d="M150 120 V128"/>' % (m[1], A) + _gnd(150, 128) + _t(136, 110, ri, anchor='end', size=11)
    elif kind == 'buf':
        b += '<path d="M40 %g H%g"/>' % (p[1], p[0]) + _t(36, p[1] + 4, vin, anchor='end', size=11)
        b += '<path d="M150 %g V20 H260 V%g M150 %g H170"/>' % (m[1], o[1], m[1])
    else:
        b += '<path d="M60 %g H%g M60 %g H%g"/>' % (p[1], p[0], m[1], m[0]) + _t(56, p[1] + 4, vin, anchor='end', size=11) + _t(56, m[1] + 4, ri, anchor='end', size=11)
    return _svg(b, 140)

P555 = {1: 'GND', 2: 'TRIG', 3: 'OUT', 4: 'RESET', 5: 'CONT', 6: 'THRES', 7: 'DISCH', 8: 'VCC'}
def ic555(mark=None, names=True):
    """ตัวถัง DIP-8 ของ 555 ขา 1–4 ซ้ายบนลงล่าง ขา 8–5 ขวาบนลงล่าง · mark = เลขขาที่ต้องการชี้ (ไม่บอกชื่อ)"""
    b = '<rect x="140" y="14" width="80" height="112" rx="6" stroke="%s"/><path d="M170 14 a10 10 0 0 0 20 0"/>' % A
    b += _t(180, 76, '555', size=14)
    for i in range(4):
        y = 30 + i * 26
        for pin, x0, x1, tx, anc in ((i + 1, 116, 140, 110, 'end'), (8 - i, 220, 244, 250, 'start')):
            col = G if pin == mark else 'currentColor'
            b += '<path d="M%g %g H%g" stroke="%s" stroke-width="%s"/>' % (x0, y, x1, col, 4 if pin == mark else 2)
            lab = str(pin) + ((' ' + P555[pin]) if names and pin != mark else (' ?' if pin == mark else ''))
            b += _t(tx, y + 4, lab, anchor=anc, size=11, color=col)
    return _svg(b, 140)

def timer555(mode='astable', ra='RA', rb='RB', c='C'):
    """บล็อกวงจร 555 แบบย่อ: astable (RA, RB, C) หรือ mono (R, C, ปุ่มกด)"""
    b = '<rect x="150" y="30" width="70" height="86" rx="6" stroke="%s"/>' % A + _t(185, 78, '555', size=13)
    b += '<path d="M60 14 H300"/>' + _t(60, 10, '+VCC', anchor='start', size=11)
    b += '<path d="M185 14 V30"/>' + _t(190, 26, '8', anchor='start', size=9)
    b += '<path d="M220 72 H270"/>' + _t(274, 76, 'OUT (3)', anchor='start', size=11)
    if mode == 'astable':
        b += _vres(110, 14, 52, ra) + _vres(110, 52, 92, rb)
        b += '<path d="M110 52 H150"/>' + _t(146, 48, '7', anchor='end', size=9)
        b += '<path d="M110 92 H150 M130 92 V104 H150"/>' + _t(146, 88, '6', anchor='end', size=9) + _t(146, 116, '2', anchor='end', size=9)
        b += '<path d="M110 92 V108 M98 108 H122 M98 114 H122 M110 114 V132"/>' + _gnd(110, 132) + _t(92, 116, c, anchor='end', size=11)
    else:
        b += _vres(110, 14, 60, ra) + '<path d="M110 60 H150 M110 60 V100 M98 100 H122 M98 106 H122 M110 106 V132"/>' + _gnd(110, 132)
        b += _t(146, 56, '6,7', anchor='end', size=9) + _t(92, 108, c, anchor='end', size=11)
        b += '<path d="M150 100 H135 V122"/><circle cx="135" cy="124" r="2"/><path d="M135 132 l8 -6"/>' + _t(146, 96, '2', anchor='end', size=9)
        b += _t(150, 138, 'ปุ่ม TRIG ลงกราวด์', anchor='start', size=10)
    return _svg(b, 146)
