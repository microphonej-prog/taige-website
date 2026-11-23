# -*- coding: utf-8 -*-
"""把两篇新文章卡片插到 blog/index.html 的 post-grid 顶部（六语 data-*）。"""
import re
import sys

sys.path.insert(0, '.')
import body_20261123_0800_a as A
import body_20261123_0800_b as B

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
ENTITY = re.compile(r'&(?!(?:amp|quot|lt|gt|#x27|#\d+);)')


def esc(v):
    return ENTITY.sub('&amp;', v).replace('"', '&quot;')


def attrs(dd):
    return ' '.join('data-%s="%s"' % (l, esc(dd[l])) for l in LANGS)


CARDS = [
    dict(slug=A.SLUG, cat=A.CAT, h3=A.H1,
         p={"zh": "同一支膠換了基材就失效。三種膠系的初黏與耐溫、五種服裝基材的實測結論，加上採購單該寫的三個數字。",
            "en": "The same adhesive fails on a new substrate. Three families compared by grip and temperature, five garment substrates, three numbers for the order.",
            "fr": "La même colle échoue sur un nouveau support. Trois familles comparées, cinq supports de vêtement, trois valeurs à inscrire.",
            "es": "El mismo adhesivo falla en otro soporte. Tres familias comparadas, cinco soportes de prenda, tres cifras para el pedido.",
            "ja": "同じ粘着剤が基材を変えると外れます。3系統の初粘と温度域、衣料5基材の実測、発注書に書く3つの数値。",
            "ko": "같은 접착제도 기재가 바뀌면 떨어집니다. 세 계열의 초기 점착과 온도 범위, 의류 기재 다섯 가지, 발주서에 적을 세 수치."}),
    dict(slug=B.SLUG, cat=B.CAT, h3=B.H1,
         p={"zh": "印頭不是突然壞的，是慢慢變淡。換卷就擦、換料就校、每季量一次黑條，五分鐘擋掉大部分退貨。",
            "en": "Printheads fade rather than fail. Wipe on every roll change, calibrate on every material change, measure a black bar quarterly.",
            "fr": "Une tête pâlit plus qu'elle ne casse : essuyer à chaque rouleau, calibrer à chaque matière, mesurer une barre noire chaque trimestre.",
            "es": "El cabezal se desvanece más que se rompe: limpiar en cada rollo, calibrar en cada material, medir una barra negra cada trimestre.",
            "ja": "ヘッドは壊れるより薄くなります。ロール交換で清掃、材料変更で調整、四半期に一度ベタ黒を測定。",
            "ko": "헤드는 고장보다 흐려집니다. 롤 교체 시 닦기, 소재 교체 시 교정, 분기마다 솔리드 검정 측정."}),
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
