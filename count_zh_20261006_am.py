#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统计 2026-10-06 上午批次两篇文章中文正文字数（data-zh 属性值 + 文本节点）。"""
import re, os

for f in ["blog/garment-security-tag-guide.html", "blog/garment-wash-dye-trims-guide.html"]:
    s = open(f, encoding="utf-8").read()
    body = re.search(r'<section class="article-body">.*?</section>', s, re.S).group(0)
    cut = body.find('相關文章')
    if cut == -1:
        cut = body.find('相关文章')
    main = body[:cut]
    zh_attrs = re.findall(r'data-zh="([^"]*)"', main)
    text = re.sub(r'<[^>]+>', '', re.sub(r'data-[a-z]+="[^"]*"', '', main))
    n_attr = len(re.findall(r'[\u4e00-\u9fff]', ' '.join(zh_attrs)))
    n_text = len(re.findall(r'[\u4e00-\u9fff]', text))
    h2 = len(re.findall(r'<h2 ', main))
    print("%s  正文汉字(不含相关文章) = %d (属性 %d + 文本 %d) ; h2 = %d ; 表格 = %d"
          % (os.path.basename(f), n_attr + n_text, n_attr, n_text, h2, main.count('<table>')))
