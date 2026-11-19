# -*- coding: utf-8 -*-
"""为 2026-11-19 14:00 两篇新文章写入 sitemap（zh + en/fr/es/ja/ko），并刷新博客首页 lastmod。"""
import re
import xml.etree.ElementTree as ET

DATE = "2026-11-19"
SLUGS = ["kraft-hang-tags-guide.html", "natural-fiber-care-label-guide.html"]
LANGS = ["blog/", "en/blog/", "fr/blog/", "es/blog/", "ja/blog/", "ko/blog/"]

path = "sitemap.xml"
with open(path, encoding="utf-8", newline="") as f:
    s = f.read()
before_lines = s.count("\n")

# 1) 博客首页 lastmod
for loc in ["https://taigetag.com/%sindex.html" % p for p in LANGS]:
    pat = re.compile(r"(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)" % re.escape(loc))
    s, n = pat.subn(lambda m: m.group(1) + DATE + m.group(2), s, count=1)
    print("lastmod %-52s %d" % (loc.replace("https://taigetag.com", ""), n))

# 2) 文章 URL
assert "</urlset>" in s
blocks = []
for slug in SLUGS:
    for p in LANGS:
        loc = "https://taigetag.com/%s%s" % (p, slug)
        pat = re.compile(
            r"(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>\r?\n\s*<changefreq>)[^<]*(</changefreq>\r?\n\s*<priority>)[^<]*(</priority>)"
            % re.escape(loc))
        s, n = pat.subn(lambda m: m.group(1) + DATE + m.group(2) + "monthly" + m.group(3) + "0.7" + m.group(4), s, count=1)
        if n:
            print("更新已有 %s" % loc.replace("https://taigetag.com", ""))
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
tree = ET.parse(path)
locs = [e.text for e in tree.getroot().iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
dups = [l for l in set(locs) if locs.count(l) > 1]
print("XML 合法，URL 总数 %d，新增 URL %d，行数 +%d，重复 URL %d" % (
    len(locs), len(blocks), s.count("\n") - before_lines, len(dups)))
for l in dups[:10]:
    print("  重复:", l)
for slug in SLUGS:
    hit = [l for l in locs if slug in l]
    print("  %s -> sitemap %d 条" % (slug, len(hit)))
