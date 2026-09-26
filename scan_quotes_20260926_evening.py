#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描正文源文件里「属性值/正文文本中的裸 ASCII 双引号」（移动端崩溃元凶）并定位。"""
import re, sys

CJK = r'[\u3000-\u303f\u4e00-\u9fff\uff00-\uffef]'

for f in sys.argv[1:]:
    s = open(f, encoding='utf-8').read()
    print("== %s  引号总数 %d (奇偶 %d)" % (f, s.count('"'), s.count('"') % 2))
    bad = 0
    for i, ch in enumerate(s):
        if ch != '"':
            continue
        prev = s[i - 1] if i else ''
        prev2 = s[i - 2:i] if i >= 2 else ''
        nxt = s[i + 1] if i + 1 < len(s) else ''
        # 正常的属性开引号： ="
        if prev == '=':
            continue
        # 正常的属性闭引号：后面是 > 或空白 或 / 或另一个属性开头（前一字符是 CJK 时才有风险）
        if nxt in '> \n' or prev in '> ':
            continue
        if re.match(CJK, prev) or re.match(CJK, nxt) or re.match(CJK, prev2[-1:] or ''):
            bad += 1
            line = s.count('\n', 0, i) + 1
            print("  嫌疑 L%-4d ...%s..." % (line, s[max(0, i - 45):i + 45].replace('\n', ' ')))
    print("   合计嫌疑 %d" % bad)
