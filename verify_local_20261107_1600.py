# -*- coding: utf-8 -*-
"""2026-11-07 16:00 批次本地校验：属性完整性 / 语言纯度 / 标题 / 卡片 / sitemap。"""
import os, re, sys
from html.parser import HTMLParser

os.chdir(os.path.dirname(os.path.abspath(__file__)))
SLUGS = ["clothing-label-compliance-central-america.html",
         "clothing-label-compliance-morocco-tunisia.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]


class AttrScan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = 0
        self.missing = []
        self.chars = {k: 0 for k in ["zh", "en", "ja", "ko", "fr", "es"]}
        self.total = 0

    def handle_starttag(self, tag, attrs):
        if tag == "section" and dict(attrs).get("class") == "article-body":
            self.in_body = 1
            return
        if not self.in_body or tag in ("meta", "link", "br", "img", "input"):
            return
        d = dict(attrs)
        if not any(k.startswith("data-") for k in d):
            return
        self.total += 1
        for l in self.chars:
            if "data-" + l not in d:
                self.missing.append((tag, l, (d.get("data-zh") or "")[:24]))
        z = d.get("data-zh") or ""
        self.chars["zh"] += len(re.findall(r"[\u4e00-\u9fff]", z))

    def handle_endtag(self, tag):
        if tag == "section" and self.in_body:
            self.in_body = 0


def cjk(s):
    return re.findall(r"[\u4e00-\u9fff]", s)


ok = True
for slug in SLUGS:
    p = "blog/" + slug
    s = open(p, encoding="utf-8").read()
    sc = AttrScan()
    sc.feed(s)
    print("%s 正文带 data-* 元素 %d 个；缺失属性 %d 处；中文字数 %d"
          % (slug, sc.total, len(sc.missing), sc.chars["zh"]))
    if sc.missing:
        ok = False
        print("   缺失样例:", sc.missing[:6])
    title = re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1)
    print("   title:", title[:70])
    print("   h1:", re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S).group(1)[:60])
    print("   canonical:", re.search(r'rel="canonical" href="([^"]+)"', s).group(1))
    print("   hreflang 数:", len(re.findall(r'rel="alternate"', s)))
    print("   JSON-LD:", s.count("application/ld+json"))
    # 属性值内裸双引号检查：data-xx="..." 后紧跟非 > 或换行的 quote 异常
    bad = re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)
    if bad:
        ok = False
        print("   空属性:", len(bad))

for lang in LANGS:
    for slug in SLUGS:
        p = "%s/blog/%s" % (lang, slug)
        s = open(p, encoding="utf-8").read()
        t = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
        i0 = s.index('<section class="article-body">')
        i1 = s.index("</main>")
        body = s[i0:i1]
        left = len(cjk(body))
        print("%s/%s title=%s | 正文汉字=%d" % (lang, slug[:38], t[:48], left))
        if lang != "ja" and left > 0:
            ok = False
            print("   残留样例:", re.findall(r"[^<>\n]{0,20}[\u4e00-\u9fff]+[^<>\n]{0,20}", body)[:3])
        if lang == "ja":
            simp = re.findall(r"[语说时间发现标签证货单价质纸带丝织卫读请让认规则术专业务东车马鸟鱼龙长门问组对个么为与从里后头买卖学习见观电]", body)
            if simp:
                ok = False
                print("   日文页残留简体字形:", "".join(sorted(set(simp))))

idx = open("blog/index.html", encoding="utf-8").read()
for slug in SLUGS:
    print("卡片 %s : %s" % (slug, idx.count('href="%s"' % slug)))

sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    urls = re.findall(r"<loc>([^<]*%s)</loc>" % re.escape(slug), sm)
    print("sitemap %s : %d 条" % (slug, len(urls)))
print("js BUST:", re.search(r'BUST_VERSION = "(\d+)"', open("js/main.js", encoding="utf-8").read()).group(1))
print("RESULT:", "PASS" if ok else "CHECK FAILED")
