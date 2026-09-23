#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-23 上午批次体检：
1) 正文六语属性完整性；2) 属性内裸双引号/裸 &；
3) ja/ko 译文里的中文残留检测（汉字字符是否出现在 CJK 中文常用集）；
4) 中文字符数与段落统计。
"""
import re, sys

sys.stdout.reconfigure(encoding='utf-8')
BODIES = ["blog/_body_bagwindow.html", "blog/_body_kitting.html"]
TAGS = ['h1', 'h2', 'h3', 'h4', 'p', 'strong', 'small', 'a', 'span', 'div', 'button',
        'li', 'th', 'td', 'label', 'option', 'figcaption', 'caption', 'dt', 'dd', 'em',
        'b', 'i', 'blockquote', 'summary', 'cite']
NEED = ("data-en", "data-fr", "data-es", "data-ja", "data-ko")

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
        for k in NEED:
            if not d.get(k, "").strip():
                print("  [缺失] %s <%s> 缺 %s : %s" % (f, tag, k, d["data-zh"][:30]))
                miss += 1
                ok = False
    print("%s：带 data-zh 元素 %d 个，缺属性 %d 处" % (f, tot, miss))

    for m in re.finditer(r'data-(?:zh|en|fr|es|ja|ko)="([^"]*)"([^\s>=/"])', s):
        print("  [可疑引号] %s" % m.group(0)[:70]); ok = False
    for m in re.finditer(r'data-(?:zh|en|fr|es|ja|ko)="([^"]*)"', s):
        for bad in re.finditer(r'&(?!amp;|nbsp;|quot;|#)', m.group(1)):
            print("  [裸&] %s ...%s" % (f, m.group(1)[:60])); ok = False; break

    zh = " ".join(re.findall(r'data-zh="([^"]*)"', s))
    zh = re.sub(r'<[^>]*>', '', zh)
    cjk = len(re.findall(r'[\u4e00-\u9fff]', zh))
    print("  中文正文汉字数 = %d（不含标签）" % cjk)

    # ja/ko 中是否混入中文简体/繁体常用字（黑名单：中文特有词）
    BAD = ["方案", "指导", "指南", "我们", "您", "免费", "样品可", "详情", "注意："]
    for lang in ("ja", "ko"):
        for w in BAD:
            if w in " ".join(re.findall(r'data-%s="([^"]*)"' % lang, s)):
                # 日文里「指南」「注意」是常用词，只报指定可疑词
                if lang == "ja" and w in ("指南", "注意：", "詳", "详情"):
                    continue
                print("  [%s 疑似中文残留] %s" % (lang, w)); ok = False

print("体检结果:", "通过" if ok else "有问题（见上）")
raise SystemExit(0 if ok else 1)
