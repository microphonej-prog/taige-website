#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-22 晚间批次本地全量校验：六语属性、标题、canonical/sitemap、JSON-LD、卡片、BUST、内链。"""
import re, json, os, sys
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')
SLUGS = ["eu-digital-product-passport-trims.html", "trims-carbon-footprint-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
EXP_TITLE = {
    "eu-digital-product-passport-trims.html": {
        "en": "Digital Product Passport", "ja": "デジタル製品パスポート",
        "ko": "디지털 제품 여권", "fr": "Passeport numérique", "es": "Pasaporte digital de producto"},
    "trims-carbon-footprint-guide.html": {
        "en": "Carbon Footprint", "ja": "カーボンフットプリント",
        "ko": "탄소발자국", "fr": "Empreinte carbone", "es": "Huella de carbono"},
}
TAGS = ['h1', 'h2', 'h3', 'h4', 'p', 'strong', 'small', 'a', 'span', 'div', 'button',
        'li', 'th', 'td', 'label', 'option', 'figcaption', 'caption', 'dt', 'dd', 'em',
        'b', 'i', 'blockquote', 'summary', 'cite']
fails = []


def fail(msg):
    fails.append(msg)
    print("  [FAIL] " + msg)


def paths():
    out = []
    for s in SLUGS:
        out.append(("blog/" + s, s, ""))
        for l in LANGS:
            out.append(("%s/blog/%s" % (l, s), s, l))
    for l in [""] + LANGS:
        out.append(("%sblog/index.html" % (l + "/" if l else ""), None, l))
    return out


print("== 1) 文件存在 / 六语属性完整性 / 标题 / h1 ==")
class Body(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False; self.n = 0; self.missing = 0; self.tags = []
    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        if tag == "section" and d.get("class", "").startswith("article-body"):
            self.in_body = True; return
        if self.in_body:
            self.n += 1
            if "data-zh" in d:
                for k in ("data-en", "data-fr", "data-es", "data-ja", "data-ko"):
                    if not d.get(k, "").strip():
                        self.missing += 1
                        if self.missing <= 3:
                            fail("%s <%s> 缺 %s" % (self.f, tag, k))
    def handle_endtag(self, tag):
        if self.in_body and tag == "section":
            self.in_body = False


ALL = paths()
for p, slug, lang in ALL:
    if not os.path.exists(p):
        fail("文件缺失 %s" % p); continue
    s = open(p, encoding="utf-8").read()
    # 标题
    m = re.search(r'<title[^>]*>(.*?)</title>', s, re.S)
    title = m.group(1).strip()
    if "TAGE" not in title:
        fail("%s 标题未含 TAGE：%s" % (p, title[:60]))
    exp = EXP_TITLE.get(slug, {}).get(lang)
    if exp and exp not in title:
        fail("%s 标题不含关键词 %s：%s" % (p, exp, title[:80]))
    if lang == "" and slug:
        if not re.search(r'<title[^>]*data-zh="[^"]*"', s):
            fail("%s 根页 title 缺 data-zh" % p)
        # 静态 description 必须是中文（爬虫读 content），且与 data-zh 一致
        mdb = re.search(r'<meta name="description".*?>', s, re.S).group(0)
        cval = re.search(r'content="([^"]*)"', mdb).group(1)
        dz = re.search(r'data-zh="([^"]*)"', mdb).group(1)
        if not re.search(r'[\u4e00-\u9fff]', cval):
            fail("%s 根页 description content 非中文" % p)
        if cval != dz:
            fail("%s 根页 description content != data-zh" % p)
        if not 80 <= len(cval) <= 120:
            fail("%s 中文 description 长度 %d 不在 80-120" % (p, len(cval)))
        den = re.search(r'data-en="([^"]*)"', mdb).group(1)
        if not 150 <= len(den) <= 160:
            fail("%s 英文 description 长度 %d 不在 150-160" % (p, len(den)))
    if slug:
        m2 = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
        if not m2 or not m2.group(1).strip():
            fail("%s 缺 h1" % p)
        b = Body(); b.f = p; b.feed(s)
        if b.n == 0:
            fail("%s article-body 未解析到元素" % p)
        if b.missing:
            fail("%s 正文六语属性缺失 %d 处" % (p, b.missing))
        # 根页仍应保留六语 data 属性（供 gen_i18n 与语言切换）
        if lang == "":
            for k in ("data-zh", "data-en", "data-fr", "data-es", "data-ja", "data-ko"):
                if ('%s=' % k) not in s:
                    fail("%s 缺 %s" % (p, k))
        # 语言页不应残留其它语言 data-*
        else:
            if re.search(r'data-(?:zh|en|fr|es|ja|ko)=', s):
                fail("%s 语言页残留 data-* 属性" % p)
        # JSON-LD
        for m3 in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            try:
                json.loads(m3.group(1))
            except Exception as e:
                fail("%s JSON-LD 非法：%s" % (p, e))
    print("  ok  %s  title=%s" % (p, title[:52]))

print("== 2) 语言首页 title 与 h1 渲染（en/ja/ko/fr/es） ==")
for p, slug, lang in ALL:
    if not slug or lang == "":
        continue
    s = open(p, encoding="utf-8").read()
    t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S).group(1)
    if re.search(r'[\u4e00-\u9fff]', t) and lang != "ja":
        fail("%s 标题残留中文：%s" % (p, t[:60]))
    if lang == "ja" and re.search(r'[，。；：]', t) and "：" in t and "タグ" not in t:
        pass
    print("      %s | h1=%s" % (t[:60], re.sub(r'<[^>]+>', '', h1)[:40]))

print("== 3) blog/index.html 卡片（六语） ==")
for l in [""] + LANGS:
    p = "%sblog/index.html" % (l + "/" if l else "")
    s = open(p, encoding="utf-8").read()
    grid = s[s.index('<div class="post-grid">'):]
    for slug in SLUGS:
        if 'href="%s"' % slug not in grid:
            fail("%s post-grid 缺卡片 %s" % (p, slug))
    if l == "":
        for k in ("data-zh", "data-en", "data-fr", "data-es", "data-ja", "data-ko"):
            if k not in grid:
                fail("根 blog/index.html 卡片缺 %s" % k)
    print("  ok  %s 卡片齐全" % p)

print("== 4) sitemap 与 canonical 一致性 ==")
sm = open("sitemap.xml", encoding="utf-8", newline="").read()
for p, slug, lang in ALL:
    if not slug:
        continue
    url = "https://taigetag.com/" + p.replace("index.html", "").rstrip("/") if False else None
    pre = (lang + "/") if lang else ""
    url = "https://taigetag.com/%sblog/%s" % (pre, slug)
    if "<loc>%s</loc>" % url not in sm:
        fail("sitemap 缺 %s" % url)
    can = re.search(r'<link rel="canonical" href="([^"]*)">', open(p, encoding="utf-8").read())
    if can.group(1) != url:
        fail("%s canonical=%s 与 sitemap %s 不一致" % (p, can.group(1), url))
block = re.search(r'<loc>https://taigetag.com/blog/eu-digital-product-passport-trims.html</loc>\s*<lastmod>([^<]*)</lastmod>', sm)
print("  新条目 lastmod:", block.group(1) if block else "未找到")
for l in [""] + LANGS:
    u = "https://taigetag.com/%sblog/index.html" % ((l + "/") if l else "")
    m = re.search(r'<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    if not m or m.group(1) != "2026-09-22":
        fail("blog index lastmod 未更新：%s -> %s" % (u, m.group(1) if m else None))
print("  <loc> 总数:", sm.count("<loc>"))

print("== 5) BUST_VERSION / 版本号 ==")
mj = open("js/main.js", encoding="utf-8").read()
bust = re.search(r'var BUST_VERSION = "([^"]*)";', mj).group(1)
print("  BUST_VERSION =", bust)
if bust != "101":
    fail("BUST_VERSION 不是 101：%s" % bust)

print("== 6) 内链有效性（相关文章链接） ==")
for p, slug, lang in ALL:
    if not slug:
        continue
    d = os.path.dirname(p)
    s = open(p, encoding="utf-8").read()
    for href in re.findall(r'<a href="([^"#]+)"', s):
        if href.startswith(("http", "mailto", "../", "tel:", "#")):
            continue
        target = os.path.join(d, href)
        if not os.path.exists(target):
            fail("%s 内链失效：%s" % (p, href))
print("  内链检查完成")

print("\n结果：", "全部通过 ✅" if not fails else "失败 %d 项 ❌" % len(fails))
sys.exit(1 if fails else 0)
