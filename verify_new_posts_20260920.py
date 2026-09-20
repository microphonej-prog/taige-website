#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-20 新增文章校验：六语属性完整性、引号畸形、JSON-LD、生成页残留、canonical/sitemap 一致性、卡片。"""
import re, json, os, sys
from html.parser import HTMLParser

NEW = ["blog/hang-tag-double-sided-printing.html", "blog/trim-quotation-comparison-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
NEED = ("data-en", "data-fr", "data-es", "data-ja", "data-ko")
fail = 0


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


print("== 1) 正文六语属性完整性 ==")
for f in NEW:
    s = open(f, encoding="utf-8").read()
    p = Collector(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = [(t, n) for t, a in dzh for n in NEED if not a.get(n, "").strip()]
    cjk_body = len(re.findall(r"[\u4e00-\u9fff]", s[s.index('class="article-body"'):s.index("</main>")]))
    print("  %-52s 标签 %d / 带 data-zh %d / 缺语种 %d %s" % (f, len(p.tags), len(dzh), len(missing), missing[:6]))
    print("     引号畸形=%d 属性值后裸字符=%d 裸&=%d JSON-LD=%d"
          % (len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)),
             len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r"&(?!(?:amp|nbsp|quot|#|lt|gt);)", s)),
             len(re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S))))
    for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        json.loads(x)
    fail += len(missing)
    if len(missing):
        fail += 1

print("== 2) 生成页（en/ja/ko/fr/es）残留检查 ==")
for f in NEW:
    slug = os.path.basename(f)
    for lang in LANGS:
        path = os.path.join(lang, f)
        s = open(path, encoding="utf-8").read()
        m0 = re.search(r'<section class="article-body">', s)
        body = s[m0.end():s.index("</section>", m0.end())]
        body_clean = re.sub(r"<script.*?</script>", "", body, flags=re.S)
        cjk = len(re.findall(r"[\u4e00-\u9fff]", body_clean))
        residue = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=', body))
        kana = len(re.findall(r"[\u3040-\u30ff]", body_clean))
        hangul = len(re.findall(r"[\uac00-\ud7af]", body_clean))
        t = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        print("  %-56s data残留=%d 汉字=%d kana=%d hangul=%d desc=%d" %
              (path, residue, cjk, kana, hangul, len(desc.group(1)) if desc else -1))
        print("      title: %s" % t[:78])
        if residue or not desc:
            fail += 1
        if lang in ("en", "fr", "es") and cjk:
            print("      !! %s 页正文残留汉字 %d" % (lang, cjk)); fail += 1
        if lang == "ja" and kana < 50:
            print("      !! ja 页假名过少（疑未翻译）"); fail += 1
        if lang == "ko" and hangul < 50:
            print("      !! ko 页谚文过少（疑未翻译）"); fail += 1

print("== 3) canonical 与 sitemap 一致性 ==")
sm = open("sitemap.xml", encoding="utf-8").read()
locs = set(re.findall(r"<loc>([^<]+)</loc>", sm))
for f in NEW:
    slug = os.path.basename(f)
    for pre in ["blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"]:
        u = "https://taigetag.com/%s%s" % (pre, slug)
        ok = ("<loc>%s</loc>" % u) in sm
        print("  %-64s sitemap=%s" % (u, ok))
        if not ok:
            fail += 1
for f in NEW:
    slug = os.path.basename(f)
    pages = [("blog", "blog/%s" % slug)] + [(l, "%s/blog/%s" % (l, slug)) for l in LANGS]
    for lang, p in pages:
        s = open(p, encoding="utf-8").read()
        can = re.search(r'<link rel="canonical" href="([^"]+)"', s).group(1)
        exp = "https://taigetag.com/blog/%s" % slug if lang == "blog" else "https://taigetag.com/%s/blog/%s" % (lang, slug)
        flag = "OK" if can == exp else "!!不一致"
        if can != exp:
            fail += 1
        print("  canonical %-46s %s %s" % (p, can.replace("https://taigetag.com", ""), flag))

print("== 4) blog 列表页卡片（六语）==")
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(p, encoding="utf-8").read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    print("  %-26s 卡片命中=%d %s" % (p, len(hit), hit))
    if len(hit) != 2:
        fail += 1
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(p, encoding="utf-8").read()
    if 'data-zh' in s.split('<div class="post-grid">')[1][:1200] and '"ja"' in s:
        pass
print("== 5) blog 首页 sitemap lastmod ==")
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    m = re.search(r"<loc>%s</loc>\r?\n\s*<lastmod>([^<]+)</lastmod>" % re.escape(u), sm)
    print("  %-52s lastmod=%s" % (u, m.group(1) if m else "缺失"))
    if not m or m.group(1) != "2026-09-20":
        fail += 1
print("== 6) BUST_VERSION ==")
mj = open("js/main.js", encoding="utf-8").read()
print("  ", re.search(r'var BUST_VERSION = "(\d+)"', mj).group(0))
print("\n结论: fail = %d" % fail)
sys.exit(1 if fail else 0)
