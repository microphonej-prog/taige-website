#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-16 20:00 批次：线上验证（无头 Chrome 六语 DOM title + h1 + 线上 sitemap）"""
import os, re, sys, subprocess, html

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
V = "164"
SLUGS = ["trim-shipment-insurance-claims-guide.html", "conflict-minerals-trims-guide.html"]
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
                       errors="replace", timeout=180)
    return r.stdout or ""


print("== 线上六语 DOM title / h1 ==")
targets = []
for s in SLUGS:
    targets.append(("blog/%s" % s, "https://taigetag.com/blog/%s?v=%s" % (s, V)))
    for l in LANGS:
        targets.append(("%s/blog/%s" % (l, s), "https://taigetag.com/%s/blog/%s?v=%s" % (l, s, V)))

for path, url in targets:
    exp_t, exp_h = local_title(path), local_h1(path)
    d = dom(url)
    gt = re.search(r"<title[^>]*>(.*?)</title>", d, re.S)
    gt = re.sub(r"\s+", " ", gt.group(1)).strip() if gt else "(无)"
    gh = re.search(r"<h1[^>]*>(.*?)</h1>", d, re.S)
    gh = re.sub(r"\s+", " ", gh.group(1)).strip() if gh else "(无)"
    ok = (html.unescape(gt) == html.unescape(exp_t)) and (html.unescape(gh) == html.unescape(exp_h))
    print(("  OK  " if ok else "  FAIL") + "  " + url)
    if ok:
        print("        title: %s" % gt[:80])
    else:
        print("        want title: %s\n        got  title: %s" % (exp_t, gt))
        print("        want h1   : %s\n        got  h1   : %s" % (exp_h, gh))
        fail.append(url)

print("== 线上 sitemap ==")
tmp = "C:/Users/micro/taige-website/_live_sitemap_20261016_2000.xml"
subprocess.run(["curl", "-sSL", "--noproxy", "*", "-o", tmp, "https://taigetag.com/sitemap.xml"], timeout=180)
sm = open(tmp, encoding="utf-8", errors="replace").read()
print("   线上 sitemap 字节:", len(sm), " <loc> 数:", sm.count("<loc>"))
for s in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % s] + ["https://taigetag.com/%s/blog/%s" % (l, s) for l in LANGS]:
        ok = "<loc>%s</loc>" % u in sm
        print(("  OK  " if ok else "  FAIL") + "  线上 sitemap 含 %s" % u)
        if not ok:
            fail.append(u)

print("== 线上页面 HTML 抽查 ==")
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
