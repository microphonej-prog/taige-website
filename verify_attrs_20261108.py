#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用 HTMLParser 逐标签核对八语属性（避免属性值里 <strong> 的 > 造成的假报警）。"""
from html.parser import HTMLParser

SLUGS = ["silica-gel-desiccant-apparel-packaging.html", "care-label-roll-direction-core-guide.html"]
LANGS = ["zh", "en", "fr", "es", "ja", "ko", "de", "pt"]
VOID = {"br", "img", "meta", "link", "input", "hr", "source"}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.problems = []
        self.total = 0
        self.in_body = False

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "section" and "article-body" in (d.get("class") or ""):
            self.in_body = True
        if self.in_body and "data-zh" in d:
            self.total += 1
            miss = [l for l in LANGS if ("data-" + l) not in d]
            if miss:
                self.problems.append((tag, miss, (d.get("data-zh") or "")[:60]))
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag == "section" and self.stack and "section" in self.stack:
            pass
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        if tag == "main":
            self.in_body = False


for slug in SLUGS:
    s = open("blog/" + slug, encoding="utf-8").read()
    p = P()
    p.feed(s)
    print("%s: 带 data-zh 的元素 %d 个, 缺语言属性 %d 个" % (slug, p.total, len(p.problems)))
    for x in p.problems[:8]:
        print("   ", x)

print("\n=== de / pt 页面静态渲染抽查 ===")
import re
for l in ("de", "pt"):
    s = open("%s/blog/care-label-roll-direction-core-guide.html" % l, encoding="utf-8").read()
    t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S).group(1)
    foot = re.search(r"<footer.*?</footer>", s, re.S).group(0)
    ftxt = re.sub(r"<[^>]+>", " ", foot)
    ftxt = re.sub(r"\s+", " ", ftxt).strip()
    print("[%s] title=%s" % (l, t.strip()))
    print("[%s] h1=%s" % (l, h1.strip()))
    print("[%s] footer 前 90 字=%s" % (l, ftxt[:90]))
    print()
