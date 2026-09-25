#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-25 下午批次线上验证：
1) 无头 Chrome dump DOM → 校验 2 篇新文章 × 6 语言的 title / h1 渲染；
2) curl 线上 sitemap.xml → 确认 2 篇 × 6 语 URL 已上线；
3) 线上 main.js BUST_VERSION = 109。
"""
import os, re, subprocess, sys, time

sys.stdout.reconfigure(encoding='utf-8')
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
TMP = os.path.join(os.environ["LOCALAPPDATA"], "Temp")
os.chdir(TMP)

SLUGS = ["footwear-luggage-trims-guide.html", "trim-artwork-copyright-guide.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
BASE = "https://taigetag.com"
V = "109"

EXPECT = {
    ("footwear-luggage-trims-guide.html", "zh"): "鞋類與箱包輔料標籤指南",
    ("footwear-luggage-trims-guide.html", "en"): "Bag Trim Labels",
    ("footwear-luggage-trims-guide.html", "ja"): "靴・バッグ副資材ラベルガイド",
    ("footwear-luggage-trims-guide.html", "ko"): "신발·가방 부자재 라벨 가이드",
    ("footwear-luggage-trims-guide.html", "fr"): "accessoires pour chaussures et sacs",
    ("footwear-luggage-trims-guide.html", "es"): "accesorios para calzado y bolsos",
    ("trim-artwork-copyright-guide.html", "zh"): "吊牌與輔料印刷的版權與商標授權指南",
    ("trim-artwork-copyright-guide.html", "en"): "Copyright and Trademark Clearance",
    ("trim-artwork-copyright-guide.html", "ja"): "タグ・副資材印刷の著作権と商標ガイド",
    ("trim-artwork-copyright-guide.html", "ko"): "행택·부자재 인쇄의 저작권과 상표 가이드",
    ("trim-artwork-copyright-guide.html", "fr"): "marques pour",
    ("trim-artwork-copyright-guide.html", "es"): "Derechos de autor y marcas",
}


def url(slug, lang):
    return "%s/%sblog/%s?lang=%s&v=%s" % (BASE, "" if lang == "zh" else lang + "/", slug, lang, V)


print("== 1) 线上 DOM 渲染（无头 Chrome） ==")
bad = 0
for slug in SLUGS:
    for lang in LANGS:
        out = "dom_pm_20260925_%s_%s.html" % (lang, slug.replace(".html", ""))
        if os.path.exists(out):
            os.remove(out)
        with open(out, "w", encoding="utf-8") as fh:
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=15000", "--dump-dom", url(slug, lang)],
                           stdout=fh, stderr=subprocess.DEVNULL, timeout=120)
        s = open(out, encoding="utf-8", errors="replace").read()
        t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
        title = t.group(1).strip() if t else "-"
        h1v = re.sub(r"\s+", " ", h1.group(1)).strip() if h1 else "-"
        exp = EXPECT[(slug, lang)]
        hit = exp.lower() in (title + " " + h1v).lower()
        h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', s, re.S)
        print("  %-40s %-3s 命中=%s  h2数=%d" % (slug, lang, "OK" if hit else "XX", len(h2s)))
        print("      title: %s" % title[:110])
        print("      h1   : %s" % h1v[:110])
        if not hit:
            bad += 1

print("== 2) 线上 sitemap.xml ==")
sp = os.path.join(TMP, "sitemap_pm_20260925.xml")
subprocess.run(["curl", "-s", "--noproxy", "*", "-o", sp, "%s/sitemap.xml?cb=%d" % (BASE, int(time.time()))],
               timeout=120)
sm = open(sp, encoding="utf-8", errors="replace").read()
print("  线上 sitemap 行数 %d, <loc> 总数 %d" % (sm.count("\n"), sm.count("<loc>")))
miss = 0
for slug in SLUGS:
    for pre in ["blog/"] + ["%s/blog/" % l for l in ["en", "ja", "ko", "fr", "es"]]:
        u = "%s/%s%s" % (BASE, pre, slug)
        if "<loc>%s</loc>" % u not in sm:
            print("  XX 缺 %s" % u)
            miss += 1
print("  新 URL 缺失数 = %d" % miss)

print("== 3) 线上 main.js BUST_VERSION ==")
mj = os.path.join(TMP, "main_pm_20260925.js")
subprocess.run(["curl", "-s", "--noproxy", "*", "-o", mj, "%s/js/main.js?cb=%d" % (BASE, int(time.time()))],
               timeout=120)
js = open(mj, encoding="utf-8", errors="replace").read()
m = re.search(r'var BUST_VERSION = "([^"]*)"', js)
print("  线上 BUST_VERSION = %s %s" % (m.group(1) if m else "?", "OK" if (m and m.group(1) == V) else "XX"))

print("\n结论: DOM 未命中 %d，sitemap 缺失 %d，BUST_VERSION=%s"
      % (bad, miss, m.group(1) if m else "?"))
sys.exit(1 if (bad or miss or not (m and m.group(1) == V)) else 0)
