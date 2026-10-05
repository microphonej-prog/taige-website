#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-05 晚间批次线上验证：
1) 六语页面（zh-Hant 根 / en / ja / ko / fr / es）无头 Chrome 渲染标题
2) 线上 sitemap.xml 含 12 个新 URL，blog 列表页 lastmod = 2026-10-05
3) blog 列表页（六语）含 2 张新卡片
用法: F:/hermes/venvs/tools/Scripts/python.exe verify_online_20261005_2000.py
注意：写临时文件必须用原生路径（F:/... 或 C:/...），/tmp 会被原生 curl 解析成 C:\\tmp 造成旧文件误判。
"""
import subprocess, re, sys, os

SCRATCH = "F:/hermes/cache/scratch"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["reach-svhc-apparel-trims-guide", "braille-tactile-label-guide"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
EXPECT = {
    "reach-svhc-apparel-trims-guide": {
        "zh": "REACH SVHC 與服裝輔料合規指南", "en": "REACH SVHC for Apparel Trims",
        "ja": "衣料副資材の REACH SVHC 対応ガイド", "ko": "의류 부자재 REACH SVHC 가이드",
        "fr": "REACH SVHC et accessoires textiles", "es": "REACH SVHC en accesorios textiles"},
    "braille-tactile-label-guide": {
        "zh": "服裝標籤的盲文與觸覺標識指南", "en": "Braille and Tactile Labels on Garment Tags",
        "ja": "衣料タグの点字・触覚表示ガイド", "ko": "의류 태그의 점자·촉각 표시 가이드",
        "fr": "Étiquettes en braille et repères tactiles", "es": "Etiquetas en braille y marcas táctiles"},
}
fails = []

os.makedirs(SCRATCH, exist_ok=True)
print("== 1) 线上六语 DOM 标题 ==")
for slug in SLUGS:
    for L in LANGS:
        f = os.path.join(SCRATCH, "v3_%s_%s.html" % (slug, L))
        with open(f, "wb") as fh:
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=12000", "--dump-dom",
                            "https://taigetag.com/blog/%s.html?lang=%s&v=1" % (slug, L)],
                           stdout=fh, stderr=subprocess.DEVNULL, timeout=90)
        s = open(f, encoding="utf-8", errors="replace").read()
        m = re.search(r'<title[^>]*>([^<]*)</title>', s)
        title = m.group(1) if m else ""
        ok = EXPECT[slug][L] in title
        if not ok:
            fails.append("%s [%s] 标题不符: %s" % (slug, L, title))
        print("  %-34s %-3s %s  %s" % (slug, L, "OK " if ok else "✗  ", title[:62]))

print("== 2) 线上 sitemap.xml 与 lastmod ==")
sm_path = os.path.join(SCRATCH, "v3_sitemap.xml")
subprocess.run(["curl", "-sS", "-o", sm_path, "--max-time", "60",
                "https://taigetag.com/sitemap.xml?cb=%d" % os.getpid()], check=True)
sm = open(sm_path, encoding="utf-8", errors="replace").read()
print("  线上 <loc> 总数 = %d" % sm.count("<loc>"))
for slug in SLUGS:
    for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
        u = "https://taigetag.com/%s%s.html" % (pre, slug)
        if "<loc>%s</loc>" % u not in sm:
            fails.append("sitemap 缺 %s" % u)
print("  12 个新 URL 检查完毕")
for u in ["https://taigetag.com/blog/index.html"] + \
         ["https://taigetag.com/%s/blog/index.html" % l for l in ("en", "ja", "ko", "fr", "es")]:
    blk = re.search(r'<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    print("    %-46s lastmod=%s" % (u, blk.group(1) if blk else "缺失"))
    if not blk or blk.group(1) != "2026-10-05":
        fails.append("%s lastmod 非 2026-10-05" % u)

print("== 3) 线上列表页卡片 ==")
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in ("en", "ja", "ko", "fr", "es")]:
    f = os.path.join(SCRATCH, "v3_idx_" + p.replace("/", "_"))
    subprocess.run(["curl", "-sS", "-o", f, "--max-time", "45",
                    "https://taigetag.com/%s?cb=%d" % (p, os.getpid())], check=True)
    s = open(f, encoding="utf-8", errors="replace").read()
    hit = [x for x in SLUGS if x in s]
    print("  %-26s 命中 %d/2 %s" % (p, len(hit), hit))
    if len(hit) != 2:
        fails.append("%s 新卡片缺失" % p)

print()
if fails:
    print("失败 %d 项：" % len(fails))
    for x in fails:
        print("  -", x)
    sys.exit(1)
print("线上验证全部通过。")
