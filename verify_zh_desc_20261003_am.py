#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-03 上午批次补充校验：线上 zh 根页 description（带 data-* 属性）长度 + 渲染后 title/desc 对照"""
import re, subprocess

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE = "https://taigetag.com"
PAGES = ["blog/leather-garment-trims-guide.html", "blog/childrenswear-trims-guide.html"]
for p in PAGES:
    url = "%s/%s?lang=zh&v=132" % (BASE, p)
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=12000",
                        "--dump-dom", url], capture_output=True, text=True, encoding="utf-8", errors="replace")
    dom = r.stdout or ""
    m = re.search(r'<meta name="description"[^>]*?content="([^"]*)"', dom, re.S)
    d = m.group(1) if m else "NONE"
    print("%s\n  desc(%d): %s" % (p, len(d), d[:150]))
    t = re.search(r"<title[^>]*>(.*?)</title>", dom, re.S)
    print("  title: %s" % (t.group(1).strip() if t else "NONE"))
