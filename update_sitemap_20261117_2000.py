#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-17 20:00：把当日新增 2 篇（6 语）写入 sitemap，并刷新 blog 列表页 lastmod。"""
import re

DATE = "2026-11-17"
SLUGS = ["hang-tag-back-printing-guide.html", "apparel-trims-chargeback-guide.html"]
LANGS = ["blog/", "en/blog/", "fr/blog/", "es/blog/", "ja/blog/", "ko/blog/"]

path = "sitemap.xml"
with open(path, encoding="utf-8", newline="") as f:
    s = f.read()

# 1) blog 列表页 lastmod（6 语）
for pre in ["blog/", "en/blog/", "fr/blog/", "es/blog/", "ja/blog/", "ko/blog/"]:
    loc = "https://taigetag.com/%sindex.html" % pre
    pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)' % re.escape(loc))
    s, n = pat.subn(r'\g<1>%s\g<2>' % DATE, s, count=1)
    print("lastmod %s -> %s (%d)" % (loc, DATE, n))

# 2) 文章 URL（6 语）
assert "</urlset>" in s
blocks = []
added = updated = 0
for slug in SLUGS:
    for pre in LANGS:
        loc = "https://taigetag.com/%s%s" % (pre, slug)
        pat = re.compile(
            r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>\r?\n\s*<changefreq>)[^<]*(</changefreq>\r?\n\s*<priority>)[^<]*(</priority>)'
            % re.escape(loc))
        s, n = pat.subn(r'\g<1>%s\g<2>monthly\g<3>0.7\g<4>' % DATE, s, count=1)
        if n:
            updated += 1
        else:
            assert loc not in s, "URL 已存在但结构不同，需人工处理: %s" % loc
            blocks.append(
                "  <url>\r\n"
                "    <loc>%s</loc>\r\n"
                "    <lastmod>%s</lastmod>\r\n"
                "    <changefreq>monthly</changefreq>\r\n"
                "    <priority>0.7</priority>\r\n"
                "  </url>\r\n" % (loc, DATE))
            added += 1

s = s.replace("</urlset>", "".join(blocks) + "</urlset>", 1)
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(s)

# 3) 校验 XML 合法 + 计数
import xml.etree.ElementTree as ET
ET.parse(path)
locs = re.findall(r"<loc>(.*?)</loc>", s)
print("sitemap 新增 %d 条、更新 %d 条；总 URL = %d；重复 URL = %d"
      % (added, updated, len(locs), len(locs) - len(set(locs))))
for slug in SLUGS:
    print(slug, "出现", sum(1 for u in locs if slug in u), "次")
