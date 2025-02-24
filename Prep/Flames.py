def nametolist(string):
	n=[]
	for i in string:
		n.append(i)
	return n
def removeempty(list):
	n=[]
	for i in list:
		if i!=" ":
			n.append(i)
	return n
def sortlist(list,num):
	newlist=list[num:]+list[:num]
	return newlist
a=input("Enter the Name:").upper()
b=input("Enter the other Name:").upper()
a=nametolist(a)
a=removeempty(a)
b=nametolist(b)
b=removeempty(b)
c=b.copy()
for i in a:
	if i in b:
		b.remove(i)
for i in c:
	if i in a:
		a.remove(i)
key=len(list(a+b))
k=0
d=" Friends lovers affectionate marriage enemies soulmates".upper().split()
while len(d)!=1:
	length=key-1
	e=0
	while length>=len(d):
		length=length-len(d)
	e=d[length]
	k=length
	d.remove(e)
	d=sortlist(d,k)
print(d)

			
			
			