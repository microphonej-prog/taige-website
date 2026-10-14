#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-14 下午批次：候选选题关键词第二遍扫描"""
import os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
files = []
for p in ["blog/*.html", "en/blog/*.html", "fr/blog/*.html", "es/blog/*.html",
          "ja/blog/*.html", "ko/blog/*.html"]:
    files += glob.glob(p)
blob = "\n".join(open(f, encoding="utf-8").read() for f in files)

KEYS = ["文胸", "内衣结构", "罩杯", "泡棉", "海绵", "bra cup", "brassiere", "lingerie",
        "丝带", "缎带", "罗纹带", "ribbon", "grosgrain", "ruban", "리본",
        "别针", "safety pin", "吊粒", "tag pin", "胶针", "pince",
        "医用", "医疗", "防护服", "medical gown", "PPE", "isolation gown", "医療",
        "家纺", "床品", "毛巾", "home textile", "bedding", "towel",
        "抗菌", "防臭", "antibacterial", "antimicrobial", "odor control",
        "吸湿排汗", "速干", "moisture wicking", "quick-dry",
        "凉感", "cooling fabric", "接触凉感",
        "保暖", "发热", "thermal lining", "heat-retaining", "石墨烯",
        "防静电", "anti-static", "antistatic",
        "议价", "谈判", "negotiat", "年度降价", "annual price",
        "框架协议", "framework agreement", "年度合同",
        "供应商准入", "新供应商", "supplier onboarding", "supplier qualification",
        "打样费", "sample fee", "版费", "tooling fee",
        "退换货", "退货", "returns", "return policy", "补货", "replenish",
        "客诉", "complaint", "索赔",
        "替代方案", "substitution", "替代料",
        "双供应商", "dual sourcing", "second source", "备份供应商",
        "价格年审", "涨价", "price increase", "原材料涨", "cost pass-through",
        "冷切", "cold cut", "热刀", "hot knife", "hot wire", "heat seal cut",
        "placket", "placket interlining", "门襟",
        "织带染色", "webbing dyeing", "织带色牢度",
        "条码追溯", "traceability", "追溯码",
        ]
for k in KEYS:
    print("%-24s %d" % (k, blob.count(k)))
