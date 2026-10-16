#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, sys
for f in ['blog/trim-color-approval-process.html', 'blog/hang-tag-color-management.html',
          'blog/woven-label-color-matching.html', 'blog/paper-bag-handle-types.html',
          'blog/poly-bag-seal-types.html', 'blog/garment-packaging-transit-testing.html']:
    s = open(f, encoding='utf-8').read()
    print('=== %s ===' % f)
    for h in re.findall(r'<h2 data-zh="([^"]*)"', s):
        print('  H2:', h[:80])
    print('  光源=%d 异谱=%d 色差=%d 承重=%d 提手=%d 热封=%d 跌落=%d' % (
        s.count('光源'), s.count('异谱'), s.count('色差'), s.count('承重'),
        s.count('提手'), s.count('热封'), s.count('跌落')))
