import requests

LOGIN_URL = "http://172.18.10.10:1000/logout?"
USERNAME = "23BCE9846"
PASSWORD = "Admin@VITAP"

# Simulate a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Referer": LOGIN_URL,  # Some portals require this
    "Origin": "http://172.18.10.10:1000"
}

# Create a session (useful if login requires cookies)
session = requests.Session()
response = session.post(LOGIN_URL, headers=headers)

# Debugging: Print response
print(f"Status Code: {response.status_code}")
print(response.text[:500])  # Print only first 500 chars of response

if response.status_code == 200:
    print("Request successful.")
else:
    print("Request failed. Server might be rejecting direct requests.")
