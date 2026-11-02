#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描两篇新正文：属性合法性 + 语言残留 + 六语覆盖"""
import re, sys
from html.parser import HTMLParser

FILES = ["blog/apparel-trims-machine-vision-inspection.html", "blog/garment-disassembly-recyclable-trims.html"]
CJK = re.compile(r'[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]')
SIMP = "这个们时说会开关边组织纤维统认证书环保复杂择对应该从来后进动产业务质问题实际标记为准筛处图纸袋单够满费值钱让举义习书买东车长门间见语请谢识讲论设试词译详误调谈诸课读变计订讨训议讯层检测触觉视质量线结构网络优势传统复图层织印规纤维压缩简热湿温湿"
SIMP = "".join(sorted(set(SIMP)))
HANZI_IN_KO = re.compile(r'[\u4e00-\u9fff]')


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = P()
    p.feed(s)
    problems = []
    counters = {"el": 0, "full6": 0}
    for tag, a in p.tags:
        if tag in ("section", "div", "br", "thead", "tbody", "tr"):
            continue
        has_zh = "data-zh" in a
        if not has_zh:
            continue
        counters["el"] += 1
        if all(k in a for k in ("data-en", "data-fr", "data-es", "data-ja", "data-ko")):
            counters["full6"] += 1
        else:
            problems.append("缺语言属性: <%s> %s" % (tag, a.get("data-zh", "")[:40]))
        for lang in ("en", "fr", "es"):
            v = a.get("data-" + lang, "")
            if CJK.search(v):
                problems.append("data-%s 含 CJK: %s" % (lang, v[:60]))
        for ch in a.get("data-ja", ""):
            if ch in SIMP and ch not in "标记线结构压缩检测触觉视质量规图层热湿温":
                problems.append("data-ja 疑似简体字 %r: %s" % (ch, a.get("data-ja", "")[:60]))
                break
        ko = a.get("data-ko", "")
        if HANZI_IN_KO.search(ko):
            problems.append("data-ko 含汉字: %s" % ko[:60])
    # 引号嵌套 / 裸双引号风险：属性值里出现 &quot; 正常，裸 " 不可能存在（HTMLParser 会截断）
    print("=== %s  元素 %d，六语齐全 %d" % (f, counters["el"], counters["full6"]))
    if problems:
        for x in problems:
            print("  !", x)
    else:
        print("  OK 无残留")
    # 字数（中文）
    zh = re.findall(r'data-zh="([^"]*)"', s)
    txt = re.sub(r'<[^>]+>', '', " ".join(zh))
    print("  中文字数约 %d" % len(re.sub(r'[^\u4e00-\u9fff]', '', txt)))
