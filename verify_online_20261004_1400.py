#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证：sitemap 含 12 个新 URL + 无头 Chrome 渲染六语 title + 各语言页 HTTP 200。"""
import subprocess, re, sys, os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CURL = ["curl", "-sS", "--noproxy", "*", "--resolve", "taigetag.com:443:185.199.108.153"]
SLUGS = ["garment-drawcord-guide.html", "lace-trimming-guide.html"]
LANGS = [("zh", ""), ("en", "en/"), ("ja", "ja/"), ("ko", "ko/"), ("fr", "fr/"), ("es", "es/")]
PAGES = [("https://taigetag.com/blog/%s" % s) for s in SLUGS]

print("== 1) 线上 sitemap ==")
r = subprocess.run(CURL + ["https://taigetag.com/sitemap.xml"], capture_output=True, text=True, encoding="utf-8")
sm = r.stdout
print("   HTTP 内容长度=%d  <loc> 总数=%d" % (len(sm), sm.count("<loc>")))
miss = 0
for s in SLUGS:
    for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
        u = "https://taigetag.com/%s%s" % (pre, s)
        if "<loc>%s</loc>" % u not in sm:
            miss += 1
            print("   缺失: %s" % u)
print("   12 个新 URL 缺失数 = %d" % miss)

print("== 2) 线上六语 DOM title（无头 Chrome） ==")
bad = 0
for url in PAGES:
    for code, prefix in LANGS:
        u = url.replace("/blog/", "/%sblog/" % prefix) + "?lang=%s&v=1" % code
        p = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=12000", "--dump-dom", u],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        m = re.search(r"<title[^>]*>(.*?)</title>", p.stdout, re.S)
        t = (m.group(1).strip() if m else "NO TITLE")
        ok = "TAGE" in t
        bad += 0 if ok else 1
        print("   [%s] %-44s %s %s" % (code, u.split("taigetag.com")[1][:44], "OK " if ok else "BAD", t[:70]))

print("== 3) 线上新页 HTTP 状态 ==")
st_bad = 0
for url in PAGES:
    for code, prefix in LANGS:
        u = url.replace("/blog/", "/%sblog/" % prefix)
        r = subprocess.run(CURL + ["-o", os.devnull, "-w", "%{http_code}", u],
                           capture_output=True, text=True)
        http = r.stdout.strip()
        if http != "200":
            st_bad += 1
        print("   %-3s %-44s -> %s" % (code, u.split("taigetag.com")[1][:44], http))

print("\ntitle 异常数 = %d ; sitemap 缺失 = %d ; 非 200 数 = %d" % (bad, miss, st_bad))
sys.exit(1 if (bad or miss or st_bad) else 0)
