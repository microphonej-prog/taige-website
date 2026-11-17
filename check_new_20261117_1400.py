# -*- coding: utf-8 -*-
"""校验新文章：每个带 data-* 的元素是否 6 语齐全；列表页卡片是否到位。"""
import re
from html.parser import HTMLParser

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
FILES = [
    "blog/printed-fabric-label-guide.html",
    "blog/stock-vs-custom-garment-labels.html",
]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.missing = []
        self.total = 0

    def handle_starttag(self, tag, attrs):
        names = [a for a, _ in attrs]
        present = [l for l in LANGS if "data-%s" % l in names]
        if not present:
            return
        self.total += 1
        if len(present) != len(LANGS):
            self.missing.append((tag, sorted(set(LANGS) - set(present))))


for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = P()
    p.feed(s)
    print("%s  带 data-* 元素 %d 个，缺语种元素 %d 个" % (f, p.total, len(p.missing)))
    for m in p.missing[:5]:
        print("   缺:", m)
    # de/pt 必须不出现
    print("   data-de=%d data-pt=%d" % (s.count('data-de="'), s.count('data-pt="')))
    print("   title:", re.search(r"<title[^>]*>([^<]*)</title>", s).group(1))

idx = open("blog/index.html", encoding="utf-8").read()
for slug in ["printed-fabric-label-guide", "stock-vs-custom-garment-labels"]:
    print("卡片 %s: %s" % (slug, idx.count('href="%s.html"' % slug)))
