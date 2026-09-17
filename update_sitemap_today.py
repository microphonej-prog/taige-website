#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""向 sitemap.xml 追加当日新增文章（4 语言）并更新 blog 首页 lastmod"""
import re

DATE = "2026-09-17"
SLUGS = ["garment-trims-supplier-audit.html", "garment-trims-cost-saving-guide.html"]
LANGS = ["blog/", "en/blog/", "fr/blog/", "es/blog/"]

path = "sitemap.xml"
with open(path, encoding="utf-8", newline="") as f:
    s = f.read()

# 1) 更新 blog 首页（含 4 语言）lastmod
before = s
for loc in ["https://taigetag.com/blog/index.html",
            "https://taigetag.com/en/blog/index.html",
            "https://taigetag.com/fr/blog/index.html",
            "https://taigetag.com/es/blog/index.html"]:
    pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)' % re.escape(loc))
    s, n = pat.subn(r'\g<1>%s\g<2>' % DATE, s, count=1)
    print("lastmod %s -> %s (%d)" % (loc, DATE, n))

# 2) 追加新 URL（每篇 4 语言）
blocks = []
for slug in SLUGS:
    for pre in LANGS:
        blocks.append(
            "  <url>\r\n"
            "    <loc>https://taigetag.com/%s%s</loc>\r\n"
            "    <lastmod>%s</lastmod>\r\n"
            "    <changefreq>monthly</changefreq>\r\n"
            "    <priority>0.7</priority>\r\n"
            "  </url>\r\n" % (pre, slug, DATE))

assert "</urlset>" in s
s = s.replace("</urlset>", "".join(blocks) + "</urlset>", 1)

with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(s)
print("追加 URL 块: %d" % len(blocks))
print("新增行数: %d" % (s.count("\n") - before.count("\n")))
