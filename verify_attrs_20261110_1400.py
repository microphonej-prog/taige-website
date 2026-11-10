# -*- coding: utf-8 -*-
"""逐元素校验 data-<lang> 齐备度（用 HTMLParser，避免属性值里 > 截断正则）。"""
import sys
from html.parser import HTMLParser

LANGS = ["zh", "en", "fr", "es", "ja", "ko", "de", "pt"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.missing = {}
        self.total = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "data-zh" not in d:
            return
        self.total += 1
        miss = [l for l in LANGS if "data-" + l not in d]
        if miss:
            key = (tag, tuple(miss))
            self.missing.setdefault(key, []).append(d.get("data-zh", "")[:40])


for f in sys.argv[1:]:
    p = P()
    p.feed(open(f, encoding="utf-8").read())
    print("== %s 带 data-zh 元素 %d，缺语言元素 %d" % (f, p.total, sum(len(v) for v in p.missing.values())))
    for (tag, miss), vals in sorted(p.missing.items(), key=lambda kv: -len(kv[1])):
        print("   <%s> 缺 %s  x%d  例: %s" % (tag, ",".join(miss), len(vals), vals[0]))
