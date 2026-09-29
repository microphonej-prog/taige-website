#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-29 晚间批次：按修正后的 desc 重新刷写两篇根页面的 title/description，
再重跑 gen_i18n 生成五语版本（sitemap / 卡片 / BUST_VERSION 已在 daily_gen 中完成，不重复）。

用法: <tools venv python> refresh_meta_20260929_evening.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable
LANGS = ["en", "ja", "ko", "fr", "es"]

from daily_meta_20260929_evening import ARTICLES

spec = importlib.util.spec_from_file_location("to_traditional", os.path.join(ROOT, "to_traditional.py"))
tt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tt)

TARGETS = []
for a in ARTICLES:
    p = "blog/%s" % a["slug"]
    s = open(p, encoding="utf-8", newline="").read()

    title_line = ('<title data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</title>'
                  % (a["title_zh"], a["title_en"], a["title_ja"], a["title_ko"],
                     a["title_fr"], a["title_es"], a["title_zh"]))
    s, n1 = re.subn(r'<title[^>]*>.*?</title>', lambda m: title_line, s, count=1, flags=re.S)
    assert n1 == 1, "title 替换失败"

    s = re.sub(r'<meta name="description".*?content="[^"]*">', 'DESC_PLACEHOLDER', s, count=1, flags=re.S)
    desc_block = ('<meta name="description" data-zh="%s"\n'
                  '      data-en="%s" data-ja="%s" data-ko="%s"\n'
                  '      data-fr="%s"\n'
                  '      data-es="%s"\n'
                  '      content="%s">' % (a["desc_zh"], a["desc_en"], a["desc_ja"], a["desc_ko"],
                                           a["desc_fr"], a["desc_es"], a["desc_zh"]))
    assert 'DESC_PLACEHOLDER' in s, "desc 占位未落位"
    s = s.replace('DESC_PLACEHOLDER', desc_block, 1)

    s = tt.convert_html(s)  # 简 → 繁（幂等；已有繁体不重复转）
    open(p, "w", encoding="utf-8", newline="").write(s)
    print("刷写 %s  title=%d字符 desc_zh=%d字 desc_en=%d字符 desc_fr=%d"
          % (p, len(a["title_zh"]), len(a["desc_zh"]), len(a["desc_en"]), len(a["desc_fr"])))
    TARGETS.append(p)

for lang in LANGS:
    r = subprocess.run([PY, "gen_i18n.py", lang] + TARGETS, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print(r.stdout[-2000:], r.stderr[-2000:])
        raise SystemExit("gen_i18n %s 失败" % lang)
    print("gen_i18n %s ok" % lang)
