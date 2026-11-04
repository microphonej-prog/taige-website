# -*- coding: utf-8 -*-
"""本地校验：文件存在、标题/描述、正文属性完整性、卡片、sitemap、JSON-LD。"""
import json, os, re, sys
from html.parser import HTMLParser

LANGS = ["en", "ja", "ko", "fr", "es"]
SLUGS = ["apparel-trims-nearshoring-sourcing-guide.html",
         "apparel-unboxing-packaging-design-guide.html"]
DATE = "2026-11-04"
LANGATTR = {"zh": "zh", "en": "en", "ja": "ja", "ko": "ko", "fr": "fr", "es": "es"}


class Chk(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.bad = []
        self.n = 0
        self.in_body = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "section" and d.get("class") == "article-body":
            self.in_body = 1
        if self.in_body and any(k.startswith("data-") for k in d):
            self.n += 1
            miss = [l for l in ("zh", "en", "ja", "ko", "fr", "es") if "data-" + l not in d]
            if miss:
                self.bad.append((tag, ", ".join(miss), (d.get("data-zh", "") or "")[:30]))


ok = True
for slug in SLUGS:
    print("=" * 70)
    for lang in ["zh"] + LANGS:
        p = "blog/" + slug if lang == "zh" else "%s/blog/%s" % (lang, slug)
        if not os.path.exists(p):
            print("  !! 缺失 %s" % p); ok = False; continue
        s = open(p, encoding="utf-8").read()
        t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1)
        d = re.search(r'<meta name="description"[^>]*?content="([^"]*)"', s, re.S)
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S).group(1)
        c = Chk(); c.feed(s)
        canon = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        print("  [%-2s] title=%d desc=%d h1=%d | 正文data元素=%d 缺语言=%d | canon=%s"
              % (lang, len(t), len(d.group(1)) if d else -1, len(h1), c.n, len(c.bad), canon))
        if c.bad:
            ok = False
            for b in c.bad[:5]:
                print("       ", b)
        # 语言纯净度：非中文页不应含汉字 (ja 允许汉字)
        if lang in ("en", "fr", "es"):
            cjk = re.findall(r"[\u4e00-\u9fff]", t + (d.group(1) if d else "") + h1)
            if cjk:
                print("       !! 标题/描述含汉字:", "".join(cjk[:10])); ok = False
        if lang == "zh":
            # 简体残留抽查（繁体页不应大量出现简体专用字）
            simp = re.findall(r"[这们说时发经过去对体]", s)
            print("       简体残留字抽样: %d %s" % (len(simp), "".join(sorted(set(simp)))))
        # JSON-LD
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            try:
                json.loads(m.group(1))
            except Exception as e:
                print("       !! JSON-LD 非法:", e); ok = False

# 卡片
idx = open("blog/index.html", encoding="utf-8").read()
for slug in SLUGS:
    n = idx.count('href="%s"' % slug)
    pos = idx.find('href="%s"' % slug)
    grid = idx.find('<div class="post-grid">')
    print("卡片 %-48s 次数=%d 位置靠前=%s" % (slug, n, pos > grid and pos - grid < 6000))
    if n < 1:
        ok = False

# sitemap
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    urls = ["https://taigetag.com/blog/%s" % slug] + \
           ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]
    for u in urls:
        blk = re.search(r"<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
        if not blk or blk.group(1) != DATE:
            print("  !! sitemap 问题:", u, blk.group(1) if blk else "缺"); ok = False
print("sitemap 新 URL 全部就位: %s (共 %d 个 <loc>)" % (ok, sm.count("<loc>")))
print("BUST_VERSION:", re.search(r'BUST_VERSION = "(\d+)"', open("js/main.js", encoding="utf-8").read()).group(1))
print("结果:", "PASS" if ok else "FAIL")
