# -*- coding: utf-8 -*-
"""把第 2 篇 ko 童装段落的补丁同步进源页 data-ko，然后重生成 ko 语言页。"""
import re

OLD = "한국은 동등한 강제 수치는 없지만 어린이제품 안전 특별법과 KC 인증이 별도 요구를 두고,"
NEW = "한국은 동등한 강제 수치는 없지만 어린이제품 안전 특별법에 따라 원산지와 취급 표시 등 표시 의무가 붙고 KC 인증이 별도 요구를 두며,"

p = "blog/trim-attachment-strength-pull-test-guide.html"
s = open(p, encoding="utf-8").read()
n = s.count(OLD)
s = s.replace(OLD, NEW)
open(p, "w", encoding="utf-8", newline="").write(s)
print("源页替换处数:", n)
