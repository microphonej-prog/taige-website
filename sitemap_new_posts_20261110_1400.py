#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-10 14:00 每日文章：sitemap 加 2 篇 × 8 语 = 16 个 URL，刷新 8 个 blog 列表页 lastmod。"""
import re
import sys

DATE = "2026-11-10"
SLUGS = ["care-label-thermal-transfer-ribbon-guide.html", "apparel-trims-aql-inspection-guide.html"]
PREFIX = ["", "en/", "fr/", "es/", "ja/", "ko/", "de/", "pt/"]

path = "sitemap.xml"
s = open(path, encoding="utf-8", newline="").read()

for pre in PREFIX:
    loc = "https://taigetag.com/%sblog/index.html" % pre
    pat = re.compile(r"(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)" % re.escape(loc))
    s, n = pat.subn(r"\g<1>%s\g<2>" % DATE, s, count=1)
    print("lastmod %s -> %s (%d)" % (loc, DATE, n))

assert "</urlset>" in s
blocks = []
added = 0
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
            added += 1

s = s.replace("</urlset>", "".join(blocks) + "</urlset>", 1)
open(path, "w", encoding="utf-8", newline="").write(s)

locs = re.findall(r"<loc>([^<]+)</loc>", s)
print("sitemap URL 总数 %d，重复 %d，本次新增 %d" % (len(locs), len(locs) - len(set(locs)), added))
for slug in SLUGS:
    hit = [l for l in locs if slug in l]
    print(slug, "条目", len(hit))
sys.exit(0)
