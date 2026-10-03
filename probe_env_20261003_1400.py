#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
try:
    import opencc
    print("opencc OK", opencc.__file__)
except Exception as e:
    print("opencc MISSING:", e)
print("python", sys.version)
