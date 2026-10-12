#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上正文中文残留抽查：en/fr/es 三语的新文章 body 内不应出现汉字"""
import re, ssl, urllib.request

SLUGS = ["dresses-skirts-trims-guide.html", "dancewear-stage-costume-trims-guide.html"]
ctx = ssl.create_default_context()
bad = 0
for s in SLUGS:
    for l in ["en", "fr", "es"]:
        u = "https://taigetag.com/%s/blog/%s?v=3" % (l, s)
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        h = urllib.request.urlopen(req, timeout=45, context=ctx).read().decode("utf-8", "replace")
        body = h[h.find('<section class="article-body"'):h.find("</main>")]
        txt = re.sub(r"<[^>]+>", "", body)
        cjk = re.findall(r"[\u4e00-\u9fff]", txt)
        resid = len(re.findall(r"data-(?:zh|en|ja|ko|fr|es)=", h))
        print("%-3s %-40s 正文汉字=%d  残留data属性=%d" % (l, s, len(cjk), resid))
        if cjk:
            bad += 1
            print("    样例:", "".join(cjk[:20]))
        if resid:
            bad += 1
print("异常页数：%d" % bad)
