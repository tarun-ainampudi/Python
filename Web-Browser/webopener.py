import webbrowser
import time

file=open(r"C:\Users\tarun\Desktop\Python\Web-Browser\query.txt","r+")
queries=file.readlines()[0].replace(" ","+")
queryList=queries.split(",")
j=1
for i  in queryList:
    url="https://www.bing.com/search?q="+i+"&qs=HS&pq=chat&sc=10-4&cvid=A522D32096FA4E1EA2C4FE7E0C0D660C&FORM=CHRDEF&sp=1&lq=0"
    if(j==1):
        j+=1
    else:
        time.sleep(7)
    webbrowser.open(url, autoraise=False)
    