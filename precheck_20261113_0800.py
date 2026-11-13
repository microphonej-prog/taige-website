# -*- coding: utf-8 -*-
"""上一步：內容模組自檢（屬性齊全、desc 長度、本地化閘門預演）"""
import importlib.util, sys
import content_3pl_20261113 as C1
import content_acrylic_20261113 as C2

spec = importlib.util.spec_from_file_location("chk", r"F:/hermes/scripts/check_localization.py")
chk = importlib.util.module_from_spec(spec); spec.loader.exec_module(chk)

ORDER = ["zh", "en", "fr", "es", "ja", "ko"]
PORT = [("3pl", C1.META, C1.BLOCKS), ("acrylic", C2.META, C2.BLOCKS)]

for name, META, BLOCKS in PORT:
    print("=" * 70)
    print(name, META["slug"])
    for k in ("title", "desc", "crumb", "h1", "tag", "summary"):
        miss = [l for l in ORDER if l not in META[k] or not META[k][l].strip()]
        print("  %-8s 缺語言: %s" % (k, miss or "無"))
    print("  desc 長度: " + ", ".join("%s=%d" % (l, len(META["desc"][l])) for l in ORDER))
    bad = []
    for i, b in enumerate(BLOCKS):
        items = []
        if b[0] == "table":
            items = b[1] + [c for row in b[2] for c in row]
        elif b[0] in ("ul", "ol"):
            items = b[1]
        else:
            items = [b[1]]
        for it in items:
            miss = [l for l in ORDER if l not in it or str(it[l]).strip() == ""]
            if miss:
                bad.append((i, b[0], miss))
    print("  區塊缺語言: %s" % (bad or "無"))

    # 閘門預演：把每個語種的 data 值拼起來，用同一套正則分析
    for lang in ("fr", "es", "ja", "ko"):
        vals = []
        for b in BLOCKS:
            items = []
            if b[0] == "table":
                items = b[1] + [c for row in b[2] for c in row]
            elif b[0] in ("ul", "ol"):
                items = b[1]
            else:
                items = [b[1]]
            vals += [it[lang] for it in items]
        vals += [META["title"][lang], META["desc"][lang], META["h1"][lang], META["crumb"][lang], META["summary"][lang]]
        text = " ".join(vals)
        chars = len("".join(text.split()))
        hits = {c: len(__import__("re").findall(rx, text, __import__("re").I)) for c, rx in chk.PATTERNS[lang].items()}
        total = sum(hits.values())
        need = 1 if chars < 800 else max(3, chars // 800)
        ok = all(v >= 1 for v in hits.values()) and total >= need
        print("  %s 預演 %s 正文%d字 法規%d/標籤%d/計量%d 合計%d(需≥%d)" % (
            "PASS" if ok else "FAIL", lang, chars, hits["法规"], hits["标签"], hits["计量"], total, need))
