# -*- coding: utf-8 -*-
"""2026-11-15 14:00：向 sitemap.xml 追加当日 2 篇（6 语）并更新 blog 首页 lastmod。"""
import re

DATE = "2026-11-15"
SLUGS = ["clothing-tagging-gun-swift-tack-guide", "garment-label-font-size-legibility-guide"]
LANGS = ["blog/", "en/blog/", "fr/blog/", "es/blog/", "ja/blog/", "ko/blog/"]

path = "sitemap.xml"
with open(path, encoding="utf-8", newline="") as f:
    s = f.read()

before = s
for loc in ["https://taigetag.com/%sindex.html" % p for p in LANGS]:
    pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)' % re.escape(loc))
    s, n = pat.subn(r'\g<1>%s\g<2>' % DATE, s, count=1)
    print("lastmod %s -> %s (%d)" % (loc, DATE, n))

assert "</urlset>" in s
blocks = []
for slug in SLUGS:
    done = 0
    for pre in LANGS:
        loc = "https://taigetag.com/%s%s.html" % (pre, slug)
        pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>\r?\n\s*<changefreq>)[^<]*(</changefreq>\r?\n\s*<priority>)[^<]*(</priority>)'
                         % re.escape(loc))
        s, n = pat.subn(r'\g<1>%s\g<2>monthly\g<3>0.7\g<4>' % DATE, s, count=1)
        if n:
            done += 1
            print("更新已有条目 %s" % loc)
        else:
            blocks.append(
                "  <url>\r\n"
                "    <loc>%s</loc>\r\n"
                "    <lastmod>%s</lastmod>\r\n"
                "    <changefreq>monthly</changefreq>\r\n"
                "    <priority>0.7</priority>\r\n"
                "  </url>\r\n" % (loc, DATE))
    print("%s: 已有 %d，新增 %d" % (slug, done, len(LANGS) - done))

s = s.replace("</urlset>", "".join(blocks) + "</urlset>", 1)

with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(s)
print("追加 URL 块: %d" % len(blocks))
print("sitemap 总 URL 数:", s.count("<loc>"))

# XML 合法性
import xml.etree.ElementTree as ET
ET.parse(path)
print("XML 解析通过")

# 重复 URL 检查
locs = re.findall(r"<loc>(.*?)</loc>", s)
dups = {u for u in locs if locs.count(u) > 1}
print("重复 URL:", dups if dups else "无")
