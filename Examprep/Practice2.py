def reversing(accno,revnum):
    if accno>0:
        step=accno%10
        revnum=revnum*10+step
        accno//=10
    else:
        return revnum
    return reversing(accno,revnum)
accno=int(input("Enter the Number:"))
revnum=0
print(f'Reversed Number is {reversing(accno,revnum)}')