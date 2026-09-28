#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""核对根页 blog/index.html 顶部两张卡的实际位置与长度。"""
S = ["eu-deforestation-regulation-packaging.html", "eu-packaging-epr-triman-guide.html"]
for pre in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
    p = "%sblog/index.html" % pre
    s = open(p, encoding="utf-8").read()
    g = s.index('<div class="post-grid">')
    pos = [s.find(sl, g) for sl in S]
    print("%-24s 位置=%s 差值=%d grid 起点=%d" % (p, pos, pos[1] - pos[0], g))
