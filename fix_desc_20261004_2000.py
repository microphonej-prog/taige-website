#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 webbing 文章的英文 description 收进 Google 显示长度（<=158 字符），
同步 meta 文件、根中文页 data-en、en/ 生成页静态 content。幂等。"""
import io, re, os

OLD = ("Webbing guide: plain, twill, herringbone and jacquard structures, polyester, "
       "nylon, PP and rPET choices, plus width, weight and strength specs to agree before ordering.")
NEW = ("Webbing guide: plain, twill, herringbone and jacquard structures, polyester, "
       "nylon, PP and rPET choices, plus width, weight and strength specs.")

assert len(NEW) <= 158, len(NEW)
print("新 desc_en 长度 = %d 字符" % len(NEW))

TARGETS = ["daily_meta_20261004_2000.py",
           "blog/webbing-tape-selection-guide.html",
           "en/blog/webbing-tape-selection-guide.html"]

for p in TARGETS:
    s = open(p, encoding="utf-8").read()
    n = s.count(OLD)
    if n == 0 and s.count(NEW):
        print("  %-52s 已是新版，跳过" % p)
        continue
    s = s.replace(OLD, NEW)
    open(p, "w", encoding="utf-8", newline="").write(s)
    print("  %-52s 替换 %d 处" % (p, n))

# 复核各语言 description 长度
print("\n== description 长度复核 ==")
for lang, key in [("zh", "data-zh"), ("en", "data-en"), ("ja", "data-ja"), ("ko", "data-ko"),
                  ("fr", "data-fr"), ("es", "data-es")]:
    p = "blog/webbing-tape-selection-guide.html"
    s = open(p, encoding="utf-8").read()
    m = re.search(r'<meta name="description"[^>]*%s="([^"]*)"' % key, s, re.S)
    m2 = re.search(r'<meta name="description" data-zh="[^"]*"', s, re.S)
    # 统一取属性
    blk = re.search(r'<meta name="description".*?>', s, re.S).group(0)
    v = re.search(r'%s="([^"]*)"' % key, blk).group(1)
    print("  webbing %-3s = %d" % (lang, len(v)))
