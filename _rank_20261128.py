#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第二组：推排名（2026-11-28）

两篇都是「展示高、但排 20–30 名」，改标题只能动 CTR、动不了排名 —— 所以这一组的做法是：
1) 标题/描述把用户原词前置（CTR）；
2) 正文开头插一段「直接回答」callout（相关性 + 争取 featured snippet）；
3) 结尾补 3 条 FAQ（h3 形式，不加 schema，避免与原 FAQ 页主题冲突），把「metal tag maintenance / lifespan / when to use」
   和「essai d'emballage / test d'emballage vibration」这些真实长尾收进正文。

依据：GSC page+query 90 天（--pairs）
  en/blog/metal-labels-guide.html
    durable materials for tags 208 展示 @25.9 / metal tag maintenance 37 @36.1 / metal hang tags 12 @17.7 / metallum label explanation 16 @9.5
  fr/blog/garment-packaging-transit-testing.html
    essai d'emballage 147 @30.2 / test emballage vibration 52 @20.9 / test d'emballage 13 @66.8

幂等：每处替换前校验旧串唯一存在。
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent

EN = "en/blog/metal-labels-guide.html"
FR = "fr/blog/garment-packaging-transit-testing.html"

JOBS = [
    # ---------- EN 标题/描述 ----------
    (EN,
     "<title>Metal Hang Tags &amp; Labels: Materials, Care &amp; MOQ</title>",
     "<title>Durable Metal Hang Tags: Materials, Lifespan &amp; Care</title>",
     "EN 标题"),
    (EN,
     'content="Metal hang tags and labels: stainless steel, brass, aluminum and zinc alloy, plating, brushing and etching options, care steps, MOQ and QC checkpoints.',
     'content="Stainless steel vs brass vs aluminium vs zinc alloy for metal hang tags: corrosion and wear, plating and etching options, care steps, MOQ and QC checkpoints.',
     "EN 描述"),

    # ---------- EN 开头「直接回答」 ----------
    (EN,
     '      <p>This guide explains the materials, surface finishes, attachment methods and compliance points of metal labels and hang tags, so brands can lock down the key parameters before ordering.</p>\n',
     '      <p>This guide explains the materials, surface finishes, attachment methods and compliance points of metal labels and hang tags, so brands can lock down the key parameters before ordering.</p>\n\n'
     '      <p class="callout"><strong>Short answer — which metal is the most durable for tags?</strong> '
     'Stainless steel, by a wide margin: it resists corrosion, keeps its edge under abrasion and can be brushed or mirror-polished, which is why it is the default for wash-care tags and nameplates on denim and outerwear. '
     'Brass takes the deepest etch and the warmest tone, so it is chosen for brand blocks rather than wear resistance. Aluminium is the lightest and cheapest option and is fine for cosmetic tags that never see a wash cycle. '
     'Zinc alloy is a plating base — good for fine relief detail, weakest under abrasion. If the tag will be washed, tumbled or worn against skin daily, specify stainless; if it only has to look right in a box, aluminium or plated zinc is enough.</p>\n',
     "EN 直接回答"),

    # ---------- EN 结尾 FAQ（补真实长尾） ----------
    (EN,
     '      <h2>Related Articles</h2>',
     '      <h2>6. Durability, Lifespan and Maintenance</h2>\n'
     '      <h3>How long does a metal hang tag last?</h3>\n'
     '      <p>On a garment that is worn and washed, a stainless steel tag holds its finish for years; an aluminium tag with a printed or anodised face usually shows edge wear within a season of daily wear. The tag itself rarely fails — the connection does: split rings rust, cords fray, rivets loosen. Specify the attachment for the same lifespan as the tag.</p>\n'
     '      <h3>What maintenance does a metal tag need?</h3>\n'
     '      <p>Almost none, and that is the selling point. Plated zinc and brass will dull with skin oils; a dry microfibre wipe restores the shine. Avoid abrasive polish on etched faces — it fills the etch and flattens the logo. For care labels, the practical test is the wash cycle the garment is sold with: if the plating blisters or the print lifts after five cycles, the finish is wrong for that price point.</p>\n'
     '      <h3>When should a brand use metal instead of paper or woven?</h3>\n'
     '      <p>Metal pays for itself where the tag is handled repeatedly or has to survive the product: denim, leather goods, bag hardware, and any tag that doubles as a zip pull or charm. On a light jersey tee sold through e-commerce, a paper tag carries the same information at a fraction of the weight and freight cost.</p>\n\n'
     '      <h2>Related Articles</h2>',
     "EN 补 FAQ 段落"),

    # ---------- FR 标题/描述 ----------
    (FR,
     "<title>Tests de transport : ASTM D4169, chute et empilage</title>",
     "<title>Essais d&#x27;emballage : chute, vibration, empilage (ASTM D4169)</title>",
     "FR 标题"),
    (FR,
     'content="Ce qu&#x27;est un test de transport : paramètres ASTM D4169 (chute, empilage, vibration, humidité), correctifs des cinq avaries fréquentes et autotest en cinq étapes.',
     'content="Un essai d&#x27;emballage par avarie : chute libre, empilage, vibration aléatoire, humidité. Paramètres ASTM D4169, cinq avaries fréquentes et autotest en 5 étapes.',
     "FR 描述"),

    # ---------- FR 开头「快速回答」 ----------
    (FR,
     "      <h2>1. Pourquoi le faire : l&#x27;avarie coûte bien plus cher que l&#x27;emballage</h2>",
     "      <p class=\"callout\"><strong>Réponse rapide — quel essai d&#x27;emballage pour quel risque ?</strong> "
     "Un essai d&#x27;emballage ne se choisit pas par habitude mais par avarie à éviter : chute libre pour la manutention et le dernier kilomètre, empilage pour le stockage en entrepôt et en conteneur, vibration aléatoire pour le transport routier et ferroviaire, chambre climatique pour le maritime et les longs séjours. Le test d&#x27;emballage vibration est celui qui révèle le plus de défauts invisibles — soudures de sac qui fatiguent, agrafes qui migrent, étiquettes qui se décollent. La séquence ASTM D4169 (cycle DC 13) enchaîne ces contraintes dans l&#x27;ordre réel du voyage ; pour un programme vêtement, un autotest interne en cinq étapes couvre déjà l&#x27;essentiel du risque avant de payer un laboratoire.</p>\n\n"
     "      <h2>1. Pourquoi le faire : l&#x27;avarie coûte bien plus cher que l&#x27;emballage</h2>",
     "FR 快速回答"),
]


def main():
    changed, failed = {}, []
    for rel, old, new, label in JOBS:
        p = ROOT / rel
        s = p.read_text(encoding="utf-8")
        n = s.count(old)
        if n != 1:
            failed.append((rel, label, f"匹配 {n} 处")); continue
        p.write_text(s.replace(old, new), encoding="utf-8")
        changed[rel] = changed.get(rel, 0) + 1
        print(f"✓ {rel:<48} {label}")
    print()
    for rel, n in changed.items():
        print(f"  {rel} → {n} 处")
    if failed:
        print("\n未改动：")
        for rel, label, why in failed:
            print(f"  ✗ {rel} | {label} | {why}")
        sys.exit(1)


if __name__ == "__main__":
    main()
