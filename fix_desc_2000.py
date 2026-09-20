#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把两篇新文章的 meta description 英文压到 150–160 字符（并略收法/西），再重跑 gen_i18n。"""
import re, os, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

FIX = {
    "blog/garment-gift-box-packaging.html": [
        ("Apparel gift box guide: lid-and-base, magnetic and drawer structures, inserts that hold the garment, wrapping and finishing choices, sizing maths, MOQ, cost and two export shipping models.",
         "Apparel gift box guide: lid-and-base, magnetic and drawer structures, inserts, wrapping and finishing, sizing maths, MOQ, cost and two shipping models."),
        ("Guide des coffrets rigides : structures à couvercle, magnétique et tiroir, calages qui maintiennent le vêtement, habillage et finitions, calcul des dimensions, minimum, coût et deux modèles d'expédition.",
         "Guide des coffrets rigides : structures à couvercle, magnétique et tiroir, calages, habillage et finitions, dimensions, minimum, coût et deux modèles d'expédition."),
        ("Guía de cajas rígidas: estructuras de tapa y base, magnética y de cajón, interiores que sujetan la prenda, forrado y acabados, cálculo de medidas, mínimo, coste y dos modelos de envío.",
         "Guía de cajas rígidas: estructuras de tapa y base, magnética y de cajón, interiores, forrado y acabados, medidas, mínimo, coste y dos modelos de envío."),
    ],
    "blog/poly-bag-cost-guide.html": [
        ("Garment poly bag cost guide: the six cost elements behind one quote, how material, thickness, cutting, printing and volume move the price, six ways to cut cost without cutting quality, and seven questions to ask.",
         "Garment poly bag cost guide: the six cost elements behind one quote, how material, thickness, cutting, printing and volume move the price, and how to cut cost."),
        ("Guide des coûts de sachet : les six postes derrière un devis, l'effet de la matière, de l'épaisseur, de la découpe, de l'impression et du volume sur le prix, six leviers d'économie et sept questions à poser.",
         "Guide des coûts de sachet : les six postes derrière un devis, l'effet de la matière, de l'épaisseur, de la découpe, de l'impression et du volume, six leviers d'économie et sept questions à poser."),
        ("Guía de costes de bolsas: las seis partidas detrás de un presupuesto, el efecto de material, grosor, corte, impresión y volumen en el precio, seis vías de ahorro y siete preguntas antes de pedir.",
         "Guía de costes de bolsas: las seis partidas detrás de un presupuesto, el efecto de material, grosor, corte, impresión y volumen, seis vías de ahorro y siete preguntas antes de pedir."),
    ],
}

for path, pairs in FIX.items():
    s = open(path, encoding="utf-8", newline="").read()
    for old, new in pairs:
        assert old in s, "未找到待替换文本: %s..." % old[:50]
        s = s.replace(old, new, 1)
    open(path, "w", encoding="utf-8", newline="").write(s)
    # 复核：提取 meta 各行长度
    blk = re.search(r'<meta name="description".*?content="', s, re.S).group(0)
    for lang in ("zh", "en", "ja", "ko", "fr", "es"):
        m = re.search(r'data-%s="([^"]*)"' % lang, blk)
        print("  %-30s desc_%s = %d" % (os.path.basename(path), lang, len(m.group(1)) if m else -1))
    mc = re.search(r'content="([^"]*)"', blk)
    print("  %-30s -> 重新生成五语版本" % os.path.basename(path))

TARGETS = list(FIX.keys())
for lang in ["en", "ja", "ko", "fr", "es"]:
    r = subprocess.run([PY, "gen_i18n.py", lang] + TARGETS, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print(r.stdout[-2000:], r.stderr[-2000:])
        raise SystemExit("gen_i18n %s 失败" % lang)
    print("gen_i18n %s ok" % lang)
