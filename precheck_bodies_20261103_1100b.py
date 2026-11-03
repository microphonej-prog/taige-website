#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验两篇新正文文件的六语属性完整性（v2：只看带 data-* 的元素）。"""
from html.parser import HTMLParser

LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
FILES = ["blog/_body_metamerism.html", "blog/_body_curl.html"]
TEXT_TAGS = {"p", "h1", "h2", "h3", "li", "td", "th", "a", "span"}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.partial = []
        self.nodata = []
        self.ok = 0
        self.chars = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        has = [k for k in d if k.startswith("data-")]
        lang_has = [l for l in LANGS if ("data-" + l) in d]
        if has and len(lang_has) != 6:
            self.partial.append("%s 只有 %s" % (tag, ",".join(lang_has)))
        elif has:
            self.ok += 1
        if tag in TEXT_TAGS and not has:
            self.nodata.append(tag)
        if tag == "div" and ("callout" in (d.get("class") or "") or "cta-box" in (d.get("class") or "")):
            if len(lang_has) != 6:
                self.partial.append("div.%s 缺语言" % d.get("class"))


for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = P()
    p.feed(s)
    zh_chars = sum(1 for c in s if "\u4e00" <= c <= "\u9fff")
    print("== %s" % f)
    print("   六语齐全元素: %d   属性不全: %d %s" % (p.ok, len(p.partial), p.partial[:5]))
    print("   文本类元素无 data: %d %s" % (len(p.nodata), p.nodata[:8]))
    print("   中文字符数（含六语重复计一次）: %d" % zh_chars)
