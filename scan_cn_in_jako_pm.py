#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描 ja/ko 数据里夹带的「中文句子」痕迹：常见中文虚词与标点组合。"""
import re, sys

MARK = ["的", "了", "是", "我们", "你们", "这", "那", "与", "和", "很", "就要", "会能",
        "可以", "什么", "怎么", "因为", "所以", "但是", "并且", "而且", "一下", "一个",
        "不是", "还是", "需要", "进行", "问题", "情况", "完整", "不完整"]
for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    for lang in ("ja", "ko"):
        for m in re.finditer(r'data-%s="([^"]*)"' % lang, s):
            v = m.group(1)
            hits = [w for w in MARK if w in v]
            if hits:
                print("!! %s [%s] %s" % (f, lang, hits))
                print("   ", v[:150])
