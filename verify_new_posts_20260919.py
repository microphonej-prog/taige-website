#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 2026-09-19 新增两篇：六语属性完整性、引号畸形、JSON-LD、生成页残留、sitemap、canonical/hreflang。"""
import json
import os
import re
from html.parser import HTMLParser

NEW = ["apparel-trims-spec-sheet-guide.html", "suiting-formalwear-trims-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
ATTRS = ["data-en", "data-fr", "data-es", "data-ja", "data-ko"]


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


fails = []
print("== 1) 中文主文件正文六语属性完整性 ==")
for slug in NEW:
    f = "blog/" + slug
    s = open(f, encoding="utf-8").read()
    p = Collector()
    p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in ATTRS:
            if not a.get(need, "").strip():
                missing.append((t, need))
    STRUCT = {"ul", "ol", "table", "tr", "div", "strong", "em", "br", "thead", "tbody"}
    # 真正要报警的：带属性却没有 data-*（说明属性写残了）；裸结构标签与「相关文章」的 <li><a data-*> 属正常
    zh_only = [t for t, a in p.tags if a and not any(k.startswith("data-") for k in a) and t not in STRUCT]
    bare = [t for t, a in p.tags if not a]
    print("  %s: 标签 %d，带 data-zh %d，缺其他语种 %d %s" %
          (f, len(p.tags), len(dzh), len(missing), missing[:6]))
    print("     无任何 data-* 的标签（应为空或纯结构标签）: %s" % zh_only)
    print("     裸标签（结构/相关文章 li 等）: %s" % sorted(set(bare)))
    bad_q = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s))
    bad_j = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[a-zA-Z]', s))
    bare_amp = len(re.findall(r"&(?!amp;|nbsp;|quot;|lt;|gt;|#\d+;)", s))
    print("     引号畸形 data-xx=\"\": %d ；属性后裸字符: %d ；裸 & : %d" % (bad_q, bad_j, bare_amp))
    if missing or bad_q or bad_j or bare_amp or zh_only:
        fails.append(f)
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    print("     JSON-LD %d 处合法；title 六语属性 %d 个" %
          (len(lds), len(re.findall(r"<title [^>]*>", s))))

print("== 2) 各语言静态页 ==")
for lang in LANGS:
    for slug in NEW:
        f = "%s/blog/%s" % (lang, slug)
        assert os.path.exists(f), "缺文件 %s" % f
        s = open(f, encoding="utf-8").read()
        m = re.search(r"<title>([^<]*)</title>", s)
        assert m, "%s 无 title" % f
        title = m.group(1)
        assert '<html lang="%s"' % lang in s, "%s html lang 错" % f
        assert "data-zh=" not in s and "data-en=" not in s, "%s 残留 data-* 属性" % f
        lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
        for x in lds:
            json.loads(x)
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S).group(1)
        kana = len(re.findall(r"[\u3040-\u30ff]", s))
        hangul = len(re.findall(r"[\uac00-\ud7af]", s))
        print("  %-28s title=%-64s h1=%s（kana=%d hangul=%d）" %
              (f, title[:62], h1[:34], kana, hangul))
        if lang == "ja" and kana < 50:
            fails.append(f + " 日语假名过少")
        if lang == "ko" and hangul < 200:
            fails.append(f + " 韩文过少")

print("== 3) 列表页卡片 ==")
for f in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(f, encoding="utf-8").read()
    grid = s[s.index('<div class="post-grid">'):]
    hits = [slug for slug in NEW if slug in grid]
    first_two = re.findall(r'<a class="more" href="([^"]+)"', grid)[:2]
    print("  %s: 新卡片 %d/2，前两张顺序=%s" % (f, len(hits), first_two))
    if len(hits) != 2 or first_two != NEW:
        fails.append(f + " 卡片缺失或未置顶")

print("== 4) sitemap ==")
s = open("sitemap.xml", encoding="utf-8").read()
for slug in NEW:
    for pre in ["blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"]:
        loc = "https://taigetag.com/%s%s" % (pre, slug)
        assert "<loc>%s</loc>" % loc in s, "sitemap 缺 %s" % loc
    print("  %s：6 条 URL 齐全" % slug)
print("  sitemap 总 URL 数: %d（应 828+12=840）" % s.count("<loc>"))

print("== 5) canonical / hreflang ==")
for slug in NEW:
    s = open("blog/" + slug, encoding="utf-8").read()
    can = re.search(r'<link rel="canonical" href="([^"]+)"', s).group(1)
    hre = re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', s)
    print("  %s canonical=%s hreflang=%s" % (slug, can, [h[0] for h in hre]))
    if len(hre) != 7 or [h[0] for h in hre] != ["zh-Hant", "en", "fr", "es", "ja", "ko", "x-default"]:
        fails.append(slug + " hreflang 数量或顺序错")

print()
print("结果: %s" % ("全部通过" if not fails else "存在问题 -> %s" % fails))
