import typer 
import string
import os
import webbrowser
import time
import pyautogui


bpc = typer.Typer()

@bpc.command()
def tabs(ntabs : int, tgap : int, index  : int):
    gen_file()
    with open(r"./query.txt","r+") as f:
        query_list = f.read().split(",")
        query_list.remove("")
    j=1
    for i  in range(index , index+ntabs):
        print(j)
        url="https://www.bing.com/search?q="+query_list[i%len(query_list)]+"&PC=U316&FORM=CHROMN"
        webbrowser.open(url)
        time.sleep(tgap)
        j+=1
        pyautogui.hotkey('ctrl','w')
    
@bpc.command()
def gen_file():
    if os.path.exists(r"./query.txt"):
        return
    else:
        letters_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)
        with open(r"./query.txt","w+") as f:
             for i in letters_list:
                 for j in letters_list:
                     string1 = i+j+","
                     f.write(string1)
        print("File Generated")

@bpc.command()
def rm_file():
    if os.path.exists(r"./query.txt"):
        os.remove(r"./query.txt")
    else:
        print("File doesn't Exist")
    
    
        
bpc()
