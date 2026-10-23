# -*- coding: utf-8 -*-
"""校验正文文件的 data 属性完整性（六语），且属性值内无裸双引号/未转义 &。"""
import sys, re
from html.parser import HTMLParser

WANT = ["data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.rows = []
        self.depth_amp = 0
        self.text = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if any(k in d for k in WANT):
            missing = [w for w in WANT if w not in d or not d[w]]
            self.rows.append((tag, missing, d.get("data-zh", "")[:40]))

    def handle_data(self, data):
        self.text.append(data)


for path in ["blog/_body_fscht.html", "blog/_body_rush.html"]:
    raw = open(path, encoding="utf-8").read()
    p = P()
    p.feed(raw)
    bad = [r for r in p.rows if r[1]]
    print("%s: 带 data-zh 的元素 %d 个，缺属性 %d 个" % (path, len(p.rows), len(bad)))
    for r in bad[:20]:
        print("   MISSING", r[0], r[1], r[2])
    # 属性值内裸双引号（生成后 XML/HTML 结构会错位）：检查形如 data-xx="..." 后紧跟非空白文本
    suspicious = re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"\w', raw)
    print("   属性后紧跟裸字符（引号嵌套可疑）:", len(suspicious), suspicious[:3])
    # 未转义 & (排除 &amp; &nbsp; &quot; &lt; &gt; &#)
    rawamps = re.findall(r'&(?!(?:amp|nbsp|quot|lt|gt|laquo|raquo|#\d+);)[a-zA-Z]{0,8}', raw)
    print("   未转义 & 可疑处:", len(rawamps), rawamps[:5])
