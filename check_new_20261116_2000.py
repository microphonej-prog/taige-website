# -*- coding: utf-8 -*-
"""新文章自检：data-* 六语完整性 + 语言页可见中文残留。"""
import re
import sys
from html.parser import HTMLParser

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
FILES = [
    "blog/woven-label-qr-code-guide.html",
    "blog/eu-textiles-epr-brand-registration-guide.html",
]
LANGPAGES = []
for l in ["en", "fr", "es", "ja", "ko"]:
    for f in FILES:
        LANGPAGES.append(f.replace("blog/", l + "/blog/"))


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


def missing_attrs(path):
    s = open(path, encoding="utf-8").read()
    p = P()
    p.feed(s)
    bad = {}
    total = 0
    for tag, a in p.tags:
        keys = [k for k in a if k.startswith("data-")]
        base = {k for k in keys if k.endswith("-ph") is False}
        if not keys:
            continue
        total += 1
        for l in LANGS:
            d = "data-%s" % l
            ph = "data-%s-ph" % l
            if d not in a and ph not in a and any(k.startswith("data-%s-" % l) is False for k in keys):
                pass
        # 有任一语言 data 属性时，要求六语齐全（ph 体系单独算）
        for l in LANGS:
            if ("data-%s" % l) not in a and ("data-%s-ph" % l) not in a:
                bad.setdefault(tag, []).append(l)
    return total, bad


for f in FILES:
    total, bad = missing_attrs(f)
    print(f, "含 data 属性标签数", total, "缺属性标签", len(bad))
    for k, v in list(bad.items())[:5]:
        print("   <", k, "> 缺", sorted(set(v)))

for f in LANGPAGES:
    s = open(f, encoding="utf-8").read()
    body = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", s, flags=re.S)
    cn = [m.group(1).strip() for m in re.finditer(r">([^<>]+)<", body) if re.search(r"[\u4e00-\u9fff]", m.group(1))]
    attr = re.findall(r'(placeholder|title|alt|aria-label)="([^"]*[\u4e00-\u9fff][^"]*)"', body)
    print(f, "可见中文段", len(cn), "属性中文", len(attr), cn[:3])
