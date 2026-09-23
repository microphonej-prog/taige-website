#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查繁体转换的二次运行差异（判断 s2t 是否幂等 / 有无简体残留）"""
import os, re, sys, importlib.util
sys.stdout.reconfigure(encoding='utf-8')
spec = importlib.util.spec_from_file_location("tt", os.path.join(os.getcwd(), "to_traditional.py"))
mod = importlib.util.module_from_spec(spec)
mod.APPLY = False
spec.loader.exec_module(mod)

FILES = sys.argv[1:]
for f in FILES:
    s0 = open(f, encoding="utf-8").read()
    s1 = mod.convert_html(s0)
    diffs = [(a, b) for a, b in zip(re.findall(r'[\u4e00-\u9fff]{1,12}', s0),
                                    re.findall(r'[\u4e00-\u9fff]{1,12}', s1)) if a != b]
    print("=== %s  长度 %d -> %d  差异片段 %d" % (f, len(s0), len(s1), len(diffs)))
    for a, b in diffs[:15]:
        print("   %s  ->  %s" % (a, b))
