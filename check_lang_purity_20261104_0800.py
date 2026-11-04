#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""语言纯净度：ja/ko/fr/es 页正文不残留简体特征字/别语言字符；zh 页确认已繁体化。"""
import re
from opencc import OpenCC

SLUGS = ["apparel-trims-nearshoring-sourcing-guide.html",
         "apparel-unboxing-packaging-design-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
SIMPLIFIED = set("这个们说来时对没开关发从后过还进动产学问题实际质量标签内为结构层设计选细节页码见让给带纸质贴这两种类级谈")
KANA = set("ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんァアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワン")
T2S = OpenCC("t2s")
bad = 0


def text(s):
    s = re.sub(r"<script.*?</script>", "", s, flags=re.S)
    s = re.sub(r"<style.*?</style>", "", s, flags=re.S)
    return re.sub(r"<[^>]+>", "", s)


for slug in SLUGS:
    # zh 首页：t2s 后应与原文一致（说明已全部繁体）
    s = open("blog/" + slug, encoding="utf-8").read()
    body = s[s.index('<section class="article-body"'):s.index("</main>")]
    t = text(body)
    diff = [c for a, c in zip(t, T2S.convert(t)) if a != c]
    print("zh   %-46s 字数=%4d 非繁体字符=%d %s" % (slug, len(t), len(diff), "".join(sorted(set(diff))[:12])))
    for lang in LANGS:
        s = open("%s/blog/%s" % (lang, slug), encoding="utf-8").read()
        body = s[s.index('<section class="article-body"'):s.index("</main>")]
        t = text(body)
        simp = sorted(set(ch for ch in t if ch in SIMPLIFIED))
        kana = sorted(set(ch for ch in t if ch in KANA))
        cjk = sorted(set(ch for ch in t if "\u4e00" <= ch <= "\u9fff"))
        hangul = sorted(set(ch for ch in t if "\uac00" <= ch <= "\ud7a3"))
        note = ""
        if lang != "ja" and kana:
            note += " 含假名"; bad += 1
        if lang in ("fr", "es", "en") and (simp or cjk):
            note += " 汉字残留=%s" % "".join((simp + cjk)[:12]); bad += 1
        if lang != "ko" and hangul:
            note += " 韩文残留"; bad += 1
        if lang == "ko" and not hangul:
            note += " !!无韩文"; bad += 1
        if lang == "ja" and not kana:
            note += " !!无假名"; bad += 1
        print("%-4s %-46s 字数=%4d%s" % (lang, slug, len(t), note))

print("\n问题语言页数:", bad)
