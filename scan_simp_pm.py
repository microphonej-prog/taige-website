#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""列出目标文件里疑似简体字命中（不限前6条），用于与基线文章对比。"""
import re, sys

SIMP = "简买卖页标签纸钱设备级发明术类别针国际货币场内设计这为么应该还个们对时实网线质订购单价格层压缩华卫组织运输经过向导开关闭户头长东车马风飞鸟鱼"
for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    hits = []
    for ch in SIMP:
        for m in re.finditer(re.escape(ch), s):
            hits.append((ch, s[max(0, m.start() - 14):m.start() + 14].replace("\n", " ")))
    # 去掉 <style> 块内的命中（全站模板共用，不算问题）
    m = re.search(r"<style>.*?</style>", s, re.S)
    print("=== %s  命中=%d" % (f, len(hits)))
    for ch, ctx in hits:
        print("    [%s] ... %s ..." % (ch, ctx))
