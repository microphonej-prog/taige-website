#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""列出属性值中 </strong> 之后疑似残留的重复小标题/冒号残渣，供人工复核。
用法: <python> list_residue_20260928_pm.py
"""
import re, sys

sys.stdout.reconfigure(encoding="utf-8")
FILES = ["blog/_body_origin.html", "blog/_body_pp.html"]
for f in FILES:
    s = open(f, encoding="utf-8").read()
    print("=== %s ===" % f)
    for m in re.finditer(r'data-(zh|en|ja|ko|fr|es)="([^"]*)"', s):
        lang, val = m.group(1), m.group(2)
        mm = re.match(r"<strong>(.*?)</strong>(.*)$", val, re.S)
        if not mm:
            continue
        rest = mm.group(2)
        if re.match(r"^[\s:：·・\-]", rest) or re.match(r"^[^\s]{1,12}[:：]", rest):
            print("  [%s] 小标题=%s | 其后=%s" % (lang, mm.group(1)[:30], rest[:60]))
