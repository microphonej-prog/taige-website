#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测量最近 8 篇文章的中文 desc 长度 + 新文章 desc_zh 明细。"""
import re, glob, os

NEW = ["blog/eu-deforestation-regulation-packaging.html",
       "blog/eu-packaging-epr-triman-guide.html"]

files = sorted(glob.glob("blog/*.html"), key=lambda p: os.path.getmtime(p), reverse=True)
print("== 最近 10 个文件（按 mtime）的 data-zh desc 长度 ==")
n = 0
for f in files:
    if f.endswith("index.html") or f.startswith("blog/_"):
        continue
    s = open(f, encoding="utf-8").read()
    m = re.search(r'<meta name="description"[^>]*?data-zh="([^"]*)"', s, re.S)
    if not m:
        continue
    print("  %-52s %d 字" % (os.path.basename(f), len(m.group(1))))
    n += 1
    if n >= 10:
        break

hs = [f for f in files if f.startswith("blog/_body_")]
print("\n== 正文汉字数（data-* 剥离后） ==")
for f in ["blog/eu-deforestation-regulation-packaging.html",
          "blog/eu-packaging-epr-triman-guide.html"]:
    s = open(f, encoding="utf-8").read()
    i = s.index('<section class="article-body">')
    body = s[i:s.index("</section>", i)]
    body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
    body = re.sub(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"', "", body)
    text = re.sub(r"<[^>]+>", "", body)
    print("  %-52s 汉字 %d" % (os.path.basename(f), len(re.findall(r"[\u4e00-\u9fff]", text))))
