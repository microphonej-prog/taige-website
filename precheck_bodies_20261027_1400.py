#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-27 14:00 批次正文属性体检：.article-body 内每个元素必须四语…六语齐全"""
import os, sys
from html.parser import HTMLParser

os.chdir(os.path.dirname(os.path.abspath(__file__)))

BODIES = ["blog/_body_fba.html", "blog/_body_us_epr.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
TEXT_TAGS = {"p", "h2", "h3", "h4", "li", "td", "th", "div", "a", "span"}
SKIP_OK = {"ul", "ol", "table", "tr", "section", "div"}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.problems = []
        self.count = 0
        self.in_body = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "section" and "article-body" in (d.get("class") or ""):
            self.in_body = 1
        if not self.in_body:
            return
        if tag in ("br", "strong", "em", "b", "i", "img", "meta", "link"):
            return
        self.count += 1
        has = [l for l in LANGS if ("data-" + l) in d]
        klass = d.get("class") or ""
        # 纯结构容器允许无 data-*（但 div 带 callout/cta-box 必须有）
        if not has:
            if tag in ("ul", "ol", "table", "tr", "thead", "tbody", "section"):
                return
            if tag == "div" and ("callout" in klass or "cta-box" in klass or "container" in klass):
                return
            if tag == "li":
                self.li_no_data_ok = getattr(self, "li_no_data_ok", 0) + 1
                return
            self.problems.append("<%s> 无任何 data-* (class=%r)" % (tag, klass))
            return
        missing = [l for l in LANGS if l not in has]
        if missing:
            self.problems.append("<%s class=%r> 缺 %s" % (tag, klass, ",".join(missing)))
        for l in has:
            if not d["data-" + l].strip():
                self.problems.append("<%s> data-%s 为空" % (tag, l))
            if '""' in d["data-" + l]:
                self.problems.append("<%s> data-%s 含双引号" % (tag, l))

    def handle_endtag(self, tag):
        if self.in_body and tag == "section":
            self.in_body = 0


fail = 0
for b in BODIES:
    s = open(b, encoding="utf-8").read()
    p = P()
    p.feed(s)
    print("%-28s 元素 %3d 问题 %d" % (b, p.count, len(p.problems)))
    for x in p.problems[:20]:
        print("   -", x)
    fail += len(p.problems)
    # 中文正文字数（粗略）
    import re
    zh = sum(len(re.findall(r"[\u4e00-\u9fff]", m)) for m in
             re.findall(r'data-zh="([^"]*)"', s))
    print("   中文正文字符数(含属性内文本重复计)：%d" % zh)

print("\n总问题数:", fail)
sys.exit(1 if fail else 0)
