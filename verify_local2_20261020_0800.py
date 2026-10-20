#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-20 08:00 批次本地验证 v2：六语 title/desc/canonical/hreflang + 根页正文六语属性 + 繁体幂等"""
import re, sys, html, importlib.util
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


def meta_content(s):
    m = re.search(r'<meta name="description"(.*?)>', s, re.S)
    if not m:
        return ""
    c = re.search(r'\scontent="([^"]*)"', m.group(1))
    return html.unescape(c.group(1)) if c else ""


for a in ARTICLES:
    print("\n== %s" % a["slug"])
    pages = [("zh", "blog/%s" % a["slug"], a["title_zh"], a["desc_zh"])]
    for l in LANGS:
        pages.append((l, "%s/blog/%s" % (l, a["slug"]), a["title_" + l], a["desc_" + l]))
    for lang, path, want_t, want_d in pages:
        s = open(path, encoding="utf-8").read()
        t = html.unescape((re.search(r"<title[^>]*>(.*?)</title>", s, re.S) or [None, ""])[1].strip())
        d = meta_content(s)
        can = (re.search(r'<link rel="canonical" href="([^"]*)"', s) or [None, ""])[1]
        hl = re.findall(r'<link rel="alternate" hreflang="([^"]+)"', s)
        html_lang = (re.search(r'<html lang="([^"]*)"', s) or [None, ""])[1]
        if lang == "zh":
            wt, wd = t2.convert_html(want_t), t2.convert_html(want_d)
        else:
            wt, wd = want_t, want_d
        ok_t, ok_d = (t == wt), (d == wd)
        ok_c = can == "https://taigetag.com/" + path
        ok_h = len(hl) == 7 and "x-default" in hl
        p = Attr()
        p.feed(s)
        print("  %-3s title=%s desc=%s(len=%d) canonical=%s hreflang=%d 六语元素=%d 缺属性=%d html_lang=%s"
              % (lang, ok_t, ok_d, len(d), ok_c, len(hl), p.n, len(p.bad), html_lang))
        for ok, name in ((ok_t, "title"), (ok_d, "desc"), (ok_c, "canonical"), (ok_h, "hreflang")):
            if not ok:
                print("      !", name, "实际:", (t if name == "title" else d if name == "desc" else can)[:110])
                fails.append((path, name))
        if p.bad:
            fails.append((path, "attr:%s" % p.bad[:2]))
    root = open("blog/%s" % a["slug"], encoding="utf-8").read()
    if t2.convert_html(root) != root:
        fails.append(("blog/%s" % a["slug"], "繁体未幂等"))
        print("  !! 繁体幂等失败")
    else:
        print("  繁体幂等 OK；main.js/assist.js/cta 齐备:",
              "js/main.js?v=" in root, "js/assist.js" in root, 'class="cta-btn"' in root)

print("\n结论: 失败项 %d" % len(fails))
for f in fails:
    print("  !!", f)
sys.exit(1 if fails else 0)
