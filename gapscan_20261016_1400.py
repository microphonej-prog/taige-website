#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""选题空白扫描：把 blog/*.html 全部转简体后统计候选关键词出现篇数/次数"""
import glob, re, os
from opencc import OpenCC

t2s = OpenCC('t2s')
files = sorted(p for p in glob.glob('blog/*.html') if '_body_' not in os.path.basename(p))
print("扫描文件数:", len(files))

KEYS = ["种子纸", "可种植", "种植", "植物种子", "plantable", "seeded paper",
        "租赁", "共享衣橱", "租衣", "rental", "循环时尚", "旧衣回收",
        "草浆", "甘蔗渣", "竹浆", "农业废料", "咖啡渣", "再生棉", "海洋塑料", "再生涤纶", "rPET",
        "一物一码", "溯源", "数字护照", "NFC",
        "文案", "信息层级", "字体", "排版", "版式", "字号",
        "拉力", "拉脱力", "鸡眼", "吊粒", "棉绳", "弹力绳",
        "开箱", "快递", "快递袋", "气泡袋", "填充",
        "关税", "HS编码", "原产地", "标签机", "条码打印机",
        "打样费", "模具", "版费", "阶梯", "报价单",
        "旺季", "黑五", "双十一", "淡季", "排产",
        "样衣", "工艺单", "规格书", "限样",
        "改标", "换标", "返工", "库存",
        "亚马逊", "TikTok", "SHEIN", "快反", "小单",
        "生物基", "可降解", "堆肥", "PLA", "水溶性",
        "扎带", "吊挂", "衣架", "标签枪", "吊牌枪",
        "标签一致性", "三码合一", "信息核对"]
files_s = {}
for p in files:
    try:
        files_s[p] = t2s.convert(open(p, encoding='utf-8').read())
    except Exception as e:
        print("读失败", p, e)

for k in KEYS:
    hit = [os.path.basename(p) for p, s in files_s.items() if k in s]
    cnt = sum(s.count(k) for s in files_s.values())
    print("%-10s 篇数=%-4d 次数=%-5d %s" % (k, len(hit), cnt, ("|".join(hit[:6]) if len(hit) <= 8 else "")))
