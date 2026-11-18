# -*- coding: utf-8 -*-
"""把两篇新文章卡片插到 blog/index.html 的 post-grid 顶部。"""
import html


def A(d):
    return " ".join('data-%s="%s"' % (l, html.escape(d[l], quote=True)) for l in ["zh", "en", "fr", "es", "ja", "ko"])


def card(tag, h3, p, href):
    return (
        '      <article class="post-card">\n'
        '        <span class="tag" %s>%s</span>\n'
        '        <h3 %s>%s</h3>\n'
        '        <p %s>%s</p>\n'
        '        <a class="more" href="%s" data-zh="閱讀全文 →" data-en="Read more →" data-fr="Lire la suite →" data-es="Leer más →" data-ja="続きを読む →" data-ko="자세히 보기 →">閱讀全文 →</a>\n'
        '      </article>\n' % (
            A(tag), tag["zh"], A(h3), h3["zh"], A(p), p["zh"], href))


CARDS = []

CARDS.append(card(
    {"zh": "合規指南", "en": "Compliance", "fr": "Conformité",
     "es": "Cumplimiento", "ja": "コンプライアンス", "ko": "컴플라이언스"},
    {"zh": "兒童服裝繩帶安全：EN 14682 的三道紅線", "en": "EN 14682 Drawcord Rules for Childrenswear",
     "fr": "EN 14682 : les règles des cordons pour enfants", "es": "EN 14682: reglas de cordones en ropa infantil",
     "ja": "子ども服のひも安全基準 EN 14682", "ko": "아동복 끈 안전 기준 EN 14682"},
    {"zh": "兜帽拉繩什麼時候一根都不能有：134 cm 的零容忍、140 mm 自由端上限、75 mm 拉鍊拉頭，附美國 ASTM F1816 對照與輔料規格書寫法。",
     "en": "When a hood drawstring is one too many: the 134 cm zero-tolerance line, 140 mm free ends, 75 mm zipper pulls, plus ASTM F1816 and spec-sheet wording.",
     "fr": "Quand un cordon de capuche est de trop : tolérance zéro jusqu'à 134 cm, extrémités de 140 mm, tirettes de 75 mm, et l'ASTM F1816.",
     "es": "Cuándo un cordón de capucha sobra: tolerancia cero hasta 134 cm, extremos de 140 mm, tiradores de 75 mm y la ASTM F1816.",
     "ja": "フードのひもが 1 本でも不可となるのはいつか。134 cm のゼロ許容、自由端 140 mm、引き手 75 mm、米国 ASTM F1816 と仕様書の書き方。",
     "ko": "후드 끈이 한 개도 안 되는 기준. 134 cm 제로 허용, 자유단 140 mm, 지퍼 손잡이 75 mm, 미국 ASTM F1816과 사양서 표기."},
    "en-14682-childrenswear-drawcord-safety.html"))

CARDS.append(card(
    {"zh": "包裝指南", "en": "Packaging Guide", "fr": "Guide emballage",
     "es": "Guía de embalaje", "ja": "包装ガイド", "ko": "포장 가이드"},
    {"zh": "輔料防霉：從回南天到集裝箱結露", "en": "Mold Prevention for Apparel Trims",
     "fr": "Moisissures sur accessoires", "es": "Moho en accesorios de confección",
     "ja": "副資材のカビ対策", "ko": "부자재 곰팡이 방지"},
    {"zh": "黴菌只認三個條件。本文講清楚哪些輔料最先發霉、集裝箱結露怎麼判定、乾燥劑用量（DIN 55474）與富馬酸二甲酯的 REACH 紅線。",
     "en": "Mold needs three conditions only: which trims mold first, how to tell container rain from a leak, desiccant sizing by DIN 55474 and the REACH ban on DMF.",
     "fr": "Trois conditions suffisent : quels accessoires moisissent d'abord, distinguer la pluie de conteneur d'une fuite, doser le dessiccant (DIN 55474), le DMF interdit.",
     "es": "Bastan tres condiciones: qué accesorios se enmohecen primero, distinguir la lluvia de contenedor de una fuga, dosificar desecante (DIN 55474) y el DMF prohibido.",
     "ja": "カビは 3 条件だけで発生します。先にカビる副資材、コンテナ結露と漏水の見分け、DIN 55474 による乾燥剤の量、DMF の REACH 規制。",
     "ko": "곰팡이는 세 조건만 충족되면 발생합니다. 먼저 곰팡이가 나는 부자재, 컨테이너 결로와 누수 구분, DIN 55474 제습제 산정, DMF의 REACH 규제."},
    "apparel-trims-mold-prevention-shipping.html"))

p = "blog/index.html"
s = open(p, encoding="utf-8", newline="").read()
marker = '<div class="post-grid">\n'
assert s.count(marker) == 1, s.count(marker)
assert "en-14682-childrenswear-drawcord-safety" not in s, "卡片已存在"
s = s.replace(marker, marker + "\n" + "".join(CARDS), 1)
open(p, "w", encoding="utf-8", newline="").write(s)
print("插入卡片 2 张，文件大小", len(s.encode("utf-8")))
