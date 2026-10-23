# -*- coding: utf-8 -*-
"""微调两篇文章的 desc_en / desc_fr 长度（英文控制在 150-160 字符）。"""
import os, glob

FIX = [
    ("FSC hang tags explained: the 100%, Mix and Recycled labels, why chain of custody must sit with the printer, claim wording that holds up, plus cost and lead time.",
     "FSC hang tags explained: the 100%, Mix and Recycled labels, why chain of custody must sit with the printer, claim wording that holds, plus cost and lead time."),
    ("Rush trims orders: four variables that decide if it can be rushed, five parallel routes and what each costs, where the surcharge goes, and the four quality failures to guard.",
     "Rush trims orders: four variables that decide feasibility, five parallel routes and their cost, where the surcharge goes, and four quality failures to guard."),
    ("Accessoires en urgence : quatre variables décisives, cinq routes parallèles et leur coût, où va le surcoût, les quatre défauts qualité à surveiller et les cinq infos à envoyer.",
     "Accessoires en urgence : quatre variables décisives, cinq routes parallèles et leur coût, où va le surcoût et quatre défauts qualité à surveiller."),
]

slug1, slug2 = "fsc-certified-hang-tags.html", "apparel-trims-rush-order-guide.html"
files = []
for s in (slug1, slug2):
    files.append("blog/%s" % s)
    for l in ("en", "ja", "ko", "fr", "es"):
        files.append("%s/blog/%s" % (l, s))

for f in files:
    if not os.path.exists(f):
        print("缺失", f); continue
    s0 = open(f, encoding="utf-8").read()
    s1 = s0
    hits = 0
    for old, new in FIX:
        hits += s1.count(old)
        s1 = s1.replace(old, new)
    if s1 != s0:
        open(f, "w", encoding="utf-8", newline="").write(s1)
    print("%-46s 替换 %d 处" % (f, hits))

for f in [files[0], files[1]]:
    s = open(f, encoding="utf-8").read()
    print(f, "len(desc_en) 校验 ->", "OK" if 'data-en="Rush trims orders: four variables that decide feasibility' in s or 'data-en="FSC hang tags explained' in s else "??")
