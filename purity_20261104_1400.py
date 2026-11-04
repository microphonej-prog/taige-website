#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""语言纯净度：en/ja/ko/fr/es 版本正文与文本节点是否残留中文（data-zh 以外的中文字符）"""
import os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SLUGS = ["trims-ph-value-skin-safety.html", "garment-trims-sewing-equipment-guide.html"]
CJK = re.compile(r'[\u4e00-\u9fff]')
KANA = re.compile(r'[\u3040-\u30ff]')
HANGUL = re.compile(r'[\uac00-\ud7af]')

for lang in ["en", "ja", "ko", "fr", "es"]:
    for slug in SLUGS:
        p = "%s/blog/%s" % (lang, slug)
        s = open(p, encoding="utf-8").read()
        # 文本节点（>...<）里的字符
        texts = re.findall(r'>([^<>]{4,})<', s)
        cjk = sum(len(CJK.findall(t)) for t in texts)
        kana = sum(len(KANA.findall(t)) for t in texts)
        hangul = sum(len(HANGUL.findall(t)) for t in texts)
        # 只看 article-body 区
        i0 = s.find('class="article-body"')
        body = s[i0:]
        btexts = re.findall(r'>([^<>]{4,})<', body)
        bcjk = sum(len(CJK.findall(t)) for t in btexts)
        print("%-3s %-44s 全文CJK=%d 正文CJK=%d かな=%d 한글=%d" % (lang, slug, cjk, bcjk, kana, hangul))
        if lang == "en" and (cjk or kana or hangul):
            for t in btexts:
                if CJK.search(t) or KANA.search(t) or HANGUL.search(t):
                    print("   ! 残留:", t[:60])
        if lang in ("fr", "es") and (kana or hangul):
            print("   ! 非目标语言字符")
