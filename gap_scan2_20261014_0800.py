#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-14 第一批选题空白扫描 round2。"""
import os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
files = []
for lang in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
    files += glob.glob(os.path.join(ROOT, lang + "blog/*.html"))
files = [f for f in files if not os.path.basename(f).startswith("_body")]
texts = [open(f, encoding="utf-8").read().lower() for f in files]

CAND = [
    ("apron/围裙", ["围裙", "apron", "エプロン", "앞치마", "tablier de cuisine"]),
    ("chef/medical uniform", ["厨师服", "chef", "医疗防护", "medical gown", "hospital gown"]),
    ("hotel linen", ["酒店布草", "hotel linen", "linge d'hotel", "lencería hotelera", "ホテルリネン", "호텔 린넨"]),
    ("packing tape/封箱", ["封箱", "封口胶带", "packing tape", "ruban adhésif", "cinta adhesiva", "封緘テープ", "포장 테이프"]),
    ("bubble/气泡袋", ["气泡袋", "bubble bag", "bubble wrap", "film à bulles", "plástico de burbujas", "プチプチ", "에어캡"]),
    ("desiccant/干燥剂", ["干燥剂", "desiccant", "déshydratant", "desecante", "乾燥剤", "건조제"]),
    ("ultrasonic welding", ["超声波", "ultrasonic", "ultrasons", "ultrasonido", "超音波", "초음파"]),
    ("pallet/托盘", ["托盘", "栈板", "pallet", "palette bois", "palé", "パレット", "팔레트"]),
    ("Amazon/FBA", ["亚马逊", "amazon", "FBA", "Amazon FBA"]),
    ("TikTok/直播电商", ["抖音", "小红书", "直播带货", "TikTok Shop", "livestream"]),
    ("worker badge/lanyard", ["工牌", "挂绳", "badge", "lanyard", "badge holder"]),
    ("laundry/dry cleaning", ["干洗", "dry clean", "nettoyage à sec", "tintorería", "ドライクリーニング", "드라이클리닝"]),
    ("wash care symbols", ["洗涤符号", "care symbol", "symbole d'entretien", "símbolo de cuidado", "洗濯表示", "세탁 기호"]),
    ("size sticker on garment", ["尺码贴", "size sticker", "sticker de taille", "pegatina de talla"]),
    ("garment bag/防尘袋", ["防尘袋", "garment bag", "housse", "funda", "ガーメントバッグ", "의류 커버"]),
    ("digital printing label", ["数码印刷", "digital printing", "impression numérique", "impresión digital", "デジタル印刷", "디지털 인쇄"]),
    ("sustainable/fiber EU", ["纤维成分", "fibre composition", "composition des fibres", "composición de fibras", "繊維組成", "섬유 조성"]),
    ("recycled content claim", ["再生材料", "recycled content", "contenu recyclé", "contenido reciclado", "再生材料", "재생 소재"]),
    ("carbon/energy", ["碳足迹", "carbon footprint", "empreinte carbone", "huella de carbono", "カーボンフットプリント", "탄소 발자국"]),
    ("water/waterless printing", ["水性油墨", "water-based ink", "encre à l'eau", "tinta al agua", "水性インキ", "수성 잉크"]),
    ("leather patch", ["皮革标", "leather patch", "patch en cuir", "parche de cuero", "レザーパッチ", "가죽 패치"]),
    ("velcro/hook loop", ["魔术贴", "hook and loop", "velcro", "bande auto-agrippante", "velcro", "マジックテープ", "벨크로"]),
    ("silicone label", ["硅胶标", "silicone label", "étiquette silicone", "etiqueta de silicona", "シリコンラベル", "실리콘 라벨"]),
    ("metal zipper", ["金属拉链", "metal zipper", "fermeture métallique", "cremallera metálica", "金属ファスナー", "금속 지퍼"]),
    ("button/纽扣", ["纽扣", "button", "bouton", "botón", "ボタン", "단추"]),
    ("scale/weight", ["计重", "称重", "weighing", "pesée", "pesaje", "計量", "계량"]),
    ("order tracking", ["订单追踪", "order tracking", "suivi de commande", "seguimiento de pedido"]),
    ("new product development", ["新品开发", "new product development", "développement produit", "desarrollo de producto"]),
    ("trim trend/season", ["流行趋势", "trend", "tendance", "tendencia", "トレンド", "트렌드"]),
    ("sportswear/leggings", ["瑜伽", "紧身裤", "leggings", "leggings", "レギンス", "레깅스"]),
]

print("扫描文件数:", len(files))
print()
for name, kws in CAND:
    per = [(k, sum(1 for t in texts if k.lower() in t)) for k in kws]
    tot = max(n for _, n in per)
    print("%-30s max=%3d   %s" % (name, tot, "  ".join("%s:%d" % (k, n) for k, n in per)))
