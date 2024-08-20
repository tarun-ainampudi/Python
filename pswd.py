string_list=["Indra@","Litq@","Psycho@","Mbia@"]
symbol_list=["$","₹"]
numbers_list=['1','2','3','4','6','0']
pswd=''

for i in string_list:
     pswd=i
     for k in numbers_list:
          if len(pswd)<=11:
                pswd+=k
                if(len(pswd)>8):
                     print(pswd)
                     for j in symbol_list:
                          print(pswd+j)
                    


