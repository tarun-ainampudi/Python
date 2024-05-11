f=open("new.txt","r+")
a=list(f.readlines())
print(a)
print(len(a))
for i in a:
    if i=="\n":
        a.remove(i)
print(a)
f.close()
f=open("new.txt","w+")
for i in a:
    f.write(i)
f.close()
