#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""desc 长度候选体检（英文目标 150-160 字符）—— 2026-09-23 晚间批次"""
CAND = {
 "socks_en_a": "Sock and knitwear trims guide: woven or tagless heat-transfer labels, size labelling by foot length, sock card sizing and pair packaging.",
 "socks_en_b": "Sock and knitwear trims guide: woven or tagless heat-transfer labels, sizing by foot length, sock card formats, pair packaging and five checks.",
 "socks_en_c": "Sock trims guide: choosing woven or tagless heat-transfer labels, sizing by foot length, sock card formats, pair packaging and acceptance checks.",
 "hats_en_a": "Hat, scarf and glove trims guide: fibre content labelling, head and palm sizing, sewing long labels and three-piece gift box ratios for buyers.",
 "hats_en_b": "Hat, scarf and glove trims guide: fibre content labelling, head and palm sizing, sewing long labels, tag fixings and three-piece gift box ratios.",
 "socks_fr_a": "Guide accessoires chaussettes : label tissé ou transfert sans couture, tailles par longueur de pied, format de carte et emballage par paire.",
 "socks_es_a": "Guía de accesorios para calcetines: etiqueta tejida o transferible sin costura, tallas por longitud de pie, formato de tarjeta y controles.",
 "hats_fr_a": "Guide accessoires bonnets, écharpes et gants : composition des fibres, tailles de tête et de main, pose des labels longs et coffrets cadeaux.",
 "hats_es_a": "Guía de accesorios para gorros, bufandas y guantes: composición de fibras, tallas de contorno, etiquetas largas y cajas de regalo.",
}
for k in sorted(CAND):
    print("%-14s %3d  %s" % (k, len(CAND[k]), CAND[k]))
