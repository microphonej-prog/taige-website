#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, re
ROOT = os.path.dirname(os.path.abspath(__file__)); os.chdir(ROOT)
for f in ["blog/apparel-trims-hs-code-customs.html",
          "blog/clothing-origin-marking-guide.html",
          "blog/garment-trims-sample-shipping-guide.html",
          "blog/garment-trims-carton-loading-guide.html"]:
    s = open(f, encoding="utf-8").read()
    hs = re.findall(r'<h[12][^>]*data-zh="([^"]{0,80})"', s)
    print("### " + os.path.basename(f))
    for h in hs:
        print("   · " + h)
    print()
