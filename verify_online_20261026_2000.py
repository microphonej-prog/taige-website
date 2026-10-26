#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上校验：headless Chrome 渲染六语 title/h1 + 抓取线上 sitemap 检查 12 个新 URL"""
import subprocess, re, os, sys, json, urllib.request, socket

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["apparel-trims-antibacterial-hygiene-packaging.html",
         "apparel-trims-static-dust-control.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
EXPECT_TITLE = {
 "apparel-trims-antibacterial-hygiene-packaging.html": {
   "zh": "抗菌輔料與衛生包裝指南",
   "en": "Antibacterial Trims and Hygiene Packaging",
   "ja": "抗菌副資材と衛生包装ガイド",
   "ko": "항균 부자재와 위생 포장 가이드",
   "fr": "Accessoires antibactériens et emballage hygiénique",
   "es": "Accesorios antibacterianos y embalaje higiénico"},
 "apparel-trims-static-dust-control.html": {
   "zh": "服裝輔料與包裝的靜電控制",
   "en": "Static Control in Garment Packaging",
   "ja": "衣料品包装の静電気対策",
   "ko": "의류 포장 정전기 대책",
   "fr": "Maîtrise de l'électricité statique",
   "es": "Control de la estática en embalaje textil"},
}

fail = []
for slug in SLUGS:
    for lang in LANGS:
        if lang == "zh":
            url = "https://taigetag.com/blog/%s?lang=zh&v=185" % slug
        else:
            url = "https://taigetag.com/%s/blog/%s?v=185" % (lang, slug)
        try:
            r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                                "--virtual-time-budget=12000", "--dump-dom", url],
                               capture_output=True, timeout=90)
            dom = r.stdout.decode("utf-8", "ignore")
        except Exception as e:
            fail.append("%s 渲染失败 %s" % (url, e))
            continue
        m = re.search(r"<title[^>]*>(.*?)</title>", dom, re.S)
        title = m.group(1).strip() if m else ""
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S)
        h1 = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else ""
        ok = EXPECT_TITLE[slug][lang] in title
        print("%s %-5s title=%s" % ("OK " if ok else "BAD", lang, title[:70]))
        if not ok:
            fail.append("%s title 不符: %s" % (url, title[:80]))
        if not h1:
            fail.append("%s h1 为空" % url)

# 线上 sitemap
try:
    req = urllib.request.Request("https://taigetag.com/sitemap.xml",
                                 headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"})
    sm = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "ignore")
    print("\n线上 sitemap 大小 %d 字节, <loc> %d" % (len(sm), sm.count("<loc>")))
    for slug in SLUGS:
        for u in ["https://taigetag.com/blog/%s" % slug] + \
                 ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS if l != "zh"]:
            hit = "<loc>%s</loc>" % u in sm
            print("  %s %s" % ("OK " if hit else "MISS", u))
            if not hit:
                fail.append("线上 sitemap 缺 %s" % u)
except Exception as e:
    fail.append("线上 sitemap 抓取失败: %s" % e)

print()
if fail:
    print("!!! 失败 %d 项" % len(fail))
    for f in fail:
        print("  -", f)
    sys.exit(1)
print("线上校验全部通过")
