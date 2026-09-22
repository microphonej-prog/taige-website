#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-22 晚间批次线上验证：
1) urllib 抓 12 个新页面 + 6 个 blog 首页（带缓存击穿参数），核对标题关键词；
2) 无头 Chrome dump-dom 渲染 12 个新页面，核对 <title> 语言正确；
3) 线上 sitemap.xml 含 12 个新 URL。
"""
import re, sys, random, subprocess, os, urllib.request

sys.stdout.reconfigure(encoding='utf-8')
CB = "?cb=%d" % random.randint(100000, 999999)
BUST = "101"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/125 Safari/537.36"

SLUGS = {
    "eu-digital-product-passport-trims.html": {
        "": "服裝輔料指南", "en": "Digital Product Passport", "ja": "デジタル製品パスポート",
        "ko": "디지털 제품 여권", "fr": "Passeport numérique", "es": "Pasaporte digital de producto"},
    "trims-carbon-footprint-guide.html": {
        "": "碳足跡覈算指南", "en": "Carbon Footprint", "ja": "カーボンフットプリント",
        "ko": "탄소발자국", "fr": "Empreinte carbone", "es": "Huella de carbono"},
}
LANGS = ["en", "ja", "ko", "fr", "es"]
fails = []


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Cache-Control": "no-cache"})
    return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "replace")


print("== 1) urllib 抓取线上页面 ==")
for slug, exp in SLUGS.items():
    for l in [""] + LANGS:
        pre = (l + "/") if l else ""
        url = "https://taigetag.com/%sblog/%s" % (pre, slug)
        try:
            s = fetch(url + CB)
        except Exception as e:
            fails.append("抓取失败 %s: %s" % (url, e)); print("  FAIL", url, e); continue
        m = re.search(r'<title[^>]*>(.*?)</title>', s, re.S)
        t = m.group(1).strip() if m else ""
        ok = exp[l] in t
        print("  %s %s | %s" % ("ok " if ok else "FAIL", url, t[:70]))
        if not ok:
            fails.append("标题不含 %s: %s" % (exp[l], url))

print("== 2) blog 首页卡片 ==")
for l in [""] + LANGS:
    pre = (l + "/") if l else ""
    url = "https://taigetag.com/%sblog/index.html" % pre
    try:
        s = fetch(url + CB)
    except Exception as e:
        fails.append("抓取失败 %s: %s" % (url, e)); continue
    miss = [sl for sl in SLUGS if sl not in s]
    print("  %s %s 缺卡片=%s" % ("ok " if not miss else "FAIL", url, miss))
    if miss:
        fails.append("%s 缺卡片 %s" % (url, miss))

print("== 3) 线上 sitemap ==")
sm = fetch("https://taigetag.com/sitemap.xml" + CB)
for slug in SLUGS:
    for l in [""] + LANGS:
        pre = (l + "/") if l else ""
        u = "https://taigetag.com/%sblog/%s" % (pre, slug)
        if "<loc>%s</loc>" % u not in sm:
            fails.append("线上 sitemap 缺 %s" % u)
            print("  FAIL 缺", u)
print("  线上 sitemap <loc> 总数:", sm.count("<loc>"))
bj = re.search(r'<loc>https://taigetag.com/blog/index.html</loc>\s*<lastmod>([^<]*)</lastmod>', sm)
print("  blog/index lastmod:", bj.group(1) if bj else "未找到")

print("== 4) 无头 Chrome 渲染标题（?lang=xx&v=%s） ==" % BUST)
for slug, exp in SLUGS.items():
    for l in [""] + LANGS:
        pre = (l + "/") if l else ""
        url = "https://taigetag.com/%sblog/%s?lang=%s&v=%s" % (pre, slug, l or "zh", BUST)
        try:
            r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                                "--virtual-time-budget=9000", "--dump-dom", url],
                               capture_output=True, text=True, encoding="utf-8", errors="replace",
                               timeout=90)
            dom = r.stdout or ""
        except Exception as e:
            fails.append("Chrome 失败 %s: %s" % (url, e)); print("  FAIL chrome", url, e); continue
        m = re.search(r'<title[^>]*>(.*?)</title>', dom, re.S)
        t = (m.group(1).strip() if m else "")
        ok = exp[l] in t
        print("  %s %s | %s" % ("ok " if ok else "FAIL", url, t[:72]))
        if not ok:
            fails.append("Chrome 渲染标题不含 %s: %s" % (exp[l], url))

print("\n线上验证：", "全部通过 ✅" if not fails else "失败 %d 项 ❌" % len(fails))
for f in fails:
    print("  -", f)
