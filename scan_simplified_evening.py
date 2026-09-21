#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描根目录页是否残留简体字（中文版应为繁体）。只列疑似简体字与其上下文。"""
import re, sys

SIMP = "简买卖页标签纸钱设备级发明术类别针国际货币场内设计这为么应该还个们对时实网线质订购单价格层压缩华卫组织运输经过向导开关闭户头长东车马风飞鸟鱼"
for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    hits = []
    for ch in SIMP:
        for m in re.finditer(re.escape(ch), s):
            hits.append((ch, s[max(0, m.start() - 12):m.start() + 12].replace("\n", " ")))
    print("%s  疑似简体字命中=%d" % (f, len(hits)))
    for ch, ctx in hits[:6]:
        print("    [%s] ... %s ..." % (ch, ctx))
