#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验正文文件的 data-* 六语完整性（HTMLParser 逐属性，避免正则截断）"""
import sys, json
from html.parser import HTMLParser

LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
KEEP = {"strong", "br", "em", "b", "i", "span", "a"}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.problems = []
        self.count = 0
        self.tagcount = {}

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        self.tagcount[tag] = self.tagcount.get(tag, 0) + 1
        if "data-zh" in d:
            self.count += 1
            missing = [l for l in LANGS if ("data-" + l) not in d]
            if missing:
                self.problems.append((tag, missing, d.get("data-zh", "")[:40]))
            for l in LANGS:
                v = d.get("data-" + l, "")
                if '"' in v:
                    self.problems.append((tag, ["bare-quote-" + l], v[:40]))
                if "\n" in v:
                    self.problems.append((tag, ["newline-" + l], v[:40]))
        if tag not in ("br", "img", "meta", "link", "input", "hr"):
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.problems.append(("MISMATCH", [tag], "stack=" + ",".join(self.stack[-3:])))


for path in sys.argv[1:]:
    s = open(path, encoding="utf-8").read()
    p = P()
    p.feed(s)
    print("=" * 60)
    print(path)
    print("  带 data 的元素: %d  问题: %d  未闭合: %s" % (p.count, len(p.problems), p.stack))
    for x in p.problems[:10]:
        print("   ", x)
    # 中文正文字数（去标签）
    import re
    txt = re.sub(r"<[^>]+>", "", s)
    zh = len(re.findall(r"[\u4e00-\u9fff]", txt))
    print("  可见中文字数(所有语言文本混合):", zh)
    print("  data-ja 计数:", s.count("data-ja="), " data-ko:", s.count("data-ko="),
          " data-fr:", s.count("data-fr="), " data-es:", s.count("data-es="))
