#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成前体检：两篇正文文件的六语属性完整性 / 引号嵌套 / 未转义 & / 非中文语种混入汉字"""
import re, sys
from html.parser import HTMLParser

BODIES = ["blog/_body_nonwoven.html", "blog/_body_certclaims.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
CJK = re.compile(r'[\u4e00-\u9fff]')

fails = 0
for b in BODIES:
    src = open(b, encoding="utf-8").read()

    class P(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=False)
            self.tags = []
            self.text = []

        def handle_starttag(self, tag, attrs):
            self.tags.append((tag, dict(attrs)))

        def handle_startendtag(self, tag, attrs):
            self.tags.append((tag, dict(attrs)))

        def handle_data(self, data):
            self.text.append(data)

    p = P()
    p.feed("<html>" + src + "</html>")
    p.close()

    missing = {}
    for tag, attrs in p.tags:
        has = [l for l in LANGS if ("data-" + l) in attrs]
        if not has:
            continue
        if len(has) != 6:
            missing.setdefault(tag, []).append(sorted(set(LANGS) - set(has)))

    empty = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', src)
    amp = re.findall(r'&(?!(?:amp|lt|gt|quot|nbsp|#\d+|#x[0-9a-fA-F]+);)', src)

    # 非中文语种里混入汉字（ja 允许汉字，ko/fr/es/en 不允许）
    mixed = []
    for lang in ["en", "ko", "fr", "es"]:
        for m in re.finditer(r'data-%s="([^"]*)"' % lang, src):
            v = m.group(1)
            hit = CJK.findall(v)
            if hit:
                mixed.append((lang, "".join(hit[:8])))

    print("=== %s ===" % b)
    print("  六语元素总数：%d" % sum(1 for t, a in p.tags if "data-zh" in a))
    print("  缺语言的元素：%d %s" % (sum(len(v) for v in missing.values()), missing))
    print("  空 data 属性：%d ；未转义 & ：%d" % (len(empty), len(amp)))
    print("  非中文语种混入汉字：%d %s" % (len(mixed), mixed[:10]))
    zh_text = "".join(p.text)
    print("  正文中文字数：%d" % len(CJK.findall(zh_text)))
    if missing or empty or amp or mixed:
        fails += 1

sys.exit(1 if fails else 0)
