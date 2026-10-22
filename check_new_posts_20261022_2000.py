# -*- coding: utf-8 -*-
"""2026-10-22 20:00 批次本地校验：六语页面/标题/正文/data 残留/卡片/sitemap。"""
import re, os, sys
from html.parser import HTMLParser

SLUGS = ["woven-label-cutting-methods.html", "hang-tag-set-combination-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
CJK = re.compile(r'[\u4e00-\u9fff]')
KANA = re.compile(r'[\u3040-\u30ff]')
HANGUL = re.compile(r'[\uac00-\ud7af]')
DATE = "2026-10-22"
DATE_ZH = "2026年10月22日"

ok = True


def fail(msg):
    global ok
    ok = False
    print("  ✗", msg)


for slug in SLUGS:
    print("==== %s ====" % slug)
    paths = {"zh": "blog/" + slug}
    for l in LANGS:
        paths[l] = "%s/blog/%s" % (l, slug)

    for l, p in paths.items():
        if not os.path.exists(p):
            fail("缺文件 " + p)
            continue
        s = open(p, encoding="utf-8").read()

        # title
        m = re.search(r'<title[^>]*>(.*?)</title>', s, re.S)
        title = m.group(1) if m else ""
        # h1
        m1 = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
        h1 = re.sub(r'<[^>]+>', '', m1.group(1)) if m1 else ""
        # description static
        d = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s)
        desc = d.group(1) if d else ""
        # data 残留（语言页应为 0）
        resid = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=', s)) if l != "zh" else -1
        # 正文元素数
        body = s[s.index('class="article-body"'):s.index("</main>")]
        n_p = body.count("<p")
        n_h2 = body.count("<h2")
        n_li = body.count("<li")
        n_td = body.count("<td")
        # 语言纯净度
        bad = ""
        if l == "en" and (CJK.search(h1) or KANA.search(h1) or HANGUL.search(h1)):
            bad = "h1 含非英文字符"
        if l == "ja" and (HANGUL.search(h1) or (CJK.search(h1) and not KANA.search(h1))):
            bad = "h1 疑似非日文"
        if l == "ko" and (KANA.search(h1) or CJK.search(h1)):
            bad = "h1 含日文汉字/中文"
        if l == "fr" and (CJK.search(h1) or KANA.search(h1) or HANGUL.search(h1)):
            bad = "h1 含非拉丁字符"
        if l == "es" and (CJK.search(h1) or KANA.search(h1) or HANGUL.search(h1)):
            bad = "h1 含非拉丁字符"
        print("  [%s] title=%s" % (l, title[:60]))
        print("        h1=%s | desc=%d字 | 残留data=%s | p=%d h2=%d li=%d td=%d %s"
              % (h1[:50], len(desc), resid, n_p, n_h2, n_li, n_td, bad))
        if not title or "TAGE" not in title:
            fail("%s title 异常" % l)
        if resid > 0:
            fail("%s 残留 data-* 属性 %d 个" % (l, resid))
        if bad:
            fail("%s %s" % (l, bad))
        if n_h2 < 5 or n_p < 5 or n_li < 10:
            fail("%s 正文结构不足" % l)
        if DATE_ZH not in s and l == "zh":
            fail("zh 页面缺日期")
    # canonical / hreflang
    s = open(paths["zh"], encoding="utf-8").read()
    can = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
    hl = dict(re.findall(r'hreflang="([^"]+)" href="([^"]+)"', s))
    print("  canonical=%s\n  hreflang=%s" % (can, hl))
    if can != "https://taigetag.com/blog/" + slug:
        fail("canonical 不符")
    if len(hl) != 7:
        fail("hreflang 数量 %d（应为 7）" % len(hl))

# 卡片
idx = open("blog/index.html", encoding="utf-8").read()
grid = idx[idx.index('<div class="post-grid">'):]
first = grid[:grid.index("</article>", grid.index("</article>") + 1) + 12]
for slug in SLUGS:
    n = idx.count('href="%s"' % slug)
    print("卡片 %s 出现 %d 次" % (slug, n))
    if n < 1:
        fail("列表页缺卡片 " + slug)
for slug in SLUGS:
    if slug not in first:
        fail("卡片不在置顶位置 " + slug)

# 卡片六语属性
for tag in ("post-card",):
    pass
cards = re.findall(r'<article class="post-card">.*?</article>', idx, re.S)[:2]
for c in cards:
    for l in ["zh", "en", "ja", "ko", "fr", "es"]:
        if "data-%s=" % l not in c:
            fail("卡片缺 data-%s" % l)

# sitemap
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    urls = ["https://taigetag.com/blog/" + slug] + ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]
    for u in urls:
        if "<loc>%s</loc>" % u not in sm:
            fail("sitemap 缺 " + u)
print("sitemap: 新URL %d 个, <loc> 总数 %d, lastmod=%s 条目 %d"
      % (sum(sm.count("<loc>https://taigetag.com/blog/" + x + "</loc>") for x in SLUGS) +
         sum(sm.count("<loc>https://taigetag.com/%s/blog/%s</loc>" % (l, x)) for l in LANGS for x in SLUGS),
         sm.count("<loc>"), DATE, sm.count("<lastmod>%s</lastmod>" % DATE)))

# BUST_VERSION
mj = open("js/main.js", encoding="utf-8").read()
print("BUST_VERSION:", re.search(r'BUST_VERSION = "(\d+)"', mj).group(1))

print("\n结论:", "全部通过 ✅" if ok else "存在问题 ❌")
sys.exit(0 if ok else 1)
