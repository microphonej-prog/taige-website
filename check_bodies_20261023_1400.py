# -*- coding: utf-8 -*-
"""校验正文六语属性完整性：每个 data-zh 元素必须同时有 en/fr/es/ja/ko；并统计中文字数。"""
import re, sys
from html.parser import HTMLParser

FILES = sys.argv[1:]
LANGS = ("en", "fr", "es", "ja", "ko")

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.bad = []
        self.count = 0
        self.tags = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        self.tags += 1
        if "data-zh" in d:
            self.count += 1
            miss = [l for l in LANGS if ("data-" + l) not in d]
            empty = [k for k, v in d.items() if k.startswith("data-") and (v is None or not v.strip())]
            if miss or empty:
                self.bad.append((tag, miss, empty, (d.get("data-zh") or "")[:40]))

for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = P()
    p.feed(s)
    zh_chars = len(re.findall(r"[\u4e00-\u9fff]", " ".join(re.findall(r'data-zh="([^"]*)"', s))))
    print("%-28s data-zh元素=%d 标签总数=%d 缺失=%d 中文字数≈%d"
          % (f, p.count, p.tags, len(p.bad), zh_chars))
    for b in p.bad[:10]:
        print("   缺失:", b)
    # 裸双引号检查：data 属性值内部若出现未转义双引号会导致属性截断，parser 会把残片当新属性
    for k in ("data-zh", "data-en", "data-fr", "data-es", "data-ja", "data-ko"):
        for m in re.finditer(k + r'=""', s):
            print("   空属性:", k, s[max(0, m.start()-60):m.start()].replace("\n", " ")[-60:])
    if re.search(r"[\ufffd]", s):
        print("   ！含替换字符 U+FFFD")
