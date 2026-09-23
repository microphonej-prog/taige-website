#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-23 下午批次：desc 长度微调（英文目标 150-160 字符，中文 80-120 字）
同步更新根目录页 data-* 与 en/ja/ko/fr/es 五语页的 content。
"""
import os, re, sys

LANGS = ["en", "ja", "ko", "fr", "es"]
ARTICLES = [
    dict(slug="pet-apparel-trims-guide.html",
         desc_zh="宠物服装辅料定制指南：讲清犬猫尺码标怎么写、主唛材质如何按绒面与贴身款选择、洗水标要标哪些内容、反光与限用物质要求，附挂卡与自封袋包装方案和可直接询价的规格表。来自东莞泰阁包装。",
         desc_en="Pet apparel trims guide: size labels for dogs and cats, neck label materials, care label content, reflective trim, restricted substances and packaging.",
         desc_ja="ペットウェアの副資材ガイド。犬猫のサイズラベル、主ラベルの素材、洗濯表示ラベルの内容、反射テープ、規制物質、ハンガーカードとチャック袋の包装をまとめました。東莞泰閣包装。",
         desc_ko="펫웨어 부자재 가이드. 견종·고양이 사이즈 라벨, 주 라벨 소재, 세탁 표시 라벨 내용, 반사 테이프, 규제 물질, 행 카드와 지퍼백 포장을 정리했습니다. 둥관 TAGE 패키징.",
         desc_fr="Guide accessoires vêtements d'animaux : labels de taille chien et chat, matières des labels, étiquettes d'entretien, bandes réfléchissantes et emballage.",
         desc_es="Guía de accesorios para ropa de mascotas: etiquetas de talla para perros y gatos, materiales, etiquetas de cuidado y tiras reflectantes para el comprador."),
    dict(slug="loungewear-pajama-trims-guide.html",
         desc_zh="家居服与睡衣辅料定制指南：绒类面料的主唛怎么选才不沾毛、洗水标与尺码标在套装上怎么配、吊牌与礼盒包装怎么设计，附可直接询价的规格表与五步验收清单。来自东莞泰阁包装。",
         desc_en="Loungewear and sleepwear trims guide: fleece-friendly neck labels, care and size labels for sets, hang tags, gift box packaging and a sampling check.",
         desc_ja="ルームウェア・パジャマの副資材ガイド。フリースに毛が付きにくい主ラベル、セットの洗濯表示とサイズラベル、タグ、ギフト包装、5ステップの検収を解説します。東莞泰閣包装。",
         desc_ko="라운지웨어·파자마 부자재 가이드. 플리스에 보풀이 붙지 않는 주 라벨, 세트의 세탁 표시와 사이즈 라벨, 행택, 선물 포장, 5단계 검수를 정리했습니다. 둥관 TAGE 패키징.",
         desc_fr="Guide accessoires de vêtements d'intérieur : labels adaptés à la polaire, entretien et tailles en ensemble, tags, emballage coffret et contrôle.",
         desc_es="Guía de accesorios para ropa de casa: etiquetas para polar, cuidado y tallas en conjunto, colgantes, embalaje de regalo y control de la muestra."),
]

for a in ARTICLES:
    print("%-34s zh=%d en=%d ja=%d ko=%d fr=%d es=%d"
          % (a["slug"], len(a["desc_zh"]), len(a["desc_en"]), len(a["desc_ja"]),
             len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))

    # --- 根目录页：整体替换 meta description 块 ---
    root = "blog/%s" % a["slug"]
    s = open(root, encoding="utf-8").read()
    block = ('<meta name="description" data-zh="%s"\n'
             '      data-en="%s" data-ja="%s" data-ko="%s"\n'
             '      data-fr="%s"\n'
             '      data-es="%s"\n'
             '      content="%s">' % (a["desc_zh"], a["desc_en"], a["desc_ja"], a["desc_ko"],
                                     a["desc_fr"], a["desc_es"], a["desc_zh"]))
    s, n = re.subn(r'<meta name="description".*?content="[^"]*">', block, s, count=1, flags=re.S)
    assert n == 1, "根页 desc 未替换"
    open(root, "w", encoding="utf-8", newline="").write(s)

    # --- 各语言页：更新 content="..."（繁体页 description 取自 data-zh，已在上一步处理）---
    for lang in LANGS:
        p = "%s/blog/%s" % (lang, a["slug"])
        t = open(p, encoding="utf-8").read()
        pat = re.compile(r'(<meta name="description"[^>]*?content=")[^"]*(">)', re.S)
        val = a["desc_%s" % lang] if lang != "ja" else a["desc_ja"]
        m = pat.search(t)
        assert m, "语言页 desc 未找到: %s" % p
        t2 = pat.sub(lambda mm: mm.group(1) + val + mm.group(2), t, count=1)
        open(p, "w", encoding="utf-8", newline="").write(t2)
        print("   %s -> content 更新 (%d 字符)" % (p, len(val)))
print("desc 微调完成")
