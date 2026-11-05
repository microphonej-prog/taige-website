#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""语言版渲染校验：CJK 残留 / kana / hangul / data-* 残留。"""
import re

SLUGS = ["clothing-label-compliance-poland.html", "clothing-label-compliance-portugal.html"]
CJK = re.compile(r"[\u4e00-\u9fff]")
KANA = re.compile(r"[\u3040-\u30ff]")
HANGUL = re.compile(r"[\uac00-\ud7af]")

for slug in SLUGS:
    for lang in ["en", "ja", "ko", "fr", "es"]:
        p = "%s/blog/%s" % (lang, slug)
        s = open(p, encoding="utf-8").read()
        body = s[s.index('<section class="article-body">'):s.index("</main>")]
        cjk = len(CJK.findall(body))
        kana = len(KANA.findall(body))
        han = len(HANGUL.findall(body))
        leak = len(re.findall(r"data-(?:zh|en|ja|ko|fr|es)=", s))
        tds = s.count("<td")
        print("%-6s %-38s CJK=%-4d kana=%-4d hangul=%-4d data残留=%-2d td=%d"
              % (lang, slug[:38], cjk, kana, han, leak, tds))
