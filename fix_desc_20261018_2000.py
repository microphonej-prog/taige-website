#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-18 20:00 批次：修正第一篇 desc 长度（zh<=120 / en<=160）并重新生成五语版本"""
import os, re, sys, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

from daily_meta_20261018_2000 import ARTICLES

a = ARTICLES[0]
slug = a["slug"]
print("desc_zh=%d desc_en=%d" % (len(a["desc_zh"]), len(a["desc_en"])))
assert len(a["desc_zh"]) <= 120 and len(a["desc_en"]) <= 160

p = "blog/%s" % slug
s = open(p, encoding="utf-8").read()
desc_block = ('<meta name="description" data-zh="%s"\n'
              '      data-en="%s" data-ja="%s" data-ko="%s"\n'
              '      data-fr="%s"\n'
              '      data-es="%s"\n'
              '      content="%s">' % (a["desc_zh"], a["desc_en"], a["desc_ja"], a["desc_ko"],
                                       a["desc_fr"], a["desc_es"], a["desc_zh"]))
s2, n = re.subn(r'<meta name="description".*?>', desc_block, s, count=1, flags=re.S)
assert n == 1, "desc 替换失败"
open(p, "w", encoding="utf-8", newline="").write(s2)
print("已更新 %s" % p)

for lang in ["en", "ja", "ko", "fr", "es"]:
    r = subprocess.run([sys.executable, "gen_i18n.py", lang, p], capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print(r.stdout[-2000:], r.stderr[-2000:])
        raise SystemExit("gen_i18n %s 失败" % lang)
    print("gen_i18n %s ok" % lang)
