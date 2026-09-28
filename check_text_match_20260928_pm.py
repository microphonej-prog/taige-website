#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对比正文元素「可见文本」与 data-zh 属性值是否一致（2026-09-28 下午批次）。

可见文本（无 JS 时的兜底与爬虫可读内容）应与 data-zh 完全一致；不一致会导致
无 JS 用户/爬虫看到的内容与切换语言后的内容不同。
用法: <python> check_text_match_20260928_pm.py
"""
import sys, re, html
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding="utf-8")
FILES = ["blog/_body_origin.html", "blog/_body_pp.html"]


class Node:
    def __init__(self, tag, attrs):
        self.tag, self.attrs, self.text = tag, attrs, []


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.nodes = []

    def handle_starttag(self, tag, attrs):
        if tag in ("br", "img"):
            if self.stack:
                self.stack[-1].text.append("</br>")
            return
        self.stack.append(Node(tag, dict(attrs)))

    def handle_startendtag(self, tag, attrs):
        if self.stack:
            self.stack[-1].text.append("<%s>" % tag)

    def handle_endtag(self, tag):
        if not self.stack:
            return
        n = self.stack.pop()
        if tag in ("br", "img"):
            return
        if self.stack:
            self.stack[-1].text.append("".join(n.text))
        self.nodes.append(n)

    def handle_data(self, data):
        if self.stack:
            self.stack[-1].text.append(data)


def norm(s):
    return re.sub(r"\s+", "", s or "")


bad = 0
for f in FILES:
    p = P()
    p.feed(open(f, encoding="utf-8").read())
    for n in p.nodes:
        if "data-zh" not in n.attrs or n.tag in ("a",):
            continue
        vis = norm("".join(n.text))
        attr = norm(n.attrs["data-zh"])
        if vis and attr and vis != attr:
            bad += 1
            print("!! <%s> 可见文本与 data-zh 不一致" % n.tag)
            print("   可见: %s" % vis[:70])
            print("   属性: %s" % attr[:70])
print("不一致 %d 处" % bad)
