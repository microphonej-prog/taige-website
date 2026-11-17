import io
for f in ["blog/hang-tag-back-printing-guide.html","blog/apparel-trims-chargeback-guide.html","body_20261117_2000_a.py","body_20261117_2000_b.py"]:
    s = io.open(f, encoding="utf-8").read()
    n = s.count("loi japonaise sur l&#x27;étiquetage") + s.count("loi japonaise sur l'étiquetage")
    s = s.replace("loi japonaise sur l&#x27;étiquetage", "loi japonaise sur les mentions obligatoires")
    s = s.replace("loi japonaise sur l'étiquetage", "loi japonaise sur les mentions obligatoires")
    io.open(f,"w",encoding="utf-8",newline="").write(s)
    print(f, n)
