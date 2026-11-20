# -*- coding: utf-8 -*-
"""把 2026-11-20 14:00 两篇新文章卡片插到 blog/index.html 的 post-grid 顶部。"""
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
    {"zh": "吊牌紙張絲流：翹曲、折線爆裂與打孔撕裂的根因",
     "en": "Paper Grain Direction for Hang Tags: Why Tags Curl, Crack and Tear",
     "fr": "Sens du grain du papier : pourquoi les étiquettes tuilent, se fissurent et se déchirent",
     "es": "Dirección de fibra del papel: por qué las etiquetas se alabean, se agrietan y se rompen",
     "ja": "下げ札の紙の目：反り・折り割れ・穴破れはなぜ起きるか",
     "ko": "행택 종이 결: 휨·접힘 균열·구멍 찢어짐은 왜 생기는가"},
    {"zh": "三個免儀器的車間驗法、可貼進採購單的三句規格，以及翹曲 3 mm、折線 5 次、掛孔 2 kg 的驗收門檻。",
     "en": "Three tests without instruments, three spec lines you can paste into an order, and pass limits of 3 mm curl, five folds and 2 kg on the hole.",
     "fr": "Trois essais sans instrument, trois lignes à copier dans le bon de commande et des limites de 3 mm de tuilage, cinq plis et 2 kg sur le trou.",
     "es": "Tres ensayos sin instrumentos, tres líneas para el pedido y límites de 3 mm de alabeo, cinco pliegues y 2 kg en el troquel.",
     "ja": "装置不要の 3 つの確認法、発注書に貼れる 3 行の仕様、そして反り 3 mm・折り 5 回・穴 2 kg の検収基準。",
     "ko": "장비 없이 하는 확인법 3가지, 발주서에 붙일 세 줄 사양, 그리고 휨 3 mm·접힘 5회·구멍 2 kg 검수 기준."},
    "hang-tag-paper-grain-direction-guide.html"))

CARDS.append(card(
    {"zh": "品質與檢測", "en": "Quality & Testing", "fr": "Qualité et essais",
     "es": "Calidad y ensayos", "ja": "品質・試験", "ko": "품질·시험"},
    {"zh": "輔料顏色公差：ΔE 怎麼寫進規格，什麼時候該讓步",
     "en": "Trim Colour Tolerance: How to Write Delta E Limits Into a Spec",
     "fr": "Tolérance de couleur : comment inscrire un Delta E au cahier des charges",
     "es": "Tolerancia de color: cómo fijar el Delta E en la especificación",
     "ja": "副資材の色公差：ΔE を仕様書に書き、どこで妥協するか",
     "ko": "부자재 색 공차: ΔE를 사양서에 쓰고 어디서 양보할까"},
    {"zh": "公式、光源與儀器幾何先鎖定，再按品類定閾值；附取樣規則、三光源同色異譜比對與不合格的三條路徑。",
     "en": "Fix the formula, light source and geometry first, then set limits by trim type, with sampling rules, three-source metamerism checks and three routes on failure.",
     "fr": "Figer formule, source et géométrie, puis des seuils par type, avec règles d'échantillonnage, contrôle métamérique à trois sources et trois voies en cas d'échec.",
     "es": "Fijar fórmula, fuente y geometría, luego límites por tipo, con muestreo, control metamérico de tres fuentes y tres vías ante el fallo.",
     "ja": "式・光源・測定幾何を先に固定し、品種別の上限を設定。抜取規則、3 光源の条件等色確認、不合格時の 3 経路まで。",
     "ko": "공식·광원·측정 기하를 먼저 고정하고 품종별 상한을 설정. 샘플링 규칙, 삼광원 조건등색 확인, 불합격 시 세 경로까지."},
    "trim-color-tolerance-delta-e-guide.html"))

p = "blog/index.html"
s = open(p, encoding="utf-8", newline="").read()
marker = '<div class="post-grid">'
assert s.count(marker) == 1, s.count(marker)
assert "hang-tag-paper-grain-direction-guide" not in s, "卡片已存在"
s = s.replace(marker, marker + "\n" + "\n" + "".join(CARDS), 1)

n_fix = s.count("&amp;amp;")
s = s.replace("&amp;amp;", "&amp;")

open(p, "w", encoding="utf-8", newline="").write(s)
print("插入卡片 2 张；修复双重转义 %d 处；文件大小 %d" % (n_fix, len(s.encode("utf-8"))))
