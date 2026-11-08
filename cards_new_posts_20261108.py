#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在 blog/index.html 的 post-grid 顶部插入 2026-11-08 两篇文章的卡片（八语）。"""
import re

CARDS = [
    dict(
        slug="silica-gel-desiccant-apparel-packaging.html",
        tag=dict(zh="包裝防潮", en="Moisture control", fr="Contrôle de l'humidité", es="Control de humedad",
                 ja="防湿包装", ko="방습 포장", de="Feuchteschutz", pt="Controle de umidade"),
        h3=dict(
            zh="服裝紙箱裡的矽膠乾燥劑：用量、放法與出口標示",
            en="Silica Gel Desiccant in Clothing Cartons: Dosage and Placement",
            fr="Dessiccant en carton d'export de vêtements : dosage et placement",
            es="Desecante en cajas de ropa para exportación: dosis y colocación",
            ja="衣料用段ボールのシリカゲル乾燥剤：使用量と配置",
            ko="의류 카톤의 실리카겔 건조제: 사용량과 배치",
            de="Silicagel-Trockenmittel im Bekleidungskarton: Dosierung und Platzierung",
            pt="Dessecante de sílica gel em caixas de roupa: dosagem e posição"),
        p=dict(
            zh="一箱放多少克、放哪裡、哪種乾燥劑在 REACH 下要避開，以及袋身警語怎麼寫。附按箱容積計算的用量表與六項進料檢驗。",
            en="How many grams per carton, where the sachet goes, which types to avoid under REACH, and how to word the warning. With a dosage table by carton volume and six incoming checks.",
            fr="Combien de grammes par carton, où placer le sachet, quels types éviter au titre de REACH et comment formuler l'avertissement. Avec tableau de dosage et six contrôles.",
            es="Cuántos gramos por caja, dónde va la bolsa, qué tipos evitar según REACH y cómo redactar el aviso. Con tabla de dosificación y seis controles de entrada.",
            ja="1 箱当たりのグラム数、置き場所、REACH で避ける種類、警告文の書き方。容積別の使用量表と受入検査 6 項目付き。",
            ko="카톤당 몇 그램, 어디에 두는지, REACH상 피할 종류, 경고문 표기 방법. 부피별 사용량 표와 입고 검사 6항목 포함.",
            de="Wie viele Gramm pro Karton, wohin der Beutel gehört, welche Typen nach REACH ausfallen und wie der Warnhinweis lautet. Mit Dosiertabelle und sechs Prüfpunkten.",
            pt="Quantos gramas por caixa, onde vai o sachê, quais tipos evitar sob o REACH e como redigir o aviso. Com tabela de dosagem e seis verificações."),
    ),
    dict(
        slug="care-label-roll-direction-core-guide.html",
        tag=dict(zh="洗水標選型", en="Care label specs", fr="Spécifications d'étiquettes", es="Especificación de etiquetas",
                 ja="洗濯表示の仕様", ko="취급 표시 사양", de="Pflegeetikett-Spezifikation", pt="Especificação de etiqueta"),
        h3=dict(
            zh="洗水標卷料：紙芯、捲繞方向與印表機匹配",
            en="Care Label Rolls: Core Size, Winding Direction and Printer Compatibility",
            fr="Rouleaux d'étiquettes d'entretien : mandrin, sens et compatibilité machine",
            es="Rollos de etiquetas de cuidado: núcleo, sentido y compatibilidad",
            ja="洗濯表示ラベルのロール：紙管径・巻き方向・プリンター適合",
            ko="취급 표시 라벨 롤: 지관, 권취 방향, 프린터 적합성",
            de="Pflegeetikett-Rollen: Kern, Wickelrichtung und Druckerpassung",
            pt="Rolos de etiqueta de conservação: tubete, sentido e compatibilidade"),
        p=dict(
            zh="印得漂亮卻一直卡紙，問題多半在卷料規格：紙芯直徑、捲繞方向、卷長與模切間距。附下單前要對的六項機器參數。",
            en="Print quality is fine but the printer keeps jamming — the fault is usually the roll spec: core diameter, winding direction, length and die-cut pitch. With six parameters to confirm before ordering.",
            fr="L'impression est bonne mais ça bourre : le défaut vient du rouleau — mandrin, sens d'enroulement, longueur et pas de découpe. Avec six paramètres à confirmer.",
            es="La impresión está bien pero se atasca: el fallo suele ser el rollo —núcleo, sentido, longitud y paso de troquel—. Con seis parámetros a confirmar.",
            ja="印刷はきれいなのに詰まる。原因はロール仕様（紙管径・巻き方向・巻長・型抜きピッチ）にあることが多いです。発注前の確認 6 項目付き。",
            ko="인쇄는 좋은데 자꾸 막힌다면 원인은 롤 사양(지관, 권취 방향, 길이, 타발 피치)입니다. 발주 전 확인 여섯 항목 포함.",
            de="Der Druck ist gut, aber es staut: Die Ursache liegt meist in der Rollenspezifikation — Kern, Wickelrichtung, Länge und Stanzteilung. Mit sechs Punkten vor der Bestellung.",
            pt="A impressão está boa mas atola: a causa costuma ser o rolo — tubete, sentido, comprimento e passo de corte. Com seis parâmetros antes do pedido."),
    ),
]

LANGS = ["zh", "en", "fr", "es", "ja", "ko", "de", "pt"]


def attrs(d):
    return " ".join('data-%s="%s"' % (l, d[l]) for l in LANGS)


idx = "blog/index.html"
s = open(idx, encoding="utf-8", newline="").read()
marker = '<div class="post-grid">\n'
assert marker in s, "post-grid 未找到"

cards = ""
for c in CARDS:
    assert c["slug"] not in s, "卡已存在：%s" % c["slug"]
    cards += (
        '      <article class="post-card">\n'
        '        <span class="tag" %s>%s</span>\n'
        '        <h3 %s>%s</h3>\n'
        '        <p %s>%s</p>\n'
        '        <a class="more" href="%s" data-zh="閱讀全文 →" data-en="Read more →" data-fr="Lire la suite →" data-es="Leer más →" data-ja="続きを読む →" data-ko="자세히 보기 →" data-de="Weiterlesen →" data-pt="Ler mais →">閱讀全文 →</a>\n'
        '      </article>\n'
        % (attrs(c["tag"]), c["tag"]["zh"], attrs(c["h3"]), c["h3"]["zh"],
           attrs(c["p"]), c["p"]["zh"], c["slug"])
    )

s = s.replace(marker, marker + "\n" + cards, 1)
open(idx, "w", encoding="utf-8", newline="").write(s)
print("blog/index.html 插入 2 张卡片完成")
