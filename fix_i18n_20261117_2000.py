# -*- coding: utf-8 -*-
"""修正两处译文细节：日语法令名在 fr/ko 栏补本地语注释；ko 正文误用的「외箱」。"""
import io

FILES = ["blog/hang-tag-back-printing-guide.html", "blog/apparel-trims-chargeback-guide.html"]
PAIRS = [
    ("家庭用品品質表示法 ; JIS L 0001", "家庭用品品質表示法 (loi japonaise sur l'étiquetage) ; JIS L 0001"),
    ("家庭用品品質表示法, JIS L 0001", "家庭用品品質表示法(일본 가정용품 품질표시법), JIS L 0001"),
    ("외箱", "외부 박스"),
]
BODY = ["body_20261117_2000_a.py", "body_20261117_2000_b.py"]

for f in FILES + BODY:
    s = io.open(f, encoding="utf-8").read()
    n_total = 0
    for a, b in PAIRS:
        n = s.count(a)
        s = s.replace(a, b)
        n_total += n
        print("%-45s %-30s -> %d" % (f, a[:28], n))
    io.open(f, "w", encoding="utf-8", newline="").write(s)
    print("  合计替换", n_total)
