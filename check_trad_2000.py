# -*- coding: utf-8 -*-
"""检查 body 文件：zh 值是否含简体字；ja/ko/fr/es/en 值是否误含汉字。"""
import importlib
import re
import sys

from opencc import OpenCC

cc = OpenCC("s2t")
MODS = [("body_20261115_2000_a","A1"), ("body_20261115_2000_b","A2")]
HAN = re.compile(r"[\u4e00-\u9fff]")

for name, var in MODS:
    m = importlib.import_module(name)
    blocks = getattr(m, var)
    print("=== %s  块数 %d" % (name, len(blocks)))
    for bi, blk in enumerate(blocks):
        kind = blk[0]
        items = []
        if kind == "table":
            items = [(("th", j), d) for j, d in enumerate(blk[1])] + \
                    [(("td", i, j), d) for i, row in enumerate(blk[2]) for j, d in enumerate(row)]
        elif kind in ("ul", "ol"):
            items = [(("li", j), d) for j, d in enumerate(blk[1])]
        else:
            items = [(("p",), blk[1])]
        for pos, d in items:
            for lang, v in d.items():
                if lang == "zh":
                    conv = cc.convert(v)
                    if conv != v:
                        diff = [(a, b) for a, b in zip(v, conv) if a != b]
                        print("  [%d]%s zh 简体→ %s" % (bi, pos, diff[:8]))
                elif lang in ("ja", "ko"):
                    # 日文汉字合法；韩文出现汉字（除括号内中文名）可疑
                    if lang == "ko" and HAN.search(v):
                        print("  [%d]%s ko 含汉字: %s" % (bi, pos, HAN.findall(v)[:6]))
                else:
                    if HAN.search(v):
                        print("  [%d]%s %s 含汉字: %s" % (bi, pos, lang, HAN.findall(v)[:6]))
print("done")
