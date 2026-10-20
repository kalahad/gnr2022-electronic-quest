# -*- coding: utf-8 -*-
"""ย้ายเกม GNR2022 ฉบับเดิม (GNR1007 UI v6 · CLIMB MODE) เข้าเอนจิน Maker Quest + NEO ARCADE
หลักการ: เนื้อหา คลังข้อสอบ และห้องทดลองที่ผ่าน QC แล้ว ดึงจากไฟล์เดิมโดยตรง (ไม่พิมพ์ใหม่)
แล้วเปลี่ยนเฉพาะ "เปลือก" ให้เป็นมาตรฐานเดียวกับทุกโซน
ไฟล์ต้นฉบับเก็บที่ tools/legacy_src/"""
import os, re, json, subprocess, html
from cpe_common import bank_js, star_table, navstops, avatars, COURSE

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), 'legacy_src')
TPL = open(os.path.join(os.path.dirname(HERE), 'template_game4.html'), encoding='utf-8').read()

def _between(s, a, b, keep_a=False):
    i = s.index(a); j = s.index(b, i + len(a))
    return s[i if keep_a else i + len(a):j]

def _js_eval(expr):
    out = subprocess.run(['node', '-e', 'const v=(' + expr + ');process.stdout.write(JSON.stringify(v))'],
                         capture_output=True, text=True, check=True)
    return json.loads(out.stdout)

# ---------- CSS: เก็บเฉพาะกฎที่แม่แบบไม่มี ----------
def _rules(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    out, i, n = [], 0, len(css)
    while i < n:
        j = css.find('{', i)
        if j < 0: break
        head = css[i:j].strip(); depth = 0; k = j
        while k < n:
            if css[k] == '{': depth += 1
            elif css[k] == '}':
                depth -= 1
                if depth == 0: break
            k += 1
        out.append((head, css[j:k + 1])); i = k + 1
    return out

def _tpl_css():
    return re.search(r'<style>(.*?)</style>', TPL, re.S).group(1)

def legacy_css(old):
    tpl = {h: b for h, b in _rules(_tpl_css())}
    keep = []
    for h, b in _rules(re.search(r'<style>(.*?)</style>', old, re.S).group(1)):
        if h.startswith(':root') or h in ('*', 'html', 'body', 'html,body') or h.startswith('body'):
            continue
        if h in tpl and (h.startswith('@') and tpl[h] == b or not h.startswith('@')):
            continue
        keep.append(h + b)
    return '\n'.join(keep)

# ---------- ส่วนประกอบจากไฟล์เดิม ----------
def extract(fname):
    s = open(os.path.join(SRC, fname), encoding='utf-8').read()
    js = s[s.index('/* ============ 1) UTILITIES ============ */'):]
    d = {}
    d['raw'] = s
    d['hero'] = re.search(r'<svg class="cityart".*?</svg>', s, re.S).group(0)
    d['title'] = re.search(r'<h1 class="title">(.*?)</h1>', s, re.S).group(1).strip()
    d['subtitle'] = re.search(r'<p class="subtitle">(.*?)</p>', s, re.S).group(1).strip()
    d['login_tag'] = re.search(r'<div class="panel login-card">\s*<span class="tag">(.*?)</span>', s, re.S).group(1)
    d['favicon'] = re.search(r'<link rel="icon" href="(.*?)">', s, re.S).group(1)
    d['desc'] = re.search(r'<meta name="description" content="(.*?)">', s, re.S).group(1)
    z = s[s.index('<!-- ===== PREVIEW 1 ===== -->'):s.index('<!-- ===== POSTTEST ===== -->')]
    z = re.sub(r'(<!-- =+[^>]*CHECK[^>]*-->\s*)?<section id="scr-check\d" class="screen">.*?</section>\s*', '', z, flags=re.S)
    body = s[s.index('<body'):s.index('<!-- ===== 0) WELCOME')]
    extra = [m.group(0) for m in re.finditer(r'<div id="([\w-]+)"[^>]*></div>', body) if ('id="%s"' % m.group(1)) not in TPL]
    d['zones'] = z.rstrip() + ('\n' + '\n'.join(extra) if extra else '')
    d['checks'] = [(html.unescape(a), b) for a, b in re.findall(r'<span class="tag">Checkpoint (?:·|&#183;) (.*?)</span>\s*<h2>ด่านฝึกหัด: (.*?)</h2>', s)]
    assert len(d['checks']) == 3, 'checkpoints not found'
    d['post_desc'] = re.search(r'<section id="scr-posttest".*?<p[^>]*>(.*?)</p>', s, re.S).group(1).strip()
    d['report_tag'] = re.search(r'<section id="scr-summary".*?<span class="tag">(.*?)</span>', s, re.S).group(1)
    # คลังข้อสอบ: เรียงให้ตัวเลือกถูกอยู่หน้าเสมอ
    bank = _js_eval(_between(js, 'const BANK = ', '\nconst SKILL_LABELS').strip().rstrip(';'))
    d['bank'] = {k: [(x['q'], [x['c'][x['a']]] + [c for i, c in enumerate(x['c']) if i != x['a']], x['e']) for x in v]
                 for k, v in bank.items()}
    d['skill_labels'] = re.search(r'const SKILL_LABELS = (\{.*?\});', js).group(1)
    d['skey'] = re.search(r"const SKEY = '(.*?)';", js).group(1)
    st = _js_eval(_between(js, 'const STAR_TABLE = ', '\nfunction starInfo').strip().rstrip(';'))
    d['ranks'] = [(r['rank'], r['msg']) for r in st]
    d['nav'] = re.findall(r"\{key:'d\d',\s*label:'(.*?)'", js)
    d['badges'] = re.search(r'const BADGE_DEFS = (\[.*?\n\]);', js, re.S).group(1)
    tips = re.search(r'function extraTips\(postInfo\)\{\n(.*?)\n\}\n', js, re.S).group(1)
    d['advice'] = tips.replace('postInfo.stars===5', 'postInfo.stars===6').replace('ครบ 5 ดาว', 'ครบ 6 ดาว')
    d['role'] = re.search(r"\$\('#sumWho'\)\.textContent='(.*?): '", js).group(1)
    # JS ห้องทดลอง: ตัวช่วยจัดรูปแบบ + LAB HELPERS + FORMULA CORE + LAB 1-3
    fmt = _between(js, '/* ---- ตัวช่วยจัดรูปแบบ', '/* ============ 2) SOUND ENGINE', keep_a=True) if 'ตัวช่วยจัดรูปแบบ' in js else ''
    labs = _between(js, '/* ============ 10) LAB HELPERS ============ */', '/* ============ 15) SUMMARY + RADAR ============ */', keep_a=True)
    d['lab_js'] = fmt + '\n' + labs
    w = _between(js, '/* ============ 17) EVENT WIRING ============ */', "$('#preLaunch').addEventListener")
    m = re.search(r"document\.addEventListener\('click',\s*e\s*=>\s*\{\n", w)
    pre_fn, rest = w[:m.start()], w[m.end():]
    body, tail = rest.split('\n});\n', 1)
    body = re.split(r"startQuiz\(rq\.dataset\.requiz\);\s*return;\s*\}\n", body, 1)[1]
    d['lab_wiring'] = body
    d['lab_js'] += '\n' + pre_fn
    boot = _between(js, '/* ============ 18) BOOT ============ */', "window.addEventListener('resize'")
    boot = boot.replace("renderAvatars(); updSoundBtns(); updXp(); renderNav('scr-welcome');", '')
    d['init_extra'] = '\n' + tail.strip() + '\n' + boot.strip() + '\n'
    d['extra_css'] = legacy_css(s)
    return d

def port(fname, o):
    """o = ค่าที่โซนกำหนดเอง: filename, brand, theme, act, features, cards ฯลฯ"""
    d = extract(fname)
    for old, new in o.get('fixes', []):          # แก้ความคลาดเคลื่อนของเนื้อหาเดิม (ตรวจแล้วระบุเหตุผลในคอนฟิกโซน)
        assert old in d['zones'] or old in d['lab_js'], 'fix not found: ' + old
        d['zones'] = d['zones'].replace(old, new); d['lab_js'] = d['lab_js'].replace(old, new)
    if o.get('rew'):                                   # ปรับสมดุลความยาวตัวเลือก (bank_rew.py)
        from bank_rew import apply as _rew
        _rew(d['bank'], o['rew'])
    for dist, m in o.get('aug', {}).items():          # เพิ่มรูปวงจรท้ายโจทย์ (ไม่ลบข้อความเดิม)
        for i, fig in m.items():
            q, c, e = d['bank'][dist][i]; d['bank'][dist][i] = (q + fig, c, e)
    return {
        'filename': o['filename'],
        'title': o.get('title', d['title']),
        'brand': o['brand'],
        'edition': o.get('edition', 'ZONE EDITION'),
        'desc': o.get('desc', d['desc']),
        'ogdesc': o.get('ogdesc', d['desc']),
        'favicon': d['favicon'],
        'theme': o['theme'],
        'extra_css': d['extra_css'] + '\n' + o.get('extra_css', ''),
        'arcade_label': o.get('arcade_label', 'ด่านไต่' + o['brand']),
        'hero_svg': o.get('hero_svg', d['hero']),
        'subtitle': o.get('subtitle', d['subtitle']),
        'login_tag': d['login_tag'],
        'features': o['features'],
        'climb_text': o.get('climb_text', 'ตัวละครไต่ขึ้น 1 ชั้น ทันที'),
        'zones_html': d['zones'],
        'checks': [tuple(x) for x in d['checks']],
        'post_desc': d['post_desc'],
        'report_tag': d['report_tag'],
        'course': COURSE,
        'footer_line': o['footer_line'],
        'bank': bank_js(d['bank']),
        'skill_labels': d['skill_labels'],
        'skey': d['skey'],
        'star_table': star_table(d['ranks']),
        'navstops': navstops(*d['nav']),
        'lock_msg': o.get('lock_msg', 'ด่านนี้ยังไม่เปิด เดินตามลำดับก่อนนะครับ'),
        'act': o['act'],
        'pre_sub': o.get('pre_sub', 'นี่คือเส้นฐานของคุณ ผ่านครบ 3 ด่านแล้วเรามาวัดกันใหม่'),
        'go_first': o.get('go_first', 'เข้าด่านแรก'),
        'lab_js': d['lab_js'],
        'lab_wiring': d['lab_wiring'],
        'init_extra': d['init_extra'],
        'badges': d['badges'],
        'advice_js': d['advice'],
        'role': d['role'],
        'filekey': o['filekey'],
        'avatars': avatars(o['theme']['INK_HEX'], o['avatar_cols']),
        '_legacy': d,
    }

def _rgb(h):
    h = h.lstrip('#'); return '%d,%d,%d' % (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))

def _mix(h, t, a):
    h = h.lstrip('#'); t = t.lstrip('#')
    c = [round(int(h[i:i+2], 16) * (1 - a) + int(t[i:i+2], 16) * a) for i in (0, 2, 4)]
    return '#%02x%02x%02x' % tuple(c)

def zone_theme(a, b, c, r, la, lb, lc, lr, bg='#070a1e'):
    """พาเลตต์ประจำโซน (มืด a b c r · สว่าง la lb lc lr) ส่วนพื้นหลังใช้โทนกลางของซีรีส์"""
    return {
        "PRIMARY_RGB": _rgb(a), "PRIMARY_HEX": a, "SECOND_RGB": _rgb(b), "SECOND_HEX": b,
        "GOLD_RGB": _rgb(c), "GOLD_HEX": c, "GOLD2_RGB": _rgb(_mix(c, '#ffffff', .45)), "GOLD2_HEX": _mix(c, '#ffffff', .45),
        "RED_RGB": _rgb(r), "RED_HEX": r, "BG_RGB": _rgb(bg), "BG_HEX": bg,
        "PANEL_RGB": _rgb(_mix(bg, a, .08)), "PANEL2_RGB": _rgb(_mix(bg, a, .13)),
        "BG2_HEX": _mix(bg, a, .04), "INK_HEX": _mix(bg, a, .06), "TEXT_HEX": "#eef0ff",
        "MUTED_HEX": "#a8afd8", "MUTED2_HEX": "#6f77a8", "MUTED3_HEX": "#5d6596",
        "SECOND2_HEX": _mix(b, '#ffffff', .3), "PRIM2_HEX": _mix(a, '#ffffff', .3),
        "LIGHT_EMBER": la, "LIGHT_CORNER": lb, "LIGHT_GOLD": lc, "LIGHT_GOLD2": _mix(lc, '#000000', .2), "LIGHT_RED": lr,
    }
