
import requests

url = 'https://172.18.10.10:7799'
response = requests.get(url,verify=r"C:\Users\abhi1\Downloads\fortinet-ca2.crt", headers={'Host': '172.18.10.10:1000'})

if response.status_code == 200:
    print("Successfully opened the website.")
else:
    print(f"Failed to open the website. Status code: {response.status_code}")
