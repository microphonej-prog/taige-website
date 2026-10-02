#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-02 晚批次（20:00）：正文文件预检 + 元数据 desc 长度体检"""
import re, sys, io, os
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

BODIES = ["blog/_body_elastic.html", "blog/_body_buttons.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = 0
        self.missing = []
        self.zh_elems = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "data-zh" not in d:
            return
        self.tags += 1
        self.zh_elems += 1
        miss = [l for l in LANGS if ("data-%s" % l) not in d]
        if miss:
            self.missing.append((tag, miss, d.get("data-zh", "")[:40]))


bad = 0
for path in BODIES:
    s = open(path, encoding="utf-8").read()
    c = Checker()
    c.feed(s)
    # 畸形属性扫描（引号嵌套）
    mal = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    # 裸双引号风险：属性值里出现 &quot; 之前不该有裸 "，用宽松检测：统计 " 是否为偶数
    quotes_even = s.count('"') % 2 == 0
    print("%-28s data-zh 元素=%d  缺语言=%d %s  畸形属性=%d  双引号偶数=%s  字节=%d"
          % (os.path.basename(path), c.zh_elems, len(c.missing), c.missing[:5],
             len(mal), quotes_even, len(s.encode("utf-8"))))
    if c.missing or mal or not quotes_even:
        bad += 1

print("预检结论：%s" % ("通过" if bad == 0 else "存在问题"))

# ---------- 元数据 desc 长度 ----------
sys.path.insert(0, ROOT)
import daily_meta_20261002_2000 as M

print("\n--- description 长度 ---")
for a in M.ARTICLES:
    print("%-40s zh=%d字 en=%d字符 ja=%d ko=%d fr=%d es=%d"
          % (a["slug"], len(a["desc_zh"]), len(a["desc_en"]), len(a["desc_ja"]),
             len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))
    if not (80 <= len(a["desc_zh"]) <= 130):
        print("   !! desc_zh 不在 80-130 区间")
    if not (120 <= len(a["desc_en"]) <= 165):
        print("   !! desc_en 不在 120-165 区间")
    # 属性值裸双引号检查
    for k, v in a.items():
        if isinstance(v, str) and '"' in v:
            print("   !! 字段 %s 含裸双引号" % k)

# ---------- 标题/文件名撞车 ----------
for a in M.ARTICLES:
    for p in ["blog/%s" % a["slug"]] + ["%s/blog/%s" % (l, a["slug"]) for l in ["en", "ja", "ko", "fr", "es"]]:
        if os.path.exists(p):
            print("!! 撞车：%s" % p)
    if "/blog/%s</loc>" % a["slug"] in open("sitemap.xml", encoding="utf-8").read():
        print("!! sitemap 已含 %s" % a["slug"])
print("撞车检查完成")
