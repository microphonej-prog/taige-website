#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-30 下午批次线上验证：六语 DOM 标题渲染 + 线上 sitemap（12 URL / blog 首页 lastmod）+ 线上卡片"""
import re, subprocess, sys, urllib.request

sys.path.insert(0, ".")
from daily_meta_20260930_pm import ARTICLES

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
KEY = {
    "woven-label-density-guide.html": {
        "zh": "織嘜密度", "en": "Weft Density", "ja": "緯密度",
        "ko": "위사 밀도", "fr": "labels tissés", "es": "etiquetas tejidas"},
    "garment-trims-development-calendar.html": {
        "zh": "開發日曆", "en": "Trims Development Calendar", "ja": "開発カレンダー",
        "ko": "개발 캘린더", "fr": "Calendrier de développement", "es": "Calendario de desarrollo"},
}


def url_of(slug, lang):
    return ("https://taigetag.com/blog/%s?v=1" % slug if lang == "zh"
            else "https://taigetag.com/%s/blog/%s?v=1" % (lang, slug))


def dom(url):
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                        "--virtual-time-budget=12000", "--dump-dom", url],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
    return r.stdout or ""


fails = []
for a in ARTICLES:
    slug = a["slug"]
    print("== %s" % slug)
    for lang in LANGS:
        d = dom(url_of(slug, lang))
        m = re.search(r"<title[^>]*>(.*?)</title>", d, re.S)
        title = m.group(1).strip() if m else ""
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", d, re.S)
        h1t = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else ""
        k = KEY[slug][lang].lower()
        ok_t, ok_h = k in title.lower(), k in h1t.lower()
        if not (ok_t and ok_h):
            fails.append("%s [%s] title=%r h1=%r" % (slug, lang, title, h1t))
        print("  %s [%s] title=%s" % ("OK " if (ok_t and ok_h) else "FAIL", lang, title[:72]))
        print("        h1=%s" % h1t[:72])

req = urllib.request.Request("https://taigetag.com/sitemap.xml?v=1",
                            headers={"User-Agent": "Mozilla/5.0 TAGE-verify"})
sm = urllib.request.urlopen(req, timeout=90).read().decode("utf-8", "replace")
print("\n线上 sitemap 字节: %d，<loc> 总数: %d" % (len(sm), sm.count("<loc>")))
for a in ARTICLES:
    for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS[1:]]:
        u = "https://taigetag.com/%s%s" % (pre, a["slug"])
        ok = ("<loc>%s</loc>" % u) in sm
        if not ok:
            fails.append("线上 sitemap 缺 %s" % u)
        print("  %s %s" % ("OK " if ok else "FAIL", u))
for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS[1:]]:
    u = "https://taigetag.com/%sindex.html" % pre
    pat = r"<loc>%s</loc>\s*<lastmod>2026-09-30</lastmod>" % re.escape(u)
    ok = bool(re.search(pat, sm))
    if not ok:
        fails.append("线上 %s lastmod 未更新" % u)
    print("  %s lastmod %s" % ("OK " if ok else "FAIL", u))

idx = urllib.request.urlopen(urllib.request.Request(
    "https://taigetag.com/blog/index.html?v=1",
    headers={"User-Agent": "Mozilla/5.0 TAGE-verify"}), timeout=90).read().decode("utf-8", "replace")
for a in ARTICLES:
    ok = a["slug"] in idx
    if not ok:
        fails.append("线上 blog/index.html 缺卡片 %s" % a["slug"])
    print("  %s 线上卡片 %s" % ("OK " if ok else "FAIL", a["slug"]))

print("\n结果:", "全部通过" if not fails else "失败 %d 项" % len(fails))
for f in fails:
    print("  -", f)
raise SystemExit(1 if fails else 0)
