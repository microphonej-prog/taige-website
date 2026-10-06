#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-06 下午批次：严格简体字表扫描（ja/ko 生成页与根页），排除日文常用汉字干扰。"""
import re

SIMP = "这们为准发后词汇语标贴纸织钢银费说过选购实际台账丝线级别页面录种类响"
FILES = ["ja/blog/sequin-rhinestone-trims-guide.html", "ja/blog/rib-knit-collar-cuff-guide.html",
         "ko/blog/sequin-rhinestone-trims-guide.html", "ko/blog/rib-knit-collar-cuff-guide.html"]

bad = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    body = re.search(r'<section class="article-body">.*?</section>', s, re.S).group(0)
    txt = re.sub(r'<[^>]+>', '', body)
    hits = re.findall(r'.{8}[%s].{8}' % SIMP, txt)
    print("%-48s 简体嫌疑 %d 处" % (f, len(hits)))
    for h in hits[:6]:
        print("    ...%s..." % h)
    bad += len(hits)

print("\n结论: %s" % ("有 %d 处疑似简体" % bad if bad else "无简体残留（严格表）"))
