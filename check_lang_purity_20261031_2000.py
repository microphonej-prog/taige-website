#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""语言纯净度抽查：en/fr/es 可见文本不得含中日韩字符；ja/ko 不得含简体高频字"""
import re, urllib.request, ssl

CJK = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]")
SIMPLIFIED = set("褶皱贴纸标签织唛缝制发线颜电导术种类别图据标识让实际时间问题选择结构价质")
SLUGS = ["medical-ppe-garment-labeling-guide", "trademark-symbols-garment-labels"]
ctx = ssl.create_default_context()


def text_of(html_s):
    s = re.sub(r"<script.*?</script>", " ", html_s, flags=re.S)
    s = re.sub(r"<style.*?</style>", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"&[a-zA-Z#0-9]+;", " ", s)


for lang in ["en", "fr", "es", "ja", "ko"]:
    for slug in SLUGS:
        url = "https://taigetag.com/%s/blog/%s.html?lang=%s&v=1" % (lang, slug, lang)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=40, context=ctx) as r:
            raw = r.read().decode("utf-8", "replace")
        t = text_of(raw)
        cjk = CJK.findall(t)
        simpl = [c for c in t if c in SIMPLIFIED]
        title = re.search(r"<title>(.*?)</title>", raw, re.S).group(1)
        print("%-3s %-46s CJK=%-4d 简体=%-2d title=%s" % (lang, slug[:44], len(cjk), len(simpl), title[:56]))
        if lang in ("en", "fr", "es") and cjk:
            print("    CJK 样例:", "".join(cjk[:15]))
        if simpl:
            print("    简体样例:", "".join(simpl[:10]))
