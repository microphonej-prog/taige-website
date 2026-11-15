# -*- coding: utf-8 -*-
"""补 ja 版的日本法规落点（家庭用品品質表示法 / JIS L 0001），同步源页 data-ja。"""
import html
import re

SLUG = "cord-locks-toggles-drawstring-hardware-guide"
OLD = "洗濯表示に「金具は裏返しで洗い、浸け置きしない」と明記します。"
NEW = ("洗濯表示に「金具は裏返しで洗い、浸け置きしない」と明記します。"
       "日本向けは家庭用品品質表示法に基づく洗濯表示が必要で、JIS L 0001 の記号と金具の実際の耐性を一致させ、"
       "40 °C の機械洗濯可とするなら亜鉛合金ではなくニッケル鍍金真鍮か樹脂を選びます。")

# 1) 改 body 文件
bp = "body_20261115_2000_b.py"
s = open(bp, encoding="utf-8").read()
assert s.count(OLD) == 1, s.count(OLD)
s = s.replace(OLD, NEW)
open(bp, "w", encoding="utf-8", newline="").write(s)

# 2) 同步源页里的 data-ja（属性值已转义，无 & 无需额外 escape）
page = "blog/%s.html" % SLUG
p = open(page, encoding="utf-8").read()
assert p.count(OLD) == 1, p.count(OLD)
p = p.replace(OLD, NEW)
open(page, "w", encoding="utf-8", newline="").write(p)
print("源页 data-ja 已补，ja 段落字符 %d -> %d" % (len(OLD), len(NEW)))
