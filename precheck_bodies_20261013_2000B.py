#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-13 第三批（20:00）正文预检：data-* 属性完整性 + 未转义 & + 裸双引号 + 结构检查"""
import re, sys, io
from html.parser import HTMLParser

BODIES = ["blog/_body_neckwear.html", "blog/_body_belts.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


bad_total = 0
for f in BODIES:
    s = open(f, encoding="utf-8").read()
    p = Collector()
    p.feed(s)
    p.close()
    total = len(p.tags)
    with_zh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in with_zh:
        lack = [l for l in LANGS if ("data-%s" % l) not in a]
        if lack:
            missing.append((t, lack, a.get("data-zh", "")[:40]))
    # 空值检查
    empty = [(t, l) for t, a in with_zh for l in LANGS if a.get("data-%s" % l, "x") == ""]
    # 未转义 & （非实体）
    raw_amp = re.findall(r'&(?!(amp|nbsp|quot|lt|gt|#\d+);)', s)
    # 属性值里裸双引号导致的畸形（HTMLParser 会容忍，用正则找 data-xx="..."> 里出现 =" 的可疑）
    odd = re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"\s*=', s)
    h2 = len(re.findall(r'<h2 ', s))
    print("== %s" % f)
    print("   标签总数 %d，含 data-zh 的标签 %d，h2 小节 %d" % (total, len(with_zh), h2))
    print("   缺语言属性的元素: %d %s" % (len(missing), missing[:5]))
    print("   值为空的属性: %d %s" % (len(empty), empty[:5]))
    print("   未转义 & : %d" % len(raw_amp))
    print("   可疑属性拼接: %d %s" % (len(odd), odd[:3]))
    if missing or empty or raw_amp or odd:
        bad_total += 1
    # 正文默认文本（非属性）里出现过少的简体残留？
    txt = re.sub(r'<[^>]+>', '', s)
    if "data-" in txt:
        i = txt.index("data-")
        print("   !! 属性泄漏片段: %r" % txt[max(0, i - 60):i + 80])
    print("   文件大小 %.1f KB" % (len(s.encode("utf-8")) / 1024.0))

print("预检结果: %s" % ("全部通过" if bad_total == 0 else "存在 %d 个文件问题" % bad_total))
sys.exit(1 if bad_total else 0)
