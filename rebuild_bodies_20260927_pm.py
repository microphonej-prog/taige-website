#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用最新正文源重建 2026-09-27 下午两篇文章的根页面（繁体）并重生成五语版本。
用于正文源微调（desc_en 长度、去掉属性里的裸 '<'、韩语标点）后同步线上文件。
"""
import importlib.util, os, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

PAIRS = [("blog/_body_sparebtn.html", "blog/garment-spare-button-bag-guide.html"),
         ("blog/_body_scorecard.html", "blog/trim-supplier-scorecard-guide.html")]
LANGS = ["en", "ja", "ko", "fr", "es"]

spec = importlib.util.spec_from_file_location("to_traditional", os.path.join(ROOT, "to_traditional.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

for body_p, root_p in PAIRS:
    s = open(root_p, encoding="utf-8").read()
    i0 = s.index('<section class="article-body">')
    i1 = s.index("\n</main>")
    b = mod.convert_html(open(body_p, encoding="utf-8").read().rstrip("\n"))
    s2 = s[:i0] + b + s[i1:]
    open(root_p, "w", encoding="utf-8", newline="").write(s2)
    print("重建 %s (%d KB)" % (root_p, len(s2.encode("utf-8")) // 1024))

for lang in LANGS:
    r = subprocess.run([sys.executable, "gen_i18n.py", lang] + [p for _, p in PAIRS],
                       capture_output=True, text=True, encoding="utf-8")
    assert r.returncode == 0, r.stdout + r.stderr
    print("gen_i18n %s ok" % lang)

# 收尾自检：属性值里不应再有裸 '<'，desc_en 长度合规
import re
for _, root_p in PAIRS:
    s = open(root_p, encoding="utf-8").read()
    bad = re.findall(r'data-[a-z]+="[^"]*<[^"/][^"]*"', s)
    d = re.search(r'data-en="([^"]{40,})"\s*\n\s*data-ja', s)
    print("%s 属性内裸 '<' %d 处；desc_en 由 meta 单独核对" % (root_p, len(bad)))
