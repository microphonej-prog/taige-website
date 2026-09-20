#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 2026-09-20 20:00 批次新增的 2 篇文章（六语）。"""
import re, json, os
from html.parser import HTMLParser

NEW = ["blog/hang-tag-edge-painting-guide.html", "blog/clothing-label-compliance-south-korea.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]

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

print("== 1) 文件存在 + 正文六语属性完整性 ==")
total_missing = 0
for f in NEW:
    assert os.path.exists(f), f
    s = open(f, encoding="utf-8").read()
    p = Collector(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in ("data-en", "data-fr", "data-es", "data-ja", "data-ko"):
            if not a.get(need, "").strip():
                missing.append((t, need))
    total_missing += len(missing)
    cjk_zh = len(re.findall(r"[\u4e00-\u9fff]", re.sub(r"<[^>]+>", "", re.sub(r"<script.*?</script>", "", s, flags=re.S))))
    print("  %s (%d KB)" % (f, len(s.encode()) // 1024))
    print("    body 标签 %d，带 data-zh %d，缺 en/fr/es/ja/ko 的 %d %s"
          % (len(p.tags), len(dzh), len(missing), missing[:8]))
    print("    引号畸形 %d ; 属性值后裸字符 %d ; 裸 & %d ; 全页汉字 %d"
          % (len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)),
             len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s)), cjk_zh))
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    print("    JSON-LD %d 处合法 ; 静态 title=%s" % (len(lds), re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)[:70]))

print("== 2) 五语生成页检查 ==")
for f in NEW:
    for lang in LANGS:
        path = os.path.join(lang, f)
        assert os.path.exists(path), path
        s = open(path, encoding="utf-8").read()
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r'</section>', s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        cjk = len(re.findall(r"[\u4e00-\u9fff]", re.sub(r"<script.*?</script>", "", body, flags=re.S)))
        q = Collector(); q.feed(s)
        residue = sum(1 for t, a in q.tags if any(k.startswith("data-") and k[5:] in ("zh", "en", "fr", "es", "ja", "ko") for k in a))
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        title = re.search(r'<title>(.*?)</title>', s, re.S)
        print("  %-60s data残留=%d 正文汉字=%d desc=%d title=%s"
              % (path, residue, cjk, len(desc.group(1)) if desc else -1, title.group(1)[:48] if title else "无"))

print("== 3) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
for f in NEW:
    slug = os.path.basename(f)
    for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS]:
        u = "https://taigetag.com/%s%s" % (pre, slug)
        assert "<loc>%s</loc>" % u in sm, u
    assert "2026-09-20" in sm
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    m = re.search(r'<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    assert m and m.group(1) == "2026-09-20", (u, m.group(1) if m else None)
print("  12 个新 URL 全部存在；blog 首页 lastmod 六语 = 2026-09-20；<loc> 总数=%d" % sm.count("<loc>"))

print("== 4) 列表页卡片（六语） ==")
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(p, encoding="utf-8").read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    print("  %-28s 命中=%s" % (p, hit))
    assert len(hit) == 2, p

print("== 5) BUST_VERSION ==")
mj = open("js/main.js", encoding="utf-8").read()
print("  ", re.search(r'var BUST_VERSION = "[^"]*";', mj).group(0))

print("\n结论: 正文缺失属性总数 = %d" % total_missing)
raise SystemExit(1 if total_missing else 0)
