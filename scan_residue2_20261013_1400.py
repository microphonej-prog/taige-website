# -*- coding: utf-8 -*-
"""残留检查（修正版）：剔除站点通用 assist 组件文案后，统计正文 CJK 与简体残留"""
import re

NEW = ["garment-embroidery-decoration-guide.html",
       "animal-derived-material-certification-guide.html"]
BASE = ["knitwear-sweater-trims-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
CHROME = ["微信", "在線", "發送"]           # 站点通用 assist 组件，六语页一律繁体中文
SIMP_ONLY = "这个们为说时应发进对开还没经过样类录签纸张关现价购单双"


def analyze(path):
    s = open(path, encoding="utf-8").read()
    body = s[s.index("<body"):]
    txt = re.sub(r'<[^>]+>', ' ', body)
    for c in CHROME:
        txt = txt.replace(c, '')
    cjk = re.findall(r'[\u4e00-\u9fff]', txt)
    simp = [c for c in txt if c in SIMP_ONLY]
    return len(cjk), "".join(cjk), len(simp), "".join(sorted(set(simp)))


print("=== 基线：既有已上线文章（同语言，剔除 assist 组件后）===")
for lang in ["zh"] + LANGS:
    p = ("blog/" if lang == "zh" else "%s/blog/" % lang) + BASE[0]
    n, chars, ns, schars = analyze(p)
    print("  %-52s 正文CJK=%-5d 简体=%-3d %s" % (p, n, ns, schars))

print("=== 本次新文章 ===")
bad = 0
for slug in NEW:
    for lang in ["zh"] + LANGS:
        p = ("blog/" if lang == "zh" else "%s/blog/" % lang) + slug
        n, chars, ns, schars = analyze(p)
        tag = ""
        if lang in ("en", "fr", "es", "ko") and n:
            tag = "  <== 正文有 CJK 残留！"
            bad += 1
        if ns:
            tag = "  <== 简体残留！"
            bad += 1
        print("  %-58s 正文CJK=%-5d 简体=%-3d %s%s" % (p, n, ns, schars, tag))

print()
print("结论：正文残留问题数 =", bad)
