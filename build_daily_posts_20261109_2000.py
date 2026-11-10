#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-09 20:00 每日文章：生成两篇新文章（8 语骨架）+ blog/index.html 卡片。

正文内容在 F:/hermes/cache/scratch/c_*_20261109.py（英文主稿 + 七语翻译）。
骨架 = blog/trim-material-substitution-guide.html（八语头尾齐全）。
"""
import html
import importlib.util
import os
import re
import sys

SKEL = "blog/trim-material-substitution-guide.html"
LANGS = ["zh", "en", "fr", "es", "ja", "ko", "de", "pt"]
DATES = {
    "zh": "2026年11月9日", "en": "November 9, 2026", "fr": "9 novembre 2026",
    "es": "9 de noviembre de 2026", "ja": "2026年11月9日", "ko": "2026년 11월 9일",
    "de": "9. November 2026", "pt": "9 de novembro de 2026",
}


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def A(d):
    """八语 data 属性（值做 HTML 转义，禁止裸双引号/裸 &）"""
    missing = [l for l in LANGS if not d.get(l)]
    assert not missing, "缺语言: %s" % missing
    return " ".join('data-%s="%s"' % (l, html.escape(d[l], quote=True)) for l in LANGS)


def body_html(blocks):
    out = ['  <section class="article-body">', '    <div class="container">', ""]
    for kind, payload in blocks:
        if kind in ("p", "h2", "h3", "callout"):
            cls = ' class="callout"' if kind == "callout" else ""
            tag = "div" if kind == "callout" else kind
            out.append('      <%s%s %s>%s</%s>' % (tag, cls, A(payload), html.escape(payload["zh"]), tag))
            out.append("")
        elif kind == "ul":
            out.append("      <ul>")
            for li in payload:
                out.append('        <li %s>%s</li>' % (A(li), html.escape(li["zh"])))
            out.append("      </ul>")
            out.append("")
        elif kind == "table":
            out.append("      <table>")
            out.append("        <thead>")
            out.append("          <tr>")
            for th in payload["head"]:
                out.append('            <th %s>%s</th>' % (A(th), html.escape(th["zh"])))
            out.append("          </tr>")
            out.append("        </thead>")
            out.append("        <tbody>")
            for row in payload["rows"]:
                out.append("          <tr>")
                for td in row:
                    out.append('            <td %s>%s</td>' % (A(td), html.escape(td["zh"])))
                out.append("          </tr>")
            out.append("        </tbody>")
            out.append("      </table>")
            out.append("")
    return "\n".join(out)


def build(c, skel, idx_html):
    slug = c["slug"]
    s = skel

    t = '<title %s>%s</title>' % (A(c["title"]), html.escape(c["title"]["zh"]))
    s, n = re.subn(r"<title[^>]*>.*?</title>", lambda m: t, s, count=1, flags=re.S)
    assert n == 1, "title 替换失败"

    d = '<meta name="description" %s content="%s">' % (A(c["desc"]), html.escape(c["desc"]["zh"], quote=True))
    s, n = re.subn(r'<meta name="description".*?>', lambda m: d, s, count=1, flags=re.S)
    assert n == 1, "description 替换失败"

    href = '<link rel="canonical" href="https://taigetag.com/blog/%s">\n' % slug
    href += '<link rel="alternate" hreflang="zh-Hant" href="https://taigetag.com/blog/%s">\n' % slug
    for l in ("en", "de", "ja", "ko", "fr", "es"):
        href += '<link rel="alternate" hreflang="%s" href="https://taigetag.com/%s/blog/%s">\n' % (l, l, slug)
    href += '<link rel="alternate" hreflang="pt-BR" href="https://taigetag.com/pt/blog/%s">\n' % slug
    href += '<link rel="alternate" hreflang="x-default" href="https://taigetag.com/blog/%s">' % slug
    s, n = re.subn(r'<link rel="canonical" href="[^"]*">(?:\n<link rel="alternate"[^\n]*>)+',
                   lambda m: href, s, count=1)
    assert n == 1, "hreflang 替换失败"

    crumb = ('<div class="crumb"><a href="../index.html" data-zh="首頁" data-en="Home" data-fr="Accueil" '
             'data-es="Inicio" data-ja="ホーム" data-ko="홈" data-de="Startseite" data-pt="Início">首頁</a>'
             ' / <a href="index.html" data-zh="輔料 FAQ" data-en="Trims FAQ" data-fr="FAQ Accessoires" '
             'data-es="FAQ Accesorios" data-ja="副資材 FAQ" data-ko="부자재 FAQ" data-de="Accessoires-FAQ" '
             'data-pt="FAQ de aviamentos">輔料 FAQ</a>'
             ' / <span %s>%s</span></div>' % (A(c["crumb"]), html.escape(c["crumb"]["zh"])))
    s, n = re.subn(r'<div class="crumb">.*?</div>', lambda m: crumb, s, count=1, flags=re.S)
    assert n == 1, "crumb 替换失败"

    h1 = '<h1 %s>%s</h1>' % (A(c["h1"]), html.escape(c["h1"]["zh"]))
    s, n = re.subn(r"<h1 [^>]*>.*?</h1>", lambda m: h1, s, count=1, flags=re.S)
    assert n == 1, "h1 替换失败"

    meta = ('<p data-zh="泰閣包裝 · 更新於 %s" data-en="By TAGE Packaging &nbsp;·&nbsp; Updated %s" '
            'data-ja="泰閣包装 · %s更新" data-ko="TAGE 패키징 · %s 업데이트" '
            'data-fr="Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le %s" '
            'data-es="Por TAGE Packaging &nbsp;·&nbsp; Actualizado el %s" '
            'data-de="Von TAGE Packaging &nbsp;·&nbsp; Aktualisiert am %s" '
            'data-pt="Por TAGE Packaging &nbsp;·&nbsp; Atualizado em %s">泰閣包裝 · 更新於 %s</p>'
            % (DATES["zh"], DATES["en"], DATES["ja"], DATES["ko"], DATES["fr"], DATES["es"],
               DATES["de"], DATES["pt"], DATES["zh"]))
    s, n = re.subn(r'<p data-zh="泰閣包裝 · 更新於.*?</p>', lambda m: meta, s, count=1, flags=re.S)
    assert n == 1, "日期行替换失败"

    skel_name = re.search(r'"position": 3,\s*"name": "([^"]*)"', skel).group(1)
    s = s.replace('"%s"' % skel_name, '"%s"' % c["h1"]["zh"])
    s, n = re.subn(r'"headline": "[^"]*"', lambda m: '"headline": "%s"' % c["h1"]["zh"], s, count=1)
    assert n == 1, "headline 替换失败"

    i0 = s.index('  <section class="article-body">')
    i1 = s.index("\n</main>")
    body = body_html(c["blocks"]).rstrip("\n")
    body += '\n\n      <h2 %s>相關文章</h2>\n\n      <ul>\n' % A({
        "zh": "相關文章", "en": "Related reading", "fr": "À lire aussi", "es": "Lecturas relacionadas",
        "ja": "関連記事", "ko": "관련 글", "de": "Weiterlesen", "pt": "Leia também"})
    for target, label in c["related"]:
        body += '        <li><a href="%s" %s>%s</a></li>\n' % (target, A(label), html.escape(label["zh"]))
    body += "      </ul>\n\n"
    body += ('      <div class="cta-box">\n        <p %s>%s</p>\n        <a class="cta-btn" href="../contact.html" %s>%s</a>\n      </div>'
             % (A(c["cta"]["p"]), html.escape(c["cta"]["p"]["zh"]),
                A(c["cta"]["a"]), html.escape(c["cta"]["a"]["zh"])))
    body += "\n\n    </div>\n  </section>\n"  # 骨架的 </div></section> 被 i0..i1 切掉，必须补回，否则文章结构破损
    s = s[:i0] + body + s[i1:]

    out = "blog/%s" % slug
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(s)
    counts = {l: len(re.findall(r'data-%s="' % l, s)) for l in LANGS}
    print("写入 %s (%d 字节) 属性计数 %s desc_en=%d 字符"
          % (out, len(s.encode("utf-8")), counts, len(c["desc"]["en"])))

    slug_in_idx = slug in idx_html
    card = ('\n      <article class="post-card">\n'
            '        <span class="tag" %s>%s</span>\n'
            '        <h3 %s>%s</h3>\n'
            '        <p %s>%s</p>\n'
            '        <a class="more" href="%s" data-zh="閱讀全文 →" data-en="Read more →" data-fr="Lire la suite →" '
            'data-es="Leer más →" data-ja="続きを読む →" data-ko="자세히 보기 →" data-de="Weiterlesen →" '
            'data-pt="Ler mais →">閱讀全文 →</a>\n'
            '      </article>\n'
            % (A(c["card"]["tag"]), html.escape(c["card"]["tag"]["zh"]),
               A(c["h1"]), html.escape(c["h1"]["zh"]),
               A(c["card"]["p"]), html.escape(c["card"]["p"]["zh"]), slug))
    return card, slug_in_idx


def main():
    sets = [
        ("F:/hermes/cache/scratch/c_tw_meta_20261109.py",
         "F:/hermes/cache/scratch/c_tw_b1_20261109.py",
         "F:/hermes/cache/scratch/c_tw_b2_20261109.py"),
        ("F:/hermes/cache/scratch/c_fa_meta_20261109.py",
         "F:/hermes/cache/scratch/c_fa_b1_20261109.py",
         "F:/hermes/cache/scratch/c_fa_b2_20261109.py"),
    ]
    contents = []
    for mp, p1, p2 in sets:
        meta = load(mp, "m_" + os.path.basename(mp)).META
        blocks = load(p1, "b1_" + os.path.basename(p1)).BLOCKS + load(p2, "b2_" + os.path.basename(p2)).BLOCKS
        c = dict(meta)
        c["blocks"] = blocks
        contents.append(c)

    skel = open(SKEL, encoding="utf-8", newline="").read()
    idx_path = "blog/index.html"
    idx = open(idx_path, encoding="utf-8", newline="").read()
    sitemap = open("sitemap.xml", encoding="utf-8").read()

    for c in contents:
        slug = c["slug"]
        for p in ["blog/" + slug, "en/blog/" + slug, "de/blog/" + slug, "pt/blog/" + slug]:
            assert not os.path.exists(p), "选题撞车：%s 已存在" % p
        assert "/blog/%s</loc>" % slug not in sitemap, "选题撞车：sitemap 已含 %s" % slug
    print("选题全新，开始生成")

    cards = ""
    for c in contents:
        card, dup = build(c, skel, idx)
        assert not dup, "卡片已存在：%s" % c["slug"]
        cards += card

    nl = "\r\n" if "\r\n" in idx else "\n"
    marker = '<div class="post-grid">' + nl
    assert marker in idx, "post-grid 未找到"
    idx = idx.replace(marker, marker + cards.replace("\n", nl), 1)
    with open(idx_path, "w", encoding="utf-8", newline="") as f:
        f.write(idx)
    print("blog/index.html 插入 2 张卡片")


if __name__ == "__main__":
    sys.exit(main())
