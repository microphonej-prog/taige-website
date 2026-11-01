#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-01 14:00 批次：手动 IndexNow 提交本批 12 个新 URL（Bing/Yandex/Seznam）。"""
import json, subprocess

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["phthalate-free-apparel-packaging.html", "garment-packaging-for-returns.html"]
urls = []
for s in SLUGS:
    urls.append("https://taigetag.com/blog/" + s)
    for l in ["en", "ja", "ko", "fr", "es"]:
        urls.append("https://taigetag.com/%s/blog/%s" % (l, s))

payload = {"host": "taigetag.com", "key": KEY,
           "keyLocation": "https://taigetag.com/%s.txt" % KEY,
           "urlList": urls}
open("F:/hermes/cache/scratch/indexnow_20261101_1400.json", "w", encoding="utf-8").write(json.dumps(payload))

r = subprocess.run(["curl", "--noproxy", "*", "-s", "-o", "/dev/null", "-w", "%{http_code}",
                    "-X", "POST", "https://api.indexnow.org/indexnow",
                    "-H", "Content-Type: application/json; charset=utf-8",
                    "-d", "@F:/hermes/cache/scratch/indexnow_20261101_1400.json"],
                   capture_output=True, text=True)
print("URL 数:", len(urls))
print("IndexNow HTTP", r.stdout, r.stderr[:200])
