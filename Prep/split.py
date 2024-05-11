integers=input("Enter the Numbers seperated with space:").split(" ")
integers=list(int(i) for i in integers)
for i in integers:
    print(i,type(i))