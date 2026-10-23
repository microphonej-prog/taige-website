# -*- coding: utf-8 -*-
import re, os, glob

d = os.path.dirname(os.path.abspath(__file__))
for f in sorted(glob.glob(os.path.join(d, "*.html"))):
    s = open(f, encoding="utf-8", errors="replace").read()
    t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    first = re.search(r'<section class="article-body">(.*?)</p>', s, re.S)
    txt = re.sub(r"<[^>]+>", " ", first.group(1)) if first else ""
    txt = " ".join(txt.split())[:80]
    print("%-52s" % os.path.basename(f))
    print("   title:", (t.group(1).strip() if t else "MISSING")[:100])
    print("   h1   :", re.sub(r"<[^>]+>", "", h1.group(1)).strip()[:90] if h1 else "MISSING")
    print("   body :", txt)
