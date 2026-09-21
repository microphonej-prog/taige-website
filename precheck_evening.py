#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验正文文件：六语属性完整性（HTMLParser）+ 引号畸形 + 裸双引号检测。"""
import re, sys
from html.parser import HTMLParser


class C(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.inb = False
        self.tags = []

    def handle_starttag(self, t, a):
        d = {k.lower(): (v or "") for k, v in a}
        if t == "section" and d.get("class", "").startswith("article-body"):
            self.inb = True
            return
        if self.inb:
            self.tags.append((t, d))

    def handle_endtag(self, t):
        if self.inb and t == "section":
            self.inb = False


FILES = sys.argv[1:]
bad_total = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = C(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    miss = []
    for t, a in dzh:
        for need in ("data-en", "data-ja", "data-ko", "data-fr", "data-es"):
            if not a.get(need, "").strip():
                miss.append((t, need))
    nod = [(t, a.get("class", "")[:24]) for t, a in p.tags if "data-zh" not in a]
    # 引号畸形：data-x="....." 后紧跟额外引号或属性名被切成怪名
    q_bad = [(t, k) for t, a in p.tags for k in a if k.startswith("data-") and any(c in k for c in '"=')]
    attr_names = set(k for t, a in p.tags for k in a if k.startswith("data-"))
    bad_total += len(miss) + len(q_bad)
    print("%s  元素=%d 带data-zh=%d 缺属性=%d %s" % (f, len(p.tags), len(dzh), len(miss), miss[:8]))
    print("    无data-zh的元素: %s" % nod)
    print("    属性名异常: %s" % q_bad)
    print("    data-* 属性种类: %s" % sorted(attr_names))
print("总问题数:", bad_total)
