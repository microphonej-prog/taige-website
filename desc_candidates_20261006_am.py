#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""候选 desc 字符串长度试算（2026-10-06 上午批次）。"""
C = {
"A1_zh": "服装零售防盗标签（EAS）指南：讲清防盗报警与 RFID 盘库为何是两套系统，对比声磁硬标、射频软标与墨水标的适用品类与限制，说明 58 kHz 与 8.2 MHz 如何匹配门店防盗门、源标签在工厂端的安装位置，并给出检测距离与验收口径。",
"A1_en": "EAS security tag guide: why anti-theft alarms and RFID counting are two systems, AM hard tags vs RF soft labels vs ink tags, 58 kHz gate matching and factory source tagging.",
"A1_fr": "Guide des étiquettes antivol EAS : alarme et inventaire RFID sont deux systèmes distincts, pastille dure AM, étiquette souple RF et pastille à encre, accord 58 kHz et pose en usine.",
"A1_es": "Guía de etiquetas antirrobo EAS: la alarma y el inventario RFID son dos sistemas, placa dura AM, etiqueta blanda RF y placa de tinta, ajuste a 58 kHz y colocación en fábrica.",
"A2_zh": "成衣染色与水洗工艺下的辅料指南：讲清 60–95 °C 水温、酸碱酶与滚筒摩擦如何破坏吊牌、织唛与洗水标，对比洗前、洗中临时标与洗后挂牌三种时机，并给出六类材质的耐受对照与验收口径。",
"A2_en": "Garment dye and wash trims guide: how 60–95 °C water, pH, enzymes and tumbling damage hang tags and labels, the three attachment timings compared, with a material tolerance table.",
"A2_fr": "Guide des accessoires en teinture en pièce et lavage : effet des 60–95 °C, du pH, des enzymes et du tambour, comparaison des trois moments de pose et tableau de tenue des matières.",
"A2_es": "Guía de accesorios en teñido en prenda y lavado: efecto de 60–95 °C, pH, enzimas y tambor, comparación de los tres momentos de colocación y tabla de tolerancia por material.",
}
for k, v in C.items():
    print("%-8s %3d" % (k, len(v)))
