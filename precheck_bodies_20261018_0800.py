#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""正文预检：六语属性完整性 / 软连字符 / 裸 & / 非中文语言里的汉字残留。"""
import re, sys
from html.parser import HTMLParser

LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
CJK = re.compile(r"[\u3400-\u9fff]")
KANA = re.compile(r"[\u3040-\u30ff]")
HANGUL = re.compile(r"[\uac00-\ud7af]")


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.problems = []
        self.count = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("br", "img", "meta", "link", "input", "hr"):
            return
        d = dict(attrs)
        if any(k.startswith("data-") for k in d) or tag in ("p", "h2", "h3", "li", "td", "th", "div", "a", "span"):
            self.count += 1
            missing = [l for l in LANGS if "data-" + l not in d]
            if missing:
                self.problems.append((tag, d.get("data-zh", "")[:40], missing))
            for l in LANGS:
                v = d.get("data-" + l)
                if v is None:
                    continue
                if "\u00ad" in v:
                    self.problems.append((tag, "SOFT-HYPHEN in " + l, [v[:60]]))
                if re.search(r"&(?![a-zA-Z#][a-zA-Z0-9]{0,8};)", v):
                    self.problems.append((tag, "RAW-AMP in " + l, [v[:60]]))
                if l in ("en", "fr", "es") and CJK.search(v):
                    self.problems.append((tag, "CJK residue in " + l, [v[:80]]))
                if l == "ko" and CJK.search(v):
                    self.problems.append((tag, "CJK residue in ko", [v[:80]]))
                if l == "ja" and CJK.search(v) and not (KANA.search(v) or CJK.search(v)):
                    self.problems.append((tag, "ja check", [v[:60]]))


for path in sys.argv[1:]:
    s = open(path, encoding="utf-8").read()
    p = P()
    p.feed(s)
    print("== %s  元素 %d  问题 %d" % (path, p.count, len(p.problems)))
    for x in p.problems[:25]:
        print("   !", x)
