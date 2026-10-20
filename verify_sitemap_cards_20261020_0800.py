#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-20 08:00 批次：sitemap 与文件一致性 + 列表页卡片 + blog index lastmod"""
import os, re, sys

sys.path.insert(0, ".")
from daily_meta_20261020_0800 import ARTICLES

LANGS = ["en", "ja", "ko", "fr", "es"]
sitemap = open("sitemap.xml", encoding="utf-8").read()
locs = re.findall(r"<loc>([^<]+)</loc>", sitemap)
print("sitemap <loc> 总数 =", len(locs))

fails = []
for a in ARTICLES:
    slug = a["slug"]
    for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS]:
        u = "https://taigetag.com/%s%s" % (pre, slug)
        if u not in locs:
            fails.append("sitemap 缺 " + u)
        if not os.path.exists("%s%s" % (pre, slug)):
            fails.append("文件缺 %s%s" % (pre, slug))
    blk = re.search(r"<loc>https://taigetag\.com/blog/%s</loc>\s*<lastmod>([^<]+)</lastmod>" % re.escape(slug), sitemap)
    print("  %-46s lastmod=%s" % (slug, blk.group(1) if blk else "NONE"))
    if not blk or blk.group(1) != "2026-10-20":
        fails.append("lastmod 错 " + slug)

for l in [""] + ["%s/" % x for x in LANGS]:
    u = "https://taigetag.com/%sblog/index.html" % l
    m = re.search(r"<loc>%s</loc>\s*<lastmod>([^<]+)</lastmod>" % re.escape(u), sitemap)
    print("  blog/index lastmod %-8s %s" % (l or "root", m.group(1) if m else "NONE"))
    if not m or m.group(1) != "2026-10-20":
        fails.append("blog index lastmod " + u)

for idx in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(idx, encoding="utf-8").read()
    card = re.search(r"<article class=\"post-card\">.*?</article>", s, re.S).group(0)
    for a in ARTICLES:
        n = s.count('href="%s"' % a["slug"])
        tag_ok = s.count(a["tag_zh"]) > 0 or s.count(a["tag_en"]) > 0
        print("  %-22s %-46s href=%d tag=%s 首卡四语属性=%d"
              % (idx, a["slug"][:44], n, tag_ok, len(re.findall(r"data-(?:zh|en|ja|ko|fr|es)=", card))))
        if n < 1 or not tag_ok:
            fails.append("%s 卡片异常 %s" % (idx, a["slug"]))

print("\n结论: 问题 %d" % len(fails))
for f in fails:
    print("  !!", f)
sys.exit(1 if fails else 0)
