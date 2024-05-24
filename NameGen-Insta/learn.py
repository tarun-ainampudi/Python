import requests
name="tarun"
for i in range(100):
    j=f"{i:02}"
    username=j
    url = "https://www.instagram.com/"+username
    response = requests.get(url)
    if "<title>Instagram</title>" in str(response.content) and username!="instagram":
          f=open(name+".txt","a+")
          f.write(name+j+"\n")
          f.close()
