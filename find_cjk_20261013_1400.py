# -*- coding: utf-8 -*-
"""定位语言页残留的 CJK / 简体字符，并对比既有文章确认是否为站点通用元素"""
import re

TARGETS = ["en/blog/garment-embroidery-decoration-guide.html",
           "fr/blog/garment-embroidery-decoration-guide.html",
           "es/blog/garment-embroidery-decoration-guide.html",
           "ko/blog/garment-embroidery-decoration-guide.html",
           "ja/blog/garment-embroidery-decoration-guide.html",
           "en/blog/animal-derived-material-certification-guide.html",
           "ja/blog/animal-derived-material-certification-guide.html",
           "en/blog/knitwear-sweater-trims-guide.html",          # 既有文章，作为基线
           "ja/blog/knitwear-sweater-trims-guide.html"]

SIMP = "这个们为说时后现关应发进对开还没经过样点种类的录书标签纸张"

for f in TARGETS:
    s = open(f, encoding="utf-8").read()
    body = s[s.index("<body"):]
    txt = re.sub(r'<[^>]+>', ' ', body)
    cjk = re.findall(r'[\u4e00-\u9fff]', txt)
    simp = [c for c in txt if c in SIMP]
    print("-" * 70)
    print(f)
    print("  CJK 数:", len(cjk), "".join(cjk[:40]))
    print("  简体字:", len(simp), "".join(simp))
    # 定位上下文
    for m in re.finditer(r'[\u4e00-\u9fff]{1,}', txt):
        print("     ctx:", repr(txt[max(0, m.start() - 20):m.end() + 20]))
