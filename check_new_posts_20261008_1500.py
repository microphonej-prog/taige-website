#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-08 下午批次本地校验：
① 2 篇新文件（根 + en/ja/ko/fr/es）是否存在
② 根文件 .article-body 内 data-zh 元素缺 data-en/fr/es/ja/ko 的数量
③ blog/index.html 有新卡片且卡片位置在 post-grid 顶部
④ 各语言版本 title 是否已本地渲染（无 data-* 残留）
⑤ sitemap 含 12 个新 URL，且 blog index lastmod 已更新
"""
import os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
from html.parser import HTMLParser

SLUGS = ["wooden-bamboo-hang-tags.html", "print-on-demand-apparel-labels.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
WANT = ("data-zh", "data-en", "data-fr", "data-es", "data-ja", "data-ko")

print("=== ① 文件存在性 ===")
for s in SLUGS:
    for p in ["blog/%s" % s] + ["%s/blog/%s" % (l, s) for l in LANGS]:
        print("  %-52s %s" % (p, "OK" if os.path.exists(p) else "!! 缺失"))


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
    bad = re.findall(r'data-(?:zh|en|fr|es|ja|ko)=\"\"', seg)
    print("  %-42s data-zh 元素=%d 缺属性=%d 空值=%d" % (s, c.n, len(c.miss), len(bad)))
    for m in c.miss[:8]:
        print("     MISS", m)

print("\n=== ③ blog/index.html 卡片 ===")
idx = open("blog/index.html", encoding="utf-8").read()
grid = idx.index('<div class="post-grid">')
for s in SLUGS:
    href = 'href="%s"' % s
    pos = idx.find(href)
    print("  %-42s 卡片存在=%s 位于 post-grid 之后=%s" % (s, href in idx, pos > grid))

print("\n=== ④ 各语言 title 本地渲染（应无 data- 残留）===")
for s in SLUGS:
    for l in LANGS:
        p = "%s/blog/%s" % (l, s)
        t = re.search(r"<title[^>]*>(.*?)</title>", open(p, encoding="utf-8").read(), re.S).group(1)
        print("  %-4s %-42s %s" % (l, s[:38], ("!! 残留属性" if "data-" in t else t[:70])))

print("\n=== ⑤ sitemap ===")
sm = open("sitemap.xml", encoding="utf-8").read()
for s in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % s] + \
             ["https://taigetag.com/%s/blog/%s" % (l, s) for l in LANGS]:
        assert "<loc>%s</loc>" % u in sm, "缺失 " + u
print("  12 个新 URL 全部在 sitemap 中 OK；total <loc> = %d" % sm.count("<loc>"))
for u in ["https://taigetag.com/blog/index.html"] + \
         ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    m = re.search(r"<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
    print("  blog index lastmod %-52s %s" % (u, m.group(1) if m else "!! 未找到"))

print("\n=== ⑥ 版本号 ===")
mj = open("js/main.js", encoding="utf-8").read()
print("  BUST_VERSION =", re.search(r'var BUST_VERSION = "([^"]*)"', mj).group(1))
