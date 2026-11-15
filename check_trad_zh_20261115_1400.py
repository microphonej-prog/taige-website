# -*- coding: utf-8 -*-
"""检查 data-zh 值与标签间可见中文是否有简体专用字（新页两篇）。"""
import re

SIMP = set("这说时对发标签质图华术应检验织唛价钱费运达设厂记录国际业务标准规格价线选择单关门问题动员双双边边设备")
FILES = ["blog/clothing-tagging-gun-swift-tack-guide.html",
         "blog/garment-label-font-size-legibility-guide.html"]

for f in FILES:
    s = open(f, encoding="utf-8").read()
    bad = {}
    for v in re.findall(r'data-zh="([^"]*)"', s):
        for ch in v:
            if ch in SIMP:
                bad.setdefault(ch, []).append(v[:50])
    print(f, "> data-zh 简体可疑:", {k: len(v) for k, v in bad.items()} or "无")
    for k, v in list(bad.items())[:3]:
        print("   ", k, v[:3])
