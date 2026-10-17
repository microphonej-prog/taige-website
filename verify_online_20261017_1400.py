#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证：六语 × 2 篇页面 title/h1 渲染 + 线上 sitemap 是否含 12 个新 URL。"""
import os, re, sys, json, subprocess, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["saree-ethnic-wear-trims-guide.html", "garment-trims-trade-show-sourcing-guide.html"]
EXPECT = {
    "zh": {
        "saree-ethnic-wear-trims-guide.html": "紗麗與南亞民族服飾輔料指南",
        "garment-trims-trade-show-sourcing-guide.html": "服裝輔料展會採購指南",
    },
    "en": {
        "saree-ethnic-wear-trims-guide.html": "Saree and South Asian Ethnic Wear Trims Guide",
        "garment-trims-trade-show-sourcing-guide.html": "Trims Trade Show Sourcing Guide",
    },
    "ja": {
        "saree-ethnic-wear-trims-guide.html": "サリーと南アジア民族衣料の副資材ガイド",
        "garment-trims-trade-show-sourcing-guide.html": "副資材の見本市活用ガイド",
    },
    "ko": {
        "saree-ethnic-wear-trims-guide.html": "사리·남아시아 민족 의류 부자재 가이드",
        "garment-trims-trade-show-sourcing-guide.html": "부자재 전시회 소싱 가이드",
    },
    "fr": {
        "saree-ethnic-wear-trims-guide.html": "Guide des accessoires de saree",
        "garment-trims-trade-show-sourcing-guide.html": "Guide des salons d'accessoires",
    },
    "es": {
        "saree-ethnic-wear-trims-guide.html": "Guía de accesorios para saree",
        "garment-trims-trade-show-sourcing-guide.html": "Guía de ferias de accesorios",
    },
}

H1EXPECT = {
    "zh": {
        "saree-ethnic-wear-trims-guide.html": "紗麗與南亞民族服飾輔料指南",
        "garment-trims-trade-show-sourcing-guide.html": "服裝輔料展會採購指南",
    },
    "en": {
        "saree-ethnic-wear-trims-guide.html": "Saree and South Asian Ethnic Wear Trims",
        "garment-trims-trade-show-sourcing-guide.html": "Trims Trade Show Sourcing",
    },
    "ja": {
        "saree-ethnic-wear-trims-guide.html": "サリーと南アジア民族衣料の副資材",
        "garment-trims-trade-show-sourcing-guide.html": "副資材の見本市活用ガイド",
    },
    "ko": {
        "saree-ethnic-wear-trims-guide.html": "사리·남아시아 민족 의류 부자재",
        "garment-trims-trade-show-sourcing-guide.html": "부자재 전시회 소싱 가이드",
    },
    "fr": {
        "saree-ethnic-wear-trims-guide.html": "Accessoires de saree et de vêtements ethniques",
        "garment-trims-trade-show-sourcing-guide.html": "Sourcing d'accessoires en salon",
    },
    "es": {
        "saree-ethnic-wear-trims-guide.html": "Accesorios para saree y ropa étnica",
        "garment-trims-trade-show-sourcing-guide.html": "Compras de accesorios en feria",
    },
}

fails = []
print("== 1) 线上 DOM 渲染（headless Chrome，六语 × 2 篇） ==")
for lang, m in EXPECT.items():
    for slug, want in m.items():
        want_h1 = H1EXPECT[lang][slug]
        if lang == "zh":
            url = "https://taigetag.com/blog/%s?lang=zh&v=167" % slug
        else:
            url = "https://taigetag.com/%s/blog/%s?lang=%s&v=167" % (lang, slug, lang)
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=12000", "--dump-dom", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
        dom = r.stdout or ""
        title = (re.search(r"<title[^>]*>(.*?)</title>", dom, re.S) or [None, ""])[1].strip()
        h1 = (re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S) or [None, ""])[1].strip()
        ok_t = want in title
        ok_h = want_h1 in h1
        if not (ok_t and ok_h):
            fails.append((url, title[:70], h1[:70]))
        print("  %-6s %-46s title_ok=%s h1_ok=%s" % (lang, slug[:44], ok_t, ok_h))
        if lang in ("en", "fr", "es"):
            body = re.search(r'<section class="article-body">(.*?)</section>', dom, re.S)
            cjk = len(re.findall(r"[\u4e00-\u9fff]", body.group(1))) if body else -1
            if cjk != 0:
                fails.append((url, "正文汉字=%s" % cjk, ""))
            print("         正文汉字=%s" % cjk)

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
    fails.append(("sitemap", str(len(miss)) + " 个 URL 缺失", ""))

print("\n== 3) 线上页面状态码抽查 ==")
for u in ["https://taigetag.com/blog/%s" % SLUGS[0],
          "https://taigetag.com/ja/blog/%s" % SLUGS[1],
          "https://taigetag.com/blog/index.html"]:
    try:
        code = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=45).getcode()
    except urllib.error.HTTPError as e:
        code = e.code
    print("  %-64s HTTP %s" % (u, code))
    if code != 200:
        fails.append((u, "HTTP %s" % code, ""))

print("\n结论: 失败项 %d" % len(fails))
for f in fails:
    print("  !!", f)
raise SystemExit(1 if fails else 0)
