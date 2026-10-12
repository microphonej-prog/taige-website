#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第二轮候选关键词覆盖扫描（裤装 / 穿绳服务 / 打托 / 尺码贴 等）"""
import os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
FILES = sorted(glob.glob("blog/*.html"))
KW = [
    "西裤", "长裤", "休闲裤", "裤头", "裤腰", "裤袋", "裤袢", "裤耳", "皮标", "皮牌",
    "预穿", "穿好绳", "散装", "成包", "零售挂装",
    "打托", "pallet", "Pallet", "栈板", "托盘化", "缠绕膜", "缠绕",
    "尺码贴", "尺码条", "尺码环", "size sticker", "size strip", "尺码标签贴",
    "形式发票", "PI", "proforma", "Proforma",
    "有机棉", "OCS", "RCS", "回收声明",
    "碳带", "标签打印机", "热敏", "自打印",
    "面料克重", "码重", "GSM",
    "腰头", "腰里", "门襟", "拉链门襟",
    "三标", "辅料三件套",
]


def count(kw):
    hits = []
    for f in FILES:
        s = open(f, encoding="utf-8", errors="ignore").read()
        if kw.lower() in s.lower():
            hits.append(os.path.basename(f))
    return hits


for kw in KW:
    h = count(kw)
    print("%-12s %3d  %s" % (kw, len(h), ", ".join(h[:8])))
