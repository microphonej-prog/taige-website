#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""正文文件预检（2026-10-14 08:00 批次，v2）：
1) 只对「含直接文本内容」的元素要求 data-zh/en/ja/ko/fr/es（纯容器/包链接的 li 不算）
2) 中文正文规模（data-zh 合计字数）
3) 空属性值 / 裸 & 检查
4) 相关文章链接目标存在性
"""
import os, re, sys, io
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
LANGS = ["data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es"]
FILES = ["blog/_body_apron.html", "blog/_body_nlcomp.html"]


class Scan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.elems = []
        self.open = []
        self.in_body = False
        self.zh = 0
        self.links = []

    def handle_starttag(self, tag, attrs):
        if not self.in_body and tag == "section" and dict(attrs).get("class") == "article-body":
            self.in_body = True
        if not self.in_body:
            return
        if tag in ("br", "img", "input", "meta", "link", "hr"):
            return
        d = dict(attrs)
        self.elems.append([tag, d, False])
        self.open.append(len(self.elems) - 1)
        if d.get("data-zh"):
            self.zh += len(re.sub(r"\s", "", d["data-zh"]))
        if tag == "a" and d.get("href"):
            self.links.append(d["href"])

    def handle_endtag(self, tag):
        if self.open:
            self.open.pop()

    def handle_data(self, data):
        if not self.in_body or not data.strip():
            return
        if self.open:
            self.elems[self.open[-1]][2] = True


ok = True
for f in FILES:
    s = io.open(os.path.join(ROOT, f), encoding="utf-8").read()
    sc = Scan()
    sc.feed(s)
    with_text = [e for e in sc.elems if e[2]]
    miss = [(t, d.get("class", ""), [a for a in LANGS if not d.get(a)])
            for t, d, _ in with_text]
    miss = [m for m in miss if m[2]]
    print("=== %s" % f)
    print("  容器元素=%d  含文本元素=%d  data-zh 合计字数=%d  缺属性元素=%d"
          % (len(sc.elems), len(with_text), sc.zh, len(miss)))
    for t in miss:
        ok = False
        print("  !! 缺属性:", t)
    for m in re.finditer(r'data-(?:zh|en|ja|ko|fr|es)=""', s):
        ok = False
        print("  !! 空属性值:", s[max(0, m.start() - 40):m.start() + 20])
    for m in re.finditer(r'&(?!(amp|nbsp|quot|lt|gt|#\d+);)', s):
        ok = False
        print("  !! 裸 &:", s[max(0, m.start() - 30):m.start() + 20].replace("\n", " "))
    for href in sorted(set(sc.links)):
        if href.startswith(("http", "#", "mailto")):
            continue
        tgt = os.path.join(ROOT, "blog", href)
        if not os.path.exists(tgt):
            ok = False
            print("  !! 链接目标不存在:", href)
    print("  内部链接 %d 个" % len(set(sc.links)))

print()
print("预检结论:", "通过" if ok else "有阻塞项")
sys.exit(0 if ok else 1)
