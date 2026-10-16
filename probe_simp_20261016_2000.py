#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""深度检查：ja/ko 属性值中的“简体字形”误用（用 OpenCC s2t 判断：s2t(c)!=c 说明是简体形）"""
import os, opencc, re
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
s2t = opencc.OpenCC("s2t")


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.hits = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for l in ("ja", "ko"):
            v = a.get("data-%s" % l)
            if not v:
                continue
            for ch in set(v):
                if "\u4e00" <= ch <= "\u9fff" and s2t.convert(ch) != ch:
                    self.hits.append((l, ch, s2t.convert(ch), v[:70]))


p = P()
for f in ["blog/_body_transins.html", "blog/_body_minerals.html"]:
    t = open(f, encoding="utf-8").read()
    p.feed(t)
print("疑似简体误用:", len(p.hits))
for h in p.hits:
    print("  ", h)
