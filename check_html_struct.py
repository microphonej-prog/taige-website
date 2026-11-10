#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全站 HTML 结构体检：报出标签不闭合 / 错配的页面，退出码 1 表示有坏页。
用法:
  python check_html_struct.py                # 扫全站
  python check_html_struct.py blog/x.html    # 只查指定文件
背景（2026-11-11）：每日文章构建脚本把骨架的 </div></section> 切掉了，13 篇文章 ×8 语
共 95 页结构破损；另外 data-zh 值里出现裸 ASCII 双引号会截断标签，症状同样是结构错乱。
发稿前跑一遍这个脚本，可当场拦住。
"""
import sys, os, glob
from html.parser import HTMLParser

VOID = {'img', 'br', 'meta', 'link', 'input', 'hr', 'source', 'area', 'base', 'col',
        'embed', 'param', 'track', 'wbr'}

class Bal(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            self.errors.append('mismatch </%s> at line %d' % (tag, self.getpos()[0]))
            while self.stack and self.stack.pop() != tag:
                pass

def scan(paths):
    bad = []
    for p in paths:
        b = Bal()
        with open(p, encoding='utf-8', errors='ignore') as f:
            b.feed(f.read())
        if b.errors or b.stack:
            bad.append((p, b.errors[:3], b.stack[:3]))
    return bad

if __name__ == '__main__':
    args = sys.argv[1:]
    if args:
        pages = [a for a in args if os.path.isfile(a)]
    else:
        pages = glob.glob('*.html') + glob.glob('blog/*.html')
        for l in ['en', 'de', 'ja', 'ko', 'fr', 'es', 'pt']:
            pages += glob.glob(l + '/*.html') + glob.glob(l + '/blog/*.html')
    bad = scan(pages)
    print('扫描 %d 页，结构异常 %d 页' % (len(pages), len(bad)))
    for p, e, st in bad[:40]:
        print('  %-58s %s %s' % (p, e, ('未闭合:' + ','.join(st)) if st else ''))
    sys.exit(1 if bad else 0)
