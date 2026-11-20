# -*- coding: utf-8 -*-
"""2026-11-20 20:00 批次构建器：以 blog/hang-tag-paper-grain-direction-guide.html 为骨架，
生成两篇新文章的根页（中文默认 + zh/en/fr/es/ja/ko 六语 data-*）。"""
import html
import importlib
import os
import re
import sys

SKELETON = "blog/hang-tag-paper-grain-direction-guide.html"
OLD_SLUG = "hang-tag-paper-grain-direction-guide"
OLD_H1 = "吊牌紙張絲流：翹曲、折線爆裂與打孔撕裂的根因"
LANGS = ["zh", "en", "fr", "es", "ja", "ko"]


def attrs(d):
    missing = [l for l in LANGS if l not in d]
    if missing:
        raise SystemExit("缺语言: %s in %r" % (missing, list(d)[:3]))
    extra = [k for k in d if k not in LANGS]
    if extra:
        raise SystemExit("多余语言键: %s" % extra)
    return " ".join('data-%s="%s"' % (l, html.escape(d[l], quote=True)) for l in LANGS)


def txt(d):
    return html.escape(d["zh"], quote=True)


def render(blocks):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "p":
            out.append('      <p %s>%s</p>' % (attrs(b[1]), txt(b[1])))
        elif kind == "h2":
            out.append('      <h2 %s>%s</h2>' % (attrs(b[1]), txt(b[1])))
        elif kind == "callout":
            out.append('      <div class="callout" %s>%s</div>' % (attrs(b[1]), txt(b[1])))
        elif kind == "ul":
            out.append("      <ul>")
            for li in b[1]:
                out.append('        <li %s>%s</li>' % (attrs(li), txt(li)))
            out.append("      </ul>")
        elif kind == "table":
            head, rows = b[1]
            out.append("      <table>")
            out.append("        <thead>")
            out.append("          <tr>")
            for c in head:
                out.append('            <th %s>%s</th>' % (attrs(c), txt(c)))
            out.append("          </tr>")
            out.append("        </thead>")
            out.append("        <tbody>")
            for r in rows:
                out.append("          <tr>")
                for c in r:
                    out.append('            <td %s>%s</td>' % (attrs(c), txt(c)))
                out.append("          </tr>")
            out.append("        </tbody>")
            out.append("      </table>")
        elif kind == "related":
            out.append('      <h2 %s>%s</h2>' % (
                attrs({"zh": "相關文章", "en": "Related Articles", "fr": "Articles connexes",
                       "es": "Artículos relacionados", "ja": "関連記事", "ko": "관련 글"}),
                "相關文章"))
            out.append("      <ul>")
            for href, d in b[1]:
                out.append('        <li><a href="%s" %s>%s</a></li>' % (href, attrs(d), txt(d)))
            out.append("      </ul>")
        elif kind == "cta":
            pd, bd = b[1]
            out.append('      <div class="cta-box">')
            out.append('        <p %s>%s</p>' % (attrs(pd), txt(pd)))
            out.append('        <a class="cta-btn" href="../contact.html" %s>%s</a>' % (attrs(bd), txt(bd)))
            out.append('      </div>')
        else:
            raise SystemExit("未知块类型: %s" % kind)
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def build(mod_name):
    mod = importlib.import_module(mod_name)
    importlib.reload(mod)
    s = open(SKELETON, encoding="utf-8", newline="").read()
    slug = mod.SLUG

    # 0) 闸门：slug 不得撞车
    if not os.environ.get("REBUILD"):
        for p in ["blog/%s.html" % slug] + ["%s/blog/%s.html" % (l, slug) for l in LANGS[1:]]:
            if os.path.exists(p):
                raise SystemExit("选题撞车：%s 已存在" % p)
        if ("/blog/%s.html</loc>" % slug) in open("sitemap.xml", encoding="utf-8").read():
            raise SystemExit("选题撞车：sitemap 已含 %s" % slug)

    # 1) title
    new_title = '<title %s>%s</title>' % (attrs(mod.TITLE), html.escape(mod.TITLE["zh"], quote=True))
    s, n = re.subn(r"<title[^>]*>.*?</title>", lambda m: new_title, s, count=1, flags=re.S)
    assert n == 1, "title 未替换"

    # 2) description
    new_desc = '<meta name="description" %s\n      content="%s">' % (
        attrs(mod.DESC), html.escape(mod.DESC["zh"], quote=True))
    s, n = re.subn(r'<meta name="description".*?>', lambda m: new_desc, s, count=1, flags=re.S)
    assert n == 1, "description 未替换"

    # 3) canonical + hreflang
    base = "https://taigetag.com/blog/%s.html" % slug
    s, n = re.subn(r'<link rel="canonical" href="[^"]*">',
                   '<link rel="canonical" href="%s">' % base, s, count=1)
    assert n == 1, "canonical 未替换"
    hl = ['<link rel="alternate" hreflang="zh-Hant" href="%s">' % base]
    for l in ["en", "fr", "es", "ja", "ko"]:
        hl.append('<link rel="alternate" hreflang="%s" href="https://taigetag.com/%s/blog/%s.html">' % (l, l, slug))
    hl.append('<link rel="alternate" hreflang="x-default" href="%s">' % base)
    s, n = re.subn(r'(?:<link rel="alternate" hreflang="[^"]*" href="[^"]*">\r?\n)+',
                   "\n".join(hl) + "\n", s, count=1)
    assert n == 1, "hreflang 块未替换"

    # 4) JSON-LD 里的 slug 与标题
    s = s.replace("https://taigetag.com/blog/%s.html" % OLD_SLUG, base)
    s = s.replace("https://taigetag.com/en/blog/%s.html" % OLD_SLUG, "https://taigetag.com/en/blog/%s.html" % slug)
    old_bc = '"name": "%s"' % OLD_H1
    assert old_bc in s, "JSON-LD 面包屑名未找到"
    s = s.replace(old_bc, '"name": "%s"' % mod.H1["zh"])
    old_hl = '"headline": "%s"' % OLD_H1
    assert old_hl in s, "JSON-LD headline 未找到"
    s = s.replace(old_hl, '"headline": "%s"' % mod.H1["zh"])

    # 5) crumb 末段分类
    i0 = s.index('<div class="crumb">')
    i1 = s.index("</div>", i0)
    crumb = s[i0:i1]
    j0 = crumb.rindex("<span ")
    j1 = crumb.index("</span>", j0) + len("</span>")
    new_span = '<span %s>%s</span>' % (attrs(mod.CATEGORY), html.escape(mod.CATEGORY["zh"], quote=True))
    s = s[:i0] + crumb[:j0] + new_span + crumb[j1:] + s[i1:]

    # 6) h1
    new_h1 = '<h1 %s>%s</h1>' % (attrs(mod.H1), html.escape(mod.H1["zh"], quote=True))
    s, n = re.subn(r"<h1[^>]*>[^<]*</h1>", lambda m: new_h1, s, count=1)
    assert n == 1, "h1 未替换"

    # 7) 正文
    start = '  <section class="article-body">\n    <div class="container">\n'
    end = "\n    </div>\n  </section>\n\n</main>"
    a = s.index(start) + len(start)
    b = s.index(end, a)
    body = render(mod.BLOCKS)
    s = s[:a] + "\n" + body + s[b:]

    out_path = "blog/%s.html" % slug
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(s)
    for l in LANGS:
        c = len(re.findall(r'data-%s="' % l, s))
        print("  %s: %d 个 data 属性" % (l, c))
    print("WROTE %s (%d bytes) desc_en=%d chars" % (out_path, len(s.encode("utf-8")), len(mod.DESC["en"])))
    return out_path


if __name__ == "__main__":
    for m in sys.argv[1:] or ["body_20261120d_a", "body_20261120d_b"]:
        build(m)
