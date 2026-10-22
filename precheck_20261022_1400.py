#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-22 14:00 批次：正文生成前体检（属性完整性 / 语言纯净度 / 默认文本一致）"""
import re, sys
from html.parser import HTMLParser

BODIES = ["blog/_body_sea.html", "blog/_body_rpet.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
CJK = re.compile(r'[\u4e00-\u9fff]')
TARGET = {"p", "h2", "h3", "li", "td", "th", "div", "a", "span", "strong"}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []          # (tag, attrs dict, inner_text)
        self.stack = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        self.tags.append([tag, d, ""])
        if tag not in ("br", "img", "meta", "link", "input", "hr"):
            self.stack.append(self.tags[-1])

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        for t in self.stack:
            t[2] += data


ok = True
for b in BODIES:
    s = open(b, encoding="utf-8").read()
    # 1. 语法：属性内不得出现裸双引号导致的 data-xx="" 空值
    for m in re.finditer(r'data-(?:zh|en|ja|ko|fr|es)=""', s):
        print("!! 空属性值", b, m.start()); ok = False
    p = P(); p.feed(s)
    total = miss = 0
    for tag, d, txt in p.tags:
        if "data-zh" not in d:
            continue
        total += 1
        for l in LANGS:
            k = "data-" + l
            if k not in d or not d[k].strip():
                miss += 1
                print("!! 缺 %s  → %s … %s" % (k, tag, txt[:40]))
                ok = False
        # 默认文本应与 data-zh 一致（允许 <strong> 等标签差异）
        a = re.sub(r'\s+', '', re.sub(r'<[^>]+>', '', d["data-zh"]))
        c = re.sub(r'\s+', '', txt)
        if a != c:
            print("!! 默认文本与 data-zh 不一致 → %s | %s || %s" % (tag, a[:50], c[:50]))
            ok = False
        # 语言纯净度：ko/fr/es 不得含汉字
        for l in ["ko", "fr", "es"]:
            if CJK.search(d.get("data-" + l, "")):
                print("!! %s 含汉字 → %s %s" % (l, tag, d["data-" + l][:60]))
                ok = False
    print("%-26s 带属性元素=%d 缺失=%d" % (b, total, miss))
    # 2. 中文正文长度（data-zh，去标签）
    zhs = "".join(re.sub(r"<[^>]+>", "", t[1]["data-zh"]) for t in p.tags if "data-zh" in t[1])
    print("   中文正文字数≈%d" % len(re.sub(r"\s", "", zhs)))
    # 3. 相关文章链接是否存在
    for href in re.findall(r'href="([a-z0-9\-]+\.html)"', s):
        import os
        if not os.path.exists("blog/" + href):
            print("!! 死链", href); ok = False

print("PRECHECK", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
