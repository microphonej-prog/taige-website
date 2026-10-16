#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-16 20:00 批次正文预检（只读）：
1) .article-body 内每个带 data-* 的元素是否六语齐全（用 HTMLParser 逐属性判断，避免正则截断误报）
2) 简体字形是否误入 ja/ko/fr/es 属性值（黑名单提示）
3) 是否为空属性值
用法: F:/hermes/venvs/tools/Scripts/python.exe precheck_bodies_20261016_2000.py
"""
import os, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
SIMPLIFIED = set("们这说过买卖织标辅客户么样发货订单证书险赔偿义务规则约简体厂验银贸运输费报价税额统码编译级线纸张胶类见证护归类确认为动区医调监测设备额纯净额")
# 只保留真正“简体独有”的字，避免误报（這些字在繁体/日韩文本中不会出现）
SIMPLIFIED = set("们这说过买卖织标辅么样发货订单证书险赔偿义务规则约简体厂验银贸运输费报价税额统码编译级线纸张胶类见证护归类确认为动区")

FILES = ["blog/_body_transins.html", "blog/_body_minerals.html"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.bad = []
        self.empty = []
        self.simpl = []
        self.count = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in ("meta", "link", "br", "img", "hr"):
            return
        have = [l for l in LANGS if ("data-%s" % l) in d]
        if have:
            self.count += 1
            missing = [l for l in LANGS if l not in have]
            if missing:
                self.bad.append((tag, have, missing, (d.get("data-zh") or "")[:40]))
            for l in have:
                if d["data-%s" % l].strip() == "":
                    self.empty.append((tag, l))
            for l in ("ja", "ko", "fr", "es"):
                if l in d:
                    hit = sorted(set(d["data-%s" % l]) & SIMPLIFIED)
                    if hit:
                        self.simpl.append((tag, l, "".join(hit), d["data-%s" % l][:60]))


html = open("blog/_body_transins.html", encoding="utf-8").read() + \
       open("blog/_body_minerals.html", encoding="utf-8").read()
p = P()
p.feed(html)
print("带 data-* 的元素总数:", p.count)
print("缺语言的元素:", len(p.bad))
for t in p.bad[:20]:
    print("   ", t)
print("空属性值:", len(p.empty), p.empty[:10])
print("ja/ko/fr/es 中出现简体字形:", len(p.simpl))
for t in p.simpl[:30]:
    print("   ", t)

# 引号安全：属性值内不应出现裸 ASCII 双引号（解析后 check）
import re
raw = open("blog/_body_transins.html", encoding="utf-8").read()
raw += open("blog/_body_minerals.html", encoding="utf-8").read()
susp = re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"\n]*"[^ \n>]*="', raw)
print("疑似引号错位片段:", len(susp), susp[:5])
print("含未转义 & 的片段:", len(re.findall(r'&(?!amp;|nbsp;|quot;|lt;|gt;|#)', raw)))
