# -*- coding: utf-8 -*-
"""2026-10-26 14:00 批次校验：六语属性完整性 / 语言纯度 / 结构 / sitemap"""
import re, io, os
from html.parser import HTMLParser

os.chdir(os.path.dirname(os.path.abspath(__file__)))
SLUGS = ["garment-packaging-cleanliness-contamination-control.html",
         "garment-packaging-budget-allocation.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
LANGFIELDS = ["data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es"]


class AttrCheck(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.bad = []
        self.total = 0
        self.langed = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("meta", "link", "br", "img", "input"):
            return
        d = dict(attrs)
        if not any(k in d for k in LANGFIELDS):
            return
        self.langed += 1
        miss = [k for k in LANGFIELDS if k not in d]
        empty = [k for k in LANGFIELDS if k in d and not str(d[k]).strip()]
        if miss or empty:
            self.bad.append((tag, d.get("class", "")[:20], miss, empty))


print("=" * 70)
for slug in SLUGS:
    for path in ["blog/%s" % slug] + ["%s/blog/%s" % (l, slug) for l in LANGS]:
        s = io.open(path, encoding="utf-8").read()
        if path.startswith("blog/"):
            body = s[s.index('class="article-body"'):s.index("\n</main>")]
        else:
            body = s[s.index('class="article-body"'):s.index("\n</main>")]
        p = AttrCheck()
        p.feed(body)
        flag = "OK " if not p.bad else "FAIL"
        print("%s %-58s 带语言属性元素=%d 缺属性=%d" % (flag, path, p.langed, len(p.bad)))
        for b in p.bad[:5]:
            print("      ", b)

print("=" * 70)
# 引号畸形扫描（data-xx=""）
for slug in SLUGS:
    for path in ["blog/%s" % slug] + ["%s/blog/%s" % (l, slug) for l in LANGS]:
        s = io.open(path, encoding="utf-8").read()
        bad = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
        if bad:
            print("引号畸形", path, len(bad))

# 语言纯度：正文纯文本统计
print("=" * 70)
for slug in SLUGS:
    for lang in LANGS:
        path = "%s/blog/%s" % (lang, slug)
        s = io.open(path, encoding="utf-8").read()
        body = s[s.index('class="article-body"'):s.index("\n</main>")]
        txt = re.sub(r"<[^>]+>", " ", body)
        cjk = len(re.findall(r"[\u4e00-\u9fff]", txt))
        kana = len(re.findall(r"[\u3040-\u30ff]", txt))
        hangul = len(re.findall(r"[\uac00-\ud7af]", txt))
        latin = len(re.findall(r"[A-Za-z]", txt))
        print("%-4s %-58s 汉字=%4d かな=%4d ハングル=%4d 拉丁=%5d"
              % (lang, slug[:56], cjk, kana, hangul, latin))

# 标题渲染检查
print("=" * 70)
for slug in SLUGS:
    for path in ["blog/%s" % slug] + ["%s/blog/%s" % (l, slug) for l in LANGS]:
        s = io.open(path, encoding="utf-8").read()
        t = re.search(r"<title[^>]*>([^<]*)</title>", s).group(1)
        c = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        h = re.search(r"<h1[^>]*>([^<]*)</h1>", s).group(1)
        print("%-52s | %s" % (path, t[:60]))
        print("%-52s | canon=%s" % ("", c))
        if not h.strip():
            print("     !! h1 空")
print("=" * 70)
