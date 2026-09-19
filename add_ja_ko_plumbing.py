#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为日语(ja)/韩语(ko)新增做管道改造（幂等）：
1) js/main.js：语言列表、目录识别、html lang 映射、自动匹配、rel 正则、BUST_VERSION
2) gen_i18n.py：支持 ja/ko（hreflang 动态生成、data 属性清理、html lang、切换器高亮）
3) 138 个源页面：切换器加 JA/KO 按钮（排在 EN 之后）、head 加 hreflang ja/ko、JSON-LD inLanguage 加 ja/ko
用法: python add_ja_ko_plumbing.py [--dry]
"""
import re, sys, os, glob

DRY = '--dry' in sys.argv
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

JA_FLAG = ('<button class="lang-flag" data-lang="ja" title="日本語" type="button">'
           '<svg viewBox="0 0 30 20" width="20" height="14" aria-hidden="true">'
           '<rect width="30" height="20" fill="#FFFFFF"/>'
           '<circle cx="15" cy="10" r="5.6" fill="#BC002D"/>'
           '<rect x="0.5" y="0.5" width="29" height="19" fill="none" stroke="rgba(0,0,0,.18)"/>'
           '</svg></button>')
KO_FLAG = ('<button class="lang-flag" data-lang="ko" title="한국어" type="button">'
           '<svg viewBox="0 0 30 20" width="20" height="14" aria-hidden="true">'
           '<rect width="30" height="20" fill="#FFFFFF"/>'
           '<circle cx="15" cy="10" r="4" fill="#0047A0"/>'
           '<path d="M11 10a4 4 0 0 1 8 0 2 2 0 0 1-4 0 2 2 0 0 0-4 0z" fill="#CD2E3A"/>'
           '<g stroke="#111" stroke-width="1.1" stroke-linecap="round">'
           '<path d="M5.6 4.4 8.3 2.8"/><path d="M6.3 5.6 9 4"/>'
           '<path d="M21 15.6 23.7 17.2"/><path d="M21.7 16.8 24.4 18.4"/>'
           '<path d="M21 2.8 23.7 4.4"/><path d="M20.3 4 23 5.6"/>'
           '<path d="M5.6 15.6 8.3 17.2"/><path d="M6.3 14.4 9 16"/>'
           '</g>'
           '<rect x="0.5" y="0.5" width="29" height="19" fill="none" stroke="rgba(0,0,0,.18)"/>'
           '</svg></button>')


def ja_ko_hrefs(base_href):
    """由 x-default(中文) href 推出 ja/ko href；语言根首页转目录形式"""
    def to(lang):
        if base_href.rstrip('/') == 'https://taigetag.com':
            return 'https://taigetag.com/%s/' % lang
        h = base_href.replace('https://taigetag.com/', 'https://taigetag.com/%s/' % lang, 1)
        # 仅语言根首页去 index.html（与 gen_i18n.py canonical 规则一致）
        return h
    return to('ja'), to('ko')


def patch_source(path):
    s0 = s = open(path, encoding='utf-8').read()
    log = []

    # 1) 切换器：JA/KO 按钮排在 EN 之后
    if 'data-lang="ja"' not in s:
        m = re.search(r'<button class="lang-flag"(?: active)? data-lang="en".*?</button>', s, re.S)
        if not m:
            return log + ['!! 未找到 EN 按钮: %s' % path]
        s = s[:m.end()] + JA_FLAG + KO_FLAG + s[m.end():]
        log.append('按钮+2')

    # 2) head hreflang ja/ko（插在 x-default 之前）
    if 'hreflang="ja"' not in s:
        m = re.search(r'<link rel="alternate" hreflang="x-default" href="([^"]+)">', s)
        if not m:
            log.append('!! 未找到 x-default')
        else:
            ja, ko = ja_ko_hrefs(m.group(1))
            ins = ('<link rel="alternate" hreflang="ja" href="%s">\n'
                   '<link rel="alternate" hreflang="ko" href="%s">\n' % (ja, ko))
            s = s[:m.start()] + ins + s[m.start():]
            log.append('hreflang+2')

    # 3) JSON-LD inLanguage 数组加 ja/ko
    m = re.search(r'"inLanguage"\s*:\s*\[([^\]]*)\]', s)
    if m and '"ja"' not in m.group(1):
        inner = m.group(1)
        if '"es"' in inner:
            inner2 = inner.replace('"es"', '"es",\n    "ja",\n    "ko"', 1)
        else:
            inner2 = inner.rstrip().rstrip(',') + ',\n    "ja",\n    "ko"\n   '
        s = s[:m.start(1)] + inner2 + s[m.end(1):]
        log.append('inLanguage+2')

    if s != s0 and not DRY:
        open(path, 'w', encoding='utf-8').write(s)
    return log


def patch_main_js():
    p = 'js/main.js'
    s0 = s = open(p, encoding='utf-8').read()

    s = s.replace('var LANGS = ["zh", "en", "fr", "es"];',
                  'var LANGS = ["zh", "en", "ja", "ko", "fr", "es"];', 1)
    s = s.replace('''    else if (_p.indexOf("/es/") >= 0) DIR_LANG = "es";''',
                  '''    else if (_p.indexOf("/es/") >= 0) DIR_LANG = "es";
    else if (_p.indexOf("/ja/") >= 0) DIR_LANG = "ja";
    else if (_p.indexOf("/ko/") >= 0) DIR_LANG = "ko";''', 1)
    s = s.replace('''    else if (sys.indexOf("en") === 0) current = "en";''',
                  '''    else if (sys.indexOf("ja") === 0) current = "ja";
    else if (sys.indexOf("ko") === 0) current = "ko";
    else if (sys.indexOf("en") === 0) current = "en";''', 1)
    s = s.replace('var LANG_HTML = { zh: "zh-CN", en: "en", fr: "fr", es: "es" };',
                  'var LANG_HTML = { zh: "zh-CN", en: "en", ja: "ja", ko: "ko", fr: "fr", es: "es" };', 1)
    s = s.replace(r'replace(/^\/(en|fr|es)\//, "")', r'replace(/^\/(en|ja|ko|fr|es)\//, "")', 1)
    s = re.sub(r'var BUST_VERSION = "(\d+)";',
               lambda m: 'var BUST_VERSION = "%d";' % (int(m.group(1)) + 1), s, count=1)

    for needle in ['"ja", "ko", "fr", "es"', '"/ja/"', '"/ko/"', 'ja: "ja"', r'(en|ja|ko|fr|es)']:
        assert needle in s, 'main.js 缺失: %s' % needle
    if not DRY:
        open(p, 'w', encoding='utf-8').write(s)
    return s != s0


def patch_gen_i18n():
    p = 'gen_i18n.py'
    s0 = s = open(p, encoding='utf-8').read()

    s = s.replace('支持 en / fr / es。', '支持 en / fr / es / ja / ko。', 1)
    s = s.replace('LANGS = {"en": "en", "fr": "fr", "es": "es"}',
                  'LANGS = {"en": "en", "fr": "fr", "es": "es", "ja": "ja", "ko": "ko"}', 1)
    s = s.replace('''              "es": ("data-es", "data-zh", "data-fr")}''',
                  '''              "es": ("data-es", "data-zh", "data-fr"),
              "ja": ("data-ja", "data-zh", "data-en"),
              "ko": ("data-ko", "data-zh", "data-en")}''', 1)
    s = s.replace('''ALT_PAIRS = {"en": [("fr", "?lang=fr"), ("es", "?lang=es")],
             "fr": [("en", "en/"), ("es", "?lang=es")],
             "es": [("en", "en/"), ("fr", "?lang=fr")]}''',
                  '''ALT_PAIRS = {"en": [("fr", "fr/"), ("es", "es/")],
             "fr": [("en", "en/"), ("es", "es/")],
             "es": [("en", "en/"), ("fr", "fr/")],
             "ja": [("en", "en/"), ("ko", "ko/")],
             "ko": [("en", "en/"), ("ja", "ja/")]}''', 1)
    s = s.replace('''    html_lang = "fr" if lang == "fr" else ("es" if lang == "es" else "en")''',
                  '''    HTML_LANG = {"en": "en", "fr": "fr", "es": "es", "ja": "ja", "ko": "ko"}
    html_lang = HTML_LANG.get(lang, "en")''', 1)
    # hreflang 动态生成（zh-CN + 全部语言 + x-default）
    old_hr = '''    en_href = 'https://taigetag.com/en/' + rel_path.replace(lang + '/', '', 1)
    fr_href = 'https://taigetag.com/fr/' + rel_path.replace(lang + '/', '', 1)
    es_href = 'https://taigetag.com/es/' + rel_path.replace(lang + '/', '', 1)
    en_href = en_href.replace('https://taigetag.com/en/index.html', 'https://taigetag.com/en/')
    fr_href = fr_href.replace('https://taigetag.com/fr/index.html', 'https://taigetag.com/fr/')
    es_href = es_href.replace('https://taigetag.com/es/index.html', 'https://taigetag.com/es/')
    hreflang_lines = [
        '<link rel="alternate" hreflang="zh-CN" href="%s">' % zh_href,
        '<link rel="alternate" hreflang="en" href="%s">' % en_href,
        '<link rel="alternate" hreflang="fr" href="%s">' % fr_href,
        '<link rel="alternate" hreflang="es" href="%s">' % es_href,
        '<link rel="alternate" hreflang="x-default" href="%s">' % zh_href,
    ]'''
    new_hr = '''    # 逐语言生成 hreflang（语言根首页去 index.html，与 canonical 规则一致）
    HL_TAG = {"en": "en", "fr": "fr", "es": "es", "ja": "ja", "ko": "ko"}
    hl_hrefs = {}
    for _l in LANGS:
        _h = 'https://taigetag.com/' + _l + '/' + rel_path.replace(lang + '/', '', 1)
        _h = _h.replace('https://taigetag.com/%s/index.html' % _l, 'https://taigetag.com/%s/' % _l)
        hl_hrefs[_l] = _h
    hreflang_lines = ['<link rel="alternate" hreflang="zh-CN" href="%s">' % zh_href]
    for _l in ["en", "ja", "ko", "fr", "es"]:
        hreflang_lines.append('<link rel="alternate" hreflang="%s" href="%s">' % (HL_TAG[_l], hl_hrefs[_l]))
    hreflang_lines.append('<link rel="alternate" hreflang="x-default" href="%s">' % zh_href)'''
    assert old_hr in s, 'gen_i18n hreflang 块未匹配'
    s = s.replace(old_hr, new_hr, 1)
    # data 属性清理要覆盖 ja/ko
    s = s.replace(r'''attrs2 = re.sub(r'\s*data-(?:zh|en|fr|es)="[^"]*"', '', attrs)''',
                  r'''attrs2 = re.sub(r'\s*data-(?:zh|en|fr|es|ja|ko)="[^"]*"', '', attrs)''', 1)
    # 切换器高亮：先清掉所有 active 再点亮本语言
    s = s.replace('''    s = re.sub(r'<button class="lang-flag active" data-lang="zh"', '<button class="lang-flag" data-lang="zh"', s)''',
                  '''    s = re.sub(r'<button class="lang-flag active"', '<button class="lang-flag"', s)''', 1)
    s = s.replace("""    if lang not in LANGS:
        print('语言必须是 en/fr/es')""",
                  """    if lang not in LANGS:
        print('语言必须是 en/fr/es/ja/ko')""", 1)
    s = s.replace("print('用法: python gen_i18n.py <en|fr|es> <page1.html> [page2.html ...]')",
                  "print('用法: python gen_i18n.py <en|fr|es|ja|ko> <page1.html> [page2.html ...]')", 1)

    for needle in ['"ja": "ja"', 'data-ja', 'hl_hrefs', 'HTML_LANG']:
        assert needle in s, 'gen_i18n.py 缺失: %s' % needle
    if not DRY:
        open(p, 'w', encoding='utf-8').write(s)
    return s != s0


if __name__ == '__main__':
    files = [p for p in ['index.html', 'products.html', 'about.html', 'contact.html', 'blog/index.html'] if os.path.exists(p)]
    files += [p for p in sorted(glob.glob('blog/*.html')) if not p.replace('\\', '/').endswith('index.html')]
    stats = {}
    bad = []
    for f in files:
        for entry in patch_source(f):
            stats[entry] = stats.get(entry, 0) + 1
            if entry.startswith('!!'):
                bad.append((f, entry))
    print('源页面: %d 个' % len(files))
    print('改动统计:', stats)
    if bad:
        print('异常:', bad[:10])
    print('main.js 已改:', patch_main_js())
    print('gen_i18n.py 已改:', patch_gen_i18n())
    if DRY:
        print('(dry-run，未写盘)')
