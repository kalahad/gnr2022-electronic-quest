# -*- coding: utf-8 -*-
"""สร้างไฟล์ "คลังข้อสอบและเฉลยผู้สอน" (HTML พิมพ์ได้) จากคอนฟิกเกมทุกโซน
ห้ามเผยแพร่ไฟล์นี้บน GitHub Pages ของนักศึกษา"""
import os, sys, html, re, importlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'games_src'))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.dirname(HERE)), 'GNR2022_คลังข้อสอบและเฉลยผู้สอน_v1.0.html')  # เก็บนอก repo เสมอ
MODS = ['g1_resistor_city', 'g2_lumen_station', 'g3_deep_crystal', 'g4_diode_forge', 'g5_storm_harbor', 'g6_night_melody', 'g7_bjt_arena', 'g8_opamp_tower', 'g9_555_clockwork']

def labels(js):
    return dict(re.findall(r"(district\d):'([^']*)'", js))

parts = []; total = 0
for m in MODS:
    g = importlib.import_module(m); cfg = g.CFG; lb = labels(cfg['skill_labels'])
    parts.append('<h2>%s</h2><p class="meta">ไฟล์ %s</p>' % (html.escape(cfg['title']), cfg['filename']))
    for d, items in (g.B if hasattr(g, 'B') else cfg['_legacy']['bank']).items():
        parts.append('<h3>%s · %s (%d ข้อ)</h3><ol>' % (d.replace('district', 'ด่านย่อย '), html.escape(lb.get(d, d)), len(items)))
        for q, c, e in items:
            total += 1
            opts = ''.join('<li%s>%s</li>' % (' class="ans"' if i == 0 else '', c[i]) for i in range(4))
            parts.append('<li class="q"><div>%s</div><ol type="A" class="opts">%s</ol><div class="ex"><b>เฉลย:</b> %s · %s</div></li>' % (q, opts, c[0], e))
        parts.append('</ol>')

# ภารกิจกู้โซน (Rescue) Z4-Z6 · tools/hub/rescue_src.py
sys.path.insert(0, os.path.join(HERE, 'hub'))
import rescue_src
parts.append('<h2>ภารกิจกู้โซน (Rescue Missions)</h2><p class="meta">ไฟล์ play/rescue.html · สุ่ม 12 จาก 15 ข้อ · ผ่าน 10/12 · "ไม่มีข้อใดถูก" ตรึงไว้ท้ายเสมอ</p>')
for z, items in rescue_src.R.items():
    parts.append('<h3>%s · %s (%d ข้อ)</h3><ol>' % (z.upper(), html.escape(rescue_src.META[z]['th']), len(items)))
    for q, c, e, mref in items:
        total += 1
        opts = ''.join('<li%s>%s</li>' % (' class="ans"' if i == 0 else '', html.escape(c[i])) for i in range(4))
        parts.append('<li class="q"><div>%s <span class="meta">[%s]</span></div><ol type="A" class="opts">%s</ol><div class="ex"><b>เฉลย:</b> %s · %s</div></li>' % (html.escape(q), html.escape(mref), opts, html.escape(c[0]), html.escape(e)))
    parts.append('</ol>')
import hard_src
parts.append('<h2>Hard Mode โซน 7 8 9</h2><p class="meta">ไฟล์ play/hard.html · สุ่ม 10 จาก 12 ข้อ · ข้อละ 45 วินาที · ผ่าน 8/10 ได้เพชรและรหัส H</p>')
for z, items in hard_src.H.items():
    parts.append('<h3>%s · %s (%d ข้อ)</h3><ol>' % (z.upper(), html.escape(hard_src.META[z]['th']), len(items)))
    for q, c, e, mref in items:
        total += 1
        opts = ''.join('<li%s>%s</li>' % (' class="ans"' if i == 0 else '', html.escape(c[i])) for i in range(4))
        parts.append('<li class="q"><div>%s <span class="meta">[%s]</span></div><ol type="A" class="opts">%s</ol><div class="ex"><b>เฉลย:</b> %s · %s</div></li>' % (html.escape(q), html.escape(mref), opts, html.escape(c[0]), html.escape(e)))
    parts.append('</ol>')

doc = """<!DOCTYPE html><html lang="th"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>คลังข้อสอบและเฉลยผู้สอน GNR2022</title>
<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600&display=swap" rel="stylesheet">
<style>
:root{--bg:#fff;--ink:#14181f;--muted:#5b6475;--ok:#0f7a3d;--line:#d9dee7;--code:#f3f5f9}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#11151b;--ink:#e8ecf2;--muted:#9aa5b5;--ok:#4ade80;--line:#2a313c;--code:#1a2029}}
body{margin:0;background:var(--bg);color:var(--ink);font-family:'Sarabun',sans-serif;line-height:1.6}
main{max-width:920px;margin:0 auto;padding:24px 16px 60px}
h1{font-size:1.5rem;margin:0 0 4px} h2{margin-top:36px;border-bottom:2px solid var(--line);padding-bottom:6px} h3{color:var(--muted);font-size:1.05rem}
.meta{color:var(--muted);font-size:.9rem;margin:0}
li.q{margin:14px 0;padding:10px 12px;border:1px solid var(--line);border-radius:10px;break-inside:avoid}
.opts li{margin:2px 0}.opts li.ans{color:var(--ok);font-weight:600}
.ex{margin-top:6px;font-size:.92rem;color:var(--muted)}
.codebox{white-space:pre-wrap;font-family:Consolas,monospace;font-size:.85rem;background:var(--code);border:1px solid var(--line);border-radius:8px;padding:8px 10px;margin:6px 0}
.warn{border-left:4px solid #d97706;padding:8px 12px;background:var(--code);border-radius:0 8px 8px 0}
@media print{li.q{border-color:#ccc} body{background:#fff;color:#000}}
</style></head><body><main>
<h1>คลังข้อสอบและเฉลยผู้สอน · GNR2022 Circuit Quest v3.1 (20 ต.ค. 2569)</h1>
<p class="meta">GNR2022 อิเล็กทรอนิกส์พื้นฐาน · ภาคเรียนที่ 1/2569 · ผศ.ดร.กุลวลัญช์ วรุณสิน · รวม %d ข้อ</p>
<p class="warn">เอกสารสำหรับผู้สอนเท่านั้น ห้ามอัปโหลดขึ้น GitHub Pages ที่เปิดให้นักศึกษา · ในเกมจริงตัวเลือกจะถูกสลับลำดับทุกครั้ง (ในเอกสารนี้ตัวเลือก A คือคำตอบที่ถูกเสมอ)</p>
%s
</main></body></html>""" % (total, '\n'.join(parts))
open(OUT, 'w', encoding='utf-8').write(doc)
print('answer key:', OUT, 'questions:', total)
