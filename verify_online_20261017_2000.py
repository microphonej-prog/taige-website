#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证：六语 × 2 篇页面 title/h1 渲染 + 线上 sitemap 是否含 12 个新 URL。"""
import os, re, sys, urllib.request, urllib.error, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["garment-label-configuration-guide.html", "apparel-trims-neutral-packaging.html"]
V = "168"

EXPECT = {
    "zh": {"garment-label-configuration-guide.html": "成衣標籤配置指南",
           "apparel-trims-neutral-packaging.html": "輔料中性包裝與多廠分貨指南"},
    "en": {"garment-label-configuration-guide.html": "Garment Label Configuration",
           "apparel-trims-neutral-packaging.html": "Neutral Packaging for Trims"},
    "ja": {"garment-label-configuration-guide.html": "衣料品ラベルの構成ガイド",
           "apparel-trims-neutral-packaging.html": "副資材の中性包装と複数工場への分納ガイド"},
    "ko": {"garment-label-configuration-guide.html": "의류 라벨 구성 가이드",
           "apparel-trims-neutral-packaging.html": "부자재 중립 포장과 다공장 분할 가이드"},
    "fr": {"garment-label-configuration-guide.html": "Configuration des étiquettes",
           "apparel-trims-neutral-packaging.html": "Emballage neutre des accessoires"},
    "es": {"garment-label-configuration-guide.html": "Configuración de etiquetas",
           "apparel-trims-neutral-packaging.html": "Embalaje neutro de accesorios"},
}

fails = []
print("== 1) 线上 DOM 渲染（headless Chrome，六语 × 2 篇，v=%s） ==" % V)
for lang, m in EXPECT.items():
    for slug, want in m.items():
        if lang == "zh":
            url = "https://taigetag.com/blog/%s?lang=zh&v=%s" % (slug, V)
        else:
            url = "https://taigetag.com/%s/blog/%s?lang=%s&v=%s" % (lang, slug, lang, V)
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=12000", "--dump-dom", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
        dom = r.stdout or ""
        title = (re.search(r"<title[^>]*>(.*?)</title>", dom, re.S) or [None, ""])[1].strip()
        h1 = (re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S) or [None, ""])[1].strip()
        ok_t, ok_h = want in title, want in h1
        print("  %-4s %-40s title_ok=%s h1_ok=%s" % (lang, slug[:38], ok_t, ok_h))
        if not (ok_t and ok_h):
            fails.append((url, title[:70], h1[:70]))
        if lang in ("en", "fr", "es"):
            body = re.search(r'<section class="article-body">(.*?)</section>', dom, re.S)
            cjk = len(re.findall(r"[\u4e00-\u9fff]", body.group(1))) if body else -1
            print("       正文汉字=%s" % cjk)
            if cjk != 0:
                fails.append((url, "正文汉字=%s" % cjk, ""))

print("\n== 2) 线上 sitemap ==")
req = urllib.request.Request("https://taigetag.com/sitemap.xml",
                             headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"})
sm = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
miss = []
for s in SLUGS:
    for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
        u = "https://taigetag.com/%s%s" % (pre, s)
        if "<loc>%s</loc>" % u not in sm:
            miss.append(u)
print("  线上 sitemap <loc> 总数=%d，缺失新 URL=%d %s" % (sm.count("<loc>"), len(miss), miss[:4]))
if miss:
    fails.append(("sitemap", "%d 个 URL 缺失" % len(miss), ""))

print("\n== 3) 线上页面状态码 ==")
for u in ["https://taigetag.com/blog/%s" % SLUGS[0],
          "https://taigetag.com/ja/blog/%s" % SLUGS[1],
          "https://taigetag.com/blog/index.html",
          "https://taigetag.com/js/main.js?v=4.2"]:
    try:
        code = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=45).getcode()
    except urllib.error.HTTPError as e:
        code = e.code
    print("  %-62s HTTP %s" % (u, code))
    if code != 200:
        fails.append((u, "HTTP %s" % code, ""))

print("\n结论: 失败项 %d" % len(fails))
for f in fails:
    print("  !!", f)
raise SystemExit(1 if fails else 0)
