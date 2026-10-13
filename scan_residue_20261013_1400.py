# -*- coding: utf-8 -*-
"""修正版残留检查：排除日文通用汉字与站点通用组件（assist 组件/微信），并对比既有文章基线"""
import re

NEW = ["blog/garment-embroidery-decoration-guide.html",
       "blog/animal-derived-material-certification-guide.html"]
BASE = ["blog/knitwear-sweater-trims-guide.html",           # 既有文章基线
        "en/blog/knitwear-sweater-trims-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
# 仅简体中文特有、日文与繁体均不使用的字
SIMP_ONLY = "这个们为说时应发进对开还没经过样类录签纸张关现价购标书单双"


def analyze(path):
    s = open(path, encoding="utf-8").read()
    body = s[s.index("<body"):]
    # 去掉 assist 组件（站点通用，各语言页都是繁体中文）
    body2 = re.sub(r'<div class="assist-.*?</div>', '', body, flags=re.S)
    body2 = re.sub(r'<button[^>]*assist[^>]*>.*?</button>', '', body2, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', body2)
    cjk = re.findall(r'[\u4e00-\u9fff]', txt)
    simp = [c for c in txt if c in SIMP_ONLY]
    return len(cjk), "".join(cjk), len(simp), "".join(simp)


print("=== 基线（既有已上线文章，同语言）===")
for p in BASE:
    n, chars, ns, schars = analyze(p)
    print("  %-52s CJK=%-5d 简体=%d  %s" % (p, n, ns, schars))
    print("      CJK样本: %s" % chars[:60])

print("=== 本批次新文章 ===")
for slug in NEW:
    for lang in LANGS:
        p = "%s/blog/%s" % (lang, slug)
        n, chars, ns, schars = analyze(p)
        print("  %-58s CJK=%-5d 简体=%-3d %s" % (p, n, ns, schars))
        if lang == "ja":
            # 定位残留简体字上下文
            s = open(p, encoding="utf-8").read()
            for c in set(schars):
                for m in list(re.finditer(c, s))[:3]:
                    print("       ja 残留 %s ctx: %s" % (c, repr(s[max(0, m.start() - 25):m.end() + 25])))
