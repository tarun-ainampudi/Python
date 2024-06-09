import requests
name="abhishek"
for i in range(100):
    j=f"{i:02}"
    username=name+j
    url = "https://www.instagram.com/"+username
    response = requests.get(url)
    if "<title>Instagram</title>" in str(response.content) and username!="instagram":
        print(username)
#f=open(name+".txt","a+")
#f.write(name+j+"\n")
#f.close()
         