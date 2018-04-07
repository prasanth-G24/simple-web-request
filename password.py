import sys
inp=input()
if len(inp)<6:
    print(6-len(inp))
    sys.exit()
special=["!","@","#","$","%","^","&","*","(",")","-","+"]
lc=0
uc=0
sc=0
num=0
total=0
for i in inp:
    if ord(i) >= 65 and ord(i) <= 91:
        uc=1
        continue
    if ord(i) >= 97 and ord(i) <= 122:
        lc=1
        continue
    if i in special:
        sc=1
        continue
    if int(i) >= 0 and int(i) <= 9:
        num=1
        continue
if lc is not 1:
    total+=1
if uc is not 1:
    total+=1
if sc is not 1:
    total+=1
if num is not 1:
    total+=1
print(total)
