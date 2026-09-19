#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""向 sitemap.xml 追加当日新增文章（4 语言）并更新 blog 首页 lastmod"""
import re

DATE = "2026-09-19"
SLUGS = ["carton-shipping-mark-guide.html", "prop65-apparel-trims-guide.html"]
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

# 2) 新增或更新当日文章 URL（每篇 4 语言）
assert "</urlset>" in s
blocks = []
for slug in SLUGS:
    done = 0
    for pre in LANGS:
        loc = "https://taigetag.com/%s%s" % (pre, slug)
        # 已存在（历史遗留的孤儿条目）→ 就地更新 lastmod/changefreq/priority，不重复追加
        pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>\r?\n\s*<changefreq>)[^<]*(</changefreq>\r?\n\s*<priority>)[^<]*(</priority>)'
                         % re.escape(loc))
        s, n = pat.subn(r'\g<1>%s\g<2>monthly\g<3>0.7\g<4>' % DATE, s, count=1)
        if n:
            done += 1
            print("更新已有条目 %s -> lastmod %s" % (loc, DATE))
        else:
            blocks.append(
                "  <url>\r\n"
                "    <loc>%s</loc>\r\n"
                "    <lastmod>%s</lastmod>\r\n"
                "    <changefreq>monthly</changefreq>\r\n"
                "    <priority>0.7</priority>\r\n"
                "  </url>\r\n" % (loc, DATE))
    print("%s: 已有 %d 条，新增 %d 条" % (slug, done, 4 - done))

s = s.replace("</urlset>", "".join(blocks) + "</urlset>", 1)

with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(s)
print("追加 URL 块: %d" % len(blocks))
print("新增行数: %d" % (s.count("\n") - before.count("\n")))
