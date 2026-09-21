#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 2026-09-21 下午新增的 2 篇六语文章：正文字段完整性、引号畸形、JSON-LD、
生成页残留、hreflang/canonical、sitemap、列表页卡片、BUST_VERSION。"""
import re, json, os, sys
from html.parser import HTMLParser

NEW = ["blog/hang-tag-metal-hardware-guide.html", "blog/garment-trims-needle-detection-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
fails = []

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

print("== 1) 正文六语属性完整性（根文件） ==")
total_missing = 0
for f in NEW:
    s = open(f, encoding="utf-8").read()
    p = Collector(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = [(t, need) for t, a in dzh for need in ("data-en", "data-ja", "data-ko", "data-fr", "data-es")
               if not a.get(need, "").strip()]
    total_missing += len(missing)
    print("  %s" % f)
    print("    正文标签 %d，带 data-zh %d，缺 en/ja/ko/fr/es %d %s" % (len(p.tags), len(dzh), len(missing), missing[:6]))
    q1 = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s))
    q2 = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[a-zA-Z]', s))
    am = len(re.findall(r'&(?!amp;|nbsp;|quot;|#|<)', s))
    print("    引号畸形=%d 属性值后裸字符=%d 裸&=%d" % (q1, q2, am))
    if q1 or q2 or am:
        fails.append("畸形字符 %s" % f)
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
    sim = len(re.findall(r'[\u4e00-\u9fff]', t)) and t != re.sub(r'[\u4e00-\u9fff]', '', t)
    print("    JSON-LD %d 处合法；静态 title = %s" % (len(lds), t[:70]))
    if len(lds) != 1:
        fails.append("JSON-LD 数量异常 %s" % f)
    # 繁体检查：data-zh 里不应再出现常见简体字
    simp = re.findall(r'[简买卖页标签纸钱设备级发明术类别针国际货币场内设计这为]', s[:200])
    print("    <html lang>=%s" % re.search(r'<html lang="([^"]+)"', s).group(1))

print("== 2) 生成页（en/ja/ko/fr/es）残留与标题 ==")
for f in NEW:
    slug = os.path.basename(f)
    for lang in LANGS:
        path = os.path.join(lang, f)
        s = open(path, encoding="utf-8").read()
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r'</section>', s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        body_ns = re.sub(r'<script.*?</script>', '', body, flags=re.S)
        cjk = len(re.findall(r'[\u4e00-\u9fff]', body_ns)) if lang in ("en", "fr", "es") else 0
        q = Collector(); q.feed(s)
        residue = sum(1 for t, a in q.tags if any(k.startswith("data-") and k[5:] in
                      ("zh", "en", "fr", "es", "ja", "ko") for k in a))
        title = re.search(r'<title>(.*?)</title>', s, re.S).group(1)
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        can = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        hl = len(re.findall(r'<link rel="alternate" hreflang="', s))
        ok = (residue == 0) and (cjk == 0) and can.endswith("/%s/blog/%s" % (lang, slug)) and hl == 7
        print("  %-44s residue=%d 正文汉字=%d desc=%d字 hreflang=%d canonical=%s %s"
              % (lang + "/blog/" + slug, residue, cjk, len(desc.group(1)) if desc else -1, hl,
                 can.replace("https://taigetag.com", ""), "OK" if ok else "!! 异常"))
        print("        title: %s" % title[:95])
        if not ok:
            fails.append("生成页异常 %s" % path)

print("== 3) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
for f in NEW:
    slug = os.path.basename(f)
    for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS]:
        u = "https://taigetag.com/%s%s" % (pre, slug)
        if "<loc>%s</loc>" % u not in sm:
            fails.append("sitemap 缺 %s" % u)
    z = re.search(r'<loc>https://taigetag.com/blog/%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(slug), sm)
    print("  %-44s lastmod=%s" % (slug, z.group(1) if z else "缺失"))
print("  <loc> 总数=%d" % sm.count("<loc>"))

print("== 4) 列表页卡片 ==")
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(p, encoding="utf-8").read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    print("  %-26s 命中=%s" % (p, hit))
    if len(hit) != 2:
        fails.append("卡片缺失 %s" % p)

print("== 5) BUST_VERSION ==")
mj = open("js/main.js", encoding="utf-8").read()
nb = re.search(r'var BUST_VERSION = "(\d+)"', mj).group(1)
print("  BUST_VERSION=%s" % nb)
if nb != "97":
    fails.append("BUST_VERSION 未升级")

print("\n缺失总数=%d 失败项=%d %s" % (total_missing, len(fails), fails))
sys.exit(1 if (total_missing or fails) else 0)
