#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把两篇新文章的英文 description 收敛到 150-160 字符（Google 展示长度，与既有文章口径一致）。
只改：根目录中文页的 data-en 属性值 + /en/ 生成页的 meta content。
"""
OLD_NEW = {
    "blog/trim-third-party-testing-guide.html": (
        "Third-party testing for garment trims: when an RSL or regulation makes testing mandatory, which test fits which trim, sample quantities and how to read the report.",
        "Third-party testing for garment trims: when an RSL or regulation makes it mandatory, which test fits which trim, sample sizes and how to read the report.",
    ),
    "blog/sample-room-trims-checklist.html": (
        "A sample room trim checklist: three tiers of standing stock, temporary substitutes when branded parts are late, stock levels and replenishment, plus sample records.",
        "Sample room trim checklist: three tiers of standing stock, temporary substitutes when branded parts are late, stock levels, replenishment and sample records.",
    ),
}

for root, (old, new) in OLD_NEW.items():
    assert 150 <= len(new) <= 160, (root, len(new))
    slug = root.split("/")[-1]
    s = open(root, encoding="utf-8").read()
    assert old in s, "根页未找到旧 desc_en: %s" % root
    s = s.replace('data-en="%s"' % old, 'data-en="%s"' % new, 1)
    open(root, "w", encoding="utf-8", newline="").write(s)

    p2 = "en/blog/%s" % slug
    s2 = open(p2, encoding="utf-8").read()
    assert old in s2, "en 页未找到旧 desc: %s" % p2
    s2 = s2.replace('content="%s"' % old, 'content="%s"' % new, 1)
    open(p2, "w", encoding="utf-8", newline="").write(s2)
    print("OK %-42s desc_en %d -> %d 字符" % (slug, len(old), len(new)))
