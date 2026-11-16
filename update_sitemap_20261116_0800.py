# -*- coding: utf-8 -*-
"""2026-11-16 08:00：把 2 篇新文章的 6 语 URL 写入 sitemap.xml，并更新 6 个 blog 首页 lastmod。"""
import re
import xml.etree.ElementTree as ET

DATE = "2026-11-16"
SLUGS = ["bag-hardware-d-rings-swivel-hooks-guide", "snap-fastener-press-stud-guide"]
PREF = ["blog/", "en/blog/", "fr/blog/", "es/blog/", "ja/blog/", "ko/blog/"]

path = "sitemap.xml"
s = open(path, encoding="utf-8", newline="").read()

# 1) 更新 6 个 blog 首页 lastmod
for pre in PREF:
    loc = "https://taigetag.com/%sindex.html" % pre
    pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)' % re.escape(loc))
    s, n = pat.subn(r'\g<1>%s\g<2>' % DATE, s, count=1)
    print("lastmod %s -> %s (%d)" % (loc, DATE, n))

# 2) 新增文章 URL（已在则就地更新）
assert "</urlset>" in s
blocks = []
for slug in SLUGS:
    for pre in PREF:
        loc = "https://taigetag.com/%s%s.html" % (pre, slug)
        pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>\r?\n\s*<changefreq>)[^<]*(</changefreq>\r?\n\s*<priority>)[^<]*(</priority>)'
                         % re.escape(loc))
        s, n = pat.subn(r'\g<1>%s\g<2>monthly\g<3>0.7\g<4>' % DATE, s, count=1)
        if n:
            print("更新已有条目 %s" % loc)
        else:
            blocks.append(
                "  <url>\r\n"
                "    <loc>%s</loc>\r\n"
                "    <lastmod>%s</lastmod>\r\n"
                "    <changefreq>monthly</changefreq>\r\n"
                "    <priority>0.7</priority>\r\n"
                "  </url>\r\n" % (loc, DATE))

s = s.replace("</urlset>", "".join(blocks) + "</urlset>", 1)

with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(s)

# 3) 校验
root = ET.parse(path).getroot()
locs = [e.text for e in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
print("新增 URL 块:", len(blocks))
print("sitemap 总 URL:", len(locs), " 去重后:", len(set(locs)))
for slug in SLUGS:
    hits = [u for u in locs if slug in u]
    print(slug, "->", len(hits), "条")
    for u in hits:
        print("   ", u)
