#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-09 20:00：把两篇新文章的 8 语 URL 写入 sitemap.xml，更新 blog 首页 lastmod。"""
import re
import sys

DATE = "2026-11-09"
SLUGS = ["clothing-label-compliance-taiwan.html", "formaldehyde-apparel-trims-guide.html"]
PREFIXES = ["blog/", "en/blog/", "de/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/", "pt/blog/"]
IDX = ["https://taigetag.com/blog/index.html"] + [
    "https://taigetag.com/%s/blog/index.html" % l for l in ("en", "ja", "ko", "fr", "es")]

path = "sitemap.xml"
s = open(path, encoding="utf-8", newline="").read()

# 1) blog 首页 lastmod（6 条：zh/en/ja/ko/fr/es；de/pt 列表页 noindex，不入 sitemap）
for loc in IDX:
    pat = re.compile(r'(<loc>%s</loc>\s*<lastmod>)[^<]*(</lastmod>)' % re.escape(loc))
    s, n = pat.subn(lambda m: m.group(1) + DATE + m.group(2), s, count=1)
    print("lastmod %-55s %d" % (loc, n))

# 2) 追加新文章 URL（幂等：已存在则只更新 lastmod）
added = 0
for slug in SLUGS:
    for pre in PREFIXES:
        loc = "https://taigetag.com/%s%s" % (pre, slug)
        if "<loc>%s</loc>" % loc in s:
            pat = re.compile(r'(<loc>%s</loc>\s*<lastmod>)[^<]*(</lastmod>)' % re.escape(loc))
            s, n = pat.subn(lambda m: m.group(1) + DATE + m.group(2), s, count=1)
            print("已存在，仅更新 lastmod: %s (%d)" % (loc, n))
            continue
        block = ("  <url>\r\n    <loc>%s</loc>\r\n    <lastmod>%s</lastmod>\r\n"
                 "    <changefreq>monthly</changefreq>\r\n    <priority>0.7</priority>\r\n  </url>\r\n") % (loc, DATE)
        s = s.replace("</urlset>", block + "</urlset>", 1)
        added += 1

print("新增 URL 数: %d" % added)

# 3) 校验：无重复 loc
locs = re.findall(r"<loc>([^<]+)</loc>", s)
dups = {u for u in locs if locs.count(u) > 1}
print("总 URL: %d  重复: %d %s" % (len(locs), len(dups), sorted(dups)[:5]))

with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(s)
assert "<urlset" in s and s.rstrip().endswith("</urlset>")
print("sitemap 写入完成")
