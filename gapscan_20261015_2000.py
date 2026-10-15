#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""选题空白扫描：把 blog/*.html 全部转简体后统计候选关键词出现篇数/次数"""
import glob, re, os
from opencc import OpenCC

t2s = OpenCC('t2s')
files = sorted(p for p in glob.glob('blog/*.html') if '_body_' not in os.path.basename(p))
print("扫描文件数:", len(files))

KEYS = ["折叠", "折法", "中折", "侧缝", "后领", "尺码对照", "尺码体系", "洗涤符号", "洗涤标识",
        "ISO 3758", "色差", "ΔE", "耐光", "耐日晒", "日晒", "克重", "缝制方式", "缝制位置",
        "吊牌绳", "胶针", "防伪", "序列号", "平压", "烫银", "植绒", "异形", "样品册",
        "收缩率", "紫外线", "抗静电", "防霉", "霉斑", "仓储", "湿度", "回收料", "再生料",
        "GRS", "OEKO", "Oeko", "FSC", "生物基", "可降解", "堆肥", "碳足迹", "水洗测试",
        "摩擦色牢度", "耐汗渍", "耐唾液", "甲醛", "偶氮", "邻苯", "重金属", "铅", "CPSIA",
        "小零件", "拉脱力", "断针", "检针", "金属探测", "吊粒", "打孔位置", "穿绳",
        "法式折", "蝴蝶折", "对折", "三折", "四折", "多折", "折页", "展开尺寸",
        "标签成本", "打样费", "阶梯价", "模具费", "版费", "刀模", "电雕", "激光",
        "贴纸", "不干胶", "热转印", "硅胶标", "滴胶", "织唛密度", "纬密", "经密",
        "校服", "工装", "酒店布草", "宠物", "婴幼儿", "泳装", "羽绒", "牛仔", "针织",
        "汉服", "婚纱", "雪纺", "丝绸", "羊毛", "羊绒", "涤纶", "尼龙", "棉"]
files_s = {}
for p in files:
    try:
        files_s[p] = t2s.convert(open(p, encoding='utf-8').read())
    except Exception as e:
        print("读失败", p, e)

for k in KEYS:
    hit = [os.path.basename(p) for p, s in files_s.items() if k in s]
    cnt = sum(s.count(k) for s in files_s.values())
    print("%-8s 篇数=%-4d 次数=%-5d %s" % (k, len(hit), cnt, ("|".join(hit[:6]) if len(hit) <= 8 else "")))
