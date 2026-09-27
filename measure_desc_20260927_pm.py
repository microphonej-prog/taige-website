#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""desc_en 长度体检（目标 150-160 字符）"""
cands = {
    "art1_current": "A spare button bag is one of the first things a shopper touches. This guide covers four formats, sizes worked back from contents, printing and child safety rules.",
    "art1_v1": "A spare button bag is often the first thing a shopper touches. This guide covers four formats, sizes worked back from contents, printing and child safety rules.",
    "art1_v2": "A spare button bag is often the first thing a shopper touches. This guide covers four formats, sizes worked back from contents, printing and child safety.",
    "art2_current": "How to score trim suppliers: on-time rate, defect rate, response speed and documents, plus weights, tiers and how scores drive order allocation, improvements and backups.",
    "art2_v1": "How to score trim suppliers: on-time rate, defect rate, response speed and documents, plus weights, tiers and how scores drive order allocation and backups.",
    "art2_v2": "How to score trim suppliers: on-time rate, defect rate, response speed and documents, plus weights, tiers and how scores drive order allocation and backups in trim.",
    "art2_v3": "How to score trim suppliers: on-time rate, defect rate, response speed and documents, plus weights, tiers and how scores drive order allocation, backups.",
}
for k, v in cands.items():
    print("%-14s %d  %s" % (k, len(v), v))
