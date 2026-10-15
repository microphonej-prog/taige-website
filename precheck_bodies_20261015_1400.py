#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-15 14:00 批次：正文预检
1) HTMLParser 逐 start tag 校验六语属性齐全
2) 属性值内裸露 ASCII 双引号检测（解析器会截断，是移动端崩溃元凶）
3) 中文正文长度体检
"""
import os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
FILES = sys.argv[1:] or ["blog/_body_ribbon.html", "blog/_body_greenclaims.html"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []
        self.texts = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs), self.getpos()[0]))

    def handle_data(self, data):
        self.texts.append(data)


bad_total = 0
for path in FILES:
    s = open(path, encoding="utf-8").read()
    p = P()
    p.feed(s)
    missing, empty, susp = [], [], []
    for tag, attrs, ln in p.tags:
        has = [k for k in attrs if k.startswith("data-") and k.split("-")[1] in LANGS]
        if not has:
            continue
        for l in LANGS:
            if ("data-%s" % l) not in attrs:
                missing.append((ln, tag, l, attrs.get("data-zh", "")[:30]))
            elif not attrs["data-%s" % l].strip():
                empty.append((ln, tag, l))
    # 裸 ASCII 双引号：属性值里出现 " 说明属性被截断
    for tag, attrs, ln in p.tags:
        for k, v in attrs.items():
            if k.startswith("data-") and v is not None and '"' in v:
                susp.append((ln, tag, k, v[:80]))
    # 属性含未转义 &（后面不接实体）
    amp = []
    for tag, attrs, ln in p.tags:
        for k, v in attrs.items():
            if k.startswith("data-") and v is not None:
                for m in re.finditer(r"&(?!(amp|lt|gt|quot|nbsp|#\d+|#x[0-9a-fA-F]+);)", v):
                    amp.append((ln, tag, k, v[max(0, m.start() - 20):m.start() + 20]))
                    break
    zh_text = "".join(p.texts)
    zh_chars = len(re.findall(r"[\u4e00-\u9fff]", zh_text))
    print("%-38s tags=%3d 带data=%3d 缺属性=%d 空值=%d 裸引号=%d 裸&=%d 中文字数=%d"
          % (os.path.basename(path), len(p.tags),
             sum(1 for t, a, l in p.tags if any(k.startswith("data-") for k in a)),
             len(missing), len(empty), len(susp), len(amp), zh_chars))
    for m in missing[:12]:
        print("   缺 data-%s @line %d <%s> zh=%s" % (m[2], m[0], m[1], m[3]))
    for e in empty[:12]:
        print("   空值 data-%s @line %d <%s>" % (e[2], e[0], e[1]))
    for x in susp[:12]:
        print("   裸引号 %s @line %d <%s> %s" % (x[2], x[0], x[1], x[3]))
    for a in amp[:12]:
        print("   裸& %s @line %d <%s> ...%s..." % (a[2], a[0], a[1], a[3]))
    bad_total += len(missing) + len(empty) + len(susp) + len(amp)
print("总计问题:", bad_total)
sys.exit(1 if bad_total else 0)
