# -*- coding: utf-8 -*-
"""构建 2026-11-21 08:00 两篇文章的根页（中文主稿，六语 data-* 属性）。"""
import html
import re
import sys

sys.path.insert(0, '.')
import body_20261121a as A
import body_20261121b as B

TEMPLATE = 'blog/black-hang-tag-white-ink-guide.html'
OLD_SLUG = 'black-hang-tag-white-ink-guide.html'
OLD_H1 = '黑卡吊牌的白墨：遮蓋力、刮花與邊緣透底'
LANGS = ['zh', 'en', 'fr', 'es', 'ja', 'ko']


def esc(v):
    """先还原实体再统一转义，避免 &#x27; 被二次转义成 &amp;#x27;"""
    return html.escape(html.unescape(v), quote=True)


def attrs(d):
    return ' '.join('data-%s="%s"' % (l, esc(d[l])) for l in LANGS)


def text(d):
    return html.escape(html.unescape(d['zh']))


def render_blocks(blocks):
    out = []
    for kind, d in blocks:
        if kind in ('p', 'h2'):
            out.append('      <%s %s>%s</%s>' % (kind, attrs(d), text(d), kind))
        elif kind == 'callout':
            out.append('      <div class="callout" %s>%s</div>' % (attrs(d), text(d)))
        elif kind == 'ul':
            out.append('      <ul>')
            for it in d:
                out.append('        <li %s>%s</li>' % (attrs(it), text(it)))
            out.append('      </ul>')
        elif kind == 'table':
            out.append('      <table>')
            out.append('        <thead>')
            out.append('          <tr>')
            for th in d['head']:
                out.append('            <th %s>%s</th>' % (attrs(th), text(th)))
            out.append('          </tr>')
            out.append('        </thead>')
            out.append('        <tbody>')
            for row in d['rows']:
                out.append('          <tr>')
                for td in row:
                    out.append('            <td %s>%s</td>' % (attrs(td), text(td)))
                out.append('          </tr>')
            out.append('        </tbody>')
            out.append('      </table>')
        else:
            raise ValueError(kind)
    return '\n\n'.join(out)


def build(mod):
    t = open(TEMPLATE, encoding='utf-8').read()
    t = t.replace(OLD_SLUG, mod.SLUG)

    title_el = '<title %s>%s</title>' % (attrs(mod.TITLE), text(mod.TITLE))
    t = re.sub(r'<title[^>]*>.*?</title>', title_el, t, count=1, flags=re.S)

    desc_el = '<meta name="description" %s\n      content="%s">' % (attrs(mod.DESC), esc(mod.DESC['zh']))
    t = re.sub(r'<meta name="description".*?>', desc_el, t, count=1, flags=re.S)

    base = 'https://taigetag.com/'
    rel = 'blog/' + mod.SLUG
    hl = ['<link rel="alternate" hreflang="zh-Hant" href="%s%s">' % (base, rel)]
    for l, tag in [('en', 'en'), ('fr', 'fr'), ('es', 'es'), ('ja', 'ja'), ('ko', 'ko')]:
        hl.append('<link rel="alternate" hreflang="%s" href="%s%s/%s">' % (tag, base, l, rel))
    hl.append('<link rel="alternate" hreflang="x-default" href="%s%s">' % (base, rel))
    t = re.sub(r'(<link rel="alternate" hreflang="[^"]*"[^>]*>\s*\n)+', '\n'.join(hl) + '\n', t, count=1)

    crumb = '<span %s>%s</span>' % (attrs(mod.CAT), text(mod.CAT))
    t = re.sub(r'<span data-zh="[^"]*" data-en="[^"]*"[^>]*>[^<]*</span>', crumb, t, count=1)

    h1_el = '<h1 %s>%s</h1>' % (attrs(mod.H1), text(mod.H1))
    t = re.sub(r'<h1 [^>]*>.*?</h1>', h1_el, t, count=1, flags=re.S)

    date_el = '<p %s>%s</p>' % (attrs(mod.DATE), text(mod.DATE))
    t = re.sub(r'<p data-zh="泰閣包裝 · 更新於[^>]*>[^<]*</p>', date_el, t, count=1)

    t = t.replace('"headline": "%s"' % OLD_H1, '"headline": "%s"' % mod.H1['zh'])
    t = t.replace('"name": "%s"' % OLD_H1, '"name": "%s"' % mod.H1['zh'])

    i_art = t.index('<section class="article-body">')
    i_end = t.index('\n\n</main>')
    head = t[:i_art]
    tail = t[i_end:]

    related = ['      <h2 %s>%s</h2>' % (attrs({l: {'zh': '相關文章', 'en': 'Related Articles', 'fr': 'Articles connexes',
                                                    'es': 'Artículos relacionados', 'ja': '関連記事', 'ko': '관련 글'}[l] for l in LANGS}),
                                          '相關文章'),
               '      <ul>']
    for r in mod.RELATED:
        d = {l: r[l] for l in LANGS}
        related.append('        <li><a href="%s" %s>%s</a></li>' % (r['slug'], attrs(d), text(d)))
    related.append('      </ul>')

    cta = ['      <div class="cta-box">',
           '        <p %s>%s</p>' % (attrs(mod.CTA_P), text(mod.CTA_P)),
           '        <a class="cta-btn" href="../contact.html" %s>%s</a>' % (attrs(mod.CTA_BTN), text(mod.CTA_BTN)),
           '      </div>']

    body = '\n\n'.join([render_blocks(mod.BLOCKS), '\n'.join(related), '\n'.join(cta)])

    out = head + '<section class="article-body">\n    <div class="container">\n\n' + body + '\n\n    </div>\n  </section>' + tail
    path = 'blog/' + mod.SLUG
    open(path, 'w', encoding='utf-8', newline='').write(out)
    print('WROTE %s  %d bytes' % (path, len(out.encode('utf-8'))))
    print('  title(zh) %d 字 | desc(en) %d 字符 | desc(zh) %d 字' % (
        len(mod.H1['zh']), len(html.unescape(mod.DESC['en'])), len(html.unescape(mod.DESC['zh']))))


build(A)
build(B)
