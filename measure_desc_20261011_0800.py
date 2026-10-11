#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""微调 desc 长度：中文 80-120 字，英文 150-160 字符。"""
import re

cands = {
    "pfas_en": [
        "PFAS guide for apparel trims: EU PFHxA limits from October 2026, California and New York thresholds, where fluorine hides, and fluorine-free options.",
        "PFAS guide for apparel trims: EU PFHxA limits from October 2026, California and New York thresholds, where fluorine hides in trims, and alternatives.",
        "PFAS guide for apparel trims: EU PFHxA limits from October 2026, California and New York state thresholds, where fluorine hides, and fluorine-free options.",
    ],
    "flr_en": [
        "EU Forced Labour Regulation guide for apparel trims: the 14 December 2027 product ban, how authorities investigate, and the six documents to prepare.",
        "EU Forced Labour Regulation guide for apparel trims: the 14 December 2027 product ban, how national authorities investigate, and the documents to prepare.",
        "EU Forced Labour Regulation guide for apparel trims: the 14 December 2027 product ban, how authorities investigate, and the six files to get ready now.",
    ],
    "flr_zh": [
        "欧盟强迫劳动条例 (EU) 2024/3015 指南：2027 年 12 月 14 日起产品禁令怎么执行、主管机关调查与 30 个工作日下架期限、与 UFLPA 和 CSDDD 的分工、辅料供应商为何被问、客户资料清单与常见缺口，以及 2027 年前可以落地的六项准备。来自东莞泰阁包装。",
    ],
    "pfas_zh": [
        "PFAS 限制与服装辅料合规指南：欧盟 PFHxA 限值 2026 年 10 月起适用于服装配件鞋类、美国加州 AB 1817 与纽约州法门槛怎么算、辅料含氟的七个位置、总有机氟与靶向分析怎么选、无氟替代路线与成本，附客户文件清单。来自东莞泰阁包装。",
    ],
}
for k, vs in cands.items():
    for v in vs:
        if k.endswith("_zh"):
            n = len(re.findall(r"[\u4e00-\u9fff]", v))
            print("%-8s 汉字=%3d  总长=%3d  %s" % (k, n, len(v), v[:40]))
        else:
            print("%-8s 字符=%3d  %s" % (k, len(v), v[:60]))
