#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-23 晚间批次：desc 长度微调（英文目标 150-160 字符，中文 80-120 字）
同步更新根目录页 data-* 与 en/ja/ko/fr/es 五语页的 content。
"""
import os, re, sys

LANGS = ["en", "ja", "ko", "fr", "es"]
ARTICLES = [
    dict(slug="sock-hosiery-trims-guide.html",
         desc_zh="袜子与针织小件辅料指南：讲清袜标该选织唛还是热转印无感标、尺码按脚长与欧码怎么写、吊卡尺寸如何配合折叠方式、成对包装与多双礼盒怎么配比，附询价规格表与五步验收清单。来自东莞泰阁包装。",
         desc_en="Sock and knitwear trims guide: woven or tagless heat-transfer labels, sizing by foot length, sock card formats, pair packaging and five acceptance checks.",
         desc_ja="靴下・ニット小物の副資材ガイド。織りラベルか熱転写の無感ラベルかの選び方、足長とEU番号の併記、カード寸法と折り方、ペア包装とギフト比率、仕様表と5つの検収項目を解説します。東莞泰閣包装。",
         desc_ko="양말·니트 소품 부자재 가이드. 직조 라벨과 열전사 무감 라벨 선택, 발 길이와 EU 호수 병기, 카드 치수와 접는 방식, 페어 포장과 선물 비율, 사양표와 5단계 검수를 정리했습니다. 둥관 TAGE 패키징.",
         desc_fr="Guide accessoires chaussettes : label tissé ou transfert sans couture, tailles par longueur de pied, format de carte et emballage par paire.",
         desc_es="Guía de accesorios para calcetines: etiqueta tejida o transferible sin costura, tallas por longitud de pie, formato de tarjeta y controles."),
    dict(slug="hat-scarf-gloves-trims-guide.html",
         desc_zh="帽子、围巾与手套辅料指南：讲清成分比例怎么标才不违规、头围与掌围尺码怎么写、长条标签缝在哪不露边、吊卡吊粒与冬季三件套礼盒如何配比，附询价规格表与五步验收清单。来自东莞泰阁包装。",
         desc_en="Hat, scarf and glove trims guide: fibre content labelling, head and palm sizing, sewing long labels, tag fixings and three-piece gift box ratios for buyers.",
         desc_ja="帽子・マフラー・手袋の副資材ガイド。組成表示の書き方、頭囲と手囲みのサイズ表記、長いラベルの縫い位置、タグと3点セットのギフト比率、仕様表と5つの検収項目を解説します。東莞泰閣包装。",
         desc_ko="모자·머플러·장갑 부자재 가이드. 혼용률 표기 방법, 머리둘레와 손둘레 사이즈, 긴 라벨 봉제 위치, 행택과 3종 선물 세트 비율, 사양표와 5단계 검수를 정리했습니다. 둥관 TAGE 패키징.",
         desc_fr="Guide accessoires bonnets, écharpes et gants : composition des fibres, tailles de tête et de main, pose des labels longs et coffrets cadeaux.",
         desc_es="Guía de accesorios para gorros, bufandas y guantes: composición de fibras, tallas de contorno, etiquetas largas y cajas de regalo."),
]

bad = 0
for a in ARTICLES:
    print("%-34s zh=%d字 en=%d字符 ja=%d ko=%d fr=%d es=%d"
          % (a["slug"], len(a["desc_zh"]), len(a["desc_en"]), len(a["desc_ja"]),
             len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))
    if not (150 <= len(a["desc_en"]) <= 160):
        print("   !! 英文 desc 不在 150-160 区间")
        bad += 1
    if not (80 <= len(a["desc_zh"]) <= 120):
        print("   !! 中文 desc 不在 80-120 区间")
        bad += 1

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

    # --- 各语言页：更新 content="..."（根/语言页 description 取自对应语言 data 值）---
    for lang in LANGS:
        p = "%s/blog/%s" % (lang, a["slug"])
        t = open(p, encoding="utf-8").read()
        pat = re.compile(r'(<meta name="description"[^>]*?content=")[^"]*(">)', re.S)
        val = a["desc_%s" % lang]
        m = pat.search(t)
        assert m, "语言页 desc 未找到: %s" % p
        t2 = pat.sub(lambda mm: mm.group(1) + val + mm.group(2), t, count=1)
        open(p, "w", encoding="utf-8", newline="").write(t2)
        print("   %s -> content 更新 (%d 字符)" % (p, len(val)))
print("desc 微调完成，问题 %d" % bad)
sys.exit(1 if bad else 0)
