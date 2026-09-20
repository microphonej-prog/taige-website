#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上正文抽查：确认新增页面的语言正文真的上线（不只看 title）。"""
import urllib.request

CHECK = [
    ("https://taigetag.com/es/blog/hang-tag-double-sided-printing.html", "Una etiqueta colgante a doble cara"),
    ("https://taigetag.com/fr/blog/hang-tag-double-sided-printing.html", "repérage"),
    ("https://taigetag.com/ja/blog/hang-tag-double-sided-printing.html", "裏写り"),
    ("https://taigetag.com/ko/blog/hang-tag-double-sided-printing.html", "비침"),
    ("https://taigetag.com/en/blog/hang-tag-double-sided-printing.html", "show-through"),
    ("https://taigetag.com/blog/hang-tag-double-sided-printing.html", "透印"),
    ("https://taigetag.com/es/blog/trim-quotation-comparison-guide.html", "presupuesto"),
    ("https://taigetag.com/fr/blog/trim-quotation-comparison-guide.html", "devis"),
    ("https://taigetag.com/ja/blog/trim-quotation-comparison-guide.html", "見積条件"),
    ("https://taigetag.com/ko/blog/trim-quotation-comparison-guide.html", "숨은 비용"),
    ("https://taigetag.com/en/blog/trim-quotation-comparison-guide.html", "amortise"),
    ("https://taigetag.com/blog/trim-quotation-comparison-guide.html", "口徑"),
    ("https://taigetag.com/blog/index.html", "hang-tag-double-sided-printing.html"),
    ("https://taigetag.com/en/blog/index.html", "trim-quotation-comparison-guide.html"),
    ("https://taigetag.com/ja/blog/index.html", "hang-tag-double-sided-printing.html"),
    ("https://taigetag.com/ko/blog/index.html", "hang-tag-double-sided-printing.html"),
    ("https://taigetag.com/fr/blog/index.html", "trim-quotation-comparison-guide.html"),
    ("https://taigetag.com/es/blog/index.html", "hang-tag-double-sided-printing.html"),
    ("https://taigetag.com/js/main.js", 'BUST_VERSION = "93"'),
]
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
    print("%s %-72s [%s] len=%d" % ("OK " if ok else "!! ", url.replace("https://taigetag.com", ""), kw, len(h)))
print("\n结论: 失败 %d / %d" % (bad, len(CHECK)))
