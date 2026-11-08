#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-08 每日文章：从 8 语骨架生成两篇新文章（正文来自 scratch 文件）。

骨架 = blog/trim-material-substitution-guide.html（zh/en/fr/es/ja/ko/de/pt 八语头尾齐全）
只替换 title / description / canonical+hreflang / crumb / h1 / 日期行 / JSON-LD 第三项与 headline / 正文整段。
"""
import os
import re

SKEL = "blog/trim-material-substitution-guide.html"
DATE_ZH = "2026年11月8日"
DATE_EN = "November 8, 2026"
DATE_FR = "8 novembre 2026"
DATE_ES = "8 de noviembre de 2026"
DATE_JA = "2026年11月8日"
DATE_KO = "2026년 11월 8일"
DATE_DE = "8. November 2026"
DATE_PT = "8 de novembro de 2026"

A = [
    dict(
        slug="silica-gel-desiccant-apparel-packaging.html",
        body=r"F:/hermes/cache/scratch/body1_20261108.html",
        title_zh="服裝出口紙箱乾燥劑指南：矽膠用量、放置與標示要求 | TAGE",
        title_en="Silica Gel Desiccant in Clothing Cartons: Dosage and Placement | TAGE",
        title_fr="Dessiccant en carton d'export : dosage, placement et étiquetage | TAGE",
        title_es="Desecante en cajas de exportación: dosis, colocación y etiquetado | TAGE",
        title_ja="衣料輸出段ボールの乾燥剤：使用量・配置・表示要件 | TAGE",
        title_ko="의류 수출 카톤 건조제: 사용량, 배치, 표시 요건 | TAGE",
        title_de="Trockenmittel im Bekleidungskarton: Dosierung, Platzierung, Kennzeichnung | TAGE",
        title_pt="Dessecante em caixa de exportação: dosagem, posição e rotulagem | TAGE",
        desc_zh="服裝出口紙箱該放多少矽膠乾燥劑、放在哪裡、哪些乾燥劑類型在 REACH 與 CLP 下要避開，以及袋身警語與紙箱標示怎麼寫。附按箱容積計算的用量對照表與六項進料檢驗。",
        desc_en="How much silica gel a clothing export carton needs, where to place it, which desiccant types to avoid under REACH, and how to label the sachet.",
        desc_fr="Quelle quantité de dessiccant par carton, où le placer, quels types éviter au titre de REACH, et comment étiqueter le sachet.",
        desc_es="Cuánto desecante necesita una caja de exportación, dónde colocarlo, qué tipos evitar según REACH y cómo etiquetar la bolsa.",
        desc_ja="衣料輸出段ボールに必要な乾燥剤の量、置き場所、REACH で避けるべき種類、小袋の表示方法を整理します。",
        desc_ko="의류 수출 카톤에 필요한 건조제 양, 배치 위치, REACH상 피해야 할 종류, 사셰 표시 방법을 정리합니다.",
        desc_de="Wie viel Trockenmittel ein Bekleidungskarton braucht, wohin es gehört, welche Typen nach REACH ausfallen und wie der Beutel gekennzeichnet wird.",
        desc_pt="Quanto dessecante uma caixa de exportação precisa, onde colocar, quais tipos evitar sob o REACH e como rotular o sachê.",
        crumb_zh="紙箱乾燥劑",
        crumb_en="Carton Desiccant",
        crumb_fr="Dessiccant en carton",
        crumb_es="Desecante en caja",
        crumb_ja="段ボールの乾燥剤",
        crumb_ko="카톤 건조제",
        crumb_de="Trockenmittel im Karton",
        crumb_pt="Dessecante na caixa",
        h1_zh="服裝紙箱裡的矽膠乾燥劑：用量、放法與出口標示",
        h1_en="Silica Gel Desiccant in Clothing Cartons: Dosage and Placement",
        h1_fr="Dessiccant en carton d'export de vêtements : dosage et placement",
        h1_es="Desecante en cajas de ropa para exportación: dosis y colocación",
        h1_ja="衣料用段ボールのシリカゲル乾燥剤：使用量と配置",
        h1_ko="의류 카톤의 실리카겔 건조제: 사용량과 배치",
        h1_de="Silicagel-Trockenmittel im Bekleidungskarton: Dosierung und Platzierung",
        h1_pt="Dessecante de sílica gel em caixas de roupa: dosagem e posição",
    ),
    dict(
        slug="care-label-roll-direction-core-guide.html",
        body=r"F:/hermes/cache/scratch/body2_20261108.html",
        title_zh="洗水標卷料規格指南：紙芯、捲繞方向與印表機匹配 | TAGE",
        title_en="Care Label Rolls: Core Size, Winding Direction and Printer Fit | TAGE",
        title_fr="Rouleaux d'étiquettes d'entretien : mandrin, sens et imprimante | TAGE",
        title_es="Rollos de etiquetas de cuidado: núcleo, sentido e impresora | TAGE",
        title_ja="洗濯表示ラベルのロール仕様：紙管・巻き方向・プリンター適合 | TAGE",
        title_ko="취급 표시 라벨 롤 사양: 지관, 권취 방향, 프린터 적합성 | TAGE",
        title_de="Pflegeetikett-Rollen: Kern, Wickelrichtung und Druckerpassung | TAGE",
        title_pt="Rolos de etiqueta de conservação: tubete, sentido e impressora | TAGE",
        desc_zh="洗水標卷料怎麼寫規格：紙芯直徑、捲繞方向、卷長、模切間距與黑標位置，加上下單前要對的六項機器參數，避免卡紙與鏡像輸出。",
        desc_en="How to specify care label rolls: core diameter, face-in or face-out winding, roll length, die-cut pitch and eye marks, plus six checks that stop jams.",
        desc_fr="Spécifier un rouleau d'étiquettes : mandrin, sens d'enroulement, longueur, pas de découpe et repères, plus six contrôles anti-bourrage.",
        desc_es="Especificar rollos de etiquetas: núcleo, sentido de bobinado, longitud, paso de troquel y marcas, más seis comprobaciones anti-atasco.",
        desc_ja="洗濯表示ロールの仕様書：紙管径、巻き方向、巻長、型抜きピッチ、黒マークと、詰まりを防ぐ 6 項目の確認点を整理します。",
        desc_ko="취급 표시 롤 사양서: 지관 직경, 권취 방향, 롤 길이, 타발 피치, 흑색 마크와 막힘을 막는 여섯 가지 확인 항목.",
        desc_de="Pflegeetikett-Rollen spezifizieren: Kerndurchmesser, Wickelrichtung, Länge, Stanzteilung und Marken — plus sechs Prüfpunkte gegen Stau.",
        desc_pt="Especificar rolos de etiqueta: tubete, sentido de bobinagem, comprimento, passo de corte e marcas, além de seis verificações contra atolamento.",
        crumb_zh="洗水標卷料",
        crumb_en="Care Label Rolls",
        crumb_fr="Rouleaux d'étiquettes",
        crumb_es="Rollos de etiquetas",
        crumb_ja="洗濯表示ロール",
        crumb_ko="취급 표시 롤",
        crumb_de="Pflegeetikett-Rollen",
        crumb_pt="Rolos de etiqueta",
        h1_zh="洗水標卷料：紙芯、捲繞方向與印表機匹配",
        h1_en="Care Label Rolls: Core Size, Winding Direction and Printer Compatibility",
        h1_fr="Rouleaux d'étiquettes d'entretien : mandrin, sens d'enroulement et compatibilité machine",
        h1_es="Rollos de etiquetas de cuidado: núcleo, sentido de bobinado y compatibilidad",
        h1_ja="洗濯表示ラベルのロール：紙管径・巻き方向・プリンター適合",
        h1_ko="취급 표시 라벨 롤: 지관, 권취 방향, 프린터 적합성",
        h1_de="Pflegeetikett-Rollen: Kern, Wickelrichtung und Druckerpassung",
        h1_pt="Rolos de etiqueta de conservação: tubete, sentido e compatibilidade",
    ),
]

skel = open(SKEL, encoding="utf-8", newline="").read()
skel_name = re.search(r'"position": 3,\s*"name": "([^"]*)"', skel).group(1)
print("骨架 breadcrumb 名:", skel_name)

sitemap = open("sitemap.xml", encoding="utf-8").read()
for a in A:
    slug = a["slug"]
    for p in ("blog/%s" % slug, "en/blog/%s" % slug, "de/blog/%s" % slug, "pt/blog/%s" % slug):
        if os.path.exists(p):
            raise SystemExit("选题撞车：%s 已存在" % p)
    if ("/blog/%s</loc>" % slug) in sitemap:
        raise SystemExit("选题撞车：sitemap 已含 %s" % slug)
print("选题全新，开始生成")

for a in A:
    slug = a["slug"]
    s = skel

    # 1 title
    title = ('<title data-zh="%s" data-en="%s" data-fr="%s" data-es="%s" data-ja="%s" data-ko="%s" data-de="%s" data-pt="%s">%s</title>'
             % (a["title_zh"], a["title_en"], a["title_fr"], a["title_es"], a["title_ja"],
                a["title_ko"], a["title_de"], a["title_pt"], a["title_zh"]))
    s, n = re.subn(r"<title[^>]*>.*?</title>", lambda m: title, s, count=1, flags=re.S)
    assert n == 1, "title 替换失败"

    # 2 description
    desc = ('<meta name="description" data-zh="%s" data-en="%s" data-fr="%s" data-es="%s" data-ja="%s" '
            'data-ko="%s" data-de="%s" data-pt="%s" content="%s">'
            % (a["desc_zh"], a["desc_en"], a["desc_fr"], a["desc_es"], a["desc_ja"],
               a["desc_ko"], a["desc_de"], a["desc_pt"], a["desc_zh"]))
    s, n = re.subn(r'<meta name="description".*?>', lambda m: desc, s, count=1, flags=re.S)
    assert n == 1, "description 替换失败"

    # 3 canonical + hreflang
    href = ('<link rel="canonical" href="https://taigetag.com/blog/%s">\n'
            '<link rel="alternate" hreflang="zh-Hant" href="https://taigetag.com/blog/%s">\n'
            '<link rel="alternate" hreflang="en" href="https://taigetag.com/en/blog/%s">\n'
            '<link rel="alternate" hreflang="fr" href="https://taigetag.com/fr/blog/%s">\n'
            '<link rel="alternate" hreflang="es" href="https://taigetag.com/es/blog/%s">\n'
            '<link rel="alternate" hreflang="ja" href="https://taigetag.com/ja/blog/%s">\n'
            '<link rel="alternate" hreflang="ko" href="https://taigetag.com/ko/blog/%s">\n'
            '<link rel="alternate" hreflang="de" href="https://taigetag.com/de/blog/%s">\n'
            '<link rel="alternate" hreflang="pt-BR" href="https://taigetag.com/pt/blog/%s">\n'
            '<link rel="alternate" hreflang="x-default" href="https://taigetag.com/blog/%s">'
            % ((slug,) * 10))
    s, n = re.subn(r'<link rel="canonical" href="[^"]*">(?:\n<link rel="alternate"[^\n]*>)+',
                   lambda m: href, s, count=1)
    assert n == 1, "hreflang 替换失败"

    # 4 crumb
    crumb = ('<div class="crumb"><a href="../index.html" data-zh="首頁" data-en="Home" data-fr="Accueil" data-es="Inicio" data-ja="ホーム" data-ko="홈" data-de="Startseite" data-pt="Início">首頁</a>'
             ' / <a href="index.html" data-zh="輔料 FAQ" data-en="Trims FAQ" data-fr="FAQ Accessoires" data-es="FAQ Accesorios" data-ja="副資材 FAQ" data-ko="부자재 FAQ" data-de="Accessoires-FAQ" data-pt="FAQ de aviamentos">輔料 FAQ</a>'
             ' / <span data-zh="%s" data-en="%s" data-fr="%s" data-es="%s" data-ja="%s" data-ko="%s" data-de="%s" data-pt="%s">%s</span></div>'
             % (a["crumb_zh"], a["crumb_en"], a["crumb_fr"], a["crumb_es"], a["crumb_ja"],
                a["crumb_ko"], a["crumb_de"], a["crumb_pt"], a["crumb_zh"]))
    s, n = re.subn(r'<div class="crumb">.*?</div>', lambda m: crumb, s, count=1, flags=re.S)
    assert n == 1, "crumb 替换失败"

    # 5 h1
    h1 = ('<h1 data-zh="%s" data-en="%s" data-fr="%s" data-es="%s" data-ja="%s" data-ko="%s" data-de="%s" data-pt="%s">%s</h1>'
          % (a["h1_zh"], a["h1_en"], a["h1_fr"], a["h1_es"], a["h1_ja"], a["h1_ko"],
             a["h1_de"], a["h1_pt"], a["h1_zh"]))
    s, n = re.subn(r'<h1 [^>]*>.*?</h1>', lambda m: h1, s, count=1, flags=re.S)
    assert n == 1, "h1 替换失败"

    # 6 日期行
    meta = ('<p data-zh="泰閣包裝 · 更新於 %s" data-en="By TAGE Packaging &nbsp;·&nbsp; Updated %s" data-ja="泰閣包装 · %s更新" '
            'data-ko="TAGE 패키징 · %s 업데이트" data-fr="Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le %s" '
            'data-es="Por TAGE Packaging &nbsp;·&nbsp; Actualizado el %s" data-de="Von TAGE Packaging &nbsp;·&nbsp; Aktualisiert am %s" '
            'data-pt="Por TAGE Packaging &nbsp;·&nbsp; Atualizado em %s">泰閣包裝 · 更新於 %s</p>'
            % (DATE_ZH, DATE_EN, DATE_JA, DATE_KO, DATE_FR, DATE_ES, DATE_DE, DATE_PT, DATE_ZH))
    s, n = re.subn(r'<p data-zh="泰閣包裝 · 更新於[^"]*".*?</p>', lambda m: meta, s, count=1, flags=re.S)
    assert n == 1, "日期行替换失败"

    # 7 JSON-LD
    s = s.replace('"%s"' % skel_name, '"%s"' % a["h1_zh"])
    s, n = re.subn(r'"headline": "[^"]*"', lambda m: '"headline": "%s"' % a["h1_zh"], s, count=1)
    assert n == 1, "headline 替换失败"

    # 8 正文
    body = open(a["body"], encoding="utf-8").read().rstrip("\n")
    i0 = s.index('  <section class="article-body">')
    i1 = s.index("\n</main>")
    s = s[:i0] + body + s[i1:]

    out = "blog/%s" % slug
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(s)
    counts = {l: len(re.findall(r'data-%s="' % l, s)) for l in
              ["zh", "en", "fr", "es", "ja", "ko", "de", "pt"]}
    print("写入 %s (%d 字节)  属性计数 %s  desc_en=%d 字符"
          % (out, len(s.encode("utf-8")), counts, len(a["desc_en"])))
