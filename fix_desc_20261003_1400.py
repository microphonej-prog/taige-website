#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""收短英文 description 到 150–165 字符（Google 显示长度），并同步到五语版本。"""
import re, subprocess, sys, os

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

NEW = {
    "blog/zipper-selection-guide.html":
        "Garment zipper guide: nylon, resin and metal teeth, size numbers #3 to #8, slider types, tape shrinkage matching, nickel release tests and a quote checklist.",
    "blog/fusible-interlining-guide.html":
        "Fusible interlining guide: woven, non-woven and knitted bases, PA/PES/PE coatings, fusing temperature, pressure, time, shrinkage matching and blistering.",
}

for f, new in NEW.items():
    s = open(f, encoding="utf-8").read()
    m = re.search(r'(<meta name="description"[^>]*?data-en=")([^"]*)(")', s, re.S)
    assert m, f
    old = m.group(2)
    print("%s\n  旧 en=%d 字符：%s\n  新 en=%d 字符：%s" % (f, len(old), old[:70], len(new), new))
    assert 145 <= len(new) <= 165, "英文 desc 长度不在 145-165：%d" % len(new)
    s = s[:m.start(2)] + new + s[m.end(2):]
    open(f, "w", encoding="utf-8", newline="").write(s)

for lang in ["en", "ja", "ko", "fr", "es"]:
    r = subprocess.run([PY, "gen_i18n.py", lang] + list(NEW.keys()),
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print(r.stdout[-2000:], r.stderr[-2000:])
        raise SystemExit("gen_i18n %s 失败" % lang)
    print("gen_i18n %s ok" % lang)
