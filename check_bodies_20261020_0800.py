#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-20 08:00 批次：正文属性齐备性 / 描述长度 / 字符集体检"""
import re, sys
from html.parser import HTMLParser

sys.path.insert(0, ".")
from daily_meta_20261020_0800 import ARTICLES

LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
TAGS_NEED = {"p", "h1", "h2", "h3", "li", "td", "th", "div", "a", "span", "strong", "em"}


class Scanner(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.problems = []
        self.count = 0
        self.zh_text = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in TAGS_NEED and ("data-zh" in d or tag in ("p", "h2", "h3", "li", "td", "th")):
            if tag in TAGS_NEED:
                self.count += 1
                miss = [l for l in LANGS if ("data-" + l) not in d]
                if miss:
                    self.problems.append("%s 缺 %s : %s" % (tag, ",".join(miss), (d.get("data-zh") or "")[:40]))
            if "data-zh" in d:
                self.zh_text.append(d["data-zh"])
        if tag not in ("br", "img", "meta", "link", "input", "hr"):
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()


for a in ARTICLES:
    s = open(a["body"], encoding="utf-8").read()
    print("== %s" % a["slug"])
    print("   desc 长度: zh=%d en=%d ja=%d ko=%d fr=%d es=%d"
          % tuple(len(a[k]) for k in ("desc_zh", "desc_en", "desc_ja", "desc_ko", "desc_fr", "desc_es")))
    print("   title 长度: zh=%d en=%d" % (len(a["title_zh"]), len(a["title_en"])))
    p = Scanner()
    p.feed(s)
    zh_chars = len(re.findall(r"[\u4e00-\u9fff]", "".join(re.findall(r'data-zh="([^"]*)"', s))))
    print("   元素数=%d  data-zh 汉字数=%d  未闭合栈=%s" % (p.count, zh_chars, p.stack))
    if p.problems:
        print("   !! 属性缺失 %d 处:" % len(p.problems))
        for x in p.problems[:20]:
            print("      -", x)
    # 字符集体检
    cyr = re.findall(r"[\u0400-\u04FF]", s)
    if cyr:
        print("   !! 西里尔字符:", set(cyr))
    for lang in ("en", "fr", "es"):
        vals = re.findall(r'data-%s="([^"]*)"' % lang, s)
        bad = [v for v in vals if re.search(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]", v)]
        if bad:
            print("   !! %s 属性含中日韩文字 %d 处，例: %s" % (lang, len(bad), bad[0][:60]))
    # 裸 & 检查（应全部为 &amp;）
    raw_amp = re.findall(r"&(?!amp;|nbsp;|quot;|lt;|gt;|#)", s)
    if raw_amp:
        print("   !! 裸 & 数量:", len(raw_amp))
    # 法语常见漏字
    for pat in ("au ordre", "Gelеz", "  "):
        if pat in s:
            print("   ?? 可疑串 %r 出现 %d 次" % (pat, s.count(pat)))
    print("   文件大小 %d KB" % (len(s.encode("utf-8")) // 1024))
