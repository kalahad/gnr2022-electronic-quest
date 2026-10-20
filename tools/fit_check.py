#!/usr/bin/env python3
"""ตรวจว่าทุกหน้าจอของเกม "จบในจอเดียว" ไม่มีแถบเลื่อนทั้งระดับหน้าและภายในการ์ด
usage: python3 tools/fit_check.py <game.html> [WxH ...]"""
import sys, os
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
f = sys.argv[1]; sizes = [tuple(map(int, s.split('x'))) for s in (sys.argv[2:] or ['1890x800', '1366x657', '1536x730', '1280x600'])]
MEASURE = """()=>{const a=document.querySelector('.screen.active'); const p=a&&a.querySelector('.panel');
 const sl=a&&a.querySelector('.neo-slide.on'); const d=document.documentElement;
 return {id:a?a.id:'', page:d.scrollHeight-innerHeight, hs:d.scrollWidth-innerWidth, panel:p?p.scrollHeight-p.clientHeight:0, slide:sl?sl.scrollHeight-sl.clientHeight:0}}"""
with sync_playwright() as pw:
    b = pw.chromium.launch(**({'executable_path': os.environ['PW_EXE'], 'args': ['--no-sandbox']} if os.environ.get('PW_EXE') else {})); bad = 0
    for w, h in sizes:
        pg = b.new_page(viewport={'width': w, 'height': h}); errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file:') else r.abort())
        pg.goto('file://' + os.path.join(ROOT, f)); pg.wait_for_timeout(600)
        res = [('welcome', pg.evaluate(MEASURE))]
        pg.fill('#playerName', 'k')
        sid = pg.query_selector('#gnrSid') or pg.query_selector('input[inputmode="numeric"]')
        if sid: sid.fill('6911111111')
        pg.click('#btnStart'); pg.wait_for_timeout(600); res.append(('pre-brief', pg.evaluate(MEASURE)))
        pg.evaluate("state.unlocked=['pretest','d1','d2','d3','posttest','summary']")
        for n in (1, 2, 3):
            pg.evaluate("goto_('scr-preview%d')" % n); pg.wait_for_timeout(450); res.append(('preview%d' % n, pg.evaluate(MEASURE)))
            pg.evaluate("goto_('scr-lesson%d')" % n); pg.wait_for_timeout(450)
            k = 0
            while True:
                pg.wait_for_timeout(450); res.append(('L%d.s%d' % (n, k), pg.evaluate(MEASURE)))
                nx = pg.query_selector('#scr-lesson%d .neo-next' % n)
                if not nx or not nx.is_visible() or k > 15: break
                nx.click(); k += 1
            pg.evaluate("goto_('scr-check%d')" % n); pg.wait_for_timeout(450); res.append(('check%d' % n, pg.evaluate(MEASURE)))
        pg.evaluate("goto_('scr-posttest')"); pg.wait_for_timeout(450); res.append(('post-brief', pg.evaluate(MEASURE)))
        pg.evaluate("state.pre=2;state.post=5;state.preByD={district1:1,district2:1,district3:0};state.postByD={district1:2,district2:2,district3:1};showSummary()")
        pg.wait_for_timeout(1500); res.append(('summary', pg.evaluate(MEASURE)))
        over = [(n, m) for n, m in res if max(m['page'], m['hs'], m['panel'], m['slide']) > 2]
        bad += len(over)
        print('%dx%d' % (w, h), 'OK' if not over else 'OVERFLOW ' + '; '.join('%s p%d h%d c%d s%d' % (n, m['page'], m['hs'], m['panel'], m['slide']) for n, m in over), errs[:2])
        pg.close()
    b.close()
    sys.exit(1 if bad else 0)
