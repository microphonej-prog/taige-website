# -*- coding: utf-8 -*-
"""把 2026-11-20 20:00 两篇新文章卡片插到 blog/index.html 的 post-grid 顶部。"""
import html

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]


def A(d):
    return " ".join('data-%s="%s"' % (l, html.escape(d[l], quote=True)) for l in LANGS)


def card(tag, h3, p, href):
    return (
        '      <article class="post-card">\n'
        '        <span class="tag" %s>%s</span>\n'
        '        <h3 %s>%s</h3>\n'
        '        <p %s>%s</p>\n'
        '        <a class="more" href="%s" data-zh="閱讀全文 →" data-en="Read more →" data-fr="Lire la suite →" data-es="Leer más →" data-ja="続きを読む →" data-ko="자세히 보기 →">閱讀全文 →</a>\n'
        '      </article>\n' % (
            A(tag), html.escape(tag["zh"], quote=True),
            A(h3), html.escape(h3["zh"], quote=True),
            A(p), html.escape(p["zh"], quote=True), href))


CARDS = []

CARDS.append(card(
    {"zh": "標籤與吊牌", "en": "Labels & Hang Tags", "fr": "Étiquettes",
     "es": "Etiquetas", "ja": "ネーム・下げ札", "ko": "라벨·행택"},
    {"zh": "黑卡吊牌白墨：遮蓋力、刮花與邊緣透底",
     "en": "White Ink on Black Hang Tags: Opacity, Scuff and Edge Show-Through",
     "fr": "Encre blanche sur étiquettes noires : opacité, rayures et bords apparents",
     "es": "Tinta blanca sobre etiquetas negras: opacidad, roce y borde visible",
     "ja": "黒い下げ札の白インキ：隠蔽力・こすれ・エッジの透け",
     "ko": "검정 행택의 흰 잉크: 은폐력·긁힘·모서리 비침"},
    {"zh": "白墨兩遍、L* ≥ 90、線寬 0.25 mm、條碼靜區 10X——四個數字管住發灰、刮花與邊緣露白。",
     "en": "Two white hits, L* 90, 0.25 mm rules and a 10X barcode quiet zone: four numbers that stop greying, scuffing and pale edges.",
     "fr": "Deux passes de blanc, L* 90, filets de 0,25 mm et zone de silence 10X : quatre chiffres contre le grisé, les rayures et les bords clairs.",
     "es": "Dos pasadas de blanco, L* 90, filetes de 0,25 mm y zona de silencio 10X: cuatro números contra el gris, el roce y los bordes claros.",
     "ja": "白 2 回刷り、L* 90、罫線 0.25 mm、バーコード静区 10X。灰色化・こすれ・縁の白浮きを抑える 4 つの数値。",
     "ko": "흰 잉크 2회, L* 90, 선 폭 0.25 mm, 바코드 정지 영역 10X. 회색화·긁힘·모서리 비침을 잡는 네 숫자."},
    "black-hang-tag-white-ink-guide.html"))

CARDS.append(card(
    {"zh": "採購與成本", "en": "Sourcing & Cost", "fr": "Achats et coûts",
     "es": "Compras y costes", "ja": "調達・コスト", "ko": "구매·원가"},
    {"zh": "吊牌下單數量怎麼算：每件張數、備品率與補印成本",
     "en": "How Many Hang Tags to Order: Per-Garment Count, Spares and Reprint Cost",
     "fr": "Combien d'étiquettes pendantes commander : ratio par pièce, stock de sécurité et coût de réimpression",
     "es": "Cuántas etiquetas colgantes pedir: ratio por prenda, reserva y coste de reimpresión",
     "ja": "下げ札の発注数量：1 着あたり枚数・予備率・再印刷コスト",
     "ko": "행택 발주 수량: 착당 매수·예비율·재인쇄 비용"},
    {"zh": "3%、5%、8% 各對應什麼場景，加上一個 10,000 件訂單算出 12,000 張的完整算例。",
     "en": "What 3, 5 and 8 percent spares actually cover, plus a full worked example where a 10,000-piece order lands at 12,000 tags.",
     "fr": "Ce que couvrent 3, 5 et 8 % de sécurité, avec un exemple complet : 10 000 pièces aboutissant à 12 000 étiquettes.",
     "es": "Qué cubren realmente 3, 5 y 8 % de reserva, con un ejemplo completo: 10.000 prendas que acaban en 12.000 etiquetas.",
     "ja": "3 %・5 %・8 % の予備が何をカバーするか。10,000 着が 12,000 枚になる計算例まで。",
     "ko": "3 %, 5 %, 8 % 예비가 각각 무엇을 덮는지, 10,000착이 12,000장이 되는 계산 예까지."},
    "hang-tag-quantity-planning-guide.html"))

p = "blog/index.html"
s = open(p, encoding="utf-8", newline="").read()
marker = '<div class="post-grid">'
assert s.count(marker) == 1, s.count(marker)
assert "black-hang-tag-white-ink-guide" not in s, "卡片已存在"
s = s.replace(marker, marker + "\n" + "\n" + "".join(CARDS), 1)

n_fix = s.count("&amp;amp;")
s = s.replace("&amp;amp;", "&amp;")

open(p, "w", encoding="utf-8", newline="").write(s)
print("插入卡片 2 张；修复双重转义 %d 处；文件大小 %d" % (n_fix, len(s.encode("utf-8"))))
