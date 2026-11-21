# -*- coding: utf-8 -*-
"""给两个 body 模块的 fr 值补合法法语省音（l un -> l'un），只动 "fr": "..." 的值。"""
import re
import sys

EL = re.compile(r"\b(l|d|n|s|c|j|m|t|qu) (?=[aeiou\u00e9\u00e8\u00ea\u00e0\u00e2\u00ee\u00ef\u00f4\u00fb\u00f9hA-Z])")


def fix(m):
    val = m.group(1)
    new = EL.sub(r"\1'", val)
    return '"fr": "%s"' % new


for path in sys.argv[1:]:
    s = open(path, encoding="utf-8").read()
    before = len(EL.findall(s))
    s2 = re.sub(r'"fr": "([^"\\]*)"', fix, s)
    open(path, "w", encoding="utf-8", newline="\n").write(s2)
    print("%s: 处理 %d 处省音模式" % (path, before))

for path in sys.argv[1:]:
    import ast
    ast.parse(open(path, encoding="utf-8").read())
    print("AST OK", path)
