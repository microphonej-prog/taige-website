#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-13 第三批线上验证：12 页 HTTP 状态 + 无头 Chrome DOM 标题/h1/描述 + 线上 sitemap 12 URL
+ 线上列表页首两卡。期望值直接从本地生成文件读取，避免手写转写错误。"""
import subprocess, re, os, ssl, sys, urllib.request, urllib.error

os.chdir("C:/Users/micro/taige-website")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["neckwear-trims-label-guide.html", "belts-suspenders-trims-guide.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
TODAY = "2026-10-13"
ctx = ssl.create_default_context()
fails = []


def local_path(slug, lang):
    return "blog/%s" % slug if lang == "zh" else "%s/blog/%s" % (lang, slug)


def expected(slug, lang):
    s = open(local_path(slug, lang), encoding="utf-8").read()
    t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1).strip()
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S).group(1).strip()
    d = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s, re.S).group(1).strip()
    return t, re.sub(r"<[^>]+>", "", h1).strip(), d


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        r = urllib.request.urlopen(req, timeout=45, context=ctx)
        return r.getcode(), r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return "ERR(%s)" % e, ""


print("========== 1) 预热 CDN + HTTP 状态（12 页） ==========")
for slug in SLUGS:
    for lang in LANGS:
        u = "https://taigetag.com/%sblog/%s?v=157" % (lang + "/" if lang != "zh" else "", slug)
        code, _ = fetch(u)
        print("  %-3s %-38s -> %s" % (lang, slug, code))
        if code != 200:
            fails.append("%s HTTP %s" % (u, code))

print("\n========== 2) 无头 Chrome DOM 渲染（12 页） ==========")
for slug in SLUGS:
    for lang in LANGS:
        texp, hexp, dexp = expected(slug, lang)
        url = "https://taigetag.com/%sblog/%s?lang=%s&v=157" % (lang + "/" if lang != "zh" else "", slug, lang)
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=12000", "--dump-dom", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
        dom = r.stdout or ""
        t = re.search(r"<title[^>]*>(.*?)</title>", dom, re.S)
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S)
        d = re.search(r'<meta name="description"[^>]*content="([^"]*)"', dom, re.S)
        title = (t.group(1).strip() if t else "NO-TITLE")
        h1v = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else "NO-H1"
        dl = len(d.group(1)) if d else 0
        gt = texp in title
        gh = hexp in h1v
        gd = dl > 40
        print("%-3s %-38s title=%s h1=%s desc=%d字 | %s" % (lang, slug[:38], "OK" if gt else "X",
                                                            "OK" if gh else "X", dl, title[:56]))
        if not gt:
            fails.append("DOM title %s -> %s（期望含 %s）" % (url, title[:60], texp[:40]))
        if not gh:
            fails.append("DOM h1 %s -> %s（期望含 %s）" % (url, h1v[:60], hexp[:40]))
        if not gd:
            fails.append("DOM desc %s 长度 %d" % (url, dl))

print("\n========== 3) 线上 sitemap（12 新 URL） ==========")
code, sm = fetch("https://taigetag.com/sitemap.xml?v=157")
print("  线上 sitemap HTTP %s，长度 %d" % (code, len(sm)))
if code != 200:
    fails.append("线上 sitemap HTTP %s" % code)
found = 0
for slug in SLUGS:
    for lang in LANGS:
        u = "https://taigetag.com/%sblog/%s" % (lang + "/" if lang != "zh" else "", slug)
        m = re.search(r"<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
        if not m:
            fails.append("线上 sitemap 缺 %s" % u)
        elif m.group(1) != TODAY:
            fails.append("线上 sitemap lastmod %s = %s" % (u, m.group(1)))
        else:
            found += 1
print("  12 个新 URL 全部存在且 lastmod=%s：%d/12" % (TODAY, found))

print("\n========== 4) 线上列表页首两卡（六语） ==========")
for lang in LANGS:
    u = "https://taigetag.com/%sblog/index.html?v=157" % (lang + "/" if lang != "zh" else "")
    code, li = fetch(u)
    g = li.find('<div class="post-grid">')
    cards = re.findall(r'<a class="more" href="([^"]+)"', li[g:], re.S)[:2] if g >= 0 else []
    ok = cards == SLUGS
    print("  %s %-3s 首卡=%s" % ("OK" if ok else "X ", lang, cards))
    if not ok:
        fails.append("线上列表页 %s 首卡 = %s" % (lang, cards))

print("\n失败项：%d" % len(fails))
for f in fails:
    print("  -", f)
sys.exit(1 if fails else 0)
