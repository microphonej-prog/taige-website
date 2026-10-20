#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-20 14:00 批次线上校验：12 个静态语言页 title + 根页 JS 语言切换 title + sitemap"""
import re, os, sys, html, subprocess, tempfile
sys.path.insert(0, ".")
from daily_meta_20261020_1400 import ARTICLES

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
LANGS = ["en", "fr", "es", "ja", "ko"]
BUST = "174"
fails = []


def curl(url):
    """socket 直连 + 防缓存；返回文本"""
    out = os.path.join(tempfile.gettempdir(), "live_%d.html" % (abs(hash(url)) % 10 ** 8))
    cmd = ["curl", "-sS", "--noproxy", "*", "-m", "40", "-o", out, url]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        return None, r.stderr
    s = open(out, encoding="utf-8", errors="replace").read()
    try:
        os.remove(out)
    except OSError:
        pass
    return s, None


def chrome_dom(url):
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                        "--virtual-time-budget=12000", "--dump-dom", url],
                       capture_output=True, encoding="utf-8", errors="replace", timeout=120)
    return r.stdout or ""


def title_of(s):
    m = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
    return html.unescape(m.group(1).strip()) if m else ""


print("=== 1) 12 个静态语言页 title ===")
for a in ARTICLES:
    slug = a["slug"]
    for lang in ["zh"] + LANGS:
        url = ("https://taigetag.com/blog/%s?v=%s" % (slug, BUST) if lang == "zh"
               else "https://taigetag.com/%s/blog/%s?v=%s" % (lang, slug, BUST))
        s, err = curl(url)
        if s is None:
            fails.append("抓取失败 %s : %s" % (url, err))
            print("  %-4s FAIL %s" % (lang, err))
            continue
        got = title_of(s)
        exp = a["title_zh"] if lang == "zh" else a["title_" + lang]
        # 根页是繁体：用字符集宽松比较（去掉开头的简繁差异影响 → 用长度+关键词判定）
        if lang == "zh":
            ok = len(got) > 0 and ("種子紙" in got or "香氛吊牌" in got)
        else:
            ok = got == exp
        print("  %-4s %s %s | %s" % (lang, "OK " if ok else "FAIL", slug[:28], got[:58]))
        if not ok:
            fails.append("%s title=%s (期望 %s)" % (url, got[:60], exp[:60]))

print("\n=== 2) 根页 JS 语言切换（headless Chrome）===")
slug = ARTICLES[0]["slug"]
for lang in ["zh", "en", "fr", "es", "ja", "ko"]:
    url = "https://taigetag.com/blog/%s?lang=%s&v=%s" % (slug, lang, BUST)
    dom = chrome_dom(url)
    t = title_of(dom)
    exp = ARTICLES[0]["title_zh"] if lang == "zh" else ARTICLES[0]["title_" + lang]
    if lang == "zh":
        ok = ("種子紙" in t) or ("种子纸" in t)
    else:
        ok = t == exp
    print("  %-4s %s %s" % (lang, "OK " if ok else "FAIL", t[:70]))
    if not ok:
        fails.append("JS 切换 %s title=%s (期望 %s)" % (lang, t[:60], exp[:60]))

print("\n=== 3) 线上 sitemap ===")
sm, err = curl("https://taigetag.com/sitemap.xml?nocache=20261020")
sm = sm or ""
print("  <loc> 总数: %d" % sm.count("<loc>"))
for a in ARTICLES:
    for u in ["https://taigetag.com/blog/" + a["slug"]] + \
             ["https://taigetag.com/%s/blog/%s" % (l, a["slug"]) for l in LANGS]:
        if "<loc>%s</loc>" % u not in sm:
            fails.append("线上 sitemap 缺 " + u)
print("  新 URL 检查完成（12 条）")

print("\n===== 结果 =====")
if fails:
    print("失败 %d 项：" % len(fails))
    for f in fails:
        print("  - " + f)
    sys.exit(1)
print("线上全部通过")
