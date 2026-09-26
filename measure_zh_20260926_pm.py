#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统计两篇新文章中文正文字数（article-body 内汉字数，用于质量核对）。"""
import re

for f in ["blog/trim-third-party-testing-guide.html", "blog/sample-room-trims-checklist.html",
          "blog/trim-ironing-heat-resistance-guide.html", "blog/knitwear-sweater-trims-guide.html",
          "blog/garment-trims-certifications.html"]:
    s = open(f, encoding="utf-8").read()
    i = s.index('<section class="article-body">')
    body = s[i:s.index("</section>", i)]
    # 只统计可见默认文本（去掉 <script>、标签、属性值）
    body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
    body = re.sub(r"data-(?:zh|en|ja|ko|fr|es)=\"[^\"]*\"", "", body)
    text = re.sub(r"<[^>]+>", "", body)
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
    print("%-46s 正文汉字 %d" % (f, cjk))
