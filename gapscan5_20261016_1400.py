#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""选题空白扫描 第五轮：服装品类空白"""
import glob, os
from opencc import OpenCC

t2s = OpenCC('t2s')
files = sorted(p for p in glob.glob('blog/*.html') if '_body_' not in os.path.basename(p))
KEYS = ["适老", "適老", "无障碍服装", "银发", "中老年", "老年", "照护", "护理",
        "磁吸扣", "魔术贴", "易穿脱", "术后", "病人服", "医护", "医院", "手术",
        "酒店", "布草", "毛巾", "床品", "浴巾",
        "骑行", "滑雪", "摩托", "潜水", "冲浪", "登山", "钓鱼", "露营", "防晒服",
        "母婴", "婴幼儿", "月子", "亲子", "童装",
        "宗教", "头巾", "hijab", "穆斯林", "阿巴亚", "斗篷", "披风", "和服", "韩服",
        "旗袍", "唐装", "马面裙", "新中式", "国风", "演出服", "电竞", "汉元素",
        "高尔夫", "马术", "击剑", "篮球", "足球", "跑步", "健身", "瑜伽",
        "工作服", "制服", "工装", "保安", "航空", "空乘", "铁路",
        "邮政", "物流", "快递员", "外卖", "餐饮", "咖啡",
        "回收标识", "分选标识", "树脂识别码", "水性胶", "压敏胶", "热熔胶",
        "耐低温", "低温", "冷藏", "冷链",
        "泳池", "氯", "防晒", "抗氯", "海水", "盐雾",
        "抗紫外", "UPF", "抗菌", "防螨", "防蚊", "抗菌整理"]
files_s = {}
for p in files:
    try:
        files_s[p] = t2s.convert(open(p, encoding='utf-8').read())
    except Exception as e:
        print("读失败", p, e)
for k in KEYS:
    hit = [os.path.basename(p) for p, s in files_s.items() if k in s]
    cnt = sum(s.count(k) for s in files_s.values())
    flag = "  <== 空白" if cnt == 0 else ""
    print("%-12s 篇数=%-4d 次数=%-5d %s%s" % (k, len(hit), cnt, ("|".join(hit[:5]) if len(hit) <= 8 else ""), flag))
