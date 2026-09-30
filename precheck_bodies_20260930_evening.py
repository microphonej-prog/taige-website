#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-30 晚上批次：正文文件前置体检（六语属性完整性 / 引号畸形 / 裸 & / 元素统计）"""
import re, sys
from html.parser import HTMLParser

BODIES = ["blog/_body_headercard.html", "blog/_body_suffocation.html"]
NEED = ["data-en", "data-ja", "data-ko", "data-fr", "data-es"]


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        self.tags.append((tag, d))


bad = 0
for f in BODIES:
    s = open(f, encoding="utf-8").read()
    p = Collector()
    p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for k in NEED:
            if not a.get(k, "").strip():
                missing.append((t, k))
    malformed = re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)
    rawq = re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[a-zA-Z]', s)
    amp = re.findall(r'&(?!amp;|nbsp;|quot;|#|middot;)', s)
    cjk = len(re.findall(r'[\u4e00-\u9fff]', s))
    n_h2 = len(re.findall(r'<h2 ', s))
    n_table = len(re.findall(r'<table>', s))
    n_callout = len(re.findall(r'class="callout"', s))
    n_cta = len(re.findall(r'class="cta-btn"', s))
    files_ok = len(re.findall(r'<li><a href="(?!index\.html)[a-z0-9-]+\.html"', s))
    print("== %s" % f)
    print("   标签 %d，带 data-zh %d，缺 en/ja/ko/fr/es %d %s" % (len(p.tags), len(dzh), len(missing), missing[:8]))
    print("   data-xx=\"\" = %d；属性后粘连字符 = %d；裸 & = %d %s" % (len(malformed), len(rawq), len(amp), amp[:5]))
    print("   h2=%d table=%d callout=%d cta=%d 相关文章内部链接=%d 中文字符≈%d" %
          (n_h2, n_table, n_callout, n_cta, files_ok, cjk))
    print("   起始标记: %s" % s[:32].replace("\n", "\\n"))
    print("   结束标记: %s" % s[-20:].replace("\n", "\\n"))
    bad += len(missing) + len(malformed) + len(rawq) + len(amp)

print("\n问题总数 = %d" % bad)
raise SystemExit(1 if bad else 0)
