#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-24 下午批次：语言页中文残留扫描（zh 兜底检测）
- en/fr/es：正文中不应出现任何连续汉字
- ja：汉字是正常书写体系，只检查简体独有字形（纸样说签码烫尔东们这为）
- ko：正文中不应出现汉字/假名
"""
import re, sys

SLUGS = ["garment-packaging-transit-testing.html", "shirt-blouse-trims-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
ALLOW = ("泰閣包裝", "東莞泰閣包裝製品有限公司", "虎門鎮", "東莞市", "廣東省", "泰閣包装")
SIMP_ONLY = re.compile(r'[纸样说签码烫尔东们这为]')
CJK_KANA = re.compile(r'[\u4e00-\u9fff\u3040-\u30ff]')

bad = 0
for slug in SLUGS:
    for lang in LANGS:
        p = "%s/blog/%s" % (lang, slug)
        s = open(p, encoding="utf-8").read()
        body = s[s.index('<section class="article-body">'):s.index('</main>')]
        if lang == "ja":
            hits = [h for h in SIMP_ONLY.findall(body)]
        elif lang == "ko":
            hits = [h for h in CJK_KANA.findall(body)]
        else:
            hits = [h for h in re.findall(r'[\u4e00-\u9fff]{2,}', body) if h not in ALLOW]
        print("%-46s 残留: %d %s" % (p, len(hits), hits[:8]))
        bad += len(hits)
print("残留总数 = %d" % bad)
sys.exit(1 if bad else 0)
