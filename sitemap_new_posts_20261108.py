#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-08 每日文章：向 sitemap.xml 加入两篇 × 8 语 共 16 个 URL，并刷新 8 个 blog 列表页 lastmod。"""
import re

DATE = "2026-11-08"
SLUGS = ["silica-gel-desiccant-apparel-packaging.html", "care-label-roll-direction-core-guide.html"]
PREFIX = ["", "en/", "fr/", "es/", "ja/", "ko/", "de/", "pt/"]

path = "sitemap.xml"
s = open(path, encoding="utf-8", newline="").read()
before = s

# 1) blog 列表页 lastmod
for pre in PREFIX:
    loc = "https://taigetag.com/%sblog/index.html" % pre
    pat = re.compile(r"(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)" % re.escape(loc))
    s, n = pat.subn(r"\g<1>%s\g<2>" % DATE, s, count=1)
    print("lastmod %s -> %s (%d)" % (loc, DATE, n))

# 2) 文章 URL
assert "</urlset>" in s
blocks = []
for slug in SLUGS:
    for pre in PREFIX:
        loc = "https://taigetag.com/%sblog/%s" % (pre, slug)
        pat = re.compile(r"(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>\r?\n\s*<changefreq>)[^<]*"
                         r"(</changefreq>\r?\n\s*<priority>)[^<]*(</priority>)" % re.escape(loc))
        s, n = pat.subn(r"\g<1>%s\g<2>monthly\g<3>0.7\g<4>" % DATE, s, count=1)
        if n:
            print("更新已有条目", loc)
        else:
            blocks.append("  <url>\r\n    <loc>%s</loc>\r\n    <lastmod>%s</lastmod>\r\n"
                          "    <changefreq>monthly</changefreq>\r\n    <priority>0.7</priority>\r\n  </url>\r\n"
                          % (loc, DATE))

s = s.replace("</urlset>", "".join(blocks) + "</urlset>", 1)
open(path, "w", encoding="utf-8", newline="").write(s)

locs = re.findall(r"<loc>([^<]+)</loc>", s)
print("追加 URL 块: %d ；sitemap 总 URL: %d ；重复: %d" % (len(blocks), len(locs), len(locs) - len(set(locs))))
for slug in SLUGS:
    print(slug, "出现", sum(1 for l in locs if l.endswith(slug)), "次")
