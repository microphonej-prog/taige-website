#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, re
ROOT = os.path.dirname(os.path.abspath(__file__)); os.chdir(ROOT)
for f in ["blog/trims-carbon-footprint-guide.html",
          "blog/eu-digital-product-passport-trims.html",
          "blog/garment-trims-freight-mode-guide.html",
          "blog/apparel-trims-payment-terms-guide.html",
          "blog/garment-trims-sourcing-guide.html",
          "blog/trim-supply-continuity-guide.html"]:
    s = open(f, encoding="utf-8").read()
    hs = re.findall(r'<h[12][^>]*data-zh="([^"]{0,80})"', s)
    print("### " + os.path.basename(f))
    for h in hs:
        print("   · " + h)
    print()
