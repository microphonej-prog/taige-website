#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查候选 desc_en 长度（目标 150–160 字符）"""
cands = [
 "How to store garment trims: what paper tags, woven labels, elastic, adhesives and metal each suffer from, plus humidity, light, FIFO and mould control.",
 "How to store garment trims: what paper tags, woven labels, elastic, adhesives and metal each suffer from, with humidity, light, FIFO and mould control.",
 "How to store garment trims and labels: what paper tags, woven labels, elastic, adhesives and metal each suffer from, with humidity, FIFO and mould control.",
 "Storing garment trims: what paper tags, woven labels, elastic, adhesives and metal each suffer from, plus humidity, light, FIFO and mould prevention.",
 "Home textile label and packaging guide: fibre content, origin, marking, dimensions and weight, after-wash stability, hospitality rules, tags and bands.",
 "Home textile label and packaging guide: fibre content, origin and marking, dimensions and weight, after-wash stability, hospitality, tags and bands.",
 "Home textile label and packaging guide: fibre content, origin, dimensions and weight, after-wash stability, hospitality and infant rules, tags and bands.",
 "Home textile label and packaging guide: fibre content, origin and marking, dimensions, after-wash stability, hospitality, infant rules, tags and bands.",
]
for c in cands:
    print("%3d  %s" % (len(c), c))
