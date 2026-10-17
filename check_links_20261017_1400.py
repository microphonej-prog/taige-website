# -*- coding: utf-8 -*-
"""新文章内部链接有效性检查：提取 blog/ 两篇新页里的相对 href，确认目标文件存在"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
FILES = ["blog/saree-ethnic-wear-trims-guide.html", "blog/garment-trims-trade-show-sourcing-guide.html"]
bad = []
for f in FILES:
    s = open(f, encoding="utf-8").read()
    hrefs = set(re.findall(r'href="([^"#:]+)"', s))
    for h in sorted(hrefs):
        if h.startswith(("..", "index.html")) or not h.endswith(".html"):
            continue
        tgt = os.path.join(os.path.dirname(f), h)
        if not os.path.exists(tgt):
            bad.append((f, h))
    print("%s 内部链接 %d 个" % (f, len([h for h in hrefs if h.endswith(".html")])))
print("失效链接 %d %s" % (len(bad), bad))
raise SystemExit(1 if bad else 0)
