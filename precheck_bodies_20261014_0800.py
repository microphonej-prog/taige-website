#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""正文文件预检（2026-10-14 08:00 批次）：
1) .article-body 内每个 start tag 是否都带 data-zh/en/ja/ko/fr/es
2) 中文正文规模（data-zh 合计字数）
3) 属性值内是否出现裸 ASCII 双引号残留（用 HTMLParser 逐属性解析，避免正则误判）
4) 相关文章链接指向的文件是否存在
"""
import os, re, sys, io
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
LANGS = ["data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es"]
FILES = ["blog/_body_apron.html", "blog/_body_nlcomp.html"]


class Scan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.in_body = 0
        self.missing = []
        self.tags = 0
        self.zh = 0
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "section" and dict(attrs).get("class") == "article-body":
            self.in_body = 1
        if not self.in_body:
            return
        if tag in ("br", "img", "input", "meta", "link"):
            return
        d = dict(attrs)
        self.tags += 1
        miss = [a for a in LANGS if a not in d or d[a] is None or d[a].strip() == ""]
        if miss:
            self.missing.append((tag, d.get("class", ""), miss))
        if d.get("data-zh"):
            self.zh += len(re.sub(r"\s", "", d["data-zh"]))
        if tag == "a" and d.get("href"):
            self.links.append(d["href"])


ok = True
for f in FILES:
    p = os.path.join(ROOT, f)
    s = io.open(p, encoding="utf-8").read()
    sc = Scan()
    sc.feed(s)
    print("=== %s" % f)
    print("  元素数=%d  data-zh 合计字数=%d  缺属性=%d" % (sc.tags, sc.zh, len(sc.missing)))
    for t in sc.missing:
        ok = False
        print("  !! 缺属性:", t)
    # 引号畸形检查：data-XXX=" 后紧跟 " （历史上移动端崩溃元凶）
    for m in re.finditer(r'data-(?:zh|en|ja|ko|fr|es)=""', s):
        ok = False
        print("  !! 空属性值:", s[max(0, m.start() - 40):m.start() + 20])
    # 未转义 & 检查
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
        else:
            print("  链接 OK:", href)

print()
print("预检结论:", "通过" if ok else "有阻塞项")
sys.exit(0 if ok else 1)
