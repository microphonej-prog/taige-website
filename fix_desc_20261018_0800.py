#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把两篇新文章的 desc_en/fr/es 收进目标长度，并回写每日元数据与已生成页面。"""
import os, re, subprocess, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable

FIX = {
    "trim-invoice-tax-export-rebate.html": {
        "en": "Trims invoicing explained: tax-inclusive versus net cost, 13% and 1% special invoices, who claims the export rebate, and a tax sheet for enquiries.",
        "fr": "Facturation des accessoires : passer du TTC au coût net, écart entre facture à 13 % et à 1 %, qui demande la détaxe à l'export, et une fiche fiscale.",
        "es": "Facturación de accesorios: pasar de precio con impuestos a coste neto, factura al 13 % frente al 1 %, quién pide la devolución y una ficha fiscal.",
    },
    "packaging-automation-bag-compatibility.html": {
        "en": "Matching poly bags to automatic lines: roll film or flat bags, gauge, friction, core size and eye marks, seven causes of jams and a trial checklist.",
        "fr": "Adapter les sachets aux lignes automatiques : film ou sachets plats, épaisseur, frottement, mandrin et repères, sept causes de bourrage, liste d'essai.",
        "es": "Adaptar bolsas a líneas automáticas: film o bolsas planas, espesor, fricción, tubo y marcas de registro, siete causas de atascos y lista de prueba.",
    },
}

for slug, langs in FIX.items():
    print("==", slug)
    for l, v in langs.items():
        print("   %s len=%d" % (l, len(v)))

# ---- 回写每日元数据（保持单一事实来源） ----
mp = "daily_meta_20261018_0800.py"
m = open(mp, encoding="utf-8").read()
for slug, langs in FIX.items():
    # 定位该 slug 的 dict 区块
    i = m.index('slug="%s"' % slug)
    j = m.index("\n    ),", i)
    seg = m[i:j]
    for l, v in langs.items():
        seg2, n = re.subn(r'desc_%s="[^"]*"' % l, 'desc_%s="%s"' % (l, v), seg, count=1)
        assert n == 1, "meta 缺 desc_%s @%s" % (l, slug)
        seg = seg2
    m = m[:i] + seg + m[j:]
open(mp, "w", encoding="utf-8", newline="").write(m)

# ---- 回写已生成的中文根页面（meta description 块内的语言属性） ----
for slug, langs in FIX.items():
    p = "blog/%s" % slug
    s = open(p, encoding="utf-8").read()
    m0 = re.search(r'<meta name="description".*?>', s, re.S)
    assert m0, "desc 块未找到 %s" % p
    block = m0.group(0)
    nb = block
    for l, v in langs.items():
        nb, n = re.subn(r'data-%s="[^"]*"' % l, 'data-%s="%s"' % (l, v), nb, count=1)
        assert n == 1, "页面缺 data-%s @%s" % (l, slug)
    s = s.replace(block, nb, 1)
    open(p, "w", encoding="utf-8", newline="").write(s)
    print("   回写", p)

# ---- 重新生成五语版本 ----
for lang in ["en", "ja", "ko", "fr", "es"]:
    r = subprocess.run([PY, "gen_i18n.py", lang] +
                       ["blog/%s" % s for s in FIX] , capture_output=True, text=True, encoding="utf-8")
    print("   gen_i18n %s rc=%d" % (lang, r.returncode))
    if r.returncode != 0:
        print(r.stdout[-1500:], r.stderr[-1500:])
        raise SystemExit(1)
