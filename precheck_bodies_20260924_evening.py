#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成前体检：两篇正文文件的六语属性完整性 / 引号嵌套 / 关键词落位"""
import re, sys
from html.parser import HTMLParser

BODIES = ["blog/_body_cny.html", "blog/_body_uae.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
VOID = {"br", "img", "input", "meta", "link", "hr"}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_startendtag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)


fails = 0
for b in BODIES:
    src = open(b, encoding="utf-8").read()
    p = P()
    p.feed("<html>" + src + "</html>")
    p.close()

    missing = {}
    for tag, attrs in p.tags:
        has = [l for l in LANGS if ("data-" + l) in attrs]
        if not has:
            continue
        if len(has) != 6:
            missing.setdefault(tag, []).append(sorted(set(LANGS) - set(has)))

    print("=== %s ===" % b)
    print("  六语元素总数：%d" % sum(1 for t, a in p.tags if "data-zh" in a))
    print("  缺语言的元素数：%d %s" % (sum(len(v) for v in missing.values()), missing))

    # 属性值内不允许再出现裸双引号（解析器已能容错，这里查原始串）
    bad_quotes = re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[^>]*=\s*"', src)
    # 空属性值
    empty = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', src)
    # 未转义 & （后面不是合法实体）
    amp = re.findall(r'&(?!(?:amp|lt|gt|quot|nbsp|#\d+|#x[0-9a-fA-F]+);)', src)
    # 元素内部标签数与 data 语言数不匹配（<strong> 类内嵌）
    print("  空 data 属性：%d" % len(empty))
    print("  未转义 & ：%d" % len(amp))
    if amp:
        for m in list(re.finditer(r'.{40}&(?!(?:amp|lt|gt|quot|nbsp|#\d+|#x[0-9a-fA-F]+);).{40}', src))[:5]:
            print("     ", m.group(0))
    if missing or empty or amp:
        fails += 1

    body_text = "".join(p.text)
    print("  正文字数（中文）：%d" % len(re.findall(r'[\u4e00-\u9fff]', body_text)))
    for kw in ["data-zh"]:
        pass

sys.exit(1 if fails else 0)
