#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证：用无头 Chrome --dump-dom 抓取 12 个新页面各语言 title/h1/描述，确认线上渲染正确"""
import subprocess, re, os, sys, tempfile

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["hang-tag-folding-types.html", "retail-floor-ready-apparel-packaging.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
EXPECT = {
    "hang-tag-folding-types.html": {
        "zh": "吊牌摺頁形式怎麼選：對摺、風琴折、多頁與卡片組合",
        "en": "Folded Hang Tags: Bi-fold, Accordion, Multi-Panel and Card Formats",
        "ja": "タグの折り形式ガイド",
        "ko": "행택 접지 형태 가이드",
        "fr": "Étiquettes suspendues pliées",
        "es": "Etiquetas colgantes plegadas",
    },
    "retail-floor-ready-apparel-packaging.html": {
        "zh": "服裝上架就緒包裝指南",
        "en": "Floor-Ready Apparel Packaging",
        "ja": "上架準備済み（Floor-Ready）包装ガイド",
        "ko": "상장 준비(Floor-Ready) 포장 가이드",
        "fr": "Emballage prêt à la vente",
        "es": "Embalaje listo para exposición",
    },
}

fails = []
for slug in SLUGS:
    for lang in LANGS:
        url = "https://taigetag.com/%sblog/%s?lang=%s&v=1" % (lang + "/" if lang != "zh" else "", slug, lang)
        tmp = os.path.join(tempfile.gettempdir(), "dom_%s_%s.html" % (slug[:12], lang))
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=12000", "--dump-dom", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
        dom = r.stdout or ""
        t = re.search(r"<title[^>]*>(.*?)</title>", dom, re.S)
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S)
        d = re.search(r'<meta name="description"[^>]*content="([^"]*)"', dom, re.S)
        title = (t.group(1).strip() if t else "NO-TITLE")
        h1v = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else "NO-H1"
        exp = EXPECT[slug][lang]
        good_t = exp in title
        good_h = exp[:12] in h1v or (lang == "zh" and "折" in h1v) or (lang != "zh" and exp.split(":")[0][:10] in h1v)
        print("%-4s %-42s title=%-8s h1=%-8s desc=%d字 | %s" %
              (lang, slug[:42], "OK" if good_t else "×", "OK" if good_h else "×",
               len(d.group(1)) if d else 0, title[:70]))
        if not good_t:
            fails.append((url, "title", title))
        if not good_h:
            fails.append((url, "h1", h1v))
        if not d or len(d.group(1)) < 40:
            fails.append((url, "desc", d.group(1) if d else "NONE"))

print("\n失败项：%d" % len(fails))
for f in fails:
    print("  -", f)
