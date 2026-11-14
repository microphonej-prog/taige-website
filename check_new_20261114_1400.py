# -*- coding: utf-8 -*-
"""新文章体检：属性覆盖、可见文本= data-zh、简化字残留、裸引号截断。"""
import re
import sys
from html.parser import HTMLParser

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
SIMPLIFIED = set("装机码规标测试带价网厂务业版权发东广应导读简这说个为种样门问题户头条级类")


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.elems = []          # (tag, attrs dict, text)
        self.cur = []

    def handle_starttag(self, tag, attrs):
        if tag in ("meta", "link", "br", "img", "input", "hr"):
            self.elems.append((tag, dict(attrs), ""))
            return
        self.stack.append((tag, dict(attrs), []))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                t, a, txt = self.stack.pop(i)
                self.elems.append((t, a, "".join(txt)))
                # 把尾部未闭合的子节点文本上抛
                while len(self.stack) > i:
                    t2, a2, txt2 = self.stack.pop()
                    self.elems.append((t2, a2, "".join(txt2)))
                return

    def handle_data(self, data):
        if self.stack:
            self.stack[-1][2].append(data)


for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    p = P()
    p.feed(s)
    # 1) 每语种覆盖
    print("==", f)
    for l in LANGS:
        n = len(re.findall(r'data-%s="' % l, s))
        print("   data-%s: %d" % (l, n))
    # 2) 元素缺失
    miss = []
    for tag, a, txt in p.elems:
        if "data-zh" in a:
            lack = [l for l in LANGS if "data-%s" % l not in a]
            if lack:
                miss.append((tag, a.get("data-zh", "")[:30], lack))
    print("   缺语种属性的元素数:", len(miss), miss[:5])
    # 3) 可见文本 vs data-zh（只查无子标签的元素）
    bad = []
    for tag, a, txt in p.elems:
        t = re.sub(r"\s+", " ", txt).strip()
        if "data-zh" in a and t and t != re.sub(r"\s+", " ", a["data-zh"]).strip():
            bad.append((tag, t[:40], a["data-zh"][:40]))
    print("   可见文本≠data-zh 的元素数:", len(bad), bad[:5])
    # 4) 局部简化字残留（只看 data-zh 与可见文本）
    simp = [c for tag, a, txt in p.elems for c in (a.get("data-zh", "") + txt) if c in SIMPLIFIED]
    print("   疑似简化字残留:", len(simp), "".join(sorted(set(simp)))[:60])
    # 5) 属性被裸引号截断（出现 data-en="" 或标签名进正文）
    print("   data-xx=\"\" 空值:", len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)))
    print("   &#x27; 转义引号出现在 href:", len(re.findall(r"href=&#x27;", s)))
    print("   noindex:", s.count("noindex"))
