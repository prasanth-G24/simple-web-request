def findDFA(DFAarg,NFAstate,NFAlist):
    returnList=list()
    x=''
    for i in DFAarg:
        returnList.append(NFAlist[NFAstate.index(i)])
    for i in returnList:
        if i == ['#']:
            continue
        else:
            x+=''.join(i)
    returnList=list(set(x))
    if len(returnList) is 0:
        return '#'
    else:
        returnList.sort()
        return returnList
n=int(input("Enter no. of states:"))
NFAstate=list()
NFAzlist=list()
NFAolist=list()
DFAstate=list()
for i in range(0,n):
    NFAstate.append(input('Enter state '+str(i+1)+":"))
    NFAzlist.append(input(NFAstate[i]+' on input 0:').split())
    NFAolist.append(input(NFAstate[i]+' on input 1:').split())
DFAstate.append(NFAzlist[0])
DFAstate.append(NFAolist[0])
print(NFAstate[0],'\t',''.join(DFAstate[0]),'\t',''.joinDFAstate[1]))
count=0
while True:
    print(''.join(DFAstate[count]),end=' ')
    op1=findDFA(DFAstate[count],NFAstate,NFAzlist)
    op2=findDFA(DFAstate[count],NFAstate,NFAolist)
    print('\t',''.join(op1),'\t',''.join(op2))
    if op1 != '#' and op2 != '#':
        if op1 in DFAstate and op2 in DFAstate:
            break
    if op1 != '#':
        if op1 not in DFAstate:
            DFAstate.append(op1)
    if op2 != '#':
        if op2 not in DFAstate:
            DFAstate.append(op2)
    count+=1
    if count is len(DFAstate):
        break
