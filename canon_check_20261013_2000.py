# -*- coding: utf-8 -*-
"""canonical 与 sitemap 一致性校验（针对本次 12 个新 URL + hreflang 互链完整性）"""
import os, re, sys

os.chdir("C:/Users/micro/taige-website")
SLUGS = ["apparel-relabeling-service-guide.html",
         "secondhand-resale-apparel-label-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
sm = open("sitemap.xml", encoding="utf-8").read()
fails = []

for slug in SLUGS:
    for l in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
        f = "%sblog/%s" % (l, slug)
        url = "https://taigetag.com/%sblog/%s" % (l, slug)
        s = open(f, encoding="utf-8").read()
        can = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        in_sm = ("<loc>%s</loc>" % url) in sm
        alt = re.findall(r'<link rel="alternate" hreflang="([^"]*)" href="([^"]*)"', s)
        alt_map = {a: b for a, b in alt}
        print("%-56s canonical=%-52s sitemap=%s hreflang=%d" % (f, can, "有" if in_sm else "无", len(alt)))
        if can != url:
            fails.append("canonical 与预期不符 %s -> %s" % (f, can))
        if not in_sm:
            fails.append("sitemap 缺 %s" % url)
        if len(alt) != 7:
            fails.append("%s hreflang 条数=%d（应为 7：zh-Hant/en/fr/es/ja/ko/x-default）" % (f, len(alt)))
        for code, href in alt:
            if code == "x-default":
                exp = "https://taigetag.com/blog/%s" % slug
            elif code == "zh-Hant":
                exp = "https://taigetag.com/blog/%s" % slug
            else:
                exp = "https://taigetag.com/%s/blog/%s" % (code, slug)
            if href != exp:
                fails.append("%s hreflang %s -> %s（应为 %s）" % (f, code, href, exp))

print()
print("canonical/hreflang 校验:", "全部一致" if not fails else "存在 %d 项问题" % len(fails))
for x in fails:
    print("  -", x)
sys.exit(0 if not fails else 1)
