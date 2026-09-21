#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抽查 ja/ko 正文确实为本语言（有假名/韩文，不是中文兜底）。"""
import re
files = ["ja/blog/hanger-bag-guide.html", "ko/blog/hanger-bag-guide.html",
         "ja/blog/shrink-film-packaging-guide.html", "ko/blog/shrink-film-packaging-guide.html"]
for p in files:
    s = open(p, encoding="utf-8").read()
    m0 = re.search(r'<section class="article-body">', s)
    m1 = re.search(r'</section>', s[m0.end():])
    b = s[m0.end():m0.end() + m1.start()]
    kana = len(re.findall(r'[\u3040-\u30ff]', b))
    hangul = len(re.findall(r'[\uac00-\ud7af]', b))
    han = len(re.findall(r'[\u4e00-\u9fff]', b))
    print("%-45s kana=%d hangul=%d 汉字=%d" % (p, kana, hangul, han))
