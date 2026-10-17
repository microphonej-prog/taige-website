# -*- coding: utf-8 -*-
from opencc import OpenCC
s2t = OpenCC("s2t")
for ch in "国学会体数実転発変経対応単価様継続選択絵図団関":
    print(ch, "->", s2t.convert(ch), "FLAG" if s2t.convert(ch) != ch else "ok")
