a=list(input())
for i in range(1,len(a)):
    if len(a) < 2:
        break
    if a[i] is a[i-1]:
        del a[i]
        del a[i-1]
        i=1
    else:
        continue
if len(a) is 0:
    print("Empty String")
else:
    print(''.join(a))
