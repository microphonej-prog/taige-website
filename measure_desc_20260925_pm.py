#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-25 下午批次 desc 长度体检"""
CANDS = {
    "A_en": [
        "Footwear and bag trim labels: EU 94/11/EC marking for upper, lining and sole, tongue woven labels, insole marks, leather patches and box labels.",
        "Footwear and bag trim labels: EU 94/11/EC material marking, tongue woven labels, insole marks, leather patches and box labels, with a checklist.",
        "Footwear and bag trim labels: EU 94/11/EC material marking for upper, lining and sole, plus tongue woven labels, insole marks and box labels.",
    ],
    "B_en": [
        "Copyright and trademark clearance for trims: documents needed by own brands, contract manufacturing and licensed IP, font and image licences and a checklist.",
        "Copyright and trademark clearance for trims: what own brands, contract manufacturing and licensed IP need, plus font, stock-image and AI-art limits.",
        "Copyright and trademark clearance for trims: what own brands, contract manufacturing and licensed IP each need, plus font and image licences.",
    ],
    "A_fr": [
        "Étiquettes pour chaussures et sacs : marquage des matières selon la directive 94/11/EC, tissés de languette, premières, patchs cuir et étiquettes de boîte.",
        "Étiquettes pour chaussures et sacs : marquage des matières (directive 94/11/EC), tissés de languette, premières, patchs cuir et étiquettes de boîte.",
    ],
    "A_es": [
        "Etiquetas para calzado y bolsos: marcado de materiales según la Directiva 94/11/EC, tejidas de lengüeta, plantillas, parches de piel y cajas.",
        "Etiquetas para calzado y bolsos: marcado de materiales (Directiva 94/11/EC), tejidas de lengüeta, plantillas, parches de piel y etiquetas de caja.",
    ],
    "B_fr": [
        "Droits d'auteur et marques pour l'impression d'accessoires : documents exigés par situation, licences de polices, images IA et contrôle avant échantillon.",
        "Droits d'auteur et marques pour l'impression d'accessoires : documents exigés, licences de polices et d'images, images IA et contrôle avant échantillon.",
    ],
    "B_es": [
        "Derechos de autor y marcas al imprimir accesorios: documentos según cada situación, licencias de fuentes, imágenes IA y control previo a la muestra.",
        "Derechos de autor y marcas al imprimir accesorios: documentos exigidos, licencias de fuentes e imágenes, imágenes IA y control previo a la muestra.",
    ],
}
for k, lst in CANDS.items():
    for i, s in enumerate(lst, 1):
        print("%s#%d  len=%d" % (k, i, len(s)))
