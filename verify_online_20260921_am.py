#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证（2026-09-21 上午批次）：六语页面正文、列表页卡片、sitemap、BUST_VERSION。"""
import urllib.request, random

CB = "?cb=%d" % random.randint(100000, 999999)

SLUGS = {
    "hanger-bag-guide.html": [
        ("blog/hanger-bag-guide.html", "掛衣袋"),
        ("en/blog/hanger-bag-guide.html", "hanger bag"),
        ("ja/blog/hanger-bag-guide.html", "ハンガー袋"),
        ("ko/blog/hanger-bag-guide.html", "걸이 비닐봉투"),
        ("fr/blog/hanger-bag-guide.html", "housses à suspendre"),
        ("es/blog/hanger-bag-guide.html", "bolsas colgantes"),
    ],
    "shrink-film-packaging-guide.html": [
        ("blog/shrink-film-packaging-guide.html", "收縮膜"),
        ("en/blog/shrink-film-packaging-guide.html", "shrink film"),
        ("ja/blog/shrink-film-packaging-guide.html", "シュリンク"),
        ("ko/blog/shrink-film-packaging-guide.html", "수축 필름"),
        ("fr/blog/shrink-film-packaging-guide.html", "film rétractable"),
        ("es/blog/shrink-film-packaging-guide.html", "film retráctil"),
    ],
}

CHECK = []
for slug, items in SLUGS.items():
    for path, kw in items:
        CHECK.append(("https://taigetag.com/" + path + CB, kw))

for pre in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
    for slug in SLUGS:
        CHECK.append(("https://taigetag.com/%sblog/index.html%s" % (pre, CB), slug))

for u in ["https://taigetag.com/blog/hanger-bag-guide.html",
          "https://taigetag.com/ja/blog/shrink-film-packaging-guide.html",
          "https://taigetag.com/ko/blog/hanger-bag-guide.html",
          "https://taigetag.com/es/blog/shrink-film-packaging-guide.html",
          "https://taigetag.com/en/blog/hanger-bag-guide.html",
          "https://taigetag.com/fr/blog/shrink-film-packaging-guide.html"]:
    CHECK.append(("https://taigetag.com/sitemap.xml" + CB, u.replace("https://taigetag.com", "https://taigetag.com")))

CHECK.append(("https://taigetag.com/js/main.js" + CB, 'BUST_VERSION = "96"'))

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
