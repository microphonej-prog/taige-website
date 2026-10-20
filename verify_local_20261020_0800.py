#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-20 08:00 批次本地验证：六语 title/desc/canonical/hreflang + 正文六语属性 + 繁体幂等"""
import re, sys, importlib.util
from html.parser import HTMLParser

sys.path.insert(0, ".")
from daily_meta_20261020_0800 import ARTICLES

LANGS = ["en", "ja", "ko", "fr", "es"]
fails = []

spec = importlib.util.spec_from_file_location("to_traditional", "to_traditional.py")
t2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t2)


class Attr(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.bad = []
        self.n = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "data-zh" in d:
            self.n += 1
            miss = [l for l in ["zh"] + LANGS if ("data-" + l) not in d]
            if miss:
                self.bad.append("<%s> 缺 %s" % (tag, ",".join(miss)))


for a in ARTICLES:
    print("\n== %s" % a["slug"])
    pages = [("zh", "blog/%s" % a["slug"], a["title_zh"], a["desc_zh"])]
    for l in LANGS:
        pages.append((l, "%s/blog/%s" % (l, a["slug"]), a["title_" + l], a["desc_" + l]))
    for lang, path, want_t, want_d in pages:
        s = open(path, encoding="utf-8").read()
        t = (re.search(r"<title[^>]*>(.*?)</title>", s, re.S) or [None, ""])[1].strip()
        d = (re.search(r'<meta name="description" content="([^"]*)"', s) or [None, ""])[1]
        can = (re.search(r'<link rel="canonical" href="([^"]*)"', s) or [None, ""])[1]
        hl = re.findall(r'<link rel="alternate" hreflang="([^"]+)"', s)
        html_lang = (re.search(r'<html lang="([^"]*)"', s) or [None, ""])[1]
        ok_t = (t == want_t)
        ok_d = (d == want_d)
        if lang == "zh":
            ok_d = ok_d or (d == t2.convert_html(want_d))
        ok_c = can.endswith(path.split("blog/")[-1]) and (path.split("blog/")[0] + "blog/") in can
        ok_h = len(hl) == 7 and "x-default" in hl
        p = Attr()
        p.feed(s)
        print("  %-3s title=%s desc=%s canonical=%s hreflang=%d 正文元素=%d 缺属性=%d html_lang=%s"
              % (lang, ok_t, ok_d, ok_c, len(hl), p.n, len(p.bad), html_lang))
        if not ok_t:
            print("      title 实际:", t[:90])
            fails.append((path, "title"))
        if not ok_d:
            print("      desc 实际:", d[:90])
            fails.append((path, "desc"))
        if not ok_c:
            print("      canonical 实际:", can)
            fails.append((path, "canonical"))
        if not ok_h:
            fails.append((path, "hreflang"))
        if p.bad:
            fails.append((path, "attr:%s" % p.bad[:2]))
    # 根目录页繁体幂等
    root = open("blog/%s" % a["slug"], encoding="utf-8").read()
    if t2.convert_html(root) != root:
        fails.append(("blog/%s" % a["slug"], "繁体未幂等（有简体残留）"))
        print("  !! 繁体幂等失败")
    else:
        print("  繁体幂等 OK")
    # 旧版脚本/资源引用
    print("  main.js:", "js/main.js?v=" in root, " assist.js:", "js/assist.js" in root,
          " cta:", 'class="cta-btn"' in root, " 相关文章:", root.count("相关文章") + root.count("相關文章"))

print("\n结论: 失败项 %d" % len(fails))
for f in fails:
    print("  !!", f)
sys.exit(1 if fails else 0)
