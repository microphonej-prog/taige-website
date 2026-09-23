#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-23 上午批次线上验证：
1) 无头 Chrome dump DOM → 校验 2 篇新文章 × 6 语言的 title / h1 渲染；
2) curl 线上 sitemap.xml → 确认 2 篇 × 6 语 URL 已上线。
"""
import os, re, subprocess, sys, time

sys.stdout.reconfigure(encoding='utf-8')
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
TMP = os.path.join(os.environ["LOCALAPPDATA"], "Temp")
os.chdir(TMP)

SLUGS = ["paper-bag-window-guide.html", "trims-kitting-guide.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
BASE = "https://taigetag.com"

EXPECT = {
    ("paper-bag-window-guide.html", "zh"): "紙袋開窗工藝指南",
    ("paper-bag-window-guide.html", "en"): "Paper Bag Window Guide",
    ("paper-bag-window-guide.html", "ja"): "紙袋の窓加工ガイド",
    ("paper-bag-window-guide.html", "ko"): "종이백 창 가공 가이드",
    ("paper-bag-window-guide.html", "fr"): "fenêtre sur sac papier",
    ("paper-bag-window-guide.html", "es"): "ventana en bolsas de papel",
    ("trims-kitting-guide.html", "zh"): "服裝輔料齊套配送指南",
    ("trims-kitting-guide.html", "en"): "Trim Kitting Guide",
    ("trims-kitting-guide.html", "ja"): "キッティングガイド",
    ("trims-kitting-guide.html", "ko"): "키팅 가이드",
    ("trims-kitting-guide.html", "fr"): "kitting d'accessoires",
    ("trims-kitting-guide.html", "es"): "kitting de accesorios",
}

def url(slug, lang):
    return "%s/%sblog/%s?lang=%s&v=102" % (BASE, "" if lang == "zh" else lang + "/", slug, lang)

print("== 1) 线上 DOM 渲染（无头 Chrome） ==")
bad = 0
for slug in SLUGS:
    for lang in LANGS:
        out = "dom_20260923_%s_%s.html" % (lang, slug.replace(".html", ""))
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
        cjk = len(re.findall(r"[\u4e00-\u9fff]", s[s.find('class="article-body"'):]))
        print("  %-30s %-3s 命中=%s  正文字符=%d" % (slug, lang, "✓" if hit else "✗", cjk))
        print("      title: %s" % title[:100])
        print("      h1   : %s" % h1v[:100])
        if not hit:
            bad += 1

print("== 2) 线上 sitemap.xml ==")
sp = os.path.join(TMP, "sitemap_20260923.xml")
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
