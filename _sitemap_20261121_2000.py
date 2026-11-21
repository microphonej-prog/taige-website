# -*- coding: utf-8 -*-
"""把 2026-11-21 20:00 两篇新文章（各六语）写入 sitemap，并刷新 blog 首页 lastmod。"""
import re

DATE = "2026-11-21"
SLUGS = ["hook-and-eye-tape-guide.html", "pocketing-fabric-guide.html"]
PRE = ["blog/", "en/blog/", "fr/blog/", "es/blog/", "ja/blog/", "ko/blog/"]

path = "sitemap.xml"
s = open(path, encoding="utf-8", newline="").read()
assert "xhtml:link" not in s

for lang in ["", "en/", "fr/", "es/", "ja/", "ko/"]:
    loc = "https://taigetag.com/%sblog/index.html" % lang
    pat = re.compile(r"(<loc>%s</loc>\n\s*<lastmod>)[^<]*(</lastmod>)" % re.escape(loc))
    s, n = pat.subn(r"\g<1>%s\g<2>" % DATE, s, count=1)
    print("blog index lastmod %-55s %d" % (loc, n))

added, updated = 0, 0
blocks = []
for slug in SLUGS:
    for pre in PRE:
        loc = "https://taigetag.com/%s%s" % (pre, slug)
        pat = re.compile(
            r"(<loc>%s</loc>\n\s*<lastmod>)[^<]*(</lastmod>\n\s*<changefreq>)[^<]*(</changefreq>\n\s*<priority>)[^<]*(</priority>)"
            % re.escape(loc))
        s, n = pat.subn(r"\g<1>%s\g<2>monthly\g<3>0.7\g<4>" % DATE, s, count=1)
        if n:
            updated += 1
        else:
            blocks.append("  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n"
                          "    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>" % (loc, DATE))
            added += 1

s = s.replace("</urlset>", "\n".join(blocks) + "\n</urlset>", 1)
open(path, "w", encoding="utf-8", newline="").write(s)
print("sitemap: added %d, updated %d, total <url> %d" % (added, updated, s.count("<url>")))

import xml.etree.ElementTree as ET
t = ET.parse(path)
locs = [e.text for e in t.getroot().iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
print("XML 合法，loc 数 %d，重复 %d" % (len(locs), len(locs) - len(set(locs))))
for slug in SLUGS:
    print(slug, [u for u in locs if slug in u])
