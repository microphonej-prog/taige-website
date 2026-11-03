#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""语言纯净度：ja/ko/fr/es 页正文里不应残留简体中文特征字与别语言字符"""
import re

SLUGS = ["hang-tag-scratch-off-guide.html", "woven-label-special-yarn-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]

# 简体中文高频特征字（繁体/日文不使用或极少使用）
SIMPLIFIED = set("这个们说来时对没开关发从后过还进动产学问题说实际质量标签内为结构层设计选细节页码见让给带纸质贴纸这那种类级谈谈论")
KANA = set("ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ")


def text(s):
    s = re.sub(r"<script.*?</script>", "", s, flags=re.S)
    s = re.sub(r"<style.*?</style>", "", s, flags=re.S)
    return re.sub(r"<[^>]+>", "", s)


bad = 0
for slug in SLUGS:
    for lang in LANGS:
        p = "%s/blog/%s" % (lang, slug)
        s = open(p, encoding="utf-8").read()
        body = s[s.index('<section class="article-body"'):s.index("</main>")]
        t = text(body)
        simp = sorted(set(ch for ch in t if ch in SIMPLIFIED))
        kana = sorted(set(ch for ch in t if ch in KANA))
        note = ""
        if lang != "ja" and kana:
            note += " 含假名%d" % len(kana)
            bad += 1
        if lang in ("fr", "es", "en") and simp:
            note += " 简体特征字=%s" % "".join(simp)
            bad += 1
        print("%-4s %-40s 字数=%4d%s" % (lang, slug, len(t), note))

print("\n问题语言页数:", bad)
