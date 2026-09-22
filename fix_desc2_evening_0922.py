#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 fix_desc_evening_0922.py 造成的错位：
- <title> 的 data-en 被误写成英文 description → 恢复为正确英文标题
- meta description 的 content 被写成英文 → 恢复为 data-zh 值（简繁一致，爬虫可读）
- meta description 的 data-en 设为 150-160 字符版本
然后重生成 en 版本。
"""
import re, subprocess, sys

sys.stdout.reconfigure(encoding='utf-8')

TITLE_EN = {
    "blog/eu-digital-product-passport-trims.html":
        "EU Digital Product Passport (DPP) for Apparel Trims &amp; Labels | TAGE",
    "blog/trims-carbon-footprint-guide.html":
        "Trim Carbon Footprint: Answering Brand PCF Questionnaires | TAGE",
}
DESC_EN = {
    "blog/eu-digital-product-passport-trims.html":
        "EU Digital Product Passport (DPP) for apparel trims: what ESPR requires, the data fields, where QR and NFC carriers go on labels, and what to prepare now.",
    "blog/trims-carbon-footprint-guide.html":
        "Trim carbon footprint: three accounting bases buyers use, four emission hot spots, three data tiers, and a data sheet to fold into your production records.",
}

for p, ten in TITLE_EN.items():
    s = open(p, encoding="utf-8").read()
    s, n1 = re.subn(r'(<title data-zh="[^"]*" data-en=")[^"]*(")',
                    lambda m: m.group(1) + ten + m.group(2), s, count=1)
    assert n1 == 1, "title data-en 修复失败 %s" % p

    m = re.search(r'<meta name="description".*?>', s, re.S)
    assert m, "未找到 description"
    blk = m.group(0)
    dz = re.search(r'data-zh="([^"]*)"', blk).group(1)
    nb = blk
    nb = re.sub(r'data-en="[^"]*"', 'data-en="%s"' % DESC_EN[p], nb, count=1)
    nb = re.sub(r'content="[^"]*"', 'content="%s"' % dz, nb, count=1)
    s = s.replace(blk, nb, 1)
    open(p, "w", encoding="utf-8", newline="").write(s)
    print("修复 %s | title_en 长度=%d | desc_en=%d | content=data-zh(%d 字)"
          % (p, len(ten), len(DESC_EN[p]), len(dz)))

for p in TITLE_EN:
    r = subprocess.run([sys.executable, "gen_i18n.py", "en", p], capture_output=True,
                       text=True, encoding="utf-8")
    print((r.stdout or r.stderr).strip())
    if r.returncode != 0:
        raise SystemExit("gen_i18n en 失败")

print("\n== 校验 ==")
for p in TITLE_EN:
    s = open(p, encoding="utf-8").read()
    t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1).strip()
    md = re.search(r'<meta name="description".*?>', s, re.S).group(0)
    content = re.search(r'content="([^"]*)"', md).group(1)
    den = re.search(r'data-en="([^"]*)"', md).group(1)
    print("根页 title:", t)
    print("   content 中文=%s (%d 字)" % (bool(re.search(r'[\u4e00-\u9fff]', content)), len(content)))
    print("   desc_en=%d 字符 一致=%s" % (len(den), den == DESC_EN[p]))
    en = "en/" + p.split("/", 1)[1]
    se = open(en, encoding="utf-8").read()
    te = re.search(r'<title[^>]*>(.*?)</title>', se, re.S).group(1).strip()
    de = re.search(r'<meta name="description" content="([^"]*)">', se).group(1)
    print("   en 页 title:", te)
    print("   en 页 desc=%d 字符 中文残留=%s" % (len(de), bool(re.search(r'[\u4e00-\u9fff]', de))))
