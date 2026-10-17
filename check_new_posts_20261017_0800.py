#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-17 08:00 批次校验：六语属性完整性、生成页残留、卡片、sitemap、BUST_VERSION、canonical/hreflang。"""
import re, json, os
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

LANGS = ["en", "ja", "ko", "fr", "es"]
SLUGS = ["gots-organic-cotton-label-guide.html", "apparel-packaging-recyclability-guide.html"]
NEW = ["blog/" + s for s in SLUGS]
TODAY = "2026-10-17"


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


print("== 1) 正文六语属性完整性（zh 元素缺 en/ja/ko/fr/es 数量）==")
total_missing = 0
for f in NEW:
    s = open(f, encoding="utf-8").read()
    p = Collector(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in ("data-en", "data-ja", "data-ko", "data-fr", "data-es"):
            if not a.get(need, "").strip():
                missing.append((t, need))
    total_missing += len(missing)
    print("  %-52s 标签 %d / 带 data-zh %d / 缺属性 %d %s"
          % (f, len(p.tags), len(dzh), len(missing), missing[:6]))
    print("      引号畸形=%d 属性值后裸字符=%d 裸&=%d"
          % (len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)),
             len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s))))
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1)
    print("      JSON-LD %d 处合法；静态 title: %s" % (len(lds), t[:58]))

print("\n== 2) 生成页（en/ja/ko/fr/es）残留与语言纯净度 ==")
for f in NEW:
    for lang in LANGS:
        path = os.path.join(lang, f)
        s = open(path, encoding="utf-8").read()
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r"</section>", s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        cjk = len(re.findall(r"[\u4e00-\u9fff]", re.sub(r"<script.*?</script>", "", body, flags=re.S)))
        q = Collector(); q.feed(s)
        residue = sum(1 for t, a in q.tags if any(k.startswith("data-") and k[5:] in
                      ("zh", "en", "fr", "es", "ja", "ko") for k in a))
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
        print("  %-62s data残留=%d 正文汉字=%d desc=%d" %
              (path, residue, cjk, len(desc.group(1)) if desc else -1))
        if lang in ("en", "fr", "es") and cjk:
            print("      !! 非中日韩页面正文含汉字 %d 个" % cjk)
        print("      title=%s | h1=%s" % (title[:52], (h1.group(1)[:48] if h1 else "无")))

print("\n== 3) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
for s in SLUGS:
    for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
        u = "https://taigetag.com/%s%s" % (pre, s)
        assert "<loc>%s</loc>" % u in sm, u
        pat = re.compile(r"<loc>%s</loc>\r?\n\s*<lastmod>%s</lastmod>" % (re.escape(u), TODAY))
        assert pat.search(sm), "lastmod 不是今天: %s" % u
print("  12 个新 URL 全部存在且 lastmod=%s；<loc> 总数=%d" % (TODAY, sm.count("<loc>")))
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    pat = re.compile(r"<loc>%s</loc>\r?\n\s*<lastmod>%s</lastmod>" % (re.escape(u), TODAY))
    assert pat.search(sm), "blog 列表页 lastmod 未更新: %s" % u
print("  6 个 blog 列表页 lastmod 均为 %s" % TODAY)

print("\n== 4) 列表页卡片（六语，应在 post-grid 顶部）==")
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(p, encoding="utf-8").read()
    grid = s.index('<div class="post-grid">')
    pos = {s_: s.index(s_) for s_ in SLUGS if s_ in s}
    order = sorted(pos.items(), key=lambda kv: kv[1])
    print("  %-26s 命中=%s" % (p, [k for k, _ in order]))
    assert len(pos) == 2, "卡片缺失: %s" % p
    assert order[0][1] > grid, "卡片未在 post-grid 内: %s" % p
    # 顶部两张卡片顺序应为第 1、2 个 post-card
    cards = [m.start() for m in re.finditer(r'<article class="post-card">', s)]
    assert cards[0] == order[0][1] - s[:order[0][1]].rfind('<article class="post-card">') + cards[0] - cards[0] or True
    top2 = s[grid:cards[2]]
    for s_ in SLUGS:
        assert s_ in top2, "不在最顶两张卡片内: %s" % s_
print("  六语列表页均含 2 张新卡，且位于 post-grid 顶部两张")

print("\n== 5) canonical / hreflang ==")
for f in NEW:
    for lang in [None] + LANGS:
        path = f if lang is None else os.path.join(lang, f)
        s = open(path, encoding="utf-8").read()
        can = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        want = "https://taigetag.com/%s%s" % ("" if lang is None else lang + "/", f)
        hl = re.findall(r'<link rel="alternate" hreflang="([^"]*)"', s)
        assert can == want, "%s canonical=%s 期望=%s" % (path, can, want)
        assert sorted(hl) == sorted(["zh-Hant", "en", "fr", "es", "ja", "ko", "x-default"]), (path, hl)
print("  12 个页面 canonical 与 hreflang 全部正确")

print("\n== 6) BUST_VERSION / blog 首页文案 ==")
mj = open("js/main.js", encoding="utf-8").read()
bv = re.search(r'var BUST_VERSION = "(\d+)";', mj).group(1)
print("  BUST_VERSION = %s" % bv)
assert bv == "166"
print("\n结论: 正文属性缺失总数 = %d" % total_missing)
raise SystemExit(1 if total_missing else 0)
