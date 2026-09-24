#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-24 早间批次线上验证：
1) 无头 Chrome dump DOM → 校验 2 篇新文章 × 6 语言的 title / h1 渲染；
2) curl 线上 sitemap.xml → 确认 2 篇 × 6 语 URL 已上线。
"""
import os, re, subprocess, sys, time

sys.stdout.reconfigure(encoding='utf-8')
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
TMP = os.path.join(os.environ["LOCALAPPDATA"], "Temp")
os.chdir(TMP)

SLUGS = ["bridal-eveningwear-trims-guide.html", "clothing-label-compliance-switzerland.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
BASE = "https://taigetag.com"
V = "105"

EXPECT = {
    ("bridal-eveningwear-trims-guide.html", "zh"): "婚紗與晚禮服輔料指南",
    ("bridal-eveningwear-trims-guide.html", "en"): "Bridal and Eveningwear Trims Guide",
    ("bridal-eveningwear-trims-guide.html", "ja"): "ウェディング・イブニングドレスの副資材ガイド",
    ("bridal-eveningwear-trims-guide.html", "ko"): "웨딩·이브닝웨어 부자재 가이드",
    ("bridal-eveningwear-trims-guide.html", "fr"): "accessoires de mariée et de soirée",
    ("bridal-eveningwear-trims-guide.html", "es"): "accesorios nupciales y de fiesta",
    ("clothing-label-compliance-switzerland.html", "zh"): "瑞士服裝標籤合規指南",
    ("clothing-label-compliance-switzerland.html", "en"): "Switzerland Clothing Label Requirements",
    ("clothing-label-compliance-switzerland.html", "ja"): "スイスの衣料ラベル要件",
    ("clothing-label-compliance-switzerland.html", "ko"): "스위스 의류 라벨 요건",
    ("clothing-label-compliance-switzerland.html", "fr"): "Étiquetage des vêtements en Suisse",
    ("clothing-label-compliance-switzerland.html", "es"): "Etiquetado de ropa en Suiza",
}


def url(slug, lang):
    return "%s/%sblog/%s?lang=%s&v=%s" % (BASE, "" if lang == "zh" else lang + "/", slug, lang, V)


print("== 1) 线上 DOM 渲染（无头 Chrome） ==")
bad = 0
for slug in SLUGS:
    for lang in LANGS:
        out = "dom_am_20260924_%s_%s.html" % (lang, slug.replace(".html", ""))
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
        print("  %-40s %-3s 命中=%s  h2数=%d" % (slug, lang, "✓" if hit else "✗", len(h2s)))
        print("      title: %s" % title[:110])
        print("      h1   : %s" % h1v[:110])
        if not hit:
            bad += 1

print("== 2) 线上 sitemap.xml ==")
sp = os.path.join(TMP, "sitemap_am_20260924.xml")
subprocess.run(["curl", "-s", "--noproxy", "*", "-o", sp, "%s/sitemap.xml?cb=%d" % (BASE, int(time.time()))],
               timeout=120)
sm = open(sp, encoding="utf-8", errors="replace").read()
print("  线上 sitemap 行数 %d, <loc> 总数 %d" % (sm.count("\n"), sm.count("<loc>")))
miss = 0
for slug in SLUGS:
    for pre in ["blog/"] + ["%s/blog/" % l for l in ["en", "ja", "ko", "fr", "es"]]:
        u = "%s/%s%s" % (BASE, pre, slug)
        if "<loc>%s</loc>" % u not in sm:
            print("  ✗ 缺 %s" % u); miss += 1
print("  新 URL 缺失数 = %d" % miss)

print("\n结论: DOM 未命中 %d，sitemap 缺失 %d" % (bad, miss))
sys.exit(1 if (bad or miss) else 0)
