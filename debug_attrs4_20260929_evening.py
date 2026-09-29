#!/usr/bin/env python3
# -*- coding: utf-8 -*-
for f in ["blog/_body_measure.html", "blog/_body_shrinkage.html"]:
    print("=====", f)
    lines = open(f, encoding="utf-8", newline="").read().split("\n")
    for k, ln in enumerate(lines[3:11], start=4):
        print("%3d| %s" % (k, repr(ln[:110])))
