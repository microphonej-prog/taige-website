#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""预检：两篇新正文文件的六语属性完整性 + HTML 解析健全性（2026-10-12 下午批次）"""
import os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
FILES = ["blog/_body_trousers.html", "blog/_body_tee.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
TAGS = ["p", "h2", "h3", "li", "th", "td", "div", "a", "span", "strong", "ol", "ul", "table"]


class Scan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.problems = []
        self.counts = {}
        self.attr_counts = {l: 0 for l in LANGS}

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in TAGS and "data-zh" in d:
            self.counts[tag] = self.counts.get(tag, 0) + 1
            for l in LANGS:
                if ("data-%s" % l) in d and d["data-%s" % l].strip():
                    self.attr_counts[l] += 1
                else:
                    self.problems.append("缺 data-%s：<%s> %s" % (l, tag, d.get("data-zh", "")[:40]))
        if tag not in ("br", "img", "meta", "link"):
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in self.stack:
            while self.stack and self.stack.pop() != tag:
                pass
        elif tag not in ("br", "img", "meta", "link"):
            self.problems.append("多余结束标签：</%s>" % tag)


for f in FILES:
    p = os.path.join(ROOT, f)
    s = open(p, encoding="utf-8").read()
    sc = Scan()
    sc.feed(s)
    print("=== %s (%d KB)" % (f, len(s.encode("utf-8")) // 1024))
    print("  带 data-zh 的元素：", sc.counts, "合计", sum(sc.counts.values()))
    print("  各语言属性命中：", sc.attr_counts)
    print("  未闭合栈：", sc.stack)
    if sc.problems:
        print("  ！问题 %d 条：" % len(sc.problems))
        for x in sc.problems[:20]:
            print("    -", x)
    else:
        print("  六语属性齐全，无异常")
    bad = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    print('  畸形 data-*="" 数量：', len(bad))
    print("  含「輔」「標」繁体字数量（应为 0，转繁前）：", len(re.findall(r'[輔標繁]', s)))
    print("  元素总数（<p>/<h2>/<h3>/<li>/<td>/<th>/<a>）：",
          len(re.findall(r'<(?:p|h2|h3|li|td|th|a)[\s>]', s)))
    # 正文中文长度（data-zh 累计）
    zh = re.findall(r'data-zh="([^"]*)"', s)
    zh_txt = re.sub(r'<[^>]+>', '', "".join(zh))
    print("  data-zh 中文字数（含标点）：", len(zh_txt))
