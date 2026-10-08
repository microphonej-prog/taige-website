#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-08 下午批次：把 scratch 中的正文分段文件拼成 blog/_body_*.html，并做属性完整性自检。

用法: F:/hermes/venvs/tools/Scripts/python.exe join_bodies_20261008_pm.py
"""
import os
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
SCRATCH = "F:/hermes/cache/scratch"

PAIRS = [
    (["wood_a.html", "wood_b.html"], "blog/_body_wood.html"),
    (["pod_a.html", "pod_b.html"], "blog/_body_pod.html"),
]
WANT = ("data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es")


def join(parts, out):
    buf = []
    for p in parts:
        with open(os.path.join(SCRATCH, p), encoding="utf-8") as f:
            s = f.read()
        if not s.endswith("\n"):
            s += "\n"
        buf.append(s)
    text = "".join(buf)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("拼接 -> %-26s %d 字节 (%d 段)" % (out, len(text.encode("utf-8")), len(parts)))
    return text


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.n = 0
        self.miss = []
        self.dupes = []
        self.tags = {}

    def handle_starttag(self, tag, attrs):
        names = [a[0] for a in attrs]
        if len(names) != len(set(names)):
            self.dupes.append(tag)
        d = dict(attrs)
        self.tags[tag] = self.tags.get(tag, 0) + 1
        if "data-zh" in d:
            self.n += 1
            m = [k for k in WANT if k not in d]
            if m:
                self.miss.append((tag, d["data-zh"][:24], m))

    handle_startendtag = handle_starttag


ok = True
for parts, out in PAIRS:
    text = join(parts, out)
    if not text.startswith('  <section class="article-body">'):
        print("  !! 开头不是 article-body section")
        ok = False
    if not text.rstrip().endswith("</section>"):
        print("  !! 结尾不是 </section>")
        ok = False
    for bad in ['data-zh=""', 'data-en=""', 'data-fr=""', 'data-es=""', 'data-ja=""', 'data-ko=""']:
        if bad in text:
            print("  !! 空属性值", bad)
            ok = False
    c = Checker()
    c.feed(text)
    print("  data-zh 元素=%d  缺属性=%d  重复属性元素=%d  标签分布=%s"
          % (c.n, len(c.miss), len(c.dupes), c.tags))
    for m in c.miss[:10]:
        print("     MISS", m)
        ok = False
    if c.dupes:
        ok = False
    h2 = text.count("<h2 ")
    print("  h2 小节=%d  table=%d  li=%d" % (h2, text.count("<table>"),
                                             text.count("<li ") + text.count("<li>")))
    if h2 < 6:
        print("  !! h2 数量偏少")
    if 'href="index.html"' not in text or 'href="../contact.html"' not in text:
        print("  !! 缺少相关文章 / CTA 链接")
        ok = False

print("自检结果:", "通过" if ok else "有问题")
sys.exit(0 if ok else 1)
