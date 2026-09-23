#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-23 晚间批次：新增 12 个文件简体残留扫描（只查简体专有字）"""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

SIMP = "说这们与后里对业务类别签标签设计将样货单于价款发货验收须应记报设备厂商视频纸张质量产线设备" \
       "东营过还进运送递结构网点线面包邮费价格钱银铜铁铝合金铜软硬纸质" \
       "为什么要样么样怎么样为这为那建议应用开关闭长宽高时间问题无风"
SIMP_SET = set(SIMP)

SLUGS = ["sock-hosiery-trims-guide.html", "hat-scarf-gloves-trims-guide.html"]
FILES = ["blog/%s" % s for s in SLUGS] + ["%s/blog/%s" % (l, s) for l in ["en", "ja", "ko", "fr", "es"] for s in SLUGS] \
        + ["blog/index.html"] + ["%s/blog/index.html" % l for l in ["en", "ja", "ko", "fr", "es"]]

total = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    hits = {}
    for ch in set(re.findall(r'[\u4e00-\u9fff]', s)):
        if ch in SIMP_SET:
            hits[ch] = s.count(ch)
    tag = "OK" if not hits else "!!"
    print("%s %-56s %s" % (tag, f, hits if hits else ""))
    total += sum(hits.values())
print("\n简体专有字命中总数 = %d" % total)
sys.exit(1 if total else 0)
