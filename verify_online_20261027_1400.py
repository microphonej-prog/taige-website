#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-27 14:00 批次线上校验：sitemap + 无头 Chrome 六语 title 渲染"""
import os, re, sys, html, subprocess, urllib.request, ssl

os.chdir(os.path.dirname(os.path.abspath(__file__)))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["amazon-fba-apparel-packaging-guide.html", "us-state-packaging-epr-laws.html"]
LANGS = [("zh", "blog"), ("en", "en/blog"), ("ja", "ja/blog"),
         ("ko", "ko/blog"), ("fr", "fr/blog"), ("es", "es/blog")]
fail = []

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# ---- 线上 sitemap ----
url = "https://taigetag.com/sitemap.xml?nocache=1"
try:
    sm = urllib.request.urlopen(url, timeout=60, context=ctx).read().decode("utf-8", "replace")
except Exception as e:
    print("sitemap 拉取失败:", e)
    sm = ""
print("线上 sitemap 长度 %d，<loc> 数 %d" % (len(sm), sm.count("<loc>")))
for slug in SLUGS:
    for lang, pre in LANGS:
        u = ("https://taigetag.com/blog/%s" % slug) if lang == "zh" else \
            ("https://taigetag.com/%s/%s" % (pre, slug))
        if ("<loc>%s</loc>" % u) not in sm:
            fail.append("线上 sitemap 缺 %s" % u)

# ---- 无头 Chrome 渲染 title ----
for slug in SLUGS:
    for lang, pre in LANGS:
        local = ("blog/%s" % slug) if lang == "zh" else ("%s/%s" % (pre, slug))
        s = open(local, encoding="utf-8").read()
        m = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
        want = html.unescape(m.group(1)).strip() if m else ""
        path = ("/blog/%s" % slug) if lang == "zh" else ("/%s/%s" % (pre, slug))
        u = "https://taigetag.com%s?lang=%s&v=999" % (path, lang)
        try:
            out = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                                  "--virtual-time-budget=12000", "--dump-dom", u],
                                 capture_output=True, timeout=120).stdout.decode("utf-8", "replace")
        except Exception as e:
            fail.append("%s %s Chrome 失败: %s" % (slug, lang, e))
            continue
        m2 = re.search(r"<title[^>]*>(.*?)</title>", out, re.S)
        got = html.unescape(m2.group(1)).strip() if m2 else ""
        ok = (got == want) and len(got) > 15
        print("%s %-42s %-3s len=%d %s" % ("ok  " if ok else "FAIL", slug, lang, len(got),
                                           "" if ok else "got=%r want=%r" % (got, want)))
        if not ok:
            fail.append("%s %s title 不符: %r != %r" % (slug, lang, got, want))

print()
if fail:
    print("!!! 线上失败 %d 项" % len(fail))
    for f in fail:
        print("  -", f)
    sys.exit(1)
print("线上全部通过")
