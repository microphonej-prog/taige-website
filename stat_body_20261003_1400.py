#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按文本节点统计正文中文字数（排除所有属性），并与既有文章对比。"""
import re, sys
from html.parser import HTMLParser

FILES = ["blog/_body_zipper.html", "blog/_body_interlining.html",
         "blog/_body_leather.html", "blog/_body_children.html",
         "blog/_body_elastic.html", "blog/_body_buttons.html"]

class T(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.buf = []
    def handle_data(self, d):
        self.buf.append(d)

for f in FILES:
    try:
        s = open(f, encoding="utf-8").read()
    except FileNotFoundError:
        print("%-34s 缺失" % f)
        continue
    p = T(); p.feed(s)
    txt = "".join(p.buf)
    print("%-34s 可见中文字数=%d  可见字符总数=%d" % (f, len(re.findall(r"[\u4e00-\u9fff]", txt)), len(txt.strip())))
