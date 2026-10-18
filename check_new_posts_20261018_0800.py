#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""本地校验：六语正文属性 / 列表卡片 / sitemap / canonical+hreflang / JSON-LD / 语言纯度。"""
import glob, json, os, re, sys
from html.parser import HTMLParser

os.chdir(os.path.dirname(os.path.abspath(__file__)))
SLUGS = ["trim-invoice-tax-export-rebate.html", "packaging-automation-bag-compatibility.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
CJK = re.compile(r"[\u3400-\u9fff]")
SIMP = re.compile(r"[这儿说当时对开为体个门发产业务实现问题标准化价签质纸买卖东华龙马鸟凤龟龄铁银铜针线条级组织经营济统计计划]")
fails = []


class BodyScan(HTMLParser):
    def __init__(self, lang):
        super().__init__(convert_charrefs=False)
        self.lang = lang
        self.n = 0
        self.missing = []

    def handle_starttag(self, tag, attrs):
        if tag in ("br", "img", "input", "meta", "link"):
            return
        d = dict(attrs)
        if not any(k.startswith("data-") for k in d):
            return
        self.n += 1
        if "data-%s" % self.lang not in d:
            self.missing.append((tag, d.get("data-zh", "")[:30]))


print("== 1) 六语页面：正文属性完整性 + 语言纯度 ==")
for lang in LANGS:
    for slug in SLUGS:
        p = "blog/%s" % slug if lang == "zh" else "%s/blog/%s" % (lang, slug)
        s = open(p, encoding="utf-8").read()
        m = re.search(r'<section class="article-body">(.*?)</section>', s, re.S)
        assert m, "article-body 缺失 " + p
        body = m.group(1)
        bs = BodyScan(lang)
        bs.feed(body)
        # 正文可见文本里的汉字（非中文页应为 0）
        text = re.sub(r"<[^>]+>", " ", body)
        cjk = len(CJK.findall(text)) if lang not in ("zh", "ja") else -1
        extra = ""
        if lang in ("en", "fr", "es") and cjk != 0:
            extra = " 汉字=%d" % cjk
            fails.append(("%s 正文汉字 %d" % (p, cjk)))
        if bs.missing:
            fails.append(("%s 缺 data-%s: %s" % (p, lang, bs.missing[:3])))
        print("  %-3s %-46s 元素=%3d 缺属性=%d%s" % (lang, slug[:44], bs.n, len(bs.missing), extra))

print("\n== 2) blog/index.html 新卡片 ==")
idx = open("blog/index.html", encoding="utf-8").read()
for slug in SLUGS:
    n = idx.count('href="%s"' % slug)
    print("  %-46s 卡片链接 %d" % (slug, n))
    if n < 1:
        fails.append("index 缺卡片 " + slug)

print("\n== 3) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    for pre in ["blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"]:
        u = "https://taigetag.com/%s%s" % (pre, slug)
        if "<loc>%s</loc>" % u not in sm:
            fails.append("sitemap 缺 " + u)
print("  <loc> 总数 %d；新增 12 URL 检查完成" % sm.count("<loc>"))
for pre in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
    u = "https://taigetag.com/%sblog/index.html" % pre
    m = re.search(r'<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    ok = m and m.group(1) == "2026-10-18"
    print("  lastmod %-46s %s" % (u, "OK" if ok else "FAIL"))
    if not ok:
        fails.append("lastmod 未更新 " + u)

print("\n== 4) canonical / hreflang / JSON-LD ==")
for lang in LANGS:
    for slug in SLUGS:
        p = "blog/%s" % slug if lang == "zh" else "%s/blog/%s" % (lang, slug)
        s = open(p, encoding="utf-8").read()
        canon = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        want = "https://taigetag.com/%sblog/%s" % ("" if lang == "zh" else lang + "/", slug)
        if canon != want:
            fails.append("canonical 不一致 %s: %s" % (p, canon))
        hl = dict(re.findall(r'hreflang="([^"]*)" href="([^"]*)"', s))
        if len(hl) != 7:
            fails.append("hreflang 数量 %d %s" % (len(hl), p))
        for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            try:
                json.loads(m)
            except Exception as e:
                fails.append("JSON-LD 解析失败 %s: %s" % (p, e))
        # title 语言
        t = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
        if lang in ("en", "fr", "es") and CJK.search(t):
            fails.append("title 含汉字 %s" % p)
        if lang == "ko" and CJK.search(t):
            fails.append("ko title 含汉字 %s" % p)
print("  六语 canonical/hreflang/JSON-LD 检查完成")

print("\n== 5) main.js 语法 ==")
r = os.system('node --check js/main.js > /dev/null 2>&1')
print("  node --check rc=%d" % r)
if r != 0:
    fails.append("main.js 语法错误")

print("\n结论：失败 %d 项" % len(fails))
for f in fails[:20]:
    print("  !!", f)
sys.exit(1 if fails else 0)
