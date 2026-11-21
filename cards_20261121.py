# -*- coding: utf-8 -*-
"""在 blog/index.html 顶部插入 2026-11-21 两篇文章卡片（六语 data-*）。"""
import html
import re

LANGS = ['zh', 'en', 'fr', 'es', 'ja', 'ko']


def esc(v):
    return html.escape(html.unescape(v), quote=True)


def attrs(d):
    return ' '.join('data-%s="%s"' % (l, esc(d[l])) for l in LANGS)


CARDS = [
    {
        'tag': {'zh': '標籤與吊牌', 'en': 'Labels &amp; Hang Tags', 'fr': 'Étiquettes', 'es': 'Etiquetas',
                'ja': 'ネーム・下げ札', 'ko': '라벨·행택'},
        'slug': 'douyin-xiaohongshu-tag-label-compliance.html',
        'h3': {'zh': '抖音小紅書服裝吊牌與標籤：合規清單 7 項',
               'en': 'Douyin and Xiaohongshu Apparel Tags and Labels: A 7-Point Checklist',
               'fr': 'Étiquettes pour Douyin et Xiaohongshu : la check-list en 7 points',
               'es': 'Etiquetas para Douyin y Xiaohongshu: lista de 7 puntos',
               'ja': '抖音・小紅書向け衣料タグと表示：7 項目の適合チェック',
               'ko': '더우인·샤오홍슈 의류 행택과 라벨: 7가지 적합성 점검'},
        'p': {'zh': '七項法定內容、洗水標耐久要求、直播鏡頭下的失分點，加一張出貨前驗收表。',
              'en': 'Seven legal items, the durable care label rule, live-stream mistakes and a one-page shipping check.',
              'fr': 'Sept mentions légales, la règle de l&#x27;étiquette durable, les erreurs en direct et une check-list d&#x27;expédition.',
              'es': 'Siete datos legales, la regla de la etiqueta duradera, errores en directo y una lista de envío.',
              'ja': '法定 7 項目、耐久表示のルール、ライブでの失点、出荷前チェック表まで。',
              'ko': '법정 7가지 항목, 내구 표시 규칙, 라이브 방송 실수, 출고 전 검수표까지.'},
    },
    {
        'tag': {'zh': '電商包裝', 'en': 'Ecommerce Packaging', 'fr': 'Emballage e-commerce', 'es': 'Embalaje ecommerce',
                'ja': 'EC 包装', 'ko': '이커머스 포장'},
        'slug': 'size-guide-insert-card-guide.html',
        'h3': {'zh': '尺碼指南卡：電商服裝退貨率的第一道防線',
               'en': 'Size Guide Insert Cards: The First Line Against Apparel Returns',
               'fr': 'Carte guide des tailles : le premier rempart contre les retours',
               'es': 'Tarjeta guía de tallas: la primera barrera contra las devoluciones',
               'ja': 'サイズガイドカード：返品を減らす最初の一手',
               'ko': '사이즈 가이드 카드: 반품을 줄이는 첫 단계'},
        'p': {'zh': '85 × 54 mm 或 90 × 50 mm、300 至 350 g/m²、四塊內容與跨市場對照表的完整規格。',
              'en': '85 × 54 mm or 90 × 50 mm, 300 to 350 g/m², the four content blocks and cross-market charts.',
              'fr': '85 × 54 mm ou 90 × 50 mm, 300 à 350 g/m², les quatre blocs et les tableaux multi-marchés.',
              'es': '85 × 54 mm o 90 × 50 mm, 300 a 350 g/m², los cuatro bloques y tablas multimercado.',
              'ja': '85 × 54 mm か 90 × 50 mm、300〜350 g/m²、4 ブロックと多市場対照表の仕様。',
              'ko': '85 × 54 mm 또는 90 × 50 mm, 300~350 g/m², 네 가지 블록과 다중 시장 대조표 사양.'},
    },
]

MORE = {'zh': '閱讀全文 →', 'en': 'Read more →', 'fr': 'Lire la suite →', 'es': 'Leer más →',
        'ja': '続きを読む →', 'ko': '자세히 보기 →'}

path = 'blog/index.html'
s = open(path, encoding='utf-8').read()

blocks = []
for c in CARDS:
    assert c['slug'] not in s, c['slug'] + ' 卡片已存在'
    blocks.append('''      <article class="post-card">
        <span class="tag" %s>%s</span>
        <h3 %s>%s</h3>
        <p %s>%s</p>
        <a class="more" href="%s" %s>%s</a>
      </article>''' % (
        attrs(c['tag']), html.escape(html.unescape(c['tag']['zh'])),
        attrs(c['h3']), html.escape(html.unescape(c['h3']['zh'])),
        attrs(c['p']), html.escape(html.unescape(c['p']['zh'])),
        c['slug'], attrs(MORE), html.escape(html.unescape(MORE['zh']))))

marker = '<div class="post-grid">\n'
i = s.index(marker) + len(marker)
s = s[:i] + '\n'.join(blocks) + '\n\n' + s[i:]
open(path, 'w', encoding='utf-8', newline='').write(s)
print('插入 2 张卡片，post-card 总数', s.count('class="post-card"'))
