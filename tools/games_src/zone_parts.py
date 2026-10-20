# -*- coding: utf-8 -*-
"""ตัวช่วยโซน Season 2 ที่แยกเนื้อหาเป็นไฟล์ใน gN_parts/ : zones.html, labs.js, wiring.js, init.js, bank.py"""
import os
def load(here, name):
    p = os.path.join(here, name)
    rd = lambda n: open(os.path.join(p, n), encoding='utf-8').read()
    return rd, p
