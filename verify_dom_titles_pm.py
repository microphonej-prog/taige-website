#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从无头 Chrome dump 出的 DOM 中提取 title 与 h1，验证线上渲染语言正确。"""
import re, glob, os

os.chdir(os.path.join(os.environ["LOCALAPPDATA"], "Temp"))
for f in sorted(glob.glob("dom_*.html")):
    s = open(f, encoding="utf-8", errors="replace").read()
    t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    body = s[s.find('class="article-body"'):]
    cjk = len(re.findall(r"[\u4e00-\u9fff]", body))
    print("== %s" % f)
    print("   title: %s" % (t.group(1).strip() if t else "-"))
    print("   h1   : %s" % (re.sub(r"\s+", " ", h1.group(1)).strip()[:90] if h1 else "-"))
    print("   正文汉字数(渲染后 DOM): %d" % cjk)
