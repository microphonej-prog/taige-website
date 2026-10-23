# -*- coding: utf-8 -*-
"""本次批次本地校验：文件/卡片/sitemap/hreflang/canonical/四语属性覆盖。"""
import re, os
from html.parser import HTMLParser

LANGS = ["en", "ja", "ko", "fr", "es"]
SLUGS = ["fsc-certified-hang-tags.html", "apparel-trims-rush-order-guide.html"]
WANT = ["data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es"]

sm = open("sitemap.xml", encoding="utf-8").read()
ok = True


class Body(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.rows = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if any(k in d for k in WANT):
            self.rows.append((tag, [w for w in WANT if w not in d or not d[w]]))


def check(path, lang):
    global ok
    s = open(path, encoding="utf-8").read()
    # 只取 article-body 段落
    i0 = s.index('<section class="article-body">')
    i1 = s.index("\n</main>")
    p = Body(); p.feed(s[i0:i1])
    bad = [r for r in p.rows if r[1]]
    # 标题静态内容
    m = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
    title_txt = m.group(1)
    m2 = re.search(r'<title[^>]*data-%s="([^"]*)"' % lang, s)
    if m2:
        want_title = m2.group(1)
        title_ok = title_txt.strip() == want_title.strip()
        title_state = "OK" if title_ok else "MISMATCH"
    else:
        title_ok = bool(title_txt.strip())
        title_state = "STATIC"
    # canonical
    canon = re.search(r'<link rel="canonical" href="([^"]+)"', s).group(1)
    alt = dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', s))
    print("  %-42s 正文元素 %3d 缺属性 %d | title %s | canonical %s"
          % (path, len(p.rows), len(bad), title_state, canon))
    if bad:
        print("     MISSING:", bad[:5]); ok = False
    if not title_ok:
        print("     title 实际:", title_txt[:80], "| 期望:", want_title[:80]); ok = False
    # canonical 与 sitemap 一致
    if "<loc>%s</loc>" % canon not in sm:
        print("     canonical 不在 sitemap:", canon); ok = False
    for k, v in alt.items():
        if k != "x-default" and "<loc>%s</loc>" % v not in sm:
            print("     hreflang %s 不在 sitemap: %s" % (k, v)); ok = False
    return len(p.rows), len(bad)


total = 0
for slug in SLUGS:
    for lang in ["zh"] + LANGS:
        path = "blog/%s" % slug if lang == "zh" else "%s/blog/%s" % (lang, slug)
        if not os.path.exists(path):
            print("  文件缺失:", path); ok = False; continue
        n, b = check(path, lang)
        total += b
print("六语正文缺失属性合计:", total)

# 卡片
for lang in ["zh"] + LANGS:
    p = "blog/index.html" if lang == "zh" else "%s/blog/index.html" % lang
    s = open(p, encoding="utf-8").read()
    hits = [slug for slug in SLUGS if 'href="%s"' % slug in s]
    first = s.index('<div class="post-grid">')
    pos = [s.index('href="%s"' % slug, first) for slug in SLUGS]
    print("  %-24s 卡片 %d/2  首个卡片位置 %s" % (p, len(hits), sorted(pos) == pos))
    if len(hits) != 2:
        ok = False

# sitemap 12 个新 URL
for slug in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % slug] + ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        if "<loc>%s</loc>" % u not in sm:
            print("  sitemap 缺:", u); ok = False
print("sitemap 新 URL 校验完成；blog 首页 lastmod:", re.findall(r"<loc>https://taigetag.com/blog/index.html</loc>\r?\n\s*<lastmod>([^<]+)", sm))
print("总判定:", "PASS" if ok and total == 0 else "FAIL")
