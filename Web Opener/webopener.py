import webbrowser
import re
import time
file=open("query.txt","r+")
queries=file.readlines()[0].replace(" ","+")
queryList=queries.split(",")
print(queryList)
for i  in queryList:
    url="https://www.bing.com/search?q="+i+"&qs=HS&pq=he&sc=10-2&cvid=9BAC1630E4BE44FB9AAD73734C6DC144&FORM=CHRDEF&sp=1&lq=0"
    time.sleep(10)
    webbrowser.open(url)
    