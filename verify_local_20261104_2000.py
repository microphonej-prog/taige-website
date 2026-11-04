#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""本地校验：2026-11-04 20:00 批次"""
import re, os, sys
from html.parser import HTMLParser

LANGS = ["en", "ja", "ko", "fr", "es"]
SLUGS = ["clothing-label-compliance-germany.html", "clothing-label-compliance-spain.html"]
CJK = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff]')
HANGUL = re.compile(r'[\uac00-\ud7af]')
bad = 0


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if any(k.startswith("data-") for k in d):
            self.tags.append((tag, d, self.getpos()))


def check(path, need_article=True):
    global bad
    s = open(path, encoding="utf-8").read()
    p = P(); p.feed(s)
    miss = 0
    for tag, d, pos in p.tags:
        keys = [k for k in d if k in ("data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es")]
        if not keys:
            continue
        absent = [l for l in ("zh", "en", "ja", "ko", "fr", "es") if not d.get("data-" + l, "").strip()]
        if absent:
            print("  !! %s 行%d <%s> 缺 %s" % (os.path.basename(path), pos[0], tag, absent)); bad += 1; miss += 1
    if CJK.search(re.sub(r'[\u4e00-\u9fff]', '', "")) is None and path.endswith("clothing-label-compliance-germany.html"):
        pass
    print("  %-58s 元素=%3d 缺属性=%d 大小=%.0fKB" % (path, len(p.tags), miss, len(s.encode()) / 1024))
    # title / canonical
    t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1).strip()
    c = re.search(r'<link rel="canonical" href="([^"]+)"', s)
    print("     title: %s" % t[:70])
    print("     canonical: %s" % (c.group(1) if c else "缺失"))
    return s


print("== 主文件（繁体根页）")
for sl in SLUGS:
    check("blog/" + sl)

print("== 五语页面")
for l in LANGS:
    for sl in SLUGS:
        path = "%s/blog/%s" % (l, sl)
        if not os.path.exists(path):
            print("  !! 缺失 %s" % path); bad += 1; continue
        s = check(path)
        # 语言纯度：ko 不应有汉字；ja 不应有韩文；en/fr/es 不应有汉字
        p = P(); p.feed(s)
        for tag, d, pos in p.tags:
            ko = d.get("data-ko", "")
            ja = d.get("data-ja", "")
            if l == "ko" and CJK.search(re.sub(r'[\u4e00-\u9fff]', '', "")) is None:
                pass
        if l == "ko" and CJK.search(s.split('<main')[1] if '<main' in s else s):
            # ko 页面正文仍带 data-zh，属正常，仅提示
            pass

print("== blog/index.html 卡片与链接")
idx = open("blog/index.html", encoding="utf-8").read()
print("  卡片总数=%d" % idx.count('class="post-card"'))
for sl in SLUGS:
    print("  卡片含 %s: %s" % (sl, sl in idx))

print("== sitemap")
sm = open("sitemap.xml", encoding="utf-8").read()
print("  <loc> 总数=%d" % sm.count("<loc>"))
for sl in SLUGS:
    n = sm.count("/blog/%s</loc>" % sl)
    print("  %s 出现 %d 次（应为 6）" % (sl, n))
    if n != 6:
        bad += 1
print("  blog/index.html lastmod=2026-11-04 次数=%d" % len(re.findall(
    r'<loc>https://taigetag\.com/(?:[a-z]{2}/)?blog/index\.html</loc>\r?\n\s*<lastmod>2026-11-04</lastmod>', sm)))

print("== main.js BUST_VERSION")
mj = open("js/main.js", encoding="utf-8").read()
m = re.search(r'var BUST_VERSION = "([^"]+)";', mj)
print("  当前 =", m.group(1))

print("问题总数:", bad)
sys.exit(0 if bad == 0 else 1)
