#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""日语/韩语上线收尾脚本（在全部 data-ja/data-ko 补齐后运行）

1) 用 gen_i18n.py 为 5 种语言（en/ja/ko/fr/es）重新生成全部 138 个源页面的静态版本
2) 更新 sitemap.xml：为每个源页面补齐 en/ja/ko/fr/es 五种语言的 <url>（zh 为根目录形式）
3) 打印统计与校验结果

用法：
  python build_ja_ko_site.py --dry      # 只报告会做什么
  python build_ja_ko_site.py            # 实际执行生成 + sitemap
"""
import os, re, sys, glob, subprocess, datetime

DRY = '--dry' in sys.argv
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable
TODAY = datetime.date.today().isoformat()
LANGS = ['en', 'ja', 'ko', 'fr', 'es']

SRC = [p for p in ['index.html', 'products.html', 'about.html', 'contact.html', 'blog/index.html']
       if os.path.exists(p)]
SRC += [p for p in sorted(glob.glob('blog/*.html')) if not p.replace('\\', '/').endswith('index.html')]


def zh_url(rel):
    rel = rel.replace('\\', '/')
    if rel == 'index.html':
        return 'https://taigetag.com/'
    return 'https://taigetag.com/' + rel


def lang_url(lang, rel):
    rel = rel.replace('\\', '/')
    u = 'https://taigetag.com/%s/%s' % (lang, rel)
    # 语言根首页用目录形式（与 canonical 规则一致）；blog/index.html 保留后缀
    u = u.replace('https://taigetag.com/%s/index.html' % lang, 'https://taigetag.com/%s/' % lang)
    return u


def gen():
    todo = [(l, p) for l in LANGS for p in SRC]
    if DRY:
        print('[dry] 将执行 gen_i18n.py 次数:', len(todo))
        return
    for l in LANGS:
        args = [PY, 'gen_i18n.py', l] + SRC
        r = subprocess.run(args, capture_output=True, text=True, encoding='utf-8')
        print('gen_i18n %s -> %d 个文件, rc=%d' % (l, len(SRC), r.returncode))
        if r.returncode != 0:
            print(r.stdout[-2000:], r.stderr[-2000:])
            sys.exit(1)


def update_sitemap():
    sm = open('sitemap.xml', encoding='utf-8').read()
    have = set(re.findall(r'<loc>([^<]+)</loc>', sm))
    # 模板：以中文 URL 的 <url> 块为样板
    m = re.search(r'(\s*<url>\s*<loc>[^<]+</loc>.*?</url>)', sm, re.S)
    tpl = m.group(1) if m else None
    assert tpl, '未找到 <url> 模板块'

    def block(url):
        b = tpl
        b = re.sub(r'<loc>[^<]*</loc>', '<loc>%s</loc>' % url, b)
        b = re.sub(r'<lastmod>[^<]*</lastmod>', '<lastmod>%s</lastmod>' % TODAY, b)
        return b

    added_total = 0
    for rel in SRC:
        base = zh_url(rel)
        # 中文 URL 若不存在，先补
        for u in [base] + [lang_url(l, rel) for l in LANGS]:
            if u in have:
                continue
            anchor = re.search(r'<url>\s*<loc>%s</loc>.*?</url>' % re.escape(base), sm, re.S)
            if not anchor:  # 中文块也不存在 → 追加到 </urlset> 前
                sm = sm.replace('</urlset>', block(u) + '\n</urlset>')
            else:
                sm = sm[:anchor.end()] + block(u) + sm[anchor.end():]
            have.add(u)
            added_total += 1
    if DRY:
        print('[dry] 预计新增 sitemap URL:', added_total)
        return
    open('sitemap.xml', 'w', encoding='utf-8', newline='').write(sm)
    print('sitemap 新增 URL 数:', added_total)


if __name__ == '__main__':
    gen()
    update_sitemap()
    if not DRY:
        sm = open('sitemap.xml', encoding='utf-8').read()
        locs = re.findall(r'<loc>([^<]+)</loc>', sm)
        print('sitemap 总 URL 数:', len(locs))
        for l in ('ja', 'ko'):
            print('  /%s/ 下 URL 数: %d' % (l, sum(1 for u in locs if '/%s/' % l in u)))
        miss = [p for p in SRC for l in ('ja', 'ko')
                if not os.path.exists(os.path.join(l, p.replace('\\', '/')))]
        print('缺失的 ja/ko 生成文件数:', len(miss), miss[:5])
