#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抽检：各语言版本正文是否残留其它语言（法/西页面不得出现汉字；页面内不得残留多余 data-zh/en/ja/ko/fr/es）"""
import os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
SLUGS = ["trim-shipment-insurance-claims-guide.html", "conflict-minerals-trims-guide.html"]
bad = 0
for s in SLUGS:
    for l in ["en", "ja", "ko", "fr", "es"]:
        p = "%s/blog/%s" % (l, s)
        t = open(p, encoding="utf-8").read()
        body = t.split('class="article-body"', 1)[1].split("</section>", 1)[0]
        # 去掉 url/href 里的中文（不应有），统计正文汉字
        han = re.findall(r"[\u4e00-\u9fff]", body)
        n_attr = len(re.findall(r"data-(?:zh|en|ja|ko|fr|es)=", t))
        print("%-3s %-46s 正文汉字 %4d  残留语言属性 %d" % (l, s[:44], len(han), n_attr))
        if l in ("fr", "es") and han:
            print("     ⚠ 示例:", "".join(han[:20]))
            bad += 1
        if l == "en" and han:
            print("     ⚠ en 页面残留汉字:", "".join(han[:20]))
            bad += 1
        if n_attr:
            print("     ⚠ 残留 data-* 语言属性:", re.findall(r"data-(?:zh|en|ja|ko|fr|es)=", t)[:5])
            bad += 1
print()
print("异常项:", bad)
sys.exit(1 if bad else 0)
