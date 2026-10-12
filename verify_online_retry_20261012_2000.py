#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证重试（2026-10-12 晚间批次）：
- 首轮部分 URL 返回 GitHub Pages 404（CDN 边缘尚未切换完成），本脚本重试全部 12 页
- h1 期望单独给（h1 与 title 在中日韩语上写法略有差异）
- 同时打印 HTTP 状态码，区分「真 404」与「渲染异常」
"""
import subprocess, re, os, tempfile, urllib.request, urllib.error, ssl, time

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["dresses-skirts-trims-guide.html", "dancewear-stage-costume-trims-guide.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
EXPECT = {
    "dresses-skirts-trims-guide.html": {
        "zh": ("連衣裙與半身裙輔料與標籤指南", "連衣裙與半身裙輔料與標籤指南"),
        "en": ("Dress and Skirt Trims Guide", "Dress and Skirt Trims Guide"),
        "ja": ("ワンピース・スカートの副資材とラベルガイド", "ワンピースとスカートの副資材"),
        "ko": ("원피스·스커트 부자재와 라벨 가이드", "원피스와 스커트 부자재"),
        "fr": ("Guide des accessoires de robe et de jupe", "Guide des accessoires de robe et de jupe"),
        "es": ("Guía de accesorios de vestido y falda", "Guía de accesorios de vestido y falda"),
    },
    "dancewear-stage-costume-trims-guide.html": {
        "zh": ("舞蹈服與演出服輔料指南", "舞蹈服與演出服輔料指南"),
        "en": ("Dancewear and Stage Costume Trims Guide", "Dancewear and Stage Costume Trims Guide"),
        "ja": ("ダンスウェア・ステージ衣装の副資材ガイド", "ダンスウェアとステージ衣装の副資材"),
        "ko": ("댄스웨어·무대 의상 부자재 가이드", "댄스웨어와 무대 의상 부자재"),
        "fr": ("Guide des accessoires de danse et de costume", "Guide des accessoires de danse et de costume"),
        "es": ("Guía de accesorios de danza y vestuario", "Guía de accesorios de danza y vestuario"),
    },
}
ctx = ssl.create_default_context()
fails = []


def status(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        r = urllib.request.urlopen(req, timeout=45, context=ctx)
        return r.getcode(), len(r.read())
    except urllib.error.HTTPError as e:
        return e.code, 0
    except Exception as e:
        return "ERR", str(e)


print("========== HTTP 状态（urllib 直连） ==========")
for slug in SLUGS:
    for lang in LANGS:
        u = "https://taigetag.com/%sblog/%s?v=1" % (lang + "/" if lang != "zh" else "", slug)
        code, size = status(u)
        print("  %-4s %-40s -> %s (%s)" % (lang, slug, code, size))
        if code != 200:
            fails.append((u, "http", code))

print("\n========== 无头 Chrome 渲染（12 页） ==========")
for slug in SLUGS:
    for lang in LANGS:
        url = "https://taigetag.com/%sblog/%s?lang=%s&v=1" % (lang + "/" if lang != "zh" else "", slug, lang)
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=12000", "--dump-dom", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
        dom = r.stdout or ""
        t = re.search(r"<title[^>]*>(.*?)</title>", dom, re.S)
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S)
        d = re.search(r'<meta name="description"[^>]*content="([^"]*)"', dom, re.S)
        title = (t.group(1).strip() if t else "NO-TITLE")
        h1v = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else "NO-H1"
        texp, hexp = EXPECT[slug][lang]
        gt, gh = texp in title, hexp in h1v
        print("%-4s %-36s title=%-3s h1=%-3s desc=%3d字 | %s | %s" %
              (lang, slug[:36], "OK" if gt else "X", "OK" if gh else "X",
               len(d.group(1)) if d else 0, title[:58], h1v[:40]))
        if not gt:
            fails.append((url, "title", title))
        if not gh:
            fails.append((url, "h1", h1v))
        if not d or len(d.group(1)) < 40:
            fails.append((url, "desc", d.group(1) if d else "NONE"))

print("\n========== 线上 blog/index.html 首卡（六语） ==========")
for lang in LANGS:
    u = "https://taigetag.com/%sblog/index.html?v=1" % (lang + "/" if lang != "zh" else "")
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        li = urllib.request.urlopen(req, timeout=45, context=ctx).read().decode("utf-8", "replace")
    except Exception as e:
        fails.append((u, "fetch", str(e)))
        print("  X  %s %s" % (lang, e))
        continue
    g = li.find('<div class="post-grid">')
    cards = re.findall(r'<a class="more" href="([^"]+)"', li[g:], re.S)[:2]
    print("  %s %s 首卡=%s" % ("OK" if cards == SLUGS else "X ", lang, cards))
    if cards != SLUGS:
        fails.append((u, "first cards", cards))

print("\n失败项：%d" % len(fails))
for f in fails:
    print("  -", f)
