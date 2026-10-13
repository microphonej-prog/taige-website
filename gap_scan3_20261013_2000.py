#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-13 晚间（20:00）批次候选选题空白扫描（第四类线索：召回/漂绿/胶粘剂/贸易术语/家纺等）"""
import glob, os, collections

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

files = sorted(glob.glob("blog/**/*.html", recursive=True))
KWS = [
    # 召回与市场撤下
    "召回", "recall", "Recall", "撤回", "下架", "撤市", "withdrawal", "CPSC",
    # 环保声明 / 漂绿
    "漂绿", "greenwashing", "green claim", "Green Claims", "环境声明", "环保声明", "绿色声明",
    # 胶粘剂 / 不干胶
    "不干胶", "压敏胶", "adhesive", "Adhesive", "可移除", "永久胶", "低温胶", "冻胶", "背胶",
    # 贸易术语
    "Incoterm", "incoterm", "贸易术语", "EXW", "FOB", "DDP", "CIF", "DAP",
    # 生态设计法规
    "ESPR", "生态设计", "ecodesign", "Ecodesign", "可持续产品",
    # 服装品类空白
    "领带", "领结", "necktie", "bow tie", "家纺", "床品", "毛巾", "浴袍", "home textile", "bedding",
    # 设备与耗材
    "碳带", "条码打印机", "标签打印机", "热转印膜", "thermal transfer", "缝纫机", "sewing machine",
    # 织唛纱线
    "织唛用线", "纱线", "涤纶线", "尼龙线", "金银线", "夜光线", "yarn",
    # 扣具与绳头
    "绳扣", "抽绳头", "cord lock", "调节扣", "buckle", "卡扣", "金属头",
    # 包装细节
    "易撕口", "撕口", "tear notch", "打孔袋", "透气孔",
    # 仓储与库存
    "库房", "仓储", "储存条件", "温湿度", "shelf life", "保质期",
    # 货运相关
    "货运保险", "货物保险", "cargo insurance", "拼柜", "LCL", "拖车",
    # 其他服务
    "验货", "第三方验货", "inspection service", "打托", "pallet",
    # 材质/工艺
    "丝网印刷", "丝印", "screen printing", "数码印刷", "digital printing", "柔印", "凸印",
    "热压", "高频", "超声波",
    # 品牌与设计
    "字体授权", "font license", "logo 规范", "品牌规范", "brand guideline",
    # 电商
    "亚马逊", "Amazon", "TikTok", "SHEIN", "Temu", "平台规则",
]
cnt = collections.Counter()
where = collections.defaultdict(list)
for f in files:
    s = open(f, encoding="utf-8").read()
    for k in KWS:
        n = s.count(k)
        if n:
            cnt[k] += n
            where[k].append((f.replace("\\", "/"), n))

for k in KWS:
    lst = sorted(where[k], key=lambda x: -x[1])
    print("== %-16s %-4d %s" % (k, cnt[k], " | ".join("%s:%d" % (a, b) for a, b in lst[:3])))
