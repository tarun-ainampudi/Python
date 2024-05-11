with open("Demo.txt","r+") as file:
    file.write("TArun")
    print(file.tell())
    file.seek(0)
    print(file.read())