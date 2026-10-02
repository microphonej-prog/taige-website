#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-02 早上批次：线上验证（无头 Chrome 六语 title/h1 + 线上 sitemap 12 个新 URL）"""
import re, subprocess, sys

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE = "https://taigetag.com"
ARTICLES = [
    ("school-uniform-trims-label-guide.html",
     {"zh": "校服與幼兒園服裝標籤指南", "en": "School Uniform Label Guide", "fr": "uniformes scolaires",
      "es": "uniformes escolares", "ja": "学校制服のラベルガイド", "ko": "교복 라벨 가이드"}),
    ("maternity-nursing-wear-trims-guide.html",
     {"zh": "孕婦裝與哺乳裝輔料指南", "en": "Nursing Wear Trims", "fr": "maternité et allaitement",
      "es": "maternidad y lactancia", "ja": "マタニティ・授乳服の副資材ガイド", "ko": "임부복·수유복 부자재 가이드"}),
]
SEGS = {"zh": "blog/%s", "en": "en/blog/%s", "fr": "fr/blog/%s", "es": "es/blog/%s",
        "ja": "ja/blog/%s", "ko": "ko/blog/%s"}

print("== 1) 线上 sitemap ==")
tmp = r"C:\Users\micro\taige-website\_live_sitemap.xml"
r = subprocess.run(["curl", "-s", "--noproxy", "*", "-m", "60", "-o", tmp,
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
        url = "%s/%s?lang=%s&v=128" % (BASE, seg % slug, lang)
        p = subprocess.run([CHROME, "--headless=new", "--disable-gpu",
                            "--virtual-time-budget=12000", "--dump-dom", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        dom = p.stdout or ""
        m = re.search(r"<title[^>]*>(.*?)</title>", dom, re.S)
        title = (m.group(1).strip() if m else "NO-TITLE")
        ok = expect[lang] in title
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S)
        h1t = (h1.group(1).strip() if h1 else "NO-H1")
        if not ok:
            fails += 1
        print("   %-6s %-42s %s | %s" % (lang, slug[:40], "OK " if ok else "FAIL", title[:52]))
        print("          h1: %s" % h1t[:60])

print("\n结论: title 校验失败 %d / 12；sitemap 缺失 %d" % (fails, missing))
sys.exit(1 if (fails or missing) else 0)
