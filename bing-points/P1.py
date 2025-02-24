import string

letters_list = list()
letters_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)
print(letters_list)

gen_list = list()

file  = open(r"./query1.txt","w+")
size = 200

for i in letters_list:
    for j in letters_list:
        string = i+j+","
        file.write(string)
file.close()

f = open(r"./query1.txt","r+")
list_gen = f.read().split(",")
list_gen.remove("")
print(list_gen)



