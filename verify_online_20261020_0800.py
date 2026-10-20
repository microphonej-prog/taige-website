#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证（2026-10-20 08:00 批次）：六语 × 2 篇 title/h1 渲染 + 线上 sitemap 12 URL + 列表页卡片 + HTTP 状态。"""
import os, re, subprocess, sys, urllib.request, urllib.error

os.chdir(os.path.dirname(os.path.abspath(__file__)))

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["vendor-labeling-manual-compliance.html", "garment-trims-repeat-order-consistency.html"]
V = "173"

EXPECT = {
    "zh": {"vendor-labeling-manual-compliance.html": "標籤手冊",
           "garment-trims-repeat-order-consistency.html": "返單一致性"},
    "en": {"vendor-labeling-manual-compliance.html": "Vendor Labeling Manual",
           "garment-trims-repeat-order-consistency.html": "Repeat-Order Consistency"},
    "ja": {"vendor-labeling-manual-compliance.html": "ラベリングマニュアル",
           "garment-trims-repeat-order-consistency.html": "返単一致"},
    "ko": {"vendor-labeling-manual-compliance.html": "라벨링 매뉴얼",
           "garment-trims-repeat-order-consistency.html": "재주문 일관성"},
    "fr": {"vendor-labeling-manual-compliance.html": "marquage client",
           "garment-trims-repeat-order-consistency.html": "Réassort d'accessoires"},
    "es": {"vendor-labeling-manual-compliance.html": "etiquetado del cliente",
           "garment-trims-repeat-order-consistency.html": "Reposición"},
}

fails = []
print("== 1) 线上 DOM 渲染（六语 × 2 篇，v=%s） ==" % V)
for lang, m in EXPECT.items():
    for slug, want in m.items():
        if lang == "zh":
            url = "https://taigetag.com/blog/%s?lang=zh&v=%s&nc=0800" % (slug, V)
        else:
            url = "https://taigetag.com/%s/blog/%s?lang=%s&v=%s&nc=0800" % (lang, slug, lang, V)
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=12000", "--dump-dom", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=150)
        dom = r.stdout or ""
        title = (re.search(r"<title[^>]*>(.*?)</title>", dom, re.S) or [None, ""])[1].strip()
        h1 = (re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S) or [None, ""])[1].strip()
        ok_t, ok_h = want in title, want in h1
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
for s in SLUGS:
    for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
        u = "https://taigetag.com/%s%s" % (pre, s)
        if "<loc>%s</loc>" % u not in sm:
            miss.append(u)
print("  线上 <loc> 总数=%d，缺失新 URL=%d %s" % (sm.count("<loc>"), len(miss), miss[:4]))
if miss:
    fails.append(("sitemap", "%d 个 URL 缺失" % len(miss), ""))

print("\n== 3) 线上列表页卡片 + 状态码 ==")
for idx_url in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in ("en", "ja", "ko", "fr", "es")]:
    try:
        idx = urllib.request.urlopen(urllib.request.Request(
            idx_url, headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"}), timeout=45).read().decode("utf-8", "replace")
    except Exception as e:
        print("  !! 列表页取回失败", idx_url, e)
        fails.append((idx_url, "取回失败", ""))
        continue
    counts = [idx.count('href="%s"' % s) for s in SLUGS]
    print("  %-52s 卡片数=%s" % (idx_url, counts))
    if min(counts) < 1:
        fails.append((idx_url, "卡片缺失", ""))
for u in ["https://taigetag.com/blog/%s" % SLUGS[0],
          "https://taigetag.com/blog/%s" % SLUGS[1],
          "https://taigetag.com/ja/blog/%s" % SLUGS[1],
          "https://taigetag.com/fr/blog/%s" % SLUGS[0],
          "https://taigetag.com/es/blog/%s" % SLUGS[1],
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
