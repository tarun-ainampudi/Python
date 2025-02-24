#6 digit otps
start=0
end=999999
f_start=f"{start:06}"
f_end=f"{end:06}"
f=open(f"{f_start}to{f_end}.txt","w+")
for i in range(start,end+1,1):
    f.write(f"{i:06}\n")
    