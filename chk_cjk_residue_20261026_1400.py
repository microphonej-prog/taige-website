# -*- coding: utf-8 -*-
import re, io
for f in ("en_garment-packaging-budget-allocation", "fr_garment-packaging-cleanliness-contamination-control", "ko_garment-packaging-budget-allocation"):
    s = io.open("F:/hermes/cache/scratch/live1026/%s.html" % f, encoding="utf-8", errors="replace").read()
    body = s[s.index('class="article-body"'):]
    txt = re.sub(r"<script.*?</script>", " ", body, flags=re.S)
    txt = re.sub(r"<[^>]+>", " ", txt)
    for m in re.finditer(r"[\u4e00-\u9fff]", txt):
        i = m.start()
        print(f, "|", repr(txt[max(0, i-40):i+40]))
