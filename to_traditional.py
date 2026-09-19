#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把站点的中文版从简体转为繁体（OpenCC s2t，只动中文，绝不动 en/fr/es/ja/ko）

规则：
- 文本节点（<script>/<style> 之外）：转
- 属性：data-zh / data-zh-ph / alt / aria-label / title / <meta> 的 content：转
- <script type="application/ld+json">：转（JSON-LD 里的中文实体名）
- 其他 <script>/<style> 内容：不动
- data-en/data-fr/data-es/data-ja/data-ko 的值：绝不动（日语汉字会被 s2t 误转）
- lang 语义：<html lang="zh-CN"> → zh-Hant；hreflang="zh-CN" → zh-Hant；"zh-CN"（inLanguage）→ zh-Hant
- 语言旗帜 title="中文" → title="繁體中文"
用法: python to_traditional.py [--apply] [file...]   默认 dry-run 只报告
"""
import re, sys, glob
from opencc import OpenCC

CC = OpenCC('s2t')
APPLY = '--apply' in sys.argv
FILES = [a for a in sys.argv[1:] if not a.startswith('--')]
if not FILES:
    FILES = (['index.html', 'products.html', 'about.html', 'contact.html', 'blog/index.html']
             + sorted(glob.glob('blog/*.html')))

ATTRS = ('data-zh', 'data-zh-ph', 'alt', 'aria-label', 'title')
STATS = {'text': 0, 'attr': 0, 'jsonld': 0, 'lang': 0}


def conv(s):
    return CC.convert(s)


def conv_attrs(tag):
    """转换白名单属性值；顺带处理 lang/hreflang 语义"""
    def repl(m):
        name, val = m.group(1), m.group(2)
        if name in ATTRS and re.search(r'[\u4e00-\u9fff]', val):
            STATS['attr'] += 1
            new = conv(val)
            if name == 'title' and val.strip() == '中文':
                new = '繁體中文'
            return '%s="%s"' % (name, new)
        if name == 'content' and re.search(r'[\u4e00-\u9fff]', val):
            STATS['attr'] += 1
            return 'content="%s"' % conv(val)
        if name in ('lang', 'hreflang') and val == 'zh-CN':
            STATS['lang'] += 1
            return '%s="zh-Hant"' % name
        return m.group(0)
    return re.sub(r'([a-zA-Z-]+)="([^"]*)"', repl, tag)


def convert_html(s):
    out, i, n = [], 0, len(s)
    while i < n:
        if s[i] == '<':
            j, in_q = i + 1, None
            while j < n:
                ch = s[j]
                if in_q:
                    if ch == in_q:
                        in_q = None
                elif ch in '"\'':
                    in_q = ch
                elif ch == '>':
                    break
                j += 1
            tag = s[i:j + 1] if j < n else s[i:]
            low = tag.lower()
            if low.startswith('<script') or low.startswith('<style'):
                closing = '</script>' if low.startswith('<script') else '</style>'
                k = s.lower().find(closing, j)
                body = s[j + 1:k] if k != -1 else s[j + 1:]
                if 'application/ld+json' in low:
                    body = conv(body)
                    STATS['jsonld'] += 1
                out.append(tag)
                out.append(body)
                if k != -1:
                    out.append(closing)
                    i = k + len(closing)
                else:
                    i = n
                continue
            out.append(conv_attrs(tag))
            i = j + 1
        else:
            j = s.find('<', i)
            if j == -1:
                j = n
            chunk = s[i:j]
            if re.search(r'[\u4e00-\u9fff]', chunk):
                STATS['text'] += 1
                chunk = conv(chunk)
            out.append(chunk)
            i = j
    return ''.join(out)


def convert_js(path):
    """main.js 整体转（无日韩字符串）；assist.js 只转 T.zh 块，并给关键词补简体变体"""
    s = open(path, encoding='utf-8').read()
    if path.endswith('assist.js'):
        m = re.search(r'(  T\.zh = \{)(.*?)(\n  \};)', s, re.S)
        if not m:
            print('  !! assist.js 未找到 T.zh 块')
            return 0
        block = m.group(2)
        # 先整块转繁体，再给关键词数组补上简体变体（顺序反了会把简体变体又转回繁体，产生重复项）
        block = conv(block)

        def kws(m2):
            inner = m2.group(1)
            # 繁体原词 + 简体变体，去重后重写（保证重复运行幂等，不会重复追加）
            words = re.findall(r'"([^"]*)"', inner)
            seen, uniq = set(), []
            for w in words:
                if w not in seen:
                    seen.add(w); uniq.append(w)
            extra = []
            for w in uniq:
                b = OpenCC('t2s').convert(w)
                if b != w and b not in seen:
                    seen.add(b); extra.append(b)
            return 'kws: [%s]' % ', '.join('"%s"' % w for w in uniq + extra)
        block = re.sub(r'kws: \[([^\]]*)\]', kws, block)
        s2 = s[:m.start(2)] + block + s[m.end(2):]
        changed = s2 != s
    else:
        s2 = conv(s)
        # main.js 的语言代码映射也要跟着改（文本转换不覆盖 JS 里的代码串）
        s2 = s2.replace('zh: "zh-CN"', 'zh: "zh-Hant"')
        changed = s2 != s
    if changed and APPLY:
        open(path, 'w', encoding='utf-8', newline='').write(s2)
    return int(changed)


if __name__ == '__main__':
    print('模式:', 'APPLY（写盘）' if APPLY else 'DRY-RUN（不写盘）')
    total = 0
    for f in FILES:
        s0 = open(f, encoding='utf-8').read()
        s = convert_html(s0)
        if s != s0:
            total += 1
            if APPLY:
                open(f, 'w', encoding='utf-8', newline='').write(s)
    print('HTML 文件改动: %d / %d' % (total, len(FILES)))
    for js in ('js/main.js', 'js/assist.js'):
        print('%-14s 改动: %d' % (js, convert_js(js)))
    print('统计:', STATS)
