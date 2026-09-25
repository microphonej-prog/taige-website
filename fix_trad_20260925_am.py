#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补跑一次 s2t 繁体转换（幂等），修正首轮遗漏的字符"""
import importlib.util

spec = importlib.util.spec_from_file_location("to_traditional", "to_traditional.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

TARGETS = ["blog/nonwoven-canvas-bag-guide.html", "blog/certification-claims-label-guide.html",
           "blog/index.html"]
for p in TARGETS:
    s0 = open(p, encoding="utf-8").read()
    s1 = mod.convert_html(s0)
    if s1 != s0:
        open(p, "w", encoding="utf-8", newline="").write(s1)
        print("已修正 %s（%d -> %d 字符）" % (p, len(s0), len(s1)))
    else:
        print("无需改动 %s" % p)
