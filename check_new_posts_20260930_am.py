#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-30 上午批次校验：四/六语覆盖、属性引号、canonical/hreflang、卡片、sitemap"""
import os, re, sys
from html.parser import HTMLParser
sys.path.insert(0, ".")
from daily_meta_20260930_am import ARTICLES

LANGS = ["en", "ja", "ko", "fr", "es"]
ATTRS = ["data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es"]
fails = []


def head(cond, msg):
    if not cond:
        fails.append(msg)
        print("  [!] " + msg)
    return cond


for a in ARTICLES:
    slug = a["slug"]
    print("== %s" % slug)
    files = ["blog/%s" % slug] + ["%s/blog/%s" % (l, slug) for l in LANGS]
    for p in files:
        head(os.path.exists(p), "缺失文件 %s" % p)
    # 1) 属性覆盖：article-body 内每个带 data-zh 的元素都必须有全部 5 个译语属性
    s = open(files[0], encoding="utf-8").read()
    body = s[s.index('class="article-body"'):s.index("</section>", s.index('class="article-body"'))]

    class Collector(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.total = 0
            self.miss = {k: 0 for k in ATTRS[1:]}
            self.bad = []

        def handle_starttag(self, tag, attrs):
            d = dict(attrs)
            if "data-zh" not in d:
                return
            self.total += 1
            for k in ATTRS[1:]:
                if k not in d or not (d[k] or "").strip():
                    self.miss[k] += 1
                    self.bad.append((tag, k, (d.get("data-zh") or "")[:28]))

    c = Collector()
    c.feed(body)
    total, miss = c.total, c.miss
    print("  article-body 带 data-zh 元素: %d，缺译语: %s" % (total, miss))
    for t, k, z in c.bad[:6]:
        print("      <%-6s> 缺 %s : %s" % (t, k, z))
    head(total > 0, "正文无 data-zh 元素")
    for k, v in miss.items():
        head(v == 0, "%s 缺 %s" % (slug, k))
    # 2) 空属性 / 引号破损（data-xx="" 或 data-xx= 后紧跟 >
    bad = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    head(not bad, "%s 存在空/破损 data 属性 %d 处" % (slug, len(bad)))
    # 3) 每个 > 片段内引号必须成对（裸双引号检测）
    odd = 0
    for m in re.finditer(r'<[^<>]*>', s):
        if m.group(0).count('"') % 2:
            odd += 1
    head(odd == 0, "%s 有 %d 个标签引号数量为奇数（疑似裸双引号）" % (slug, odd))
    # 4) 六语文档的 title / h1 / description
    for p in files:
        t = open(p, encoding="utf-8").read()
        tt = re.search(r'<title[^>]*>(.*?)</title>', t, re.S).group(1)
        head(tt.strip() != "", "%s 线上 title 为空" % p)
        head(t.count('rel="canonical"') == 1, "%s canonical 数量异常" % p)
        head(t.count('hreflang=') == 7, "%s hreflang 数量 %d（应为 7）" % (p, t.count('hreflang=')))
        head('missing' not in tt.lower() and 'undefined' not in tt.lower(), "%s title 异常 %s" % (p, tt))
    # 5) canonical 与 sitemap 规则一致
    for p in files:
        t = open(p, encoding="utf-8").read()
        can = re.search(r'<link rel="canonical" href="([^"]+)"', t).group(1)
        if p == files[0]:
            exp = "https://taigetag.com/blog/%s" % slug
        else:
            exp = "https://taigetag.com/%s/blog/%s" % (p.split("/")[0], slug)
        head(can == exp, "canonical 不符 %s -> %s (期望 %s)" % (p, can, exp))

# 6) blog/index.html 卡片
idx = open("blog/index.html", encoding="utf-8").read()
for a in ARTICLES:
    head(a["slug"] in idx, "首页卡片缺失 %s" % a["slug"])
print("blog/index.html 卡片命中: %d/2" % sum(1 for a in ARTICLES if a["slug"] in idx))

# 7) sitemap
sm = open("sitemap.xml", encoding="utf-8").read()
for a in ARTICLES:
    for p in [a["slug"]] + ["%s/blog/%s" % (l, a["slug"]) for l in LANGS]:
        u = "https://taigetag.com/%s" % ("blog/%s" % p if not p.startswith(("en/", "ja/", "ko/", "fr/", "es/")) else p)
        head("<loc>%s</loc>" % u in sm, "sitemap 缺 %s" % u)
print("sitemap <loc> 总数:", sm.count("<loc>"))

print("\n结果:", "全部通过" if not fails else "失败 %d 项" % len(fails))
