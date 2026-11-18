# -*- coding: utf-8 -*-
"""线上验收：title/描述/hreflang/sitemap 是否含新 URL、卡片是否上线。"""
import re
import ssl
import urllib.request

CTX = ssl.create_default_context()
SLUGS = ["care-label-fiber-content-tolerance-guide", "trim-test-report-reading-guide"]


def get(u):
    rq = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 verify"})
    with urllib.request.urlopen(rq, timeout=45, context=CTX) as r:
        return r.status, r.read().decode("utf-8", "ignore")


st, html_root = get("https://taigetag.com/blog/%s.html" % SLUGS[0])
print("root A", st, "| title:", re.search(r"<title[^>]*>(.*?)</title>", html_root, re.S).group(1)[:60])
st, h = get("https://taigetag.com/en/blog/%s.html" % SLUGS[1])
print("en B", st, "| title:", re.search(r"<title[^>]*>(.*?)</title>", h, re.S).group(1)[:70])
print("   hreflang 条数:", len(re.findall(r'hreflang="', h)),
      "| noindex:", "noindex" in h.lower())
print("   正文首段 en:", re.search(r"<p>(Most people[^<]{0,80})", h).group(1))

st, sm = get("https://taigetag.com/sitemap.xml")
print("sitemap", st, "URL 数:", sm.count("<loc>"))
for s in SLUGS:
    print("  %s -> %d 条" % (s, sm.count(s)))

st, bi = get("https://taigetag.com/ja/blog/index.html")
print("ja blog index", st, "| 新卡:", "care-label-fiber-content-tolerance-guide" in bi,
      "| trim:", "trim-test-report-reading-guide" in bi, "| noindex:", "noindex" in bi.lower())
