#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
s = open("blog/_body_measure.html", encoding="utf-8").read()
i = s.index("<p ")
j = s.index(">", i)
print("第一个 p 标签长度:", j - i + 1)
print("标签末尾 60 字符:", repr(s[j - 60:j + 1]))
print("紧随其后 120 字符:", repr(s[j + 1:j + 121]))
print("---- 该标签内各属性出现次数 ----")
tag = s[i:j + 1]
for l in ["zh", "en", "fr", "es", "ja", "ko"]:
    print("  data-%s= :" % l, tag.count("data-%s=" % l))
print("---- 引号总数 ----", tag.count('"'))
