# -*- coding: utf-8 -*-
"""2026-10-13 下午批次本地校验：文件 / 六语属性完整 / 语言页残留 / 列表首卡 / sitemap / BUST / 内链"""
import os, re, glob, sys
from html.parser import HTMLParser

ROOT = "C:/Users/micro/taige-website"
os.chdir(ROOT)
SLUGS = ["garment-embroidery-decoration-guide.html",
         "animal-derived-material-certification-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
TODAY = "2026-10-13"
SIMPLIFIED_ONLY = "这个们为说时应发进对开还没经过样类录签纸张关现价购单双"
CHROME = ["微信", "在線", "發送"]   # 站点通用 assist 组件文案，六语页一律繁体，非本批次问题

fails = []


def fail(msg):
    fails.append(msg)
    print("  [FAIL] " + msg)


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs), self.getpos()[0]))


print("=== 1) 文件存在性（2 篇 × 6 语）===")
for slug in SLUGS:
    for p in ["blog/" + slug] + ["%s/blog/%s" % (l, slug) for l in LANGS]:
        if os.path.exists(p):
            print("  ok %-64s %d KB" % (p, os.path.getsize(p) // 1024))
        else:
            fail("缺失文件 " + p)

print("=== 2) 中文根页：article-body 内 data-* 元素六语完整性 ===")
for slug in SLUGS:
    s = open("blog/" + slug, encoding="utf-8").read()
    seg = s[s.index('<section class="article-body">'):s.index("\n</main>")]
    p = P(); p.feed(seg)
    tot = miss = 0
    for tag, a, line in p.tags:
        if not any(k.startswith("data-") for k in a):
            continue
        tot += 1
        lack = [l for l in ["zh", "en", "ja", "ko", "fr", "es"] if ("data-" + l) not in a]
        if lack:
            miss += 1
            fail("%s 行%d <%s> 缺 %s" % (slug, line, tag, lack))
    print("  %s: 带 data-* 元素 %d，缺语言 %d" % (slug, tot, miss))
    if re.search(r'data-(?:zh|en|ja|ko|fr|es)=""', seg):
        fail(slug + " 存在畸形空属性")
    # 正文中英文页不应有简化字残留（此处查中文根页无需）
    for kw in ["绣花", "刺绣", "LWG", "RWS", "RDS", "动物源"] if "animal" in slug else ["绣花", "针数", "衬料"]:
        print("     关键词 %-6s: %d 次" % (kw, seg.count(kw)))

print("=== 3) 各语言页残留检查 ===")
for slug in SLUGS:
    for lang in LANGS:
        p = "%s/blog/%s" % (lang, slug)
        s = open(p, encoding="utf-8").read()
        body = s[s.index("<body"):]
        txt = re.sub(r'<[^>]+>', ' ', body)
        for c in CHROME:
            txt = txt.replace(c, '')
        cjk = len(re.findall(r'[\u4e00-\u9fff]', txt))
        simp = sum(txt.count(c) for c in SIMPLIFIED_ONLY)
        html_lang = re.search(r'<html lang="([^"]*)"', s).group(1)
        t = re.search(r'<title>(.*?)</title>', s, re.S).group(1)
        dattr = len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=', body))
        flag = ""
        if lang in ("en", "fr", "es") and cjk:
            flag += " CJK残留=%d" % cjk
        if simp:
            flag += " 简体残留=%d" % simp
        if dattr:
            flag += " 残留data属性=%d" % dattr
        if html_lang != lang:
            flag += " html.lang=%s" % html_lang
        if flag:
            fail("%s %s%s" % (p, flag, ""))
        print("  %-58s lang=%-3s CJK=%-4d 简体=%-3d data属性=%-3d title=%s"
              % (p, html_lang, cjk, simp, dattr, t[:52]))

print("=== 4) blog/index.html 首两张卡片 ===")
for lang in ["zh"] + LANGS:
    p = "blog/index.html" if lang == "zh" else "%s/blog/index.html" % lang
    s = open(p, encoding="utf-8").read()
    cards = re.findall(r'<article class="post-card">(.*?)</article>', s, re.S)
    print("  %-24s 卡片总数=%d" % (p, len(cards)))
    for i, c in enumerate(cards[:2]):
        m = re.search(r'href="([^"]+)"', c)
        bad = not any(sl in m.group(1) for sl in SLUGS)
        if bad:
            fail("%s 第%d张卡不是本次新文章: %s" % (p, i + 1, m.group(1)))
        nattrs = len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=', c))
        print("     卡%d href=%-46s data属性=%d" % (i + 1, m.group(1), nattrs))

print("=== 5) sitemap.xml ===")
sm = open("sitemap.xml", encoding="utf-8").read()
n_new = 0
for slug in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % slug] + \
             ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        m = re.search(r'<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
        if not m:
            fail("sitemap 缺 " + u)
        elif m.group(1) != TODAY:
            fail("sitemap lastmod 错 %s -> %s" % (u, m.group(1)))
        else:
            n_new += 1
print("  新增文章 URL 各语言合计正确: %d / 12" % n_new)
i = 0
for u in ["https://taigetag.com/blog/index.html"] + \
         ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    m = re.search(r'<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    if not m or m.group(1) != TODAY:
        fail("blog index lastmod 未更新: " + u)
    else:
        i += 1
print("  blog 列表页 lastmod 更新正确: %d / 6" % i)
print("  <loc> 总数:", sm.count("<loc>"))
# sitemap 与文件一致性（抽查本次新 URL）
for slug in SLUGS:
    for l in ["", "en/", "fr/", "es/", "ja/", "ko/"]:
        f = "%sblog/%s" % (l, slug)
        if not os.path.exists(f):
            fail("sitemap 有 URL 但缺文件: " + f)

print("=== 6) BUST_VERSION / main.js ===")
mj = open("js/main.js", encoding="utf-8").read()
b = re.search(r'var BUST_VERSION = "(\d+)";', mj).group(1)
print("  BUST_VERSION =", b)
if b != "155":
    fail("BUST_VERSION 不是 155")

print("=== 7) 新文章内链可达性 ===")
for slug in SLUGS:
    s = open("blog/" + slug, encoding="utf-8").read()
    for href in set(re.findall(r'href="([^"#]+)"', s)):
        if href.startswith(("http", "mailto", "../", "tel:", "data:", "sms:", "javascript:")):
            continue
        if not os.path.exists("blog/" + href):
            fail("%s 内链断链: %s" % (slug, href))
        else:
            print("  ok %s -> %s" % (slug[:26], href))

print()
print("=" * 60)
print("本地校验结论:", "全部通过" if not fails else "存在 %d 项问题" % len(fails))
for f in fails:
    print("  -", f)
sys.exit(0 if not fails else 1)
