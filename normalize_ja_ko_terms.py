#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""术语统一 + 补齐未标注中文（幂等）
- 只在 data-ja / data-ko 属性值内做术语替换（不碰中文默认文本、不碰其它属性）
- 给 4 个主页面的 微信 / 在线 / 发送 三处未标注文本补 data-zh/en/ja/ko/fr/es
用法: python normalize_ja_ko_terms.py [--dry]
"""
import re, sys

DRY = '--dry' in sys.argv
FILES = ["index.html", "products.html", "about.html", "contact.html"]

JA_RULES = [
    ("アパレル用タグ", "衣料用タグ"), ("アパレル吊り札", "衣料用タグ"),
    ("織りネーム", "織りラベル"), ("メインネーム", "メインラベル"), ("主ラベル", "メインラベル"),
    ("製品ラインナップ", "製品一覧"), ("製品センター", "製品一覧"),
    ("お見積もり依頼", "お見積り依頼"),
    ("環境にやさしい紙袋", "エコ紙袋"),
    ("宣伝パンフレット", "パンフレット"),
    ("TAGE包装", "泰閣包装"),
]
KO_RULES = [
    ("태각 포장", "TAGE 패키징"), ("TAGE 포장", "TAGE 패키징"),
    ("타이거", "TAGE"), ("태거", "TAGE"),
    ("포장제품 유한공사", "패키징 유한공사"),
    ("동관", "둥관"),
    ("연락처", "문의하기"),
    ("케어 라벨", "세탁 표시 라벨"),
    ("포장 백", "포장백"),
    ("홍보 브로셔", "브로슈어"), ("브로셔", "브로슈어"),
    ("빠른 링크", "바로가기"),
]

UNTAGGED = [
    ('<span>微信 13128118931</span>',
     '<span data-zh="微信 13128118931" data-en="WeChat 13128118931" data-ja="WeChat 13128118931" '
     'data-ko="위챗 13128118931" data-fr="WeChat 13128118931" data-es="WeChat 13128118931">微信 13128118931</span>'),
    ('<span class="st" id="assistStatus">在线</span>',
     '<span class="st" id="assistStatus" data-zh="在线" data-en="Online" data-ja="オンライン" '
     'data-ko="온라인" data-fr="En ligne" data-es="En línea">在线</span>'),
    ('<button id="assistSend" type="button">发送</button>',
     '<button id="assistSend" type="button" data-zh="发送" data-en="Send" data-ja="送信" '
     'data-ko="보내기" data-fr="Envoyer" data-es="Enviar">发送</button>'),
]


def fix_attr_values(s, attr, rules):
    n = [0]

    def repl(m):
        v = m.group(1)
        for a, b in rules:
            if a in v:
                v = v.replace(a, b)
                n[0] += 1
        return '%s="%s"' % (attr, v)
    s = re.sub(r'%s="([^"]*)"' % attr, repl, s, flags=re.S)
    return s, n[0]


if __name__ == '__main__':
    for f in FILES:
        s0 = s = open(f, encoding='utf-8').read()
        s, n_ja = fix_attr_values(s, 'data-ja', JA_RULES)
        s, n_ko = fix_attr_values(s, 'data-ko', KO_RULES)
        # 副資材 FAQ 修正（负向前瞻避免重复加）
        s = re.sub(r'(?<!副)資材 FAQ', '副資材 FAQ', s)
        n_untagged = 0
        for old, new in UNTAGGED:
            if old in s:
                s = s.replace(old, new)
                n_untagged += 1
        print('%-16s ja替换=%d ko替换=%d 未标注补齐=%d 有变化=%s' % (f, n_ja, n_ko, n_untagged, s != s0))
        if s != s0 and not DRY:
            open(f, 'w', encoding='utf-8', newline='').write(s)
    if DRY:
        print('(dry-run)')
