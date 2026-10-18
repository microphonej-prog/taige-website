#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统计文章正文汉字数，做长度对照。"""
import re, sys

for p in sys.argv[1:]:
    s = open(p, encoding="utf-8").read()
    b = re.search(r'<section class="article-body">(.*?)</section>', s, re.S).group(1)
    t = re.sub(r"<[^>]+>", " ", b)
    t = re.sub(r"\s+", " ", t)
    print("%-52s 汉字 %d  可见字符 %d" % (p, len(re.findall(r"[\u4e00-\u9fff]", t)), len(t)))
