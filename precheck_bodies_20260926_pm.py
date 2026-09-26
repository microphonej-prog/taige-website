#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-26 下午批次：正文源文件预检 + 生成后校验（六语，含 ja/ko）。

检查项：
 0) 正文源文件：裸 &、空 data-*、属性后裸字符、双引号奇偶
 1) 中文页正文六语属性完整性 + 默认文本与 data-zh 一致性（重建 innerHTML 比对）
 2) 五语生成页：data-* 残留、正文汉字残留、desc 长度、title
 3) sitemap：新 URL 齐全、blog/index lastmod
 4) 列表页卡片命中与前 3 张顺序
"""
import re, sys, json, os
from html.parser import HTMLParser

NEW = ["blog/trim-third-party-testing-guide.html",
       "blog/sample-room-trims-checklist.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
BODIES = ["blog/_body_testlab.html", "blog/_body_samproom.html"]
VOID = {"br", "img", "meta", "link", "input", "hr", "source"}

print("== 0) 正文源文件预检 ==")
bad = 0
for f in BODIES:
    s = open(f, encoding="utf-8").read()
    bare_amp = [m.start() for m in re.finditer(r'&(?!amp;|nbsp;|quot;|#\d+;|lt;|gt;)', s)]
    empty_attr = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    attr_tail = re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)
    quotes_odd = s.count('"') % 2
    print("  %s: 长度 %d 字节；裸 & %d；空 data-* %d；属性后裸字符 %d；双引号奇偶 %d"
          % (f, len(s.encode("utf-8")), len(bare_amp), len(empty_attr), len(attr_tail), quotes_odd))
    for i in bare_amp[:5]:
        print("    裸 & 上下文: ...%s..." % s[max(0, i - 60):i + 60].replace("\n", " "))
    for t in attr_tail[:5]:
        print("    属性后裸字符: %s" % t[:90])
    bad += len(bare_amp) + len(empty_attr) + len(attr_tail) + quotes_odd


class Collector(HTMLParser):
    """收集 article-body 内的标签属性，并重建带 data-zh 元素的 innerHTML。"""

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.tags = []
        self.stack = []
        self.depth = 0
        self.results = []   # (tag, data_zh, rebuilt_inner)

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        if tag == "section" and d.get("class", "").startswith("article-body"):
            self.in_body = True
            self.stack = []
            return
        if not self.in_body:
            return
        self.tags.append((tag, d))
        for e in self.stack:
            if e["dzh"] is not None:
                e["buf"].append("<%s>" % tag)
        self.stack.append({"tag": tag, "dzh": d.get("data-zh"), "buf": []})
        if tag in VOID:
            e = self.stack.pop()
            if e["dzh"] is not None:
                self.results.append((tag, e["dzh"], "".join(e["buf"])))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_data(self, data):
        if not self.in_body:
            return
        for e in self.stack:
            if e["dzh"] is not None:
                e["buf"].append(data)

    def handle_entityref(self, name):
        if self.in_body:
            for e in self.stack:
                if e["dzh"] is not None:
                    e["buf"].append("&%s;" % name)

    def handle_charref(self, name):
        if self.in_body:
            for e in self.stack:
                if e["dzh"] is not None:
                    e["buf"].append("&#%s;" % name)

    def _close(self, tag):
        while self.stack:
            e = self.stack.pop()
            if e["dzh"] is not None:
                self.results.append((e["tag"], e["dzh"], "".join(e["buf"])))
            if e["tag"] == tag:
                return True
        return False

    def handle_endtag(self, tag):
        if not self.in_body:
            return
        if tag == "section":
            while self.stack:
                e = self.stack.pop()
                if e["dzh"] is not None:
                    self.results.append((e["tag"], e["dzh"], "".join(e["buf"])))
            self.in_body = False
            return
        self._close(tag)
        for e in self.stack:
            if e["dzh"] is not None:
                e["buf"].append("</%s>" % tag)


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


print("== 1) 中文页正文六语属性完整性 + data-zh 与默认文本一致性 ==")
total_missing = 0
total_mismatch = 0
for f in NEW:
    if not os.path.exists(f):
        print("  %s 尚未生成，跳过" % f)
        continue
    s = open(f, encoding="utf-8").read()
    p = Collector()
    p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in ("data-en", "data-ja", "data-ko", "data-fr", "data-es"):
            if not a.get(need, "").strip():
                missing.append((t, need))
    total_missing += len(missing)

    mism = []
    for t, dzh_val, inner in p.results:
        if norm(dzh_val) != norm(inner):
            mism.append((t, dzh_val[:40], norm(inner)[:40]))
    total_mismatch += len(mism)

    print("  %s" % f)
    print("    article-body 内标签 %d 个，带 data-zh 的 %d 个；缺 en/ja/ko/fr/es 的 %d 个 %s"
          % (len(p.tags), len(dzh), len(missing), missing[:6]))
    print("    data-zh 与默认文本不一致 %d 处 %s" % (len(mism), mism[:4]))
    print("    引号畸形=%d  属性后裸字符=%d  裸 &=%d"
          % (len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)),
             len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s))))
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    print("    JSON-LD %d 处合法；静态 title=%s"
          % (len(lds), re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1)[:56]))

print("== 2) 五语生成页检查（残留 / 汉字 / desc 长度） ==")
for f in NEW:
    slug = os.path.basename(f)
    for lang in LANGS:
        path = os.path.join(lang, "blog", slug)
        if not os.path.exists(path):
            print("  %-66s 缺失" % path)
            continue
        s = open(path, encoding="utf-8").read()
        m0 = re.search(r'<section class="article-body">', s)
        body = s[m0.end():]
        body = body[:re.search(r"</section>", body).start()]
        cjk = len(re.findall(r"[\u4e00-\u9fff]", re.sub(r"<script.*?</script>", "", body, flags=re.S)))
        q = Collector()
        q.feed(s)
        residue = sum(1 for t, a in q.tags if any(k.startswith("data-") for k in a))
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
        print("  %-56s data-*=%-2d 正文汉字=%-4d desc=%-4d title=%s"
              % (lang + "/blog/" + slug, residue, cjk, len(desc.group(1)) if desc else -1, title[:46]))

print("== 3) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
n = 0
for f in NEW:
    if not os.path.exists(f):
        print("  尚未生成，跳过：%s" % f)
        continue
    slug = os.path.basename(f)
    for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS]:
        u = "https://taigetag.com/%s%s" % (pre, slug)
        assert "<loc>%s</loc>" % u in sm, u
        n += 1
print("  新 URL %d / 预期 %d 个；<loc> 总数=%d；blog/index lastmod 2026-09-26 命中 %d 处"
      % (n, 6 * len(NEW), sm.count("<loc>"),
         len(re.findall(r"<loc>https://taigetag\.com/(?:[a-z]{2}/)?blog/index\.html</loc>\r?\n\s*<lastmod>2026-09-26", sm))))

print("== 4) 列表页卡片 ==")
PAGES = ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS] \
    if all(os.path.exists(f) for f in NEW) else []
if not PAGES:
    print("  尚未生成，跳过")
for p in PAGES:
    s = open(p, encoding="utf-8").read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    grid = s.index('<div class="post-grid">')
    order = re.findall(r'<article class="post-card">.*?href="([^"]+\.html)"', s[grid:], re.S)[:3]
    print("  %-24s 命中=%s 前3张=%s" % (p, hit, order))

print("\n结论: 正文缺语种属性总数 = %d；data-zh 与默认文本不一致 = %d；源文件预检问题 = %d"
      % (total_missing, total_mismatch, bad))
raise SystemExit(1 if (total_missing or total_mismatch or bad) else 0)
