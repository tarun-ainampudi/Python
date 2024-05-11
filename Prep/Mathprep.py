# Enter your code here. Read input from STDIN. Print output to STDOUT
mylist=[]
n=int(input())
for _ in range(n):
    m=int(input())
    n=input()
    mylist.append(n)
updatedlists=[]
for i in mylist:
    varlist=[]
    for j in i.split(' '):
        varlist.append(int(j))
    updatedlists.append(varlist)
def leftarm(list):
    varlist=list.copy()
    templist=[]
    hold=list[0]
    templist.append(hold)
    list.pop(0)
    while len(list)>0:
        if hold>=list[0]:
            templist.append(list[0])
            list.pop(0)
        elif hold>=list[len(list)-1]:
            templist.append(list[len(list)-1])
            list.pop(len(list)-1)
        else:
            break    
    if len(varlist)==len(templist):
        return 1
    else:
        return 0
def rightarm(list):
    varlist=list.copy()
    templist=[]
    hold=list[len(list)-1]
    templist.append(hold)
    list.pop(len(list)-1)
    while len(list)>0:
        if hold>=list[0]:
            templist.append(list[0])
            list.pop(0)
        elif hold>=list[len(list)-1]:
            templist.append(list[len(list)-1])
            list.pop(len(list)-1)
        else:
            break    
    if len(varlist)==len(templist):
        return 1
    else:
        return 0
lastlists=[]
for i in updatedlists:
    j=i.copy()
    templist=[]
    templist.append(leftarm(i))
    templist.append(rightarm(j))
    lastlists.append(templist)
for i in lastlists:
    if any(i):
        print("Yes")
    else:
        print("No")            
