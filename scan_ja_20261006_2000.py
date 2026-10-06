#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-06 晚间批次：ja/ko 语言残留扫描（全角逗号、汉字残留）。"""
import re

for f in ["blog/_body_saltspray.html", "blog/_body_functional.html"]:
    s = open(f, encoding="utf-8").read()
    vals = re.findall(r'data-ja="([^"]*)"', s)
    hits = [v[:70] for v in vals if '\uff0c' in v or '\uff1b' in v or '\u3000' in v]
    print(f, "ja 含全角逗号/分号/全角空格:", len(hits))
    for h in hits[:8]:
        print("   ", h)
    ko = re.findall(r'data-ko="([^"]*)"', s)
    kh = [v[:60] for v in ko if re.search(r'[\u4e00-\u9fff]', v)]
    print(f, "ko 含汉字:", len(kh), kh[:3])
# 整站对照：最近一次上线文章的 ja 值是否也含 、
ref = open("blog/sequin-rhinestone-trims-guide.html", encoding="utf-8").read()
rv = re.findall(r'data-ja="([^"]*)"', ref)
print("参考线上文章 ja 值:", len(rv), "含、:", sum(1 for v in rv if '\u3001' in v),
      "含全角逗号:", sum(1 for v in rv if '\uff0c' in v), "含全角括号:", sum(1 for v in rv if '\uff08' in v))
