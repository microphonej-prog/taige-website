#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
SLUGS = ["trim-invoice-tax-export-rebate.html", "packaging-automation-bag-compatibility.html"]
for lang in ["zh", "en", "ja", "ko", "fr", "es"]:
    for slug in SLUGS:
        p = "blog/%s" % slug if lang == "zh" else "%s/blog/%s" % (lang, slug)
        s = open(p, encoding="utf-8").read()
        m = re.search(r"<title>(.*?)</title>", s, re.S)
        m2 = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
        print("%-3s %-45s exact=%s loose=%s len=%d" % (lang, slug[:43], bool(m), bool(m2), len(s)))
