# -*- coding: utf-8 -*-
"""SEASON 1 · ZONE 5 — STORM HARBOR : ท่าเรือพายุ
ย้ายจากเกมฉบับเดิม (gnr2022_game5_storm_harbor.html) เข้าเอนจินมาตรฐาน"""
from legacy_port import port, zone_theme
from qfig import halfwave, bridge, zener

TH = zone_theme('#3b82f6', '#22d3ee', '#fde047', '#f43f5e', '#1d4ed8', '#0e7490', '#8a6a00', '#be123c', bg='#050a18')
CFG = port('gnr2022_game5_storm_harbor.html', {
    'filename': 'game5_storm_harbor.html',
    'brand': 'STORM HARBOR',
    'edition': 'STORM EDITION',
    'theme': TH,
    'act': {'floor': 'ชั้น', 'top': 'ยอดประภาคาร', 'ground': 'ท่าเรือ', 'theme': 'storm'},
    'features': '<span>S1 · โซน 5</span><span>RECTIFIER · FILTER · ZENER</span><span>PRETEST / POSTTEST</span><span>ระบบดาว 6 ดวง</span>',
    'climb_text': 'ตัวละครไต่ประภาคารขึ้น 1 ชั้น ทันที',
    'footer_line': 'Season 1 · โซน 5 วงจรเรียงกระแส ตัวกรอง และซีเนอร์ — ภาคเรียนที่ 1/2569',
    'filekey': 'GNR2022_Z5_stormharbor',
    'rew': 'g5',
    'go_first': 'เข้าประตูท่าเรือ',
    # รูปวงจรประกอบโจทย์ (ต่อท้ายโจทย์เดิม ไม่ลบข้อความ)
    'aug': {
        'district1': {2: halfwave('50 Hz'), 3: halfwave('Vm'), 9: halfwave('AC', d='D1 ?'), 10: halfwave('24 Vrms')},
        'district2': {3: bridge('AC'), 9: bridge('50 Hz'), 11: bridge('12 Vrms')},
        'district3': {0: halfwave('AC', cap='C'), 9: bridge('AC', cap='470 µF'), 10: zener('Vin', 'Rs', 'Vz', 'RL (ดึงกระแสมากขึ้น)'),
                      11: halfwave('ยอด 24 V', cap='1000 µF 16 V')}},
    'avatar_cols': ['#3b82f6', '#22d3ee', '#fde047', '#f43f5e', '#93c5fd', '#67e8f9'],
})
