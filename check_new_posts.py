#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描文章：属性引号畸形 + .article-body 内 data-fr/data-es 缺失（引号感知版）"""
import re, sys

TAGS = "p|h1|h2|h3|h4|li|td|th|div|span|a|strong|small|button|em"

def protect(s):
    """引号内的 < > 换成占位符，避免属性值里的 HTML 破坏标签正则"""
    buf, in_q = [], False
    for c in s:
        if c == '"':
            in_q = not in_q
            buf.append(c)
        elif c == '>' and in_q:
            buf.append('__GTH__')
        elif c == '<' and in_q:
            buf.append('__GLT__')
        else:
            buf.append(c)
    return ''.join(buf)

def check(path, verbose=True):
    raw = open(path, encoding="utf-8").read()
    s = protect(raw)
    # 1) 崩溃式引号嵌套（如 data-en=""text"）
    bad = re.findall(r'data-(?:zh|en|fr|es)=""[^\s>]', s)
    # 2) article-body 内每个带 data-* 的元素必须有四语
    i0 = s.find('<section class="article-body">')
    i1 = s.find('</section>', i0)
    body = s[i0:i1]
    pat = re.compile(r'<(%s)(\s[^>]*?)>' % TAGS)
    miss, total = [], 0
    for m in pat.finditer(body):
        attrs = m.group(0)
        if not re.search(r'data-(?:zh|en|fr|es)="', attrs):
            continue
        total += 1
        lack = [l for l in ("zh", "en", "fr", "es") if not re.search(r'data-%s="[^"]*"' % l, attrs)]
        if lack:
            miss.append((lack, re.sub(r'\s+', ' ', attrs)[:100]))
    print("%s: 四语元素 %d 个 | 缺语言 %d 个 | 崩溃式引号 %d 处" % (path, total, len(miss), len(bad)))
    if verbose:
        for lack, a in miss[:15]:
            print("   MISS %s -> %s" % (','.join(lack), a))
        for b in bad[:10]:
            print("   BAD -> %s" % b)
    return len(miss) + len(bad)

targets = sys.argv[1:] or ["blog/clothing-label-compliance-japan.html", "blog/paper-bag-cost-guide.html"]
rc = sum(check(t) for t in targets)
print("TOTAL ISSUES:", rc)
sys.exit(1 if rc else 0)
