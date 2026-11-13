#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为 2026-11-13 20:00 两篇新文章追加 sitemap（6 语），并刷新 blog 首页 lastmod。"""
import re

DATE = "2026-11-13"
SLUGS = ["trim-crocking-perspiration-fastness-guide.html", "garment-trims-small-parts-safety-guide.html"]
LANGS = ["blog/", "en/blog/", "fr/blog/", "es/blog/", "ja/blog/", "ko/blog/"]

path = "sitemap.xml"
s = open(path, encoding="utf-8", newline="").read()
before_lines = s.count("\n")

# 1) blog 首页 lastmod（6 语）
for pre in LANGS:
    loc = "https://taigetag.com/%sindex.html" % pre
    pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)' % re.escape(loc))
    s, n = pat.subn(r'\g<1>%s\g<2>' % DATE, s, count=1)
    print("lastmod %s -> %s (%d)" % (loc, DATE, n))

# 2) 新增文章 URL
blocks = []
for slug in SLUGS:
    for pre in LANGS:
        loc = "https://taigetag.com/%s%s" % (pre, slug)
        assert "<loc>%s</loc>" % loc not in s, "已存在: %s" % loc
        blocks.append(
            "  <url>\r\n"
            "    <loc>%s</loc>\r\n"
            "    <lastmod>%s</lastmod>\r\n"
            "    <changefreq>monthly</changefreq>\r\n"
            "    <priority>0.7</priority>\r\n"
            "  </url>\r\n" % (loc, DATE))
s = s.replace("</urlset>", "".join(blocks) + "</urlset>", 1)
open(path, "w", encoding="utf-8", newline="").write(s)
print("追加 %d 条 URL；新增行数 %d" % (len(blocks), s.count("\n") - before_lines))

# 3) XML 合法性
import xml.etree.ElementTree as ET
t = ET.parse(path)
locs = [e.text for e in t.iter() if e.tag.endswith("loc")]
print("XML 合法，<loc> 总数 %d，重复 %d" % (len(locs), len(locs) - len(set(locs))))
