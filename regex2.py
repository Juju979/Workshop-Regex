import re

with open("exo2/exo2.txt", "r") as file:
    txt = file.read()

rgx = re.compile(".* : \{(\s.*=.*\s)*\}")
res = rgx.findall(txt)
for i in res:
    print(i, end = '')
print()