#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证（2026-10-12 下午批次）：
1) 无头 Chrome --dump-dom 抓取 12 个新页面（2 篇 × 6 语）确认 title/h1/description 渲染正确
2) curl 抓线上 sitemap.xml 确认含 2 个新 URL 与 lastmod
3) 确认线上 js/main.js 的 BUST_VERSION 已升级到 153
"""
import subprocess, re, os, sys, tempfile, urllib.request, ssl

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["trousers-pants-trims-guide.html", "tshirt-hoodie-trims-guide.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
EXPECT = {
    "trousers-pants-trims-guide.html": {
        "zh": "褲裝輔料與標籤指南",
        "en": "Trouser and Pants Trims Guide",
        "ja": "パンツの副資材とラベルガイド",
        "ko": "바지 부자재와 라벨 가이드",
        "fr": "Guide des accessoires de pantalon",
        "es": "Guía de accesorios de pantalón",
    },
    "tshirt-hoodie-trims-guide.html": {
        "zh": "T恤與衛衣輔料指南",
        "en": "T-Shirt and Hoodie Trims Guide",
        "ja": "Tシャツとパーカーの副資材ガイド",
        "ko": "티셔츠와 후디 부자재 가이드",
        "fr": "Guide des accessoires de t-shirt et de sweat",
        "es": "Guía de accesorios de camiseta y sudadera",
    },
}

fails = []
print("========== 1) 线上 DOM 标题/描述 12 页 ==========")
for slug in SLUGS:
    for lang in LANGS:
        url = "https://taigetag.com/%sblog/%s?lang=%s&v=1" % (lang + "/" if lang != "zh" else "", slug, lang)
        tmp = os.path.join(tempfile.gettempdir(), "dom_%s_%s.html" % (slug[:10], lang))
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=12000", "--dump-dom", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
        dom = r.stdout or ""
        if not dom:
            dom = open(tmp, encoding="utf-8", errors="replace").read() if os.path.exists(tmp) else ""
        t = re.search(r"<title[^>]*>(.*?)</title>", dom, re.S)
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S)
        d = re.search(r'<meta name="description"[^>]*content="([^"]*)"', dom, re.S)
        title = (t.group(1).strip() if t else "NO-TITLE")
        h1v = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else "NO-H1"
        exp = EXPECT[slug][lang]
        good_t = exp in title
        good_h = exp[:10] in h1v
        print("%-4s %-36s title=%-3s h1=%-3s desc=%3d字 | %s" %
              (lang, slug[:36], "OK" if good_t else "×", "OK" if good_h else "×",
               len(d.group(1)) if d else 0, title[:72]))
        if not good_t:
            fails.append((url, "title", title))
        if not good_h:
            fails.append((url, "h1", h1v))
        if not d or len(d.group(1)) < 40:
            fails.append((url, "desc", d.group(1) if d else "NONE"))

print("\n========== 2) 线上 sitemap.xml ==========")
ctx = ssl.create_default_context()
try:
    req = urllib.request.Request("https://taigetag.com/sitemap.xml?v=1", headers={"User-Agent": "Mozilla/5.0"})
    live = urllib.request.urlopen(req, timeout=45, context=ctx).read().decode("utf-8", "replace")
except Exception as e:
    live = ""
    fails.append(("sitemap", "fetch", str(e)))
if live:
    print("线上 sitemap 长度 %d 字符" % len(live))
    for slug in SLUGS:
        for u in ["https://taigetag.com/blog/%s" % slug] + \
                 ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in ["en", "ja", "ko", "fr", "es"]]:
            if "<loc>%s</loc>" % u in live:
                print("  OK  %s" % u)
            else:
                print("  ×   %s" % u)
                fails.append(("sitemap", "missing", u))
    m = re.search(r'<loc>https://taigetag\.com/blog/index\.html</loc>\s*<lastmod>([^<]*)</lastmod>', live)
    print("  blog/index.html lastmod =", m.group(1) if m else "?")
else:
    print("线上 sitemap 抓取失败")

print("\n========== 3) 线上 js/main.js BUST_VERSION ==========")
try:
    req = urllib.request.Request("https://taigetag.com/js/main.js?v=1", headers={"User-Agent": "Mozilla/5.0"})
    mj = urllib.request.urlopen(req, timeout=45, context=ctx).read().decode("utf-8", "replace")
    m = re.search(r'BUST_VERSION\s*=\s*"([^"]*)"', mj)
    print("线上 BUST_VERSION =", m.group(1) if m else "未找到")
    if not m or m.group(1) != "153":
        fails.append(("main.js", "BUST_VERSION", m.group(1) if m else "?"))
except Exception as e:
    fails.append(("main.js", "fetch", str(e)))
    print("main.js 抓取失败：", e)

print("\n失败项：%d" % len(fails))
for f in fails:
    print("  -", f)
