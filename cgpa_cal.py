import re
dic =  {
    's':10,
    'a':9,
    'b':8,
    'c':7,
    'd':6,
    'e':5
}
string = input("Enter String (Ex:4a 4a 4a 4a 3b 3c ....) : ").lower()
#print(dic['a'])==9
grade_list = string.split()
gpa_numerator = 0
gpa_denominator = 0
for i in grade_list:
    gpa_denominator+=int(i[0])
    gpa_numerator+=(int(i[0])*dic[i[-1]])
gpa = gpa_numerator/gpa_denominator
print(f"No.of Credits : {gpa_denominator}")
print(f"Your GPA is : {gpa:.2f}")
input()