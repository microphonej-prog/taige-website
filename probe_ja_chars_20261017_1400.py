# -*- coding: utf-8 -*-
"""列出 ja 属性里所有被 s2t 改写的字符去重清单，人工判断是否为合法日文汉字"""
import re, sys, os
from html.parser import HTMLParser
from opencc import OpenCC

s2t = OpenCC("s2t")


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.vals = []

    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if k.lower() in ("data-ja", "data-ko"):
                self.vals.append((k.lower(), v or ""))


for f in ["blog/_body_saree.html", "blog/_body_tradeshow.html"]:
    s = open(f, encoding="utf-8").read()
    p = P(); p.feed(s)
    chars = {}
    for lang, v in p.vals:
        if lang != "data-ja":
            continue
        for ch in v:
            if "\u4e00" <= ch <= "\u9fff" and s2t.convert(ch) != ch:
                chars.setdefault(ch, 0)
                chars[ch] += 1
    print(f, "ja 去重被改写字符 %d 个:" % len(chars))
    print("  ", " ".join("%s(%d)" % (c, n) for c, n in sorted(chars.items(), key=lambda x: -x[1])))
