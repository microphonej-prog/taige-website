#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""向 IndexNow 手动提交本批次 12 个新 URL，并打印返回码"""
import json, subprocess, os

SLUGS = ["garment-label-inhouse-printing-vs-outsourcing.html", "trim-order-currency-exchange-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
BASE = "https://taigetag.com"

urls = []
for s in SLUGS:
    urls.append("%s/blog/%s" % (BASE, s))
    for l in LANGS:
        urls.append("%s/%s/blog/%s" % (BASE, l, s))

payload = {
    "host": "taigetag.com",
    "key": KEY,
    "keyLocation": "%s/%s.txt" % (BASE, KEY),
    "urlList": urls,
}
p = r"C:\Users\micro\AppData\Local\Temp\indexnow_2100.json"
open(p, "w", encoding="utf-8").write(json.dumps(payload, ensure_ascii=False))
print("URL 数:", len(urls))

r = subprocess.run(["curl", "-s", "-o", os.devnull, "-w", "%{http_code}", "--noproxy", "*",
                    "-X", "POST", "https://api.indexnow.org/indexnow",
                    "-H", "Content-Type: application/json; charset=utf-8",
                    "--data-binary", "@" + p],
                   capture_output=True, text=True)
print("IndexNow HTTP", r.stdout.strip() or r.stderr.strip())
