#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-03 上午批次：线上验证（无头 Chrome 六语 title/h1 + 线上 sitemap 12 个新 URL）"""
import re, subprocess, sys

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE = "https://taigetag.com"
ARTICLES = [
    ("leather-garment-trims-guide.html",
     {"zh": "皮革與仿皮服裝輔料指南", "en": "Leather Garment Trims Guide", "fr": "Guide des accessoires pour cuir",
      "es": "Guía de accesorios para cuero", "ja": "レザー・合皮衣料の副資材ガイド", "ko": "가죽·인조가죽 의류 부자재 가이드"}),
    ("childrenswear-trims-guide.html",
     {"zh": "童裝輔料選型指南", "en": "Childrenswear Trims Guide", "fr": "Guide des accessoires enfant",
      "es": "Guía de accesorios infantiles", "ja": "子供服の副資材ガイド", "ko": "아동복 부자재 가이드"}),
]
SEGS = {"zh": "blog/%s", "en": "en/blog/%s", "fr": "fr/blog/%s", "es": "es/blog/%s",
        "ja": "ja/blog/%s", "ko": "ko/blog/%s"}

print("== 1) 线上 sitemap ==")
tmp = r"C:\Users\micro\taige-website\_live_sitemap.xml"
subprocess.run(["curl", "-s", "--noproxy", "*", "-m", "60", "-o", tmp,
                "%s/sitemap.xml" % BASE], capture_output=True, text=True)
s = open(tmp, encoding="utf-8", errors="replace").read()
print("   sitemap 大小 %d 字节, <loc> %d" % (len(s), s.count("<loc>")))
missing = 0
for slug, _ in ARTICLES:
    for lang, seg in SEGS.items():
        u = "%s/%s" % (BASE, seg % slug)
        if "<loc>%s</loc>" % u not in s:
            print("   MISSING %s" % u)
            missing += 1
print("   12 个新 URL 缺失 %d" % missing)

print("== 2) 无头 Chrome 六语 title 渲染 ==")
fails = 0
for slug, expect in ARTICLES:
    for lang, seg in SEGS.items():
        url = "%s/%s?lang=%s&v=132" % (BASE, seg % slug, lang)
        p = subprocess.run([CHROME, "--headless=new", "--disable-gpu",
                            "--virtual-time-budget=12000", "--dump-dom", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        dom = p.stdout or ""
        m = re.search(r"<title[^>]*>(.*?)</title>", dom, re.S)
        title = (m.group(1).strip() if m else "NO-TITLE")
        ok = expect[lang] in title
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S)
        h1t = (h1.group(1).strip() if h1 else "NO-H1")
        desc = re.search(r'<meta name="description" content="([^"]*)"', dom)
        if not ok:
            fails += 1
        print("   %-6s %-36s %s | %s" % (lang, slug[:34], "OK " if ok else "FAIL", title[:56]))
        print("          h1: %s" % h1t[:64])
        print("          desc(%d): %s" % (len(desc.group(1)) if desc else -1,
                                          (desc.group(1)[:70] if desc else "NONE")))

print("\n结论: title 校验失败 %d / 12；sitemap 缺失 %d" % (fails, missing))
sys.exit(1 if (fails or missing) else 0)
