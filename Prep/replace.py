import re
file=open("replace.txt","r+")
txt=file.readlines()
file.close()
mod_txt=[]
for i in txt:
    mod_txt.append(re.sub(" ","‏‏‎ ‎",i))
file=open("rep.txt","w")
for i in mod_txt:
    file.write(i)
file.close
print(mod_txt)