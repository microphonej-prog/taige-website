#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-14 下午批次：选题空白扫描（六语站全量 HTML 关键词计数）"""
import os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

files = []
for p in ["blog/*.html", "en/blog/*.html", "fr/blog/*.html", "es/blog/*.html",
          "ja/blog/*.html", "ko/blog/*.html"]:
    files += glob.glob(p)
files += ["index.html", "en/index.html", "contact.html", "products.html"]
text = []
for f in files:
    try:
        text.append(open(f, encoding="utf-8").read())
    except Exception as e:
        print("skip", f, e)
blob = "\n".join(text)
print("扫描文件数:", len(files), "总字符:", len(blob))

KEYS = [
    "超声波", "超音波", "ultrasonic", "Ultrasonic", "cho son", "초음파",
    "激光切割", "laser cut", "laser-cut", "laser cutting", "レーザーカット", "레이저 커팅",
    "热切", "hot cut", "hot-cut", "hot cutting", "封边", "sealing edge", "fray",
    "毛边", "脱纱", "raveling", "unravel",
    "仓储", "warehouse", "Warehouse", "storage condition", "保管条件", "창고",
    "库存保管", "shelf life", "保存期限", "保管", "stock rotation", "先进先出", "FIFO",
    "发霉", "mildew", "mold growth", "霉斑", "カビ", "곰팡이",
    "虫害", "pest", "insect", "防虫", "moth",
    "胶水老化", "adhesive aging", "粘性下降", "rubber band", "橡皮筋",
    "黄变", "yellowing", "泛黄",
    "湿度", "humidity", "RH ", "除湿", "dehumidifi",
    "卷装", "roll storage", "reel", "盘装",
    "有效期", "expiry", "过期",
]

for k in KEYS:
    n = blob.count(k)
    print("%-22s %d" % (k, n))
