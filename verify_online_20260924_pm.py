#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-24 下午批次线上验证：
1) 无头 Chrome dump DOM → 校验 2 篇新文章 × 6 语言的 title / h1 渲染；
2) curl 线上 sitemap.xml → 确认 2 篇 × 6 语 URL 已上线。
"""
import os, re, subprocess, sys, time

sys.stdout.reconfigure(encoding='utf-8')
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
TMP = os.path.join(os.environ["LOCALAPPDATA"], "Temp")
os.chdir(TMP)

SLUGS = ["garment-packaging-transit-testing.html", "shirt-blouse-trims-guide.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
BASE = "https://taigetag.com"
V = "106"

EXPECT = {
    ("garment-packaging-transit-testing.html", "zh"): "服裝包裝運輸測試指南",
    ("garment-packaging-transit-testing.html", "en"): "Apparel Packaging Transit Testing",
    ("garment-packaging-transit-testing.html", "ja"): "衣料包装の輸送テストガイド",
    ("garment-packaging-transit-testing.html", "ko"): "의류 포장 운송 테스트 가이드",
    ("garment-packaging-transit-testing.html", "fr"): "tests de transport d'emballage",
    ("garment-packaging-transit-testing.html", "es"): "pruebas de transporte de embalaje",
    ("shirt-blouse-trims-guide.html", "zh"): "襯衫與女衫輔料指南",
    ("shirt-blouse-trims-guide.html", "en"): "Shirt and Blouse Trims Guide",
    ("shirt-blouse-trims-guide.html", "ja"): "シャツ・ブラウスの副資材ガイド",
    ("shirt-blouse-trims-guide.html", "ko"): "셔츠·블라우스 부자재 가이드",
    ("shirt-blouse-trims-guide.html", "fr"): "accessoires de chemise",
    ("shirt-blouse-trims-guide.html", "es"): "accesorios para camisa",
}


def url(slug, lang):
    return "%s/%sblog/%s?lang=%s&v=%s" % (BASE, "" if lang == "zh" else lang + "/", slug, lang, V)


print("== 1) 线上 DOM 渲染（无头 Chrome） ==")
bad = 0
for slug in SLUGS:
    for lang in LANGS:
        out = "dom_pm_20260924_%s_%s.html" % (lang, slug.replace(".html", ""))
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
sp = os.path.join(TMP, "sitemap_pm_20260924.xml")
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
