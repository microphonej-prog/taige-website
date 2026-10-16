#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修正后线上复查：韩语页正文无汉字、BUST_VERSION=165、两页六语 title 仍正常"""
import subprocess, re
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["trim-shipment-insurance-claims-guide.html", "conflict-minerals-trims-guide.html"]
fail = []
def curl(u):
    r = subprocess.run(["curl", "-sS", "--noproxy", "*", "-o", "-", u], capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=120)
    return r.stdout
# 1) 韩语页汉字
for s in SLUGS:
    t = curl("https://taigetag.com/ko/blog/%s?v=165" % s)
    body = t.split('class="article-body"', 1)[1].split("</section>", 1)[0] if 'class="article-body"' in t else ""
    han = re.findall(r"[\u4e00-\u9fff]", body)
    print(("  OK  " if not han else "  FAIL") + "  ko 页 %s 正文汉字 %d %s" % (s, len(han), "".join(han[:10])))
    if han: fail.append("ko " + s)
# 2) BUST_VERSION 165 + 页面 title 六语
for s in SLUGS:
    for l in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
        u = "https://taigetag.com/%sblog/%s?v=165" % (l, s)
        d = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=12000",
                            "--dump-dom", u], capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=180).stdout or ""
        tt = re.search(r"<title[^>]*>(.*?)</title>", d, re.S)
        tt = re.sub(r"\s+", " ", tt.group(1)).strip() if tt else "(无)"
        bust = 'v=165' in d or 'BUST_VERSION' in d
        ok = bool(tt) and tt != "(无)"
        print(("  OK  " if ok else "  FAIL") + "  %s  title: %s" % (u, tt[:70]))
        if not ok: fail.append(u)
m = curl("https://taigetag.com/js/main.js")
print("  线上 main.js BUST_VERSION =", (re.search(r'var BUST_VERSION = "(\d+)"', m) or ["?", "?"])[1])
print("\nFAIL:", len(fail), fail)
