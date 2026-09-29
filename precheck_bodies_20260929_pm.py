#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""正文文件体检：六语属性完整性、引号畸形、裸 &、默认中文正文字数。"""
import re, sys, io, os
from html.parser import HTMLParser
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILES = ['blog/_body_continuity.html', 'blog/_body_comm.html']
BAD_ATTR = re.compile(r'data-(zh|en|ja|ko|fr|es)="[^"]*"[A-Za-z]')
ok = True
for f in FILES:
    s = open(f, encoding='utf-8').read()
    print("=" * 72)
    print(f, "%d KB" % (len(s.encode('utf-8')) // 1024))
    print("  开头: %r" % s[:40])
    print("  结尾: %r" % s[-30:])
    if not s.startswith('  <section class="article-body">'):
        print("  !! 开头缩进不对"); ok = False
    if not s.rstrip('\n').endswith('</section>'):
        print("  !! 结尾不是 </section>"); ok = False
    cnt = {}
    for a in ('zh', 'en', 'ja', 'ko', 'fr', 'es'):
        cnt[a] = len(re.findall(r'data-%s=' % a, s))
    print("  属性数:", cnt)
    if len(set(cnt.values())) != 1:
        print("  !! 六语属性数量不一致"); ok = False
    empt = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    print("  空属性: %d ; 属性值后裸字符: %d ; 裸&: %d ; 属性内换行: %d"
          % (len(empt), len(BAD_ATTR.findall(s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s)),
             len(re.findall(r'data-[a-z]+="[^"]*\n[^"]*"', s))))
    if empt or BAD_ATTR.findall(s) or re.findall(r'&(?!amp;|nbsp;|quot;|#)', s):
        ok = False

    # 默认文本（元素之间的中文）字数
    txt = re.sub(r'<[^>]+>', ' ', s)
    txt = re.sub(r'data-[a-z-]+="[^"]*"', ' ', txt, flags=re.S)
    zh = len(re.findall(r'[\u4e00-\u9fff]', txt))
    print("  默认可见正文汉字数: %d" % zh)

    class P(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=False); self.tags = []
        def handle_starttag(self, tag, attrs):
            d = {k.lower(): (v or '') for k, v in attrs}
            self.tags.append((tag, d))
    p = P(); p.feed(s)
    zh_tags = [(t, a) for t, a in p.tags if 'data-zh' in a]
    miss = []
    for t, a in zh_tags:
        for need in ('data-en', 'data-ja', 'data-ko', 'data-fr', 'data-es'):
            if not a.get(need, '').strip():
                miss.append((t, need))
    print("  article-body 标签 %d 个（带 data-zh %d 个），缺其它语言 %d 处 %s"
          % (len(p.tags), len(zh_tags), len(miss), miss[:6]))
    if miss:
        ok = False
print("\n体检结论:", "通过" if ok else "有问题")
raise SystemExit(0 if ok else 1)
