#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-29 上午批次校验：属性完整性、卡片、sitemap、canonical/hreflang、版本号。"""
import re, os, sys, glob

os.chdir(os.path.dirname(os.path.abspath(__file__)))
SLUGS = ["trim-digital-sampling-3d.html", "trim-coding-standardization.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
LANGS6 = ["zh", "en", "ja", "ko", "fr", "es"]
DATE = "2026-09-29"
fails = []


def fail(msg):
    fails.append(msg)
    print("FAIL  " + msg)


def protect(s):
    """把引号内的 < 和 > 换成占位符（属性值里有 <strong> 等标签时正则会被截断）"""
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
    # 每个带 data-* 的元素，六语必须齐全
    tags = re.findall(r'<([a-zA-Z0-9]+)\b([^>]*?)>', body)
    n_el = 0
    for tag, attrs in tags:
        if 'data-zh=' not in attrs and 'data-en=' not in attrs:
            continue
        n_el += 1
        for l in LANGS6:
            if not re.search(r'data-%s="' % l, attrs):
                fail("%s <%s> 缺 data-%s" % (path, tag, l))
    # 畸形属性（相邻空引号 = 嵌套引号崩坏）
    bad = re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', body)
    if bad:
        fail("%s 畸形空属性 %d 处" % (path, len(bad)))
    return n_el


print("=== 1) 六语元素属性完整性 ===")
for slug in SLUGS:
    for f in ["blog/" + slug] + [l + "/blog/" + slug for l in LANGS]:
        n = check_body_attrs(f)
        print("  %-46s 带 data-* 元素 %s" % (f, n))

print("=== 2) 各语言 title 渲染（静态生成结果） ===")
want = {
    "trim-digital-sampling-3d.html": {
        "zh": "數字化打樣", "en": "Digital Sampling for Trims",
        "ja": "デジタルサンプリング", "ko": "디지털 샘플링",
        "fr": "Échantillonnage numérique", "es": "Muestreo digital"},
    "trim-coding-standardization.html": {
        "zh": "編碼與版庫", "en": "Trims Coding and Tooling Library",
        "ja": "コード化と版ライブラリ", "ko": "코딩과 판 라이브러리",
        "fr": "Codification et bibliothèque", "es": "Codificación y biblioteca"},
}
for slug in SLUGS:
    for l in LANGS6:
        p = ("blog/" + slug) if l == "zh" else ("%s/blog/%s" % (l, slug))
        s = open(p, encoding="utf-8").read()
        t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
        ok = want[slug][l] in t
        if not ok:
            fail("%s title 不含关键词 %r → %s" % (p, want[slug][l], t[:80]))
        # 残留 data-*
        resid = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=', t + s[:s.index('<title')]))
        print("  %-46s %s | %s" % (p, "OK " if ok else "BAD", t[:70]))
        if l != "zh" and re.search(r'data-(?:zh|en|fr|es|ja|ko)="', s):
            extra = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="', s))
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
        # 中文版不应有 data-zh 残留之外的重复 hreflang
print("  六语 canonical/hreflang 检查完成")

print("=== 4) blog/index.html 卡片 ===")
idx = open("blog/index.html", encoding="utf-8").read()
grid = idx[idx.index('<div class="post-grid">'):]
for slug in SLUGS:
    pos_card = grid.find('href="%s"' % slug)
    pos_other = grid.find('href="%s"' % SLUGS[1 - SLUGS.index(slug)])
    if pos_card == -1:
        fail("blog/index.html 缺卡片 %s" % slug)
    else:
        print("  卡片 %-34s 位置 %d（相对）" % (slug, pos_card))
m2 = re.search(r'<div class="post-grid">\s*(<article class="post-card">.*?</article>)', grid, re.S)
first = m2.group(1) if m2 else ""
for slug in SLUGS:
    if slug not in first and slug not in grid[:2000]:
        print("  提示：%s 不在网格最前两张，检查插入位置" % slug)
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
if v != "120":
    fail("BUST_VERSION 不是 120")

print("=== 7) 内部链接存在性 ===")
for slug in SLUGS:
    for l in ["zh"] + LANGS:
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

print()
if fails:
    print("共 %d 项失败：" % len(fails))
    for f in fails:
        print(" - " + f)
    sys.exit(1)
print("全部检查通过 ✅")
