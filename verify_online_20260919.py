#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证：headless Chrome 渲染新页六语 title/h1，并确认线上 sitemap 含新 URL。"""
import re
import subprocess
import urllib.request

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["apparel-trims-spec-sheet-guide.html", "suiting-formalwear-trims-guide.html"]
LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
BASE = "https://taigetag.com/%s"


def chrome_title(url):
    out = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=12000",
                          "--dump-dom", url], capture_output=True, timeout=120)
    html = out.stdout.decode("utf-8", "replace")
    t = re.search(r"<title[^>]*>(.*?)</title>", html, re.S)
    h = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    title = t.group(1).strip() if t else "!!无 title"
    head = re.sub(r"\s+", " ", h.group(1)).strip() if h else "!!无 h1"
    return title, head


print("== 线上 sitemap ==")
sp = None
for opener in ("direct", "curl"):
    try:
        if opener == "direct":
            req = urllib.request.Request(BASE % "sitemap.xml", headers={"User-Agent": "Mozilla/5.0"})
            sp = urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "replace")
        else:
            sp = subprocess.run(["curl", "-s", "--noproxy", "*", BASE % "sitemap.xml"],
                                capture_output=True, timeout=60).stdout.decode("utf-8", "replace")
        if sp and "<urlset" in sp:
            print("  取到 sitemap（方式: %s，%d 字节，%d 个 URL）" % (opener, len(sp), sp.count("<loc>")))
            break
        print("  方式 %s 未取到有效 sitemap" % opener)
    except Exception as e:
        print("  方式 %s 失败: %s" % (opener, e))
for slug in SLUGS:
    for pre in ["blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"]:
        loc = "https://taigetag.com/%s%s" % (pre, slug)
        print("  %s %s" % ("OK " if sp and "<loc>%s</loc>" % loc in sp else "缺失", loc))

print("== headless Chrome 六语渲染 ==")
for slug in SLUGS:
    for lang in LANGS:
        url = "%s?lang=%s&v=1" % (BASE % ("blog/" + slug), lang)
        title, h1 = chrome_title(url)
        print("  [%s|%s] title=%s\n             h1=%s" % (lang, slug[:22], title[:110], h1[:70]))
