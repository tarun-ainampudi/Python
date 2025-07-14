import string
# g_str = "aaaaaaaaaaaaaayyiiiizzzzzsssssyyyyyyyyyyddddrrrrrr"
# k=15
# g_str = "aaabbb"
# k = 3
g_str = "bbbbkkkkkkkkkhhhhhwwnnnnnnrrrrrrrvvvjjbbbbbbbbgvww"
k=37
# lowercase_letters = list(string.ascii_lowercase)

vals = []
count = 1

for i in range(len(g_str)):
                
    if i+1 < len(g_str) and g_str[i] == g_str[i+1] :
        count+=1
    else:
        vals.append(count)
        count = 1
print(f"Vals : {vals}")

li = []

# if len(g_str) <=5 and k>20:
li.append(vals) 

for i in li:
    item = i.copy()
    for j in range(len(i)):
        if i[j]-1>=1:
            item[j] = item[j]  - 1
            if item not in li:
                li.append(item)
            item = i.copy()
        else : continue
        
    totl = 1
    for i in vals:
        totl = totl*i

        
print(li)
print(len(li))
print((totl-len(li))%((10**9) + 7))

# else:
#     if (sum([1]*len(vals)) < k):
#         li.append([1]*len(vals))        
#     for i in li:
#         item = i.copy()
#         for j in range(len(i)):
#             if i[j]+1<=vals[j]:
#                 item[j] = item[j]  + 1
#                 if item not in li and sum(item)<k:
#                     li.append(item)
#                 item = i.copy()
#             else : continue
            
#     totl = 1
#     for i in vals:
#         totl = totl*i
#     print(totl)
#     print(li)
#     print((totl-len(li))%((10**9) + 7))
#     cal = totl-len(li)
        
        


