#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-01 14:00 批次线上校验：六语 title 渲染 + 线上 sitemap 是否含新 URL。"""
import subprocess, re, sys, time

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["phthalate-free-apparel-packaging.html", "garment-packaging-for-returns.html"]
LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
EXPECT = {
    "zh": "塑化|包裝|包装",
    "en": "Phthalate|Returns",
    "fr": "phtalates|Emballage",
    "es": "ftalatos|Embalaje",
    "ja": "フタル酸|返品",
    "ko": "프탈레이트|반품",
}

fails = []
for slug in SLUGS:
    for lang in LANGS:
        # 语言子目录直连（与站点 hreflang 一致），v=1 绕过边缘缓存
        if lang == "zh":
            url = "https://taigetag.com/blog/%s?lang=zh&v=191" % slug
        else:
            url = "https://taigetag.com/%s/blog/%s?lang=%s&v=191" % (lang, slug, lang)
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=9000", "--dump-dom", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        dom = r.stdout or ""
        m = re.search(r'<title[^>]*>(.*?)</title>', dom, re.S)
        title = m.group(1).strip() if m else "NONE"
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', dom, re.S)
        h1v = re.sub(r'<[^>]+>', '', h1.group(1)).strip()[:40] if h1 else "NONE"
        ok = bool(re.search(EXPECT[lang], title)) and title != "NONE"
        print("%-42s %-3s %-5s title=%s" % (slug, lang, "OK" if ok else "FAIL", title[:80]))
        print("      h1=%s" % h1v)
        if not ok:
            fails.append("%s %s title=%s" % (slug, lang, title))
        time.sleep(0.5)

sm = subprocess.run(["curl", "--noproxy", "*", "-s", "--max-time", "40",
                     "https://taigetag.com/sitemap.xml"], capture_output=True, text=True,
                    encoding="utf-8", errors="replace").stdout
print("\n线上 sitemap 长度 %d 字符" % len(sm))
for slug in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % slug] + \
             ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in ["en", "ja", "ko", "fr", "es"]]:
        ok = "<loc>%s</loc>" % u in sm
        print("  %-72s %s" % (u, "OK" if ok else "MISSING"))
        if not ok:
            fails.append("sitemap 缺 " + u)

print("\n线上失败项：%d" % len(fails))
for f in fails:
    print("  [X]", f)
sys.exit(1 if fails else 0)
