# -*- coding: utf-8 -*-
"""就地修正第一篇两处文案（繁体错字 + 法/西语度量表述），随后需重生成语言页。"""
f = "blog/clothing-tagging-gun-swift-tack-guide.html"
s = open(f, encoding="utf-8").read()
pairs = [
    ("車一道线都要先墊襯", "車一道線都要先墊襯"),
    ("taille en 号 ou cm", "taille japonaise (号) ou cm"),
    ("talla en 号 o cm", "talla japonesa (号) o cm"),
]
for a, b in pairs:
    n = s.count(a)
    s = s.replace(a, b)
    print("%-26s 替换 %d 处" % (a, n))
open(f, "w", encoding="utf-8", newline="").write(s)
print("已写入", f)
