#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-05 上午批次：正文文件六语属性体检
- 每个带 data-zh 的元素必须同时有 data-en/ja/ko/fr/es
- data-en/fr/es/ko 不得含中日文字符（日文含假名+汉字，只查 en/fr/es/ko）
- 属性值里不得出现未转义的裸 & （应为 &amp;）
- 属性值里不得出现裸双引号（HTMLParser 会直接报错）
"""
import sys, re
from html.parser import HTMLParser

FILES = sys.argv[1:] or ["blog/_body_piping.html", "blog/_body_shoulderpad.html"]
LANGS = ["data-en", "data-ja", "data-ko", "data-fr", "data-es"]
CJK = re.compile(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]')
HANGUL = re.compile(r'[\uac00-\ud7af]')
KANA = re.compile(r'[\u3040-\u30ff]')
BAD_AMP = re.compile(r'&(?!(amp|lt|gt|quot|apos|nbsp|#\d+|#x[0-9a-fA-F]+);)')

problems = []


class P(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=False)
        self.path = path
        self.n_ok = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "data-zh" not in d:
            return
        missing = [k for k in LANGS if k not in d]
        if missing:
            problems.append("%s <%s> 缺 %s" % (self.path, tag, ",".join(missing)))
            return
        self.n_ok += 1
        for k in LANGS:
            v = d[k] or ""
            if not v.strip():
                problems.append("%s <%s> %s 为空" % (self.path, tag, k))
            if k == "data-ja":
                continue
            if CJK.search(v):
                problems.append("%s <%s> %s 含中日文字符: %s" % (self.path, tag, k, v[:60]))
            if k in ("data-en", "data-fr", "data-es") and HANGUL.search(v):
                problems.append("%s <%s> %s 含韩文" % (self.path, tag, k))
            if k == "data-ko" and KANA.search(v):
                problems.append("%s <%s> %s 含日文假名" % (self.path, tag, k))
            m = BAD_AMP.search(v)
            if m:
                problems.append("%s <%s> %s 裸 & 未转义: ...%s..." % (self.path, tag, k, v[max(0, m.start() - 30):m.start() + 30]))
        # 可见文本非空
        txt = d.get("data-zh", "")
        if not txt.strip():
            problems.append("%s <%s> data-zh 空" % (self.path, tag))


for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = P(f)
    try:
        p.feed(s)
        p.close()
    except Exception as e:
        problems.append("%s 解析失败: %s" % (f, e))
    n_zh = len(re.findall(r'data-zh="', s))
    print("%-32s 六语齐备元素 %3d / data-zh 出现 %3d 处" % (f, p.n_ok, n_zh))
    if p.n_ok != n_zh:
        problems.append("%s 六语齐备(%d) != data-zh 总数(%d)" % (f, p.n_ok, n_zh))

print()
if problems:
    print("发现问题 %d 个：" % len(problems))
    for x in problems[:60]:
        print("  -", x)
    sys.exit(1)
print("体检通过：六语属性齐备、无语言串味、无裸 & 。")
