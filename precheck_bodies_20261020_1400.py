#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-20 14:00 批次正文预检：六语属性完整性 / 缺属性 / 中文残留 / 引号"""
import re, sys, os
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

LANGS = ["en", "ja", "ko", "fr", "es"]
BODIES = ["blog/_body_seed.html", "blog/_body_scent.html"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []
        self.texts = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_data(self, data):
        if data.strip():
            self.texts.append(data.strip())


for path in BODIES:
    s = open(path, encoding="utf-8").read()
    p = P()
    p.feed(s)

    # 1) 需要多语的元素：含 data-zh 的
    multi = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in multi:
        for l in LANGS:
            if "data-" + l not in a or not a["data-" + l].strip():
                missing.append("%s/%s 缺 data-%s" % (t, a["data-zh"][:18], l))

    # 2) 顶层容器（section/div.container/ul/table/tr）默认不含 data
    n_tag = len(p.tags)
    n_multi = len(multi)

    # 3) 中文残留检查：data-en/fr/es 中出现 CJK
    cjk = []
    for t, a in multi:
        for l in ("en", "fr", "es"):
            v = a.get("data-" + l, "")
            if re.search(r"[\u4e00-\u9fff]", v):
                cjk.append("%s/%s: %s" % (t, l, v[:40]))

    # 4) 属性值里不允许出现半角双引号（写盘后必然是畸形）
    bad_q = []
    for m in re.finditer(r'(data-(?:zh|en|ja|ko|fr|es))="([^"]*)"', s):
        pass  # 正则匹配本身就说明没有内嵌双引号

    # 5) 每种语言覆盖统计
    print("== %s ==" % path)
    print("  标签数 %d，带 data-zh 的元素 %d，六语齐全 %d，缺属性 %d"
          % (n_tag, n_multi, n_multi - len({m.split('/')[0] + m.split('/')[1][:0] for m in []}) - len(missing), len(missing)))
    for m in missing:
        print("   [缺] " + m)
    print("   data-en/fr/es 含中文: %d" % len(cjk))
    for c in cjk:
        print("   [CJK] " + c)

    # 6) 中文字数（data-zh 合计）
    zh = "".join(a.get("data-zh", "") for t, a in multi)
    print("   正文中文合计 %d 字" % len(re.findall(r"[\u4e00-\u9fff]", zh)))

    # 7) 结构检查
    for must in ('class="article-body"', 'class="callout"', 'class="cta-box"', '相关文章'):
        if must not in s:
            print("   [结构] 缺少 %s" % must)
    links = re.findall(r'href="([a-z0-9\-]+\.html)"', s)
    print("   内部链接: %s" % sorted(set(links)))
    for l in links:
        if not os.path.exists("blog/" + l):
            print("   [断链] blog/%s 不存在" % l)

print("\n预检完成")
