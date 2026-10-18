#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证：六语 × 2 篇 title/h1 渲染 + 线上 sitemap 12 URL + 列表页卡片 + HTTP 状态。"""
import os, re, subprocess, sys, urllib.request, urllib.error

os.chdir(os.path.dirname(os.path.abspath(__file__)))

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["trim-inner-packing-spec.html", "adhesive-trim-shelf-life.html"]
V = "170"

EXPECT = {
    "zh": {"trim-inner-packing-spec.html": "服裝輔料內包裝規格指南",
           "adhesive-trim-shelf-life.html": "自粘輔料保質期與膠層老化管理"},
    "en": {"trim-inner-packing-spec.html": "Trims Inner Packing Specs",
           "adhesive-trim-shelf-life.html": "Adhesive Trim Shelf Life"},
    "ja": {"trim-inner-packing-spec.html": "衣料副資材の内装仕様ガイド",
           "adhesive-trim-shelf-life.html": "粘着副資材の保存期間"},
    "ko": {"trim-inner-packing-spec.html": "의류 부자재 내포장 사양 가이드",
           "adhesive-trim-shelf-life.html": "점착 부자재 유통기한"},
    "fr": {"trim-inner-packing-spec.html": "Conditionnement interne des accessoires",
           "adhesive-trim-shelf-life.html": "Durée de vie des accessoires autocollants"},
    "es": {"trim-inner-packing-spec.html": "Embalaje interior de accesorios",
           "adhesive-trim-shelf-life.html": "Vida útil de accesorios autoadhesivos"},
}

fails = []
print("== 1) 线上 DOM 渲染（六语 × 2 篇，v=%s） ==" % V)
for lang, m in EXPECT.items():
    for slug, want in m.items():
        if lang == "zh":
            url = "https://taigetag.com/blog/%s?lang=zh&v=%s" % (slug, V)
        else:
            url = "https://taigetag.com/%s/blog/%s?lang=%s&v=%s" % (lang, slug, lang, V)
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=12000", "--dump-dom", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=150)
        dom = r.stdout or ""
        title = (re.search(r"<title[^>]*>(.*?)</title>", dom, re.S) or [None, ""])[1].strip()
        h1 = (re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S) or [None, ""])[1].strip()
        ok_t, ok_h = want in title, want in h1
        print("  %-3s %-44s title_ok=%s h1_ok=%s" % (lang, slug[:42], ok_t, ok_h))
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
print("  线上 <loc> 总数=%d，缺失新 URL=%d %s" % (sm.count("<loc>"), len(miss), miss[:4]))
if miss:
    fails.append(("sitemap", "%d 个 URL 缺失" % len(miss), ""))

print("\n== 3) 线上列表页卡片 + 状态码 ==")
idx = urllib.request.urlopen(urllib.request.Request(
    "https://taigetag.com/blog/index.html", headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"}),
    timeout=45).read().decode("utf-8", "replace")
for s in SLUGS:
    n = idx.count('href="%s"' % s)
    print("  卡片 %-46s %d" % (s, n))
    if n < 1:
        fails.append(("index", s, ""))
for u in ["https://taigetag.com/blog/%s" % SLUGS[0],
          "https://taigetag.com/ko/blog/%s" % SLUGS[1],
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
