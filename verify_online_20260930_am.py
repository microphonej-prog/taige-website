#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-30 上午批次线上验证：六语 DOM 标题渲染 + 线上 sitemap 与卡片"""
import os, re, subprocess, sys, json, time
sys.path.insert(0, ".")
from daily_meta_20260930_am import ARTICLES

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SCRATCH = r"F:\hermes\cache\scratch"
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
TOK = {
    "zh": "TAGE",
    "en": "TAGE",
    "ja": "TAGE",
    "ko": "TAGE",
    "fr": "TAGE",
    "es": "TAGE",
}
# 每篇文章在六语下的标题关键词（用于确认不是回落到默认语言）
KEY = {
    "trim-color-approval-process.html": {
        "zh": "顏色批", "en": "Colour Approval Process", "ja": "色承認",
        "ko": "색상 승인", "fr": "couleur", "es": "aprobación de color"},
    "trim-quality-8d-report-guide.html": {
        "zh": "質量異常", "en": "Quality Failure Handling", "ja": "品質異常対応",
        "ko": "품질 이상 대응", "fr": "non-conformité", "es": "no conformidad"},
}


def url_of(slug, lang):
    return "https://taigetag.com/blog/%s?v=1" % slug if lang == "zh" else \
           "https://taigetag.com/%s/blog/%s?v=1" % (lang, slug)


def dom(url):
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                        "--virtual-time-budget=12000", "--dump-dom", url],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
    return r.stdout or ""


fails = []
for a in ARTICLES:
    slug = a["slug"]
    print("== %s" % slug)
    for lang in LANGS:
        d = dom(url_of(slug, lang))
        m = re.search(r"<title[^>]*>(.*?)</title>", d, re.S)
        title = (m.group(1).strip() if m else "")
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", d, re.S)
        h1t = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else ""
        t_low, h_low = title.lower(), h1t.lower()
        k_low = KEY[slug][lang].lower()
        ok_t = k_low in t_low
        ok_h = k_low in h_low
        status = "OK " if (ok_t and ok_h) else "FAIL"
        if not (ok_t and ok_h):
            fails.append("%s [%s] title=%r h1=%r" % (slug, lang, title, h1t))
        print("  %s [%s] title=%s" % (status, lang, title[:70]))
        print("        h1=%s" % h1t[:70])

# 线上 sitemap
import urllib.request
req = urllib.request.Request("https://taigetag.com/sitemap.xml?v=1",
                             headers={"User-Agent": "Mozilla/5.0 TAGE-verify"})
sm = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
print("\n线上 sitemap 字节: %d，<loc> 总数: %d" % (len(sm), sm.count("<loc>")))
for a in ARTICLES:
    for p in ["blog/%s" % a["slug"]] + ["%s/blog/%s" % (l, a["slug"]) for l in LANGS[1:]]:
        u = "https://taigetag.com/%s" % p
        ok = ("<loc>%s</loc>" % u) in sm
        if not ok:
            fails.append("线上 sitemap 缺 %s" % u)
        print("  %s %s" % ("OK " if ok else "FAIL", u))
    ok = re.search(r"<loc>https://taigetag\.com/blog/index\.html</loc>\s*<lastmod>2026-09-30</lastmod>", sm)
    if not ok:
        fails.append("线上 blog/index.html lastmod 未更新")

# 线上首页卡片
idx = urllib.request.urlopen(urllib.request.Request(
    "https://taigetag.com/blog/index.html?v=1", headers={"User-Agent": "Mozilla/5.0 TAGE-verify"}),
    timeout=60).read().decode("utf-8", "replace")
for a in ARTICLES:
    ok = a["slug"] in idx
    if not ok:
        fails.append("线上 blog/index.html 缺卡片 %s" % a["slug"])
    print("  %s 线上卡片 %s" % ("OK " if ok else "FAIL", a["slug"]))

print("\n结果:", "全部通过" if not fails else "失败 %d 项" % len(fails))
for f in fails:
    print("  -", f)
