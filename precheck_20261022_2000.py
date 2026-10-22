# -*- coding: utf-8 -*-
"""批次前体检：正文文件属性完整性 + 裸双引号/裸 & + 术语表。"""
import re
from html.parser import HTMLParser

FILES = ["blog/_body_wlcut.html", "blog/_body_hgset.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
TEXT_TAGS = set("p h2 h3 li td th div a span strong em b i blockquote small label dt dd caption".split())


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.rows = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        self.stack.append(tag)
        if len(self.stack) == 1 or tag in TEXT_TAGS:
            has_data = any(k in d for k in ("data-zh", "data-en", "data-fr", "data-es", "data-ja", "data-ko"))
            if has_data:
                self.rows.append((tag, {k: v for k, v in d.items() if k.startswith("data-")}, self.getpos()))

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()


for f in FILES:
    s = open(f, encoding="utf-8").read()
    print("=== %s (%d KB) ===" % (f, len(s.encode()) // 1024))
    # 1) 裸 & （不是实体）
    bad_amp = [m.start() for m in re.finditer(r'&(?!(amp|nbsp|quot|lt|gt|#\d+|#x[0-9a-fA-F]+);)', s)]
    print("  裸 & 数量：%d" % len(bad_amp))
    if bad_amp:
        for p in bad_amp[:5]:
            print("    ...", s[max(0, p - 40):p + 20].replace("\n", " "))
    # 2) 属性值里裸双引号：data-xx="... "xxx"...  检测双引号内出现 " 后紧跟字母（启发式）
    suspicious = re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[^"]*"', s)
    print("  可疑裸引号片段：%d" % len(suspicious))
    for x in suspicious[:3]:
        print("    ", x[:120])
    # 3) 属性完整性
    c = Checker()
    c.feed(s)
    miss = []
    for tag, attrs, pos in c.rows:
        lack = [l for l in LANGS if ("data-" + l) not in attrs]
        if lack:
            miss.append((pos, tag, lack, list(attrs.keys())))
    print("  带 data-* 的元素数：%d ；缺语种：%d" % (len(c.rows), len(miss)))
    for pos, tag, lack, keys in miss[:8]:
        print("    行%d <%s> 缺 %s  现有=%s" % (pos[0], tag, lack, keys))
    # 4) h2 / table / callout / cta 计数
    print("  h2=%d  table=%d  callout=%d  cta-btn=%d  链接=%d"
          % (s.count("<h2"), s.count("<table"), s.count('class="callout"'),
             s.count('class="cta-btn"'), s.count("<a href=")))
    # 5) 中文字符量（data-zh 汇总）
    zh = "".join(re.findall(r'data-zh="([^"]*)"', s))
    print("  data-zh 中文总字数：%d" % len(re.findall(r'[\u4e00-\u9fff]', zh)))
