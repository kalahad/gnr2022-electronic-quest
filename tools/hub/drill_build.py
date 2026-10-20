# -*- coding: utf-8 -*-
"""สร้าง rescue.html และ hard.html จากเครื่องยนต์เดียวกัน (drill_head.html + drill_script.html)
usage: python3 tools/hub/drill_build.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rescue_src, hard_src
HEAD = open(os.path.join(HERE, 'drill_head.html'), encoding='utf-8').read()
SCRIPT = open(os.path.join(HERE, 'drill_script.html'), encoding='utf-8').read()

def page(fname, title, brand, desc, items, meta, conf):
    for z, v in items.items():
        for q, c, e, m in v: assert len(c) == 4 and len(set(c)) == 4, q
    data = {z: [{'q': q, 'c': c, 'e': e, 'm': m} for q, c, e, m in v] for z, v in items.items()}
    out = HEAD.replace('__TITLE__', title).replace('__BRAND__', brand).replace('__DESC__', desc) + SCRIPT
    out = out.replace('/*__DATA__*/{}', json.dumps(data, ensure_ascii=False)).replace('/*__META__*/{}', json.dumps(meta, ensure_ascii=False))
    out = out.replace('/*__CONF__*/{}', json.dumps(conf, ensure_ascii=False))
    assert '__' not in out.replace('__proto__', ''), 'placeholder left'
    open(os.path.join(HERE, fname), 'w', encoding='utf-8').write(out); print(fname, len(out))

HOW = 'ทุกข้อให้กด <b>ส่ง · มั่นใจ</b> หรือ <b>ส่ง · ไม่แน่ใจ</b> ตามจริง เพื่อแยกความเข้าใจผิดออกจากการเดา'
rmeta = {z: dict(m, lead='กลางภาคห้องเราทำโซนนี้ได้เฉลี่ย <b>%s%%</b> ภารกิจนี้รวมข้อที่ห้องพลาดมากที่สุดมาให้ฝึกแบบข้อสอบจริง รวมถึงข้อที่คำตอบคือ "ไม่มีข้อใดถูก"' % m['pct']) for z, m in rescue_src.META.items()}
page('rescue.html', 'Rescue Missions', 'RESCUE MISSIONS', 'ภารกิจกู้โซน GNR2022: ฝึกข้อที่ห้องพลาดในกลางภาค โซน 4 5 6 แบบข้อสอบจริง พร้อมแยกความเข้าใจผิดจากการเดา',
     rescue_src.R, rmeta, {'nq': 12, 'pass': 10, 'timer': 0, 'store': 'rescue', 'prefix': 'r', 'label': 'RESCUE', 'h1': 'ภารกิจกู้โซน',
     'howto': HOW, 'reward': 'รับรหัสแสตมป์', 'passText': 'กู้โซนสำเร็จ', 'stampNote': 'แสดงรหัสนี้กับผู้สอน (นับเข้า Combo Stamp ตามที่ผู้สอนประกาศ)', 'tagPre': 'เจาะ'})
page('hard.html', 'Hard Mode', 'HARD MODE', 'Hard Mode GNR2022: โจทย์หลายขั้นตอนของโซน 7 8 9 จับเวลา ไม่มีคำใบ้ ผ่านแล้วได้เพชร',
     hard_src.H, hard_src.META, {'nq': 10, 'pass': 8, 'timer': 45, 'store': 'hard', 'prefix': 'h', 'label': 'HARD MODE', 'h1': 'Hard Mode โซน',
     'howto': 'ไม่มีคำใบ้ จับเวลาข้อละ 45 วินาที หมดเวลานับเป็นผิด ' + HOW, 'reward': 'ได้เพชรและรหัส', 'passText': 'ได้เพชร',
     'stampNote': 'เพชรแสดงบนหน้าแผนที่และกระดานห้อง ผู้สอนตรวจรหัสนี้ได้ที่ปุ่ม "ผู้สอน"', 'tagPre': ''})
