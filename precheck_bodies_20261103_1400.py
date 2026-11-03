#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验两篇新正文文件的六语属性完整性（HTMLParser 逐属性判断，避免正则在属性值内的 > 截断）"""
import sys
from html.parser import HTMLParser

LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
FILES = ["blog/_body_scratch.html", "blog/_body_yarn.html"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.issues = []
        self.info = []
        self.count = 0
        self.tags = {}

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in ("br", "img", "meta", "link", "input", "hr",
                   "section", "div", "table", "thead", "tbody", "tr", "ul"):
            return
        self.count += 1
        self.tags[tag] = self.tags.get(tag, 0) + 1
        missing = [l for l in LANGS if ("data-" + l) not in d]
        if missing:
            if tag == "li" and not any(k.startswith("data-") for k in d):
                self.info.append("相关文章 li（纯链接，属性在 a 上）")
                return
            self.issues.append("%s 缺 %s" % (tag, ",".join(missing)))
        for l in LANGS:
            v = d.get("data-" + l)
            if v is not None and not v.strip():
                self.issues.append("%s 的 data-%s 为空" % (tag, l))


bad = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = P()
    p.feed(s)
    print("== %s  元素数=%d  类型=%s" % (f, p.count, p.tags))
    print("   缺/空语言属性的元素: %d" % len(p.issues))
    for i in p.issues[:15]:
        print("     -", i)
    bad += len(p.issues)
    # 裸引号体检：属性值内出现裸 " 会截断解析，统计可疑片段
    print("   data-zh 出现次数: %d" % s.count("data-zh="))
    print("   可疑双引号片段 (=\"\"): %d" % s.count('=""'))
    # 中文正文长度
    import re
    zh = re.findall(r'data-zh="(.*?)"\s', s)
    body_zh = "".join(re.findall(r'data-zh="([^"]*)"[^>]*>[^<]*</(?:p|h2|li|td|th|a|span)>', s, re.S))
    print("   中文正文可见字数约: %d" % len(re.sub(r"<[^>]+>", "", body_zh)))

print("总问题数: %d" % bad)
sys.exit(1 if bad else 0)
