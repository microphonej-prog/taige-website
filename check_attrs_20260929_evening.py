#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-29 晚间批次：正文片段的六语属性/引号/转义自检（跑在生成之前）"""
import re, sys

FILES = ["blog/_body_shrinkage.html", "blog/_body_measure.html"]
LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
bad = 0

for f in FILES:
    s = open(f, encoding="utf-8").read()
    counts = {}
    for l in LANGS:
        counts[l] = len(re.findall(r'data-%s="' % l, s))
    same = len(set(counts.values())) == 1
    print("%-34s %s  %s" % (f, counts, "OK 六语属性数一致" if same else "!!! 数量不一致"))
    if not same:
        bad += 1

    # 1) 属性值内裸双引号：出现 ="" 或者 值结尾紧跟 attr 名
    dq = re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[^\s>/]', s)
    if dq:
        print("   !! 属性后紧跟可疑字符 %d 处，例：%s" % (len(dq), dq[:3]))
        bad += 1

    # 2) 空属性
    empty = re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)
    if empty:
        print("   !! 空属性 %d 处" % len(empty))
        bad += 1

    # 3) 未转义的 &（不是实体）
    amp = re.findall(r'&(?!(?:amp|nbsp|quot|lt|gt|#\d+|hellip|mdash|ndash|rsquo|lsquo|ldquo|rdquo|middot|times|deg|eacute|egrave|agrave|ccedil|ecirc|ocirc|ucirc|iacute|oacute|aacute|eacute|ntilde|uuml|ouml|auml);)', s)
    if amp:
        print("   !! 疑似裸 & %d 处" % len(amp))
        bad += 1

    # 4) 元素上的 data-zh 是否都至少有 en/fr/es/ja/ko 同元素（粗检：按标签块统计）
    tags = re.findall(r'<(p|li|h2|h3|td|th|div|span|a)\b([^>]*data-(?:zh|en|fr|es|ja|ko)=[^>]*)>', s)
    missing = []
    for name, attrs in tags:
        if 'data-zh=' in attrs:
            miss = [l for l in LANGS if ('data-%s="' % l) not in attrs]
            if miss:
                missing.append((name, miss, attrs[:70]))
    if missing:
        print("   !! 缺语种元素 %d 处：" % len(missing))
        for m in missing[:8]:
            print("      ", m)
        bad += 1

    # 5) 结构完整性
    for token in ['<section class="article-body">', '</section>', 'class="cta-box"', '相关文章']:
        if token not in s:
            print("   !! 缺少 %s" % token)
            bad += 1

    print("   h2 小节数 %d，表格 %d 个，链接 %d 个，字节 %d"
          % (s.count("<h2 "), s.count("<table>"), len(re.findall(r'<a href=', s)), len(s.encode())))

print("\n结论：", "全部通过" if bad == 0 else "%d 项待修" % bad)
sys.exit(1 if bad else 0)
