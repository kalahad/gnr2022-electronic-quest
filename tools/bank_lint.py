# -*- coding: utf-8 -*-
"""ตรวจความยาวตัวเลือก (กันเดาจากความยาว) usage: python3 tools/bank_lint.py <module ใน games_src> [...]"""
import sys, os, re, statistics, importlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'games_src'))
COMB = set([0x0E31] + list(range(0x0E34, 0x0E3B)) + list(range(0x0E47, 0x0E4F)))
def vis(s): return sum(1 for ch in re.sub(r'<[^>]+>', '', s) if ord(ch) not in COMB)
def lint(B, name):
    bad = []; n = lo = sh = sec = 0
    for d, items in B.items():
        for i, (q, c, e) in enumerate(items):
            L = [vis(x) for x in c]; med = statistics.median(L[1:]); n += 1
            if not (0.70 * med - 6 <= L[0] <= 1.25 * med + 6): bad.append('%s[%d] ถูก=%d มัธยฐานลวง=%g : %s' % (d, i, L[0], med, c))
            s = sorted(L, reverse=True)
            if L[0] == s[0] and s.count(s[0]) == 1: lo += 1
            if L[0] == s[-1] and s.count(s[-1]) == 1: sh += 1
            if L[0] == s[1] and s.count(s[1]) == 1: sec += 1
    for lab, v, lim in (('ถูก=ยาวสุด', lo, .30), ('ถูก=สั้นสุด', sh, .35), ('ถูก=ยาวรอง', sec, .35)):
        if v / n > lim: bad.append('%s %d/%d = %.0f%% เกิน %.0f%%' % (lab, v, n, 100 * v / n, 100 * lim))
    print(name, 'ข้อ', n, '· ยาวสุด %d สั้นสุด %d ยาวรอง %d' % (lo, sh, sec))
    for b in bad: print('  !', b)
    return not bad
ok = True
for m in sys.argv[1:]:
    ok &= lint(importlib.import_module(m).B, m)
print('ผ่านทุกด่าน' if ok else 'ไม่ผ่าน'); sys.exit(0 if ok else 1)
