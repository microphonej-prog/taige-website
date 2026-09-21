#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证（2026-09-21 晚间批次）：六语正文、列表页卡片、sitemap、BUST_VERSION。"""
import urllib.request, random

CB = "?cb=%d" % random.randint(100000, 999999)

SLUGS = {
    "clothing-label-compliance-saudi-arabia.html": [
        ("blog/clothing-label-compliance-saudi-arabia.html", "阿拉伯語"),
        ("en/blog/clothing-label-compliance-saudi-arabia.html", "Arabic"),
        ("ja/blog/clothing-label-compliance-saudi-arabia.html", "アラビア語"),
        ("ko/blog/clothing-label-compliance-saudi-arabia.html", "아랍어"),
        ("fr/blog/clothing-label-compliance-saudi-arabia.html", "arabe"),
        ("es/blog/clothing-label-compliance-saudi-arabia.html", "árabe"),
    ],
    "clothing-label-compliance-turkey.html": [
        ("blog/clothing-label-compliance-turkey.html", "土耳其語"),
        ("en/blog/clothing-label-compliance-turkey.html", "Turkish"),
        ("ja/blog/clothing-label-compliance-turkey.html", "トルコ語"),
        ("ko/blog/clothing-label-compliance-turkey.html", "터키어"),
        ("fr/blog/clothing-label-compliance-turkey.html", "turc"),
        ("es/blog/clothing-label-compliance-turkey.html", "turco"),
    ],
}

CHECK = []
for slug, items in SLUGS.items():
    for path, kw in items:
        CHECK.append(("https://taigetag.com/" + path + CB, kw))

for pre in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
    for slug in SLUGS:
        CHECK.append(("https://taigetag.com/%sblog/index.html%s" % (pre, CB), slug))

for u in ["https://taigetag.com/blog/clothing-label-compliance-saudi-arabia.html",
          "https://taigetag.com/en/blog/clothing-label-compliance-saudi-arabia.html",
          "https://taigetag.com/ja/blog/clothing-label-compliance-turkey.html",
          "https://taigetag.com/ko/blog/clothing-label-compliance-saudi-arabia.html",
          "https://taigetag.com/fr/blog/clothing-label-compliance-turkey.html",
          "https://taigetag.com/es/blog/clothing-label-compliance-saudi-arabia.html"]:
    CHECK.append(("https://taigetag.com/sitemap.xml" + CB, "<loc>%s</loc>" % u))

CHECK.append(("https://taigetag.com/js/main.js" + CB, 'BUST_VERSION = "98"'))

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
