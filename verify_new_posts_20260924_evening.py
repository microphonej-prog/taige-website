#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-24 晚间批次本地验证：文件/卡片/sitemap/六语属性/链接/繁体/版本号"""
import os, re, sys, json, html
from html.parser import HTMLParser

SLUGS = ["chinese-new-year-trims-order-planning.html", "clothing-label-compliance-uae.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
ALL = [""] + LANGS  # "" = 根目录
DATE = "2026-09-24"
fails = []


def ck(name, cond, detail=""):
    print("%s %s%s" % ("[OK]  " if cond else "[FAIL]", name, ("  " + detail) if detail else ""))
    if not cond:
        fails.append(name)


# ---------- ① 文件存在 ----------
for slug in SLUGS:
    paths = ["blog/" + slug] + ["%s/blog/%s" % (l, slug) for l in LANGS]
    miss = [p for p in paths if not os.path.exists(p)]
    ck("① 文件存在 %s（6 语言）" % slug, not miss, str(miss))

# ---------- ② blog/index.html 卡片 ----------
idx = open("blog/index.html", encoding="utf-8").read()
grid = idx[idx.index('<div class="post-grid">'):]
first_two = re.findall(r'<article class="post-card">(.*?)</article>', grid, re.S)[:2]
hrefs_top = [re.search(r'href="([^"]+)"', b).group(1) for b in first_two]
ck("② 顶部两张卡就是新文章", sorted(hrefs_top) == sorted(SLUGS), str(hrefs_top))
for l in LANGS:
    p = "%s/blog/index.html" % l
    s = open(p, encoding="utf-8").read()
    g = s[s.index('<div class="post-grid">'):]
    top2 = [re.search(r'href="([^"]+)"', b).group(1)
            for b in re.findall(r'<article class="post-card">(.*?)</article>', g, re.S)[:2]]
    ok = sorted(top2) == sorted(SLUGS)
    ck("② %s 语言列表页顶部两张卡正确" % (l or "zh"), ok, str(top2))
for slug in SLUGS:
    n = idx.count('href="%s"' % slug)
    ck("② 根列表页卡片唯一 %s" % slug, n == 1, "出现 %d 次" % n)

# ---------- ③ sitemap ----------
sm = open("sitemap.xml", encoding="utf-8", newline="").read()
for slug in SLUGS:
    for l in ALL:
        u = "https://taigetag.com/" + (l + "/" if l else "") + "blog/" + slug
        pat = "<loc>%s</loc>\r\n    <lastmod>%s</lastmod>" % (u, DATE)
        ck("③ sitemap %s" % u.replace("https://taigetag.com/", ""), pat in sm)
for l in ALL:
    u = "https://taigetag.com/" + (l + "/" if l else "") + "blog/index.html"
    pat = "<loc>%s</loc>\r\n    <lastmod>%s</lastmod>" % (u, DATE)
    ck("③ blog index lastmod %s" % (l or "zh"), pat in sm)

# ---------- ④⑤ 六语属性 + 标题/描述 ----------
class Body(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.tags = []
        self.chars = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "section" and "article-body" in (d.get("class") or ""):
            self.in_body = True
        if self.in_body:
            self.tags.append((tag, d))

    def handle_endtag(self, tag):
        if tag == "section" and self.in_body:
            self.in_body = False

    def handle_data(self, data):
        if self.in_body:
            self.chars.append(data)


for slug in SLUGS:
    for l in ALL:
        p = ("blog/" if not l else l + "/blog/") + slug
        s = open(p, encoding="utf-8").read()
        # 标题
        t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1).strip()
        ck("④ title 非空 %s" % p, len(t) > 20, t[:60])
        # canonical
        can = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        want = "https://taigetag.com/" + (l + "/" if l else "") + "blog/" + slug
        ck("④ canonical 正确 %s" % p, can == want, can)
        # hreflang 7 条
        hl = re.findall(r'<link rel="alternate" hreflang="([^"]*)"', s)
        ck("④ hreflang 7 条 %s" % p, len(hl) == 7 and "zh-Hant" in hl and "x-default" in hl, str(len(hl)))
        # 描述 content
        m = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s, re.S)
        ck("④ description 有 content %s" % p, bool(m) and len(m.group(1)) > 40)

    # ⑤ 根文件 article-body 六语完整
    b = Body()
    b.feed(open("blog/" + slug, encoding="utf-8").read())
    elems = [a for t, a in b.tags if any("data-" + l in a for l in ["zh", "en", "ja", "ko", "fr", "es"])]
    nzh = sum(1 for a in elems if "data-zh" in a)
    missing = []
    for a in elems:
        lack = [l for l in ["en", "ja", "ko", "fr", "es"] if ("data-" + l) not in a]
        if lack:
            missing.append(lack)
    ck("⑤ %s article-body 缺 data-fr/data-es = 0" % slug, not missing,
       "共 %d 个多语元素 / %d 带 data-zh / 缺 %d" % (len(elems), nzh, len(missing)))

    # 生成语言版本内不应再有 data-zh
    for l in LANGS:
        p = "%s/blog/%s" % (l, slug)
        s = open(p, encoding="utf-8").read()
        n = len(re.findall(r'data-zh="', s))
        ck("⑤ %s 无残留 data-zh" % p, n == 0, "%d 处" % n)
        if l in ("en", "fr", "es"):
            seg_ab = s[s.index('class="article-body"'):s.index("</main>")]
            cjk = re.findall(r"[\u4e00-\u9fff]", seg_ab)
            ck("⑤ %s 正文段无中文残留" % p, len(cjk) == 0, "%d 个汉字" % len(cjk))


# ---------- ⑥ 内部链接可达 ----------
for slug in SLUGS:
    s = open("blog/" + slug, encoding="utf-8").read()
    seg = s[s.index('class="article-body"'):s.index("</main>")]
    hrefs = set(re.findall(r'href="([^"#]+)"', seg))
    bad = []
    for h in hrefs:
        if h.startswith(("http", "mailto:", "tel:")):
            continue
        tgt = os.path.normpath(os.path.join("blog", h))
        if not os.path.exists(tgt):
            bad.append(h)
    ck("⑥ %s 正文内部链接可达" % slug, not bad, str(bad))

# ---------- ⑦ 繁体（根目录页不应再被 s2t 改动） ----------
import importlib.util
spec = importlib.util.spec_from_file_location("to_traditional", "to_traditional.py")
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
for slug in SLUGS + ["index.html"]:
    s = open("blog/" + slug, encoding="utf-8").read()
    ck("⑦ 繁体已到位 blog/%s" % slug, mod.convert_html(s) == s)

# ---------- ⑧ 版本号 ----------
mj = open("js/main.js", encoding="utf-8").read()
m = re.search(r'var BUST_VERSION = "([^"]*)";', mj)
ck("⑧ BUST_VERSION = 107", m and m.group(1) == "107", m.group(1) if m else "none")

print("\n===== 结论：%d 项失败 =====" % len(fails))
for f in fails:
    print(" -", f)
sys.exit(1 if fails else 0)
