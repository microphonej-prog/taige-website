#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统计新文章正文中文与英文篇幅（data-zh 文本字数 / data-en 词数）。"""
import re, sys
sys.stdout.reconfigure(encoding="utf-8")
for slug in ["trim-digital-sampling-3d.html", "trim-coding-standardization.html"]:
    s = open("blog/" + slug, encoding="utf-8").read()
    body = re.search(r'<section class="article-body">.*?</section>', s, re.S).group(0)
    zh = "".join(re.findall(r'data-zh="([^"]*)"', body))
    zh = re.sub(r"<[^>]*>", "", zh)
    n_zh = len(re.findall(r"[\u4e00-\u9fff]", zh))
    en = " ".join(re.findall(r'data-en="([^"]*)"', body))
    n_en = len(re.findall(r"[A-Za-z][A-Za-z'-]*", en))
    h2 = len(re.findall(r"<h2 ", body))
    tbl = len(re.findall(r"<table>", body))
    print("%-40s 正文汉字 %d 字 / 英文 %d 词 / h2 %d 节 / 表格 %d 个"
          % (slug, n_zh, n_en, h2 - 1, tbl))
