#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-28 晚间批次预检：正文源文件 + 文章元数据（六语）静态体检。"""
import re, os, sys
from daily_meta_20260928_evening import ARTICLES

SIMP_ONLY = set("产个门这说关时长场应该对让从为发处于单价线织衬复货买质检标记给过还样种类"
                "设备库图术语识别级题问结构档书报议讲归认录")

BODIES = [a["body"] for a in ARTICLES]
bad = 0

print("== 1) 正文源文件预检 ==")
for f in BODIES:
    s = open(f, encoding="utf-8").read()
    bare_amp = [m.start() for m in re.finditer(r'&(?!amp;|nbsp;|quot;|#\d+;|lt;|gt;)', s)]
    empty_attr = re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"', s)
    empty = [x for x in empty_attr if x.endswith('=""')]
    attr_tail = re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)
    odd = s.count('"') % 2
    tags = len(re.findall(r'<(?:p|li|td|th|h2|h3|div|a)\b', s))
    print("  %-26s 元素 %3d；裸 & %d；空属性 %d；属性后裸字符 %d；引号奇偶 %d"
          % (os.path.basename(f), tags, len(bare_amp), len(empty), len(attr_tail), odd))
    for i in bare_amp[:5]:
        print("    裸 & : ...%s..." % s[max(0, i - 70):i + 70].replace("\n", " "))
    for t in attr_tail[:5]:
        print("    属性后裸字符: %s" % t[:100])
    bad += len(bare_amp) + len(empty) + len(attr_tail) + odd

    for lang in ("ja", "ko"):
        for m in re.finditer(r'data-%s="([^"]*)"' % lang, s):
            hits = sorted(set(ch for ch in m.group(1) if ch in SIMP_ONLY))
            if hits:
                bad += 1
                print("    !! %s 含简体字形 %s : %s" % (lang, hits, m.group(1)[:70]))

print("== 2) 元数据（title / h1 / crumb / tag / desc）体检 ==")
for a in ARTICLES:
    print("  %s" % a["slug"])
    print("    desc 长度: zh=%d en=%d ja=%d ko=%d fr=%d es=%d"
          % (len(a["desc_zh"]), len(a["desc_en"]), len(a["desc_ja"]),
             len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))
    print("    title 长度: zh=%d en=%d ja=%d ko=%d fr=%d es=%d"
          % (len(a["title_zh"]), len(a["title_en"]), len(a["title_ja"]),
             len(a["title_ko"]), len(a["title_fr"]), len(a["title_es"])))
    for key, val in a.items():
        if not isinstance(val, str):
            continue
        if '"' in val:
            bad += 1
            print("    !! %s 含裸双引号" % key)
        if re.search(r'&(?!amp;|nbsp;|quot;|#\d+;)', val):
            bad += 1
            print("    !! %s 含裸 &" % key)
        if key in ("title_ja", "desc_ja", "h1_ja", "crumb_ja", "tag_ja",
                   "title_ko", "desc_ko", "h1_ko", "crumb_ko", "tag_ko"):
            hits = sorted(set(c for c in val if c in SIMP_ONLY))
            if hits:
                bad += 1
                print("    !! %s 含简体字形 %s" % (key, hits))
    if not (80 <= len(a["desc_zh"]) <= 130):
        print("    ~ desc_zh 长度提示 %d（参考 80-130）" % len(a["desc_zh"]))
    if not (145 <= len(a["desc_en"]) <= 165):
        print("    ~ desc_en 长度提示 %d（参考 150-160 字符）" % len(a["desc_en"]))

print("\n结论: 预检问题 = %d" % bad)
raise SystemExit(1 if bad else 0)
