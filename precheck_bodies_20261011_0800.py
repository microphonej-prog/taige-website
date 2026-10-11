#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成前预检：正文六语属性完整性、引号畸形、裸 &、表格列数、内链、desc 长度、选题撞车。"""
import os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

from daily_meta_20261011_0800 import ARTICLES
LANGS = ("en", "ja", "ko", "fr", "es")


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.tags = []

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        if tag == "section" and d.get("class", "").startswith("article-body"):
            self.in_body = True
            return
        if self.in_body:
            self.tags.append((tag, d))

    def handle_endtag(self, tag):
        if self.in_body and tag == "section":
            self.in_body = False


fail = 0
print("== 1) 选题撞车检查 ==")
sm0 = open("sitemap.xml", encoding="utf-8").read()
for a in ARTICLES:
    for p in ["blog/%s" % a["slug"]] + ["%s/blog/%s" % (l, a["slug"]) for l in LANGS]:
        if os.path.exists(p):
            print("  !! 已存在: %s" % p); fail += 1
    if "/blog/%s</loc>" % a["slug"] in sm0:
        print("  !! sitemap 已含 %s" % a["slug"]); fail += 1
print("  OK（无重名文件、sitemap 无同 slug）")

print("== 2) 正文六语属性完整性 ==")
for a in ARTICLES:
    s = open(a["body"], encoding="utf-8").read()
    p = Collector(); p.feed(s)
    dzh = [(t, x) for t, x in p.tags if "data-zh" in x]
    missing = []
    for t, x in dzh:
        for need in ("data-en", "data-ja", "data-ko", "data-fr", "data-es"):
            if not x.get(need, "").strip():
                missing.append((t, need))
    print("  %s" % a["body"])
    print("    正文标签 %d 个，带 data-zh %d 个；缺五语的 %d 个 %s"
          % (len(p.tags), len(dzh), len(missing), missing[:8]))
    print("    缺 data-fr 或 data-es 的元素数: %d" % len([m for m in missing if m[1] in ("data-fr", "data-es")]))
    print("    引号畸形 data-xx=\"\" : %d ; 属性值后裸字符: %d ; 裸 &: %d"
          % (len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)),
             len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#|lt;|gt;)', s))))
    if missing:
        fail += 1
    if re.search(r'data-(?:zh|en|fr|es|ja|ko)=""', s):
        fail += 1
    # 中文字数（去掉标签）
    txt = re.sub(r'<[^>]+>', '', re.search(r'data-zh="(.*?)"\s+data-en=', s, re.S).group(1))
    print("    首段中文 %d 字" % len(re.findall(r'[\u4e00-\u9fff]', txt)))
    for ti, tb in enumerate(re.findall(r"<table.*?</table>", s, re.S), 1):
        rows = re.findall(r"<tr>(.*?)</tr>", tb, re.S)
        counts = [len(re.findall(r"<(?:th|td)\b", r)) for r in rows]
        ok = len(set(counts)) == 1
        print("    表 %d：%d 行，各行列数 %s %s" % (ti, len(rows), counts, "OK" if ok else "!! 列数不一致"))
        if not ok:
            fail += 1
    for href in sorted(set(re.findall(r'<a href="([^"#?]+)"', s))):
        if href.startswith(("http", "mailto", "tel")):
            continue
        if not os.path.exists(os.path.join("blog", href)):
            print("    !! 死链: %s" % href); fail += 1

print("== 3) desc 长度与 meta 字段 ==")
for a in ARTICLES:
    d = a["desc_zh"]
    print("  %-46s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
          % (a["slug"], len(re.findall(r"[\u4e00-\u9fff]", d)), len(a["desc_en"]),
             len(a["desc_ja"]), len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))
    for k in ("title_zh", "title_en", "title_ja", "title_ko", "title_fr", "title_es",
              "crumb_zh", "crumb_en", "crumb_ja", "crumb_ko", "crumb_fr", "crumb_es",
              "h1_zh", "h1_en", "h1_ja", "h1_ko", "h1_fr", "h1_es",
              "tag_zh", "tag_en", "tag_ja", "tag_ko", "tag_fr", "tag_es",
              "sum_zh", "sum_en", "sum_ja", "sum_ko", "sum_fr", "sum_es",
              "body", "slug"):
        if not a.get(k):
            print("    !! 缺字段 %s" % k); fail += 1
    if '"' in a["title_en"] or '"' in a["title_fr"] or '"' in a["title_es"]:
        print("    !! title 含裸双引号"); fail += 1
    for k, v in a.items():
        if isinstance(v, str) and re.search(r'&(?!amp;|nbsp;|quot;|#|lt;|gt;)', v):
            print("    !! %s 含裸 &" % k); fail += 1

print("\n预检结论: 问题数 = %d" % fail)
raise SystemExit(1 if fail else 0)
