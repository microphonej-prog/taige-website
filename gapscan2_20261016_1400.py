#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""选题空白扫描 第二轮"""
import glob, re, os
from opencc import OpenCC

t2s = OpenCC('t2s')
files = sorted(p for p in glob.glob('blog/*.html') if '_body_' not in os.path.basename(p))
KEYS = ["退货", "退换货", "AQL", "抽检", "验货", "湿度指示", "干燥剂", "防潮",
        "碳标签", "CBAM", "碳关税", "碳中和", "碳足迹",
        "FORM A", "RCEP", "自贸", "原产地证", "产地证", "清关", "报关", "商检",
        "拼柜", "体积重", "抛重", "集装箱", "托盘", "缠绕膜", "打托",
        "热敏", "碳带", "打印机", "洗唛二维码", "数字洗水标", "电子洗标",
        "无障碍", "色盲", "皮肤敏感", "致敏", "试穿", "挂装", "立体包装", "塑封",
        "二次销售", "翻新", "换包装", "组合装", "成套", "辅料套装", "礼盒",
        "越南", "印尼", "泰国", "马来西亚", "菲律宾", "新加坡", "德国", "意大利",
        "西班牙", "法国", "波兰", "以色列", "南非", "埃及", "摩洛哥", "尼日利亚",
        "巴基斯坦", "孟加拉", "斯里兰卡", "柬埔寨", "缅甸", "哈萨克", "乌兹别克",
        "厄瓜多尔", "乌拉圭", "巴拉圭", "危地马拉", "哥斯达黎加", "巴拿马", "多米尼加",
        "牙买加", "新西兰", "挪威", "瑞典", "丹麦", "爱尔兰", "葡萄牙", "希腊", "乌克兰",
        "库房", "立体仓", "货架", "拣货", "发货", "标签打印", "贴标机", "自动贴标",
        "供应商切换", "二供", "备选供应商", "议价", "年降", "成本核算", "报价对比",
        "打版", "刀模", "纸样", "出血", "拼版", "印刷文件"]
files_s = {}
for p in files:
    try:
        files_s[p] = t2s.convert(open(p, encoding='utf-8').read())
    except Exception as e:
        print("读失败", p, e)
for k in KEYS:
    hit = [os.path.basename(p) for p, s in files_s.items() if k in s]
    cnt = sum(s.count(k) for s in files_s.values())
    print("%-12s 篇数=%-4d 次数=%-5d %s" % (k, len(hit), cnt, ("|".join(hit[:5]) if len(hit) <= 8 else "")))
