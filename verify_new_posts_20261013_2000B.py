#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-13 第三批本地校验：六语属性完整性、canonical/hreflang、生成页残留、ja/ko 简体嫌疑、
列表卡片、sitemap、内部链接。用 tools venv 跑（需要 opencc）。"""
import re, json, os, sys
from html.parser import HTMLParser
from opencc import OpenCC

CC = OpenCC("s2t")
SLUGS = ["neckwear-trims-label-guide.html", "belts-suspenders-trims-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
ROOT_LANGS = ["zh"] + LANGS
TODAY = "2026-10-13"
fails = []


class BodyCollector(HTMLParser):
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


print("== 1) 根页（繁体）正文六语属性完整性 ==")
missing_total = 0
for slug in SLUGS:
    f = "blog/%s" % slug
    s = open(f, encoding="utf-8").read()
    p = BodyCollector(); p.feed(s); p.close()
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = [(t, need) for t, a in dzh for need in
               ("data-en", "data-ja", "data-ko", "data-fr", "data-es") if not a.get(need, "").strip()]
    missing_total += len(missing)
    print("  %s：正文标签 %d，带 data-zh %d，缺语种 %d %s" % (f, len(p.tags), len(dzh), len(missing), missing[:6]))
    # JSON-LD
    for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        json.loads(x)
    # canonical / hreflang
    can = re.search(r'<link rel="canonical" href="([^"]*)">', s).group(1)
    hre = dict(re.findall(r'<link rel="alternate" hreflang="([^"]*)" href="([^"]*)">', s))
    ok = (can == "https://taigetag.com/blog/%s" % slug and len(hre) == 7 and
          hre.get("x-default") == can and hre.get("en") == "https://taigetag.com/en/blog/%s" % slug)
    print("    canonical=%s hreflang=%d ok=%s" % (can, len(hre), ok))
    if not ok:
        fails.append("hreflang/canonical %s" % f)
    # ja 属性简体嫌疑
    sus = set()
    for m in re.finditer(r'data-ja="([^"]*)"', s):
        for c in m.group(1):
            if re.match(r"[\u4e00-\u9fff]", c) and CC.convert(c) != c:
                sus.add(c)
    print("    data-ja 简体嫌疑字: %s" % ("".join(sorted(sus)) or "无"))

print("== 2) 五语生成页 ==")
for slug in SLUGS:
    for lang in LANGS:
        f = "%s/blog/%s" % (lang, slug)
        s = open(f, encoding="utf-8").read()
        can = re.search(r'<link rel="canonical" href="([^"]*)">', s).group(1)
        exp = "https://taigetag.com/%s/blog/%s" % (lang, slug)
        title = re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1)
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r"</section>", s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        residue = len(re.findall(r"data-(?:zh|en|ja|ko|fr|es)=", body))
        cjk = len(re.findall(r"[\u4e00-\u9fff]", body))
        hangul = len(re.findall(r"[\uac00-\ud7a3]", body))
        kana = len(re.findall(r"[\u3040-\u30ff]", body))
        latin = len(re.findall(r"[A-Za-z]", body))
        note = ""
        if lang in ("en", "fr", "es") and cjk:
            note = " !! 中文残留"
            fails.append("中文残留 %s" % f)
        if lang == "ja" and kana < 100:
            note = " !! 日文假名过少"
            fails.append("ja 假名过少 %s" % f)
        if lang == "ko" and hangul < 200:
            note = " !! 韩文过少"
            fails.append("ko 谚文过少 %s" % f)
        if residue:
            note += " !! data-* 残留"
            fails.append("data-* 残留 %s" % f)
        if can != exp:
            note += " !! canonical"
            fails.append("canonical %s" % f)
        print("  %-52s title=%s | 汉字%d 假名%d 谚文%d 拉丁%d%s"
              % (f, title[:26], cjk, kana, hangul, latin, note))

print("== 3) 列表页卡片（六语）==")
for lang in ROOT_LANGS:
    f = "blog/index.html" if lang == "zh" else "%s/blog/index.html" % lang
    s = open(f, encoding="utf-8").read()
    hit = [x for x in SLUGS if x in s]
    grid = s.index('<div class="post-grid">')
    first_two = s[grid:grid + 4000]
    order_ok = all(x in first_two for x in SLUGS)
    print("  %-24s 命中=%d 置顶=%s" % (f, len(hit), order_ok))
    if len(hit) != 2 or not order_ok:
        fails.append("列表卡片 %s" % f)

print("== 4) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
new_urls = []
for slug in SLUGS:
    for lang in ROOT_LANGS:
        u = "https://taigetag.com/%sblog/%s" % (lang + "/" if lang != "zh" else "", slug)
        m = re.search(r"<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
        if not m:
            fails.append("sitemap 缺 %s" % u)
        elif m.group(1) != TODAY:
            fails.append("sitemap lastmod %s = %s" % (u, m.group(1)))
        new_urls.append(u)
for lang in ROOT_LANGS:
    u = "https://taigetag.com/%sblog/index.html" % (lang + "/" if lang != "zh" else "")
    m = re.search(r"<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
    if not m or m.group(1) != TODAY:
        fails.append("blog index lastmod %s" % u)
print("  新 URL %d 个全部含今日 lastmod；<loc> 总数 %d" % (len(new_urls), sm.count("<loc>")))

print("== 5) 内部链接可解析 ==")
for slug in SLUGS:
    f = "blog/%s" % slug
    s = open(f, encoding="utf-8").read()
    hrefs = re.findall(r'<a [^>]*href="([^"]+)"', s)
    bad = []
    for h in hrefs:
        if h.startswith(("http", "mailto:", "#", "tel:")):
            continue
        tgt = os.path.normpath(os.path.join("blog", h.split("#")[0]))
        if not os.path.exists(tgt):
            bad.append(h)
    print("  %s：链接 %d 个，断链 %d %s" % (f, len(hrefs), len(bad), bad))
    if bad:
        fails.append("断链 %s %s" % (f, bad))

print("\n结论: 问题 %d 项 %s" % (len(fails), fails))
sys.exit(1 if fails else 0)
