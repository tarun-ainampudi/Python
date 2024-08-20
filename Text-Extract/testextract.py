import re

f = open("employee.txt","r+")

nl = f.readlines()

f.close()

sl=[]

for i in nl:
    j=i.replace("\t","")
    j=j.replace("\n",'')
    sl.append(j)

single_line = ""

for i in sl:
    single_line+=i

pt = ">([a-zA-Z-. 0-9]+-[a-zA-Z-. 0-9]+)<"

list=re.findall(pt,single_line)

f = open("list.txt","w")

for i in list:
    f.write(i+"\n")

f.close()

