#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""定位 data-zh 与默认文本的差异点（打印首个不同位置附近的 repr）。"""
import sys, re, importlib.util

spec = importlib.util.spec_from_file_location("pc", "precheck_bodies_20260926_pm.py")

# 复用 precheck 里的 Collector：直接 exec 到只到 class 定义前太麻烦，这里独立实现最小版
from html.parser import HTMLParser
VOID = {"br", "img", "meta", "link", "input", "hr", "source"}


class C(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.stack = []
        self.results = []

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        if tag == "section" and d.get("class", "").startswith("article-body"):
            self.in_body = True
            return
        if not self.in_body:
            return
        for e in self.stack:
            if e["dzh"] is not None:
                e["buf"].append("<%s>" % tag)
        self.stack.append({"tag": tag, "dzh": d.get("data-zh"), "buf": []})
        if tag in VOID:
            e = self.stack.pop()
            if e["dzh"] is not None:
                self.results.append((tag, e["dzh"], "".join(e["buf"])))

    def handle_data(self, data):
        if self.in_body:
            for e in self.stack:
                if e["dzh"] is not None:
                    e["buf"].append(data)

    def handle_entityref(self, name):
        if self.in_body:
            for e in self.stack:
                if e["dzh"] is not None:
                    e["buf"].append("&%s;" % name)

    def handle_charref(self, name):
        if self.in_body:
            for e in self.stack:
                if e["dzh"] is not None:
                    e["buf"].append("&#%s;" % name)

    def _close(self, tag):
        while self.stack:
            e = self.stack.pop()
            if e["dzh"] is not None:
                self.results.append((e["tag"], e["dzh"], "".join(e["buf"])))
            if e["tag"] == tag:
                return

    def handle_endtag(self, tag):
        if not self.in_body:
            return
        if tag == "section":
            while self.stack:
                e = self.stack.pop()
                if e["dzh"] is not None:
                    self.results.append((e["tag"], e["dzh"], "".join(e["buf"])))
            self.in_body = False
            return
        self._close(tag)
        for e in self.stack:
            if e["dzh"] is not None:
                e["buf"].append("</%s>" % tag)


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


for f in ["blog/trim-third-party-testing-guide.html", "blog/sample-room-trims-checklist.html"]:
    s = open(f, encoding="utf-8").read()
    p = C()
    p.feed(s)
    print("=====", f, "元素", len(p.results))
    shown = 0
    for t, dzh, inner in p.results:
        a, b = norm(dzh), norm(inner)
        if a != b:
            i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
            print("  [%s] len dzh=%d inner=%d 差异位置=%d" % (t, len(a), len(b), i))
            print("     dzh  : ...%s..." % a[max(0, i - 25):i + 25])
            print("     inner: ...%s..." % b[max(0, i - 25):i + 25])
            shown += 1
            if shown >= 3:
                break
