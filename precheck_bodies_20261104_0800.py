# -*- coding: utf-8 -*-
"""修正文文件里文本节点开头的多余空格，并扫描属性完整性/裸 & /裸引号。"""
import re, sys
from html.parser import HTMLParser

LANGS = ("zh", "en", "ja", "ko", "fr", "es")


class Chk(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.bad = []
        self.n = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if not any(k.startswith("data-") for k in d):
            return
        self.n += 1
        missing = [l for l in LANGS if "data-" + l not in d]
        if missing:
            self.bad.append((tag, d.get("data-zh", "")[:40], "缺:" + ",".join(missing)))


for p in sys.argv[1:]:
    s = open(p, encoding="utf-8").read()
    n0 = len(s)
    s = s.replace('"> <', '"><').replace('"> ', '">')
    if len(s) != n0:
        open(p, "w", encoding="utf-8", newline="").write(s)
        print("%s 清理空格 %d 字符" % (p, n0 - len(s)))
    c = Chk()
    c.feed(s)
    print("%s: data 元素 %d 个, 缺语言 %d" % (p, c.n, len(c.bad)))
    for b in c.bad[:20]:
        print("   ", b)
    # 裸 & / 连续双引号 / 空 data 属性
    for m in re.finditer(r'data-(?:zh|en|ja|ko|fr|es)=""', s):
        print("   空属性 at", s[:m.start()].count("\n") + 1)
    for m in re.finditer(r'="[^"]*"[^"\s>]', s):
        print("   可疑引号 at", s[:m.start()].count("\n") + 1, s[m.start():m.start() + 60])
    for m in re.finditer(r'&(?!amp;|nbsp;|quot;|lt;|gt;|#\d+;|[a-z]+;)', s):
        print("   裸& at", s[:m.start()].count("\n") + 1, s[m.start() - 20:m.start() + 20])
