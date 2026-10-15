#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-15 下午批次：手动 IndexNow 提交本批 12 个新 URL（复核 GH Actions 结果）"""
import json, subprocess, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["ribbon-trims-guide.html", "eu-green-claims-apparel-labels.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
V = "160"

urls = []
for s in SLUGS:
    urls.append("https://taigetag.com/blog/%s?v=%s" % (s, V))
    for l in LANGS:
        urls.append("https://taigetag.com/%s/blog/%s?v=%s" % (l, s, V))
urls = [u.replace("?v=%s" % V, "") for u in urls]

payload = {"host": "taigetag.com", "key": KEY,
           "keyLocation": "https://taigetag.com/%s.txt" % KEY, "urlList": urls}
open("indexnow_20261015_1400.json", "w", encoding="utf-8").write(json.dumps(payload))
print("提交 URL 数:", len(urls))
r = subprocess.run(["curl", "-sS", "--noproxy", "*", "-X", "POST", "https://api.indexnow.org/indexnow",
                    "-H", "Content-Type: application/json; charset=utf-8",
                    "--data-binary", "@indexnow_20261015_1400.json",
                    "-o", "-", "-w", "\nIndexNow HTTP %{http_code}\n"],
                   capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
print(r.stdout.strip())
print(r.stderr.strip()[:300])
