# -*- coding: utf-8 -*-
"""2026-11-14 14:00：把 2 篇新文章的 6 语 URL 写入 sitemap，并刷新 blog 首页 lastmod。"""
import re
import xml.etree.ElementTree as ET

DATE = "2026-11-14"
SLUGS = ["apparel-size-designation-en-13402.html", "silicone-gripper-tape-guide.html"]
LANGS = ["blog/", "en/blog/", "fr/blog/", "es/blog/", "ja/blog/", "ko/blog/"]

path = "sitemap.xml"
with open(path, encoding="utf-8", newline="") as f:
    s = f.read()

# 1) blog 首页 lastmod
for pre in LANGS:
    loc = "https://taigetag.com/%sindex.html" % pre
    pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)' % re.escape(loc))
    s, n = pat.subn(r"\g<1>%s\g<2>" % DATE, s, count=1)
    print("lastmod %s -> %s (%d)" % (loc, DATE, n))

# 2) 文章 URL
blocks, added, updated = [], 0, 0
for slug in SLUGS:
    for pre in LANGS:
        loc = "https://taigetag.com/%s%s" % (pre, slug)
        pat = re.compile(
            r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>\r?\n\s*<changefreq>)[^<]*(</changefreq>\r?\n\s*<priority>)[^<]*(</priority>)'
            % re.escape(loc))
        s, n = pat.subn(r"\g<1>%s\g<2>monthly\g<3>0.7\g<4>" % DATE, s, count=1)
        if n:
            updated += 1
        else:
            blocks.append(
                "  <url>\r\n"
                "    <loc>%s</loc>\r\n"
                "    <lastmod>%s</lastmod>\r\n"
                "    <changefreq>monthly</changefreq>\r\n"
                "    <priority>0.7</priority>\r\n"
                "  </url>\r\n" % (loc, DATE))
            added += 1

assert "</urlset>" in s
s = s.replace("</urlset>", "".join(blocks) + "</urlset>", 1)
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(s)

tree = ET.parse(path)
root = tree.getroot()
locs = [e.text for e in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
print("XML 合法；URL 总数 %d；本次新增 %d，就地更新 %d；重复 URL %d"
      % (len(locs), added, updated, len(locs) - len(set(locs))))
