#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把晚间第一篇的中文 desc 从 122 字收到 120 字以内（删去「採購方」三字），
同步更新 data-zh 与 content 两处（根目录页为繁体，不做重新生成以免影响其他语种）。"""
import re

P = "blog/trim-supplier-social-compliance-audit.html"
s = open(P, encoding="utf-8").read()

m = re.search(r'data-zh="(輔料供應商[^"]*來自東莞泰閣包裝。)"', s)
assert m, "未找到 data-zh desc"
old = m.group(1)
new = old.replace("以及採購方寫進詢價與合同的五條條款", "以及寫進詢價與合同的五條條款")
assert new != old, "替换规则未命中"
assert len(new) <= 120, "仍超长：%d" % len(new)

n1 = s.count('data-zh="%s"' % old)
n2 = s.count('content="%s"' % old)
assert n1 == 1 and n2 == 1, "命中数异常 data-zh=%d content=%d" % (n1, n2)
s = s.replace(old, new)
open(P, "w", encoding="utf-8", newline="").write(s)
print("desc_zh 由 %d 字缩至 %d 字，已同步 data-zh / content" % (len(old), len(new)))
print(new)
