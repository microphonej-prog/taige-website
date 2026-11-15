# -*- coding: utf-8 -*-
"""校验两篇新文章的 zh 属性是否为繁体（opencc s2t 转换后应不变），并统计属性覆盖。"""
import html
import re
import sys

from opencc import OpenCC

cc = OpenCC("s2t")
FILES = ["blog/woven-label-loom-types-guide.html", "blog/trim-attachment-strength-pull-test-guide.html"]
LANGS = ["zh", "en", "fr", "es", "ja", "ko"]

for f in FILES:
    s = open(f, encoding="utf-8").read()
    zh_vals = re.findall(r'data-zh="([^"]*)"', s)
    changed = []
    for v in zh_vals:
        t = html.unescape(v)
        conv = cc.convert(t)
        if conv != t:
            changed.append((t[:40], conv[:40]))
    print(f, "data-zh 元素数:", len(zh_vals), "需转繁:", len(changed))
    for a, b in changed[:8]:
        print("   ", a, "->", b)
    # 属性覆盖：每个含 data-zh 的标签是否六语齐全
    miss = []
    for m in re.finditer(r"<(\w+)(\s[^>]*data-zh=\"[^\"]*\"[^>]*)>", s):
        tag = m.group(0)
        for l in LANGS:
            if ('data-%s="' % l) not in tag:
                miss.append((m.group(1), l))
    print("   缺语言属性:", len(miss), miss[:6])
    # 可见中文残留数（正文标签间文本含中文即正常，仅统计缺少 data-en 的元素）
    print("   h2 数:", len(re.findall(r"<h2 ", s)), " 表格行:", len(re.findall(r"<tr>", s)),
          " 内链:", len(re.findall(r'href="[\w-]+\.html"', s)))
