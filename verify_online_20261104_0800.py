#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-04 08:00 批次线上校验：
1) 无头 Chrome 抓 ?lang=xx&v=1 的 title（验证语言跳转与渲染）
2) curl（--resolve 直连 Pages IP）抓静态语言页 title
3) 线上 sitemap.xml 含 12 个新 URL
4) 六语 blog/index.html 均含两篇新卡片
用法: F:/hermes/venvs/tools/Scripts/python.exe verify_online_20261104_0800.py
"""
import re, subprocess, sys

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["apparel-trims-nearshoring-sourcing-guide.html",
         "apparel-unboxing-packaging-design-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
HOST = "taigetag.com"
IP = "185.199.108.153"
fails = []


def dump(url):
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--virtual-time-budget=12000",
           "--dump-dom", "--no-proxy-server", url]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=90)
    return r.stdout or ""


def title_of(html):
    m = re.search(r'<title[^>]*>(.*?)</title>', html, re.S)
    return (m.group(1).strip() if m else "NONE")


def curl(url):
    cmd = ["curl", "-s", "--noproxy", "*", "--resolve", "%s:443:%s" % (HOST, IP), url]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=90)
    return r.stdout


print("== 1) 无头 Chrome：?lang 跳转后的 title ==")
for slug in SLUGS:
    for lang in ["zh", "en", "ja", "ko", "fr", "es"]:
        url = "https://%s/blog/%s?lang=%s&v=1" % (HOST, slug, lang)
        t = title_of(dump(url))
        print("  %-46s lang=%-2s -> %s" % (slug[:46], lang, t[:70]))
        if t == "NONE" or len(t) < 10:
            fails.append("Chrome title 异常 %s lang=%s" % (slug, lang))
        if lang in ("en", "fr", "es") and re.search(r'[\u4e00-\u9fff]', t):
            fails.append("title 混入中文 %s lang=%s" % (slug, lang))

print("\n== 2) 静态语言页 title（curl 直连） ==")
for slug in SLUGS:
    for lang in LANGS:
        url = "https://%s/%s/blog/%s?cb=0800" % (HOST, lang, slug)
        t = title_of(curl(url))
        print("  %-3s %-40s -> %s" % (lang, slug[:40], t[:64]))
        if t == "NONE":
            fails.append("静态页 title 缺失 %s/%s" % (lang, slug))
        if lang in ("en", "fr", "es", "ko") and re.search(r'[\u4e00-\u9fff]', t):
            fails.append("静态 title 混入中文 %s %s" % (lang, slug))

print("\n== 3) 线上 sitemap ==")
sm = curl("https://%s/sitemap.xml?cb=0800" % HOST)
print("  size=%d  <loc>=%d" % (len(sm), sm.count("<loc>")))
for slug in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % slug] + ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        if "<loc>%s</loc>" % u not in sm:
            fails.append("线上 sitemap 缺 %s" % u)
print("  12 个新 URL 检查完成")

print("\n== 4) 线上 blog 列表页卡片 ==")
for pre in ["", "en/", "fr/", "es/", "ja/", "ko/"]:
    html = curl("https://%s/%sblog/index.html?cb=0800" % (HOST, pre))
    hit = all(slug in html for slug in SLUGS)
    print("  %-3s index 含两篇=%s" % (pre or "zh", hit))
    if not hit:
        fails.append("线上 %sblog/index.html 缺卡片" % pre)

print("\n失败项：%d" % len(fails))
for f in fails:
    print("  [X]", f)
sys.exit(1 if fails else 0)
