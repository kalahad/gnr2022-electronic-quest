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
