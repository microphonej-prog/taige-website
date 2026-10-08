#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""直接向 IndexNow 提交本次新增的 12 个 URL，确认密钥文件有效、端点返回 200/202。"""
import json, urllib.request, urllib.error

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["wooden-bamboo-hang-tags.html", "print-on-demand-apparel-labels.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
urls = []
for s in SLUGS:
    urls.append("https://taigetag.com/blog/%s" % s)
    for l in LANGS:
        urls.append("https://taigetag.com/%s/blog/%s" % (l, s))

ktxt = "https://taigetag.com/%s.txt" % KEY
try:
    r = urllib.request.urlopen(urllib.request.Request(ktxt, headers={"User-Agent": "Mozilla/5.0"}), timeout=60)
    body = r.read().decode("utf-8", "replace").strip()
    print("密钥文件 %s -> HTTP %s ; 内容匹配=%s" % (ktxt, r.status, body == KEY))
except Exception as e:
    print("密钥文件读取失败:", e)

payload = json.dumps({"host": "taigetag.com", "key": KEY, "keyLocation": ktxt, "urlList": urls}).encode("utf-8")
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=payload,
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    r = urllib.request.urlopen(req, timeout=90)
    print("IndexNow 提交 %d 个 URL -> HTTP %s（202/200 = 成功）" % (len(urls), r.status))
except urllib.error.HTTPError as e:
    print("IndexNow HTTP %s : %s" % (e.code, e.read()[:200]))
except Exception as e:
    print("IndexNow 提交异常:", e)
