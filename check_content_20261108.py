# -*- coding: utf-8 -*-
"""內容體檢：非中文語種不得含 CJK；不得有裸 &；不得有 ASCII 雙引號遺留。"""
import re, sys
import content_faq_20261108 as CF
import content_sub_20261108 as CS

CJK = re.compile(r'[\u4e00-\u9fff]')
HANGUL = re.compile(r'[\uac00-\ud7af]')
bad = 0


def check(label, d):
    global bad
    if not isinstance(d, dict):
        return
    for lang, v in d.items():
        if lang in ("zh", "href") or not isinstance(v, str):
            continue
        if lang in ("fr", "es", "de", "pt") and CJK.search(v):
            print("CJK 殘留 [%s/%s]: %s" % (label, lang, v[:80])); bad += 1
        if lang == "ko" and CJK.search(v):
            print("韓文含漢字 [%s/%s]: %s" % (label, lang, v[:80])); bad += 1
        if lang == "ja" and HANGUL.search(v):
            print("日文含韓文 [%s/%s]" % (label, lang)); bad += 1
        if re.search(r'&(?!amp;|lt;|gt;|quot;|nbsp;|#)', v):
            print("裸 & [%s/%s]: %s" % (label, lang, v[:80])); bad += 1
        if '"' in v:
            print("ASCII 雙引號 [%s/%s]" % (label, lang)); bad += 1
        if not v.strip():
            print("空值 [%s/%s]" % (label, lang)); bad += 1


def walk(blocks):
    for b in blocks:
        kind, payload = b[0], b[1]
        if kind == "table":
            head, rows = b[1], b[2]
            for th in head:
                check("table-th", th)
            for row in rows:
                assert len(row) == len(head), "表格列數不一致"
                for td in row:
                    check("table-td", td)
        elif kind in ("ul", "ol"):
            for li in payload:
                check("li", li)
        else:
            check(kind, payload)


for name, mod in (("FAQ", CF), ("SUB", CS)):
    for k in ("title", "desc", "crumb", "h1", "tag", "summary"):
        check("%s.%s" % (name, k), mod.META[k])
    walk(mod.BLOCKS)
    print("%s: desc_zh=%d 字  desc_en=%d 字符  blocks=%d"
          % (name, len(mod.META["desc"]["zh"]), len(mod.META["desc"]["en"]), len(mod.BLOCKS)))
print("問題數：", bad)
sys.exit(1 if bad else 0)
