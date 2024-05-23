import requests
name="tarun"
for i in range(100):
    j=f"{i:02}"
    f=open(name+".txt","a+")
    f.write(name+j+"\n")
    f.close()
file=open(name+".txt","r")
lines=file.readlines()
file.close()
for i in lines:
    username=i
    url = "https://www.instagram.com/"+username
    response = requests.get(url)
    if "<title>Instagram</title>" in str(response.content) and username!="instagram":
           f=open(name+"-available.txt","a+")
           f.write(username)
           f.close()
