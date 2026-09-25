#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-24 晚间批次线上验证：
1) 无头 Chrome dump DOM → 校验 2 篇新文章 × 6 语言的 title / h1 渲染；
2) curl 线上 sitemap.xml → 确认 2 篇 × 6 语 URL 已上线。
"""
import os, re, subprocess, sys, time

sys.stdout.reconfigure(encoding='utf-8')
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
TMP = os.path.join(os.environ["LOCALAPPDATA"], "Temp")
os.chdir(TMP)

SLUGS = ["chinese-new-year-trims-order-planning.html", "clothing-label-compliance-uae.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
BASE = "https://taigetag.com"
V = "107"

EXPECT = {
    ("chinese-new-year-trims-order-planning.html", "zh"): "春節排產與輔料交期規劃",
    ("chinese-new-year-trims-order-planning.html", "en"): "Chinese New Year Trim Lead Times",
    ("chinese-new-year-trims-order-planning.html", "ja"): "春節と副資材の納期計画",
    ("chinese-new-year-trims-order-planning.html", "ko"): "춘절과 부자재 납기 계획",
    ("chinese-new-year-trims-order-planning.html", "fr"): "Nouvel An chinois et délais d'accessoires",
    ("chinese-new-year-trims-order-planning.html", "es"): "Año Nuevo chino y plazos de accesorios",
    ("clothing-label-compliance-uae.html", "zh"): "阿聯酋與海灣市場服裝標籤合規指南",
    ("clothing-label-compliance-uae.html", "en"): "UAE and Gulf Clothing Label Compliance",
    ("clothing-label-compliance-uae.html", "ja"): "UAE・湾岸市場の衣料ラベル適合ガイド",
    ("clothing-label-compliance-uae.html", "ko"): "UAE·걸프 시장 의류 라벨 컴플라이언스",
    ("clothing-label-compliance-uae.html", "fr"): "Étiquettes pour les Émirats et le Golfe",
    ("clothing-label-compliance-uae.html", "es"): "Etiquetas para Emiratos y el Golfo",
}


def url(slug, lang):
    return "%s/%sblog/%s?lang=%s&v=%s" % (BASE, "" if lang == "zh" else lang + "/", slug, lang, V)


print("== 1) 线上 DOM 渲染（无头 Chrome） ==")
bad = 0
for slug in SLUGS:
    for lang in LANGS:
        out = "dom_eve_20260924_%s_%s.html" % (lang, slug.replace(".html", ""))
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
        print("  %-42s %-3s 命中=%s  h2数=%d" % (slug, lang, "OK" if hit else "XX", len(h2s)))
        print("      title: %s" % title[:110])
        print("      h1   : %s" % h1v[:110])
        if not hit:
            bad += 1

print("== 2) 线上 sitemap.xml ==")
sp = os.path.join(TMP, "sitemap_eve_20260924.xml")
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

# 3) 语言切换跳转版本号（BUST_VERSION 已升到 107）
print("== 3) 线上 main.js BUST_VERSION ==")
mj = os.path.join(TMP, "main_eve_20260924.js")
subprocess.run(["curl", "-s", "--noproxy", "*", "-o", mj, "%s/js/main.js?cb=%d" % (BASE, int(time.time()))],
               timeout=120)
js = open(mj, encoding="utf-8", errors="replace").read()
m = re.search(r'var BUST_VERSION = "([^"]*)"', js)
print("  线上 BUST_VERSION = %s %s" % (m.group(1) if m else "?", "OK" if (m and m.group(1) == V) else "XX"))

print("\n结论: DOM 未命中 %d，sitemap 缺失 %d，BUST_VERSION=%s"
      % (bad, miss, m.group(1) if m else "?"))
sys.exit(1 if (bad or miss or not (m and m.group(1) == V)) else 0)
