#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""本地校验 v2：六语正文属性 / 列表卡片 / sitemap / canonical+hreflang / JSON-LD / 语言纯度。"""
import json, os, re, sys
from html.parser import HTMLParser

os.chdir(os.path.dirname(os.path.abspath(__file__)))
SLUGS = ["trim-inner-packing-spec.html", "adhesive-trim-shelf-life.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
CJK = re.compile(r"[\u3400-\u9fff]")
SIMP_ONLY = "这们说时对开为个门发产业务实现问题价签质纸买卖东华龙马鸟凤龟龄铁银铜针线组织经营济统计计划让给还过应该样种"
fails = []


class BodyScan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.n = 0
        self.missing = []

    def handle_starttag(self, tag, attrs):
        if tag in ("br", "img", "input", "meta", "link"):
            return
        d = dict(attrs)
        if not any(k.startswith("data-") for k in d):
            return
        self.n += 1
        miss = [l for l in LANGS if "data-" + l not in d]
        if miss:
            self.missing.append((tag, d.get("data-zh", "")[:30], miss))


print("== 1) 正文属性完整性（各语言页面） ==")
for lang in LANGS:
    for slug in SLUGS:
        p = "blog/%s" % slug if lang == "zh" else "%s/blog/%s" % (lang, slug)
        s = open(p, encoding="utf-8").read()
        m = re.search(r'<section class="article-body">(.*?)</section>', s, re.S)
        assert m, "article-body 缺失 " + p
        body = m.group(1)
        bs = BodyScan()
        bs.feed(body)
        text = re.sub(r"<[^>]+>", " ", body)
        text = re.sub(r"\s+", " ", text).strip()
        info = "可见文本 %d 字符" % len(text)
        if lang != "zh":
            if len(text) < 1500:
                fails.append("%s 正文过短 %d" % (p, len(text)))
            if lang in ("en", "fr", "es", "ko") and CJK.search(text):
                fails.append("%s 正文含汉字 %d" % (p, len(CJK.findall(text))))
            if lang in ("ja", "ko"):
                bad = [c for c in SIMP_ONLY if c in text]
                if bad:
                    fails.append("%s 含简体字 %s" % (p, "".join(bad)))
        print("  %-3s %-46s data属性元素=%3d 缺属性=%d  %s"
              % (lang, slug[:44], bs.n, len(bs.missing), info))
        if bs.missing:
            fails.append("%s 缺语言属性 %s" % (p, bs.missing[:3]))

print("\n== 2) blog/index.html 新卡片 ==")
idx = open("blog/index.html", encoding="utf-8").read()
for slug in SLUGS:
    n = idx.count('href="%s"' % slug)
    print("  %-46s 卡片链接 %d" % (slug, n))
    if n != 1:
        fails.append("index 卡片数异常 %s=%d" % (slug, n))

print("\n== 3) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
miss = []
for slug in SLUGS:
    for pre in ["blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"]:
        u = "https://taigetag.com/%s%s" % (pre, slug)
        if "<loc>%s</loc>" % u not in sm:
            miss.append(u)
print("  <loc> 总数 %d，新增 12 URL 缺失 %d" % (sm.count("<loc>"), len(miss)))
fails.extend(miss)
for pre in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
    u = "https://taigetag.com/%sblog/index.html" % pre
    m = re.search(r'<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    if not (m and m.group(1) == "2026-10-18"):
        fails.append("lastmod 未更新 " + u)
print("  blog index lastmod 六语检查完成")

print("\n== 4) canonical / hreflang / JSON-LD / title 语言 ==")
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
        ld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
        if len(ld) != 1:
            fails.append("JSON-LD 数量 %d %s" % (len(ld), p))
        for blk in ld:
            try:
                json.loads(blk)
            except Exception as e:
                fails.append("JSON-LD 解析失败 %s: %s" % (p, e))
        t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1).strip()
        if lang in ("en", "fr", "es", "ko") and CJK.search(t):
            fails.append("title 含汉字 %s" % p)
        if len(t) < 15:
            fails.append("title 过短 %s: %s" % (p, t))
print("  六语 canonical/hreflang/JSON-LD/title 检查完成")

print("\n== 5) main.js 语法 + BUST_VERSION ==")
import subprocess
_r = subprocess.run(['F:/hermes/node/node.exe', '--check', 'C:/Users/micro/taige-website/js/main.js'],
                    capture_output=True, text=True)
r = _r.returncode
mj = open("js/main.js", encoding="utf-8").read()
bv = re.search(r'BUST_VERSION = "(\d+)"', mj).group(1)
print("  node --check rc=%d  BUST_VERSION=%s  stderr=%s" % (r, bv, (_r.stderr or "").strip()[:120]))
if r != 0:
    fails.append("main.js 语法错误")
if bv != "170":
    fails.append("BUST_VERSION 未升到 170")

print("\n结论：失败 %d 项" % len(fails))
for f in fails[:25]:
    print("  !!", f)
sys.exit(1 if fails else 0)
