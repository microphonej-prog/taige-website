#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-23 下午批次校验：六语文件齐备 / canonical+hreflang / JSON-LD / 六语覆盖 /
   列表页卡片 / sitemap URL / 语言页无中文残留（en/fr/es）"""
import os, re, json, sys

SLUGS = ["pet-apparel-trims-guide.html", "loungewear-pajama-trims-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
TODAY = "2026-09-23"
problems = []


def cjk(s):
    return re.findall(r'[\u4e00-\u9fff]', s)


def split_tags(s):
    out, i, n = [], 0, len(s)
    while i < n:
        if s[i] == '<':
            j, in_q = i + 1, False
            while j < n:
                c = s[j]
                if c == '"':
                    in_q = not in_q
                elif c == '>' and not in_q:
                    break
                j += 1
            out.append(s[i:j + 1])
            i = j + 1
        else:
            i += 1
    return out


for slug in SLUGS:
    print("=== %s ===" % slug)
    root = "blog/%s" % slug
    files = [root] + ["%s/blog/%s" % (l, slug) for l in LANGS]
    for p in files:
        if not os.path.exists(p):
            problems.append("缺文件 %s" % p)
    s = open(root, encoding="utf-8").read()

    # 1) 根页 canonical + 8 条 hreflang
    m = re.search(r'<link rel="canonical" href="([^"]+)">', s)
    assert m, "canonical 缺失"
    if m.group(1) != "https://taigetag.com/blog/%s" % slug:
        problems.append("canonical 错: %s" % m.group(1))
    hrefl = re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)">', s)
    if len(hrefl) != 7:
        problems.append("hreflang 数量 %d（应为 7）" % len(hrefl))
    print("  canonical=%s hreflang=%d" % (m.group(1), len(hrefl)))

    # 2) 根页正文六语覆盖
    miss_fr = miss_es = miss_ja = miss_ko = n_data = 0
    body = s[s.index('<section class="article-body">'):s.index('</main>')]
    for t in split_tags(body):
        if re.match(r'<(p|h2|h3|li|td|th|div|a|span)\b', t) and 'data-zh=' in t:
            n_data += 1
            miss_fr += ' data-fr=' not in t
            miss_es += ' data-es=' not in t
            miss_ja += ' data-ja=' not in t
            miss_ko += ' data-ko=' not in t
    print("  正文元素 %d，缺 fr=%d es=%d ja=%d ko=%d" % (n_data, miss_fr, miss_es, miss_ja, miss_ko))
    if miss_fr or miss_es or miss_ja or miss_ko:
        problems.append("%s 正文六语缺失 fr=%d es=%d ja=%d ko=%d" % (slug, miss_fr, miss_es, miss_ja, miss_ko))

    # 3) JSON-LD 合法性 + 六语 inLanguage
    for p in files:
        t = open(p, encoding="utf-8").read()
        ld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S)
        if len(ld) != 1:
            problems.append("%s JSON-LD 数量 %d" % (p, len(ld)))
            continue
        try:
            data = json.loads(ld[0])
        except Exception as e:
            problems.append("%s JSON-LD 解析失败: %s" % (p, e))
            continue
        arts = [g for g in data["@graph"] if g.get("@type") == "Article"]
        if not arts or slug not in arts[0]["url"]:
            problems.append("%s Article URL 不符" % p)
        if len(arts[0].get("inLanguage", [])) != 6:
            problems.append("%s inLanguage 不是 6 语" % p)
    print("  JSON-LD 校验通过")

    # 4) 语言页：无 data-* 残留、标题语言正确
    for l in LANGS:
        p = "%s/blog/%s" % (l, slug)
        t = open(p, encoding="utf-8").read()
        if "data-zh=" in t or "data-ja=" in t or "data-ko=" in t:
            problems.append("%s 残留 data-* 属性" % p)
        title = re.search(r'<title>([^<]*)</title>', t).group(1)
        if l in ("en", "fr", "es") and cjk(title):
            problems.append("%s 标题含中文: %s" % (p, title))
        desc = re.search(r'<meta name="description"[^>]*content="([^"]*)"', t, re.S).group(1)
        if len(desc) < 60:
            problems.append("%s desc 过短 (%d)" % (p, len(desc)))
        print("  [%s] %s" % (l, title[:72]))

    # 5) sitemap
    sm = open("sitemap.xml", encoding="utf-8").read()
    for u in ["https://taigetag.com/blog/%s" % slug] + \
             ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        if "<loc>%s</loc>" % u not in sm:
            problems.append("sitemap 缺 %s" % u)
    print("  sitemap 12 URL 齐备")

# 6) 列表页卡片
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    t = open(p, encoding="utf-8").read()
    grid = t.split('<div class="post-grid">')[1]
    head = grid[:9000]
    for slug in SLUGS:
        if slug not in head:
            problems.append("%s 顶部卡片内未见 %s" % (p, slug))
    order = re.findall(r'<a class="more" href="([^"]+)"', grid)
    if order[:2] != SLUGS:
        problems.append("%s 新卡片未排在最前两位: %s" % (p, order[:2]))
    print("  %-28s 卡片 ok（前 2 张 = %s）" % (p, order[:2]))

# 7) blog/index lastmod
sm = open("sitemap.xml", encoding="utf-8").read()
for u in ["https://taigetag.com/blog/index.html"] + \
         ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    pat = re.compile(r'<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(u))
    d = pat.search(sm).group(1)
    if d != TODAY:
        problems.append("blog index lastmod %s = %s" % (u, d))
print("blog index lastmod = %s ✓" % TODAY)

print("\n问题数 = %d" % len(problems))
for x in problems:
    print("  !! %s" % x)
sys.exit(1 if problems else 0)
