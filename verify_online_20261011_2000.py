#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证 2026-10-11 晚间批次：无头 Chrome 六语 DOM title + 线上 sitemap 新 URL + 六语列表页首卡。"""
import os, re, subprocess, sys, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
from daily_meta_20261011_2000 import ARTICLES

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SCRATCH = "F:/hermes/cache/scratch"
LANGS = [("zh-Hant", ""), ("en", "en/"), ("ja", "ja/"), ("ko", "ko/"), ("fr", "fr/"), ("es", "es/")]

_spec = importlib.util.spec_from_file_location("to_traditional", os.path.join(ROOT, "to_traditional.py"))
_tm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_tm)


def _s2t(x):
    return _tm.convert_html('<p>%s</p>' % x).replace("<p>", "").replace("</p>", "").strip()


EXPECT = {
    "zh-Hant": dict(zip([a["slug"] for a in ARTICLES], [a["title_zh"] for a in ARTICLES])),
    "en": dict(zip([a["slug"] for a in ARTICLES], [a["title_en"] for a in ARTICLES])),
    "ja": dict(zip([a["slug"] for a in ARTICLES], [a["title_ja"] for a in ARTICLES])),
    "ko": dict(zip([a["slug"] for a in ARTICLES], [a["title_ko"] for a in ARTICLES])),
    "fr": dict(zip([a["slug"] for a in ARTICLES], [a["title_fr"] for a in ARTICLES])),
    "es": dict(zip([a["slug"] for a in ARTICLES], [a["title_es"] for a in ARTICLES])),
}

fails = 0
print("== 1) 线上 sitemap 新 URL ==")
smf = os.path.join(SCRATCH, "online_sitemap_2000.xml")
subprocess.run(["curl", "-s", "-m", "60", "--noproxy", "*", "-o", smf,
                "https://taigetag.com/sitemap.xml"], check=True)
sm = open(smf, encoding="utf-8").read()
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
        url = "https://taigetag.com/%sblog/%s?v=151" % (pre, a["slug"])
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
        ok = bool(core) and core in title
        if not ok:
            fails += 1
        print("  %-40s %-52s %s" % ("%s %s" % (lang, a["slug"][:30]), title[:50],
                                    "OK" if ok else "!! 期望含 %s" % core))

print("== 3) 线上六语列表页首卡 ==")
for pre in ("", "en/", "ja/", "ko/", "fr/", "es/"):
    p = os.path.join(SCRATCH, "online_idx_%s.html" % (pre.replace("/", "") or "zh"))
    subprocess.run(["curl", "-s", "-m", "60", "--noproxy", "*", "-o", p,
                    "https://taigetag.com/%sblog/index.html?v=151" % pre], check=True)
    s = open(p, encoding="utf-8").read()
    hit = [a["slug"] for a in ARTICLES if a["slug"] in s]
    print("  %-24s 新卡片命中=%d %s" % ("%sblog/index.html" % pre, len(hit), hit))
    if len(hit) != 2:
        fails += 1

print("== 4) 线上首页 HTML 的 BUST_VERSION ==")
jsf = os.path.join(SCRATCH, "online_main_2000.js")
subprocess.run(["curl", "-s", "-m", "60", "--noproxy", "*", "-o", jsf,
                "https://taigetag.com/js/main.js?v=151"], check=True)
js = open(jsf, encoding="utf-8").read()
m = re.search(r'var BUST_VERSION = "([^"]*)";', js)
print("  线上 main.js BUST_VERSION = %s" % (m.group(1) if m else "未找到"))
if not m or m.group(1) != "151":
    fails += 1

print("\n线上验证失败项 = %d" % fails)
raise SystemExit(1 if fails else 0)
