#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-17 08:00 批次：正文文件预检（六语属性完整性 / ja-ko 简体字形误用 / fr-es 混入汉字 / 引号畸形）"""
import os, re, sys
from html.parser import HTMLParser
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from opencc import OpenCC

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
s2t = OpenCC("s2t")
FILES = ["blog/_body_gots.html", "blog/_body_recycle.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, {k.lower(): (v or "") for k, v in attrs}))


total_missing = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = P(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in LANGS:
            if not a.get("data-" + need, "").strip():
                missing.append((t, need))
    total_missing += len(missing)
    print("== %s" % f)
    print("   带 data-zh 的元素 %d 个；缺 en/ja/ko/fr/es 合计 %d %s" % (len(dzh), len(missing), missing[:8]))

    simp, han_fr, han_es, han_ko = [], [], [], []
    for tag, a in p.tags:
        for l in ("ja", "ko"):
            v = a.get("data-" + l)
            if not v:
                continue
            for ch in set(v):
                if "\u4e00" <= ch <= "\u9fff" and s2t.convert(ch) != ch:
                    simp.append((l, ch, s2t.convert(ch), v[:60]))
        for l, box in (("fr", han_fr), ("es", han_es)):
            v = a.get("data-" + l) or ""
            h = re.findall(r"[\u4e00-\u9fff]", v)
            if h:
                box.append((l, "".join(h[:6]), v[:60]))
        v = a.get("data-ko") or ""
        h = re.findall(r"[\u4e00-\u9fff]", v)
        if h:
            han_ko.append(("ko", "".join(h[:6]), v[:60]))

    print("   ja/ko 疑似简体字形: %d %s" % (len(simp), simp[:10]))
    print("   ko 汉字混入: %d %s" % (len(han_ko), han_ko[:5]))
    print("   fr 汉字混入: %d %s" % (len(han_fr), han_fr[:5]))
    print("   es 汉字混入: %d %s" % (len(han_es), han_es[:5]))
    print("   畸形 data-xx=\"\" : %d ; 属性值后裸字符: %d ; 裸 & : %d ; 属性内裸双引号: %d"
          % (len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)),
             len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s)),
             len([1 for t, a in p.tags for k, v in a.items() if k.startswith("data-") and '"' in v])))
    print("   段落数 p=%d h2=%d li=%d table=%d" %
          (len(re.findall(r"<p ", s)), len(re.findall(r"<h2 ", s)),
           len(re.findall(r"<li ", s)), len(re.findall(r"<table>", s))))

print("\n结论: 属性缺失总数 = %d" % total_missing)
raise SystemExit(1 if total_missing else 0)
