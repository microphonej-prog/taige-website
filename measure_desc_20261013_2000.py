# -*- coding: utf-8 -*-
"""2026-10-13 晚间批次：desc 长度体检（zh 80-120 字，en 150-160 字符）"""
import importlib.util, os, re, json

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
spec = importlib.util.spec_from_file_location("m", "daily_meta_20261013_2000.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

for a in m.ARTICLES:
    zh = a["desc_zh"]
    print("==", a["slug"])
    for k in ("desc_zh", "desc_en", "desc_ja", "desc_ko", "desc_fr", "desc_es"):
        v = a[k]
        cjk = len(re.findall(r'[\u4e00-\u9fff]', v))
        print("   %-9s len=%-4d cjk=%-4d %s" % (k, len(v), cjk, v[:70]))
    for k in ("title_zh", "title_en", "title_ja", "title_ko", "title_fr", "title_es"):
        print("   %-9s len=%-4d %s" % (k, len(a[k]), a[k][:80]))
    # 引号/实体检查
    for k, v in a.items():
        if isinstance(v, str):
            assert '"' not in v, (a["slug"], k, "含裸双引号")
            if "&" in v:
                print("   [裸&]", k, v)
