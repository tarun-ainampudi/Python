import webbrowser
import time
import pyautogui

file=open(r"C:\Users\tarun\Desktop\Python\Web-Browser\query.txt","r+")
queries=file.readlines()[0].replace(" ","+")
queryList=queries.split(",")
j=1
for i  in queryList:
    print(j)
    url="https://www.bing.com/search?q="+i+"&PC=U316&FORM=CHROMN"
    webbrowser.open(url, autoraise=False)
    time.sleep(12)
    j+=1
    pyautogui.hotkey('ctrl','w')
    
    