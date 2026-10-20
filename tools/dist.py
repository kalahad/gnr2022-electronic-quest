#!/usr/bin/env python3
"""ประกอบ repo gnr-electronic สำหรับอัปโหลดขึ้น GitHub Pages
usage: python3 tools/dist.py <ที่เก็บไฟล์เดิมของ gnr-electronic> <ไฟล์เกมเดิม(ชั่วคราว)> <ปลายทาง>

โครงสร้างผลลัพธ์
  index.html            หน้าแผนที่ภารกิจ (HUB)
  play/                 เกมบทเรียนรายโซน  s<ซีซัน>-z<โซน>-<ชื่อ>.html
  lab/                  ห้องทดลองจำลอง    lab-<รูป/ไอซี>-<ชื่อ>.html
  boss/final-boss.html  จำลองสอบปลายภาค
  <ชื่อไฟล์เดิม>.html    หน้าส่งต่ออัตโนมัติ (ลิงก์/QR เก่าไม่เสีย)
  tools/                ซอร์สสำหรับสร้างเกมใหม่
"""
import os, re, sys, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# เกมระบบใหม่ (สร้างจาก tools/games_src) -> ชื่อไฟล์บน repo
PLAY = {
    'game1_resistor_city.html':  's1-z1-resistor-city.html',
    'game2_lumen_station.html':  's1-z2-lumen-station.html',
    'game3_deep_crystal.html':   's1-z3-deep-crystal.html',
    'game4_diode_forge.html':    's1-z4-diode-forge.html',
    'game5_storm_harbor.html':   's1-z5-storm-harbor.html',
    'game6_night_melody.html':   's1-z6-night-melody.html',
    'game7_bjt_arena.html':      's2-z7-bjt-arena.html',
    'game8_opamp_tower.html':    's2-z8-opamp-tower.html',
    'game9_555_clockwork.html':  's2-z9-555-clockwork.html',
}
# เกมฉบับเดิม ใช้ชั่วคราวจนกว่าฉบับระบบใหม่จะพร้อม (ชื่อปลายทางเดียวกัน)
LEGACY = {
    'gnr2022_game1_resistor_color_code.html':     's1-z1-resistor-city.html',
    'gnr2022_game2_lumen_station.html':           's1-z2-lumen-station.html',
    'gnr2022_game3_deep_crystal_expedition.html': 's1-z3-deep-crystal.html',
    'gnr2022_game5_storm_harbor.html':            's1-z5-storm-harbor.html',
}
LABS = {
    'Content_1_digit_forge_7segment_lab5.html':      'lab/lab-7seg-digit-forge.html',
    'Lab_3_4_sun_chime_light_alarm_3_40.html':       'lab/lab-3-40-sun-chime.html',
    'Lab_3_5_dusk_guard_night_light_3_44.html':      'lab/lab-3-44-dusk-guard.html',
    'Lab_3_6_beam_sentry_intruder_alarm_3_47.html':  'lab/lab-3-47-beam-sentry.html',
    'Lab_3_7_pulse_eye_reflective_object_3_50.html': 'lab/lab-3-50-pulse-eye.html',
    'Lab_1_3_trip_point_level_detector_sim.html':    'lab/lab-lm339-trip-point.html',
    'Proj_1_bar_ranger_led_ruler_sim.html':          'lab/lab-lm339-bar-ranger.html',
    'Boss_Battle_Exam_Simulator.html':               'boss/final-boss.html',
}
# ลิงก์เก่าที่เคยแจก (รวม repo gnr2022-circuit-quest ที่ใช้ชื่อ game3_night_melody.html)
EXTRA_REDIRECT = {}

BACK = ('<a href="../index.html" class="gnr-back" aria-label="กลับแผนที่ภารกิจ" style="position:fixed;left:10px;bottom:10px;z-index:2147483000;'
        'display:inline-flex;align-items:center;gap:6px;padding:7px 12px;border-radius:999px;font:500 13px/1 Kanit,system-ui,sans-serif;'
        'text-decoration:none;color:#f4f4ff;background:rgba(10,10,25,.72);border:1px solid rgba(255,255,255,.18);backdrop-filter:blur(8px);'
        'box-shadow:0 6px 20px -8px rgba(0,0,0,.6)">'
        '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>แผนที่</a>\n')

def stub(target):
    return ('<!DOCTYPE html><html lang="th"><head><meta charset="utf-8"><title>ย้ายไปที่ใหม่</title>'
            '<meta http-equiv="refresh" content="0; url=%s"><link rel="canonical" href="%s">'
            '<script>location.replace(%r + location.search + location.hash);</script></head>'
            '<body style="font-family:sans-serif;padding:24px">หน้านี้ย้ายแล้ว <a href="%s">ไปที่หน้าใหม่</a></body></html>\n') % (target, target, target, target)

FB = '<script src="%sfeedback.js" defer></script>\n'

def inject_fb(s, prefix='../'):
    s = re.sub(r'<script src="(\.\./)?feedback\.js" defer></script>\n', '', s)
    i = s.rindex('</body>')
    return s[:i] + FB % prefix + s[i:]

def inject_back(s):
    s = re.sub(r'<a href="\.\./index\.html" class="gnr-back".*?</a>\n', '', s, flags=re.S)
    i = s.rindex('</body>')
    return s[:i] + BACK + s[i:]

def main(old_site, legacy_dir, out):
    if os.path.isdir(out):
        for f in os.listdir(out):
            if f != '.git':
                p = os.path.join(out, f)
                shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    for d in ('play', 'lab', 'boss'):
        os.makedirs(os.path.join(out, d), exist_ok=True)
    built = set()
    for src, dst in PLAY.items():
        p = os.path.join(ROOT, src)
        if os.path.exists(p):
            s = open(p, encoding='utf-8').read()
            open(os.path.join(out, 'play', dst), 'w', encoding='utf-8').write(inject_fb(s)); built.add(dst)
            print('play  ', dst, '(ระบบใหม่)')
    for src, dst in LEGACY.items():
        if dst in built: continue
        p = os.path.join(legacy_dir, src)
        if os.path.exists(p):
            s = open(p, encoding='utf-8').read()
            open(os.path.join(out, 'play', dst), 'w', encoding='utf-8').write(inject_fb(inject_back(s)))
            print('play  ', dst, '(ฉบับเดิมชั่วคราว)')
    for src, dst in LABS.items():
        s = open(os.path.join(old_site, src), encoding='utf-8').read()
        if 'http-equiv="refresh"' in s and len(s) < 4000:     # ไฟล์ชื่อเดิมใน repo เป็นหน้าส่งต่อ ใช้ฉบับที่เผยแพร่อยู่แทน
            s = open(os.path.join(old_site, dst), encoding='utf-8').read()
        s = s.replace('href="index.html"', 'href="../index.html"')
        open(os.path.join(out, dst), 'w', encoding='utf-8').write(inject_fb(inject_back(s)))
        open(os.path.join(out, src), 'w', encoding='utf-8').write(stub(dst))
        print('lab   ', dst, '<-', src)
    for src, dst in EXTRA_REDIRECT.items():
        open(os.path.join(out, src), 'w', encoding='utf-8').write(stub(dst))
    hub = open(os.path.join(HERE, 'hub', 'index.html'), encoding='utf-8').read()
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(inject_fb(hub, ''))
    shutil.copy(os.path.join(HERE, 'hub', 'feedback.js'), os.path.join(out, 'feedback.js'))
    for pg in ('rescue.html', 'hard.html'):                           # ภารกิจกู้โซน Z4-Z6 และ Hard Mode Z7-Z9
        rs = open(os.path.join(HERE, 'hub', pg), encoding='utf-8').read()
        open(os.path.join(out, 'play', pg), 'w', encoding='utf-8').write(inject_fb(inject_back(rs)))
        print('drill  play/' + pg)
    shutil.copy(os.path.join(ROOT, 'README.md'), os.path.join(out, 'README.md'))
    open(os.path.join(out, '.nojekyll'), 'w').close()
    skip = shutil.ignore_patterns('__pycache__', '*.pyc', '*.png', 'make_index.py', 'template_index.html', 'index_neo.css',
                                  'index_shot.py', 'pin_shots.py', 'pinout.css', 'pinout.js')
    shutil.copytree(HERE, os.path.join(out, 'tools'), ignore=skip)
    print('done ->', out)

if __name__ == '__main__':
    main(*sys.argv[1:4])
