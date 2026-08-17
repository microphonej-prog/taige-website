#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把根目录中文版页面转换为 /<lang>/ 独立语言版（静态渲染，SEO 友好）。
支持 en / fr / es。元素缺对应语言 data 属性时回退中文。
用法: python gen_i18n.py en index.html products.html ...
"""
import re, html, os, sys

LANGS = {"en": "en", "fr": "fr", "es": "es"}          # data 属性后缀
LANG_ATTRS = {"en": ("data-en", "data-fr", "data-es"), # 取此语言 / 删这些
              "fr": ("data-fr", "data-zh", "data-es"),
              "es": ("data-es", "data-zh", "data-fr")}
# 主语言之间的互链（hreflang 中除自身外的两个）
ALT_PAIRS = {"en": [("fr", "?lang=fr"), ("es", "?lang=es")],
             "fr": [("en", "en/"), ("es", "?lang=es")],
             "es": [("en", "en/"), ("fr", "?lang=fr")]}

def protect(s):
    """把双引号内的 > 换成占位符，避免属性值里的 HTML（如 <em>）破坏正则"""
    buf, i, in_q = [], 0, False
    while i < len(s):
        c = s[i]
        if c == '"':
            in_q = not in_q
            buf.append(c)
        elif c == '>' and in_q:
            buf.append('__GTH__')
        else:
            buf.append(c)
        i += 1
    return ''.join(buf)

def strip_cjk(s):
    """去掉字符串里的中文字符（用于 alt）"""
    return re.sub(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]+', '', s).strip()

def convert(lang, src_path, out_path, page_abs_url):
    take, drop_zh, drop_other = LANG_ATTRS[lang]
    with open(src_path, encoding='utf-8') as f:
        s = f.read()
    s = protect(s)  # 保护引号内 >

    # ---------- 1. html lang ----------
    html_lang = "fr" if lang == "fr" else ("es" if lang == "es" else "en")
    s = re.sub(r'<html lang="zh-CN">', '<html lang="%s">' % html_lang, s)

    # ---------- 2. title ----------
    m = re.search(r'<title[^>]*%s="([^"]*)"[^>]*>.*?</title>' % take, s, re.S)
    if m:
        new_title = html.escape(html.unescape(m.group(1)))
        s = re.sub(r'<title[^>]*>.*?</title>', '<title>%s</title>' % new_title, s, count=1, flags=re.S)

    # ---------- 3. meta description ----------
    m = re.search(r'<meta name="description"[^>]*%s="([^"]*)"[^>]*>' % take, s)
    if m:
        new_desc = html.escape(html.unescape(m.group(1)))
        s = re.sub(r'<meta name="description"[^>]*>',
                   '<meta name="description" content="%s">' % new_desc, s, count=1)

    # ---------- 4. canonical + og:url ----------
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
    en_href = 'https://taigetag.com/en/' + rel_path.replace(lang + '/', '', 1)
    fr_href = 'https://taigetag.com/fr/' + rel_path.replace(lang + '/', '', 1)
    es_href = 'https://taigetag.com/es/' + rel_path.replace(lang + '/', '', 1)
    en_href = en_href.replace('https://taigetag.com/en/index.html', 'https://taigetag.com/en/')
    fr_href = fr_href.replace('https://taigetag.com/fr/index.html', 'https://taigetag.com/fr/')
    es_href = es_href.replace('https://taigetag.com/es/index.html', 'https://taigetag.com/es/')
    hreflang_lines = [
        '<link rel="alternate" hreflang="zh-CN" href="%s">' % zh_href,
        '<link rel="alternate" hreflang="en" href="%s">' % en_href,
        '<link rel="alternate" hreflang="fr" href="%s">' % fr_href,
        '<link rel="alternate" hreflang="es" href="%s">' % es_href,
        '<link rel="alternate" hreflang="x-default" href="%s">' % zh_href,
    ]
    hreflang = '\n'.join(hreflang_lines)
    s = s.replace('<link rel="canonical" href="%s">' % page_abs_url,
                  '<link rel="canonical" href="%s">\n%s' % (page_abs_url, hreflang), 1)

    # ---------- 6. 带 data-* 的普通元素：文本替换 + 删除多余 data-* ----------
    for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'strong', 'small', 'a', 'span', 'div', 'button', 'li']:
        def repl(m):
            attrs, content = m.group(2), m.group(3)
            de = re.search(r'%s="([^"]*)"' % take, attrs)
            if not de:
                return m.group(0)
            v = html.unescape(de.group(1))
            # 删除其它语言 data 属性（保留 data-lang 等）
            attrs2 = re.sub(r'\s*data-(?:zh|en|fr|es)="[^"]*"', '', attrs)
            if re.search(r'<[a-zA-Z]', v):
                content_new = v  # 含 HTML 标签（如 <em>）→ 原样
            else:
                content_new = html.escape(v)
            return '<%s%s>%s</%s>' % (tag, attrs2, content_new, tag)
        pat = r'<(%s)([^>]*?%s="[^"]*"[^>]*)>(.*?)</%s>' % (tag, take, tag)
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
    # 再处理不带前缀的（根目录页面在 /<lang>/ 下：css/ -> ../css/）
    s = re.sub(r'(href|src)="(css|js|images)/', r'\1="../\2/', s)
    # videos/ assets/ 同理
    s = re.sub(r'(href|src)="(videos|assets)/', r'\1="../\2/', s)
    # blog/ 前缀链接保持相对（fr/index.html 里 blog/index.html -> fr/blog/index.html，正确）

    # ---------- 9. 语言切换按钮：本语言高亮 ----------
    s = re.sub(r'<button class="lang-flag active" data-lang="zh"', '<button class="lang-flag" data-lang="zh"', s)
    s = re.sub(r'<button class="lang-flag" data-lang="%s"' % lang,
               '<button class="lang-flag active" data-lang="%s"' % lang, s)

    s = s.replace('__GTH__', '>')  # 还原

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(s)
    print('OK  %s -> %s' % (src_path, out_path))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('用法: python gen_i18n.py <en|fr|es> <page1.html> [page2.html ...]')
        sys.exit(1)
    lang = sys.argv[1]
    if lang not in LANGS:
        print('语言必须是 en/fr/es')
        sys.exit(1)
    for p in sys.argv[2:]:
        # 保留相对子目录结构：blog/xxx.html -> en/blog/xxx.html
        rel = p.replace('\\', '/')
        convert(lang, p, os.path.join(lang, rel),
                'https://taigetag.com/%s/%s' % (lang, rel))
