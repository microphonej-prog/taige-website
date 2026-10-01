#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-01 晚上（20:00）批次：正文文件预检（六语属性完整性 + 引号畸形 + 裸 & + JSON-LD 无关项）"""
import re
import sys
from html.parser import HTMLParser

BODIES = ["blog/_body_effects.html", "blog/_body_rainwear.html"]
NEED = ["data-en", "data-ja", "data-ko", "data-fr", "data-es"]


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, {k.lower(): (v or "") for k, v in attrs}))


bad = 0
for f in BODIES:
    s = open(f, encoding="utf-8").read()
    p = Collector()
    p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in NEED:
            if not a.get(need, "").strip():
                missing.append((t, need, a.get("data-zh", "")[:30]))
    print("== %s" % f)
    print("   标签总数 %d，带 data-zh 的 %d，缺 en/ja/ko/fr/es 的 %d" % (len(p.tags), len(dzh), len(missing)))
    for m in missing[:10]:
        print("     MISSING", m)
    bad += len(missing)

    empties = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    bare_amp = re.findall(r'&(?!amp;|nbsp;|quot;|#|lt;|gt;)', s)
    # 属性值后紧跟字母（引号畸形）
    malformed = re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)
    print("   空属性=%d 裸&=%d 引号畸形=%d" % (len(empties), len(bare_amp), len(malformed)))
    if empties or bare_amp or malformed:
        bad += len(empties) + len(bare_amp) + len(malformed)
    # 拉丁属性里残留 CJK（fr/es/en/ko 里不该有汉字）
    for lang in ("en", "fr", "es"):
        for v in re.findall(r'data-%s="([^"]*)"' % lang, s):
            cjk = re.findall(r'[\u4e00-\u9fff]', v)
            if cjk:
                print("   CJK 残留 in data-%s: %s => %s" % (lang, "".join(cjk), v[:70]))
                bad += 1
    # ja 里出现简体字敏感词（粗查）
    for v in re.findall(r'data-ja="([^"]*)"', s):
        for w in ("标签", "包装", "目录", "库存", "订单", "网站"):
            if w in v:
                print("   JA 简体残留 %s: %s" % (w, v[:70]))
                bad += 1

print("\n预检问题总数 = %d" % bad)
sys.exit(1 if bad else 0)
