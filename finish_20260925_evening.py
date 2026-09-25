#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-25 晚间批次 步骤 3-6（主脚本在 to_traditional 处因解释器缺 opencc 中断后接手）：
3) 简体→繁体（幂等）  4) gen_i18n 六语生成  5) sitemap  6) BUST_VERSION 升级
须用 F:/hermes/venvs/tools/Scripts/python.exe 运行（该环境装有 opencc）。
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable
print("解释器:", PY)

SLUGS = ["garment-trims-fabric-compatibility-guide.html", "textile-phenolic-yellowing-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
SITEMAP_DATE = "2026-09-25"
BUST_OLD, BUST_NEW = "109", "110"

# ---------- 3) 简体 → 繁体 ----------
spec = importlib.util.spec_from_file_location("to_traditional", os.path.join(ROOT, "to_traditional.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
changed = []
for p in ["blog/%s" % s for s in SLUGS] + ["blog/index.html"]:
    s0 = open(p, encoding="utf-8").read()
    s1 = mod.convert_html(s0)
    if s1 != s0:
        open(p, "w", encoding="utf-8", newline="").write(s1)
        changed.append(os.path.basename(p))
print("繁体转换改动: %d %s" % (len(changed), changed))

# ---------- 4) gen_i18n 生成五语版本 ----------
TARGETS = ["blog/%s" % s for s in SLUGS] + ["blog/index.html"]
for lang in LANGS:
    r = subprocess.run([PY, "gen_i18n.py", lang] + TARGETS, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print(r.stdout[-3000:], r.stderr[-3000:])
        raise SystemExit("gen_i18n %s 失败" % lang)
    print("gen_i18n %s -> %d 文件 ok" % (lang, len(TARGETS)))

# ---------- 5) sitemap ----------
sm = open("sitemap.xml", encoding="utf-8", newline="").read()
before = sm.count("<loc>")


def block(url):
    return ("  <url>\r\n    <loc>%s</loc>\r\n    <lastmod>%s</lastmod>\r\n"
            "    <changefreq>monthly</changefreq>\r\n    <priority>0.7</priority>\r\n  </url>\r\n"
            % (url, SITEMAP_DATE))


blocks = []
for slug in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % slug] + \
             ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        if "<loc>%s</loc>" % u in sm:
            print("  已存在，跳过:", u)
            continue
        blocks.append(block(u))
sm = sm.replace("</urlset>", "".join(blocks) + "</urlset>", 1)

for u in ["https://taigetag.com/blog/index.html"] + \
         ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)' % re.escape(u))
    sm, n = pat.subn(r'\g<1>%s\g<2>' % SITEMAP_DATE, sm, count=1)
    assert n == 1, "blog index lastmod 未更新: %s" % u

open("sitemap.xml", "w", encoding="utf-8", newline="").write(sm)
print("sitemap 新增 %d 个 URL，<loc> 总数 %d -> %d" % (len(blocks), before, sm.count("<loc>")))

# ---------- 6) BUST_VERSION ----------
mj = open("js/main.js", encoding="utf-8").read()
if 'var BUST_VERSION = "%s";' % BUST_OLD in mj:
    mj = mj.replace('var BUST_VERSION = "%s";' % BUST_OLD, 'var BUST_VERSION = "%s";' % BUST_NEW, 1)
    open("js/main.js", "w", encoding="utf-8", newline="").write(mj)
    print("BUST_VERSION %s -> %s" % (BUST_OLD, BUST_NEW))
elif 'var BUST_VERSION = "%s";' % BUST_NEW in mj:
    print("BUST_VERSION 已是 %s，跳过" % BUST_NEW)
else:
    raise SystemExit("BUST_VERSION 状态异常")
