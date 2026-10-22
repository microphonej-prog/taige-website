#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上校验：12 个 URL 的 title（curl 直连，绕 TUN），sitemap 含新 URL"""
import subprocess, re, time

BASE = "https://taigetag.com"
SLUGS = ["magnetic-trims-air-freight-guide.html", "trim-label-consistency-audit-guide.html"]
PREFIX = {"zh": "/blog/", "en": "/en/blog/", "ja": "/ja/blog/", "ko": "/ko/blog/", "fr": "/fr/blog/", "es": "/es/blog/"}

def get(url):
    r = subprocess.run(["curl", "-sS", "--noproxy", "*", "-m", "40", "-A", "Mozilla/5.0", url],
                       capture_output=True)
    return r.stdout.decode("utf-8", "replace")

for slug in SLUGS:
    for lang, pre in PREFIX.items():
        url = BASE + pre + slug + "?lang=%s&v=175" % lang
        s = get(url)
        m = re.search(r'<title[^>]*>(.*?)</title>', s, re.S)
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
        print("%-4s %-42s len=%6d title=%s" % (lang, slug, len(s), (m.group(1).strip()[:60] if m else "!! NO TITLE")))
        if h1:
            print("      h1=%s" % h1.group(1).strip()[:60])

sm = get(BASE + "/sitemap.xml")
for slug in SLUGS:
    print("sitemap %s -> %d" % (slug, len(re.findall(r'<loc>[^<]*%s</loc>' % re.escape(slug), sm))))
print("sitemap 总 <loc>:", sm.count("<loc>"))
