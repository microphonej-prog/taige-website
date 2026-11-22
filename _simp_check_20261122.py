# -*- coding: utf-8 -*-
"""检查 body 模块里 data-zh 值是否混入简体字：用 OpenCC s2t 对比。"""
import sys, re
sys.path.insert(0, '.')
import body_20261122_0800_a as A
import body_20261122_0800_b as B

try:
    from opencc import OpenCC
except Exception as e:
    print('NO_OPENCC', e)
    raise SystemExit(0)

cc = OpenCC('s2t')
LANGS = ['zh', 'en', 'fr', 'es', 'ja', 'ko']


def texts(mod):
    yield 'TITLE', mod.TITLE
    yield 'DESC', mod.DESC
    yield 'H1', mod.H1
    yield 'DATE', mod.DATE
    yield 'CTA_P', mod.CTA_P
    yield 'CTA_BTN', mod.CTA_BTN
    for i, (kind, d) in enumerate(mod.BLOCKS):
        if kind == 'table':
            for j, th in enumerate(d['head']):
                yield 'BLOCK%d.head%d' % (i, j), th
            for r, row in enumerate(d['rows']):
                for c, td in enumerate(row):
                    yield 'BLOCK%d.r%dc%d' % (i, r, c), td
        elif kind == 'ul':
            for k, it in enumerate(d):
                yield 'BLOCK%d.item%d' % (i, k), it
        else:
            yield 'BLOCK%d' % i, d

for name, mod in (('A', A), ('B', B)):
    print('====', name, mod.SLUG)
    for pos, d in texts(mod):
        v = d['zh']
        conv = cc.convert(v)
        if conv != v:
            diffs = sorted({(a, b) for a, b in zip(v, conv) if a != b})
            print(' %-18s %s' % (pos, diffs))
