# -*- coding: utf-8 -*-
"""SEASON 1 · ZONE 2 — LUMEN STATION : สถานีตรวจวัดแสงอัตโนมัติ
ย้ายจากเกมฉบับเดิม (gnr2022_game2_lumen_station.html) เข้าเอนจินมาตรฐาน: เนื้อหา คลังข้อสอบ 36 ข้อ และห้องทดลอง 3 ห้องคงเดิม"""
from legacy_port import port, zone_theme

TH = zone_theme('#38bdf8', '#facc15', '#a3e635', '#f87171', '#0369a1', '#8a6a00', '#4d7c0f', '#b91c1c', bg='#06111d')
CFG = port('gnr2022_game2_lumen_station.html', {
    'filename': 'game2_lumen_station.html',
    'brand': 'LUMEN STATION',
    'edition': 'SENSOR EDITION',
    'theme': TH,
    'act': {'floor': 'ชั้น', 'top': 'ยอดเสาสัญญาณ', 'ground': 'ฐานสถานี', 'theme': 'radar'},
    'features': '<span>S1 · โซน 2</span><span>VR · LDR · ADC</span><span>PRETEST / POSTTEST</span><span>ระบบดาว 6 ดวง</span>',
    'climb_text': 'ตัวละครไต่เสาสัญญาณขึ้น 1 ชั้น ทันที',
    'footer_line': 'Season 1 · โซน 2 ตัวต้านทานปรับค่าได้ LDR และวงจรแบ่งแรงดันสู่ ADC — ภาคเรียนที่ 1/2569',
    'filekey': 'GNR2022_Z2_lumenstation',
    'go_first': 'เข้าสถานีแรก',
    # R = 10 kΩ × (300/10)^-0.7 = 0.925 kΩ (ฉบับเดิมเขียน 0.87 kΩ ซึ่งตรงกับราว 330 lx)
    'fixes': [('<td>ประมาณ 0.87 kΩ</td>', '<td>ประมาณ 0.93 kΩ</td>')],
    'avatar_cols': ['#38bdf8', '#facc15', '#a3e635', '#f87171', '#7dd3fc', '#fde047'],
})
