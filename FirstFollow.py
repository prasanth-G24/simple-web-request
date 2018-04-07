def isTerminal(char):
    if ord(char) >=65 and ord(char) <=90:
        return False
    else:
        return True
def findFirst(symbol,char):
    firstList=list()
    count=0
    for i in symbol:
        if i is char:
            firstList.append(count)
        count+=1
    return firstList
def findFollow(symbol,pos):
    if pos+1 is len(symbol):
        return -1
    else:
        return symbol[pos+1]
first = dict()
follow = dict()
n=int(input("Enter no.of productions:"))
symbol=list()
production=list()
count=1
for i in range(0,n):
    inp=input("Enter production "+str(count)+":").split("->")
    symbol.append(inp[0])
    production.append(inp[1])
    count+=1
for i,j in zip(symbol,production):
    if isTerminal(j[0]):
        if i not in first:
            first[i]=j[0]
        else:
            temp=first[i]
            first[i]=temp+j[0]
    else:
        pos=findFirst(symbol,j[0])
        for x in pos:
            if isTerminal(production[x][0]):
                if i not in first:
                    first[i]=production[x][0]
                else:
                    temp=first[i]
                    first[i]=temp+production[x][0]
                    continue
            else:
                if i not in first:
                    first[i]=production[x][0]
                else:
                    temp=first[i]
                    first[i]=temp+production[x][0]
                    continue
flag=1
for i,j in zip(symbol,production):
    if flag is not 0:
        follow[i]='$'
        flag=0
    for x in j:
        if isTerminal(x):
            continue
        else:
            fol=findFollow(j,j.index(x))
            if fol is -1:
                if x not in follow:
                    follow[x]=follow[i]
                else:
                    temp=follow[i]
                    follow[x]=temp+follow[x]
            elif isTerminal(fol):
                if x not in follow:
                    follow[x]=fol
                else:
                    temp=follow[x]
                    follow[x]=temp+fol
            else:
                fir=first[fol]
                for z in fir:
                    if z is '#':
                        if x not in follow:
                            follow[x]=follow[i]
                        else:
                            print("here")
                            temp=follow[i]
                            follow[x]=temp+follow[x]
                    elif x not in fol:
                        follow[x]=z
                    else:
                        temp=follow[x]
                        follow[x]=temp+z
for i in first:
    for j in first[i]:
        if isTerminal(j):
            continue
        else:
            first[i]=first[i].replace(j,first[j])
for i in follow:
    for j in follow[i]:
        if isTerminal(j):
            continue
        else:
            follow[i]=follow[i].replace(j,first[j])
print("First:")
for i in first:
    j="".join(set(first[i]))
    j=list(j)
    print(i+":",j)
print("Follow:")
for i in follow:
    j="".join(set(follow[i]))
    j=list(j)
    print(i+":",j)
