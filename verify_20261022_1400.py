#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-22 14:00 批次本地校验：六语文件 / title / 正文属性 / 卡片 / sitemap"""
import os, re, sys
from daily_meta_20261022_1400 import ARTICLES

LANGS = ["en", "ja", "ko", "fr", "es"]
ok = True


def chk(cond, msg):
    global ok
    print(("  ✓ " if cond else "  ✗ ") + msg)
    if not cond:
        ok = False


for a in ARTICLES:
    slug = a["slug"]
    print("\n== %s ==" % slug)
    paths = ["blog/" + slug] + ["%s/blog/%s" % (l, slug) for l in LANGS]
    for p in paths:
        chk(os.path.exists(p), "存在 %s" % p)
    # 根页 title / h1
    s = open("blog/" + slug, encoding="utf-8").read()
    t = re.search(r'<title[^>]*>([^<]*)</title>', s).group(1)
    chk("TAGE" in t and "針織" not in t, "根页 title: %s" % t[:60])
    for attr in ["data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es"]:
        chk(attr in s[:2000], "title 带 %s" % attr)
    h1 = re.search(r'<h1[^>]*>([^<]*)</h1>', s).group(1)
    chk(a["h1_zh"] != h1 and len(h1) > 5, "根页 h1: %s" % h1[:50])
    # 骨架残留
    chk("knitwear-sweater-trims-guide" not in s, "无骨架 URL 残留")
    chk("針織與毛衣類服裝輔料指南" not in s, "无骨架 h1 残留")
    # canonical / hreflang
    can = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
    chk(can == "https://taigetag.com/blog/" + slug, "canonical %s" % can)
    hl = len(re.findall(r'hreflang="', s))
    chk(hl == 7, "hreflang 数=%d (zh-Hant+5+x-default)" % hl)
    # 各语言 title 渲染（gen_i18n 静态化）
    for l in LANGS:
        q = "%s/blog/%s" % (l, slug)
        x = open(q, encoding="utf-8").read()
        tt = re.search(r'<title>([^<]*)</title>', x)
        chk(bool(tt) and "TAGE" in tt.group(1) and "針織" not in tt.group(1),
            "%s title: %s" % (l, (tt.group(1)[:50] if tt else "缺失")))
        chk('<html lang="%s"' % l in x, "%s html lang" % l)
        chk("data-zh=" not in x and "data-en=" not in x, "%s 无残留 data-* 语言属性" % l)
        # 正文首段语言纯净
        body = x[x.index('article-body'):]
        first = re.search(r'<p>([^<]{20,})</p>', body)
        if first:
            txt = first.group(1)
            cjk = len(re.findall(r'[\u4e00-\u9fff]', txt))
            chk((l == "ja") or cjk == 0, "%s 正文首段无汉字残留(%d)" % (l, cjk))
    # 正文属性完整性（根页）
    body = s[s.index('<section class="article-body">'):]
    els = re.findall(r'<(?:p|h2|h3|li|td|th|div|a|span)\s[^>]*data-zh=', body)
    miss = 0
    for tag in re.finditer(r'<(\w+)\s((?:[^>"\']|"[^"]*"|\'[^\']*\')*)>', body):
        at = tag.group(2)
        if "data-zh=" not in at:
            continue
        for l in ["en", "ja", "ko", "fr", "es"]:
            if ("data-%s=" % l) not in at:
                miss += 1
                print("    缺 data-%s: %s" % (l, at[:60]))
    chk(miss == 0, "正文四/六语属性缺失数=%d（根页元素 %d 个）" % (miss, len(els)))
    # 相关文章链接可访问
    for href in re.findall(r'<a href="([a-z0-9\-]+\.html)"', body):
        chk(os.path.exists("blog/" + href), "相关链接存在 %s" % href)

# blog/index.html 卡片
idx = open("blog/index.html", encoding="utf-8").read()
grid = idx[idx.index('<div class="post-grid">'):]
for a in ARTICLES:
    pos = grid.find('href="%s"' % a["slug"])
    chk(pos > 0 and pos < 6000, "卡片靠前 %s (位置 %d)" % (a["slug"], pos))
for l in LANGS:
    x = open("%s/blog/index.html" % l, encoding="utf-8").read()
    for a in ARTICLES:
        chk('href="%s"' % a["slug"] in x, "%s/blog/index.html 含卡片 %s" % (l, a["slug"]))

# sitemap
sm = open("sitemap.xml", encoding="utf-8").read()
for a in ARTICLES:
    for u in ["https://taigetag.com/blog/%s" % a["slug"]] + \
             ["https://taigetag.com/%s/blog/%s" % (l, a["slug"]) for l in LANGS]:
        chk("<loc>%s</loc>" % u in sm, "sitemap 含 %s" % u)
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    m = re.search(r'<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    chk(bool(m) and m.group(1) == "2026-10-22", "blog index lastmod %s = %s" % (u[-24:], m.group(1) if m else "?"))

# BUST_VERSION
mj = open("js/main.js", encoding="utf-8").read()
chk('var BUST_VERSION = "176";' in mj, "BUST_VERSION=176")

print("\nRESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
