#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成前体检：① desc 长度 ② 正文属性完整性（html.parser 逐属性判断）③ 属性值里的裸双引号/引号失衡"""
import re, sys, os
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
sys.path.insert(0, ROOT)

from daily_meta_20261008_am import ARTICLES

print("=== ① desc 长度 ===")
for a in ARTICLES:
    print("%-42s zh=%d en=%d ja=%d ko=%d fr=%d es=%d"
          % (a["slug"], len(a["desc_zh"]), len(a["desc_en"]), len(a["desc_ja"]),
             len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))

WANT = ("data-zh", "data-en", "data-fr", "data-es", "data-ja", "data-ko")


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.missing = []
        self.zh_elems = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "data-zh" in d:
            self.zh_elems += 1
            miss = [k for k in WANT if k not in d]
            if miss:
                self.missing.append((tag, d.get("data-zh", "")[:40], miss))

    handle_startendtag = handle_starttag


print("\n=== ②/③ 正文属性体检 ===")
for a in ARTICLES:
    raw = open(a["body"], encoding="utf-8").read()
    c = Checker()
    c.feed(raw)
    # 裸双引号：属性值里出现 "" 或 =" 紧跟引号等畸形
    bad_q = re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', raw)
    dq = re.findall(r'="{2,}', raw)
    print("%-42s 带 data-zh 元素=%d 缺属性=%d 空值=%d 畸形引号=%d"
          % (a["slug"], c.zh_elems, len(c.missing), len(bad_q), len(dq)))
    for m in c.missing[:10]:
        print("    MISS", m)
    if bad_q:
        print("    空 data 值:", bad_q[:5])
    if dq:
        print("    畸形引号:", dq[:5])
    print("    字符数=%d 字节=%d" % (len(raw), len(raw.encode("utf-8"))))
