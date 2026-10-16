#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os, glob
for f in ['blog/clothing-price-ticket-guide.html', 'blog/apparel-relabeling-service-guide.html',
          'blog/hang-tag-vs-sticker.html', 'blog/trim-order-change-cancellation-guide.html',
          'blog/trim-pre-production-sample-guide.html', 'blog/trim-order-contract-terms-guide.html',
          'blog/secondhand-resale-apparel-label-guide.html', 'blog/small-batch-fast-reorder-trims.html',
          'blog/trim-tooling-ownership-guide.html', 'blog/garment-trims-quality-inspection.html']:
    if not os.path.exists(f):
        print('缺文件', f); continue
    s = open(f, encoding='utf-8').read()
    print('=== %s ===' % f)
    for h in re.findall(r'<h2 data-zh="([^"]*)"', s):
        print('  H2:', h[:70])
    for k in ['促銷', '折扣', '清倉', 'Omnibus', '原價', '變更', '版次', '版本號', 'ECN', '復驗']:
        c = s.count(k)
        if c:
            print('  kw %s=%d' % (k, c))
print()
print('--- slug 撞车检查 ---')
for slug in ['promotional-hangtag-discount-guide.html', 'trim-engineering-change-guide.html']:
    paths = ['blog/%s' % slug] + ['%s/blog/%s' % (l, slug) for l in ['en', 'ja', 'ko', 'fr', 'es']]
    print(slug, [p for p in paths if os.path.exists(p)] or 'OK 全新')
sm = open('sitemap.xml', encoding='utf-8').read()
for slug in ['promotional-hangtag-discount-guide.html', 'trim-engineering-change-guide.html']:
    print(slug, 'sitemap命中' if slug in sm else 'sitemap OK')
