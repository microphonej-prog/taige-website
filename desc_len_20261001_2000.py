#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-01 20:00 批次：desc 长度体检 + JA/KO 残留复检（排除误报词 包装/作业 等合法日文汉字）"""
import re, sys
sys.path.insert(0, ".")
from daily_meta_20261001_2000 import ARTICLES

print("== desc 长度 ==")
for a in ARTICLES:
    print("  %-46s zh=%d字 en=%d字符 ja=%d ko=%d fr=%d es=%d"
          % (a["slug"], len(a["desc_zh"]), len(a["desc_en"]), len(a["desc_ja"]),
             len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))
    print("     title_zh=%d title_en=%d" % (len(a["title_zh"]), len(a["title_en"])))

print("\n== JA/KO 简体残留复检（排除合法日文词） ==")
LEGIT = ("包装", "作業", "資材", "表示", "製品", "品質", "天然", "自由", "飛行")
bad = 0
for f in ["blog/_body_effects.html", "blog/_body_rainwear.html"]:
    s = open(f, encoding="utf-8").read()
    for lang, words in (("ja", ("标签", "包装袋", "目录", "库存", "订单", "网站", "印刷厂", "制作", "进行")),):
        for v in re.findall(r'data-%s="([^"]*)"' % lang, s):
            for w in words:
                if w in v:
                    print("  JA 疑似残留 %s: %s" % (w, v[:80]))
                    bad += 1
    for lang in ("en", "fr", "es"):
        for v in re.findall(r'data-%s="([^"]*)"' % lang, s):
            cjk = re.findall(r'[\u4e00-\u9fff]', v)
            if cjk:
                print("  %s CJK 残留: %s" % (lang, v[:80]))
                bad += 1
print("复检问题 = %d" % bad)
