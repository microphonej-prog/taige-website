#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""候选选题关键词全站覆盖扫描（2026-10-12 14:00 批次）
统计每个候选关键词在 blog/*.html（含 _body_*.html）中出现的文件数，用于判断选题是否空白。
"""
import os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

FILES = sorted(glob.glob("blog/*.html"))
KW = [
    "吊粒", "穿绳", "串装", "挂绳服务", "T恤", "卫衣", "连衣裙", "裤装", "牛仔裤",
    "灯箱", "对色", "Pantone", "潘通", "色卡", "Delta E", "色差",
    "GRS", "再生涤纶", "rPET", "再生纱", "有机棉", "FSC",
    "AATCC", "ISO 6330", "耐洗", "水洗测试", "缩水率",
    "打托", "托盘", "栈板", "拼柜", "拼箱", "集装箱",
    "形式发票", "装箱单", "报关", "原产地",
    "检针", "金属探测", "异物",
    "抗菌", "防螨", "抗静电", "防水", "防污",
    "尺码贴", "尺码圈", "size strip", "数字尺码",
    "吊牌绳", "棉绳", "弹力绳", "线圈",
    "洗唛", "主唛", "成分标",
    "二维码", "溯源", "防伪",
    "打样费", "样品费", "开发费",
    "版权", "字体授权", "商标授权",
    "BOM", "物料清单",
    "快递袋", "邮购袋", "气泡袋",
    "吊牌克重", "铜版纸", "棉纸", "石头纸",
    "车缝", "缝制位置", "缝纫",
    "半成品", "备料", "常备库存",
    "防霉", "防潮", "干燥剂",
    "标签打印机", "热转印", "碳带",
]

counts = {}
for kw in KW:
    hits = []
    for f in FILES:
        s = open(f, encoding="utf-8", errors="ignore").read()
        if kw.lower() in s.lower():
            hits.append(f)
    counts[kw] = hits

for kw in KW:
    hits = counts[kw]
    print("%-12s %3d 个文件  %s" % (kw, len(hits), ", ".join(os.path.basename(h) for h in hits[:6])))
