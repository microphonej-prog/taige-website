#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-08 晚批次本地校验：
① 2 篇新文件（根 + en/ja/ko/fr/es）是否存在
② 根文件 .article-body 内 data-zh 元素缺 data-en/fr/es/ja/ko 的数量
③ blog/index.html 有新卡片且卡片位置在 post-grid 顶部
④ 各语言版本 title 是否已本地渲染（无 data-* 残留）
⑤ sitemap 含 12 个新 URL，且 blog index lastmod 已更新
⑥ JSON-LD 合法性 + 版本号
"""
import os, re, sys, json

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
from html.parser import HTMLParser

SLUGS = ["vacuum-compression-apparel-packaging.html", "stone-paper-hang-tags-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
WANT = ("data-zh", "data-en", "data-fr", "data-es", "data-ja", "data-ko")

bad = 0
print("=== ① 文件存在性 ===")
for s in SLUGS:
    for p in ["blog/%s" % s] + ["%s/blog/%s" % (l, s) for l in LANGS]:
        ok = os.path.exists(p)
        bad += (not ok)
        print("  %-56s %s" % (p, "OK" if ok else "!! 缺失"))


class C(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.n = 0
        self.miss = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "data-zh" in d:
            self.n += 1
            m = [k for k in WANT if k not in d]
            if m:
                self.miss.append((tag, d["data-zh"][:30], m))

    handle_startendtag = handle_starttag


print("\n=== ② 根文件正文属性完整性（article-body 容器内）===")
for s in SLUGS:
    raw = open("blog/%s" % s, encoding="utf-8").read()
    i0 = raw.index('<section class="article-body">')
    i1 = raw.index("</main>")
    seg = raw[i0:i1]
    c = C()
    c.feed(seg)
    empty = re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', seg)
    print("  %-44s data-zh 元素=%d 缺属性=%d 空值=%d" % (s, c.n, len(c.miss), len(empty)))
    bad += len(c.miss) + len(empty)
    for m in c.miss[:8]:
        print("     MISS", m)

print("\n=== ③ blog/index.html 卡片 ===")
idxs = {"zh": "blog/index.html"}
for l in LANGS:
    idxs[l] = "%s/blog/index.html" % l
for l, p in idxs.items():
    idx = open(p, encoding="utf-8").read()
    grid = idx.index('<div class="post-grid">')
    for s in SLUGS:
        href = 'href="%s"' % s
        pos = idx.find(href)
        ok = (href in idx) and pos > grid
        bad += (not ok)
        print("  %-4s %-44s 卡片=%s 位于 post-grid 之后=%s" % (l, s, href in idx, pos > grid))

print("\n=== ④ 各语言 title 本地渲染（应无 data- 残留）===")
for s in SLUGS:
    for l in LANGS:
        p = "%s/blog/%s" % (l, s)
        t = re.search(r"<title[^>]*>(.*?)</title>", open(p, encoding="utf-8").read(), re.S).group(1)
        badt = ("data-" in t)
        bad += badt
        print("  %-4s %-44s %s" % (l, s[:40], ("!! 残留属性" if badt else t[:74])))
    t0 = re.search(r"<title[^>]*>(.*?)</title>",
                   open("blog/%s" % s, encoding="utf-8").read(), re.S).group(1)
    print("  %-4s %-44s %s" % ("zh", s[:40], t0[:74] if "data-" not in t0 else "!! 残留属性"))
    bad += ("data-" in t0)

print("\n=== ⑤ sitemap ===")
sm = open("sitemap.xml", encoding="utf-8").read()
for s in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % s] + \
             ["https://taigetag.com/%s/blog/%s" % (l, s) for l in LANGS]:
        if "<loc>%s</loc>" % u not in sm:
            bad += 1
            print("  !! 缺失", u)
print("  12 个新 URL %s；total <loc> = %d" % ("全部在 sitemap 中" if bad == 0 else "有缺失", sm.count("<loc>")))
for u in ["https://taigetag.com/blog/index.html"] + \
         ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    m = re.search(r"<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
    print("  blog index lastmod %-52s %s" % (u, m.group(1) if m else "!! 未找到"))
    bad += (m is None)

print("\n=== ⑥ JSON-LD 与版本号 ===")
for s in SLUGS:
    txt = open("blog/%s" % s, encoding="utf-8").read()
    ld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', txt, re.S)
    okjson = True
    for blk in ld:
        try:
            json.loads(blk)
        except Exception as e:
            okjson = False
            print("  !! JSON-LD 解析失败 %s: %s" % (s, e))
    grid = txt.count('class="post-grid"')
    print("  %-44s JSON-LD 块=%d 合法=%s post-grid 残留=%d" % (s, len(ld), okjson, grid))
    bad += (len(ld) != 1) + (not okjson) + grid

mj = open("js/main.js", encoding="utf-8").read()
print("  BUST_VERSION =", re.search(r'var BUST_VERSION = "([^"]*)"', mj).group(1))

print("\n结论:", "本地校验全部通过" if bad == 0 else "有 %d 处异常" % bad)
sys.exit(1 if bad else 0)
