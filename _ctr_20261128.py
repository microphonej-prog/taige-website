#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CTR 优化（2026-11-28）：6 个高展示低点击页面的 title / meta description 重写

依据：GSC page+query 28 天数据（tools/gsc.py --pairs），选的是「已进首屏或接近首屏、展示量高、CTR 接近 0」的页面。
原则：把用户真实搜索的原词放到标题最前面（含日/韩/西/法的本地写法与常见错拼），标题 60 字符内，描述给具体数字，不承诺做不到的事。

幂等：每条替换前先检查旧串是否还在，不在就跳过并报警（重复跑不会写坏）。
"""
import pathlib, sys, re

ROOT = pathlib.Path(__file__).resolve().parent

# (文件, 旧串, 新串, 说明)
JOBS = [
    # ---------- 1. EN：trims reorder point（348 展示 @4.3，0 点击） ----------
    ("en/blog/small-batch-fast-reorder-trims.html",
     "<title>Trims Reorder Point &amp; Safety Stock: Small-Batch Guide</title>",
     "<title>Trims Reorder Point: Formula &amp; Safety Stock for Small Runs</title>",
     "EN reorder 标题"),
    ("en/blog/small-batch-fast-reorder-trims.html",
     'content="Set a reorder point for hang tags, woven labels and poly bags: safety stock maths, MOQ trade-offs, colour-drift risk, plus 3-7 day sampling and 10-25 day runs."',
     'content="Work the reorder point out from lead time and MOQ, not gut feel: the formula, safety stock for 3-7 day sampling and 10-25 day runs, and colour-drift batching."',
     "EN reorder 描述"),

    # ---------- 2. JA：韓国 洗濯表示（141 展示 @6.5，CTR 0.71%） ----------
    ("ja/blog/clothing-label-compliance-south-korea.html",
     "<title>韓国の衣料ラベル規制ガイド：KCマーク・混用率・韓国語の洗濯表示 | TAGE</title>",
     "<title>韓国 洗濯表示 一覧｜韓国語ラベルとKCマークの意味・書き方 | TAGE</title>",
     "JA 韓国洗濯表示 标题"),
    ("ja/blog/clothing-label-compliance-south-korea.html",
     'content="韓国の衣料ラベル規制ガイド。生活用品安全管理法に基づく品質表示項目、KC の安全確認と供給者適合性確認、混用率の許容差、KS K 0021 の洗濯記号、韓国語の文字サイズ規定まで、輸出前に確認すべき項目を整理しました。"',
     'content="韓国の洗濯表示を一覧で解説。韓国語の洗濯マークの意味、KCマークと供給者適合性確認、混用率の許容差、輸出時に必要な表示項目と文字サイズ規定までまとめました。"',
     "JA 韓国洗濯表示 描述"),

    # ---------- 3. FR：what is epauliere（150 展示 @6.8，0 点击） ----------
    ("fr/blog/shoulder-pad-structure-trims-guide.html",
     "<title>Guide des épaulières et accessoires de structure | TAGE</title>",
     "<title>Épaulière : définition, rôle et 5 constructions comparées | TAGE</title>",
     "FR 肩垫 标题"),
    ("fr/blog/shoulder-pad-structure-trims-guide.html",
     'content="Guide des épaulières et accessoires de structure : cinq constructions comparées, épaisseur et forme selon le vêtement, plus toile de poitrine et feutre de col."',
     'content="Qu’est-ce qu’une épaulière ? Définition, rôle dans l’épaule, cinq constructions comparées (épaisseur, forme, maintien), plus toile de poitrine et feutre de col."',
     "FR 肩垫 描述"),

    # ---------- 4. ES：reetiquetado（117 展示 @8.8，0 点击） ----------
    ("es/blog/apparel-relabeling-service-guide.html",
     "<title>Reetiquetado de prendas: qué es, cuándo y cómo se hace</title>",
     "<title>Reetiquetado de prendas: 6 accesorios y 3 riesgos</title>",
     "ES reetiquetado 标题"),
    ("es/blog/apparel-relabeling-service-guide.html",
     'content="Cambiar de marca, mercado o tallaje obliga a reetiquetar. Seis accesorios a sustituir, descoser o sobreetiquetar, seis riesgos, presupuesto y control."',
     'content="Reetiquetado: qué es, cuándo lo exige un cambio de marca, mercado o tallaje, los 6 accesorios a sustituir o sobreetiquetar, los riesgos y el control de calidad."',
     "ES reetiquetado 描述"),

    # ---------- 5. KO：드로코드（98 展示 @3.8–8.4，0 点击） ----------
    ("ko/blog/garment-drawcord-guide.html",
     "<title>드로코드 종류와 팁 마감: 후디·재킷 스트링 선택 가이드</title>",
     "<title>드로코드 종류 4가지와 후디·재킷 스트링 선택법 | TAGE</title>",
     "KO 드로코드 标题"),
    ("ko/blog/garment-drawcord-guide.html",
     'content="원형 코드, 평직 테이프, 편조 코드, 신축 코드의 용도별 비교와 폴리에스터·면·나일론·재생 폴리 선택 기준, 금속·플라스틱 팁 마감, EN 14682와 ASTM F1816 아동복 규정, 견적 기준까지 정리했습니다."',
     'content="원형 코드·평직 테이프·편조·신축 코드 4가지 비교, 후디·재킷·코트별 선택 기준, 금속·플라스틱 팁 마감, EN 14682·ASTM F1816 아동복 규정까지 정리했습니다."',
     "KO 드로코드 描述"),

    # ---------- 6. ZH-Hant + EN：正嘜側嘜 / carton marks ----------
    ("blog/carton-shipping-mark-guide.html",
     'data-zh="正嘜側嘜位置與外箱嘜頭範例：六項必填欄位 | TAGE"',
     'data-zh="正嘜側嘜位置範例（含正麥側麥）｜外箱嘜頭六項必填欄位 | TAGE"',
     "ZH 箱嘜 标题属性"),
    ("blog/carton-shipping-mark-guide.html",
     ">正嘜側嘜位置與外箱嘜頭範例：六項必填欄位 | TAGE</title>",
     ">正嘜側嘜位置範例（含正麥側麥）｜外箱嘜頭六項必填欄位 | TAGE</title>",
     "ZH 箱嘜 可见标题"),
    ("blog/carton-shipping-mark-guide.html",
     'data-zh="正嘜貼箱面右上、側嘜貼短邊側面，位置錯了目的港倉庫照樣拒收。六項必填欄位逐條拆解，毛重淨重怎麼實測、箱規標記怎麼寫，附嘜頭範本與直接印刷對比貼標的單箱成本，換款不必重開版。"',
     'data-zh="正嘜（正麥）貼箱面右上、側嘜（側麥）貼短邊側面，位置錯了目的港倉庫照樣拒收。六項必填欄位逐條拆解，毛重淨重怎麼實測、箱規標記怎麼寫，附嘜頭範本與直接印刷對比貼標的單箱成本。"',
     "ZH 箱嘜 描述"),
    ("en/blog/carton-shipping-mark-guide.html",
     "<title>Carton Mark Placement: Main &amp; Side Mark Positions, 6 Fields</title>",
     "<title>Carton Shipping Marks: Main &amp; Side Placement, 6 Fields</title>",
     "EN 箱嘜 标题"),
    ("en/blog/carton-shipping-mark-guide.html",
     'content="Wrong carton mark placement still gets containers rejected. Six mandatory fields, measured G.W./N.W., size marks, a fill-in template and print-vs-sticker cost."',
     'content="Wrong carton mark placement still gets containers rejected. Six mandatory fields, measured G.W./N.W., size marks, a fill-in template and print-vs-sticker cost per carton."',
     "EN 箱嘜 描述"),
]


def main():
    touched = {}
    failed = []
    for rel, old, new, label in JOBS:
        p = ROOT / rel
        if not p.exists():
            failed.append((rel, label, "文件不存在")); continue
        s = p.read_text(encoding="utf-8")
        n = s.count(old)
        if n == 0:
            failed.append((rel, label, "旧串没找到（可能已改过）")); continue
        s = s.replace(old, new)
        p.write_text(s, encoding="utf-8")
        touched[rel] = touched.get(rel, 0) + n
        print(f"✓ {rel:<52} {label}  ({n} 处)")

    print("\n改动文件：")
    for rel, n in touched.items():
        print(f"  {rel}  →  {n} 处")
    if failed:
        print("\n未改动：")
        for rel, label, why in failed:
            print(f"  ✗ {rel} | {label} | {why}")
        sys.exit(1)


if __name__ == "__main__":
    main()
