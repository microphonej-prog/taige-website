#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全站 ja/ko 完整性校验（HTMLParser 版，正确处理含引号/内联标签的属性值）

对每个已补 data-ja 的文件，与 git HEAD 版本对比：
  1. 计数 zh == ja == ko
  2. data-ja/data-ko 值内无裸 " 或 '
  3. HEAD 里的 (data-zh/en/fr/es 属性, 值) 序列必须是当前文件的**有序子序列**
     （即：只在原有基础上新增，不允许改动或删除既有值）
  4. 可见文本序列与 HEAD 完全一致（排除 script/style/svg）
用法: python verify_all_ja_ko.py [glob...]
"""
import re, subprocess, glob, sys
from html.parser import HTMLParser

SKIP = {'script', 'style', 'svg'}


class Cap(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.texts = []
        self.attrs = []
        self.depth_skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.depth_skip += 1
        d = dict(attrs)
        for a in ('zh', 'en', 'fr', 'es', 'ja', 'ko'):
            k = 'data-' + a
            if k in d:
                self.attrs.append((a, d[k]))

    def handle_endtag(self, tag):
        if tag in SKIP and self.depth_skip:
            self.depth_skip -= 1

    def handle_data(self, data):
        if self.depth_skip:
            return
        t = data.strip()
        if t:
            self.texts.append(re.sub(r'\s+', ' ', t))


def cap(s):
    c = Cap()
    c.feed(s)
    return c


def head_of(p):
    return subprocess.check_output(['git', 'show', 'HEAD:' + p.replace(chr(92), '/')]).decode('utf-8')


def is_subseq(small, big):
    it = iter(big)
    return all(any(x == y for y in it) for x in small)


def main(patterns):
    files = []
    for pat in patterns:
        files += sorted(glob.glob(pat))
    done = [p for p in files if 'data-ja="' in open(p, encoding='utf-8').read()]
    print('待检文件数: %d（已补 ja: %d）' % (len(files), len(done)))
    bad, added_total = [], 0
    for p in done:
        s = open(p, encoding='utf-8').read()
        cur, head = cap(s), cap(head_of(p))
        c = {a: len(re.findall(r'data-%s="' % a, s)) for a in ('zh', 'ja', 'ko')}
        q = [v for v in re.findall(r'data-(?:ja|ko)="([^"]*)"', s, re.S) if '"' in v or "'" in v]
        ha = [(a, v) for a, v in head.attrs if a in ('zh', 'en', 'fr', 'es')]
        ca = [(a, v) for a, v in cur.attrs if a in ('zh', 'en', 'fr', 'es')]
        problems = []
        if not (c['zh'] == c['ja'] == c['ko']):
            problems.append('计数 %s' % c)
        if q:
            problems.append('引号异常 %d' % len(q))
        if not is_subseq(ha, ca):
            problems.append('原有 zh/en/fr/es 值被改动或删除')
        if cur.texts != head.texts:
            problems.append('可见文本与 HEAD 不一致')
        added_total += len(ca) - len(ha)
        if problems:
            bad.append((p, problems))
    print('原有属性新增总数（zh/en/fr/es 侧，含主页面有意补齐）:', added_total)
    print('异常文件数:', len(bad))
    for p, pr in bad[:20]:
        print('  !!', p, pr)
    print('全部通过 ✅' if not bad else '存在异常 ⚠️')
    return 1 if bad else 0


if __name__ == '__main__':
    pats = sys.argv[1:] or ['index.html', 'products.html', 'about.html', 'contact.html', 'blog/*.html']
    sys.exit(main(pats))
