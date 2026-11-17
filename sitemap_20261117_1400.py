# -*- coding: utf-8 -*-
"""2026-11-17 14:00：把两篇新文章的中文页与 5 个语言页写入 sitemap.xml（幂等）。"""
import re
import xml.etree.ElementTree as ET

SLUGS = ["printed-fabric-label-guide", "stock-vs-custom-garment-labels"]
LANGS = ["", "en/", "fr/", "es/", "ja/", "ko/"]
DATE = "2026-11-17"

p = "sitemap.xml"
s = open(p, encoding="utf-8").read()
existing = set(re.findall(r"<loc>(.*?)</loc>", s))

added = []
blocks = []
for slug in SLUGS:
    for lang in LANGS:
        url = "https://taigetag.com/%sblog/%s.html" % (lang, slug)
        if url in existing:
            print("已存在，跳过:", url)
            continue
        blocks.append(
            "  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n"
            "    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>\n" % (url, DATE))
        added.append(url)

assert blocks, "没有新增 URL"
s = s.replace("</urlset>", "".join(blocks) + "</urlset>")
open(p, "w", encoding="utf-8", newline="").write(s)

# 校验 XML 合法 + 无重复
tree = ET.parse(p)
locs = [e.text for e in tree.getroot().iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
print("新增 URL 数:", len(added))
for u in added:
    print("  +", u)
print("sitemap URL 总数:", len(locs))
dups = [u for u in set(locs) if locs.count(u) > 1]
print("重复 URL:", dups if dups else "0")
assert not dups
