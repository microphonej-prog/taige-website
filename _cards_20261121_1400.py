# -*- coding: utf-8 -*-
"""把两篇新文章卡片插到 blog/index.html 的 post-grid 顶部（六语 data-*）。"""
import html
import sys

sys.path.insert(0, '.')
import body_20261121_1400_a as A
import body_20261121_1400_b as B

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]

CARDS = [
    dict(slug=A.SLUG, cat=A.CAT, h3=A.H1,
         p={"zh": "30 × 15 mm 還是 50 × 25 mm、紙面還是膜面、可移除還是熱熔，加上歐日韓台的標示要求與六個驗收數字。",
            "en": "30 × 15 mm or 50 × 25 mm, paper or film face, removable or hot melt, plus EU, JP, KR and TW labelling rules and six inspection numbers.",
            "fr": "30 × 15 mm ou 50 × 25 mm, papier ou film, détachable ou hot melt, avec les règles UE, JP, KR, TW et six chiffres de contrôle.",
            "es": "30 × 15 mm o 50 × 25 mm, papel o film, removible o hot melt, con reglas UE, JP, KR, TW y seis cifras de control.",
            "ja": "30 × 15 mm か 50 × 25 mm、紙かフィルム、再剥離かホットメルト。EU・日本・韓国・台湾の表示要件と検収 6 数値。",
            "ko": "30 × 15 mm 또는 50 × 25 mm, 종이 또는 필름, 재박리 또는 핫멜트. EU·일본·한국·대만 표시 요건과 검수 6수치."}),
    dict(slug=B.SLUG, cat=B.CAT, h3=B.H1,
         p={"zh": "寬度、折法、切邊與針距怎麼定，縫製五個設定避免起皺，以及它不能取代的法定標示。",
            "en": "Width, fold, cut edge and stitch count, five sewing settings that stop puckering, and the legal labels a hem tag cannot replace.",
            "fr": "Largeur, pliage, coupe et point, cinq réglages anti-fronçage et les marquages légaux qu&#x27;il ne remplace pas.",
            "es": "Ancho, pliegue, corte y puntada, cinco ajustes que evitan el fruncido y los marcados legales que no sustituye.",
            "ja": "幅・折り・裁断・針数の決め方、ひきつれを防ぐ 5 設定、代替できない法定表示。",
            "ko": "폭·접힘·재단·바늘 수 결정법, 주름을 막는 다섯 설정, 대체할 수 없는 법정 표시."}),
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
