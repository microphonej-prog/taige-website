# -*- coding: utf-8 -*-
"""把两篇新文章卡片插到 blog/index.html 的 post-grid 顶部（2026-11-19 08:00）。"""
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
    {"zh": "採購與規格", "en": "Sourcing &amp; Specs", "fr": "Sourcing &amp; specs",
     "es": "Compras y fichas", "ja": "調達・仕様", "ko": "소싱·사양"},
    {"zh": "輔料規格書怎麼寫：技術包裡的六個欄位", "en": "How to Write Trim Specs in a Tech Pack",
     "fr": "Rédiger les spécifications d'accessoires", "es": "Especificaciones de accesorios en la ficha técnica",
     "ja": "仕様書（テックパック）の副資材欄の書き方", "ko": "테크팩 부자재 사양서 작성법"},
    {"zh": "輔料被打樣打回，多半不是工藝問題：編號、結構、尺寸與允差、顏色基準、位置與用量、合規欄位，缺一個就多一輪。附四種輔料的寫法與允差口徑。",
     "en": "Trims come back from sampling for one reason: a missing field. Six fields every trim line needs, with examples for hang tags, woven labels, care labels and cords.",
     "fr": "Six champs qu'une ligne d'accessoire doit porter : code, construction, dimensions et tolérances, couleur, pose et conformité, avec des exemples concrets.",
     "es": "Seis campos que toda línea de accesorio debe llevar: código, construcción, dimensiones y tolerancias, color, posición y conformidad, con ejemplos.",
     "ja": "副資材がサンプル戻しになる理由は項目の欠落です。品番・構造・寸法と許容差・色基準・取付位置・法令表示の 6 項目を実例つきで整理。",
     "ko": "부자재 샘플 반려는 항목 누락에서 옵니다. 품번·구조·치수와 허용차·색 기준·부착 위치·법정 표시 6개 항목을 사례로 정리."},
    "tech-pack-trim-spec-guide.html"))

CARDS.append(card(
    {"zh": "標籤與吊牌", "en": "Labels &amp; Hang Tags", "fr": "Étiquettes",
     "es": "Etiquetas", "ja": "ネーム・下げ札", "ko": "라벨·행택"},
    {"zh": "吊牌掛繩與彈力圈：從線徑到拉力的選型", "en": "Hang Tag Cords, Strings and Elastic Loops",
     "fr": "Cordons, fils et élastiques pour étiquettes", "es": "Cordones, hilos y elásticos para etiquetas",
     "ja": "下げ札の紐・ゴムループ・取付具", "ko": "행택 끈·고무줄·부착구"},
    {"zh": "掛繩不是配件而是規格：五種材質的線徑與拉力對照、切長／圈長／懸掛長三種寫法、孔徑 2:1 原則、童裝頸部限制與三項驗收。",
     "en": "The cord is a spec, not an accessory: five materials compared, cut, loop and hang length conventions, the 2:1 hole rule and three acceptance checks.",
     "fr": "Le cordon est une spécification : cinq matières comparées, longueurs coupée, boucle et suspension, règle du trou 2:1 et trois contrôles de réception.",
     "es": "El cordón es una especificación: cinco materiales comparados, longitudes cortada, lazo y caída, regla del ojal 2:1 y tres controles de recepción.",
     "ja": "紐は付属品ではなく仕様です。5 素材の太さと強度、カット長・ループ長・掛け長、穴径 2:1 の原則、子ども服の制限と受入 3 項目。",
     "ko": "끈은 부속품이 아니라 사양입니다. 5개 소재의 굵기와 강도, 재단·루프·걸이 길이, 구멍 2:1 원칙, 아동복 제한과 검사 3항목."},
    "hang-tag-cord-elastic-guide.html"))

p = "blog/index.html"
s = open(p, encoding="utf-8", newline="").read()
marker = '<div class="post-grid">\n'
assert s.count(marker) == 1, s.count(marker)
assert "tech-pack-trim-spec-guide" not in s, "卡片已存在"
s = s.replace(marker, marker + "\n" + "".join(CARDS), 1)
open(p, "w", encoding="utf-8", newline="").write(s)
print("插入卡片 2 张，文件大小", len(s.encode("utf-8")))
