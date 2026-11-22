# -*- coding: utf-8 -*-
"""把两篇新文章卡片插到 blog/index.html 的 post-grid 顶部（六语 data-*）。"""
import html
import sys

sys.path.insert(0, '.')
import body_20261122_1400_a as A
import body_20261122_1400_b as B

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]

CARDS = [
    dict(slug=A.SLUG, cat=A.CAT, h3=A.H1,
         p={"zh": "海關看進口商、監管看 SNI、門店看印尼語洗護。三份文件、五行印尼語、五個數字，一次講清。",
            "en": "Customs reads the importer, the regulator reads SNI, the store reads Indonesian care text. Three documents, five lines, five numbers.",
            "fr": "La douane lit l'importateur, l'autorité lit le SNI, le rayon lit l'entretien en indonésien. Trois documents, cinq lignes, cinq chiffres.",
            "es": "La aduana lee el importador, la autoridad el SNI, la tienda el cuidado en indonesio. Tres documentos, cinco líneas, cinco cifras.",
            "ja": "税関は輸入者、監督官庁は SNI、店頭はインドネシア語の洗濯表示を見る。3 書類・5 行・5 数値で整理します。",
            "ko": "세관은 수입자, 감독기관은 SNI, 매장은 인도네시아어 취급 표시를 봅니다. 서류 세 가지, 다섯 줄, 다섯 수치로 정리."}),
    dict(slug=B.SLUG, cat=B.CAT, h3=B.H1,
         p={"zh": "CSDDD 不會罰你，客戶會換掉你。買家最先要的四份文件、合約保證的三句話、批號追溯的三點一線。",
            "en": "CSDDD will not fine you; the customer will replace you. The four documents requested first, three contract sentences, three-point traceability.",
            "fr": "La CSDDD ne vous sanctionne pas, le client vous remplace. Quatre documents, trois phrases de contrat, trois points de traçabilité.",
            "es": "La CSDDD no le multa, el cliente le sustituye. Cuatro documentos, tres frases de contrato, tres puntos de trazabilidad.",
            "ja": "CSDDD は罰金より先に「交代」が来る。最初に求められる 4 書類、契約の 3 文、ロット遡及の 3 点。",
            "ko": "CSDDD는 벌금보다 교체가 먼저 옵니다. 최초 요청 서류 네 가지, 계약 세 문장, 로트 추적 세 지점."}),
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
