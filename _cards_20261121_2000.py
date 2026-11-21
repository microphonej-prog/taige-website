# -*- coding: utf-8 -*-
"""把两篇新文章卡片插到 blog/index.html 的 post-grid 顶部（六语 data-*）。"""
import html
import sys

sys.path.insert(0, '.')
import body_20261121_2000_a as A
import body_20261121_2000_b as B

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]

CARDS = [
    dict(slug=A.SLUG, cat=A.CAT, h3=A.H1,
         p={"zh": "內衣後扣、褲腰鉤條、裙門襟小鉤受力完全不同。鉤數、鍍層、鎳釋放與五個驗收數字，一次講清。",
            "en": "Bra backs, waistband hooks and skirt plackets load differently. Hook count, coating, nickel release and five acceptance numbers.",
            "fr": "Dos de soutien-gorge, crochets de ceinture et pattes de jupe ne chargent pas pareil. Nombre, revêtement, nickel et cinq chiffres.",
            "es": "Espaldas de sujetador, corchetes de cinturilla y tapetas cargan distinto. Número, recubrimiento, níquel y cinco cifras.",
            "ja": "ブラ後ろ、腰ホック、スカート前立てでは荷重が違います。フック数、めっき、ニッケル溶出、検収 5 数値。",
            "ko": "브라 후크, 허리 후크, 스커트 여밈은 하중이 다릅니다. 후크 수, 도금, 니켈 용출, 검수 다섯 수치."}),
    dict(slug=B.SLUG, cat=B.CAT, h3=B.H1,
         p={"zh": "塔夫綢、府綢、斜紋、針織、網眼怎麼選：克重、縮水、耐摩擦與化學限值的四組數字。",
            "en": "Taffeta, poplin, twill, jersey or mesh: four sets of numbers covering weight, shrinkage, crocking and chemical limits.",
            "fr": "Taffetas, popeline, sergé, jersey ou filet : quatre jeux de chiffres, grammage, retrait, frottement et limites chimiques.",
            "es": "Tafetán, popelina, sarga, jersey o malla: cuatro juegos de cifras, gramaje, encogimiento, frote y límites químicos.",
            "ja": "タフタ、ポプリン、ツイル、天竺、メッシュの選び方。目付・収縮・摩擦・化学規制値の 4 組の数値。",
            "ko": "태프타, 포플린, 트윌, 저지, 메시 선택법. 평량·수축·마찰·화학 기준 네 가지 수치."}),
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
