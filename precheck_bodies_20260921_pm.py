#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""正文中转文件预检：六语属性完整性、引号畸形、裸 & 等。"""
import re, sys, os
from html.parser import HTMLParser

BODIES = ["blog/_body_hang_tag_metal_hardware.html",
          "blog/_body_garment_trims_needle_detection.html"]
LANGS = ("data-en", "data-ja", "data-ko", "data-fr", "data-es")
KEY = {"data-en", "data-ja", "data-ko", "data-fr", "data-es", "data-zh"}
fails = 0

class C(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, {k.lower(): (v or "") for k, v in attrs}))

for f in BODIES:
    s = open(f, encoding="utf-8").read()
    p = C(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    miss = [(t, k) for t, a in dzh for k in LANGS if not a.get(k, "").strip()]
    stray = [(t, sorted(set(a) & KEY)) for t, a in p.tags
             if (set(a) & KEY) and "data-zh" not in a]
    q1 = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s))
    q2 = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[a-zA-Z]', s))
    am = len(re.findall(r'&(?!amp;|nbsp;|quot;|#|<)', s))
    dq = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[^>\s/][^>]*?="', s))
    zh = len(re.findall(r'[\u4e00-\u9fff]', re.sub(r'data-(?:zh)="[^"]*"', '', s)))
    # 默认文本（标签之间的中文）应有内容，抽样统计默认文本兜底为简体的元素数
    print("%s\n  tags=%d data-zh=%d 缺语种=%d %s\n  空值=%d 值后裸字符=%d 裸&=%d 标签外汉字=%d"
          % (f, len(p.tags), len(dzh), len(miss), miss[:6], q1, q2, am, zh))
    if stray:
        print("  非 data-zh 却带语种属性的标签:", stray[:6])
        fails += 1
    fails += 1 if (miss or q1 or q2 or am) else 0
    for t, a in dzh:
        for k in LANGS:
            v = a.get(k, "")
            if 'href' in a and t == "a":
                pass
    print("  <a> 数量=%d  <table>/<tr> 数量=%d/%d"
          % (sum(1 for t, a in p.tags if t == "a"),
             sum(1 for t, a in p.tags if t == "table"),
             sum(1 for t, a in p.tags if t == "tr")))
print("失败项=%d" % fails)
sys.exit(1 if fails else 0)
