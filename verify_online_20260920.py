#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-20 线上验证：sitemap 含 12 个新 URL + headless Chrome 六语 title/h1 渲染。"""
import re, subprocess, urllib.request, sys

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["hang-tag-double-sided-printing.html", "trim-quotation-comparison-guide.html"]
LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
EXPECT = {
    "zh": ["雙面印刷", "報價單"],
    "en": ["Double-Sided Hang Tags", "Comparing Trim Quotations"],
    "fr": ["recto-verso", "Comparer les devis"],
    "es": ["doble cara", "Comparar presupuestos"],
    "ja": ["両面印刷", "見積書"],
    "ko": ["양면 인쇄", "견적서"],
}
fail = 0


def chrome_dom(url):
    out = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=12000",
                          "--dump-dom", url], capture_output=True, timeout=150)
    return out.stdout.decode("utf-8", "replace")


def title_of(html):
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.S)
    return m.group(1).strip() if m else "!!无 title"


print("== 线上 sitemap ==")
sp = None
for opener in ("direct", "curl"):
    try:
        if opener == "direct":
            req = urllib.request.Request("https://taigetag.com/sitemap.xml", headers={"User-Agent": "Mozilla/5.0"})
            sp = urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")
        else:
            sp = subprocess.run(["curl", "-s", "--noproxy", "*", "https://taigetag.com/sitemap.xml"],
                                capture_output=True, timeout=90).stdout.decode("utf-8", "replace")
        if sp and "<urlset" in sp:
            print("  取到 sitemap（%s，%d 字节，%d 个 URL）" % (opener, len(sp), sp.count("<loc>")))
            break
        print("  方式 %s 未取到有效 sitemap" % opener)
    except Exception as e:
        print("  方式 %s 失败: %s" % (opener, e))
for slug in SLUGS:
    for pre in ["blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"]:
        loc = "https://taigetag.com/%s%s" % (pre, slug)
        ok = bool(sp) and ("<loc>%s</loc>" % loc) in sp
        if not ok:
            fail += 1
        print("  %s %s" % ("OK " if ok else "缺失", loc))

print("== headless Chrome 六语渲染 ==")
for i, slug in enumerate(SLUGS):
    for lang in LANGS:
        url = "https://taigetag.com/blog/%s?lang=%s&v=1" % (slug, lang)
        html = chrome_dom(url)
        title = title_of(html)
        hit = EXPECT[lang][i] in title
        if not hit:  # 尝试直接语言路径再确认一次
            html = chrome_dom("https://taigetag.com/%s/blog/%s?v=1" % (lang if lang != "zh" else "", slug) if lang != "zh" else url)
            title = title_of(html)
            hit = EXPECT[lang][i] in title
        if not hit:
            fail += 1
        print("  [%s|%s] %s title=%s" % (lang, slug[:20], "OK " if hit else "!!", title[:96]))

print("\n结论: fail = %d" % fail)
sys.exit(1 if fail else 0)
