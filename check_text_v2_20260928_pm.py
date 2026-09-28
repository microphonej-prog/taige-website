#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""精确核对（v2）：元素可见文本 vs data-zh（两边都去标签、统一空白与实体）+
六语属性是否与可见文本同样带 <strong> 小标题（2026-09-28 下午批次）。
用法: <python> check_text_v2_20260928_pm.py
"""
import sys, re, html
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding="utf-8")
FILES = ["blog/_body_origin.html", "blog/_body_pp.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]


class Node:
    def __init__(self, tag, attrs):
        self.tag, self.attrs, self.text = tag, attrs, []


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.nodes = [], []

    def handle_starttag(self, tag, attrs):
        if tag in ("br", "img"):
            if self.stack:
                self.stack[-1].text.append(" ")
            return
        self.stack.append(Node(tag, dict(attrs)))

    def handle_startendtag(self, tag, attrs):
        if self.stack:
            self.stack[-1].text.append(" ")

    def handle_endtag(self, tag):
        if tag in ("br", "img") or not self.stack:
            return
        n = self.stack.pop()
        if self.stack:
            self.stack[-1].text.append("".join(n.text))
        self.nodes.append(n)

    def handle_data(self, data):
        if self.stack:
            self.stack[-1].text.append(data)


def plain(s):
    return re.sub(r"\s+", "", re.sub(r"<[^>]+>", "", html.unescape(s or "")))


bad_text = bad_strong = 0
for f in FILES:
    p = P()
    p.feed(open(f, encoding="utf-8").read())
    for n in p.nodes:
        if "data-zh" not in n.attrs or n.tag == "a":
            continue
        vis = plain("".join(n.text))
        a_zh = plain(n.attrs["data-zh"])
        if vis and a_zh and vis != a_zh:
            bad_text += 1
            print("!! <%s> 文本不一致\n   可见: %s\n   属性: %s" % (n.tag, vis[:60], a_zh[:60]))
        vis_strong = "".join(n.text).lstrip().startswith("<strong>")
        for lang in LANGS:
            v = n.attrs.get("data-%s" % lang)
            if v is None:
                continue
            if v.startswith("<strong>") != vis_strong:
                bad_strong += 1
                print("!! <%s> data-%s 小标题标记与可见文本不一致：%s" % (n.tag, lang, v[:40]))
print("文本不一致 %d 处；<strong> 标记不一致 %d 处" % (bad_text, bad_strong))
