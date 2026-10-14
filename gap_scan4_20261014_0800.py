#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-14 第一批选题空白扫描 round4：欧盟可持续/法规线索（中文用繁体）。"""
import os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
files = []
for lang in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
    files += glob.glob(os.path.join(ROOT, lang + "blog/*.html"))
files = [f for f in files if not os.path.basename(f).startswith("_body")]
texts = [(f, open(f, encoding="utf-8").read()) for f in files]

CAND = [
    ("greenwashing", ["greenwashing", "綠色聲明", "绿色声明", "green claims", "allégations environnementales", "blanchiment écologique", "ecoblanqueo", "グリーンウォッシュ", "그린워싱"]),
    ("ESPR ecodesign", ["ESPR", "ecodesign", "écoconception", "ecodiseño", "生態設計", "エコデザイン", "에코디자인"]),
    ("France EPR", ["Refashion", "法國 EPR", "法国 EPR", "French EPR", "REP textile France"]),
    ("Netherlands EPR", ["荷蘭", "荷兰", "Netherlands EPR", "Uitgebreide producentenverantwoordelijkheid"]),
    ("LkSG supply chain", ["LkSG", "Lieferkettengesetz", "supply chain due diligence", "devoir de vigilance", "德國供應鏈"]),
    ("CSRD", ["CSRD", "corporate sustainability reporting", "CSRD 報告"]),
    ("CBAM", ["CBAM", "碳關稅", "碳关税", "carbon border"]),
    ("microplastics", ["microplastics", "微塑料", "microplastiques", "microplásticos", "マイクロプラスチック", "미세플라스틱"]),
    ("bio-based", ["bio-based", "biobased", "生物基", "biosourcé", "de base biológica", "バイオベース", "바이오 기반"]),
    ("compostable", ["compostable", "可堆肥", "compostable", "compostable", "生分解性コンポスト", "퇴비화"]),
    ("biodegradable", ["biodegradable", "可降解", "biodégradable", "biodegradable", "生分解性", "생분해"]),
    ("recyclability design", ["recyclability", "可回收設計", "design for recycling", "recyclabilité", "reciclabilidad", "リサイクル設計", "재활용 설계"]),
    ("mono-material", ["mono-material", "單一材質", "单一材质", "monomatériau", "monomaterial", "モノマテリアル", "단일 소재"]),
    ("single-use plastic", ["single-use plastic", "一次性塑料", "plastique à usage unique", "plástico de un solo uso", "使い捨てプラ", "일회용 플라스틱"]),
    ("digital label", ["digital product passport", "數位產品護照", "数字产品护照", "passeport numérique", "pasaporte digital", "デジタル製品パスポート", "디지털 제품 여권"]),
    ("green claim eco-label", ["eco-label", "EU Ecolabel", "歐盟生態標籤", "écolabel", "etiqueta ecológica", "エコラベル", "에코라벨"]),
    ("plastic tax", ["plastic tax", "塑料稅", "taxe plastique", "impuesto al plástico", "プラスチック税", "플라스틱세"]),
    ("packaging weight reduction", ["lightweighting", "減重", "轻量化", "réduction du poids", "ligereza", "軽量化", "경량화"]),
    ("organic cotton", ["organic cotton", "有機棉", "有机棉", "coton biologique", "algodón orgánico", "オーガニックコットン", "유기농 면"]),
    ("BCI", ["BCI", "Better Cotton", "良好棉花", "coton durable", "algodón sostenible"]),
    ("GOTS", ["GOTS", "全球有機紡織", "全球有机纺织", "Global Organic Textile"]),
    ("RCS", ["RCS", "Recycled Claim Standard", "回收聲明標準"]),
    ("OEKO-TEX", ["OEKO-TEX", "STANDARD 100", "海恩斯坦"]),
    ("chemical ZDHC", ["ZDHC", "MRSL", "限用物質清單", "限用物质清单"]),
    ("water use", ["water footprint", "水足跡", "水足迹", "empreinte eau", "huella hídrica", "ウォーターフットプリント", "물 발자국"]),
    ("circularity repair", ["circularity", "循環經濟", "循环经济", "économie circulaire", "economía circular", "サーキュラー", "순환 경제"]),
    ("solar energy factory", ["solar", "太陽能", "太阳能", "énergie solaire", "energía solar", "太陽光発電", "태양광"]),
    ("audit BSCI Sedex", ["BSCI", "Sedex", "SMETA", "WRAP", "社會責任審核"]),
]

print("扫描文件数:", len(files))
print()
for name, kws in CAND:
    per = []
    for k in kws:
        hit = [f for f, t in texts if k.lower() in t.lower()]
        per.append((k, len(hit), hit[:2]))
    print("%-28s %s" % (name, "  ".join("%s:%d" % (k, n) for k, n, _ in per)))
    for k, n, ex in per:
        if n:
            print("        %s -> %s" % (k, [os.path.basename(x) for x in ex]))
