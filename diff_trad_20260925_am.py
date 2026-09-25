#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""找出根目录页里 s2t 仍会改动的位置"""
import importlib.util, difflib, sys

spec = importlib.util.spec_from_file_location("to_traditional", "to_traditional.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

for p in sys.argv[1:]:
    s0 = open(p, encoding="utf-8").read()
    s1 = mod.convert_html(s0)
    if s0 == s1:
        print("== %s 无需改动" % p)
        continue
    print("== %s 有 %d 处差异" % (p, sum(1 for a, b in zip(s0, s1) if a != b)))
    sm = difflib.SequenceMatcher(None, s0, s1)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        print("   %s: %r -> %r" % (tag, s0[max(0, i1 - 40):i2 + 40], s1[max(0, j1 - 40):j2 + 40]))
