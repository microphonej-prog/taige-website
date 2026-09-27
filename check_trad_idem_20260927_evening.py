#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""晚间批次：繁体转换幂等性检查（再次转换应无改动）+ 简体专有字形残留扫描。"""
import importlib.util, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
spec = importlib.util.spec_from_file_location("to_traditional", os.path.join(ROOT, "to_traditional.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

FILES = ["blog/trim-supplier-social-compliance-audit.html",
         "blog/trim-quotation-validity-guide.html",
         "blog/index.html"]
SIMP = set("产个门这说关时长场应该对让从为发处于单价线织衬复货买质检标记给过还样种类设备库图术语题问结构档书报议讲归录审")

bad = 0
for p in FILES:
    s = open(p, encoding="utf-8").read()
    left = mod.convert_html(s)
    diff = (left != s)
    if diff:
        bad += 1
        print("!! %s 仍可被转换（简体残留）" % p)
    hits = set()
    for m in re.finditer(r'data-zh="([^"]*)"', s):
        hits |= set(ch for ch in m.group(1) if ch in SIMP)
    print("%-52s 幂等=%s  简体残留字形=%s" % (p, "OK" if not diff else "XX", sorted(hits) or "无"))
    bad += len(hits)

print("结论：问题 %d" % bad)
sys.exit(1 if bad else 0)
