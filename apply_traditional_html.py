#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""只对指定 HTML 文件做简体→繁体转换（复用 to_traditional.convert_html），不动 js/*.js。

用法: python apply_traditional_html.py <file.html> [file2.html ...]
"""
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("tt", "to_traditional.py")
tt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tt)

for f in sys.argv[1:]:
    if f.startswith('--'):
        continue
    s0 = open(f, encoding='utf-8').read()
    s = tt.convert_html(s0)
    if s != s0:
        open(f, 'w', encoding='utf-8', newline='').write(s)
    print('%s -> %s' % (f, '已转换' if s != s0 else '无变化'))
print('统计:', tt.STATS)
