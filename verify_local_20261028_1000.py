#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-28 10:00 批次本地校验：六语属性完整性、引号畸形、JSON-LD、lang 纯度、sitemap、卡片、canonical/hreflang"""
import re, json, os, sys
from html.parser import HTMLParser

os.chdir(os.path.dirname(os.path.abspath(__file__)))
NEW = ["blog/trim-supplier-switchover-guide.html",
       "blog/ai-generated-artwork-trim-printing-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
FAIL = 0


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


print("== 1) 根页正文六语属性完整性 ==")
total_missing = 0
for f in NEW:
    s = open(f, encoding="utf-8").read()
    p = Collector(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in ("data-en", "data-ja", "data-ko", "data-fr", "data-es"):
            if not a.get(need, "").strip():
                missing.append((t, need, a.get("data-zh", "")[:20]))
    total_missing += len(missing)
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1)
    desc = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s, re.S).group(1)
    print("  %s" % f)
    print("    正文标签 %d，带 data-zh %d，缺语 %d %s"
          % (len(p.tags), len(dzh), len(missing), missing[:6]))
    bad_attr = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s))
    raw_amp = len(re.findall(r'&(?!amp;|nbsp;|quot;|#|lt;|gt;)', s))
    print("    引号畸形 %d ; 裸 & %d ; JSON-LD %d 处合法" % (bad_attr, raw_amp, len(lds)))
    if bad_attr:
        FAIL += 1
    print("    静态 title: %s" % t[:80])
    print("    静态 desc [%d 字]: %s" % (len(desc), desc[:70]))

print("== 2) 语言页残留与标题 ==")
for lang in LANGS:
    for f in NEW:
        path = os.path.join(lang, f)
        s = open(path, encoding="utf-8").read()
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r"</section>", s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        body_clean = re.sub(r"<script.*?</script>", "", body, flags=re.S)
        cjk = len(re.findall(r"[\u4e00-\u9fff]", body_clean))
        residue = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="', s))
        title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
        flag = ""
        if lang in ("en", "fr", "es", "ko") and cjk:
            flag = "  <<< 汉字残留异常"
            FAIL += 1
        if residue:
            flag += "  <<< data-* 残留"
            FAIL += 1
        print("  %-58s 汉字=%4d data残留=%d%s | %s" % (path, cjk, residue, flag, title[:56]))

print("== 3) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
n = 0
for f in NEW:
    slug = os.path.basename(f)
    for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS]:
        u = "https://taigetag.com/%s%s" % (pre, slug)
        assert "<loc>%s</loc>" % u in sm, u
        n += 1
print("  新增 URL 全部存在: %d 个；<loc> 总数=%d" % (n, sm.count("<loc>")))
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    m = re.search(r'<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    assert m and m.group(1) == "2026-10-28", (u, m.group(1) if m else None)
print("  blog 列表页 lastmod 已更新为 2026-10-28（6 处）")

print("== 4) canonical / hreflang 与 sitemap 一致性 ==")
for lang in LANGS:
    for f in NEW:
        path = os.path.join(lang, f)
        s = open(path, encoding="utf-8").read()
        canon = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        expect = "https://taigetag.com/%s/%s" % (lang, f.replace("\\", "/"))
        assert canon == expect, (canon, expect)
        assert "<loc>%s</loc>" % canon in sm, canon
        hl = dict(re.findall(r'<link rel="alternate" hreflang="([^"]*)" href="([^"]*)"', s))
        assert set(hl) == {"zh-Hant", "en", "ja", "ko", "fr", "es", "x-default"}, hl
        for k, v in hl.items():
            assert "<loc>%s</loc>" % v in sm, (k, v)
print("  10 个语言页 canonical 与 sitemap 一致，hreflang 7 条齐全且均在 sitemap 内")

print("== 5) 列表页卡片（六语） ==")
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(p, encoding="utf-8").read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    grid = s.index('<div class="post-grid">')
    # 卡片起点 = 该卡片 href 往前最近的 <article class="post-card">
    starts = []
    for f in NEW:
        idx = s.index(os.path.basename(f), grid)
        starts.append(idx - s.rindex('<article class="post-card">', grid, idx))
    # 前两张卡片 = 网格内最早的 article 位置
    arts = [m.start() for m in re.finditer(r'<article class="post-card">', s[grid:])]
    first_two_len = len(arts) >= 2 and arts[1] < 3500
    print("  %-26s 新卡片命中=%d %s (第一张距 grid 起点 %d 字符)" % (p, len(hit), hit, arts[0] if arts else -1))
    if len(hit) != 2 or not first_two_len:
        FAIL += 1
        print("     <<< 卡片缺失或位置异常")

print("== 6) 正文长度与关键词 ==")
for f in NEW:
    s = open(f, encoding="utf-8").read()
    p = Collector(); p.feed(s)
    zh = " ".join(a.get("data-zh", "") for t, a in p.tags)
    zh_text = re.sub(r"<[^>]+>", "", zh)
    print("  %-58s 中文正文 %d 字" % (f, len(re.findall(r"[\u4e00-\u9fff]", zh_text))))

print("== 7) BUST_VERSION ==")
mj = open("js/main.js", encoding="utf-8").read()
print("  ", re.search(r'var BUST_VERSION = "[^"]*";', mj).group(0))
print("\n结论: 缺语总数 = %d, 其他异常 = %d" % (total_missing, FAIL))
sys.exit(1 if (total_missing or FAIL) else 0)
