# -*- coding: utf-8 -*-
"""把两篇新文章卡片插到 blog/index.html 的 post-grid 顶部（2026-11-19 20:00）。"""
import html
import re

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
    {"zh": "吊牌上該印什麼：九個欄位與它們的法律歸屬", "en": "What to Print on a Hang Tag: Nine Fields and Where They Belong",
     "fr": "Que faut-il imprimer sur une étiquette : neuf champs et leur place", "es": "Qué imprimir en una etiqueta colgante: nueve campos y su lugar",
     "ja": "下げ札に何を刷るか：9 項目とその置き場所", "ko": "행택에 무엇을 인쇄할까: 9개 항목과 그 위치"},
    {"zh": "九個欄位裡只有六個該印在吊牌上，另外三個的正確位置是耐久洗水標。附字高下限、條碼 ANSI 等級、版本管控與五項打樣驗收。",
     "en": "Only six of the nine fields belong on the tag; three belong on a durable care label. Type sizes, ANSI barcode grade, version control and five proof checks.",
     "fr": "Seuls six des neuf champs vont sur l'étiquette, trois sur une étiquette durable. Hauteurs de caractères, classe ANSI, gestion des versions et cinq contrôles.",
     "es": "Solo seis de los nueve campos van en la etiqueta; tres van en una etiqueta duradera. Cuerpos de letra, clase ANSI, versiones y cinco controles.",
     "ja": "9 項目のうち下げ札に載せるのは 6 項目、残り 3 項目は耐久ラベルへ。文字高、ANSI 等級、版管理、量産前 5 項目の確認まで。",
     "ko": "9개 항목 중 행택에 넣을 것은 6개, 나머지 3개는 내구성 라벨로. 글자 높이, ANSI 등급, 버전 관리, 양산 전 점검 5항목까지."},
    "hang-tag-content-checklist.html"))

CARDS.append(card(
    {"zh": "包裝與物流", "en": "Packaging & Logistics", "fr": "Emballage et logistique",
     "es": "Embalaje y logística", "ja": "梱包・物流", "ko": "포장·물류"},
    {"zh": "每單包裝成本：六個成本項與一個能對帳的數字", "en": "Packaging Cost per Order: Six Lines and One Number You Can Defend",
     "fr": "Coût d'emballage par commande : six postes et un chiffre défendable", "es": "Coste de embalaje por pedido: seis líneas y una cifra defendible",
     "ja": "1 注文あたりの梱包コスト：6 つの費目と説明できる数字", "ko": "주문당 포장 원가: 여섯 항목과 방어 가능한 숫자"},
    {"zh": "單價不是成本。主包裝、內襯、封口、標籤、工時、損耗六行相加才是每單成本，附材積重算法與三個不損防護的降本動作。",
     "en": "Unit price is not cost. Six lines — pack, fill, closure, labels, labour, damage — add up to cost per order, plus dimensional weight and three savings that keep protection.",
     "fr": "Le prix unitaire n'est pas un coût. Six postes — emballage, calage, fermeture, étiquettes, main-d'œuvre, rebuts — font le coût par commande, avec poids volumétrique.",
     "es": "El precio unitario no es el coste. Seis líneas — envase, relleno, cierre, etiquetas, mano de obra, merma — dan el coste por pedido, con peso volumétrico.",
     "ja": "単価はコストではありません。主包装・緩衝材・封かん・ラベル・作業時間・破損の 6 費目で 1 注文コストを出し、容積重量と改善 3 点も整理。",
     "ko": "단가는 원가가 아닙니다. 주 포장재·완충재·밀봉·라벨·작업 시간·파손 여섯 항목으로 주문당 원가를 내고 부피 중량과 개선 3점을 정리."},
    "packaging-cost-per-order.html"))

p = "blog/index.html"
s = open(p, encoding="utf-8", newline="").read()
marker = '<div class="post-grid">'
assert s.count(marker) == 1, s.count(marker)
assert "hang-tag-content-checklist" not in s, "卡片已存在"
s = s.replace(marker, marker + "\n" + "\n" + "".join(CARDS), 1)

# 顺手修掉历史卡片里被双重转义的 &amp;amp;
n_fix = s.count("&amp;amp;")
s = s.replace("&amp;amp;", "&amp;")

open(p, "w", encoding="utf-8", newline="").write(s)
print("插入卡片 2 张；修复双重转义 %d 处；文件大小 %d" % (n_fix, len(s.encode("utf-8"))))
