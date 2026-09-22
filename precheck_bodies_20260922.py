#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-22 批次正文预检：六语属性完整性 / 引号畸形 / 表格列数 / data-zh 与文本一致性"""
import re, sys
from html.parser import HTMLParser

BODIES = ["blog/_body_russia.html", "blog/_body_claims.html"]
LANGS = ["data-en", "data-ja", "data-ko", "data-fr", "data-es"]


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.tags = []
        self.rows = []          # 每个 table 的行单元格数
        self.cur_table = None
        self.cur_row = None
        self.text_by_zh = {}    # (行号占位) 记录 data-zh → 文本
        self.cur = None

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        if tag == "section" and d.get("class", "").startswith("article-body"):
            self.in_body = True
            return
        if not self.in_body:
            return
        self.tags.append((tag, d))
        if tag == "table":
            self.cur_table = []
        elif tag == "tr" and self.cur_table is not None:
            self.cur_row = []
        elif tag in ("th", "td") and self.cur_row is not None:
            self.cur_row.append(d.get("data-zh", ""))
        if "data-zh" in d:
            self.cur = [d["data-zh"], []]

    def handle_data(self, data):
        if self.cur is not None:
            self.cur[1].append(data)

    def handle_endtag(self, tag):
        if tag in ("th", "td") and self.cur_row is not None:
            pass
        elif tag == "tr" and self.cur_table is not None:
            self.cur_table.append(len(self.cur_row or []))
            self.cur_row = None
        elif tag == "table" and self.cur_table is not None:
            self.rows.append(self.cur_table)
            self.cur_table = None
        if tag == "section" and self.in_body:
            self.in_body = False
        if self.cur is not None and tag not in ("br", "strong", "em", "b", "i", "a", "span"):
            zh, chunks = self.cur
            txt = "".join(chunks).strip()
            zh_plain = re.sub(r"<[^>]+>", "", zh).strip()
            if txt and txt != zh_plain:
                self.text_by_zh.setdefault(txt, zh_plain)
            self.cur = None


bad = 0
for f in BODIES:
    s = open(f, encoding="utf-8").read()
    p = Collector(); p.feed(s)
    zh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in zh:
        for need in LANGS:
            if not a.get(need, "").strip():
                missing.append((t, a.get("data-zh", "")[:14], need))
    print("== %s" % f)
    print("   标签 %d，带 data-zh 的 %d；缺 en/ja/ko/fr/es 的 %d %s"
          % (len(p.tags), len(zh), len(missing), missing[:6]))
    print("   data-xx=\"\" 畸形: %d ; 属性值后裸字符: %d ; 裸 & : %d"
          % (len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)),
             len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|lt;|gt;|#)', s))))
    print("   表格列数：%s" % p.rows)
    for r in p.rows:
        if len(set(r)) > 1:
            print("   !! 表格列数不一致: %s" % r)
            bad += 1
    for txt, zhv in p.text_by_zh.items():
        print("   !! 文本与 data-zh 不一致:\n      data-zh=%s\n      text   =%s" % (zhv[:60], txt[:60]))
        bad += 1
    if missing:
        bad += 1

# 中文占比粗检：日文属性里不应出现简体中文特有字（的/与/为/个 等）
for f in BODIES:
    s = open(f, encoding="utf-8").read()
    for attr in ("data-ja", "data-ko", "data-fr", "data-es"):
        vals = re.findall(r'%s="([^"]*)"' % attr, s)
        susp = [v for v in vals if re.search(r'[的一是了和与为个这样们]', v) and attr != "data-ja"]
        if susp:
            print("!! %s 的 %s 中出现疑似中文: %s" % (f, attr, susp[:2]))
            bad += 1
print("\n预检结论: %s" % ("通过" if bad == 0 else "发现 %d 个问题" % bad))
sys.exit(0 if bad == 0 else 1)
