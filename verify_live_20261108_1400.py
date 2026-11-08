# -*- coding: utf-8 -*-
"""线上最终验证：新页正文/标题/语言页抽样 + sitemap 一致性。"""
import sys, io, re, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE = "https://taigetag.com/"


def get(path):
    req = urllib.request.Request(BASE + path, headers={"User-Agent": "Mozilla/5.0 TAGE-check"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.status, r.read().decode("utf-8", "ignore")


checks = ["blog/care-label-symbols-chart.html", "blog/eyelet-grommet-rivet-guide.html",
          "en/blog/care-label-symbols-chart.html", "de/blog/care-label-symbols-chart.html",
          "pt/blog/eyelet-grommet-rivet-guide.html", "ja/blog/eyelet-grommet-rivet-guide.html",
          "ko/blog/care-label-symbols-chart.html", "fr/blog/eyelet-grommet-rivet-guide.html",
          "es/blog/care-label-symbols-chart.html"]

for p in checks:
    st, body = get(p)
    t = re.search(r"<title>(.*?)</title>", body, re.S)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
    ni = "noindex" in body.lower()
    hl = len(re.findall(r'hreflang="', body))
    print("%d %-46s %5dB hreflang=%d noindex=%s | %s" % (
        st, p, len(body.encode()), hl, "Y" if ni else "N",
        (t.group(1).strip()[:50] if t else "NO TITLE")))
    if h1:
        print("      H1:", re.sub(r"<[^>]+>", "", h1.group(1)).strip()[:60])

st, sm = get("sitemap.xml")
locs = re.findall(r"<loc>([^<]+)</loc>", sm)
print("\nsitemap: HTTP %d, %d loc, 唯一 %d" % (st, len(locs), len(set(locs))))
for s in ("care-label-symbols-chart", "eyelet-grommet-rivet-guide"):
    hits = [u for u in locs if s in u]
    print("  %s: %d URLs" % (s, len(hits)))

st, js = get("js/main.js")
print("main.js BUST:", re.search(r'BUST_VERSION = "(\d+)"', js).group(1))
key = get("IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc.txt")
print("IndexNow key file: HTTP %d, 内容匹配 %s" % (key[0], key[1].strip() == "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"))
