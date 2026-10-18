#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证（20:00 批次）：六语 × 2 篇 title/h1 渲染 + 线上 sitemap 12 URL + 列表页卡片 + HTTP 状态。"""
import os, re, subprocess, sys, urllib.request, urllib.error

os.chdir(os.path.dirname(os.path.abspath(__file__)))

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["compostable-packaging-certification-guide.html", "trim-scrap-destruction-certificate-guide.html"]
V = "171"

EXPECT = {
    "zh": {"compostable-packaging-certification-guide.html": "服裝包裝可堆肥認證指南",
           "trim-scrap-destruction-certificate-guide.html": "服裝輔料安全銷燬指南"},
    "en": {"compostable-packaging-certification-guide.html": "Compostable Packaging Certification",
           "trim-scrap-destruction-certificate-guide.html": "Scrapping Garment Trims"},
    "ja": {"compostable-packaging-certification-guide.html": "衣料包装の堆肥化認証ガイド",
           "trim-scrap-destruction-certificate-guide.html": "衣料副資材の安全な廃棄ガイド"},
    "ko": {"compostable-packaging-certification-guide.html": "의류 포장 퇴비화 인증 가이드",
           "trim-scrap-destruction-certificate-guide.html": "의류 부자재 안전 폐기 가이드"},
    "fr": {"compostable-packaging-certification-guide.html": "Certification compostable des emballages",
           "trim-scrap-destruction-certificate-guide.html": "Destruction sécurisée des accessoires"},
    "es": {"compostable-packaging-certification-guide.html": "Certificación compostable de embalajes",
           "trim-scrap-destruction-certificate-guide.html": "Destrucción segura de accesorios"},
}

fails = []
print("== 1) 线上 DOM 渲染（六语 × 2 篇，v=%s） ==" % V)
for lang, m in EXPECT.items():
    for slug, want in m.items():
        if lang == "zh":
            url = "https://taigetag.com/blog/%s?lang=zh&v=%s&nc=2000" % (slug, V)
        else:
            url = "https://taigetag.com/%s/blog/%s?lang=%s&v=%s&nc=2000" % (lang, slug, lang, V)
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=12000", "--dump-dom", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=150)
        dom = r.stdout or ""
        title = (re.search(r"<title[^>]*>(.*?)</title>", dom, re.S) or [None, ""])[1].strip()
        h1 = (re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S) or [None, ""])[1].strip()
        ok_t, ok_h = want in title, want in h1
        body = re.search(r'<section class="article-body">(.*?)</section>', dom, re.S)
        blen = len(re.sub(r"<[^>]+>", " ", body.group(1))) if body else -1
        print("  %-3s %-44s title_ok=%s h1_ok=%s body=%d" % (lang, slug[:42], ok_t, ok_h, blen))
        if not (ok_t and ok_h):
            fails.append((url, title[:70], h1[:70]))
        if body is None or blen < 1200:
            fails.append((url, "正文渲染异常 body=%d" % blen, ""))
        if lang in ("en", "fr", "es"):
            cjk = len(re.findall(r"[\u4e00-\u9fff]", body.group(1))) if body else -1
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
