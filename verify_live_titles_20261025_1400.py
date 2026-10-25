#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""解析线上 headless Chrome DOM，验证六语 title/h1 渲染"""
import re, os, glob

SLUGS = ["tyvek-washable-paper-hang-tag-guide", "garment-label-sewing-defect-troubleshooting"]
NAMES = {
    "zh": "杜邦紙與水洗牛皮紙吊牌指南", "en": "Tyvek and Washable Kraft Paper Hang Tags",
    "ja": "タイベックとウォッシャブルクラフト紙", "ko": "타이벡과 워셔블 크라프트지",
    "fr": "Étiquettes en Tyvek", "es": "Colgantes de Tyvek",
}
NAMES2 = {
    "zh": "服裝標籤車縫缺陷排查", "en": "Label Sewing Defects",
    "ja": "衣料ラベル縫製の不良対策", "ko": "의류 라벨 봉제 불량 대책",
    "fr": "Défauts de couture des étiquettes", "es": "Defectos de costura en etiquetas",
}

ok = True
for slug in SLUGS:
    for lang in ["zh", "en", "ja", "ko", "fr", "es"]:
        p = "live_dom/%s_%s.html" % (lang, slug)
        if not os.path.exists(p):
            print("MISSING", p)
            ok = False
            continue
        s = open(p, encoding="utf-8", errors="replace").read()
        t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
        h = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
        t = re.sub(r"\s+", " ", t.group(1)).strip() if t else "NO-TITLE"
        h = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", h.group(1))).strip() if h else "NO-H1"
        exp = NAMES[lang] if slug.startswith("tyvek") else NAMES2[lang]
        t_ok = exp in t
        h_ok = exp in h
        if not (t_ok and h_ok):
            ok = False
        print("%-3s %-46s title=%s h1=%s" % (lang, slug[:44], "OK" if t_ok else "FAIL", "OK" if h_ok else "FAIL"))
        print("     T:", t[:110])
        print("     H:", h[:110])

print("\n线上六语渲染:", "全部通过" if ok else "有失败")
