#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-20 08:00 批次：正文属性齐备性 / 描述长度 / 字符集体检（v2）"""
import re, sys
from html.parser import HTMLParser

sys.path.insert(0, ".")
from daily_meta_20261020_0800 import ARTICLES

LANGS = ["zh", "en", "ja", "ko", "fr", "es"]


class Scanner(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.problems = []
        self.count = 0
        self.zh = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "data-zh" in d:
            self.count += 1
            miss = [l for l in LANGS if ("data-" + l) not in d]
            if miss:
                self.problems.append("<%s> 缺 %s: %s" % (tag, ",".join(miss), d["data-zh"][:40]))
            self.zh.append(d["data-zh"])
            allowed = set("data-" + l for l in LANGS) | {"class", "href"}
            for k in d:
                if k not in allowed:
                    self.problems.append("<%s> 属性异常键 %r（引号嵌套？）" % (tag, k))
        if tag not in ("br", "img", "meta", "link", "input", "hr"):
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()


for f in ("blog/_body_bom.html", "blog/_body_vlm.html", "blog/_body_reorder.html"):
    s0 = open(f, encoding="utf-8").read()
    zh_vals = re.findall(r'data-zh="([^"]*)"', s0)
    print("%-30s data-zh 汉字数=%d" % (f, len(re.findall(r"[\u4e00-\u9fff]", "".join(zh_vals)))))

for a in ARTICLES:
    s = open(a["body"], encoding="utf-8").read()
    print("\n== %s" % a["slug"])
    print("   desc 长度: zh=%d en=%d ja=%d ko=%d fr=%d es=%d"
          % tuple(len(a[k]) for k in ("desc_zh", "desc_en", "desc_ja", "desc_ko", "desc_fr", "desc_es")))
    p = Scanner()
    p.feed(s)
    zh_chars = len(re.findall(r"[\u4e00-\u9fff]", "".join(p.zh)))
    print("   带 data-zh 元素=%d  汉字=%d  未闭合=%s" % (p.count, zh_chars, p.stack))
    for x in p.problems[:20]:
        print("   !!", x)
    if not p.problems:
        print("   属性齐备 OK")
    cyr = set(re.findall(r"[\u0400-\u04FF]", s))
    if cyr:
        print("   !! 西里尔字符:", cyr)
    for lang in ("en", "fr", "es"):
        vals = re.findall(r'data-%s="([^"]*)"' % lang, s)
        bad = [v for v in vals if re.search(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]", v)]
        if bad:
            print("   !! %s 含中日韩文字 %d 处: %s" % (lang, len(bad), bad[0][:60]))
    raw_amp = re.findall(r"&(?!amp;|nbsp;|quot;|lt;|gt;|#)", s)
    if raw_amp:
        print("   !! 裸 & 数量:", len(raw_amp))
    for pat in ("au ordre", "Gelеz"):
        if pat in s:
            print("   ?? 可疑串 %r" % pat)
