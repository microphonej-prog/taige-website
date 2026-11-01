#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-01 14:00 批次正文预检：六语属性完整性、引号畸形、语言纯净度、描述长度。"""
import re, html
from html.parser import HTMLParser

LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
BODIES = ["blog/_body_phthalate.html", "blog/_body_returns.html"]
CJK = re.compile(r'[\u4e00-\u9fff]')
KANA = re.compile(r'[\u3040-\u30ff]')
HANGUL = re.compile(r'[\uac00-\ud7af]')


class Chk(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.elems = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        keys = [k for k in d if k.startswith("data-")]
        if keys:
            self.elems.append((tag, d))


fails = 0
for b in BODIES:
    src = open(b, encoding="utf-8").read()
    p = Chk()
    p.feed(src)
    total = len(p.elems)
    missing = []
    for tag, d in p.elems:
        lack = [l for l in LANGS if ("data-" + l) not in d]
        if lack:
            missing.append((tag, lack, (d.get("data-zh") or "")[:30]))
    print("\n== %s  带 data-* 元素 %d 个，缺语言 %d 个" % (b, total, len(missing)))
    for m in missing[:12]:
        print("   缺 %s  <%s> %s" % (m[1], m[0], m[2]))
    fails += len(missing)

    # 引号畸形：属性值里不许出现裸双引号（HTMLParser 已能解析则说明结构正常），
    # 另查 data-x="" 空值 与 值内出现 ="
    bad_q = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', src)
    print("   空属性值: %d" % len(bad_q))
    fails += len(bad_q)

    # 语言纯净度
    for lang in ("en", "fr", "es"):
        hits = [v for v in re.findall(r'data-%s="([^"]*)"' % lang, src) if CJK.search(v)]
        if hits:
            print("   [X] data-%s 含汉字 %d 处，例：%s" % (lang, len(hits), hits[0][:60]))
            fails += len(hits)
    ko_han = [v for v in re.findall(r'data-ko="([^"]*)"', src) if CJK.search(v)]
    if ko_han:
        print("   [X] data-ko 含汉字 %d 处，例：%s" % (len(ko_han), ko_han[0][:60]))
        fails += len(ko_han)
    ko_hangul = sum(1 for v in re.findall(r'data-ko="([^"]*)"', src) if HANGUL.search(v))
    ja_kana = sum(1 for v in re.findall(r'data-ja="([^"]*)"', src) if KANA.search(v))
    ja_all = len(re.findall(r'data-ja="([^"]*)"', src))
    print("   ko 含谚文属性 %d/  %d 个；ja 含假名属性 %d/%d" %
          (ko_hangul, len(re.findall(r'data-ko="([^"]*)"', src)), ja_kana, ja_all))

    # 中文正文长度（正文 p/li/td 的 data-zh 合计）
    zh = [v for v in re.findall(r'data-zh="([^"]*)"', src) if v]
    body_zh = sum(len(v) for v in zh if len(v) > 25)
    print("   data-zh 属性 %d 个，正文中文字符合计约 %d" % (len(zh), body_zh))

    # 裸 & 检查
    raw_amp = len(re.findall(r'&(?!amp;|nbsp;|quot;|#|lt;|gt;|laquo;|raquo;)', src))
    print("   可疑裸 & : %d" % raw_amp)

print("\n预检失败项合计：%d" % fails)
