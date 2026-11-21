# -*- coding: utf-8 -*-
"""校验新文章：六语属性完整、可见文本为中文、无占位符泄漏、内链存在。"""
import re
import sys
from html.parser import HTMLParser

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
FILES = ["blog/clothing-size-stickers-guide.html", "blog/hem-tag-guide.html"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = P()
    p.feed(s)
    withdata = [(t, a) for t, a in p.tags if any(k.startswith("data-") and k.split("-")[1] in LANGS for k in a)]
    missing = []
    for t, a in withdata:
        miss = [l for l in LANGS if ("data-%s" % l) not in a]
        if miss:
            missing.append((t, miss))
    print("%-45s 带属性元素 %3d | 缺语种元素 %d" % (f, len(withdata), len(missing)))
    if missing[:3]:
        print("   ", missing[:3])
    # 可见文本中文
    plain = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", s, flags=re.S)
    cjk = [m.group(1)[:40] for m in re.finditer(r">([^<>]+)<", plain) if re.search(r"[\u4e00-\u9fff]", m.group(1))]
    print("   可见中文片段 %d（应为中文主稿）" % len(cjk))
    # 占位符 / 裸属性截断
    for bad in ["__PH", "&amp;#x27;", 'data-en=""']:
        n = s.count(bad)
        if n:
            print("   !! 异常串 %s x%d" % (bad, n))
    # 内链目标存在
    import os
    for h in set(re.findall(r'href="([^"]+\.html)"', s)):
        if h.startswith(("http", "../", "#")):
            continue
        path = os.path.normpath(os.path.join("blog", h))
        if not os.path.exists(path):
            print("   !! 死链", h)
    print()
