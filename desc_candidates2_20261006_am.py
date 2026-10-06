#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""候选 desc（英文）长度试算 2。"""
C = {
"a": "EAS security tag guide: anti-theft alarms and RFID counting differ, AM hard tags vs RF soft labels vs ink tags, 58 kHz gate matching and factory source tagging.",
"b": "EAS security tag guide: alarms and RFID counting are two systems, AM hard tags vs RF soft labels vs ink tags, 58 kHz gate matching and factory source tagging.",
"c": "EAS security tag guide: why alarms and RFID counting are two systems, hard tags vs soft labels vs ink tags, 58 kHz gate matching and factory source tagging.",
"d": "Garment dye and wash trims guide: how 60–95 °C water, pH, enzymes and tumbling damage hang tags and labels, and the three attachment timings compared.",
"e": "Garment dye and wash trims guide: how 60–95 °C water, pH, enzymes and tumbling damage tags and labels, with three attachment timings and a tolerance table.",
"f": "Garment dye and wash trims guide: how 60–95 °C water, pH, enzymes and tumbling damage tags and labels, the three attachment timings, and a material tolerance table.",
}
for k, v in C.items():
    print("%-3s %3d  %s" % (k, len(v), v[:40]))
