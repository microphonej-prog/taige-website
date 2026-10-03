#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成页语言纯净度扫描：ja 不得含简体专用字，ko/fr/es 不得含汉字，ja 不得含谚文。"""
import re, sys

NEW = ["blog/zipper-selection-guide.html", "blog/fusible-interlining-guide.html"]
SIMPLIFIED_ONLY = "衬胶链织这们说认让过还为与门关龙组务词汇专鲜艳浊温剧价体质检齐单发设备选图区块点线级术结"


def body_of(path):
    s = open(path, encoding="utf-8").read()
    m0 = re.search(r'<section class="article-body">', s)
    m1 = re.search(r'</section>', s[m0.end():])
    return re.sub(r'<script.*?</script>', '', s[m0.end():m0.end() + m1.start()], flags=re.S)

bad = 0
for f in NEW:
    for lang, forbid in [("ja", None), ("ko", r"[\u4e00-\u9fff]"),
                         ("fr", r"[\u4e00-\u9fff]"), ("es", r"[\u4e00-\u9fff]")]:
        p = "%s/%s" % (lang, f)
        b = body_of(p)
        cjk = len(re.findall(r"[\u4e00-\u9fff]", b))
        hangul_ja = len(re.findall(r"[\uac00-\ud7af]", b)) if lang == "ja" else 0
        simp = [c for c in b if c in SIMPLIFIED_ONLY] if lang == "ja" else []
        flag = (lang in ("ko", "fr", "es") and cjk > 0) or (lang == "ja" and simp) or hangul_ja
        if flag:
            bad += 1
        print("  %-42s 汉字=%d 谚文(ja)=%d ja简体可疑=%s" % (p, cjk, hangul_ja, "".join(sorted(set(simp)))))
print("\n异常项 = %d" % bad)
sys.exit(1 if bad else 0)
