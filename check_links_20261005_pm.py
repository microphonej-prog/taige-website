#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查 2 篇新文章（六语版本）内部链接与资源引用是否都能在仓库中找到。"""
import os, re

SLUGS = ["sewing-thread-selection-guide.html", "flame-retardant-trims-guide.html"]
PAGES = ["blog/%s" % s for s in SLUGS] + ["%s/blog/%s" % (l, s) for l in ("en", "ja", "ko", "fr", "es") for s in SLUGS]

missing = []
for p in PAGES:
    base = os.path.dirname(p)
    s = open(p, encoding="utf-8").read()
    for attr in ("href", "src"):
        for m in re.finditer(r'%s="([^"]+)"' % attr, s):
            u = m.group(1)
            if u.startswith(("http", "#", "mailto:", "javascript:", "data:", "tel:")):
                continue
            u = u.split("?")[0].split("#")[0]
            target = os.path.normpath(os.path.join(base, u))
            if not os.path.exists(target):
                missing.append("%s -> %s" % (p, u))
print("检查页面数 %d，缺失引用 %d" % (len(PAGES), len(missing)))
for x in missing:
    print("  ✗", x)
