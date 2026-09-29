#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-29 下午批次线上验证：六语 DOM 标题（无头 Chrome）+ 线上 sitemap + 版本号 + 卡片。
用法: <python> verify_online_20260929_pm.py
"""
import re, os, sys, subprocess, tempfile

os.chdir(os.path.dirname(os.path.abspath(__file__)))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BUST = "121"
SLUGS = ["trim-supply-continuity-guide.html", "trim-supplier-communication-guide.html"]
LANGS = [("zh", ""), ("en", "en/"), ("ja", "ja/"), ("ko", "ko/"), ("fr", "fr/"), ("es", "es/")]
WANT = {
    "trim-supply-continuity-guide.html": {
        "zh": "供應中斷", "en": "Trims Supply Continuity",
        "ja": "副資材の供給継続", "ko": "부자재 공급 연속성",
        "fr": "Continuité d'approvisionnement", "es": "Continuidad de suministro"},
    "trim-supplier-communication-guide.html": {
        "zh": "服裝輔料溝通指南", "en": "Trims Supplier Communication",
        "ja": "副資材サプライヤーとのやり取り", "ko": "부자재 공급사 커뮤니케이션",
        "fr": "Communication fournisseur", "es": "Comunicación con proveedores"},
}
fails = []


def chrome_title(url):
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                        "--virtual-time-budget=12000", "--dump-dom", url],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
    m = re.search(r'<title[^>]*>(.*?)</title>', r.stdout or "", re.S)
    return m.group(1).strip() if m else ""


print("=== 1) 线上六语标题（?v=%s 防缓存） ===" % BUST)
for slug in SLUGS:
    for code, pref in LANGS:
        url = "https://taigetag.com/%sblog/%s?v=%s" % (pref, slug, BUST)
        t = chrome_title(url)
        ok = WANT[slug][code] in t
        if not ok:
            fails.append("title %s [%s] → %r" % (slug, code, t[:70]))
        print("  %-4s %-42s %s | %s" % (code, slug, "OK " if ok else "BAD", t[:72]))

print("=== 2) 线上 sitemap ===")
tmp = os.path.join(tempfile.gettempdir(), "tg_sitemap_check.xml")
subprocess.run(["curl", "-sS", "-o", tmp, "https://taigetag.com/sitemap.xml"], check=True)
sm = open(tmp, encoding="utf-8", errors="replace").read()
for slug in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % slug] + \
             ["https://taigetag.com/%s/blog/%s" % (l, slug) for l, _ in LANGS[1:]]:
        if "<loc>%s</loc>" % u not in sm:
            fails.append("线上 sitemap 缺 %s" % u)
m = re.search(r'<loc>https://taigetag.com/blog/index.html</loc>\s*<lastmod>([^<]*)</lastmod>', sm)
print("  线上 <loc> 总数 %d；blog 列表页 lastmod = %s" % (sm.count("<loc>"), m and m.group(1)))
if not m or m.group(1) != "2026-09-29":
    fails.append("线上 blog index lastmod = %s" % (m and m.group(1)))

print("=== 3) 线上列表页卡片 ===")
tmp2 = os.path.join(tempfile.gettempdir(), "tg_index_check.html")
subprocess.run(["curl", "-sS", "-o", tmp2, "https://taigetag.com/blog/index.html"], check=True)
idx = open(tmp2, encoding="utf-8", errors="replace").read()
for slug in SLUGS:
    n = idx.count(slug)
    print("  %-42s 命中 %d 次" % (slug, n))
    if n == 0:
        fails.append("线上列表页缺卡片 %s" % slug)

print("=== 4) 本地 BUST_VERSION ===")
mj = open("js/main.js", encoding="utf-8").read()
v = re.search(r'var BUST_VERSION = "([^"]*)"', mj).group(1)
print("  BUST_VERSION = %s" % v)
if v != BUST:
    fails.append("BUST_VERSION = %s" % v)

print()
if fails:
    print("失败 %d 项：" % len(fails))
    for f in fails:
        print(" - " + f)
    sys.exit(1)
print("线上验证全部通过 ✅")
