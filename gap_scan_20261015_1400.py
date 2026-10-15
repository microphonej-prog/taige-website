#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-15 下午批次：候选选题关键词全站扫描（六语）"""
import os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
files = []
for p in ["blog/*.html", "en/blog/*.html", "fr/blog/*.html", "es/blog/*.html",
          "ja/blog/*.html", "ko/blog/*.html"]:
    files += glob.glob(p)
blob = "\n".join(open(f, encoding="utf-8").read() for f in files)
print("扫描文件数:", len(files), " 字符数:", len(blob))

KEYS = ["丝带", "缎带", "grosgrain", "satin ribbon", "ruban", "리본", "ribbon",
        "文胸", "内衣结构", "罩杯", "bra cup", "brassiere", "lingerie", "브라",
        "医用", "医疗", "防护服", "medical gown", "PPE", "isolation gown", "医療用", "의료",
        "抗菌", "防臭", "antimicrobial", "antibacterial", "odor control", "抗菌防臭",
        "吸湿排汗", "速干", "moisture wicking", "quick-dry", "흡습속건",
        "凉感", "接触凉感", "cooling fabric",
        "议价", "谈判", "negoti", "年度降价", "annual price",
        "框架协议", "framework agreement",
        "打样费", "sample fee", "版费", "tooling fee",
        "退换货", "退货", "returns", "return policy", "replenish",
        "客诉", "complaint", "索赔", "claim handling",
        "替代方案", "substitution", "替代料",
        "双供应商", "dual sourcing", "second source",
        "冷切", "cold cut", "热刀", "hot knife", "hot wire",
        "门襟", "placket",
        "织带染色", "webbing dye", "色牢度 webbing",
        "条码追溯", "追溯码", "traceability code",
        "吊粒", "tag pin", "胶针",
        "安全别针", "safety pin", "epingle",
        "洗水标 缝制", "care label sewing",
        "刺绣标", "embroidery patch",
        "刺绣线", "embroidery thread",
        "丝印", "screen printing",
        "夜光", "反光", "phosphorescent",
        "香氛", "microencapsul", "fragrance",
        "儿童 安全", "drawcord 儿童",
        "腰带", "腰带辅料", "belt loop",
        "衬布", "衬里", "interlining", "fusible",
        "缝纫线 匹配", "thread color match",
        "包装 合规 声明", "packaging claim",
        ]
for k in KEYS:
    print("%-26s %d" % (k, blob.count(k)))
