a="11 33".split(" ")
length=int(a[0])
width=int(a[1])
b="---"
c='.|.'
e=[]
n=length//2
k=1
for i in range(n):
    d=b*(n-i)+c*(k)+b*(n-i)
    e.append(d)
    k=k+2
o=width-7
o=o//2
for i in range(len(e)):
    print(e[i])
print("-"*o+"WELCOME"+"-"*o)
for i in range(len(e)):
    print(e[len(e)-i-1])
