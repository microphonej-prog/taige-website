#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-29 下午批次校验：属性完整性、卡片、sitemap、canonical/hreflang、版本号、内部链接。"""
import re, os, sys, html

os.chdir(os.path.dirname(os.path.abspath(__file__)))
SLUGS = ["trim-supply-continuity-guide.html", "trim-supplier-communication-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
LANGS6 = ["zh", "en", "ja", "ko", "fr", "es"]
DATE = "2026-09-29"
BUST = "121"
fails = []


def fail(msg):
    fails.append(msg)
    print("FAIL  " + msg)


def protect(s):
    buf, i, in_q = [], 0, False
    while i < len(s):
        c = s[i]
        if c == '"':
            in_q = not in_q
            buf.append(c)
        elif c == '>' and in_q:
            buf.append('__GTH__')
        elif c == '<' and in_q:
            buf.append('__GLT__')
        else:
            buf.append(c)
        i += 1
    return ''.join(buf)


def check_body_attrs(path):
    s = open(path, encoding="utf-8").read()
    m = re.search(r'<section class="article-body">.*?</section>', s, re.S)
    if not m:
        return fail("%s 无 article-body" % path)
    body = protect(m.group(0))
    tags = re.findall(r'<([a-zA-Z0-9]+)\b([^>]*?)>', body)
    n_el = 0
    for tag, attrs in tags:
        if 'data-zh=' not in attrs and 'data-en=' not in attrs:
            continue
        n_el += 1
        for l in LANGS6:
            if not re.search(r'data-%s="' % l, attrs):
                fail("%s <%s> 缺 data-%s" % (path, tag, l))
    bad = re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', body)
    if bad:
        fail("%s 畸形空属性 %d 处" % (path, len(bad)))
    bare = re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[A-Za-z]', body)
    if bare:
        fail("%s 属性值后裸字符 %d 处" % (path, len(bare)))
    return n_el


print("=== 1) 六语元素属性完整性 ===")
for slug in SLUGS:
    for f in ["blog/" + slug] + [l + "/blog/" + slug for l in LANGS]:
        n = check_body_attrs(f)
        print("  %-50s 带 data-* 元素 %s" % (f, n))

print("=== 2) 各语言 title 渲染（静态生成结果） ===")
want = {
    "trim-supply-continuity-guide.html": {
        "zh": "供應中斷", "en": "Trims Supply Continuity",
        "ja": "供給継続", "ko": "공급 연속성",
        "fr": "Continuité d'approvisionnement", "es": "Continuidad de suministro"},
    "trim-supplier-communication-guide.html": {
        "zh": "溝通", "en": "Trims Supplier Communication",
        "ja": "副資材サプライヤーとのやり取り", "ko": "부자재 공급사 커뮤니케이션",
        "fr": "Communication fournisseur", "es": "Comunicación con proveedores"},
}
for slug in SLUGS:
    for l in LANGS6:
        p = ("blog/" + slug) if l == "zh" else ("%s/blog/%s" % (l, slug))
        s = open(p, encoding="utf-8").read()
        t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
        t_plain = html.unescape(t)
        ok = want[slug][l] in t_plain
        if not ok:
            fail("%s title 不含关键词 %r → %s" % (p, want[slug][l], t[:80]))
        print("  %-50s %s | %s" % (p, "OK " if ok else "BAD", t[:70]))
        if l != "zh":
            extra = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="', s))
            if extra:
                print("     注意：残留 data-* %d 处（应仅在语言按钮 data-lang）" % extra)

print("=== 3) canonical / hreflang ===")
for slug in SLUGS:
    for l in LANGS6:
        p = ("blog/" + slug) if l == "zh" else ("%s/blog/%s" % (l, slug))
        s = open(p, encoding="utf-8").read()
        c = re.search(r'<link rel="canonical" href="([^"]*)"', s)
        expect = "https://taigetag.com/blog/%s" % slug if l == "zh" else \
                 "https://taigetag.com/%s/blog/%s" % (l, slug)
        if not c or c.group(1) != expect:
            fail("%s canonical=%s 期望 %s" % (p, c and c.group(1), expect))
        hl = re.findall(r'hreflang="([^"]*)" href="([^"]*)"', s)
        if len(hl) != 7:
            fail("%s hreflang 条数 %d != 7" % (p, len(hl)))
print("  六语 canonical/hreflang 检查完成")

print("=== 4) blog/index.html 卡片 ===")
idx = open("blog/index.html", encoding="utf-8").read()
grid = idx[idx.index('<div class="post-grid">'):]
for slug in SLUGS:
    pos = grid.find('href="%s"' % slug)
    if pos == -1:
        fail("blog/index.html 缺卡片 %s" % slug)
    else:
        print("  卡片 %-40s 相对位置 %d" % (slug, pos))
for l in LANGS:
    p = "%s/blog/index.html" % l
    s = open(p, encoding="utf-8").read()
    for slug in SLUGS:
        if slug not in s:
            fail("%s 缺卡片 %s" % (p, slug))
print("  六语 blog 列表页卡片检查完成")

print("=== 5) sitemap ===")
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % slug] + \
             ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        if "<loc>%s</loc>" % u not in sm:
            fail("sitemap 缺 %s" % u)
print("  <loc> 总数 %d" % sm.count("<loc>"))
for u in ["https://taigetag.com/blog/index.html"] + \
         ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    m = re.search(r'<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    if not m or m.group(1) != DATE:
        fail("blog index lastmod 未更新 %s → %s" % (u, m and m.group(1)))
print("  blog 列表页 lastmod 已更新为 %s" % DATE)

print("=== 6) 版本号 ===")
mj = open("js/main.js", encoding="utf-8").read()
v = re.search(r'var BUST_VERSION = "([^"]*)"', mj).group(1)
print("  BUST_VERSION = %s" % v)
if v != BUST:
    fail("BUST_VERSION 不是 %s" % BUST)

print("=== 7) 内部链接存在性 ===")
for slug in SLUGS:
    for l in LANGS6:
        p = ("blog/" + slug) if l == "zh" else ("%s/blog/%s" % (l, slug))
        base = os.path.dirname(p)
        s = open(p, encoding="utf-8").read()
        body = re.search(r'<section class="article-body">.*?</section>', s, re.S).group(0)
        for href in re.findall(r'href="([^"#]+)"', body):
            if href.startswith(("http", "mailto", "tel")):
                continue
            tgt = os.path.normpath(os.path.join(base, href))
            if not os.path.exists(tgt):
                fail("%s 链接不存在：%s" % (p, href))
print("  正文内部链接检查完成")

print("=== 8) JSON-LD 合法性 + 中文页静态 desc ===")
import json
for slug in SLUGS:
    for l in LANGS6:
        p = ("blog/" + slug) if l == "zh" else ("%s/blog/%s" % (l, slug))
        s = open(p, encoding="utf-8").read()
        lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
        for x in lds:
            try:
                json.loads(x)
            except Exception as e:
                fail("%s JSON-LD 非法：%s" % (p, e))
        d = re.search(r'<meta name="description"[^>]*>', s, re.S)
        dm = d and re.search(r'content="([^"]*)"', d.group(0))
        h1 = re.search(r'<h1[^>]*>([^<]*)</h1>', s)
        if not dm:
            fail("%s 静态 description 缺失" % p)
        print("  %-50s JSON-LD=%d desc=%d字 h1=%s" % (p, len(lds), len(dm.group(1)) if dm else -1,
                                                     (h1.group(1)[:26] if h1 else "-")))

print()
if fails:
    print("共 %d 项失败：" % len(fails))
    for f in fails:
        print(" - " + f)
    sys.exit(1)
print("全部检查通过 ✅")
