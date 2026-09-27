#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""desc 长度 / 正文字数体检（生成前）。"""
import sys, re, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.getcwd())
from daily_meta_20260927_evening import ARTICLES

for a in ARTICLES:
    print("%s" % a["slug"])
    for k in ("desc_zh", "desc_en", "desc_ja", "desc_ko", "desc_fr", "desc_es"):
        v = a[k]
        flag = ""
        if k == "desc_zh" and not (80 <= len(v) <= 125):
            flag = "  <= 目标 80-120 字"
        if k == "desc_en" and not (148 <= len(v) <= 160):
            flag = "  <= 目标 150-160 字符"
        print("   %-8s %3d%s" % (k, len(v), flag))
    body = open(a["body"], encoding="utf-8").read()
    i = body.index('<section class="article-body">')
    seg = re.sub(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"', "", body[i:])
    text = re.sub(r"<[^>]+>", "", seg)
    han = len(re.findall(r"[\u4e00-\u9fff]", text))
    print("   正文汉字 %d 字；元素数 %d；h2 %d 个；表格 %d 个；内链 %d 个"
          % (han, len(re.findall(r'data-zh="', body)),
             len(re.findall(r"<h2 ", body)), len(re.findall(r"<table>", body)),
             len(re.findall(r'<a href="', body))))
