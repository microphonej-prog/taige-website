#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-16 14:00 批次：线上验证（无头 Chrome 六语 DOM title + h1 + 线上 sitemap + BUST 抽查）"""
import os, re, sys, subprocess, html

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
V = "162"
SLUGS = ["adaptive-accessible-clothing-trims-guide.html", "modest-wear-hijab-trims-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
DATE = "2026-10-16"
fail = []


def local_title(path):
    s = open(path, encoding="utf-8").read()
    return re.sub(r"\s+", " ", re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1)).strip()


def local_h1(path):
    s = open(path, encoding="utf-8").read()
    m = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def dom(url):
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=12000",
                        "--dump-dom", url], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=120)
    return r.stdout or ""


print("== 线上六语 DOM title / h1 ==")
targets = []
for s in SLUGS:
    targets.append(("blog/%s" % s, "https://taigetag.com/blog/%s?v=%s" % (s, V)))
    for l in LANGS:
        targets.append(("%s/blog/%s" % (l, s), "https://taigetag.com/%s/blog/%s?v=%s" % (l, s, V)))

for path, url in targets:
    exp_t = local_title(path)
    exp_h = local_h1(path)
    d = dom(url)
    got_t = re.search(r"<title[^>]*>(.*?)</title>", d, re.S)
    got_t = re.sub(r"\s+", " ", got_t.group(1)).strip() if got_t else "(无)"
    got_h = re.search(r"<h1[^>]*>(.*?)</h1>", d, re.S)
    got_h = re.sub(r"\s+", " ", got_h.group(1)).strip() if got_h else "(无)"
    ok = (html.unescape(got_t) == html.unescape(exp_t)) and (html.unescape(got_h) == html.unescape(exp_h))
    print(("  OK  " if ok else "  FAIL") + "  " + url)
    if not ok:
        print("        want title: %s" % exp_t)
        print("        got  title: %s" % got_t)
        print("        want h1   : %s" % exp_h)
        print("        got  h1   : %s" % got_h)
        fail.append(url)

print("== 线上 sitemap ==")
tmp = "C:/Users/micro/taige-website/_live_sitemap_20261016_1400.xml"
subprocess.run(["curl", "-sSL", "--noproxy", "*", "-o", tmp, "https://taigetag.com/sitemap.xml"],
               timeout=180)
sm = open(tmp, encoding="utf-8", errors="replace").read()
print("   线上 sitemap 字节:", len(sm), " <loc> 数:", sm.count("<loc>"))
for s in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % s] + ["https://taigetag.com/%s/blog/%s" % (l, s) for l in LANGS]:
        ok = "<loc>%s</loc>" % u in sm
        print(("  OK  " if ok else "  FAIL") + "  线上 sitemap 含 %s" % u)
        if not ok:
            fail.append(u)
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    m = re.search(r"<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
    ok = bool(m) and m.group(1) == DATE
    print(("  OK  " if ok else "  FAIL") + "  线上 blog index lastmod %s = %s" % (u, m.group(1) if m else "?"))
    if not ok:
        fail.append(u)

print("== 线上页面 HTML 抽查（BUST 版本） ==")
for s in SLUGS:
    for l in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
        u = "https://taigetag.com/%sblog/%s?v=%s" % (l, s, V)
        r = subprocess.run(["curl", "-sS", "--noproxy", "*", "-o", "-", u],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
        ok = "js/main.js?v=" in r.stdout and len(r.stdout.encode("utf-8")) > 20000
        print(("  OK  " if ok else "  FAIL") + "  %s 线上 HTML %d 字节" % (u, len(r.stdout.encode("utf-8"))))
        if not ok:
            fail.append(u)

print()
print("FAIL 数:", len(fail))
for f in fail:
    print("  -", f)
sys.exit(1 if fail else 0)
