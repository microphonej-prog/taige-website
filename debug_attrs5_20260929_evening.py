#!/usr/bin/env python3
# -*- coding: utf-8 -*-
for f in ["blog/_body_measure.html", "blog/_body_shrinkage.html"]:
    lines = open(f, encoding="utf-8", newline="").read().split("\n")
    ln = lines[3]
    print("=====", f, "len=", len(ln))
    print("quote count:", ln.count('"'), " gt count:", ln.count(">"), " lt count:", ln.count("<"))
    gt = [k for k, c in enumerate(ln) if c == ">"]
    print("gt positions:", gt, "tail repr:", repr(ln[-30:]))
    if gt:
        print("around first gt:", repr(ln[max(0, gt[0] - 40):gt[0] + 10]))
