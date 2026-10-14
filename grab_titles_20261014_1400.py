#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""提取候选内链文章的多语 h1，用于正文「相关文章」区块"""
import os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

CANDS = ["garment-trims-inventory-management", "garment-moisture-proof-packaging",
         "textile-phenolic-yellowing-guide", "trim-odor-solvent-residue-guide",
         "hang-tag-lamination-guide", "poly-bag-thickness-guide",
         "care-label-fabric-content", "garment-packaging-guide",
         "clothing-label-compliance-usa", "paper-bag-lamination-finishing",
         "garment-moisture-proof-packaging", "clothing-size-label-guide",
         "retail-floor-ready-apparel-packaging", "poly-bag-suffocation-warning-guide"]

for c in CANDS:
    p = "blog/%s.html" % c
    if not os.path.exists(p):
        print("MISSING", p)
        continue
    s = open(p, encoding="utf-8").read()
    m = re.search(r'<h1 ([^>]*)>', s, re.S)
    attrs = m.group(1)
    out = {}
    for k in ["zh", "en", "ja", "ko", "fr", "es"]:
        mm = re.search(r'data-%s="([^"]*)"' % k, attrs)
        out[k] = mm.group(1) if mm else "??"
    print("##", c)
    for k in ["zh", "en", "ja", "ko", "fr", "es"]:
        print("   %s = %s" % (k, out[k]))
