#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""晚間批次：本批与上一批文章中文正文长度对照（同一口径）。"""
import re, os

FILES = ["blog/_body_saltspray.html", "blog/_body_functional.html",
         "blog/sequin-rhinestone-trims-guide.html", "blog/rib-knit-collar-cuff-guide.html",
         "blog/garment-security-tag-guide.html", "blog/garment-wash-dye-trims-guide.html"]


def count(main):
    zh_attrs = re.findall(r'data-zh="([^"]*)"', main)
    text = re.sub(r'<[^>]+>', '', re.sub(r'data-[a-z]+="[^"]*"', '', main))
    return (len(re.findall(r'[\u4e00-\u9fff]', ' '.join(zh_attrs)))
            + len(re.findall(r'[\u4e00-\u9fff]', text)))


for f in FILES:
    if not os.path.exists(f):
        print("MISS", f); continue
    s = open(f, encoding="utf-8").read()
    seg = re.search(r'<section class="article-body">.*?</section>', s, re.S)
    main = seg.group(0) if seg else s
    cut = max(main.find('相關文章'), main.find('相关文章'))
    if cut != -1:
        main = main[:cut]
    print("%-50s 汉字=%d" % (os.path.basename(f), count(main)))
