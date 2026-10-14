#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对照：既有已生成语言页（neckwear/belts）在 article-body 内是否保留 data-* 属性。"""
import os, re, io
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)


class S(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_body = False
        self.depth = 0
        self.stack = []
        self.items = []

    def handle_starttag(self, tag, attrs):
        if not self.in_body and tag == "section" and dict(attrs).get("class") == "article-body":
            self.in_body = True
            self.depth = 1
            return
        if not self.in_body or tag in ("br", "img", "input", "meta", "link", "hr"):
            return
        if tag == "section":
            self.depth += 1
        self.stack.append([tag, dict(attrs), ""])
        self.items.append(self.stack[-1])

    def handle_endtag(self, tag):
        if not self.in_body:
            return
        if tag == "section":
            self.depth -= 1
            if self.depth == 0:
                self.in_body = False
                return
        if self.stack:
            self.stack.pop()

    def handle_data(self, data):
        if self.in_body and self.stack and data.strip():
            self.stack[-1][2] += data.strip()


for p in ["en/blog/neckwear-trims-label-guide.html", "en/blog/belts-suspenders-trims-guide.html",
          "en/blog/apron-trims-label-guide.html", "blog/apron-trims-label-guide.html",
          "blog/clothing-label-compliance-netherlands.html"]:
    s = io.open(p, encoding="utf-8").read()
    sc = S()
    sc.feed(s)
    texted = [it for it in sc.items if it[2]]
    with_en = [it for it in texted if it[1].get("data-en")]
    with_zh = [it for it in texted if it[1].get("data-zh")]
    print("%-52s 文本元素=%3d 带data-en=%3d 带data-zh=%3d" % (p, len(texted), len(with_en), len(with_zh)))
