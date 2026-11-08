# -*- coding: utf-8 -*-
"""发布前本地校验：属性完整性 / 卡片 / sitemap 去重 / hreflang / noindex 基线 / 中文残留。"""
import sys, io, os, re, glob, html
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
os.chdir(r"C:/Users/micro/taige-website")

SLUGS = ["care-label-symbols-chart.html", "eyelet-grommet-rivet-guide.html"]
LANGS = ["zh", "en", "fr", "es", "ja", "ko", "de", "pt"]

print("=== 1) 源页 data 属性覆盖（每个元素八语齐全？）===")
from html.parser import HTMLParser


class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.bad = []
        self.total = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        present = [l for l in LANGS if ("data-" + l) in d]
        if present:
            self.total += 1
            missing = [l for l in LANGS if l not in present]
            if missing:
                self.bad.append((tag, missing, (d.get("data-zh") or "")[:30]))


for s in SLUGS:
    p = Scan()
    p.feed(open("blog/" + s, encoding="utf-8").read())
    print("  %s: 带data元素 %d, 缺语种元素 %d" % (s, p.total, len(p.bad)))
    for b in p.bad[:5]:
        print("    !", b)

print("=== 2) blog/index.html 卡片 ===")
idx = open("blog/index.html", encoding="utf-8").read()
for s in SLUGS:
    print("  %s: 卡片 %d 处" % (s, idx.count('href="%s"' % s)))

print("=== 3) sitemap 去重 + 新 URL ===")
sm = open("sitemap.xml", encoding="utf-8").read()
locs = re.findall(r"<loc>([^<]+)</loc>", sm)
print("  <loc> 总数 %d, 唯一 %d, 重复 %d" % (len(locs), len(set(locs)), len(locs) - len(set(locs))))
for s in SLUGS:
    got = [u for u in locs if u.endswith("/blog/" + s)]
    print("  %s: sitemap 条目 %d -> %s" % (s, len(got), [u.split("taigetag.com")[1] for u in got]))

print("=== 4) 各语言页 noindex / hreflang 条数 ===")
for s in SLUGS:
    for l in LANGS:
        f = ("blog/" + s) if l == "zh" else ("%s/blog/%s" % (l, s))
        t = open(f, encoding="utf-8").read()
        hl = len(re.findall(r'hreflang="', t))
        ni = "noindex" in t.lower()
        title = re.search(r"<title[^>]*>(.*?)</title>", t, re.S)
        print("  %-9s %-32s hreflang=%d noindex=%s title=%s" % (
            l, s, hl, "Y" if ni else "N", (title.group(1)[:44] if title else "?")))

print("=== 5) 中文残留（de/pt 页正文可见中文）===")
for s in SLUGS:
    for l in ("de", "pt"):
        t = open("%s/blog/%s" % (l, s), encoding="utf-8").read()
        body = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", t, flags=re.S)
        hits = [m.group(1)[:40] for m in re.finditer(r">([^<>]+)<", body) if re.search(r"[\u4e00-\u9fff]", m.group(1))]
        print("  %s/%s 可见中文片段 %d %s" % (l, s, len(hits), hits[:3]))

print("=== 6) noindex 基线（de/pt 文章应仍 noindex）===")
for l in ("de", "pt"):
    files = [f for f in glob.glob("%s/blog/*.html" % l) if not f.endswith("index.html")]
    ni = [f for f in files if "noindex" in open(f, encoding="utf-8").read().lower()]
    print("  %s: 文章 %d, noindex %d, 可索引 %d" % (l, len(files), len(ni), len(files) - len(ni)))

print("=== 7) BUST_VERSION / 内部死链（新页）===")
print("  BUST:", re.search(r'BUST_VERSION = "(\d+)"', open("js/main.js", encoding="utf-8").read()).group(1))
missing = {}
for l in LANGS:
    d = "blog" if l == "zh" else "%s/blog" % l
    for s in SLUGS:
        p = os.path.join(d, s)
        txt = open(p, encoding="utf-8").read()
        for h in re.findall(r'href="([^"]+)"', txt):
            if h.startswith(("http", "mailto:", "tel:", "#", "javascript:", "data:")):
                continue
            tgt = h.split("?")[0].split("#")[0]
            if not tgt:
                continue
            full = os.path.normpath(os.path.join(d, tgt))
            if not os.path.exists(full):
                missing[(p, h)] = missing.get((p, h), 0) + 1
print("  新页死链:", len(missing))
for k in list(missing)[:10]:
    print("   ", k)
