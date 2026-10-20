#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, ".")
from daily_meta_20261020_0800 import ARTICLES as OLD
from daily_meta_20261020_1400 import ARTICLES as NEW

print("上一批次 desc 长度基线：")
for a in OLD:
    print("  %-44s zh=%d en=%d ja=%d ko=%d fr=%d es=%d" % (a["slug"], len(a["desc_zh"]), len(a["desc_en"]),
          len(a["desc_ja"]), len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))

cands = [
 "Scented hang tags: how microcapsule fragrance releases, full coating versus a scent patch, scent families by garment type, longevity tests and allergen compliance.",
 "Scented hang tags: how microcapsule fragrance releases, full coating versus a scent patch, matching scent to garment type, and how to measure longevity.",
 "Scented hang tags: microcapsule release, full versus spot coating, scent families per garment type, longevity testing and allergen compliance for export.",
 "Scented hang tags explained: microcapsule release, coating versus scent patch, scent families by garment type, measured longevity and allergen rules.",
]
print("\n候选英文 desc：")
for c in cands:
    print("  %d  %s" % (len(c), c))
