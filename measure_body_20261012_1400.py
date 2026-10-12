#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统计正文 data-zh 字符量 + 定位繁体字残留（2026-10-12 下午批次）"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

for f in ["blog/_body_tee.html", "blog/_body_trousers.html",
          "blog/_body_folding.html", "blog/_body_retail.html"]:
    s = open(f, encoding="utf-8").read()
    zh = re.sub(r'<[^>]+>', '', "".join(re.findall(r'data-zh="([^"]*)"', s)))
    zh_body = re.sub(r'\s+', '', zh)
    print("%-28s data-zh 字符: %d" % (f, len(zh_body)))

print("--- 繁体字残留定位 ---")
for f in ["blog/_body_tee.html", "blog/_body_trousers.html"]:
    s = open(f, encoding="utf-8").read()
    for m in re.finditer(r'[輔標繁]', s):
        ctx = s[max(0, m.start() - 45):m.start() + 25].replace("\n", " ")
        print("%s | %s | ...%s..." % (f, m.group(0), ctx))
