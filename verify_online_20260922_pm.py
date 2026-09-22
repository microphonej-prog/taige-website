#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证（2026-09-22 下午批次）：六语正文、列表页卡片、sitemap、BUST_VERSION。"""
import urllib.request, random

CB = "?cb=%d" % random.randint(100000, 999999)

SLUGS = {
    "garment-trims-order-tracking-guide.html": [
        ("blog/garment-trims-order-tracking-guide.html", "服裝輔料跟單指南"),
        ("en/blog/garment-trims-order-tracking-guide.html", "Apparel Trims Order Tracking"),
        ("ja/blog/garment-trims-order-tracking-guide.html", "衣料副資材の受発注管理ガイド"),
        ("ko/blog/garment-trims-order-tracking-guide.html", "의류 부자재 수주 관리 가이드"),
        ("fr/blog/garment-trims-order-tracking-guide.html", "Suivi de commande d'accessoires"),
        ("es/blog/garment-trims-order-tracking-guide.html", "Seguimiento de pedidos de accesorios"),
    ],
    "hang-tag-ink-safety-guide.html": [
        ("blog/hang-tag-ink-safety-guide.html", "吊牌油墨安全指南"),
        ("en/blog/hang-tag-ink-safety-guide.html", "Hang Tag Ink Safety"),
        ("ja/blog/hang-tag-ink-safety-guide.html", "タグのインキ安全ガイド"),
        ("ko/blog/hang-tag-ink-safety-guide.html", "행택 잉크 안전 가이드"),
        ("fr/blog/hang-tag-ink-safety-guide.html", "Sécurité des encres d'étiquettes"),
        ("es/blog/hang-tag-ink-safety-guide.html", "Seguridad de la tinta en etiquetas"),
    ],
}

CHECK = []
for slug, items in SLUGS.items():
    for path, kw in items:
        CHECK.append(("https://taigetag.com/" + path + CB, kw))

for pre in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
    for slug in SLUGS:
        CHECK.append(("https://taigetag.com/%sblog/index.html%s" % (pre, CB), slug))

for u in ["https://taigetag.com/blog/garment-trims-order-tracking-guide.html",
          "https://taigetag.com/en/blog/garment-trims-order-tracking-guide.html",
          "https://taigetag.com/ja/blog/hang-tag-ink-safety-guide.html",
          "https://taigetag.com/ko/blog/hang-tag-ink-safety-guide.html",
          "https://taigetag.com/fr/blog/garment-trims-order-tracking-guide.html",
          "https://taigetag.com/es/blog/hang-tag-ink-safety-guide.html"]:
    CHECK.append(("https://taigetag.com/sitemap.xml" + CB, "<loc>%s</loc>" % u))

CHECK.append(("https://taigetag.com/js/main.js" + CB, 'BUST_VERSION = "100"'))

bad = 0
for url, kw in CHECK:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"})
        h = urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")
        ok = kw in h
    except Exception as e:
        ok, h = False, str(e)
    if not ok:
        bad += 1
    print("%s %-58s [%s] len=%d" % ("OK " if ok else "!! ", url.replace("https://taigetag.com", "")[:58], kw, len(h)))
print("\n结论: 失败 %d / %d" % (bad, len(CHECK)))
