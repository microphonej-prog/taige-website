# -*- coding: utf-8 -*-
"""2026-11-15 14:00 验收：属性齐全 / 语言页中文残留 / 卡片 / sitemap / hreflang 目标存在。"""
import html.parser
import os
import re
import sys

SLUGS = ["clothing-tagging-gun-swift-tack-guide", "garment-label-font-size-legibility-guide"]
LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
FILES = {(l, s): (("blog/%s.html" % s) if l == "zh" else ("%s/blog/%s.html" % (l, s))) for l in LANGS for s in SLUGS}


class P(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.bad = []
        self.total = 0
        self.stack = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "data-zh" in d:
            self.total += 1
            miss = [l for l in LANGS if "data-%s" % l not in d]
            if miss:
                self.bad.append((tag, d.get("data-zh", "")[:40], miss))
        if not d and "data-bg" not in d:
            pass


def check_attrs(path):
    src = open(path, encoding="utf-8").read()
    body = src[src.index('class="article-body"') if 'class="article-body"' in src else 0:]
    p = P()
    p.feed(src)
    return p.total, p.bad


print("=== ① 属性齐全（全页扫描）===")
ok = True
for l in LANGS:
    for s in SLUGS:
        f = FILES[(l, s)]
        if not os.path.exists(f):
            print("缺失文件", f)
            ok = False
            continue
        total, bad = check_attrs(f)
        flag = "OK" if not bad else "BAD"
        if bad:
            ok = False
        print("%s %-52s data-zh 元素 %3d 缺语言 %d %s" % (flag, f, total, len(bad), bad[:3] if bad else ""))

print("\n=== ② 语言页正文中文残留（fr/es/ja/ko，排除品牌名与语言按钮标题）===")
CJK = re.compile(r"[\u4e00-\u9fff]")
ALLOW = ["泰閣", "泰阁", "江磊", "張旭勝", "陳清港", "東莞泰閣包裝製品有限公司", "首頁", "輔料 FAQ",
         "日本語", "繁體中文", "한국어", "Français", "Español", "English", "中文"]
for l in ["fr", "es", "ja", "ko"]:
    for s in SLUGS:
        f = "%s/blog/%s.html" % (l, s)
        src = open(f, encoding="utf-8").read()
        m = re.search(r'<section class="article-body">(.*?)</section>', src, re.S)
        seg = m.group(1) if m else ""
        seg = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", seg, flags=re.S)
        # 只看标签之间的可见文本与属性值
        texts = re.findall(r">([^<>]+)<", seg) + re.findall(r'data-[a-z]{2}="([^"]*)"', seg)
        hits = []
        for t in texts:
            if CJK.search(t):
                hits.append(t.strip()[:60])
        print("%-6s %-50s 中文片段 %d" % (l, s, len(hits)))
        for h in hits[:5]:
            print("      ", h)

print("\n=== ③ blog/index.html 卡片 ===")
for l in LANGS:
    f = "blog/index.html" if l == "zh" else "%s/blog/index.html" % l
    src = open(f, encoding="utf-8").read()
    c = [s for s in SLUGS if 'href="%s.html"' % s in src]
    print("%-4s %s -> %d/2 卡片" % (l, f, len(c)))

print("\n=== ④ sitemap 覆盖 ===")
sm = open("sitemap.xml", encoding="utf-8").read()
for s in SLUGS:
    n = len(re.findall(r"<loc>https://taigetag\.com/(?:[a-z]{2}/)?blog/%s\.html</loc>" % s, sm))
    print("%-50s %d/6" % (s, n))

print("\n=== ⑤ hreflang 目标存在性 ===")
for l in LANGS:
    for s in SLUGS:
        f = FILES[(l, s)]
        src = open(f, encoding="utf-8").read()
        links = re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', src)
        miss = []
        for code, url in links:
            rel = url.replace("https://taigetag.com/", "")
            p = "index.html" if rel in ("", "/") else rel
            if not os.path.exists(p):
                miss.append((code, rel))
        print("%-4s %-46s alternates=%d 目标缺失=%d %s" % (l, s, len(links), len(miss), miss if miss else ""))

print("\nRESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
