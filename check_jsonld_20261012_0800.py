#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 12 个新页面的 JSON-LD 合法性（json.loads）"""
import re, json

SLUGS = ["hang-tag-folding-types.html", "retail-floor-ready-apparel-packaging.html"]
LANGS = ["", "en", "ja", "ko", "fr", "es"]
bad = 0
for s in SLUGS:
    for l in LANGS:
        p = ("%s/blog/%s" % (l, s)) if l else "blog/%s" % s
        src = open(p, encoding="utf-8").read()
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', src, re.S)
        assert len(blocks) == 1, "%s JSON-LD 块数量 %d" % (p, len(blocks))
        try:
            d = json.loads(blocks[0])
        except Exception as e:
            bad += 1
            print("× JSON 解析失败", p, e)
            continue
        types = [n.get("@type") for n in d.get("@graph", [])]
        names = [n.get("headline") or n.get("name") for n in d.get("@graph", [])]
        print("OK", p, types, "|", (names[0] or "")[:46])
print("JSON-LD 非法文件数：", bad)
