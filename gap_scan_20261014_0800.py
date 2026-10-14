#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-14 第一批选题空白扫描：统计候选关键词在全站 blog/*.html（含六语）中的出现文件数。"""
import os, re, glob, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
files = []
for lang in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
    files += glob.glob(os.path.join(ROOT, lang + "blog/*.html"))
files = [f for f in files if not os.path.basename(f).startswith("_body")]
texts = {}
for f in files:
    try:
        texts[f] = open(f, encoding="utf-8").read()
    except Exception as e:
        print("READ FAIL", f, e)

CAND = [
    ("azo-dye", ["偶氮", "azo dye", "azo-", "Azofarbstoff", "colorantes azoicos", "colorants azoïques", "아조 염료", "アゾ染料"]),
    ("formaldehyde", ["甲醛", "formaldehyde", "formaldéhyde", "formaldehído", "ホルムアルデヒド", "포름알데히드"]),
    ("phthalate", ["邻苯二甲酸", "phthalate", "phtalate", "ftalato", "フタル酸", "프탈레이트", "塑化剂"]),
    ("metamerism", ["同色异谱", "metamerism", "métamérisme", "metamerismo", "条件等色", "메타메리즘"]),
    ("FSC paper", ["FSC", "森林管理委员会", "Forest Stewardship"]),
    ("GRS recycled", ["GRS", "全球回收标准", "Global Recycled Standard", "recycled polyester label"]),
    ("AQL sampling", ["AQL", "抽样检验", "sampling plan", "acceptable quality limit"]),
    ("trademark", ["商标注册", "trademark", "marque déposée", "marca registrada", "상표", "商標"]),
    ("home textile/bedding", ["家纺", "床品", "home textile", "bedding", "linge de lit", "ropa de cama", "寝具", "침구"]),
    ("baby/infant", ["婴幼儿", "婴儿", "babywear", "infant", "nourrisson", "bebé", "乳幼児", "유아"]),
    ("apron", ["围裙", "apron", "tablier", "delantal", "エプロン", "앞치마"]),
    ("adhesive/glue", ["胶水", "粘合", "adhesive", "colle", "pegamento", "接着剤", "접착제"]),
    ("PSI inspection", ["出货前检验", "PSI", "pre-shipment inspection", "inspection avant expédition", "inspección previa"]),
    ("Egypt compliance", ["埃及", "Egypt", "Égypte", "Egipto", "エジプト", "이집트"]),
    ("South Africa compliance", ["南非", "South Africa", "Afrique du Sud", "Sudáfrica", "남아프리카"]),
    ("Norway compliance", ["挪威", "Norway", "Norvège", "Noruega", "ノルウェー", "노르웨이"]),
    ("Sweden compliance", ["瑞典", "Sweden", "Suède", "Suecia", "スウェーデン", "스웨덴"]),
    ("Germany textile law", ["德国", "Textilkennzeichnung", "Germany labelling", "Allemagne étiquetage"]),
    ("Netherlands", ["荷兰", "Netherlands", "Pays-Bas", "Países Bajos"]),
    ("Poland", ["波兰", "Poland", "Pologne", "Polonia"]),
    ("New Zealand", ["新西兰", "New Zealand", "Nouvelle-Zélande", "Nueva Zelanda"]),
    ("Indonesia", ["印尼", "印度尼西亚", "Indonesia", "Indonésie"]),
    ("Vietnam", ["越南", "Vietnam", "Viêt Nam"]),
    ("Ecuador", ["厄瓜多尔", "Ecuador", "Équateur"]),
    ("Israel", ["以色列", "Israel", "Israël"]),
    ("golf/tennis", ["高尔夫", "golf", "tennis", "ゴルフ", "골프"]),
    ("swimwear", ["泳装", "swimwear", "maillot de bain", "traje de baño", "水着", "수영복"]),
    ("denim", ["牛仔", "denim", "jean", "denim", "デニム", "데님"]),
    ("trim storage/humidity", ["湿度", "humidity", "humidité", "humedad", "湿度管理", "습도"]),
    ("mold/mildew", ["发霉", "霉变", "mold", "mildew", "moisissure", "moho", "カビ", "곰팡이"]),
    ("shrinkage of fabric trims", ["缩水", "shrinkage", "rétrécissement", "encogimiento", "収縮", "수축"]),
    ("laser cut", ["激光切割", "激光镂空", "laser cut", "découpe laser", "corte láser", "レーザーカット", "레이저 컷"]),
    ("hangtag elastic string", ["弹力绳", "elastic string", "élastique", "elástico", "ゴムひも", "고무줄"]),
    ("price negotiation", ["议价", "还价", "negotiation", "négociation", "negociación", "価格交渉", "가격 협상"]),
    ("trims for handbags", ["手袋", "handbag", "sac à main", "bolso", "ハンドバッグ", "핸드백"]),
    ("cosplay/uniform school", ["cosplay", "制服", "uniform", "uniforme", "uniforme", "制服", "교복"]),
    ("sustainable cotton/Bci", ["BCI", "better cotton", "良好棉花", "coton durable", "algodón sostenible"]),
    ("vegan leather label", ["素皮", "vegan leather", "cuir végétal", "cuero vegano", "ヴィーガンレザー", "비건 레더"]),
]

print("扫描文件数:", len(files))
print()
for name, kws in CAND:
    hit = set()
    per = []
    for kw in kws:
        c = [f for f, t in texts.items() if kw.lower() in t.lower()]
        per.append((kw, len(c)))
        hit |= set(c)
    print("%-28s files=%3d   %s" % (name, len(hit), "  ".join("%s:%d" % (k, n) for k, n in per if n)))
