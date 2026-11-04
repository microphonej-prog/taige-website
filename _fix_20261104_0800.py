import re
p = "blog/_body_nearshore.html"
s = open(p, encoding="utf-8").read()
s2 = s.replace('"> ', '">')
print("fixed:", s.count('"> '))
open(p, "w", encoding="utf-8", newline="").write(s2)
print("remaining:", open(p, encoding="utf-8").read().count('"> <'))
