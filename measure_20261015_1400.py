#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""desc / title 长度体检"""
import os, re, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
sys.path.insert(0, ROOT)
from daily_meta_20261015_1400 import ARTICLES

for a in ARTICLES:
    print("==", a["slug"])
    for k in ["title_zh", "title_en", "h1_zh"]:
        print("   %-9s len=%d  %s" % (k, len(a[k]), a[k][:90]))
    for k in ["desc_zh", "desc_en", "desc_ja", "desc_ko", "desc_fr", "desc_es"]:
        print("   %-8s len=%d" % (k, len(a[k])))
