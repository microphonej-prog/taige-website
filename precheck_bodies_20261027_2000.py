# -*- coding: utf-8 -*-
"""正文预检：六语属性完整性（HTMLParser，避免正则被属性内 > 截断）、裸引号、裸 & 检查"""
import re, sys, os
from html.parser import HTMLParser

os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILES = ["blog/_body_collab.html", "blog/_body_offshore.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = 0
        self.stack = []
        self.elems = 0
        self.missing = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "section" and d.get("class") == "article-body":
            self.in_body = 1
        if self.in_body:
            self.elems += 1
            keys = [k for k in d if k.startswith("data-")]
            if keys:
                miss = [l for l in LANGS if "data-%s" % l not in d]
                if miss:
                    self.missing.append((tag, d.get("data-zh", "")[:30], miss))
                for k in keys:
                    v = d[k] or ""
                    if v.strip() == "":
                        self.errors.append((tag, k, "空值"))
            if tag not in ("br", "img", "meta", "link", "input", "hr"):
                self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.in_body:
            if tag == "section":
                if self.stack and self.stack[-1] == "section":
                    self.stack.pop()
                self.in_body = 0
                return
            if self.stack and self.stack[-1] == tag:
                self.stack.pop()
            else:
                self.errors.append((tag, "标签不匹配", str(self.stack[-3:])))


for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = P()
    p.feed(s)
    zh_chars = len(re.findall(r"[\u4e00-\u9fff]", "".join(re.findall(r'data-zh="([^"]*)"', s))))
    print("=== %s" % f)
    print("  元素数=%d  缺语言=%d  其他错误=%d  data-zh 汉字数=%d"
          % (p.elems, len(p.missing), len(p.errors), zh_chars))
    for m in p.missing[:10]:
        print("   ! 缺语言", m)
    for e in p.errors[:10]:
        print("   ! ", e)
    # 裸 & （排除合法实体）
    bad_amp = [m.start() for m in re.finditer(r"&(?!(amp|nbsp|quot|lt|gt|#\d+);)", s)]
    print("  裸 & 个数=%d" % len(bad_amp))
    # 属性值内出现裸双引号：形如 data-xx="...""  或 =="""
    print("  疑似引号嵌套=%d" % len(re.findall(r'data-[a-z]+=""', s)))
    # 表格/列表结构计数
    print("  h2=%d  p=%d  table=%d  li=%d  callout=%d"
          % (s.count("<h2"), s.count("<p "), s.count("<table>"), s.count("<li "), s.count('class="callout"')))
