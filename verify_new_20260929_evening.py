#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-29 晚间批次本地校验：生成后的六语页面 / 列表卡片 / sitemap / BUST_VERSION"""
import re, os, sys, json

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

SLUGS = ["woven-label-shrinkage-guide.html", "trim-measurement-tolerance-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
TAKE = {"en": "en", "ja": "ja", "ko": "ko", "fr": "fr", "es": "es"}
bad = 0

TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.S)
DESC_RE = re.compile(r'<meta name="description"[^>]*?content="([^"]*)"[^>]*>', re.S)


def fail(msg):
    global bad
    bad += 1
    print("   !! " + msg)


# ---------- 1) 根页面 + 五语页面 ----------
for slug in SLUGS:
    path = "blog/%s" % slug
    s = open(path, encoding="utf-8", newline="").read()
    t = TITLE_RE.search(s).group(1)
    d = DESC_RE.search(s).group(1)
    print("%-42s title=%s" % (slug, t[:56]))
    print("      desc=%s" % d[:70])
    if "data-" in t or "data-" in d:
        fail("根页面 title/desc 仍有 data- 残留")
    if 'lang="zh-Hant"' not in s:
        fail("根页面 html lang 不是 zh-Hant")
    for token in ["application/ld+json", 'href="../css/style.css?v=']:
        if token not in s:
            fail("缺 %s" % token)
    for tok_re, label in [(r'src="\.\./js/main\.js\?v=[\d.]+"', "main.js"),
                          (r'src="\.\./js/assist\.js\?v=[\d.]+"', "assist.js"),
                          (r'(?:辅料|輔料) FAQ', "辅料 FAQ 链接"),
                          (r'(?:相关|相關)文章', "相关文章小节"),
                          (r'class="cta-box"', "cta-box")]:
        if not re.search(tok_re, s):
            fail("缺 %s" % label)
    n_ld = len(re.findall(r'application/ld\+json', s))
    try:
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            json.loads(blk)
    except Exception as e:
        fail("JSON-LD 非法：%s" % e)

    for lang in LANGS:
        p2 = "%s/blog/%s" % (lang, slug)
        s2 = open(p2, encoding="utf-8", newline="").read()
        t2 = TITLE_RE.search(s2).group(1)
        d2 = DESC_RE.search(s2).group(1)
        body_no_script = re.sub(r'<script.*?</script>', '', s2, flags=re.S)
        body_no_script = re.sub(r'<style.*?</style>', '', body_no_script, flags=re.S)
        cjk_hits = re.findall(r'[\u4e00-\u9fff]+', re.sub(r'<[^>]*>', '', body_no_script))
        cjk = sum(len(h) for h in cjk_hits)
        resid = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="', s2))
        leak = len(re.findall(r'>(?:\s*)data-(?:zh|en|fr|es|ja|ko)="', s2))
        print("   %-4s title=%s" % (lang, t2[:62]))
        if "data-" in t2 or "data-" in d2:
            fail("%s title/desc 有 data- 残留" % lang)
        if resid:
            fail("%s 元素仍残留 data-* 属性 %d 处（该元素缺本语言属性）" % (lang, resid))
        if leak:
            fail("%s 正文泄漏 data-* 字面量 %d 处" % (lang, leak))
        if 'hreflang="zh-Hant"' not in s2 or 'hreflang="x-default"' not in s2:
            fail("%s hreflang 不完整" % lang)
        if lang != "ja" and cjk > 20:
            fail("%s 正文汉字 %d 个（%s），超出全站既有基线" % (lang, cjk, "/".join(cjk_hits[:6])))
        print("        正文汉字残留 %d 字符（已排除 JSON-LD/样式；全站既有基线约 10 个）" % cjk)

# ---------- 2) 列表页卡片 ----------
for lang, idx in [("zh", "blog/index.html")] + [(l, "%s/blog/index.html" % l) for l in LANGS]:
    s = open(idx, encoding="utf-8", newline="").read()
    grid = s.find('<div class="post-grid">')
    blocks = re.findall(r'<article class="post-card">(.*?)</article>', s[grid:], re.S)[:2]
    hrefs = [re.search(r'href="([^"]+)"', b).group(1) for b in blocks]
    ok = hrefs == SLUGS
    print("   %-4s 首两卡=%s  %s" % (lang, hrefs, "OK" if ok else "!! 顺序或内容不对"))
    if not ok:
        fail("%s 列表页首两卡不是本次两篇新文章" % lang)

# ---------- 3) sitemap ----------
sm = open("sitemap.xml", encoding="utf-8", newline="").read()
n_loc = sm.count("<loc>")
print("   sitemap <loc> 总数 %d" % n_loc)
for slug in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % slug] + ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        if "<loc>%s</loc>" % u not in sm:
            fail("sitemap 缺 %s" % u)
        else:
            seg = sm[sm.index("<loc>%s</loc>" % u):][:200]
            if "<lastmod>2026-09-29</lastmod>" not in seg:
                fail("lastmod 不对：%s" % u)
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    seg = sm[sm.index("<loc>%s</loc>" % u):][:200]
    if "<lastmod>2026-09-29</lastmod>" not in seg:
        fail("blog index lastmod 未更新：%s" % u)

# ---------- 4) BUST_VERSION ----------
mj = open("js/main.js", encoding="utf-8").read()
b = re.search(r'var BUST_VERSION = "(\d+)"', mj).group(1)
print("   BUST_VERSION = %s" % b)
if b != "122":
    fail("BUST_VERSION 应为 122")

print("\n结论：", "全部通过" if bad == 0 else "%d 项待修" % bad)
sys.exit(1 if bad else 0)
