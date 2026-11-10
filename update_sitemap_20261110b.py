#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sitemap：为本批 2 篇文章写入 8 语 URL（幂等），并刷新 8 语 blog 首页 lastmod。"""
import re

DATE = "2026-11-10"
SLUGS = ["label-stitch-density-spi-guide.html", "reusable-returnable-garment-packaging.html"]
LANGS = ["", "en/", "de/", "ja/", "ko/", "fr/", "es/", "pt/"]

path = "sitemap.xml"
s = open(path, encoding="utf-8", newline="").read()

# 1) blog 首页 lastmod（8 语）
for pre in LANGS:
    loc = "https://taigetag.com/%sblog/index.html" % pre
    pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)' % re.escape(loc))
    s, n = pat.subn(r'\g<1>%s\g<2>' % DATE, s, count=1)
    print("lastmod %s -> %s (%d)" % (loc, DATE, n))

# 2) 文章 URL
blocks = []
for slug in SLUGS:
    new = 0
    for pre in LANGS:
        loc = "https://taigetag.com/%sblog/%s" % (pre, slug)
        pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>\r?\n\s*<changefreq>)[^<]*(</changefreq>\r?\n\s*<priority>)[^<]*(</priority>)'
                         % re.escape(loc))
        s, n = pat.subn(r'\g<1>%s\g<2>monthly\g<3>0.7\g<4>' % DATE, s, count=1)
        if n:
            print("更新已有 %s" % loc)
        else:
            blocks.append(
                "  <url>\r\n    <loc>%s</loc>\r\n    <lastmod>%s</lastmod>\r\n"
                "    <changefreq>monthly</changefreq>\r\n    <priority>0.7</priority>\r\n  </url>\r\n" % (loc, DATE))
            new += 1
    print("%s: 新增 %d / 8" % (slug, new))

s = s.replace("</urlset>", "".join(blocks) + "</urlset>", 1)
open(path, "w", encoding="utf-8", newline="").write(s)
print("追加 URL 块: %d" % len(blocks))

# 3) 去重与总数
locs = re.findall(r"<loc>([^<]+)</loc>", s)
dup = {u for u in locs if locs.count(u) > 1}
print("总 URL: %d  重复: %d %s" % (len(locs), len(dup), list(dup)[:5]))
