#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""语言纯净度检查：fr/es 页可见文本不得含中日韩汉字；ja/ko 页不得含简体高频字"""
import re, os

SLUGS = ["tyvek-washable-paper-hang-tag-guide.html", "garment-label-sewing-defect-troubleshooting.html"]
CJK = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]")
SIMPLIFIED = set("褶皱贴纸标签织唛缝制发线颜电导术种类别图据标识让实际时间问题选择结构价线质")


def visible_text(path):
    s = open(path, encoding="utf-8").read()
    s = re.sub(r"<script.*?</script>", " ", s, flags=re.S)
    s = re.sub(r"<style.*?</style>", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"&[a-z#0-9]+;", " ", s)
    return s


for lang in ["en", "fr", "es", "ja", "ko"]:
    for slug in SLUGS:
        p = "%s/blog/%s" % (lang, slug)
        t = visible_text(p)
        cjk = CJK.findall(t)
        simpl = [c for c in t if c in SIMPLIFIED]
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", open(p, encoding="utf-8").read(), re.S).group(1).strip()
        print("%-3s %-46s CJK可见字符=%-4d 简体高频字=%-2d h1=%s" %
              (lang, slug[:44], len(cjk), len(simpl), h1[:60]))
        if cjk and lang in ("en", "fr", "es"):
            print("     样例:", "".join(cjk[:20]))
        if simpl:
            print("     简体样例:", "".join(simpl[:12]))
