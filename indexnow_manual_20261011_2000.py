#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""手动向 IndexNow 提交本批次 12 个新 URL（六语 × 2 篇），用于核对真实 HTTP 返回码。

用法: F:/hermes/venvs/tools/Scripts/python.exe indexnow_manual_20261011_2000.py
说明: GH Actions「Ping Search Engines」在 push 时已自动全量提交；本脚本为独立复核。
"""
import json
import urllib.request

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["apparel-label-barcode-printing-guide.html", "trim-odor-solvent-residue-guide.html"]
LANGS = ["", "en/", "ja/", "ko/", "fr/", "es/"]
URLS = ["https://taigetag.com/%sblog/%s" % (l, s) for s in SLUGS for l in LANGS]

payload = json.dumps({
    "host": "taigetag.com",
    "key": KEY,
    "keyLocation": "https://taigetag.com/%s.txt" % KEY,
    "urlList": URLS,
}).encode("utf-8")

req = urllib.request.Request("https://api.indexnow.org/indexnow", data=payload,
                            headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        print("IndexNow HTTP %d（200/202 = 提交被接受），共 %d 个 URL" % (r.status, len(URLS)))
except urllib.error.HTTPError as e:
    print("IndexNow HTTP %d" % e.code)

try:
    with urllib.request.urlopen("https://taigetag.com/%s.txt" % KEY, timeout=60) as r:
        body = r.read().decode("utf-8").strip()
        print("密钥文件 HTTP %d，内容匹配=%s" % (r.status, body == KEY))
except urllib.error.HTTPError as e:
    print("密钥文件 HTTP %d" % e.code)
