#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修正版：允许某语言文件不含其它语言 desc（ja/ko 文件只含自身），逐步替换并汇总"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

OLD = {
    "en": "Plus-size womenswear trims: size labels up to 5XL, reinforced waistband and side-seam care labels, stretch-fabric care marks, hang tag size charts and larger bags.",
    "fr": "Guide des accessoires grande taille : étiquettes de taille jusqu'au 5XL, ceinture et couture latérale renforcées, entretien des tissus extensibles, mesures sur l'étiquette suspendue et emballages plus grands.",
    "es": "Guía de accesorios de talla grande: etiquetas de talla hasta la 5XL, cinturilla y costura lateral reforzadas, cuidado de tejidos elásticos, medidas en la etiqueta colgante y embalajes mayores.",
}
NEW = {
    "en": "Plus-size womenswear trims: size labels to 5XL, reinforced waistband and side-seam care labels, stretch care marks, hang tag size charts and larger bags.",
    "fr": "Guide des accessoires grande taille : étiquettes jusqu'au 5XL, ceinture et couture latérale renforcées, entretien des tissus extensibles et emballages plus grands.",
    "es": "Guía de accesorios de talla grande: etiquetas hasta la 5XL, cinturilla y costura lateral reforzadas, cuidado de tejidos elásticos y embalajes mayores.",
}

SLUG = "plus-size-womenswear-trims-guide.html"
FILES = ["blog/%s" % SLUG] + ["%s/blog/%s" % (l, SLUG) for l in ("en", "ja", "ko", "fr", "es")]

total = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    hits = 0
    for k in ("en", "fr", "es"):
        if OLD[k] in s:
            s = s.replace(OLD[k], NEW[k])
            hits += 1
    if hits:
        open(f, "w", encoding="utf-8", newline="").write(s)
    print("%-52s 替换 %d 处" % (f, hits))
    total += hits

# 残留检查
resid = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    for k in ("en", "fr", "es"):
        if OLD[k] in s:
            print("!! 仍残留旧 desc (%s): %s" % (k, f))
            resid += 1
print("总替换 %d 处，残留 %d 处" % (total, resid))
