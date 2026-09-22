#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""运行前体检 v2：
1) 正文六语属性完整性；2) 属性内裸双引号；
3) 用已有线上 ja/ko 译文语料做字符差异检测（新译文里出现语料中从未用过的字符 = 疑似中文残留）。
"""
import re, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')
BODIES = {"blog/_body_dpp.html": None, "blog/_body_carbon.html": None}
TAGS = ['h1', 'h2', 'h3', 'h4', 'p', 'strong', 'small', 'a', 'span', 'div', 'button',
        'li', 'th', 'td', 'label', 'option', 'figcaption', 'caption', 'dt', 'dd', 'em',
        'b', 'i', 'blockquote', 'summary', 'cite']

# 语料：所有已上线 blog 文章（排除本次新文件）
files = subprocess.run(["git", "ls-files", "blog/*.html"], capture_output=True,
                       text=True).stdout.split()
corpus = {"ja": set(), "ko": set()}
for f in files:
    base = f.split("/")[-1]
    if base in ("_body_dpp.html", "_body_carbon.html"):
        continue
    s = open(f, encoding="utf-8").read()
    for m in re.finditer(r'data-(ja|ko)="([^"]*)"', s):
        corpus[m.group(1)].update(m.group(2))
print("语料字符数 ja=%d ko=%d （来自 %d 个文件）" % (len(corpus["ja"]), len(corpus["ko"]), len(files)))

ok = True
for f in BODIES:
    s = open(f, encoding="utf-8").read()
    tot = miss = 0
    for m in re.finditer(r'<([a-zA-Z0-9]+)((?:\s+[a-zA-Z-]+="[^"]*")*)\s*/?>', s):
        tag, attrs = m.group(1).lower(), m.group(2)
        if tag not in TAGS:
            continue
        d = dict(re.findall(r'([a-zA-Z-]+)="([^"]*)"', attrs))
        if "data-zh" not in d:
            continue
        tot += 1
        for k in ("data-en", "data-fr", "data-es", "data-ja", "data-ko"):
            if not d.get(k, "").strip():
                print("  [缺失] %s <%s> 缺 %s: %s" % (f, tag, k, d["data-zh"][:28]))
                miss += 1
                ok = False
    bare = len(re.findall(r'="[^"]*"[^"<>=]*"', ''))
    print("%s：带 data-zh 元素 %d 个，缺属性 %d 处" % (f, tot, miss))
    # 裸双引号（属性值内出现 " 后再接 " 的畸形模式）
    for m in re.finditer(r'data-(?:zh|en|fr|es|ja|ko)="([^"]*)"([^\s>=/"])', s):
        print("  [可疑引号] %s ...%s" % (f, m.group(0)[:60]))
        ok = False
    # 字符差异检测
    for lang in ("ja", "ko"):
        used = set()
        for m in re.finditer(r'data-%s="([^"]*)"' % lang, s):
            used.update(m.group(1))
        novel = sorted(c for c in used if c not in corpus[lang] and c.strip() and not c.isascii())
        # 只报 CJK / 全角标点类
        novel = [c for c in novel if not c.isascii()]
        if novel:
            print("  [%s 语料未见字符] %s" % (lang, " ".join(novel)))
            for c in novel:
                for m in re.finditer(r'data-%s="([^"]*)"' % lang, s):
                    if c in m.group(1):
                        print("      → %s" % m.group(1)[:80])
                        break
            ok = False

print("体检结果:", "通过" if ok else "有问题（见上）")
