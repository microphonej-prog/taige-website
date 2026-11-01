#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 2026-10-31 批次遗留坏链 href="blog/index.html"（六语共 12 个文件），并检查新文章内链是否存在"""
import os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

SLUGS_OLD = ["medical-ppe-garment-labeling-guide.html", "trademark-symbols-garment-labels.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
fixed = []
for slug in SLUGS_OLD:
    for p in ["blog/%s" % slug] + ["%s/blog/%s" % (l, slug) for l in LANGS]:
        s = open(p, encoding="utf-8").read()
        n = s.count('href="blog/index.html"')
        if n:
            s = s.replace('href="blog/index.html"', 'href="index.html"')
            open(p, "w", encoding="utf-8", newline="").write(s)
            fixed.append("%s(%d)" % (p, n))
print("坏链修复: %d 个文件 %s" % (len(fixed), fixed))

# 全站剩余坏链扫描（blog 目录内的相对链接）
left = []
for p in glob.glob("blog/*.html") + glob.glob("*/blog/*.html"):
    s = open(p, encoding="utf-8").read()
    if 'href="blog/index.html"' in s:
        left.append(p)
print("全站剩余 href=\"blog/index.html\":", left if left else "无")

# 新文章内链存在性
for slug in ["ecommerce-mailer-box-guide.html", "packaging-tape-guide.html"]:
    for base, p in [("blog", "blog/%s" % slug)] + [("%s/blog" % l, "%s/blog/%s" % (l, slug)) for l in LANGS]:
        s = open(p, encoding="utf-8").read()
        hrefs = re.findall(r'href="([^"#?:]+\.html)"', s)
        bad = [h for h in hrefs if h.startswith(("http", "//")) is False and not os.path.exists(os.path.join(base, h))]
        print("%-46s 内链 %d 个，坏链 %s" % (p, len(hrefs), bad if bad else "无"))
