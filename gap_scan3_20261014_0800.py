#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-14 第一批选题空白扫描 round3：中文关键词改用繁体（根目录页已转繁）。"""
import os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
files = []
for lang in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
    files += glob.glob(os.path.join(ROOT, lang + "blog/*.html"))
files = [f for f in files if not os.path.basename(f).startswith("_body")]
texts = [(f, open(f, encoding="utf-8").read()) for f in files]

CAND = [
    ("apron 圍裙", ["圍裙", "围裙", "apron", "エプロン", "앞치마"]),
    ("chef 廚師服", ["廚師服", "厨师服", "chef ", "chef's", "コックコート", "조리복"]),
    ("medical 醫療服", ["醫療", "手术衣", "手術衣", "medical gown", "surgical gown", "scrubs"]),
    ("metamerism 同色異譜", ["同色異譜", "同色异谱", "metamerism", "métamérisme", "metamerismo", "條件等色"]),
    ("desiccant 乾燥劑", ["乾燥劑", "干燥剂", "desiccant"]),
    ("pallet 托盤", ["托盤", "托盘", "pallet"]),
    ("carbon 碳足跡", ["碳足跡", "碳足迹", "carbon footprint"]),
    ("fiber 纖維成分", ["纖維成分", "纤维成分", "fibre composition", "fiber composition"]),
    ("care symbols 洗滌符號", ["洗滌符號", "洗涤符号", "care symbol", "洗濯表示", "세탁 기호"]),
    ("dry clean 乾洗", ["乾洗", "干洗", "dry clean"]),
    ("garment bag 防塵袋", ["防塵袋", "防尘袋", "garment bag"]),
    ("digital print 數碼印刷", ["數碼印刷", "数码印刷", "digital printing"]),
    ("button 紐扣", ["紐扣", "纽扣", "button "]),
    ("silicone 矽膠標", ["矽膠標", "硅胶标", "silicone label"]),
    ("leather patch 皮革標", ["皮革標", "皮革标", "leather patch"]),
    ("velcro 魔術貼", ["魔術貼", "魔术贴", "魔鬼氈", "velcro", "hook and loop"]),
    ("size sticker 尺碼貼", ["尺碼貼", "尺码贴", "size sticker"]),
    ("NPD 新品開發", ["新品開發", "新品开发", "new product development", "新商品開発"]),
    ("laser 激光鏤空", ["激光鏤空", "鐳射", "激光切割", "laser cut", "laser-cut"]),
    ("vegan leather 素皮", ["素皮", "純素皮革", "vegan leather", "植物基皮革"]),
    ("sportswear 瑜伽", ["瑜伽", "緊身褲", "leggings", "yoga"]),
    ("hotel linen 酒店布草", ["酒店布草", "hotel linen", "hospitality textile"]),
    ("badge 工牌", ["工牌", "掛繩", "lanyard", "badge holder"]),
    ("ultrasonic 超聲波", ["超聲波", "超声波", "ultrasonic"]),
    ("tag trend 流行趨勢", ["流行趨勢", "流行趋势", "trend"]),
    ("trim storage 輔料倉儲", ["輔料倉儲", "倉儲", "倉庫", "warehouse storage"]),
]

print("扫描文件数:", len(files))
print()
for name, kws in CAND:
    per = []
    for k in kws:
        hit = [f for f, t in texts if k.lower() in t.lower()]
        per.append((k, len(hit), hit[:2]))
    print("%-26s %s" % (name, "  ".join("%s:%d" % (k, n) for k, n, _ in per)))
    for k, n, ex in per:
        if n:
            print("        %s -> %s" % (k, [os.path.basename(x) for x in ex]))
