#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证（2026-10-19 08:00 批次）：六语 × 2 篇 title/h1 渲染 + 线上 sitemap 12 URL + 列表页卡片 + HTTP 状态。
title 与 h1 按设计不同文（h1 更完整），分别断言。"""
import os, re, subprocess, sys, urllib.request, urllib.error

os.chdir(os.path.dirname(os.path.abspath(__file__)))

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
B1 = "garment-trims-bom-consumption-guide.html"
B2 = "apparel-trims-price-adjustment-guide.html"
V = "172"

EXPECT = {
    "zh": {B1: ("服裝輔料單耗覈算指南", "服裝輔料單耗覈算指南"),
           B2: ("輔料報價爲什麼會變", "輔料報價爲什麼會變")},
    "en": {B1: ("Trim Consumption and BOM Costing", "Garment Trim Consumption and BOM Costing"),
           B2: ("Why Trim Prices Change", "Why Trim Quotations Change")},
    "ja": {B1: ("衣料副資材の単耗計算ガイド", "衣料副資材の単耗計算ガイド"),
           B2: ("副資材の価格が変わる理由", "副資材の価格が変わる理由")},
    "ko": {B1: ("의류 부자재 소요량 산출 가이드", "의류 부자재 소요량 산출 가이드"),
           B2: ("부자재 가격이 변하는 이유", "부자재 가격이 변하는 이유")},
    "fr": {B1: ("Consommation d'accessoires et calcul BOM", "Consommation d'accessoires et calcul BOM"),
           B2: ("Pourquoi le prix des accessoires change", "Pourquoi un devis d'accessoires change")},
    "es": {B1: ("Consumo de accesorios y cálculo BOM", "Consumo de accesorios y cálculo BOM"),
           B2: ("Por qué cambia el precio de los accesorios", "Por qué cambia un presupuesto de accesorios")},
}

fails = []
print("== 1) 线上 DOM 渲染（六语 × 2 篇，v=%s） ==" % V)
for lang, m in EXPECT.items():
    for slug, (wt, wh) in m.items():
        if lang == "zh":
            url = "https://taigetag.com/blog/%s?lang=zh&v=%s&nc=0800b" % (slug, V)
        else:
            url = "https://taigetag.com/%s/blog/%s?lang=%s&v=%s&nc=0800b" % (lang, slug, lang, V)
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=12000", "--dump-dom", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=150)
        dom = r.stdout or ""
        title = (re.search(r"<title[^>]*>(.*?)</title>", dom, re.S) or [None, ""])[1].strip()
        h1 = (re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S) or [None, ""])[1].strip()
        ok_t, ok_h = wt in title, wh in h1
        body = re.search(r'<section class="article-body">(.*?)</section>', dom, re.S)
        blen = len(re.sub(r"<[^>]+>", " ", body.group(1))) if body else -1
        print("  %-3s %-46s title_ok=%s h1_ok=%s body=%d" % (lang, slug[:44], ok_t, ok_h, blen))
        if not (ok_t and ok_h):
            fails.append((url, title[:70], h1[:70]))
        if body is None or blen < 1200:
            fails.append((url, "正文渲染异常 body=%d" % blen, ""))
        if lang in ("en", "fr", "es") and body:
            cjk = len(re.findall(r"[\u4e00-\u9fff]", body.group(1)))
            if cjk != 0:
                fails.append((url, "正文汉字=%s" % cjk, ""))

print("\n== 2) 线上 sitemap ==")
req = urllib.request.Request("https://taigetag.com/sitemap.xml",
                             headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"})
sm = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
miss = []
for s in (B1, B2):
    for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
        u = "https://taigetag.com/%s%s" % (pre, s)
        if "<loc>%s</loc>" % u not in sm:
            miss.append(u)
print("  线上 <loc> 总数=%d，缺失新 URL=%d %s" % (sm.count("<loc>"), len(miss), miss[:4]))
if miss:
    fails.append(("sitemap", "%d 个 URL 缺失" % len(miss), ""))

print("\n== 3) 线上列表页卡片 + 状态码 ==")
idx = urllib.request.urlopen(urllib.request.Request(
    "https://taigetag.com/blog/index.html", headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"}),
    timeout=45).read().decode("utf-8", "replace")
for s in (B1, B2):
    n = idx.count('href="%s"' % s)
    print("  卡片 %-46s %d" % (s, n))
    if n < 1:
        fails.append(("index", s, ""))
for u in ["https://taigetag.com/blog/%s" % B1,
          "https://taigetag.com/ja/blog/%s" % B2,
          "https://taigetag.com/js/main.js?v=%s" % V]:
    try:
        code = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}),
                                      timeout=45).getcode()
    except urllib.error.HTTPError as e:
        code = e.code
    print("  %-64s HTTP %s" % (u, code))
    if code != 200:
        fails.append((u, "HTTP %s" % code, ""))

print("\n结论: 失败项 %d" % len(fails))
for f in fails:
    print("  !!", f)
sys.exit(1 if fails else 0)
