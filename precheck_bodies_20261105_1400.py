#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""拼接 2026-11-05 14:00 批次正文分片，并做四/六语属性完整性检查"""
import os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

PAIRS = [
    ("blog/_body_nordic.html", ["blog/_body_nordic_p1.html", "blog/_body_nordic_p2.html", "blog/_body_nordic_p3.html"]),
    ("blog/_body_lowtemp.html", ["blog/_body_lowtemp_p1.html", "blog/_body_lowtemp_p2.html", "blog/_body_lowtemp_p3.html"]),
]

for out, parts in PAIRS:
    s = "".join(open(p, encoding="utf-8").read() for p in parts)
    open(out, "w", encoding="utf-8", newline="").write(s)
    print("拼接 %s -> %d KB" % (out, len(s.encode("utf-8")) // 1024))

LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
CJK = re.compile(r"[\u4e00-\u9fff]")
KANA = re.compile(r"[\u3040-\u30ff]")
HANGUL = re.compile(r"[\uac00-\ud7af]")


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.nodes = []
        self.cur = None

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if any(k.startswith("data-") for k in d):
            self.nodes.append((tag, d, self.getpos()[0]))
        if tag not in ("br", "img", "meta", "link", "input", "hr"):
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()


ok = True
for out, _ in PAIRS:
    s = open(out, encoding="utf-8").read()
    p = P()
    p.feed(s)
    miss = {}
    empty = {}
    cjk = []
    kor = []
    jap = []
    for tag, d, line in p.nodes:
        if "data-zh" not in d:
            continue
        for l in LANGS:
            k = "data-" + l
            if k not in d:
                miss.setdefault(l, []).append(line)
            elif not (d[k] or "").strip():
                empty.setdefault(l, []).append(line)
        for l in ("en", "fr", "es", "ko"):
            v = d.get("data-" + l, "")
            if CJK.search(v):
                cjk.append((line, l, CJK.search(v).group(0)))
        kv = d.get("data-ko", "")
        if kv and not HANGUL.search(kv):
            kor.append(line)
        jv = d.get("data-ja", "")
        if jv and not KANA.search(jv) and not re.search(r"[ァ-ヴ]", jv):
            jap.append((line, jv[:40]))
    print("\n== %s  带 data-* 元素 %d 个" % (out, len(p.nodes)))
    print("   缺属性: %s" % (miss if miss else "无"))
    print("   空值: %s" % (empty if empty else "无"))
    print("   en/fr/es/ko 含汉字: %s" % (cjk[:10] if cjk else "无"))
    print("   ko 无韩文: %s" % (kor[:10] if kor else "无"))
    print("   ja 无假名(疑似中文): %s" % (jap[:10] if jap else "无"))
    if miss or empty or cjk or kor:
        ok = False

sys.exit(0 if ok else 1)
