#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

REPL = {
 "bridal-eveningwear-trims-guide.html": [
   ("Bridal and eveningwear trims guide: how to choose satin neck labels, care labels for dry-clean-only and beaded styles, foil tags, ribbon hardware and gift boxes.",
    "Bridal and eveningwear trims guide: satin neck labels, care labels for dry-clean-only and beaded styles, foil hang tags, ribbons and gift box packaging."),
 ],
 "clothing-label-compliance-switzerland.html": [
   ("Switzerland clothing label rules: Swiss fibre labelling compared with the EU, German and French wording, care symbols, the importer as responsible party, GS1 760 barcodes.",
    "Switzerland clothing label requirements: fibre content, German and French wording, care symbols, the importer as responsible party and GS1 760 barcodes."),
 ],
}

LANGS = ["", "en", "ja", "ko", "fr", "es"]
for slug, pairs in REPL.items():
    for old, new in pairs:
        print("new len = %d" % len(new))
        assert 150 <= len(new) <= 160, "长度不合规: %d" % len(new)
        for l in LANGS:
            p = os.path.join(l, "blog", slug) if l else os.path.join("blog", slug)
            s = open(p, encoding="utf-8").read()
            n = s.count(old)
            if n == 0:
                # 数据里可能是已转繁/被 gen_i18n 处理的版本，直接报出来
                print("  !! %s 未找到旧串" % p)
                continue
            s = s.replace(old, new)
            open(p, "w", encoding="utf-8", newline="").write(s)
            print("  %s 替换 %d 处" % (p, n))
print("done")
