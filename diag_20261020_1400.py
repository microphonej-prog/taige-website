#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, sys
sys.path.insert(0, ".")
from daily_meta_20261020_1400 import ARTICLES

a = ARTICLES[0]
raw = open("en/blog/%s" % a["slug"], encoding="utf-8").read()
body = raw[raw.index('class="article-body"'):]
txt = re.sub(r"<[^>]+>", "\x00", body)
for m in re.finditer(r"[\u4e00-\u9fff]+", txt):
    st = max(0, m.start() - 80)
    print("命中: %r" % m.group(0))
    print("  上下文: %s" % txt[st:m.end() + 40].replace("\x00", " | "))

print("\n--- fr desc 对比 ---")
r = open("fr/blog/%s" % a["slug"], encoding="utf-8").read()
got = re.search(r'<meta name="description"[^>]*content="([^"]*)"', r, re.S).group(1)
exp = a["desc_fr"]
print("期望(%d): %s" % (len(exp), exp))
print("实际(%d): %s" % (len(got), got))
for i in range(min(len(exp), len(got))):
    if exp[i] != got[i]:
        print("首个差异 @%d: 期望 %r vs 实际 %r" % (i, exp[max(0, i-20):i+20], got[max(0, i-20):i+20]))
        break
