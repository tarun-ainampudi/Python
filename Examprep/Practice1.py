def prime(anylist):
    count=0
    primelist=[]
    for i in anylist:
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            primelist.append(i)
    return len(primelist)
lenoflist=int(input("Enter the Number of Elements in List:"))
Elements=input(f"Enter the {lenoflist} Elements seperated with space:").split(" ")
Elements=list(int(x) for x in Elements)
numofprime=prime(Elements)
if numofprime%2==0:
    print("The given list is not a lucky list")
else:
    print("The given list is a lucky list")

