#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""正文四/六语属性体检：解析 .article-body 内每个带 data-zh 的元素，检查缺哪个语言。
用法: F:/hermes/venvs/tools/Scripts/python.exe precheck_bodies_20261101_2000.py
"""
import sys, io
from html.parser import HTMLParser

FILES = [
    ("blog/_body_samplefee.html", "打样费与样品政策"),
    ("blog/_body_perforation.html", "吊牌易撕线"),
]
LANGS = ["data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.elems = []   # (tag, dict attrs)
        self.in_body = False

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        cls = d.get("class", "")
        if tag == "section" and "article-body" in cls:
            self.in_body = True
        if self.in_body:
            self.elems.append((tag, d))
        if tag not in ("meta", "link", "img", "br", "hr", "input"):
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag == "section" and self.in_body:
            self.in_body = False


ok = True
for path, label in FILES:
    s = open(path, encoding="utf-8").read()
    p = P()
    p.feed(s)
    total = 0
    missing = {}
    for tag, d in p.elems:
        if "data-zh" not in d:
            continue
        # 只统计需要文案的元素
        if tag in ("html", "body", "head", "meta", "link", "section", "div", "table", "thead",
                   "tbody", "tr", "ul", "ol", "br", "img", "style", "script"):
            continue
        total += 1
        miss = [l for l in LANGS if l not in d]
        if miss:
            missing.setdefault(tuple(miss), 0)
            missing[tuple(miss)] += 1
    print("%-34s %s  需翻译元素 %d，缺失分布 %s" % (path, label, total, missing or "无"))
    if missing:
        ok = False
    # 裸双引号检测（属性值里出现未转义的引号会让解析错乱）
    if '=""' in s:
        print("  !! 发现空属性或引号异常（=\"\"）")
        ok = False
    if "<strong>" in s and s.count("<strong>") != s.count("</strong>"):
        print("  !! strong 标签不配对")
        ok = False

print("PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
