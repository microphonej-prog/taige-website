import re
t = open("ko/blog/conflict-minerals-trims-guide.html", encoding="utf-8").read()
body = t.split('class="article-body"',1)[1].split("</section>",1)[0]
for m in re.finditer(r"[\u4e00-\u9fff]", body):
    print("位置", m.start(), ":", body[max(0,m.start()-60):m.start()+60].replace("\n"," "))
