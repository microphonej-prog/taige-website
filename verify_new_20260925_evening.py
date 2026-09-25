#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-25 晚间批次本地校验：六语属性完整性 / 生成页残留 / 列表卡片 / sitemap / JSON-LD / 引号畸形"""
import re, os, sys, json
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')
os.chdir(r"C:\Users\micro\taige-website")

SLUGS = ["garment-trims-fabric-compatibility-guide.html", "textile-phenolic-yellowing-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
BAD = 0


class C(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, {k.lower(): (v or '') for k, v in attrs}))


print("== 1) 六语版本存在性 + 正文六语完整性 ==")
for slug in SLUGS:
    for pre in [""] + [l + "/" for l in LANGS]:
        p = "%sblog/%s" % (pre, slug)
        if not os.path.exists(p):
            print("  XX 缺失", p); BAD += 1; continue
        s = open(p, encoding='utf-8').read()
        pp = C(); pp.feed(s)
        dzh = [(t, a) for t, a in pp.tags if 'data-zh' in a]
        need = ('data-en', 'data-ja', 'data-ko', 'data-fr', 'data-es')
        miss = [(t, k) for t, a in dzh for k in need if not a.get(k, '').strip()]
        residue = sum(1 for t, a in pp.tags if any(k in ('data-zh', 'data-en', 'data-ja', 'data-ko', 'data-fr', 'data-es') for k in a))
        t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S)
        d = re.search(r'<meta name="description" content="([^"]*)"', s)
        lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
        for x in lds:
            json.loads(x)
        amp = len(re.findall(r'&(?!amp;|nbsp;|quot;|#|lt;|gt;|middot;)', s))
        qbad = len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s))
        can = re.search(r'<link rel="canonical" href="([^"]*)"', s)
        print("  %-58s 六语缺=%d 数据残留=%d title=%s desc=%d字 JSON-LD=%d 裸&=%d 空值=%d"
              % (p, len(miss), residue, (t.group(1)[:34] if t else '-'), len(d.group(1)) if d else -1, len(lds), amp, qbad))
        if miss or residue or amp or qbad or len(lds) != 1:
            BAD += 1
            print("     ", miss[:5])
        if can is None:
            print("      无 canonical"); BAD += 1

print("== 2) 生成页语言纯净度（en/fr/es/ko 正文不得含中日韩汉字；ja 必须含假名）==")
for slug in SLUGS:
    for lang in LANGS:
        p = "%s/blog/%s" % (lang, slug)
        s = open(p, encoding='utf-8').read()
        m0 = s.index('<section class="article-body">')
        m1 = s.index('</section>', m0)
        body = s[m0:m1]
        body = re.sub(r'<script.*?</script>', '', body, flags=re.S)
        han = len(re.findall(r'[\u4e00-\u9fff]', body))
        kana = len(re.findall(r'[\u3040-\u30ff]', body))
        hangul = len(re.findall(r'[\uac00-\ud7af]', body))
        ok = True
        if lang in ('en', 'fr', 'es', 'ko') and han:
            ok = False
        if lang == 'ja' and kana < 50:
            ok = False
        if lang == 'ko' and hangul < 50:
            ok = False
        print("  %-56s 汉字=%d 假名=%d 韩字=%d %s" % (p, han, kana, hangul, "OK" if ok else "XX"))
        if not ok:
            BAD += 1

print("== 3) blog 列表页卡片（六语，且位于 post-grid 顶部）==")
for pre in [""] + [l + "/" for l in LANGS]:
    p = "%sblog/index.html" % pre
    s = open(p, encoding='utf-8').read()
    grid = s[s.index('<div class="post-grid">'):]
    head = grid[:4000]
    hits = [sl for sl in SLUGS if sl in head]
    order_ok = head.index(SLUGS[0]) < head.index(SLUGS[1]) if len(hits) == 2 else False
    print("  %-28s 顶部命中 %d/2 顺序=%s" % (p, len(hits), order_ok))
    if len(hits) != 2:
        BAD += 1

print("== 4) sitemap ==")
sm = open("sitemap.xml", encoding='utf-8').read()
cnt = 0
for slug in SLUGS:
    for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS]:
        u = "https://taigetag.com/%s%s" % (pre, slug)
        pat = re.compile(r'<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(u))
        m = pat.search(sm)
        if not m:
            print("  XX 缺", u); BAD += 1
        else:
            cnt += 1
            if m.group(1) != "2026-09-25":
                print("  XX lastmod", u, m.group(1)); BAD += 1
print("  新 URL 齐全 %d/12，<loc> 总数 %d" % (cnt, sm.count("<loc>")))
for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS]:
    u = "https://taigetag.com/%sindex.html" % pre
    pat = re.compile(r'<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(u))
    m = pat.search(sm)
    if not m or m.group(1) != "2026-09-25":
        print("  XX blog index lastmod", u, m.group(1) if m else None); BAD += 1

print("== 5) BUST_VERSION ==")
mj = open("js/main.js", encoding='utf-8').read()
m = re.search(r'var BUST_VERSION = "([^"]*)"', mj)
print("  BUST_VERSION =", m.group(1), "OK" if m.group(1) == "110" else "XX")
if m.group(1) != "110":
    BAD += 1

print("\n结论: 问题总数 =", BAD)
raise SystemExit(1 if BAD else 0)
