# -*- coding: utf-8 -*-
"""把两篇新文章卡片插到 blog/index.html 的 post-grid 顶部（六语 data-*）。"""
import html
import sys

sys.path.insert(0, '.')
import body_20261122_0800_a as A
import body_20261122_0800_b as B

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]

CARDS = [
    dict(slug=A.SLUG, cat=A.CAT, h3=A.H1,
         p={"zh": "切邊、撕裂、水溶、熱熔四種襯紙怎麼配針數？毛巾布的貼面、甲醛限值與五項驗收數字，一次講清。",
            "en": "Cutaway, tearaway, wash-away or fusible: how to match backing weight to stitch count, plus toppings, formaldehyde limits and five acceptance numbers.",
            "fr": "Découpe, arrachage, soluble ou thermocollant : accorder le grammage au nombre de points, film de dessus, formaldéhyde et cinq contrôles.",
            "es": "Recortable, desgarrable, soluble o termoadhesiva: ajustar gramaje a puntadas, film superior, formaldehído y cinco controles.",
            "ja": "カットアウェイ・ティアアウェイ・水溶性・接着の選び方。目付と針数の対応、パイル地用フィルム、ホルムアルデヒド、検収 5 項目。",
            "ko": "컷어테이·티어어테이·수용성·접착형 선택. 평량과 바늘 수 대응, 파일 원단용 필름, 포름알데히드 한도, 검수 다섯 항목."}),
    dict(slug=B.SLUG, cat=B.CAT, h3=B.H1,
         p={"zh": "1 L 等於 0.635 mm，釦眼長度＝直徑＋厚度＋2 mm。L 號換算表、布料搭配、鎳釋放與童裝安全線，五個數字直接寫進採購單。",
            "en": "1 L is 0.635 mm and a buttonhole is diameter plus thickness plus 2 mm. Ligne table, fabric matching, nickel release and childrenswear safety.",
            "fr": "1 L vaut 0,635 mm et la boutonnière = diamètre + épaisseur + 2 mm. Table des lignes, accord tissu, nickel et sécurité enfant.",
            "es": "1 L son 0,635 mm y el ojal = diámetro + espesor + 2 mm. Tabla de líneas, correspondencia con el tejido, níquel y seguridad infantil.",
            "ja": "1 L は 0.635 mm、ボタン穴＝直径＋厚み＋2 mm。ライン換算表、生地との対応、ニッケル溶出、子供服の安全まで。",
            "ko": "1 L은 0.635 mm, 단추 구멍 = 지름 + 두께 + 2 mm. 리뉴 환산표, 원단 대응, 니켈 용출, 아동복 안전까지."}),
]

READ = {"zh": "閱讀全文 →", "en": "Read more →", "fr": "Lire la suite →", "es": "Leer más →",
        "ja": "続きを読む →", "ko": "자세히 보기 →"}


def esc(v):
    return html.escape(html.unescape(v), quote=True)


def attrs(d):
    return ' '.join('data-%s="%s"' % (l, esc(d[l])) for l in LANGS)


blocks = []
for c in CARDS:
    blocks.append('      <article class="post-card">')
    blocks.append('        <span class="tag" %s>%s</span>' % (
        attrs(c["cat"]), html.escape(html.unescape(c["cat"]["zh"]))))
    blocks.append('        <h3 %s>%s</h3>' % (
        attrs(c["h3"]), html.escape(html.unescape(c["h3"]["zh"]))))
    blocks.append('        <p %s>%s</p>' % (
        attrs(c["p"]), html.escape(html.unescape(c["p"]["zh"]))))
    blocks.append('        <a class="more" href="%s" %s>%s</a>' % (
        c["slug"], attrs(READ), html.escape(READ["zh"])))
    blocks.append('      </article>')
new = "\n".join(blocks) + "\n"

path = "blog/index.html"
s = open(path, encoding="utf-8").read()
anchor = '      <div class="post-grid">\n'
assert s.count(anchor) == 1, s.count(anchor)
for c in CARDS:
    assert c["slug"] not in s, c["slug"]
s = s.replace(anchor, anchor + new, 1)
open(path, "w", encoding="utf-8", newline="").write(s)
print("inserted 2 cards into blog/index.html; file now %d bytes" % len(s.encode("utf-8")))
