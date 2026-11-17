# -*- coding: utf-8 -*-
"""发布前自检 v2：属性齐全 / 可见中文残留 / 卡片 / hreflang / noindex
允许的中文残留：日语法令专名（家庭用品品質表示法）、站点既有页脚的「微信/在線」、语言按钮名。
ja 页不查 CJK（假名与汉字同属 CJK 区）。"""
import re
from html.parser import HTMLParser

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
SLUGS = ["hang-tag-back-printing-guide", "apparel-trims-chargeback-guide"]
DIRS = {"zh": "blog", "en": "en/blog", "fr": "fr/blog", "es": "es/blog", "ja": "ja/blog", "ko": "ko/blog"}
CJK = re.compile(r"[\u4e00-\u9fff]")
ALLOW = ("家庭用品品質表示法", "微信", "在線", "泰閣")


class AttrScan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.total = 0
        self.missing = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "data-zh" in d:
            self.total += 1
            lack = [l for l in LANGS if "data-%s" % l not in d]
            if lack:
                self.missing.append((tag, lack))


def visible_text(s):
    s = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", s, flags=re.S)
    return [m.group(1).strip() for m in re.finditer(r">([^<>]+)<", s) if m.group(1).strip()]


ok = True
for slug in SLUGS:
    s = open("%s/%s.html" % (DIRS["zh"], slug), encoding="utf-8").read()
    p = AttrScan()
    p.feed(s)
    print("%-32s 属性元素 %d，缺语言 %d" % (slug, p.total, len(p.missing)))
    if p.missing:
        ok = False
        print("   ", p.missing[:5])
    for lang in ["en", "fr", "es", "ko"]:
        f = "%s/%s.html" % (DIRS[lang], slug)
        t = open(f, encoding="utf-8").read()
        bad = [x for x in visible_text(t) if CJK.search(x) and not any(a in x for a in ALLOW)]
        hl = len(re.findall(r"hreflang=", t))
        noidx = "noindex" in t
        card = slug + ".html" in open("%s/index.html" % DIRS[lang], encoding="utf-8").read()
        flag = "" if (not bad and hl == 7 and not noidx and card) else "  <-- 检查"
        print("   %-3s 中文残留 %d | hreflang %d | noindex %s | 卡片 %s%s"
              % (lang, len(bad), hl, noidx, card, flag))
        if bad:
            print("      ", bad[:3])
        if bad or hl != 7 or noidx or not card:
            ok = False
    f = "%s/%s.html" % (DIRS["ja"], slug)
    t = open(f, encoding="utf-8").read()
    hl = len(re.findall(r"hreflang=", t))
    card = slug + ".html" in open("%s/index.html" % DIRS["ja"], encoding="utf-8").read()
    print("   ja  hreflang %d | noindex %s | 卡片 %s" % (hl, "noindex" in t, card))
    if hl != 7 or "noindex" in t or not card:
        ok = False

print("\n总体:", "PASS" if ok else "FAIL")
