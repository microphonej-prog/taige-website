#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证（2026-10-12 晚间批次）：
1) 无头 Chrome --dump-dom 抓取 12 个新页面（2 篇 × 6 语）确认 title/h1/description 渲染正确
2) 线上 sitemap.xml 确认含 12 个新 URL 与 lastmod=2026-10-12
3) 线上 js/main.js 的 BUST_VERSION 应为 154
4) 线上 blog/index.html（六语）首张卡片即本次新文章
"""
import subprocess, re, os, sys, tempfile, urllib.request, ssl

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["dresses-skirts-trims-guide.html", "dancewear-stage-costume-trims-guide.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
EXPECT = {
    "dresses-skirts-trims-guide.html": {
        "zh": "連衣裙與半身裙輔料與標籤指南",
        "en": "Dress and Skirt Trims Guide",
        "ja": "ワンピース・スカートの副資材とラベルガイド",
        "ko": "원피스·스커트 부자재와 라벨 가이드",
        "fr": "Guide des accessoires de robe et de jupe",
        "es": "Guía de accesorios de vestido y falda",
    },
    "dancewear-stage-costume-trims-guide.html": {
        "zh": "舞蹈服與演出服輔料指南",
        "en": "Dancewear and Stage Costume Trims Guide",
        "ja": "ダンスウェア・ステージ衣装の副資材ガイド",
        "ko": "댄스웨어·무대 의상 부자재 가이드",
        "fr": "Guide des accessoires de danse et de costume",
        "es": "Guía de accesorios de danza y vestuario",
    },
}

fails = []
print("========== 1) 线上 DOM 标题/描述 12 页 ==========")
for slug in SLUGS:
    for lang in LANGS:
        url = "https://taigetag.com/%sblog/%s?lang=%s&v=1" % (lang + "/" if lang != "zh" else "", slug, lang)
        tmp = os.path.join(tempfile.gettempdir(), "dom_%s_%s.html" % (slug[:10], lang))
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=12000", "--dump-dom", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
        dom = r.stdout or ""
        if not dom:
            dom = open(tmp, encoding="utf-8", errors="replace").read() if os.path.exists(tmp) else ""
        t = re.search(r"<title[^>]*>(.*?)</title>", dom, re.S)
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S)
        d = re.search(r'<meta name="description"[^>]*content="([^"]*)"', dom, re.S)
        title = (t.group(1).strip() if t else "NO-TITLE")
        h1v = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else "NO-H1"
        exp = EXPECT[slug][lang]
        good_t = exp in title
        good_h = exp[:10] in h1v
        print("%-4s %-34s title=%-3s h1=%-3s desc=%3d字 | %s" %
              (lang, slug[:34], "OK" if good_t else "X", "OK" if good_h else "X",
               len(d.group(1)) if d else 0, title[:70]))
        if not good_t:
            fails.append((url, "title", title))
        if not good_h:
            fails.append((url, "h1", h1v))
        if not d or len(d.group(1)) < 40:
            fails.append((url, "desc", d.group(1) if d else "NONE"))

print("\n========== 2) 线上 sitemap.xml ==========")
ctx = ssl.create_default_context()
try:
    req = urllib.request.Request("https://taigetag.com/sitemap.xml?v=1", headers={"User-Agent": "Mozilla/5.0"})
    live = urllib.request.urlopen(req, timeout=45, context=ctx).read().decode("utf-8", "replace")
except Exception as e:
    live = ""
    fails.append(("sitemap", "fetch", str(e)))
if live:
    print("线上 sitemap 长度 %d 字符" % len(live))
    for slug in SLUGS:
        for u in ["https://taigetag.com/blog/%s" % slug] + \
                 ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in ["en", "ja", "ko", "fr", "es"]]:
            okk = "<loc>%s</loc>" % u in live
            lm = re.search(r'<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), live)
            print("  %s %s  lastmod=%s" % ("OK" if okk else "X ", u, lm.group(1) if lm else "?"))
            if not okk:
                fails.append(("sitemap", "missing", u))
            elif not lm or lm.group(1) != "2026-10-12":
                fails.append(("sitemap", "lastmod", u))
    m = re.search(r'<loc>https://taigetag\.com/blog/index\.html</loc>\s*<lastmod>([^<]*)</lastmod>', live)
    print("  blog/index.html lastmod =", m.group(1) if m else "?")
    if not m or m.group(1) != "2026-10-12":
        fails.append(("sitemap", "blog index lastmod", m.group(1) if m else "?"))
else:
    print("线上 sitemap 抓取失败")

print("\n========== 3) 线上 js/main.js BUST_VERSION ==========")
try:
    req = urllib.request.Request("https://taigetag.com/js/main.js?v=1", headers={"User-Agent": "Mozilla/5.0"})
    mj = urllib.request.urlopen(req, timeout=45, context=ctx).read().decode("utf-8", "replace")
    m = re.search(r'BUST_VERSION\s*=\s*"([^"]*)"', mj)
    print("线上 BUST_VERSION =", m.group(1) if m else "未找到")
    if not m or m.group(1) != "154":
        fails.append(("main.js", "BUST_VERSION", m.group(1) if m else "?"))
except Exception as e:
    fails.append(("main.js", "fetch", str(e)))
    print("main.js 抓取失败：", e)

print("\n========== 4) 线上 blog/index.html 首卡（六语） ==========")
for lang in LANGS:
    u = "https://taigetag.com/%sblog/index.html?v=1" % (lang + "/" if lang != "zh" else "")
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        li = urllib.request.urlopen(req, timeout=45, context=ctx).read().decode("utf-8", "replace")
    except Exception as e:
        fails.append((u, "fetch", str(e)))
        print("  X  %s 抓取失败 %s" % (lang, e))
        continue
    g = li.find('<div class="post-grid">')
    cards = re.findall(r'<a class="more" href="([^"]+)"', li[g:], re.S)[:2]
    okk = cards == SLUGS
    print("  %s %s 首卡=%s" % ("OK" if okk else "X ", lang, cards))
    if not okk:
        fails.append((u, "first cards", cards))

print("\n失败项：%d" % len(fails))
for f in fails:
    print("  -", f)
