#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验：正文中所有带 data-zh 的元素是否都具备其它五语（六语覆盖）"""
import os
from html.parser import HTMLParser

os.chdir(os.path.dirname(os.path.abspath(__file__)))
NEED = ["data-en", "data-fr", "data-es", "data-ja", "data-ko"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.bad = []
        self.withzh = 0

    def handle_starttag(self, t, a):
        d = dict(a)
        if "data-zh" in d:
            self.withzh += 1
            miss = [k for k in NEED if k not in d or not d[k].strip()]
            if miss:
                self.bad.append((t, miss))


for f in ["blog/_body_bom.html", "blog/_body_price.html", "blog/_body_destroy.html"]:
    p = P()
    p.feed(open(f, encoding="utf-8").read())
    print("%-28s data-zh 元素=%d 缺语种=%d %s" % (f, p.withzh, len(p.bad), p.bad[:5]))
