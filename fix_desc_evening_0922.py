#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把两篇新文章的英文 description 收到 150-160 字符，并重生成 en 版本。"""
import re, subprocess, sys, os
sys.stdout.reconfigure(encoding='utf-8')

FIX = {
    "blog/eu-digital-product-passport-trims.html":
        "EU Digital Product Passport (DPP) for apparel trims: what ESPR requires, the data fields, where QR and NFC carriers go on labels, and what to prepare now.",
    "blog/trims-carbon-footprint-guide.html":
        "Trim carbon footprint: three accounting bases buyers use, four emission hot spots, three data tiers, and a data sheet to fold into your production records.",
}
for p, new in FIX.items():
    print("%s 新英文描述 %d 字符" % (os.path.basename(p), len(new)))
    assert 150 <= len(new) <= 160, "英文描述长度不在 150-160: %d" % len(new)
    s = open(p, encoding="utf-8").read()
    s, n1 = re.subn(r'(data-en=")[^"]*(")', lambda m: m.group(1) + new + m.group(2), s, count=1)
    assert n1 == 1, "data-en 替换失败 %s" % p
    s, n2 = re.subn(r'(<meta name="description"[^>]*content=")[^"]*(">)',
                    lambda m: m.group(1) + new + m.group(2), s, count=1, flags=re.S)
    assert n2 == 1, "content 替换失败 %s" % p
    open(p, "w", encoding="utf-8", newline="").write(s)
    print("  已更新", p)

for p, new in FIX.items():
    r = subprocess.run([sys.executable, "gen_i18n.py", "en", p], capture_output=True,
                       text=True, encoding="utf-8")
    print(r.stdout.strip() or r.stderr.strip())
    if r.returncode != 0:
        raise SystemExit("gen_i18n en 失败")

# 校验生成结果
for p, new in FIX.items():
    en = "en/" + p.split("/", 1)[1]
    s = open(en, encoding="utf-8").read()
    m = re.search(r'<meta name="description" content="([^"]*)">', s)
    print("%s -> %d 字符 | 一致=%s" % (en, len(m.group(1)), m.group(1) == new))
