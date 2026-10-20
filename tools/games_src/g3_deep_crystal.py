# -*- coding: utf-8 -*-
"""SEASON 1 · ZONE 3 — DEEP CRYSTAL : ภารกิจสำรวจผลึกลึก
ย้ายจากเกมฉบับเดิม (gnr2022_game3_deep_crystal_expedition.html) เข้าเอนจินมาตรฐาน"""
from legacy_port import port, zone_theme
from qfig import pn

TH = zone_theme('#22d3ee', '#818cf8', '#f0abfc', '#fb7185', '#0e7490', '#4338ca', '#a21caf', '#be123c', bg='#050b1a')
CFG = port('gnr2022_game3_deep_crystal_expedition.html', {
    'filename': 'game3_deep_crystal.html',
    'brand': 'DEEP CRYSTAL',
    'edition': 'CRYSTAL EDITION',
    'theme': TH,
    'act': {'floor': 'ชั้น', 'top': 'ปากถ้ำผลึก', 'ground': 'ก้นถ้ำ', 'theme': 'crystal'},
    'features': '<span>S1 · โซน 3</span><span>BAND · DOPING · PN</span><span>PRETEST / POSTTEST</span><span>ระบบดาว 6 ดวง</span>',
    'climb_text': 'นักสำรวจไต่ขึ้นจากถ้ำผลึก 1 ชั้น ทันที',
    'footer_line': 'Season 1 · โซน 3 แถบพลังงาน การเจือสาร และรอยต่อ PN — ภาคเรียนที่ 1/2569',
    'rew': 'g3',
    'filekey': 'GNR2022_Z3_deepcrystal',
    'go_first': 'ลงถ้ำชั้นแรก',
    # รูปวงจรประกอบโจทย์ (ต่อท้ายโจทย์เดิม ไม่ลบข้อความ)
    'aug': {'district3': {2: pn(True)}},
    'avatar_cols': ['#22d3ee', '#818cf8', '#f0abfc', '#fb7185', '#67e8f9', '#a5b4fc'],
})
