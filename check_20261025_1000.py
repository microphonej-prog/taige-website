# -*- coding: utf-8 -*-
"""2026-10-25 10:00 批次校验：六语属性完整性 / 语言页渲染 / 卡片 / sitemap / 中文字数"""
import re, os, json
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
LANGS = ("en", "fr", "es", "ja", "ko")
SLUGS = ["german-supply-chain-act-trims-suppliers.html", "trim-export-incoterms-guide.html"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.bad, self.count, self.tags = [], 0, 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        self.tags += 1
        if "data-zh" in d:
            self.count += 1
            miss = [l for l in LANGS if ("data-" + l) not in d]
            empty = [k for k, v in d.items() if k.startswith("data-") and (v is None or not v.strip())]
            if miss or empty:
                self.bad.append((tag, miss, empty, (d.get("data-zh") or "")[:40]))


print("=== 1. 根目录页（繁体中文）===")
for slug in SLUGS:
    f = "blog/" + slug
    s = open(f, encoding="utf-8").read()
    p = P(); p.feed(s)
    zh = len(re.findall(r"[\u4e00-\u9fff]", " ".join(re.findall(r'data-zh="([^"]*)"', s))))
    t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1)
    d = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s, re.S).group(1)
    print("%-46s data-zh元素=%d 标签=%d 缺失=%d 中文字数≈%d" % (slug, p.count, p.tags, len(p.bad), zh))
    print("   title:", t[:70])
    print("   desc :", d[:60], "...(%d)" % len(d))
    for b in p.bad[:8]:
        print("   缺失:", b)
    # JSON-LD
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    ok = 0
    for b in blocks:
        try:
            json.loads(b); ok += 1
        except Exception as e:
            print("   JSON-LD 非法:", e)
    print("   JSON-LD 块=%d 合法=%d" % (len(blocks), ok))
    # 裸双引号 / 空属性
    for k in ("data-zh", "data-en", "data-fr", "data-es", "data-ja", "data-ko"):
        n = len(re.findall(k + r'=""', s))
        if n:
            print("   空属性 %s x%d" % (k, n))
    # 相关文章内链存在的文件
    for m in re.finditer(r'<li><a href="([a-z0-9\-]+\.html)"', s):
        t2 = os.path.join("blog", m.group(1))
        if not os.path.exists(t2):
            print("   ！死链:", m.group(1))

print("\n=== 2. 语言页渲染 ===")
for lang in LANGS:
    for slug in SLUGS:
        f = "%s/blog/%s" % (lang, slug)
        s = open(f, encoding="utf-8").read()
        t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1)
        html_lang = re.search(r'<html lang="([^"]*)"', s).group(1)
        body = s[s.index('<section class="article-body">'):s.index("</main>")]
        h2s = re.findall(r"<h2[^>]*>(.*?)</h2>", body, re.S)
        cjk_res = len(re.findall(r'data-zh="', body))
        zh_res = len(re.findall(r"[\u4e00-\u9fff]", body))
        print("%-3s %-46s lang=%s h2=%d 残留data-zh=%d 正文汉字=%d" %
              (lang, slug[:46], html_lang, len(h2s), cjk_res, zh_res))
        print("     title:", t[:80])

print("\n=== 3. 卡片 ===")
for lang in ("",) + LANGS:
    f = ("%s/blog/index.html" % lang) if lang else "blog/index.html"
    s = open(f, encoding="utf-8").read()
    print("%-24s 卡片: %s" % (f, [slug for slug in SLUGS if slug in s]))

print("\n=== 4. sitemap ===")
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    for pre in [""] + ["%s/" % l for l in LANGS]:
        u = "https://taigetag.com/%sblog/%s" % (pre, slug)
        print("  %-70s %s" % (u, "OK" if ("<loc>%s</loc>" % u) in sm else "缺失!"))
print("  blog index lastmod:", re.findall(r"<loc>https://taigetag.com/blog/index.html</loc>\s*<lastmod>([^<]*)</lastmod>", sm))

print("\n=== 5. 版本号 ===")
print(" ", re.search(r'var BUST_VERSION = "([^"]*)";', open("js/main.js", encoding="utf-8").read()).group(1))
