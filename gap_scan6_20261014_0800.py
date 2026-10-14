#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""round6：品类词空白扫描（英文/日文/韩文为可靠字符；中文用繁体）。"""
import os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
rows = []
for lang in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
    for f in glob.glob(os.path.join(ROOT, lang + "blog/*.html")):
        if os.path.basename(f).startswith("_body"):
            continue
        rows.append((os.path.basename(f), open(f, encoding="utf-8").read().lower()))

CAND = [
    ("leggings", ["leggings", "レギンス", "레깅스", "緊身褲", "打底褲"]),
    ("tights/hosiery", ["tights", "タイツ", "스타킹", "褲襪"]),
    ("sports bra", ["sports bra", "スポーツブラ", "스포츠 브라"]),
    ("vest/tank", ["tank top", "タンクトップ", "vest top", "背心"]),
    ("jacket/coat", ["jacket", "ジャケット", "재킷"]),
    ("kimono/poncho/cape", ["kimono", "poncho", "cape ", "pelerine"]),
    ("bathrobe", ["bathrobe", "robe de chambre", "bata de baño", "バスローブ", "목욕 가운"]),
    ("mittens/gloves", ["mittens", "ミトン", "장갑", "手套"]),
    ("face mask", ["face mask", "face covering", "マスク", "마스크"]),
    ("shoelace", ["shoelace", "shoe lace", "靴ひも", "신발끈"]),
    ("slipper", ["slipper", "サンダル", "슬리퍼", "拖鞋"]),
    ("umbrella", ["umbrella", "傘 ", "우산", "雨傘"]),
    ("backpack/duffel", ["backpack", "duffel", "backpack", "リュック", "백팩"]),
    ("sleeping bag/tent", ["sleeping bag", "tent", "寝袋", "텐트"]),
    ("towel/tea towel", ["tea towel", "bath towel", "タオル", "타월", "毛巾"]),
    ("bedding/duvet", ["duvet", "bed sheet", "挂布", "かけ布団", "이불", "床單"]),
    ("curtain", ["curtain", "カーテン", "커튼", "窗簾"]),
    ("uniform service/medical", ["hospital", "病院", "병원", "診所", "clinic"]),
    ("housekeeping/cleaner", ["housekeeping", "cleaner uniform", "客室清掃", "하우스키핑"]),
    ("salon/beauty", ["salon", "美容院", "미용실", "beauty uniform"]),
    ("security guard", ["security guard", "警衛", "경비"]),
    ("staff shirt/polo", ["polo", "ポロシャツ", "반팔 티", "護士"]),
    ("name tag/badge", ["name tag", "name badge", "ネームプレート", "명찰", "胸牌"]),
    ("tote/canvas bag", ["tote", "canvas bag", "トート", "캔버스백"]),
    ("sticker/label roll", ["roll label", "price ticket roll", "ロールラベル", "롤 라벨"]),
    ("hang tag elastic cord", ["elastic cord", "stretch cord", "ゴム紐", "고무 코드"]),
]

print("文件数:", len(rows))
print()
for name, kws in CAND:
    per = []
    for k in kws:
        hit = [f for f, t in rows if k.lower() in t]
        per.append((k, len(hit), sorted(set(hit))[:2]))
    print("%-22s %s" % (name, "  ".join("%s:%d" % (k, n) for k, n, _ in per)))
