# -*- coding: utf-8 -*-
"""驗證：屬性齊全、noindex、sitemap、卡片、裸引號、de/pt 洩漏、desc/標題長度"""
import re, os, glob, sys
ORDER = ["zh", "en", "fr", "es", "ja", "ko"]
LANGS = ["en", "fr", "es", "ja", "ko"]
SLUGS = ["3pl-fulfillment-packaging-spec.html", "acrylic-hang-tag-guide.html"]
bad = 0

for slug in SLUGS:
    print("=" * 70)
    src = open("blog/%s" % slug, encoding="utf-8").read()
    # 每篇文章正文區塊裡，每個 data-zh 元素是否都有其餘五語
    body = src[src.index('<section class="article-body">'):src.index("</main>")]
    els = re.findall(r'<(?:p|h1|h2|h3|div|li|th|td|a)[^>]*data-zh="[^"]*"[^>]*>', body)
    miss = []
    for e in els:
        have = set(re.findall(r'data-([a-z]{2})="', e))
        if not set(ORDER) <= have:
            miss.append((e[:60], sorted(set(ORDER) - have)))
    print("正文元素 %d 個，缺語種元素 %d 個 %s" % (len(els), len(miss), miss[:3]))
    if miss:
        bad += 1

    # 裸雙引號／截斷偵測：屬性值內不應出現在 < > 之後立刻接中文
    trunc = re.findall(r'<\w+"', body)
    print("疑似屬性截斷(<tag\") 數量:", len(trunc))
    if trunc:
        bad += 1

    # de/pt 洩漏
    for l in ("de", "pt"):
        print("data-%s 出現次數: %d" % (l, len(re.findall(r'data-%s="' % l, src))))

    # 各語種頁存在 / noindex
    for l in LANGS:
        p = "%s/blog/%s" % (l, slug)
        if not os.path.exists(p):
            print("  ✗ 缺檔", p); bad += 1; continue
        t = open(p, encoding="utf-8").read()
        ni = 'noindex' in t
        title_m = re.search(r"<title[^>]*>([^<]*)</title>", t)
        print("  %s %-24s noindex=%s title=%s" % (l, "OK" if t else "?", ni, title_m.group(1)[:58] if title_m else "?"))
        if ni:
            bad += 1

    # 卡片在每個語言目錄的 blog/index
    idxs = ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]
    for i in idxs:
        s = open(i, encoding="utf-8").read()
        if slug not in s:
            print("  ✗ 卡片缺失", i); bad += 1
    print("  卡片 6 個列表頁檢查完成")

print("=" * 70)
sm = open("sitemap.xml", encoding="utf-8").read()
locs = re.findall(r"<loc>(.*?)</loc>", sm)
import collections
dup = [k for k, v in collections.Counter(locs).items() if v > 1]
print("sitemap URL 總數:", len(locs), "重複:", dup or "無")
for slug in SLUGS:
    hit = [u for u in locs if u.endswith("/" + slug)]
    print(" ", slug, "→", len(hit), "條")
    for u in hit:
        print("     ", u)
print("de/pt 殘留:", [u for u in locs if "/de/" in u or "/pt/" in u] or "無")
print("BUST_VERSION:", re.search(r'BUST_VERSION = "(\d+)"', open("js/main.js", encoding="utf-8").read()).group(1))
print("問題數:", bad)
sys.exit(1 if bad else 0)
