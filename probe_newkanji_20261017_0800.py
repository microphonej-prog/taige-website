#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""参考集比对：新增正文 data-ja / data-ko 中的汉字，是否出现在既有语料（blog/*.html 的 data-ja/ko）中。
    出现「从未用过的新字」时人工复核是否有中文混入。"""
import os, re, glob
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
NEW = ["blog/_body_gots.html", "blog/_body_recycle.html"]


class P(HTMLParser):
    def __init__(self, lang):
        super().__init__(convert_charrefs=False)
        self.lang = lang
        self.chars = set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        v = a.get("data-" + self.lang) or ""
        for ch in v:
            if "\u4e00" <= ch <= "\u9fff":
                self.chars.add(ch)


def collect(files, lang):
    p = P(lang)
    for f in files:
        p.feed(open(f, encoding="utf-8").read())
    return p.chars


ref_pool = sorted(set(glob.glob("blog/*.html")))
for lang in ("ja", "ko"):
    ref = collect(ref_pool, lang)
    new = collect(NEW, lang)
    fresh = sorted(new - ref)
    print("== %s：既有语料汉字 %d 个；新正文汉字 %d 个；其中的新字 %d 个" % (lang, len(ref), len(new), len(fresh)))
    print("   %s" % "".join(fresh))
