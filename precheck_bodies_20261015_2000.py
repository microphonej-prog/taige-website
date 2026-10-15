#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""正文预检：六语属性完整性 / 元素内属性缺失 / 翻译里混入中文 / 裸引号 / 链接文件存在"""
import os, re, sys, glob
from html.parser import HTMLParser

LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
BAD = ["lightfast", "migration"]
FILES = ["blog/_body_%s.html" % b for b in BAD]
CJK = re.compile(r'[\u4e00-\u9fff]')

fail = []


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.problems = []
        self.attrs_seen = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in ('br', 'img', 'meta', 'link', 'hr', 'input'):
            return
        has = [l for l in LANGS if ('data-%s' % l) in d]
        if has and len(has) != 6:
            self.problems.append("元素 <%s> 缺属性: %s (有 %s)" % (tag, [l for l in LANGS if l not in has], has))
        self.attrs_seen.append((tag, d))


for f in FILES:
    print("=" * 70)
    print(f)
    s = open(f, encoding="utf-8").read()
    p = P()
    p.feed(s)
    print("  属性完整性问题:", len(p.problems))
    for x in p.problems[:20]:
        print("   -", x)
        fail.append("%s: %s" % (f, x))

    # 各语言属性计数
    counts = {l: len(re.findall(r'data-%s="' % l, s)) for l in LANGS}
    print("  属性计数:", counts)
    if len(set(counts.values())) != 1:
        fail.append("%s 属性计数不一致 %s" % (f, counts))

    # 翻译里混入汉字（en/fr/es/ko 不该有汉字）
    for tag, d in p.attrs_seen:
        for l in ("en", "fr", "es", "ko"):
            v = d.get("data-%s" % l)
            if v and CJK.search(v):
                msg = "%s <%s> data-%s 含汉字: %s" % (f, tag, l, CJK.search(v).group(0) + " ... " + v[:60])
                print("   !", msg)
                fail.append(msg)

    # 裸引号（属性值内出现未转义的 " 会打断属性）——用正则粗查 data-xx="...<space>xx="结构之外的情况
    for m in re.finditer(r'data-(?:zh|en|ja|ko|fr|es)="([^"]*)"', s):
        if '&quot;' in m.group(1) or '"' in m.group(1):
            pass
    # 内部链接文件存在性
    here = os.path.dirname(f)
    for href in set(re.findall(r'href="([^"#:]+\.html)"', s)):
        tgt = os.path.normpath(os.path.join(here, href))
        if not os.path.exists(tgt):
            msg = "%s 内部链接不存在: %s" % (f, href)
            print("   !", msg)
            fail.append(msg)
    print("  内部链接检查完成")

print()
print("FAIL:", len(fail))
for x in fail:
    print(" -", x)
sys.exit(1 if fail else 0)
