#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-08 晚批次（20:00）正文文件预检：
① 每个带 data-zh 的元素是否齐全 data-en/ja/ko/fr/es
② 是否有空属性值 data-x=""
③ 属性值里是否混入裸 ASCII 双引号（会截断属性 / 移动端崩溃元凶）
④ 结构检查：section/container/相关文章/cta-box 是否成对
⑤ 中文正文字数统计
"""
import os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

BODIES = ["blog/_body_vacuum.html", "blog/_body_stone.html"]
WANT = ("data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es")


class C(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.n = 0
        self.miss = []

    def handle_starttag(self, tag, attrs):
        d = {}
        for k, v in attrs:
            d[k] = v
        if "data-zh" in d:
            self.n += 1
            m = [k for k in WANT if k not in d]
            if m:
                self.miss.append((tag, d["data-zh"][:40], m))

    handle_startendtag = handle_starttag


bad_total = 0
for b in BODIES:
    s = open(b, encoding="utf-8").read()
    print("=== %s (%d KB) ===" % (b, len(s.encode("utf-8")) // 1024))
    c = C()
    c.feed(s)
    print("  data-zh 元素 = %d ; 缺属性 = %d" % (c.n, len(c.miss)))
    for m in c.miss[:10]:
        print("    MISS", m)

    empty = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    print("  空属性值 = %d" % len(empty))

    # 属性值内混入裸双引号：形如 ="x"y"  → 统计每行 " 的奇偶
    odd = 0
    for i, line in enumerate(s.split("\n"), 1):
        if line.count('"') % 2:
            odd += 1
            if odd <= 5:
                print("    引号奇数行 %d: %s" % (i, line[:110]))
    print("  双引号奇数行 = %d" % odd)

    # 结构
    print("  section 开合: %d / %d" % (s.count('<section class="article-body">'), s.count("</section>")))
    print("  div 开合: %d / %d" % (s.count("<div"), s.count("</div>")))
    print("  table 开合: %d / %d" % (s.count("<table>"), s.count("</table>")))
    print("  cta-box = %d ; 相关文章 h2 = %d" % (s.count('class="cta-box"'), s.count("相关文章")))
    print("  <em>/<i> 残留 = %d" % (s.count("<em>") + s.count("<i>")))
    # 中文正文字数（data-zh 值 + 文本节点里的中文，粗略）
    zh = "".join(re.findall(r'data-zh="([^"]*)"', s))
    zh_han = len(re.findall(r"[\u4e00-\u9fff]", zh))
    print("  data-zh 汉字数 = %d" % zh_han)

    bad_total += len(c.miss) + len(empty) + odd

print("\n结论:", "全部通过" if bad_total == 0 else "有 %d 处异常" % bad_total)
sys.exit(1 if bad_total else 0)
