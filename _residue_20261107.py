# -*- coding: utf-8 -*-
"""定位各语言版本正文里的汉字残留具体内容。"""
import os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SLUGS = ["clothing-label-compliance-central-america.html",
         "clothing-label-compliance-morocco-tunisia.html"]
for lang in ["en", "ko", "fr", "es", "ja"]:
    for slug in SLUGS:
        s = open("%s/blog/%s" % (lang, slug), encoding="utf-8").read()
        body = s[s.index('<section class="article-body">'):]
        hits = re.findall(r"[^<>\n]{0,40}[\u4e00-\u9fff]+[^<>\n]{0,40}", body)
        print("== %s/%s  %d 处" % (lang, slug[:34], len(hits)))
        for h in hits[:6]:
            print("   ", h.strip()[:110])
