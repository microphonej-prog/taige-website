#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查骨架中除 body 外是否残留针织专属文案"""
import re, sys
s = open('blog/knitwear-sweater-trims-guide.html', encoding='utf-8').read()
i0 = s.index('  <section class="article-body">')
i1 = s.index('\n</main>')
head, tail = s[:i0], s[i1:]
for name, part in (('HEAD/hero', head), ('TAIL', tail)):
    for m in re.finditer(r'針織|毛衫|毛衣|針織毛衣', part):
        a = max(0, m.start() - 90)
        print('[%s] ...%s...' % (name, part[a:m.end() + 90].replace('\n', ' ')))
print('--- HEAD 结构标签 ---')
for m in re.finditer(r'<(section|div|h1|h2|p|nav|link|script)[^>]{0,120}', head):
    t = m.group(0)
    if 'class=' in t or 'rel=' in t or 'src=' in t:
        print(' ', t[:150])
