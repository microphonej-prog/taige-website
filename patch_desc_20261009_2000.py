#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-09 晚间批次：修正第一篇 desc 长度（desc_en 163 -> <=160，fr/es 收敛到 ~150）并同步到已生成的六语文件"""
import os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

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

for k in ("en", "fr", "es"):
    print("%s: %d -> %d 字符" % (k, len(OLD[k]), len(NEW[k])))

SLUG = "plus-size-womenswear-trims-guide.html"
FILES = ["blog/%s" % SLUG] + ["%s/blog/%s" % (l, SLUG) for l in ("en", "ja", "ko", "fr", "es")]

for f in FILES:
    s = open(f, encoding="utf-8").read()
    hits = 0
    for k in ("en", "fr", "es"):
        if OLD[k] in s:
            s = s.replace(OLD[k], NEW[k])
            hits += 1
    assert hits > 0, "未找到待替换 desc: %s" % f
    open(f, "w", encoding="utf-8", newline="").write(s)
    print("已更新 %s（%d 处）" % (f, hits))
