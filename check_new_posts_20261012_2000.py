#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 2026-10-12 晚间批次两篇新文章：文件/卡片/sitemap/六语渲染/属性完整性/中文残留/引号安全"""
import os, re, sys, json
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
SLUGS = ["dresses-skirts-trims-guide.html", "dancewear-stage-costume-trims-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
DATE = "2026-10-12"
ATTRS = ["zh", "en", "ja", "ko", "fr", "es"]
ok, fail = [], []


def chk(cond, msg):
    (ok if cond else fail).append(msg)


# ---------- 1. 文件存在 ----------
for s in SLUGS:
    for p in ["blog/%s" % s] + ["%s/blog/%s" % (l, s) for l in LANGS]:
        chk(os.path.exists(p), "存在 %s" % p)


# ---------- 1b. 原始文本属性计数（引号/裸双引号的粗筛） ----------
for s in SLUGS:
    src = open("blog/%s" % s, encoding="utf-8").read()
    counts = {a: len(re.findall(r'data-%s="' % a, src)) for a in ATTRS}
    chk(len(set(counts.values())) == 1, "%s 六语属性计数一致：%s" % (s, counts))
    # 属性值内裸双引号会表现为属性名紧邻异常片段，粗筛：值内不允许出现 =" 之外的分隔错误
    bad = re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z\-]*=', src)
    chk(not bad, "%s 属性值内无裸双引号异常（%d 处）" % (s, len(bad)))


# ---------- 2. 中文根页：属性完整性 + 关键结构 ----------
class AttrScan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = 0
        self.total = 0
        self.missing = {l: 0 for l in ATTRS[1:]}
        self.stack = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "section" and d.get("class") == "article-body":
            self.in_body += 1
        elif tag == "section" and self.in_body:
            self.in_body += 1
        if self.in_body and tag in ("p", "h2", "h3", "li", "th", "td", "div", "a", "span") and "data-zh" in d:
            self.total += 1
            for l in self.missing:
                if not d.get("data-%s" % l, "").strip():
                    self.missing[l] += 1

    def handle_endtag(self, tag):
        if tag == "section" and self.in_body:
            self.in_body -= 1


for s in SLUGS:
    src = open("blog/%s" % s, encoding="utf-8").read()
    sc = AttrScan()
    sc.feed(src)
    chk(sc.total > 50, "%s 正文带 data-zh 元素 %d 个" % (s, sc.total))
    chk(sum(sc.missing.values()) == 0, "%s 缺 data-en/ja/ko/fr/es 数量：%s" % (s, sc.missing))
    chk("輔" in src or "連" in src, "%s 已繁化（含繁体字）" % s)
    m = re.search(r'<title[^>]*>(.*?)</title>', src, re.S)
    chk(m and "| TAGE" in m.group(1), "%s 中文 title：%s" % (s, m.group(1)[:60]))
    chk(all(('data-%s' % a) in src for a in ATTRS), "%s title/desc 六语属性齐" % s)
    chk(re.search(r'<meta name="description"[^>]*content="[^"]{30,}"', src, re.S) is not None,
        "%s 静态 description content 非空" % s)
    chk(re.search(r'<link rel="canonical" href="https://taigetag.com/blog/%s">' % re.escape(s), src) is not None,
        "%s canonical 正确" % s)
    chk(src.count('hreflang="ko"') == 1 and src.count('hreflang="x-default"') == 1,
        "%s hreflang 六语 + x-default 各一处" % s)
    chk(src.count("application/ld+json") == 1, "%s JSON-LD 一处" % s)
    for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', src, re.S):
        try:
            json.loads(blk)
            chk(True, "%s JSON-LD 合法" % s)
        except Exception as e:
            chk(False, "%s JSON-LD 非法：%s" % (s, e))
    links = re.findall(r'<a href="([a-z0-9\-]+\.html)"', src)
    chk(len([x for x in links if os.path.exists("blog/%s" % x)]) >= 2,
        "%s 相关文章内链有效：%s" % (s, sorted(set(links))[:6]))
    chk('href="../contact.html"' in src, "%s CTA 指向 ../contact.html" % s)

# ---------- 3. 语言子目录页：title/desc 已本地化，无中文残留 ----------
for s in SLUGS:
    for l in LANGS:
        p = "%s/blog/%s" % (l, s)
        src = open(p, encoding="utf-8").read()
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', src, re.S).group(1)
        has_cjk = bool(re.search(r'[\u4e00-\u9fff]', h1))
        if l in ("en", "fr", "es"):
            chk(not has_cjk, "%s h1 无中文残留：%s" % (p, h1[:50]))
            body = src[src.index('<section class="article-body"'):src.index('</main>')]
            cjk = len(re.findall(r'[\u4e00-\u9fff]', re.sub(r'<[^>]+>', '', body)))
            chk(cjk == 0, "%s 正文（article-body..main）无中文（%d 处）" % (p, cjk))
        else:
            chk(True, "%s h1=%s" % (p, h1[:40]))
        remain = len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=', src))
        chk(remain == 0, "%s 已剔除 data-* 属性（剩 %d）" % (p, remain))
        chk('../../css/style.css' in src and '../../js/main.js' in src,
            "%s 资源路径 ../->../../ 正确" % p)
        chk(('https://taigetag.com/%s/blog/%s' % (l, s)) in src, "%s canonical 指向自身" % p)

# ---------- 4. blog/index.html 卡片 ----------
idx = open("blog/index.html", encoding="utf-8").read()
grid = idx.index('<div class="post-grid">')
cards_order = re.findall(r'<article class="post-card">.*?<a class="more" href="([^"]+)"', idx[grid:], re.S)
chk(cards_order[:2] == SLUGS, "index 卡片顺序前两位=本次新文章：%s" % cards_order[:2])
chk(all(s in cards_order for s in SLUGS), "两张卡片都在卡片列表中")
chk(len(cards_order) == len(set(cards_order)), "卡片 slug 无重复（共 %d 张）" % len(cards_order))
for l in LANGS:
    li = open("%s/blog/index.html" % l, encoding="utf-8").read()
    for s in SLUGS:
        chk(('href="%s"' % s) in li, "%s/blog/index.html 含 %s" % (l, s))

# ---------- 5. sitemap ----------
sm = open("sitemap.xml", encoding="utf-8").read()
for s in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % s] + ["https://taigetag.com/%s/blog/%s" % (l, s) for l in LANGS]:
        chk("<loc>%s</loc>" % u in sm, "sitemap 含 %s" % u)
        blk = re.search(r'<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
        chk(blk and blk.group(1) == DATE, "sitemap lastmod=%s  %s" % (DATE, u))
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    blk = re.search(r'<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    chk(blk and blk.group(1) == DATE, "blog index lastmod=%s  %s" % (DATE, u))
chk(sm.count("<loc>") == len(set(re.findall(r'<loc>([^<]+)</loc>', sm))), "sitemap URL 无重复")

# ---------- 6. BUST_VERSION / 资源版本 ----------
mj = open("js/main.js", encoding="utf-8").read()
chk('var BUST_VERSION = "154";' in mj, "BUST_VERSION = 154")
chk('js/main.js?v=' in idx, "index 引用带版本号 main.js")

print("通过 %d 项，失败 %d 项" % (len(ok), len(fail)))
if fail:
    print("\n==== 失败明细 ====")
    for f in fail:
        print(" -", f)
else:
    print("全部校验通过")
print("\n---- 抽查通过项 ----")
for o in ok[:14]:
    print(" *", o)
