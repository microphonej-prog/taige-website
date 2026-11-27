#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""持续优化 · 第 3 批（2026-11-28）：A 类剩下的两页（排 5–6 名、CTR 0）

依据 GSC（28 天）：
  /en/blog/apparel-trims-hs-code-customs.html  91 展示 @5.2，0 点击
      trim hs code 12@6.4 · main label hs code 8@2.4 · hang tag hs code 2@5.5
  /es/blog/hook-and-loop-tape-guide.html       85 展示 @6.3，0 点击
      tipos de velcro 49@6.0 · partes del velcro 7@5.6 · tipos de velcro para ropa 7@7.1

做法：标题把「用户怎么问」放在最前（HS code for … / Tipos de velcro …），
描述里补上他真正想知道的细节（章节号、macho/hembra、能不能缝/粘、洗几次），不编数据。
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent
EN = "en/blog/apparel-trims-hs-code-customs.html"
ES = "es/blog/hook-and-loop-tape-guide.html"

JOBS = [
    (EN,
     "<title>Trims HS Code: Hang Tag Ch.48, Label Ch.58, Bag Ch.39</title>",
     "<title>HS Codes for Garment Trims: Hang Tags, Labels, Bags</title>",
     "EN 标题"),
    (EN,
     'content="Which HS code for hang tags, woven labels, poly bags or paper bags? Chapter 48, 58 and 39 classification, four variables, customs documents checklist.',
     'content="Which HS code for hang tags, woven labels or poly bags: Chapter 48, 58 and 39 classification, the four variables customs asks about, and the documents checklist.',
     "EN 描述"),
    (ES,
     "<title>Tipos de velcro: cuál elegir, materiales y lavado</title>",
     "<title>Tipos de velcro: macho y hembra, para ropa y lavado</title>",
     "ES 标题"),
    (ES,
     'content="Tipos de velcro comparados: estándar, seta, inyectado y autoadhesivo, con resistencia, ruido, ancho y ciclos de lavado. Incluye lista de compra y verificación.',
     'content="Tipos de velcro: cuál es el macho y cuál la hembra, estándar, seta, inyectado y autoadhesivo, cuál se cose y cuál se pega, y qué aguanta el lavado."',
     "ES 描述"),
]


def main():
    ok = 0
    for rel, old, new, label in JOBS:
        p = ROOT / rel
        s = p.read_text(encoding="utf-8")
        n = s.count(old)
        if n != 1:
            print(f"✗ {rel} | {label} | 匹配 {n} 处")
            sys.exit(1)
        p.write_text(s.replace(old, new), encoding="utf-8")
        print(f"✓ {rel:<48} {label}")
        ok += 1
    print(f"\n完成 {ok} 处")


if __name__ == "__main__":
    main()
