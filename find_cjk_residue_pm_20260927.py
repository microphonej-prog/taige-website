#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""定位 ko/en/fr/es 生成页正文里残留的 CJK 字符（正文段落内，排除 script/style）。"""
import re, sys

for p in sys.argv[1:]:
    s = open(p, encoding="utf-8").read()
    m = re.search(r'<section class="article-body">', s)
    body = s[m.end():]
    body = body[:body.index("</section>")] if "</section>" in body else body
    clean = re.sub(r"<script.*?</script>|<style.*?</style>", "", body, flags=re.S)
    clean = re.sub(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"', "", clean)
    for mm in re.finditer(r"[^\s<>]{0,25}[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]+[^\s<>]{0,25}", clean):
        print("%-56s ...%s..." % (p, mm.group(0)))
