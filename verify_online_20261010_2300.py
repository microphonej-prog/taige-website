#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证（2026-10-10 晚间批次）：无头 Chrome 六语 DOM 标题 + 线上 sitemap 新 URL + 线上列表页首卡。
用法: F:/hermes/venvs/tools/Scripts/python.exe verify_online_20261010_2300.py
"""
import re, sys, subprocess, urllib.request, ssl, os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
V = "148"
BASE = "https://taigetag.com"
EXPECT = {
    "uflpa-apparel-trims-traceability-guide.html": {
        "zh": "美國 UFLPA 服裝輔料溯源指南", "en": "US UFLPA Guide for Apparel Trims",
        "ja": "米国 UFLPA 衣料副資材", "ko": "미국 UFLPA 의류 부자재", "fr": "Guide UFLPA", "es": "Guía UFLPA"},
    "corrugated-carton-strength-guide.html": {
        "zh": "瓦楞外箱選型指南", "en": "Corrugated Carton Selection Guide",
        "ja": "段ボール外箱の選定ガイド", "ko": "골판지 상자 선정 가이드",
        "fr": "Guide de choix des cartons ondulés", "es": "Guía de cajas de cartón ondulado"},
}
LANGDIR = {"zh": "", "en": "en/", "ja": "ja/", "ko": "ko/", "fr": "fr/", "es": "es/"}


def dom_title(url):
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                        "--virtual-time-budget=12000", "--dump-dom", url],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=90)
    m = re.search(r'<title[^>]*>(.*?)</title>', r.stdout, re.S)
    return (m.group(1).strip() if m else "<no title>"), len(r.stdout)


def fetch(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (verify)"})
    with urllib.request.urlopen(req, timeout=45, context=ctx) as f:
        return f.read().decode("utf-8", "replace")


print("== A) 六语线上标题（无头 Chrome DOM） ==")
fails = []
for slug, langs in EXPECT.items():
    for lang, need in langs.items():
        url = "%s/%sblog/%s?lang=%s&v=%s" % (BASE, LANGDIR[lang], slug, lang, V)
        t, n = dom_title(url)
        ok = need in t
        print("  %-58s %s  %s" % (url.replace(BASE, ""), "OK" if ok else "!!", t[:78]))
        if not ok:
            fails.append((url, t))

print("\n== B) 线上 sitemap.xml ==")
sm = fetch(BASE + "/sitemap.xml")
for slug in EXPECT:
    for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
        u = "<loc>%s/%s%s</loc>" % (BASE, pre, slug)
        if u not in sm:
            print("  !! 缺 %s" % u)
            fails.append(u)
    print("  %s 六语 URL 全部在线" % slug)
print("  线上 <loc> 总数 = %d" % sm.count("<loc>"))

print("\n== C) 线上列表页首卡 ==")
for lang in ("zh", "en", "ja", "ko", "fr", "es"):
    html = fetch("%s/%sblog/index.html?v=%s" % (BASE, LANGDIR[lang], V))
    grid = html.index('<div class="post-grid">')
    first = re.findall(r'<a class="more" href="([^"]*)"', html[grid:])[:2]
    ok = sorted(first) == sorted(EXPECT.keys())
    print("  %-4s 首卡=%s %s" % (lang, first, "OK" if ok else "!!"))
    if not ok:
        fails.append(("first-card", lang, first))

print("\n== 结论: 失败 %d 项 ==" % len(fails))
for f in fails:
    print("  ", f)
sys.exit(1 if fails else 0)
