#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""20:00 批次：统计两篇中文版正文汉字数 + 属性元素数"""
import os, re

os.chdir(os.path.dirname(os.path.abspath(__file__)))
CJK = re.compile(r"[\u4e00-\u9fff]")
for slug in ["compostable-packaging-certification-guide.html", "trim-scrap-destruction-certificate-guide.html"]:
    s = open("blog/%s" % slug, encoding="utf-8").read()
    body = re.search(r'<section class="article-body">(.*?)</section>', s, re.S).group(1)
    text = re.sub(r"<[^>]+>", " ", body)
    print("%-52s 汉字=%d 可见字符=%d" % (slug, len(CJK.findall(text)), len(re.sub(r"\s+", " ", text).strip())))
