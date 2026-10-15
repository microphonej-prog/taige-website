#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-15 14:00 批次：候选选题覆盖度第三遍（按文件定位，六语）"""
import os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
files = []
for p in ["blog/*.html", "en/blog/*.html", "fr/blog/*.html", "es/blog/*.html",
          "ja/blog/*.html", "ko/blog/*.html"]:
    files += glob.glob(p)
files = [f for f in files if not os.path.basename(f).startswith("_body_")]
blob = "\n".join(open(f, encoding="utf-8").read() for f in files)

KEYS = ["袋布", "pocketing", "pocket bag", "領撐", "collar stay", "插骨",
        "漂綠", "greenwashing", "green claims", "綠色聲明", "環境聲明", "environmental claim",
        "誤導", "misleading", "2024/825", "賦權消費者",
        "租賃", "rental", "租借", "服裝租",
        "一次性", "disposable", "nonwoven gown", "不織布 防護",
        "醫用", "medical", "MDR", "EN 13795",
        "絲帶", "緞帶", "ribbon", "satin", "grosgrain", "velvet ribbon", "리본", "ruban",
        "蝴蝶結", "bow", "nœud", "lazo",
        "脣膏", "化妝",
        "領帶", "領結",
        "縫份", "seam",
        "熨燙",
        "掛繩", "lanyard", "頸繩",
        "布標 洗標 車縫 位置",
        "包裝 空隙", "void fill",
        "服裝 潮牌", "streetwear",
        "聯名", "collab",
        "限量 吊牌", "limited edition tag",
        ]
for k in KEYS:
    n = blob.count(k)
    hits = []
    for f in files:
        c = open(f, encoding="utf-8").read().count(k)
        if c and "/" not in f.replace("blog/", ""):
            pass
    if n < 60:
        for f in files:
            if "/" in f:
                continue
            c = open(f, encoding="utf-8").read().count(k)
            if c:
                hits.append("%s(%d)" % (os.path.basename(f), c))
    print("%-22s %6d  %s" % (k, n, ", ".join(hits[:6])))
