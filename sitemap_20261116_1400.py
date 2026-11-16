# -*- coding: utf-8 -*-
"""2026-11-16 14:00 文章入 sitemap：2 篇 × 6 语 + blog 首页 lastmod。"""
import re
import xml.etree.ElementTree as ET

DATE = "2026-11-16"
SLUGS = ["goh-vs-flat-pack-apparel-shipping-guide.html",
         "clothing-label-compliance-new-zealand.html"]
PREFIX = ["blog/", "en/blog/", "fr/blog/", "es/blog/", "ja/blog/", "ko/blog/"]

path = "sitemap.xml"
with open(path, encoding="utf-8", newline="") as f:
    s = f.read()
before_lines = s.count("\n")

# 1) blog 首页 lastmod
for pre in PREFIX:
    loc = "https://taigetag.com/%sindex.html" % pre
    pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)' % re.escape(loc))
    s, n = pat.subn(r'\g<1>%s\g<2>' % DATE, s, count=1)
    print("lastmod %s -> %s (%d)" % (loc, DATE, n))

# 2) 文章 URL
blocks = []
added = updated = 0
for slug in SLUGS:
    for pre in PREFIX:
        loc = "https://taigetag.com/%s%s" % (pre, slug)
        pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>\r?\n\s*<changefreq>)[^<]*(</changefreq>\r?\n\s*<priority>)[^<]*(</priority>)'
                         % re.escape(loc))
        s, n = pat.subn(r'\g<1>%s\g<2>monthly\g<3>0.7\g<4>' % DATE, s, count=1)
        if n:
            updated += 1
        else:
            blocks.append(
                "  <url>\r\n    <loc>%s</loc>\r\n    <lastmod>%s</lastmod>\r\n"
                "    <changefreq>monthly</changefreq>\r\n    <priority>0.7</priority>\r\n  </url>\r\n"
                % (loc, DATE))
            added += 1

s = s.replace("</urlset>", "".join(blocks) + "</urlset>", 1)
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(s)

# 3) 校验
t = ET.parse(path)
locs = [e.text for e in t.iter() if e.tag.endswith("loc")]
dups = {u for u in locs if locs.count(u) > 1}
print("新增 %d 条，更新 %d 条，URL 总数 %d，重复 %d 条" % (added, updated, len(locs), len(dups)))
for slug in SLUGS:
    print(slug, sum(1 for u in locs if u.endswith(slug)))
