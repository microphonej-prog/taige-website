# -*- coding: utf-8 -*-
"""本地驗收：八語齊全、語言純度、卡片、sitemap、hreflang。"""
import re, os, glob
from html.parser import HTMLParser

ORDER = ["zh", "en", "fr", "es", "ja", "ko", "de", "pt"]
SLUGS = ["garment-trims-faq.html", "trim-material-substitution-guide.html"]
CJK = re.compile(r'[\u4e00-\u9fff]')


class BodyScan(HTMLParser):
    """統計 .article-body 內元素的 data-* 覆蓋"""
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.depth = 0
        self.in_body = False
        self.tags = []
        self.elem = 0
        self.missing = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "section" and "article-body" in (d.get("class") or ""):
            self.in_body = True
            self.depth = 1
            return
        if self.in_body:
            if tag == "section":
                self.depth += 1
            if tag in ("p", "h2", "h3", "li", "td", "th", "div", "a", "span", "strong", "em"):
                if tag == "div" and "container" in (d.get("class") or ""):
                    return
                if "data-zh" in d:
                    self.elem += 1
                    miss = [l for l in ORDER if ("data-" + l) not in d]
                    if miss:
                        self.missing.append((tag, d.get("class"), miss))
                else:
                    self.missing.append((tag, d.get("class"), ["NO data-zh"]))

    def handle_endtag(self, tag):
        if self.in_body and tag == "section":
            self.depth -= 1
            if self.depth == 0:
                self.in_body = False


print("=== 1) 八語覆蓋（.article-body 內元素） ===")
for slug in SLUGS:
    s = open("blog/" + slug, encoding="utf-8").read()
    p = BodyScan()
    p.feed(s)
    print("%-42s 元素 %d，缺語 %d" % (slug, p.elem, len(p.missing)))
    for m in p.missing[:8]:
        print("   ", m)

print("\n=== 2) 語言目錄文件存在 ===")
for slug in SLUGS:
    row = []
    for l in ORDER:
        f = "blog/" + slug if l == "zh" else "%s/blog/%s" % (l, slug)
        row.append("%s=%s" % (l, "OK" if os.path.isfile(f) else "MISSING"))
    print(slug, " ".join(row))

print("\n=== 3) 語言純度（正文首段是否本語種，CJK 殘留） ===")
for l in ORDER:
    f = ("blog/" + SLUGS[0]) if l == "zh" else ("%s/blog/%s" % (l, SLUGS[0]))
    t = open(f, encoding="utf-8").read()
    body = t[t.index('article-body'):t.index('\n</main>')]
    body = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', body, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', body)
    first = " ".join(txt.split())[:60]
    print("%-3s CJK=%d 首段: %s" % (l, len(CJK.findall(body)), first))

print("\n=== 4) noindex / robots ===")
for l in ORDER:
    f = ("blog/" + SLUGS[1]) if l == "zh" else ("%s/blog/%s" % (l, SLUGS[1]))
    t = open(f, encoding="utf-8").read()
    print("%-3s noindex=%s" % (l, "noindex" in t.lower()))

print("\n=== 5) hreflang 條數 / canonical ===")
for l in ORDER:
    f = "blog/" + SLUGS[0] if l == "zh" else "%s/blog/%s" % (l, SLUGS[0])
    t = open(f, encoding="utf-8").read()
    hl = re.findall(r'<link rel="alternate" hreflang="([^"]+)"', t)
    can = re.search(r'<link rel="canonical" href="([^"]+)"', t).group(1)
    print("%-3s hreflang=%d %s | canonical=%s" % (l, len(hl), hl, can))

print("\n=== 6) 列表頁卡片 ===")
s = open("blog/index.html", encoding="utf-8").read()
for slug in SLUGS:
    print(slug, "cards=", s.count('href="%s"' % slug))
for l in ["en", "de", "pt"]:
    t = open("%s/blog/index.html" % l, encoding="utf-8").read()
    print(l, "index cards=", sum(t.count('href="%s"' % x) for x in SLUGS))

print("\n=== 7) sitemap ===")
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    n = len(re.findall(r'<loc>https://taigetag\.com/(?:[a-z]+/)?blog/%s</loc>' % re.escape(slug), sm))
    print(slug, "URL 數 =", n, "| zh:", ("<loc>https://taigetag.com/blog/%s</loc>" % slug) in sm,
          "| de:", ("<loc>https://taigetag.com/de/blog/%s</loc>" % slug) in sm,
          "| lastmod:", re.search(r'<loc>https://taigetag\.com/blog/%s</loc>\s*<lastmod>([^<]+)' % re.escape(slug), sm).group(1))
print("sitemap 總 URL =", sm.count("<loc>"))

print("\n=== 8) 屬性引號畸形掃描 ===")
for f in ["blog/" + s for s in SLUGS] + ["%s/blog/%s" % (l, s) for l in ORDER[1:] for s in SLUGS]:
    t = open(f, encoding="utf-8").read()
    bad = re.findall(r'data-(?:zh|en|fr|es|ja|ko|de|pt)=""', t)
    odd = re.findall(r'<div class="crumb">.*?</div>', t, re.S)
    if bad:
        print("  ! 空屬性", f, len(bad))
print("  掃描完成")
