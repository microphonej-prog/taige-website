#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-14 下午批次：正文预检
1) HTMLParser 逐 start tag 校验六语属性齐全
2) 空属性 / 属性值内裸露双引号残留检测
3) 中文正文长度体检（与近期文章对比）
"""
import os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

LANGS = ["zh", "en", "ja", "ko", "fr", "es"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []       # (tag, {attr:val}, lineno)
        self.texts = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs), self.getpos()[0]))

    def handle_data(self, data):
        self.texts.append(data)


def check(path):
    s = open(path, encoding="utf-8").read()
    p = P()
    p.feed(s)
    missing = []
    empty = []
    for tag, attrs, ln in p.tags:
        has = [k for k in attrs if k.startswith("data-") and k.split("-")[1] in LANGS]
        if not has:
            continue
        for l in LANGS:
            if ("data-%s" % l) not in attrs:
                missing.append((ln, tag, l, attrs.get("data-zh", "")[:30]))
            elif not attrs["data-%s" % l].strip():
                empty.append((ln, tag, l))
    # 属性值内裸双引号：解析器不会报错，但值会被截断，表现为值以 " 结尾异常/过短
    susp = []
    for tag, attrs, ln in p.tags:
        for k, v in attrs.items():
            if k.startswith("data-") and v is not None:
                if v.count('"') or v.count("'") > 4:
                    susp.append((ln, tag, k, v[:60]))
    zh_text = "".join(t for t in p.texts)
    zh_chars = len(re.findall(r"[\u4e00-\u9fff]", zh_text))
    print("%-40s tags=%3d 带data标签=%3d 缺属性=%d 空值=%d 可疑引号=%d 中文字数=%d"
          % (os.path.basename(path), len(p.tags),
             sum(1 for t, a, l in p.tags if any(k.startswith("data-") for k in a)),
             len(missing), len(empty), len(susp), zh_chars))
    for m in missing[:10]:
        print("   缺 data-%s @line %d <%s> zh=%s" % (m[2], m[0], m[1], m[3]))
    for e in empty[:10]:
        print("   空值 data-%s @line %d <%s>" % (e[2], e[0], e[1]))
    for x in susp[:10]:
        print("   可疑引号 %s @line %d <%s> %s" % (x[2], x[0], x[1], x[3]))
    return len(missing) + len(empty)


bad = 0
for f in ["blog/_body_storage.html", "blog/_body_hometextile.html",
          "blog/_body_apron.html", "blog/_body_nlcomp.html"]:
    if os.path.exists(f):
        bad += check(f)
print("总计问题:", bad)
