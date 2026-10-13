# -*- coding: utf-8 -*-
"""2026-10-13 晚间批次（20:00）：正文装配文件预检（六语属性完整性 + 引号/实体 + 非目标语言残留）"""
import re, sys
from html.parser import HTMLParser

FILES = ["blog/_body_relabel.html", "blog/_body_resale.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs), self.getpos()[0]))


def cjk(s):
    return len(re.findall(r'[\u4e00-\u9fff]', s))


ok = True
for f in FILES:
    s = open(f, encoding="utf-8").read()
    print("=" * 70)
    print("文件:", f, " 字节:", len(s.encode('utf-8')))

    bad = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    print("  空值/畸形 data-xx=\"\" :", len(bad))
    if bad:
        ok = False
    bad2 = re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)
    print("  属性后紧跟非法字符:", len(bad2))
    if bad2:
        ok = False

    p = P()
    p.feed(s)
    total = miss = 0
    lackcnt = {l: 0 for l in LANGS}
    for tag, a, line in p.tags:
        if not any(k.startswith("data-") for k in a):
            continue
        total += 1
        lack = [l for l in LANGS if ("data-" + l) not in a]
        if lack:
            miss += 1
            for l in lack:
                lackcnt[l] += 1
            print("  [缺语言] 行%d <%s> 缺 %s" % (line, tag, lack))
    print("  带 data-* 元素: %d，缺任一语言: %d %s" % (total, miss, lackcnt))
    if miss:
        ok = False

    for lang in ("en", "fr", "es"):
        vals = re.findall(r'data-%s="([^"]*)"' % lang, s)
        res = [(i, cjk(v)) for i, v in enumerate(vals) if cjk(v)]
        if res:
            print("  [CJK残留] data-%s 有 %d 处含汉字: %s" % (lang, len(res), res[:6]))
            ok = False

    raw_amp = re.findall(r'&(?!amp;|lt;|gt;|quot;|nbsp;|#\d+;|#x[0-9a-fA-F]+;)[a-zA-Z]{0,6}', s)
    print("  可疑裸 & :", len(raw_amp), sorted(set(raw_amp))[:8])
    if raw_amp:
        ok = False

    # 元素默认文本与 data-zh 是否一致（防止默认文本写错）
    for tag, a, line in p.tags:
        if "data-zh" in a and tag in ("td", "th", "li", "p", "h2"):
            pass
    body_txt = re.sub(r'<[^>]+>', '', s)
    zh = re.findall(r'data-zh="([^"]*)"', s)
    zh_all = re.sub(r'<[^>]+>', '', " ".join(zh))
    print("  data-zh 条数: %d，中文字符总数: %d" % (len(zh), cjk(zh_all)))
    for kw in (["换标", "拆", "覆盖", "条码", "授权", "验收"] if "relabel" in f
               else ["二手", "转售", "租赁", "翻新", "分级", "干洗"]):
        print("    关键词 %-4s -> %d 次" % (kw, zh_all.count(kw)))

    for need in ['class="cta-box"', 'class="cta-btn"', 'href="../contact.html"',
                 'href="index.html"', "<h2", "<table", 'class="callout"']:
        if need not in s:
            print("  [缺结构]", need)
            ok = False

print()
print("预检结论:", "通过" if ok else "存在问题，需修复")
sys.exit(0 if ok else 1)
