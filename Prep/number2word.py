import num2word
loop = 1
while loop==1:
    try:
        a=int(input("Enter the number:"))
        if a==0:
            print("Zero")
        else:
            print(num2word.word(a))
    except Exception as b:
        print(f"An Error Occured : {b}")
    finally:
        loop = int(input("Enter 1 to continue 0 to Stop:"))
        if loop != 1:
            break