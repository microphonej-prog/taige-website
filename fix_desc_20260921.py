#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修正两篇新文章的多语 description 长度（zh 80-120 字、en 150-160 字符），
然后重新生成五语版本。"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

NEW = {
    "blog/hanger-bag-guide.html": dict(
        zh="服装挂装胶袋指南：挂装与平装怎么取舍、四种常见袋型、袋宽袋长如何从肩宽衣长反推、挂钩开孔与承重加固、材质厚度与防雾膜、印刷与出口标识，附打样验收清单。来自东莞泰阁包装。",
        en="Hanger bag guide: hanging versus flat packing, four bag types, sizing from shoulder width, hook holes and load, anti-fog film, printing and sampling checks.",
        ja="ハンガー袋のガイド。掛け包装と平積みの使い分け、4タイプの袋、肩幅と着丈からの寸法逆算、フック穴と耐荷重、素材と防曇フィルム、印刷・輸出表示、サンプル検収まで解説します。東莞泰閣包装。",
        ko="걸이 비닐봉투 가이드: 걸이 포장과 평면 포장의 선택, 네 가지 봉투 형태, 어깨너비에서 치수 역산, 고리 구멍과 하중, 김서림 방지 필름, 인쇄와 수출 표시까지 정리했습니다. 둥관 TAGE 패키징.",
        fr="Guide des housses à suspendre : suspension ou emballage à plat, quatre types de sacs, dimensions depuis le vêtement, trous et charge, film anti-buée et marquage export.",
        es="Guía de bolsas colgantes: colgar o empaquetar en plano, cuatro tipos, medidas desde la prenda, orificios y carga, film antivaho y marcado de exportación.",
    ),
    "blog/shrink-film-packaging-guide.html": dict(
        zh="服装热收缩膜包装指南：PE、POF 与交联 PE 的透明度与收缩温度差异、收缩方向造成的变形、15–25μm 厚度差别、封口与排气打孔参数、与胶袋的取舍，附打样验收清单。来自东莞泰阁包装。",
        en="Shrink film guide: PE, POF and cross-linked PE compared, distortion from shrink direction, 15–25μm thickness, sealing and venting, and film versus bags.",
        ja="衣料品のシュリンク包装ガイド。PE・POF・架橋PEの透明性と収縮温度の違い、収縮方向による歪み、15〜25μmの厚み、シールとベント穴、ポリ袋との比較を解説します。東莞泰閣包装。",
        ko="의류 수축 필름 포장 가이드: PE, POF, 가교 PE의 투명도와 수축 온도 차이, 수축 방향에 따른 변형, 15~25μm 두께, 실링과 에어 벤트, 비닐봉투와의 비교를 정리했습니다. 둥관 TAGE 패키징.",
        fr="Guide du film rétractable : PE, POF et réticulé comparés, déformation liée au sens de retrait, épaisseurs de 15 à 25 μm, soudure et évents, film ou sachet.",
        es="Guía del film retráctil: PE, POF y reticulado comparados, deformación por la dirección de retracción, 15–25 μm, sellado y venteo, film o bolsa.",
    ),
}

for p, d in NEW.items():
    print("%-46s zh=%d字 en=%d ja=%d ko=%d fr=%d es=%d"
          % (os.path.basename(p), len(d["zh"]), len(d["en"]), len(d["ja"]), len(d["ko"]),
             len(d["fr"]), len(d["es"])))
    assert 80 <= len(d["zh"]) <= 120, "zh 长度不合规"
    assert 150 <= len(d["en"]) <= 160, "en 长度不合规"

for p, d in NEW.items():
    s = open(p, encoding="utf-8").read()
    block = ('<meta name="description" data-zh="%s"\n'
             '      data-en="%s" data-ja="%s" data-ko="%s"\n'
             '      data-fr="%s"\n'
             '      data-es="%s"\n'
             '      content="%s">' % (d["zh"], d["en"], d["ja"], d["ko"], d["fr"], d["es"], d["zh"]))
    s2, n = re.subn(r'<meta name="description".*?content="[^"]*">', block, s, count=1, flags=re.S)
    assert n == 1, "description 替换失败: %s" % p
    open(p, "w", encoding="utf-8", newline="").write(s2)
    print("已更新 description: %s" % p)

# 简体 -> 繁体（幂等）
spec = importlib.util.spec_from_file_location("to_traditional", os.path.join(ROOT, "to_traditional.py"))
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
for p in NEW:
    s0 = open(p, encoding="utf-8").read()
    s1 = mod.convert_html(s0)
    if s1 != s0:
        open(p, "w", encoding="utf-8", newline="").write(s1)
    print("繁体转换完成: %s" % p)

# 重新生成五语版本
for lang in ["en", "ja", "ko", "fr", "es"]:
    r = subprocess.run([PY, "gen_i18n.py", lang] + list(NEW.keys()),
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print(r.stdout[-2000:], r.stderr[-2000:])
        raise SystemExit("gen_i18n %s 失败" % lang)
print("gen_i18n 五语重新生成完成")
