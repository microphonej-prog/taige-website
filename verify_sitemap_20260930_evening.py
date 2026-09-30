#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""提交前最后一关：sitemap.xml 可解析 + 新文章 URL 排序与文件一致 + 六语文件存在性。"""
import os, re
import xml.etree.ElementTree as ET

tree = ET.parse("sitemap.xml")
locs = [e.text for e in tree.getroot().iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
print("sitemap 可解析，<loc> 总数 %d" % len(locs))
assert len(locs) == len(set(locs)), "sitemap 有重复 URL"
print("URL 无重复")

NEW = ["garment-bag-header-card-guide.html", "poly-bag-suffocation-warning-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
for slug in NEW:
    for pre, path in [("", "blog/%s" % slug)] + [("%s/" % l, "%s/blog/%s" % (l, slug)) for l in LANGS]:
        u = "https://taigetag.com/%sblog/%s" % (pre, slug)
        assert u in locs, u
        assert os.path.exists(path), path
    print("  %s：6 语 URL 与文件齐备" % slug)
print("OK")
