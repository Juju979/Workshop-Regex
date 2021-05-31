import re

with open("exo3/exo3.txt", "r") as file:
    txt = file.read()

rgx = re.compile("")
res = rgx.findall(txt)
for i in res:
    print(i, end = '')
print()