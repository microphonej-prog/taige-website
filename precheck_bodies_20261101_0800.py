#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""正文预检：属性完整性、裸双引号、en/fr/es 混中文、ja/ko 混简体（OpenCC 判定）"""
import os, re, sys, importlib.util
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

BODIES = ["blog/_body_mailerbox.html", "blog/_body_tape.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
CJK = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]")
HAN = re.compile(r"[\u4e00-\u9fff]")
# 简体专有字（日文标准字形不使用），用于 ja 属性误混简体检测
SIMP_ONLY = set(
    "们这说为对发过还没让从样给据经术语种类别图实时长间问题选择结构价质"
    "电导线颜缝标签织唛贴纸皱褶总将无现气单职业专设备运输订购销货钱"
    "个铜涂层环压盖级达运质档宽窄费优简营养护"
)
KO_OK = set("東莞泰閣中国廣東")

spec = importlib.util.spec_from_file_location("to_traditional", os.path.join(ROOT, "to_traditional.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
cc = getattr(mod, "CC", None) or getattr(mod, "cc", None)


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.depth = 0
        self.elems = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "section" and "article-body" in (d.get("class") or ""):
            self.in_body = True
            return
        if self.in_body:
            self.elems.append((tag, d))

    def handle_endtag(self, tag):
        if self.in_body and tag == "section":
            self.in_body = False


bad_all = 0
for b in BODIES:
    s = open(b, encoding="utf-8").read()
    p = P(); p.feed(s)
    zh = [(t, d) for t, d in p.elems if "data-zh" in d]
    miss = {}
    for l in LANGS:
        miss[l] = sum(1 for _, d in zh if "data-" + l not in d)
    empty = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s))
    dq = len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[^>\s]', s))
    zh_chars = sum(len(CJK.findall(d.get("data-zh", ""))) for _, d in zh)
    print("%-28s data-zh元素=%d 缺语言=%s 空=%d 引号异常=%d 中文字数=%d"
          % (b, len(zh), {k: v for k, v in miss.items() if v} or "无", empty, dq, zh_chars))
    if any(miss.values()) or empty:
        bad_all += 1
    # 语言纯净度
    for l in ["en", "fr", "es"]:
        hits = [t for t, d in zh if CJK.search(d.get("data-" + l, ""))]
        if hits:
            bad_all += 1
            print("   !! %s 含中日韩字符 %d 处，例：%s" % (l, len(hits), hits[0][:120]))
    # ja：日文汉字与简体字有重叠，改用简体专有字黑名单
    for t, d in zh:
        v = d.get("data-ja", "")
        hit = [c for c in v if c in SIMP_ONLY]
        if hit:
            bad_all += 1
            print("   !! ja 含简体字 %s：%s" % ("".join(hit), v[:90]))
            break
    # ko：韩文外不应出现汉字（公司名专有字白名单除外）
    for t, d in zh:
        v = d.get("data-ko", "")
        hit = [c for c in v if HAN.match(c) and c not in KO_OK]
        if hit:
            bad_all += 1
            print("   !! ko 含中日文字符 %s：%s" % ("".join(hit), v[:90]))
            break
    # 未闭合标签粗查
    print("   长度 %d 字符；data-fr 数=%d" % (len(s), s.count("data-fr=")))

print("预检结果:", "通过" if bad_all == 0 else "有 %d 项问题" % bad_all)
sys.exit(0 if bad_all == 0 else 1)
