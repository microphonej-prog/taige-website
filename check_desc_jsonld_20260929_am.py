#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验中文根目录页 description/title 静态可读（爬虫不执行 JS），以及 JSON-LD 合法性。"""
import re, json, sys
sys.stdout.reconfigure(encoding="utf-8")
SLUGS = ["trim-digital-sampling-3d.html", "trim-coding-standardization.html"]
bad = 0
for slug in SLUGS:
    p = "blog/" + slug
    s = open(p, encoding="utf-8").read()
    m = re.search(r'<meta name="description"(.*?)>', s, re.S)
    attrs = m.group(1) if m else ""
    c = re.search(r'content="([^"]*)"', attrs)
    ok_c = bool(c and len(c.group(1)) >= 80 and "data-zh" in attrs and "data-en" in attrs)
    t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S)
    tv = t.group(1).strip() if t else ""
    print("%-40s description content=%d 字 | title=%d 字 | %s"
          % (slug, len(c.group(1)) if c else -1, len(tv), "OK" if ok_c else "XX"))
    if not ok_c:
        bad += 1
    # JSON-LD 合法性 + 单条
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    print("   JSON-LD 块数 = %d" % len(lds))
    for i, blk in enumerate(lds):
        try:
            d = json.loads(blk)
        except Exception as e:
            print("   XX JSON-LD #%d 解析失败：%s" % (i, e))
            bad += 1
            continue
        types = [n.get("@type") for n in d.get("@graph", [d])]
        print("   JSON-LD #%d @type = %s" % (i, types))
        if "Article" not in types:
            print("   XX 缺 Article")
            bad += 1
    # canonical 与 sitemap 一致
    can = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
    print("   canonical = %s %s" % (can, "OK" if can == "https://taigetag.com/blog/" + slug else "XX"))
    if can != "https://taigetag.com/blog/" + slug:
        bad += 1
print()
print("问题数: %d" % bad)
sys.exit(1 if bad else 0)
