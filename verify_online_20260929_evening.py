#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-29 晚间批次线上验证：六语 DOM 标题 + 正文渲染语言 + 线上 sitemap + 列表卡片 + 版本号。
用法: <python> verify_online_20260929_evening.py
"""
import re, os, sys, subprocess, tempfile

os.chdir(os.path.dirname(os.path.abspath(__file__)))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BUST = "122"
SLUGS = ["woven-label-shrinkage-guide.html", "trim-measurement-tolerance-guide.html"]
LANGS = [("zh", ""), ("en", "en/"), ("ja", "ja/"), ("ko", "ko/"), ("fr", "fr/"), ("es", "es/")]
WANT = {
    "woven-label-shrinkage-guide.html": {
        "zh": "織嘜與洗水標縮水率指南", "en": "Woven Label Shrinkage Guide",
        "ja": "織りラベルと洗濯表示ラベルの収縮率ガイド", "ko": "직조 라벨·세탁 표시 라벨 수축률 가이드",
        "fr": "Retrait des labels tissés", "es": "Encogimiento de etiquetas tejidas"},
    "trim-measurement-tolerance-guide.html": {
        "zh": "服裝輔料尺寸測量與公差指南", "en": "Trims Measurement and Tolerance Guide",
        "ja": "副資材の寸法測定と公差ガイド", "ko": "부자재 치수 측정과 공차 가이드",
        "fr": "Mesure et tolérance des accessoires", "es": "Medición y tolerancia de accesorios"},
}
BODY = {
    "woven-label-shrinkage-guide.html": {
        "zh": "三種收縮機制", "en": "Three Mechanisms",
        "ja": "3つのメカニズム", "ko": "세 가지 메커니즘",
        "fr": "trois mécanismes", "es": "tres mecanismos"},
    "trim-measurement-tolerance-guide.html": {
        "zh": "三類分歧", "en": "Three Sources of Disagreement",
        "ja": "3つの食い違い", "ko": "세 가지 불일치",
        "fr": "Trois sources de désaccord", "es": "Tres fuentes de desacuerdo"},
}
fails = []


def chrome_dom(url):
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                        "--virtual-time-budget=12000", "--dump-dom", url],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=150)
    return r.stdout or ""


print("=== 1) 线上六语标题与正文渲染（?v=%s 防缓存） ===" % BUST, flush=True)
for slug in SLUGS:
    for code, pref in LANGS:
        url = "https://taigetag.com/%sblog/%s?v=%s" % (pref, slug, BUST)
        dom = chrome_dom(url)
        m = re.search(r'<title[^>]*>(.*?)</title>', dom, re.S)
        t = m.group(1).strip() if m else ""
        ok_t = WANT[slug][code] in t
        ok_b = BODY[slug][code] in dom
        if not ok_t:
            fails.append("title %s [%s] → %r" % (slug, code, t[:70]))
        if not ok_b:
            fails.append("body %s [%s] 未见 %r" % (slug, code, BODY[slug][code]))
        # 语言页不应残留中文属性字面量
        leak = 'data-zh="' in dom
        if pref and leak:
            fails.append("泄漏 data-zh：%s [%s]" % (slug, code))
        print("  %-4s %-40s title=%s body=%s%s" % (
            code, slug, "OK " if ok_t else "BAD", "OK " if ok_b else "BAD",
            " 泄漏data-zh!" if (pref and leak) else ""), flush=True)
        print("       %s" % t[:96], flush=True)

print("=== 2) 线上 sitemap ===", flush=True)
tmp = os.path.join(tempfile.gettempdir(), "tg_sitemap_check_eve.xml")
subprocess.run(["curl", "-sS", "-o", tmp, "https://taigetag.com/sitemap.xml"], check=True)
sm = open(tmp, encoding="utf-8", errors="replace").read()
for slug in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % slug] + \
             ["https://taigetag.com/%s/blog/%s" % (l, slug) for l, _ in LANGS[1:]]:
        if "<loc>%s</loc>" % u not in sm:
            fails.append("线上 sitemap 缺 %s" % u)
        else:
            seg = sm[sm.index("<loc>%s</loc>" % u):][:200]
            if "<lastmod>2026-09-29</lastmod>" not in seg:
                fails.append("线上 sitemap lastmod 非 2026-09-29：%s" % u)
m = re.search(r'<loc>https://taigetag.com/blog/index.html</loc>\s*<lastmod>([^<]*)</lastmod>', sm)
print("  线上 <loc> 总数 %d；blog 列表页 lastmod = %s" % (sm.count("<loc>"), m and m.group(1)), flush=True)
if not m or m.group(1) != "2026-09-29":
    fails.append("线上 blog index lastmod = %s" % (m and m.group(1)))

print("=== 3) 线上列表页卡片 ===", flush=True)
tmp2 = os.path.join(tempfile.gettempdir(), "tg_index_check_eve.html")
subprocess.run(["curl", "-sS", "-o", tmp2, "https://taigetag.com/blog/index.html"], check=True)
idx = open(tmp2, encoding="utf-8", errors="replace").read()
for slug in SLUGS:
    n = idx.count(slug)
    print("  %-42s 命中 %d 次" % (slug, n), flush=True)
    if n == 0:
        fails.append("线上列表页缺卡片 %s" % slug)

print("=== 4) 线上 main.js 版本号 ===", flush=True)
tmp3 = os.path.join(tempfile.gettempdir(), "tg_main_check_eve.js")
subprocess.run(["curl", "-sS", "-o", tmp3, "https://taigetag.com/js/main.js?v=%s" % BUST], check=True)
js = open(tmp3, encoding="utf-8", errors="replace").read()
v = re.search(r'var BUST_VERSION = "([^"]*)"', js)
print("  线上 BUST_VERSION = %s" % (v and v.group(1)), flush=True)
if not v or v.group(1) != BUST:
    fails.append("线上 BUST_VERSION = %s" % (v and v.group(1)))

print(flush=True)
if fails:
    print("失败 %d 项：" % len(fails))
    for f in fails:
        print(" - " + f)
    sys.exit(1)
print("线上验证全部通过 ✅")
