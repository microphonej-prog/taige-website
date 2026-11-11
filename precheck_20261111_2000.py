# -*- coding: utf-8 -*-
"""生成前预检：八语齐备、无 ASCII 双引号、表格行列数一致、描述长度。"""
import sys
sys.path.insert(0, ".")
import content_plastic_hw_20261111 as A
import content_ind_laundry_20261111 as B

ORDER = ["zh", "en", "fr", "es", "ja", "ko", "de", "pt"]
bad = 0


def walk(d, path):
    global bad
    if isinstance(d, dict):
        if set(d.keys()) - {"href"}:
            miss = [l for l in ORDER if l not in d]
            if miss:
                print("缺语言", path, miss); bad += 1
            for k, v in d.items():
                if k in ORDER:
                    if '"' in v:
                        print("裸双引号", path, k, v[:40]); bad += 1
                    if "&" in v and "&amp;" not in v and "&nbsp;" not in v:
                        print("裸 &", path, k, v[:40]); bad += 1
    elif isinstance(d, list):
        for i, x in enumerate(d):
            walk(x, "%s[%d]" % (path, i))


for mod in (A, B):
    M = mod.META
    for k in ("title", "desc", "crumb", "h1", "tag", "summary"):
        walk(M[k], "%s.%s" % (M["slug"], k))
    for i, b in enumerate(mod.BLOCKS):
        if b[0] == "table":
            head, rows = b[1], b[2]
            for r in rows:
                if len(r) != len(head):
                    print("表格列数不一致", M["slug"], i, len(r), len(head)); bad += 1
            walk(head, "%s.tbl%d.head" % (M["slug"], i))
            walk(rows, "%s.tbl%d.rows" % (M["slug"], i))
        else:
            walk(b[1], "%s.b%d.%s" % (M["slug"], i, b[0]))
    walk(mod.BTN, M["slug"] + ".BTN")
    print(M["slug"], "desc_en=%d desc_zh=%d blocks=%d" % (
        len(M["desc"]["en"]), len(M["desc"]["zh"]), len(mod.BLOCKS)))

print("问题数:", bad)
