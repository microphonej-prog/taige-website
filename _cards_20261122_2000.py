# -*- coding: utf-8 -*-
"""把两篇新文章卡片插到 blog/index.html 的 post-grid 顶部（六语 data-*）。"""
import re
import sys

sys.path.insert(0, '.')
import body_20261122_2000_a as A
import body_20261122_2000_b as B

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
ENTITY = re.compile(r'&(?!(?:amp|quot|lt|gt|#x27|#\d+);)')


def esc(v):
    return ENTITY.sub('&amp;', v).replace('"', '&quot;')


def attrs(dd):
    return ' '.join('data-%s="%s"' % (l, esc(dd[l])) for l in LANGS)


CARDS = [
    dict(slug=A.SLUG, cat=A.CAT, h3=A.H1,
         p={"zh": "同克重的紙，厚度可以差 30%。把紙種、克重、厚度寫成三行，供應商就沒有換紙的空間。",
            "en": "Two boards at 350 g/m² can differ 30 percent in caliper. Three lines on the PO close that gap.",
            "fr": "Deux cartons de 350 g/m² peuvent différer de 30 % en épaisseur. Trois lignes sur le bon de commande suffisent.",
            "es": "Dos cartones de 350 g/m² pueden diferir un 30 % en espesor. Tres líneas en el pedido cierran esa brecha.",
            "ja": "同じ 350 g/m² でも厚みは 30% 違うことがあります。仕様を3行にすれば、紙の差し替え余地が消えます。",
            "ko": "같은 350 g/m²라도 두께는 30% 차이가 납니다. 사양을 세 줄로 쓰면 지종 교체 여지가 사라집니다."}),
    dict(slug=B.SLUG, cat=B.CAT, h3=B.H1,
         p={"zh": "透光紙的成敗在兩件事：白墨放在哪裡、樣品疊在什麼上面看。其餘都是細節。",
            "en": "Translucent tags live or die on two decisions: where the white underlay goes, and what the sample sits on.",
            "fr": "Une étiquette translucide se joue sur deux choix : où va la sous-couche blanche, et sur quoi l'échantillon est posé.",
            "es": "Una etiqueta translúcida se decide en dos puntos: dónde va el blanco de fondo y sobre qué se aprueba la muestra.",
            "ja": "透けるタグの成否は2点で決まります。白下地をどこに置くか、サンプルを何の上で見るか。",
            "ko": "반투명 행택은 두 가지에서 갈립니다. 백색 하지를 어디에 두는지, 샘플을 무엇 위에서 보는지."}),
]

READ = {"zh": "閱讀全文 →", "en": "Read more →", "fr": "Lire la suite →", "es": "Leer más →",
        "ja": "続きを読む →", "ko": "자세히 보기 →"}

blocks = []
for c in CARDS:
    blocks.append('      <article class="post-card">')
    blocks.append('        <span class="tag" %s>%s</span>' % (attrs(c["cat"]), esc(c["cat"]["zh"])))
    blocks.append('        <h3 %s>%s</h3>' % (attrs(c["h3"]), esc(c["h3"]["zh"])))
    blocks.append('        <p %s>%s</p>' % (attrs(c["p"]), esc(c["p"]["zh"])))
    blocks.append('        <a class="more" href="%s" %s>%s</a>' % (c["slug"], attrs(READ), esc(READ["zh"])))
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
