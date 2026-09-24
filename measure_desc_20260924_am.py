#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cands = {
 "A1": [
  "Bridal and eveningwear trims guide: satin neck labels, care labels for dry-clean-only and beaded styles, foil hang tags, ribbons and gift box packaging.",
  "Bridal and eveningwear trims guide: satin neck labels, care labels for dry-clean-only and beaded styles, foil hang tags, ribbons and boxed packaging.",
 ],
 "A2": [
  "Switzerland clothing label requirements: fibre content, German and French wording, care symbols, importer as responsible party, GS1 760 barcodes.",
  "Switzerland clothing label requirements: fibre content, German and French wording, care symbols, the importer as responsible party and GS1 760 barcodes.",
 ],
}
for k, v in cands.items():
    for x in v:
        print(k, len(x), x)
