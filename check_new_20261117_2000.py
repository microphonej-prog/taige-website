# -*- coding: utf-8 -*-
"""发布前自检：属性齐全 / 可见中文残留 / 卡片 / hreflang / noindex"""
import re
from html.parser import HTMLParser

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
SLUGS = ["hang-tag-back-printing-guide", "apparel-trims-chargeback-guide"]
DIRS = {"zh": "blog", "en": "en/blog", "fr": "fr/blog", "es": "es/blog", "ja": "ja/blog", "ko": "ko/blog"}
CJK = re.compile(r"[\u4e00-\u9fff]")


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
    parts = [m.group(1) for m in re.finditer(r">([^<>]+)<", s)]
    return [p.strip() for p in parts if p.strip()]


ok = True
for slug in SLUGS:
    src = "%s/%s.html" % (DIRS["zh"], slug)
    s = open(src, encoding="utf-8").read()
    p = AttrScan()
    p.feed(s)
    print("%-32s 属性元素 %d，缺语言 %d" % (slug, p.total, len(p.missing)))
    if p.missing:
        ok = False
        print("   ", p.missing[:5])
    for lang in LANGS[1:]:
        f = "%s/%s.html" % (DIRS[lang], slug)
        t = open(f, encoding="utf-8").read()
        bad = [x for x in visible_text(t) if CJK.search(x)]
        # 允许：语言切换按钮的语言名、团队人名
        bad = [x for x in bad if not re.fullmatch(r"(繁體中文|日本語|한국어|Français|Español|English|中文)", x)]
        hl = len(re.findall(r'hreflang=', t))
        noidx = "noindex" in t
        card = slug + ".html" in open("%s/index.html" % DIRS[lang], encoding="utf-8").read()
        flag = "" if (not bad and hl == 7 and not noidx and card) else "  <-- 检查"
        print("   %-3s 可见中文残留 %d | hreflang %d | noindex %s | 列表卡片 %s%s"
              % (lang, len(bad), hl, noidx, card, flag))
        if bad:
            print("      ", bad[:3])
        if bad or hl != 7 or noidx or not card:
            ok = False

print("\n总体:", "PASS" if ok else "FAIL")
