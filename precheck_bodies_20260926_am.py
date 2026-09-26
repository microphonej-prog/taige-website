#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-26 早间批次：正文文件预检 + 生成后校验（六语，含 ja/ko）。"""
import re, sys, json, os
from html.parser import HTMLParser

NEW = ["blog/trim-order-quantity-unit-conversion.html",
       "blog/trim-ironing-heat-resistance-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
BODIES = ["blog/_body_qty.html", "blog/_body_iron.html"]

print("== 0) 正文源文件预检 ==")
bad = 0
for f in BODIES:
    s = open(f, encoding="utf-8").read()
    bare_amp = [m.start() for m in re.finditer(r'&(?!amp;|nbsp;|quot;|#\d+;|lt;|gt;)', s)]
    empty_attr = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    attr_tail = re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)
    # 属性值内出现裸双引号（双引号包裹中又出现 "）会导致解析异常：统计引号数是否成对
    quotes_odd = s.count('"') % 2
    print("  %s: 长度 %d 字节；裸 & %d；空 data-* %d；属性后裸字符 %d；双引号奇偶 %d"
          % (f, len(s.encode('utf-8')), len(bare_amp), len(empty_attr), len(attr_tail), quotes_odd))
    if bare_amp:
        for i in bare_amp[:5]:
            print("    裸 & 上下文: ...%s..." % s[max(0, i-60):i+60].replace("\n", " "))
    bad += len(bare_amp) + len(empty_attr) + len(attr_tail) + quotes_odd

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

print("== 1) 中文页正文六语属性完整性 ==")
total_missing = 0
for f in NEW:
    if not os.path.exists(f):
        print("  %s 尚未生成，跳过" % f)
        continue
    s = open(f, encoding='utf-8').read()
    p = Collector(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in ("data-en", "data-ja", "data-ko", "data-fr", "data-es"):
            if not a.get(need, "").strip():
                missing.append((t, need))
    total_missing += len(missing)
    print("  %s" % f)
    print("    article-body 内标签 %d 个，带 data-zh 的 %d 个；缺 en/ja/ko/fr/es 的 %d 个 %s"
          % (len(p.tags), len(dzh), len(missing), missing[:6]))
    print("    引号畸形=%d  属性后裸字符=%d  裸 &=%d"
          % (len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)),
             len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s))))
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    print("    JSON-LD %d 处合法；静态 title=%s" % (len(lds), re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)[:56]))

print("== 2) 五语生成页检查（残留 / 汉字 / desc 长度） ==")
for f in NEW:
    slug = os.path.basename(f)
    for lang in LANGS:
        path = os.path.join(lang, "blog", slug)
        if not os.path.exists(path):
            print("  %-66s 缺失" % path); continue
        s = open(path, encoding='utf-8').read()
        m0 = re.search(r'<section class="article-body">', s)
        body = s[m0.end():]
        body = body[:re.search(r'</section>', body).start()]
        cjk = len(re.findall(r'[\u4e00-\u9fff]', re.sub(r'<script.*?</script>', '', body, flags=re.S)))
        q = Collector(); q.feed(s)
        residue = sum(1 for t, a in q.tags if any(k.startswith("data-") for k in a))
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        title = re.search(r'<title>(.*?)</title>', s, re.S).group(1)
        print("  %-56s data-*=%-2d 正文汉字=%-4d desc=%-4d title=%s"
              % (lang + "/blog/" + slug, residue, cjk, len(desc.group(1)) if desc else -1, title[:46]))

print("== 3) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
n = 0
for f in NEW:
    slug = os.path.basename(f)
    for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS]:
        u = "https://taigetag.com/%s%s" % (pre, slug)
        assert "<loc>%s</loc>" % u in sm, u
        n += 1
print("  新 URL %d 个全部存在；<loc> 总数=%d；blog/index lastmod 2026-09-26 命中 %d 处"
      % (n, sm.count("<loc>"), len(re.findall(r'<loc>https://taigetag\.com/(?:[a-z]{2}/)?blog/index\.html</loc>\r?\n\s*<lastmod>2026-09-26', sm))))

print("== 4) 列表页卡片 ==")
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(p, encoding='utf-8').read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    # 卡片顺序：新卡片应位于 post-grid 之后的第一/第二张
    grid = s.index('<div class="post-grid">')
    order = re.findall(r'<article class="post-card">.*?href="([^"]+\.html)"', s[grid:], re.S)[:3]
    print("  %-24s 命中=%s 前3张=%s" % (p, hit, order))

print("\n结论: 正文缺语种属性总数 = %d" % total_missing)
raise SystemExit(1 if total_missing else 0)
