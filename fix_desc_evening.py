#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修正两篇新文章的 description 长度（中文 80-120 字、英文 150-160 字符），
改完对根目录页做一次繁体转换（幂等），再重跑 gen_i18n 五语。"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

FIX = {
    "blog/clothing-label-compliance-saudi-arabia.html": dict(
        zh="沙特阿拉伯服装标签合规指南：纺织产品技术法规要求标签用阿拉伯语标注纤维成分、洗护说明、原产地与责任方，进口清关需 SASO 的 SABER 符合性证书。讲清七项必标信息、阿拉伯语排版要点、ISO 3758 洗护符号对齐与打样核对清单。来自东莞泰阁包装。",
        en="Saudi Arabia clothing label rules: Arabic fibre content, care and origin, importer details, and SASO SABER product and shipment certificates for clearance.",
    ),
    "blog/clothing-label-compliance-turkey.html": dict(
        zh="土耳其服装标签合规指南：纺织与皮革产品标签条例以欧盟 1007/2011 为蓝本，消费者信息必须用土耳其语标注纤维成分、洗护说明、原产地与责任方，进口经 TAREKS 风险抽检。含术语对照表、成分公差口径与打样核对清单。来自东莞泰阁包装。",
        en="Turkey clothing label rules: Turkish-language fibre composition, care and origin, rules modelled on EU 1007/2011, TAREKS import inspection and a terminology table.",
    ),
}

for path, vals in FIX.items():
    s = open(path, encoding="utf-8").read()
    m = re.search(r'<meta name="description".*?>', s, re.S)
    blk = m.group(0)
    b2, n1 = re.subn(r'data-zh="[^"]*"', 'data-zh="%s"' % vals["zh"], blk, count=1)
    b2, n2 = re.subn(r'data-en="[^"]*"', 'data-en="%s"' % vals["en"], b2, count=1)
    b2, n3 = re.subn(r'content="[^"]*"', 'content="%s"' % vals["zh"], b2, count=1)
    assert (n1, n2, n3) == (1, 1, 1), (path, n1, n2, n3)
    s = s[:m.start()] + b2 + s[m.end():]

    # 繁体转换（幂等）
    spec = importlib.util.spec_from_file_location("to_traditional", os.path.join(ROOT, "to_traditional.py"))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    s = mod.convert_html(s)
    open(path, "w", encoding="utf-8", newline="").write(s)
    print("修正 description:", path)

for lang in ["en", "ja", "ko", "fr", "es"]:
    r = subprocess.run([PY, "gen_i18n.py", lang] + list(FIX.keys()),
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print(r.stdout[-2000:], r.stderr[-2000:])
        raise SystemExit("gen_i18n %s 失败" % lang)
    print("gen_i18n %s ok" % lang)
