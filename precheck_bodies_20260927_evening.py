#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-27 晚间批次：正文源文件预检（六语属性、引号、裸 &、ja/ko 误用简体字形/汉字）。"""
import re, sys, collections

BODIES = ["blog/_body_socialaudit.html", "blog/_body_pricevalid.html"]
SIMP_ONLY = set("产个门这说关时长场应该对让从为发处于单价线织衬复货买质检标记给过还样种类"
                "设备库图术语识别级题问结构档书报议讲归认录机经验获营类")

bad = 0
for f in BODIES:
    s = open(f, encoding="utf-8").read()
    bare_amp = [m.start() for m in re.finditer(r'&(?!amp;|nbsp;|quot;|#\d+;|lt;|gt;)', s)]
    empty_attr = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    attr_tail = re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)
    print("%s: %d 字节；裸 & %d；空 data-* %d；属性后裸字符 %d；双引号奇偶 %d"
          % (f, len(s.encode("utf-8")), len(bare_amp), len(empty_attr), len(attr_tail), s.count('"') % 2))
    for i in bare_amp[:5]:
        print("   裸 & 上下文: ...%s..." % s[max(0, i - 60):i + 60].replace("\n", " "))
    for t in attr_tail[:5]:
        print("   属性后裸字符: %s" % t[:100])
    tags = re.findall(r'<\s*([a-zA-Z][a-zA-Z0-9]*)', s)
    print("   标签种类: %s" % sorted(set(t.lower() for t in tags)))
    print("   带 data-zh 的元素数 %d" % len(re.findall(r'data-zh=', s)))
    bad += len(bare_amp) + len(empty_attr) + len(attr_tail) + s.count('"') % 2

    for lang in ("ja", "ko"):
        for m in re.finditer(r'data-%s="([^"]*)"' % lang, s):
            v = m.group(1)
            hits = sorted(set(ch for ch in v if ch in SIMP_ONLY))
            if hits:
                bad += 1
                print("   !! %s 含简体/繁体误用字形 %s : %s" % (lang, hits, v[:80]))
            if lang == "ko":
                han = sorted(set(ch for ch in v if "\u4e00" <= ch <= "\u9fff"))
                if han:
                    bad += 1
                    print("   !! ko 含汉字 %s : %s" % (han, v[:80]))

print("\n预检问题合计 = %d" % bad)
sys.exit(1 if bad else 0)
