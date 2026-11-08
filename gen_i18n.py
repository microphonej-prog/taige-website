#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把根目录中文版页面转换为 /<lang>/ 独立语言版（静态渲染，SEO 友好）。
支持 en / fr / es / ja / ko。元素缺对应语言 data 属性时回退中文。
用法: python gen_i18n.py en index.html products.html ...
"""
import re, html, os, sys

LANGS = {"en": "en", "fr": "fr", "es": "es", "ja": "ja", "ko": "ko", "de": "de", "pt": "pt"}          # data 属性后缀
LANG_ATTRS = {"en": ("data-en", "data-fr", "data-es"), # 取此语言 / 删这些
              "fr": ("data-fr", "data-zh", "data-es"),
              "es": ("data-es", "data-zh", "data-fr"),
              "ja": ("data-ja", "data-zh", "data-en"),
              "ko": ("data-ko", "data-zh", "data-en"),
              "de": ("data-de", "data-zh", "data-en"),
              "pt": ("data-pt", "data-zh", "data-en")}
# 主语言之间的互链（hreflang 中除自身外的两个）
ALT_PAIRS = {"en": [("fr", "fr/"), ("es", "es/")],
             "fr": [("en", "en/"), ("es", "es/")],
             "es": [("en", "en/"), ("fr", "fr/")],
             "ja": [("en", "en/"), ("ko", "ko/")],
             "ko": [("en", "en/"), ("ja", "ja/")]}

def protect(s):
    """把双引号内的 < 和 > 换成占位符，避免属性值里的 HTML（如 <em>、<strong>）
    破坏正则——只屏蔽 > 时，标签正则仍会锚定在属性值里的 '<strong' 上，导致
    li/p 等元素转换错乱（内容混入其它语言、残留 data-* 属性）"""
    buf, i, in_q = [], 0, False
    while i < len(s):
        c = s[i]
        if c == '"':
            in_q = not in_q
            buf.append(c)
        elif c == '>' and in_q:
            buf.append('__GTH__')
        elif c == '<' and in_q:
            buf.append('__GLT__')
        else:
            buf.append(c)
        i += 1
    return ''.join(buf)

def strip_cjk(s):
    """去掉字符串里的中文字符（用于 alt）"""
    return re.sub(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]+', '', s).strip()

def normalize_cluster(rel_clean):
    """把同一页面的所有语言版本 hreflang 重新对齐（只声明存在且可索引的目标），幂等。"""
    try:
        import fix_hreflang as F
    except Exception:
        return
    for _l in ['zh', 'en', 'de', 'ja', 'ko', 'fr', 'es', 'pt']:
        _p = F.file_for(_l, rel_clean)
        if not os.path.isfile(_p):
            continue
        try:
            _s = open(_p, encoding='utf-8', errors='ignore').read()
        except OSError:
            continue
        if 'noindex' in _s.lower():
            continue
        if not F.ALT_RE.search(_s):
            continue
        _block = F.build_block(_l, rel_clean)
        _first = [True]

        def _rep(mm):
            if _first[0]:
                _first[0] = False
                return _block + "\n"
            return ""

        _new = F.ALT_RE.sub(_rep, _s)
        if _new != _s:
            open(_p, 'w', encoding='utf-8', newline='').write(_new)
            print('  hreflang 同步: %s' % _p.replace(F.ROOT + '/', ''))


FALLBACK = {"de": "data-en", "pt": "data-en"}   # 缺译文时优先英文，绝不回退中文


def convert(lang, src_path, out_path, page_abs_url):
    take, drop_zh, drop_other = LANG_ATTRS[lang]
    fb = FALLBACK.get(lang)
    _src = open(src_path, encoding='utf-8').read()
    has_lang = ('%s="' % take) in _src
    take_any = take if not fb else '(?:%s|%s)' % (take, fb)
    with open(src_path, encoding='utf-8') as f:
        s = f.read()
    s = protect(s)  # 保护引号内 >

    # ---------- 1. html lang ----------
    HTML_LANG = {"en": "en", "fr": "fr", "es": "es", "ja": "ja", "ko": "ko", "de": "de", "pt": "pt"}
    html_lang = HTML_LANG.get(lang, "en")
    s = re.sub(r'<html lang="(?:zh-CN|zh-Hant)"', '<html lang="%s"' % html_lang, s)

    # ---------- 2. title ----------
    m = re.search(r'<title[^>]*%s="([^"]*)"[^>]*>.*?</title>' % take, s, re.S)
    if not m and fb:
        m = re.search(r'<title[^>]*%s="([^"]*)"[^>]*>.*?</title>' % fb, s, re.S)
    if m:
        new_title = html.escape(html.unescape(m.group(1)))
        s = re.sub(r'<title[^>]*>.*?</title>', '<title>%s</title>' % new_title, s, count=1, flags=re.S)

    # ---------- 3. meta description ----------
    m = re.search(r'<meta name="description"[^>]*%s="([^"]*)"[^>]*>' % take, s)
    if not m and fb:
        m = re.search(r'<meta name="description"[^>]*%s="([^"]*)"[^>]*>' % fb, s)
    if m:
        new_desc = html.escape(html.unescape(m.group(1)))
        s = re.sub(r'<meta name="description"[^>]*>',
                   '<meta name="description" content="%s">' % new_desc, s, count=1)

    # ---------- 4. canonical + og:url ----------
    # 仅语言根首页（en/index.html 等）用目录形式（/en/ 而非 /en/index.html），
    # 与 sitemap/hreflang 一致，避免 GSC "备用网页"误判；blog 首页 sitemap 用 index.html，保持不变
    if page_abs_url.endswith('/%s/index.html' % lang):
        page_abs_url = page_abs_url[:-len('index.html')]
    s = re.sub(r'<link rel="canonical"[^>]*>',
               '<link rel="canonical" href="%s">' % page_abs_url, s, count=1)
    s = re.sub(r'<meta property="og:url"[^>]*>',
               '<meta property="og:url" content="%s">' % page_abs_url, s, count=1)
    # 清除源页面已有的 hreflang（防止重复；新 hreflang 在步骤5插入）
    s = re.sub(r'\n?\s*<link rel="alternate" hreflang="[^"]*"[^>]*>\n?', '\n', s)

    # ---------- 5. hreflang（插在 canonical 后，各语言精确到本页面） ----------
    # page_abs_url 形如 https://taigetag.com/fr/blog/xxx.html
    rel_path = page_abs_url.replace('https://taigetag.com/', '')  # fr/blog/xxx.html
    zh_href = page_abs_url.replace('/' + lang + '/', '/')  # https://taigetag.com/blog/xxx.html
    if lang != 'zh':
        zh_href = zh_href.replace('https://taigetag.com/index.html', 'https://taigetag.com/')
    # 逐语言生成 hreflang（语言根首页去 index.html，与 canonical 规则一致）
    HL_TAG = {"en": "en", "fr": "fr", "es": "es", "ja": "ja", "ko": "ko", "de": "de", "pt": "pt-BR"}
    hl_hrefs = {}
    for _l in LANGS:
        _h = 'https://taigetag.com/' + _l + '/' + rel_path.replace(lang + '/', '', 1)
        _h = _h.replace('https://taigetag.com/%s/index.html' % _l, 'https://taigetag.com/%s/' % _l)
        hl_hrefs[_l] = _h
    # 只声明“目标页真实存在且可索引”的语言，避免单向 hreflang / 指向 noindex 或 404
    _rel_clean = rel_path.replace(lang + '/', '', 1)

    def _usable(_l):
        _f = os.path.join(_l, _rel_clean or 'index.html')
        if not os.path.isfile(_f):
            return False
        try:
            _t = open(_f, encoding="utf-8", errors="ignore").read()
        except OSError:
            return False
        return "noindex" not in _t.lower()

    hreflang_lines = ['<link rel="alternate" hreflang="zh-Hant" href="%s">' % zh_href]
    for _l in ["en", "de", "ja", "ko", "fr", "es", "pt"]:
        if _l == lang or _usable(_l):
            hreflang_lines.append('<link rel="alternate" hreflang="%s" href="%s">' % (HL_TAG[_l], hl_hrefs[_l]))
    hreflang_lines.append('<link rel="alternate" hreflang="x-default" href="%s">' % zh_href)
    hreflang = '\n'.join(hreflang_lines)
    s = s.replace('<link rel="canonical" href="%s">' % page_abs_url,
                  '<link rel="canonical" href="%s">\n%s' % (page_abs_url, hreflang), 1)

    # ---------- 6. 带 data-* 的普通元素：文本替换 + 删除多余 data-* ----------
    for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'strong', 'small', 'a', 'span', 'div', 'button', 'li', 'th', 'td',
                'label', 'option', 'figcaption', 'caption', 'dt', 'dd', 'em', 'b', 'i', 'blockquote', 'summary', 'cite']:
        def repl(m):
            attrs, content = m.group(2), m.group(3)
            de = re.search(r'%s="([^"]*)"' % take, attrs)
            if not de and fb:
                de = re.search(r'%s="([^"]*)"' % fb, attrs)
            if not de:
                return m.group(0)
            v = html.unescape(de.group(1))
            # 删除其它语言 data 属性（保留 data-lang 等）
            attrs2 = re.sub(r'\s*data-(?:zh|en|fr|es|ja|ko|de|pt)="[^"]*"', '', attrs)
            if re.search(r'<[a-zA-Z]', v):
                content_new = v  # 含 HTML 标签（如 <em>）→ 原样
            else:
                content_new = html.escape(v)
            return '<%s%s>%s</%s>' % (tag, attrs2, content_new, tag)
        pat = r'<(%s)([^>]*?%s="[^"]*"[^>]*)>(.*?)</%s>' % (tag, take_any, tag)
        s = re.sub(pat, repl, s, flags=re.S)

    # ---------- 6b. 所有 img alt 去中文 ----------
    s = re.sub(r'alt="([^"]*)"',
               lambda m: 'alt="%s"' % re.sub(r'\s+', ' ', strip_cjk(m.group(1))), s)

    # ---------- 7. 相对资源路径修正 ----------
    # blog 页面在 /<lang>/blog/ 下：../css/ -> ../../css/
    s = re.sub(r'(href|src)="\.\./(css|js|images)/', r'\1="../../\2/', s)
    # data-bg 随机背景路径同样处理（逗号分隔多图，全部替换）
    s = re.sub(r'data-bg="([^"]*)"',
               lambda m: 'data-bg="%s"' % m.group(1).replace('../images/', '../../images/'), s)
    # 内联 style 里的 url("../images/...") 同样要回退两级（源仅 blog/index.html 使用）
    s = s.replace('url("../images/', 'url("../../images/')
    s = s.replace("url('../images/", "url('../../images/")
    # 再处理不带前缀的（根目录页面在 /<lang>/ 下：css/ -> ../css/）
    s = re.sub(r'(href|src)="(css|js|images)/', r'\1="../\2/', s)
    # videos/ assets/ 同理
    s = re.sub(r'(href|src)="(videos|assets)/', r'\1="../\2/', s)
    # blog/ 前缀链接保持相对（fr/index.html 里 blog/index.html -> fr/blog/index.html，正确）

    # ---------- 9. 语言切换按钮：本语言高亮 ----------
    s = re.sub(r'<button class="lang-flag active"', '<button class="lang-flag"', s)
    s = re.sub(r'<button class="lang-flag" data-lang="%s"' % lang,
               '<button class="lang-flag active" data-lang="%s"' % lang, s)

    s = s.replace('__GTH__', '>').replace('__GLT__', '<')  # 还原

    # ---------- 10. de/pt：清掉最后一处中文（微信标签 / 客服浮窗） ----------
    if lang in ('de', 'pt'):
        for a, b in (('微信 13128118931', 'WeChat 13128118931'),
                     ('>在線<', '>Online<'),
                     ('>發送<', '>Send<'),
                     ('微信', 'WeChat')):
            s = s.replace(a, b)

    if fb and not has_lang:          # 该语种尚无译文：保持 noindex
        if 'name="robots"' in s:
            s = re.sub(r'<meta name="robots"[^>]*>',
                       '<meta name="robots" content="noindex,follow">', s)
        else:
            s = re.sub(r'</head>',
                       '<meta name="robots" content="noindex,follow"></head>', s, count=1)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(s)
    print('OK  %s -> %s' % (src_path, out_path))
    normalize_cluster(rel_path.replace(lang + '/', '', 1) or 'index.html')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('用法: python gen_i18n.py <en|fr|es|ja|ko> <page1.html> [page2.html ...]')
        sys.exit(1)
    lang = sys.argv[1]
    if lang not in LANGS:
        print('语言必须是 en/fr/es/ja/ko')
        sys.exit(1)
    for p in sys.argv[2:]:
        # 保留相对子目录结构：blog/xxx.html -> en/blog/xxx.html
        rel = p.replace('\\', '/')
        convert(lang, p, os.path.join(lang, rel),
                'https://taigetag.com/%s/%s' % (lang, rel))
