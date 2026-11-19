# -*- coding: utf-8 -*-
"""把两篇新文章卡片插到 blog/index.html 的 post-grid 顶部（2026-11-19 14:00）。"""
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
    {"zh": "標籤與吊牌", "en": "Labels &amp; Hang Tags", "fr": "Étiquettes",
     "es": "Etiquetas", "ja": "ネーム・下げ札", "ko": "라벨·행택"},
    {"zh": "牛皮紙吊牌：克重、印刷與環保聲明", "en": "Kraft Paper Hang Tags: GSM, Print and Green Claims",
     "fr": "Étiquettes kraft : grammage, impression et allégations", "es": "Etiquetas kraft: gramaje, impresión y alegaciones",
     "ja": "クラフト紙の下げ札：坪量・印刷・環境表示", "ko": "크라프트 행택: 평량·인쇄·환경 표시"},
    {"zh": "牛皮紙吊牌最容易在三處出錯：克重不足捲邊、本色紙上品牌色偏、環保聲明沒有依據。附 300–450 g/m² 對照、白墨打底與順色設計、採購單五欄位與四項驗收。",
     "en": "Kraft tags fail in three places: too little GSM, brand colours drifting on brown stock, and green claims with no evidence. Ranges, printing routes, PO fields and four acceptance checks.",
     "fr": "L'étiquette kraft échoue sur trois points : grammage insuffisant, couleurs qui dérivent sur papier brun, allégations sans preuve. Grammages, impression, champs du bon de commande et quatre contrôles.",
     "es": "La etiqueta kraft falla en tres puntos: gramaje escaso, color que se desvía en papel marrón y alegaciones sin prueba. Gramajes, impresión, campos del pedido y cuatro controles.",
     "ja": "クラフト下げ札は 3 点で失敗します。坪量不足による反り、茶紙での色ずれ、根拠のない環境表示。坪量 300〜450 g/m² の比較、白下地と地色活用、発注 5 項目と受入 4 項目。",
     "ko": "크라프트 행택은 세 곳에서 실패합니다. 평량 부족으로 인한 말림, 갈색 종이에서의 색 이탈, 근거 없는 환경 표시. 평량 300~450 g/m² 비교, 백색 바탕과 바탕색 활용, 발주 5항목과 검사 4항목."},
    "kraft-hang-tags-guide.html"))

CARDS.append(card(
    {"zh": "洗水標與合規", "en": "Care Labels &amp; Compliance", "fr": "Étiquettes &amp; conformité",
     "es": "Etiquetas y normativa", "ja": "洗濯表示・法令", "ko": "세탁 표시·규정"},
    {"zh": "天然纖維洗水標：羊毛、蠶絲、喀什米爾與亞麻", "en": "Care Labels for Wool, Silk, Cashmere and Linen",
     "fr": "Étiquettes d'entretien : laine, soie, cachemire et lin", "es": "Etiquetas de cuidado: lana, seda, cachemir y lino",
     "ja": "天然繊維の洗濯表示：ウール・シルク・カシミヤ・リネン", "ko": "천연 섬유 세탁 표시: 울·실크·캐시미어·리넨"},
    {"zh": "通用「30 ℃ 輕柔」寫在羊毛上就是毀衣服。四種纖維的洗滌上限與乾洗代號、ISO 3758 符號順序、5% 規則、三次洗滌後的縮率允收與標材字高。",
     "en": "A generic 30 °C gentle line ruins wool. Wash limits and dry-clean codes for four fibres, ISO 3758 symbol order, the 5% rule, and shrinkage acceptance after three washes.",
     "fr": "Un « 30 °C délicat » générique détruit la laine. Limites de lavage et codes de nettoyage des quatre fibres, ordre ISO 3758, règle des 5 % et retrait après trois lavages.",
     "es": "Un «30 °C suave» genérico arruina la lana. Límites de lavado y códigos en seco de cuatro fibras, orden ISO 3758, regla del 5 % y encogimiento tras tres lavados.",
     "ja": "汎用の「30 ℃ 弱い洗濯」はウールを傷めます。4 繊維の洗濯上限とドライ記号、ISO 3758 の記号順序、5 % ルール、3 回洗濯後の収縮許容と文字高。",
     "ko": "범용 '30 ℃ 약한 세탁'은 울을 망칩니다. 네 섬유의 세탁 상한과 드라이 기호, ISO 3758 기호 순서, 5% 규칙, 3회 세탁 후 수축 허용과 글자 높이."},
    "natural-fiber-care-label-guide.html"))

p = "blog/index.html"
s = open(p, encoding="utf-8", newline="").read()
marker = '<div class="post-grid">\n'
assert s.count(marker) == 1, s.count(marker)
assert "kraft-hang-tags-guide" not in s, "卡片已存在"
s = s.replace(marker, marker + "\n" + "".join(CARDS), 1)
open(p, "w", encoding="utf-8", newline="").write(s)
print("插入卡片 2 张，文件大小", len(s.encode("utf-8")))
