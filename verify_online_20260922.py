#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证（2026-09-22 上午批次）：六语正文、列表页卡片、sitemap、BUST_VERSION。"""
import urllib.request, random

CB = "?cb=%d" % random.randint(100000, 999999)

SLUGS = {
    "clothing-label-compliance-russia.html": [
        ("blog/clothing-label-compliance-russia.html", "俄羅斯服裝標籤合規指南"),
        ("en/blog/clothing-label-compliance-russia.html", "Russia Clothing Label Requirements"),
        ("ja/blog/clothing-label-compliance-russia.html", "ロシアの衣料ラベル規制ガイド"),
        ("ko/blog/clothing-label-compliance-russia.html", "러시아 의류 라벨 규정 가이드"),
        ("fr/blog/clothing-label-compliance-russia.html", "Étiquetage des vêtements en Russie"),
        ("es/blog/clothing-label-compliance-russia.html", "Etiquetado de ropa en Rusia"),
    ],
    "garment-trims-claims-liability-guide.html": [
        ("blog/garment-trims-claims-liability-guide.html", "服裝輔料質量索賠指南"),
        ("en/blog/garment-trims-claims-liability-guide.html", "Apparel Trims Quality Claims"),
        ("ja/blog/garment-trims-claims-liability-guide.html", "品質クレームガイド"),
        ("ko/blog/garment-trims-claims-liability-guide.html", "품질 클레임 가이드"),
        ("fr/blog/garment-trims-claims-liability-guide.html", "Réclamations qualité sur les accessoires"),
        ("es/blog/garment-trims-claims-liability-guide.html", "Reclamaciones de calidad en accesorios"),
    ],
}

CHECK = []
for slug, items in SLUGS.items():
    for path, kw in items:
        CHECK.append(("https://taigetag.com/" + path + CB, kw))

for pre in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
    for slug in SLUGS:
        CHECK.append(("https://taigetag.com/%sblog/index.html%s" % (pre, CB), slug))

for u in ["https://taigetag.com/blog/clothing-label-compliance-russia.html",
          "https://taigetag.com/en/blog/clothing-label-compliance-russia.html",
          "https://taigetag.com/ja/blog/garment-trims-claims-liability-guide.html",
          "https://taigetag.com/ko/blog/garment-trims-claims-liability-guide.html",
          "https://taigetag.com/fr/blog/clothing-label-compliance-russia.html",
          "https://taigetag.com/es/blog/garment-trims-claims-liability-guide.html"]:
    CHECK.append(("https://taigetag.com/sitemap.xml" + CB, "<loc>%s</loc>" % u))

CHECK.append(("https://taigetag.com/js/main.js" + CB, 'BUST_VERSION = "99"'))

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
