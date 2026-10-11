#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证 2026-10-11 上午批次：无头 Chrome 六语 DOM title + 线上 sitemap 新 URL + 列表页首卡。"""
import os, re, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
from daily_meta_20261011_0800 import ARTICLES

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
LANGS = [("zh-Hant", ""), ("en", "en/"), ("ja", "ja/"), ("ko", "ko/"), ("fr", "fr/"), ("es", "es/")]
# 简体期望值 → 繁体（根目录中文版由 to_traditional 转繁），仅用于比对
import importlib.util
_spec = importlib.util.spec_from_file_location("to_traditional", os.path.join(ROOT, "to_traditional.py"))
_tm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_tm)


def _s2t(x):
    return _tm.convert_html('<p>%s</p>' % x).replace("<p>", "").replace("</p>", "").strip()

# 每语期望 title 前缀（取 meta 里的 title 值去掉品牌后片段）
EXPECT = {
    "zh-Hant": dict(zip([a["slug"] for a in ARTICLES], [a["title_zh"] for a in ARTICLES])),
    "en": dict(zip([a["slug"] for a in ARTICLES], [a["title_en"] for a in ARTICLES])),
    "ja": dict(zip([a["slug"] for a in ARTICLES], [a["title_ja"] for a in ARTICLES])),
    "ko": dict(zip([a["slug"] for a in ARTICLES], [a["title_ko"] for a in ARTICLES])),
    "fr": dict(zip([a["slug"] for a in ARTICLES], [a["title_fr"] for a in ARTICLES])),
    "es": dict(zip([a["slug"] for a in ARTICLES], [a["title_es"] for a in ARTICLES])),
}

print("== 1) 线上 sitemap 新 URL ==")
subprocess.run(["curl", "-s", "-m", "60", "--noproxy", "*", "-o", "online_sitemap.xml",
                "https://taigetag.com/sitemap.xml"], check=True)
sm = open("online_sitemap.xml", encoding="utf-8").read()
fails = 0
for a in ARTICLES:
    slug = a["slug"]
    for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
        u = "https://taigetag.com/%s%s" % (pre, slug)
        ok = "<loc>%s</loc>" % u in sm
        if not ok:
            fails += 1
        print("  %s %s" % ("OK " if ok else "!! ", u))
print("  线上 <loc> 总数=%d" % sm.count("<loc>"))

print("== 2) 无头 Chrome 六语 DOM title ==")
for lang, pre in LANGS:
    for a in ARTICLES:
        url = "https://taigetag.com/%sblog/%s?v=149" % (pre, a["slug"])
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=12000", "--dump-dom", url],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=90)
        dom = r.stdout or ""
        m = re.search(r"<title[^>]*>(.*?)</title>", dom, re.S)
        title = (m.group(1).strip() if m else "")
        exp = EXPECT[lang][a["slug"]].replace("&amp;", "&")
        if lang == "zh-Hant":
            exp = _s2t(exp)
        core = exp.split("|")[0].strip()[:28]
        ok = core and core in title
        if not ok:
            fails += 1
        print("  %-38s %-52s %s" % ("%s %s" % (lang, a["slug"][:30]), title[:50], "OK" if ok else "!! 期望含 %s" % core))

print("== 3) 线上列表页首卡 ==")
for pre in ("", "en/", "ja/", "ko/", "fr/", "es/"):
    p = "online_idx_%s.html" % (pre.replace("/", "") or "zh")
    subprocess.run(["curl", "-s", "-m", "60", "--noproxy", "*", "-o", p,
                    "https://taigetag.com/%sblog/index.html?v=149" % pre], check=True)
    s = open(p, encoding="utf-8").read()
    hit = [a["slug"] for a in ARTICLES if a["slug"] in s]
    print("  %-24s 新卡片命中=%d %s" % ("%sblog/index.html" % pre, len(hit), hit))
    if len(hit) != 2:
        fails += 1

print("\n线上验证失败项 = %d" % fails)
raise SystemExit(1 if fails else 0)
