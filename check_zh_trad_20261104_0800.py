#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""zh 页繁体化确认：用 HTMLParser 取纯文本节点，s2t 后应完全一致。"""
from html.parser import HTMLParser
from opencc import OpenCC
import sys

S2T = OpenCC("s2t")
SLUGS = ["apparel-trims-nearshoring-sourcing-guide.html",
         "apparel-unboxing-packaging-design-guide.html"]


class T(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.buf = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1

    def handle_data(self, d):
        if not self.skip:
            self.buf.append(d)


for slug in SLUGS:
    p = "blog/" + slug
    t = T(); t.feed(open(p, encoding="utf-8").read())
    txt = "".join(t.buf)
    conv = S2T.convert(txt)
    diffs = [(a, c) for a, c in zip(txt, conv) if a != c]
    # 只统计汉字差异
    han = [(a, c) for a, c in diffs if "\u4e00" <= a <= "\u9fff"]
    print("%-46s 纯文本=%d 字, s2t 改动=%d, 其中汉字=%d %s"
          % (slug, len(txt), len(diffs), len(han), han[:8]))
