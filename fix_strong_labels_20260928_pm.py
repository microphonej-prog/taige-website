#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 <li> 可见文本里的 <strong>小标题：</strong> 补进对应的六语 data-* 属性
（2026-09-28 下午批次）。属性值里禁止裸双引号，这里只用单引号/无引号文案。

用法: <python> fix_strong_labels_20260928_pm.py [--apply]
"""
import re, sys

sys.stdout.reconfigure(encoding="utf-8")
APPLY = "--apply" in sys.argv
FILES = ["blog/_body_origin.html", "blog/_body_pp.html"]

# 中文标签 -> (en, ja, ko, fr, es)
L = {
    "美国：": ("United States", "米国", "미국", "États-Unis", "Estados Unidos"),
    "欧盟与英国：": ("EU and UK", "EU・英国", "EU·영국", "UE et Royaume-Uni", "UE y Reino Unido"),
    "中东：": ("Middle East", "中東", "중동", "Moyen-Orient", "Oriente Medio"),
    "拉美：": ("Latin America", "中南米", "중남미", "Amérique latine", "Latinoamérica"),
    "日本与韩国：": ("Japan and Korea", "日本・韓国", "일본·한국", "Japon et Corée", "Japón y Corea"),
    "电商平台：": ("Marketplaces", "EC プラットフォーム", "전자상거래 플랫폼", "Places de marché", "Plataformas de venta"),
    "用法：": ("Wording", "表記", "표기", "Formulation", "Redacción"),
    "一致性：": ("Consistency", "一貫性", "일관성", "Cohérence", "Coherencia"),
    "耐洗：": ("Wash resistance", "耐洗性", "내세탁성", "Tenue au lavage", "Resistencia al lavado"),
    "版面：": ("Layout", "レイアウト", "레이아웃", "Mise en page", "Maqueta"),
    "透明袋：": ("Clear bags", "透明フィルム", "투명 필름", "Film transparent", "Film transparente"),
    "不一致：": ("Disagreeing surfaces", "不一致", "불일치", "Surfaces divergentes", "Superficies en desacuerdo"),
    "漏印：": ("Omission", "記載漏れ", "누락", "Oubli", "Omisión"),
    "被裁：": ("Cut away", "断裁で欠落", "재단 손실", "Coupé au rognage", "Cortado"),
    "语言不符：": ("Wrong language", "言語不一致", "언어 불일치", "Mauvaise langue", "Idioma incorrecto"),
    "转口要求：": ("Third-country requests", "第三国表示の要請", "제3국 표기 요청", "Demande d'un pays tiers", "Solicitud de tercer país"),
    "三方签样：": ("Three-way sign-off", "三者署名", "3자 서명", "Validation à trois", "Firma a tres bandas"),
    "记录要素：": ("Record the essentials", "記録項目", "기록 항목", "Éléments à tracer", "Datos a registrar"),
    "实物与照片双留：": ("Keep both object and image", "現物と写真の併用", "실물과 사진 병행", "Objet et photo", "Objeto y foto"),
    "有效期：": ("Validity", "有効期間", "유효 기간", "Validité", "Validez"),
    "变更重签：": ("Re-approve on change", "変更時は再承認", "변경 시 재승인", "Revalider tout changement", "Revalidar cambios"),
    "写进订单：": ("Write it into the order", "注文書に明記", "주문서에 명시", "Inscrire au commande", "Escribirlo en el pedido"),
    "留缓冲：": ("Allow buffer", "余裕を確保", "버퍼 확보", "Prévoir une marge", "Deja margen"),
    "包装同步：": ("Approve packing together", "包装も同時に", "포장도 함께", "Valider l'emballage en même temps", "Aprobar el embalaje a la vez"),
    "寄了不看：": ("Sent but unread", "送ったが見られない", "보냈지만 확인 없음", "Envoyé, jamais lu", "Enviado y sin leer"),
    "标准含糊：": ("Vague standards", "基準が曖昧", "기준 모호", "Critères flous", "Criterios vagos"),
    "多头确认：": ("Too many approvers", "承認者が多頭", "승인자 다수", "Trop de valideurs", "Demasiados validadores"),
}
PUNCT = {"en": ":", "ja": "：", "ko": ":", "fr": " :", "es": ":"}
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
STRIP = re.compile(r"^(?:三处不一致|位置被裁掉|不一致|被裁)[：:]")

def find_lis(s):
    """返回 [(start, head_end, end, head, visible)]，属性值内可能含 <strong> 的 > ，需按引号扫描"""
    res, i = [], 0
    while True:
        st = s.find("<li", i)
        if st == -1:
            break
        j, in_q = st + 3, None
        while j < len(s):
            ch = s[j]
            if in_q:
                if ch == in_q:
                    in_q = None
            elif ch in '"\'':
                in_q = ch
            elif ch == ">":
                break
            j += 1
        en = s.find("</li>", j)
        if en == -1:
            print("  !! 未闭合 <li> @%d" % st)
            break
        res.append((st, j, en, s[st + 3:j], s[j + 1:en]))
        i = en + 5
    return res


total = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    out = []
    for st, head_end, en, head, vis in find_lis(s):
        lm = re.match(r"\s*<strong>(.*?)</strong>", vis)
        if "data-zh=" not in head or not lm:
            continue
        label = lm.group(1)
        if not label.endswith("：") or label not in L:
            print("  ?? 未登记标签：%s (%s)" % (label, f))
            continue
        new_head = head
        changed = False
        for i, lang in enumerate(LANGS):
            am = re.search(r'data-%s="([^"]*)"' % lang, new_head)
            if not am or am.group(1).startswith("<strong>"):
                continue
            val = STRIP.sub("", am.group(1))
            if lang == "zh":
                lab = label
            else:
                lab = L[label][LANGS.index(lang) - 1] + PUNCT[lang]
            new_head = new_head[:am.start(1)] + "<strong>%s</strong>%s" % (lab, val) + new_head[am.end(1):]
            changed = True
        if changed:
            total += 1
            out.append((st, en + 5, "<li" + new_head + ">" + vis + "</li>"))
    for st, en2, rep in reversed(out):
        s = s[:st] + rep + s[en2:]
    if out and APPLY:
        open(f, "w", encoding="utf-8", newline="").write(s)
        print("已写盘 %s（%d 处）" % (f, len(out)))
    else:
        print("%s：待处理 %d 处" % (f, len(out)))
print("合计处理 %d 处（%s）" % (total, "APPLY" if APPLY else "dry-run"))
