#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-05 晚间批次预检：正文六语属性完整性 + 引号畸形 + 裸 & + desc 长度"""
import re, sys, importlib.util
from html.parser import HTMLParser

sys.path.insert(0, ".")
from daily_meta_20261005_2000 import ARTICLES

LANGS = ("en", "ja", "ko", "fr", "es")


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.tags = []

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        if tag == "section" and d.get("class", "").startswith("article-body"):
            self.in_body = True
            return
        if self.in_body:
            self.tags.append((tag, d))

    def handle_endtag(self, tag):
        if self.in_body and tag == "section":
            self.in_body = False


print("== 1) 正文六语属性完整性 ==")
total_missing = 0
for a in ARTICLES:
    s = open(a["body"], encoding="utf-8").read()
    p = Collector()
    p.feed(s)
    dzh = [(t, x) for t, x in p.tags if "data-zh" in x]
    missing = []
    for t, x in dzh:
        for need in LANGS:
            if not x.get("data-" + need, "").strip():
                missing.append((t, need))
    total_missing += len(missing)
    print("  %s" % a["body"])
    print("    标签 %d 个，带 data-zh 的 %d 个；缺语言属性 %d 个 %s"
          % (len(p.tags), len(dzh), len(missing), missing[:8]))
    print("    引号畸形 data-xx=\"\" : %d ; 裸 & : %d ; 元素数不足元素: %d"
          % (len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s)),
             len(re.findall(r'<(p|h2|h3|li|th|td|div|table)(?![^>]*data-zh)', s))))

print("\n== 2) desc 长度 ==")
for a in ARTICLES:
    ok_zh = 80 <= len(a["desc_zh"]) <= 120
    ok_en = 150 <= len(a["desc_en"]) <= 160
    print("  %-40s zh=%3d %s | en=%3d %s"
          % (a["slug"], len(a["desc_zh"]), "OK" if ok_zh else "调整",
             len(a["desc_en"]), "OK" if ok_en else "调整"))

print("\n== 3) 内链目标存在性 ==")
import os
for a in ARTICLES:
    s = open(a["body"], encoding="utf-8").read()
    for href in re.findall(r'<a href="([^"]+)"', s):
        if href.startswith("http") or href.startswith(".."):
            continue
        target = os.path.join("blog", href)
        print("  %-34s -> %-42s %s" % (a["slug"], href, "OK" if os.path.exists(target) else "缺失!"))

print("\n结论: 缺失语言属性总数 = %d" % total_missing)
raise SystemExit(1 if total_missing else 0)
