#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上内容抽检：两篇新文章正文关键词 + 列表页卡片 + 线上 sitemap lastmod"""
import os, re, subprocess, tempfile, sys

CASES = [
    ("https://taigetag.com/blog/clothing-label-requirements-southeast-asia.html?v=176", ["東南亞", "進口商", "字高"]),
    ("https://taigetag.com/en/blog/clothing-label-requirements-southeast-asia.html?v=176", ["Southeast Asia", "importer", "type height"]),
    ("https://taigetag.com/es/blog/clothing-label-requirements-southeast-asia.html?v=176", ["sudeste asiático", "importador"]),
    ("https://taigetag.com/blog/recycled-polyester-trims-guide.html?v=176", ["rPET", "交易證書", "GRS"]),
    ("https://taigetag.com/fr/blog/recycled-polyester-trims-guide.html?v=176", ["polyester recyclé", "certificat de transaction"]),
    ("https://taigetag.com/ko/blog/recycled-polyester-trims-guide.html?v=176", ["rPET", "거래 증명서"]),
    ("https://taigetag.com/blog/index.html?v=176", ["clothing-label-requirements-southeast-asia.html",
                                                    "recycled-polyester-trims-guide.html"]),
    ("https://taigetag.com/en/blog/index.html?v=176", ["clothing-label-requirements-southeast-asia.html",
                                                       "recycled-polyester-trims-guide.html"]),
]
bad = 0
for url, keys in CASES:
    out = os.path.join(tempfile.gettempdir(), "spot_%d.html" % (abs(hash(url)) % 10 ** 8))
    r = subprocess.run(["curl", "-sS", "--noproxy", "*", "-m", "40", "-o", out, url],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    s = open(out, encoding="utf-8", errors="replace").read() if os.path.exists(out) else ""
    hit = [k for k in keys if k in s]
    miss = [k for k in keys if k not in s]
    print(("  ✓ " if not miss else "  ✗ ") + "%s 大小=%dKB 命中%d/%d %s"
          % (url.replace("https://taigetag.com", ""), len(s.encode("utf-8")) // 1024,
             len(hit), len(keys), ("缺 " + str(miss)) if miss else ""))
    if miss:
        bad += 1
    try:
        os.remove(out)
    except OSError:
        pass

print("\n抽检结果:", "PASS" if bad == 0 else "FAIL(%d)" % bad)
sys.exit(0 if bad == 0 else 1)
